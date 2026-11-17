#!/usr/bin/env python3
"""Telegram Ads autopilot for WhatIfStack (stdlib only).

Commands (run from repo root):
  report   pull ads + daily stats via the Telegram Ads API, write data/daily.csv,
           data/ads.json and report.md (metrics + recommendations)
  guard    pause losing ads (rules in config.json -> guard). Pausing never spends money.
  apply    execute owner-approved actions from approved.json (create ad, add budget, cpm,
           unpause, pause). Every action needs "approved": "<date> <who>", runs once
           (idempotency key = action id), and the total new spend per ISO week is capped by
           config.json -> weekly_spend_cap (0 = only explicitly approved actions).
  autopilot  optional: add budget to winning ads inside weekly_spend_cap
           (config.json -> autopilot.enabled must be true; set by the owner).
  check    check candidate channels (data/candidates.txt) on public t.me/s/ pages and
           merge into channels.csv

Token: env TG_ADS_TOKEN (GitHub secret). Never commit the token.
API docs: https://ads.telegram.org/docs/api
"""
import csv, datetime as dt, json, os, re, statistics, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ads/telegram
DATA = os.path.join(ROOT, 'data')
API = 'https://promoteapi.telegram.org/'
NOW = dt.datetime.now(dt.timezone.utc)


def load(path, default):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


CFG = load(os.path.join(ROOT, 'config.json'), {})


def call(method, idem=None, **params):
    token = os.environ.get('TG_ADS_TOKEN')
    if not token:
        sys.exit('TG_ADS_TOKEN is not set: add it as a GitHub secret (owner only).')
    body = json.dumps({k: v for k, v in params.items() if v is not None}).encode()
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    if idem:
        headers['Idempotency-Key'] = idem
    req = urllib.request.Request(API + method, data=body, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                res = json.loads(r.read().decode())
            break
        except Exception as e:  # network hiccup
            if attempt == 2:
                raise
            time.sleep(3 * (attempt + 1))
    if not res.get('ok'):
        raise RuntimeError(f'{method}: {res.get("error")}')
    return res['result']


# ---------------------------------------------------------------- metrics
def metrics(ad):
    v, c, a, s = ad.get('views', 0), ad.get('clicks', 0) or 0, ad.get('actions', 0) or 0, ad.get('spent_budget', 0) or 0
    return {
        'ctr': round(100 * c / v, 2) if v else None,
        'cvr': round(100 * a / c, 1) if c else None,
        'cpc': round(s / c, 3) if c else None,
        'cpa': round(s / a, 3) if a else None,
    }


def public_subs(username):
    """Subscriber count from the public t.me/s page (no account involved)."""
    try:
        html = urllib.request.urlopen(f'https://t.me/s/{username}', timeout=20).read().decode('utf-8', 'replace')
        m = re.search(r'counter_value">([\d.,]+[KM]?)</span>\s*<span class="counter_type">subscribers', html)
        if not m:
            return None
        v = m.group(1).replace(',', '.')
        mul = 1000 if v.endswith('K') else 1_000_000 if v.endswith('M') else 1
        return int(float(v.rstrip('KM')) * mul)
    except Exception:
        return None


def cmd_report():
    ads = call('getAdsList', limit=100, return_target=True)['ads']
    acc = call('getCurrentAccount')
    save(os.path.join(DATA, 'ads.json'), ads)
    # daily stats per ad
    rows = []
    for ad in ads:
        frm = int(ad['created_date']) // 86400 * 86400
        st = call('getAdStats', ad_id=ad['ad_id'], from_time=frm, to_time=int(NOW.timestamp()) + 86400, interval=86400)
        for it in st:
            rows.append({'date': dt.datetime.fromtimestamp(it['from_time'], dt.timezone.utc).date().isoformat(),
                         'ad_id': ad['ad_id'], 'title': ad['title'], 'views': it.get('views', 0),
                         'clicks': it.get('clicks', 0), 'actions': it.get('actions', 0),
                         'spent': it.get('spent_budget', 0)})
        time.sleep(0.3)
    with open(os.path.join(DATA, 'daily.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['date', 'ad_id', 'title', 'views', 'clicks', 'actions', 'spent'])
        w.writeheader(); w.writerows(rows)
    # channel growth (public)
    ch = CFG.get('promoted_channel', 'WhatIfStack')
    subs = public_subs(ch)
    growth = load(os.path.join(DATA, 'subs.json'), {})
    if subs:
        growth[NOW.date().isoformat()] = subs
        save(os.path.join(DATA, 'subs.json'), growth)

    # report
    cpas = [metrics(a)['cpa'] for a in ads if metrics(a)['cpa']]
    med_cpa = statistics.median(cpas) if cpas else None
    total_spent = sum(a.get('spent_budget', 0) or 0 for a in ads)
    total_act = sum(a.get('actions', 0) or 0 for a in ads)
    L = [f'# Telegram Ads — звіт {NOW:%Y-%m-%d %H:%M} UTC', '',
         f'Баланс акаунта: {acc.get("remaining_budget")} {acc.get("currency")} · витрачено всього: {round(total_spent, 2)} · '
         f'дій (підписок): {total_act} · середня ціна підписки: {round(total_spent / total_act, 3) if total_act else "—"}',
         f'Підписники @{ch}: {subs if subs else "—"}', '',
         '| ad | назва | статус | покази | кліки | CTR% | підписки | CVR% | витрачено | залишок | CPA | рішення |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for a in sorted(ads, key=lambda a: (metrics(a)['cpa'] or 1e9)):
        m = metrics(a)
        L.append(f"| {a['ad_id']} | {a['title']} | {a.get('status')}{' (pause)' if a.get('is_paused') else ''} | "
                 f"{a.get('views', 0)} | {a.get('clicks', 0)} | {m['ctr'] or '—'} | {a.get('actions', 0)} | {m['cvr'] or '—'} | "
                 f"{round(a.get('spent_budget', 0) or 0, 2)} | {round(a.get('remaining_budget', 0) or 0, 2)} | {m['cpa'] or '—'} | "
                 f"{decide(a, med_cpa)[1]} |")
    L += ['', 'Правила: див. config.json → guard / autopilot. Рішення «пауза» guard виконує сам; '
          'усе, що збільшує витрати, — тільки через approved.json або автопілот у межах тижневого ліміту.']
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


def decide(ad, med_cpa):
    g = CFG.get('guard', {})
    m = metrics(ad)
    v, s, a = ad.get('views', 0), ad.get('spent_budget', 0) or 0, ad.get('actions', 0) or 0
    if ad.get('is_paused') or ad.get('status') not in ('active',):
        return None, '—'
    if v >= g.get('min_views_ctr', 3000) and (m['ctr'] or 0) < g.get('min_ctr', 0.3):
        return 'pause', f"пауза: CTR {m['ctr']}% < {g.get('min_ctr', 0.3)}%"
    if not ad.get('action_type'):
        return None, 'підписки не трекаються (action_type порожній) — оцінка лише за CTR/CPC'
    if s >= g.get('min_spent_no_action', 1.5) and a == 0:
        return 'pause', f'пауза: витрачено {round(s, 2)} без підписок'
    if med_cpa and m['cpa'] and s >= g.get('min_spent_cpa', 1.5) and m['cpa'] > g.get('cpa_vs_median', 2.0) * med_cpa:
        return 'pause', f"пауза: CPA {m['cpa']} > {g.get('cpa_vs_median', 2.0)}× медіани {round(med_cpa, 3)}"
    if med_cpa and m['cpa'] and m['cpa'] <= med_cpa and a >= g.get('min_actions_winner', 5):
        return 'scale', f"переможець: CPA {m['cpa']} ≤ медіани — масштабувати / розбити на підгрупи"
    return None, 'збираємо дані'


def cmd_guard():
    if not CFG.get('guard', {}).get('enabled', True):
        print('guard disabled'); return
    ads = call('getAdsList', limit=100)['ads']
    cpas = [metrics(a)['cpa'] for a in ads if metrics(a)['cpa']]
    med = statistics.median(cpas) if cpas else None
    log = []
    for a in ads:
        act, why = decide(a, med)
        if act == 'pause':
            call('editAd', ad_id=a['ad_id'], is_paused=True)
            log.append(f"{NOW:%Y-%m-%d} guard: paused ad {a['ad_id']} «{a['title']}» — {why}")
    append_log(log)
    print('\n'.join(log) or 'guard: nothing to pause')


def week_key(d):
    y, w, _ = d.isocalendar()
    return f'{y}-W{w:02d}'


def spend_this_week(state):
    return sum(x['amount'] for x in state.get('spend', []) if x['week'] == week_key(NOW.date()))


def cmd_apply():
    path = os.path.join(ROOT, 'approved.json')
    actions = load(path, [])
    state = load(os.path.join(DATA, 'state.json'), {'spend': []})
    cap = float(CFG.get('weekly_spend_cap', 0))
    log = []
    for act in actions:
        if act.get('done') or not act.get('approved'):
            continue
        amount = float(act.get('budget', act.get('amount', 0)) or 0)
        if cap and spend_this_week(state) + amount > cap:
            log.append(f"{NOW:%Y-%m-%d} apply: SKIP {act['id']} — тижневий ліміт {cap} буде перевищено")
            continue
        t = act['type']
        if t == 'create':
            target = {'type': 'channels'}
            if act.get('channels'):
                target['channel_ids'] = ['@' + c.lstrip('@') for c in act['channels']]
            if act.get('topic_ids'):
                target['topic_ids'] = act['topic_ids']
            if act.get('languages'):
                target['language_codes'] = act['languages']
            target['exclude_channel_ids'] = ['@' + CFG.get('promoted_channel', 'WhatIfStack')]
            res = call('createAd', idem=act['id'], title=act['title'], text=act['text'],
                       promote_url=act.get('promote_url', 'https://t.me/' + CFG.get('promoted_channel', 'WhatIfStack')),
                       cpm=act['cpm'], placement='channel_post', target=target,
                       impression_frequency=act.get('frequency', 1), initial_budget=amount,
                       is_paused=False)
            act['ad_id'] = res.get('ad_id')
        elif t == 'increase_budget':
            call('increaseAdBudget', idem=act['id'], ad_id=act['ad_id'], amount=amount)
        elif t == 'cpm':
            call('editAd', ad_id=act['ad_id'], cpm=act['cpm'])
        elif t == 'unpause':
            call('editAd', ad_id=act['ad_id'], is_paused=False)
        elif t == 'pause':
            call('editAd', ad_id=act['ad_id'], is_paused=True)
        else:
            log.append(f"apply: unknown type {t}"); continue
        act['done'] = NOW.isoformat(timespec='minutes')
        if amount:
            state['spend'].append({'week': week_key(NOW.date()), 'amount': amount, 'id': act['id']})
        log.append(f"{NOW:%Y-%m-%d} apply: {t} {act['id']} ({act.get('approved')}) ok")
    save(path, actions)
    save(os.path.join(DATA, 'state.json'), state)
    append_log(log)
    print('\n'.join(log) or 'apply: nothing to do')


def cmd_autopilot():
    ap = CFG.get('autopilot', {})
    cap = float(CFG.get('weekly_spend_cap', 0))
    if not ap.get('enabled') or cap <= 0:
        print('autopilot off (owner sets autopilot.enabled + weekly_spend_cap)'); return
    state = load(os.path.join(DATA, 'state.json'), {'spend': []})
    ads = call('getAdsList', limit=100)['ads']
    cpas = [metrics(a)['cpa'] for a in ads if metrics(a)['cpa']]
    med = statistics.median(cpas) if cpas else None
    target = ap.get('target_cpa') or med
    step = float(ap.get('step', 3))
    log = []
    for a in sorted(ads, key=lambda a: metrics(a)['cpa'] or 1e9):
        m = metrics(a)
        if a.get('is_paused') or a.get('status') != 'active' or not m['cpa'] or not target:
            continue
        if m['cpa'] <= target and (a.get('actions') or 0) >= ap.get('min_actions', 5) and (a.get('remaining_budget') or 0) < ap.get('refill_below', 1.0):
            if spend_this_week(state) + step > cap:
                log.append(f"{NOW:%Y-%m-%d} autopilot: ліміт тижня {cap} вичерпано"); break
            key = f"ap-{a['ad_id']}-{NOW:%Y%m%d}"
            call('increaseAdBudget', idem=key, ad_id=a['ad_id'], amount=step)
            state['spend'].append({'week': week_key(NOW.date()), 'amount': step, 'id': key})
            log.append(f"{NOW:%Y-%m-%d} autopilot: +{step} до ad {a['ad_id']} «{a['title']}» (CPA {m['cpa']} ≤ ціль {round(target, 3)})")
    save(os.path.join(DATA, 'state.json'), state)
    append_log(log)
    print('\n'.join(log) or 'autopilot: nothing to refill')


# ---------------------------------------------------------------- channel checks (public pages only)
SCAM = re.compile(r'zooab|movanft|daily (return|income|profit)|vip (investment|plan)|invite code|three-tier|team reward|referral (reward|rebate)|withdraw', re.I)


def parse_views(v):
    v = v.replace(',', '.')
    mul = 1000 if v.endswith('K') else 1_000_000 if v.endswith('M') else 1
    try:
        return float(v.rstrip('KM')) * mul
    except ValueError:
        return 0


def check_channel(u):
    html = urllib.request.urlopen(f'https://t.me/s/{u}', timeout=20).read().decode('utf-8', 'replace')
    subs = re.search(r'counter_value">([\d.,]+[KM]?)</span>\s*<span class="counter_type">subscribers', html)
    subs = int(parse_views(subs.group(1))) if subs else 0
    views = sorted(parse_views(x) for x in re.findall(r'tgme_widget_message_views">([\d.,]+[KM]?)<', html))
    dates = sorted(re.findall(r'<time datetime="([^"]+)"', html))
    text = ' '.join(re.sub(r'<[^>]+>', ' ', t) for t in re.findall(r'tgme_widget_message_text[^>]*>(.*?)</div>', html, re.S))
    lat, cyr = len(re.findall(r'[A-Za-z]', text)), len(re.findall(r'[Ѐ-ӿ]', text))
    med = views[len(views) // 2] if views else 0
    last = dates[-1] if dates else None
    days = (NOW - dt.datetime.fromisoformat(last)).days if last else 999
    return {'username': u, 'link': f'https://t.me/{u}', 'subs': subs, 'median_views': int(med),
            'ER_%': round(100 * med / subs) if subs else 0, 'last_post_days': days,
            'lang': 'en' if lat > 2 * cyr else ('ru/uk' if cyr > lat else 'other'),
            'scam_signals': ','.join(sorted({m.group(0).lower() for m in SCAM.finditer(text)}))}


def cmd_check():
    cand_path = os.path.join(DATA, 'candidates.txt')
    if not os.path.exists(cand_path):
        print('no data/candidates.txt'); return
    base_path = os.path.join(ROOT, 'channels.csv')
    with open(base_path, encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    known = {r['username'].lower(): r for r in rows}
    cands = [l.strip().lstrip('@') for l in open(cand_path, encoding='utf-8') if l.strip()]
    added = 0
    for u in cands:
        try:
            c = check_channel(u)
        except Exception as e:
            print('skip', u, e); continue
        reasons = []
        if c['lang'] != 'en': reasons.append('не англ.')
        if c['subs'] < 1000: reasons.append('<1000 підп.')
        if c['last_post_days'] > 30: reasons.append(f"неактивний {c['last_post_days']} дн.")
        if c['ER_%'] < 3: reasons.append(f"ER {c['ER_%']}%")
        if c['ER_%'] > 150: reasons.append(f"ER {c['ER_%']}% (накрутка)")
        row = known.get(u.lower(), {k: '' for k in fields})
        row.update({k: v for k, v in c.items() if k in fields})
        row['status'] = 'TEST' if not reasons else 'skip'
        row['why_not'] = '; '.join(reasons)
        row.setdefault('cluster', '')
        if not row.get('cluster'):
            row['cluster'] = 'C. Малі/середні EN крипто 1–50k' if c['subs'] <= 50000 else 'D. Великі EN крипто >50k'
        row['found_via'] = row.get('found_via') or 'ads_similar'
        if u.lower() not in known:
            rows.append(row); known[u.lower()] = row; added += 1
        time.sleep(0.4)
    with open(base_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    os.remove(cand_path)
    print(f'check: {len(cands)} checked, {added} new')


def append_log(lines):
    if not lines:
        return
    with open(os.path.join(os.path.dirname(ROOT), 'log.md'), 'a', encoding='utf-8') as f:
        f.write('\n' + '\n'.join('- ' + l for l in lines) + '\n')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'report'
    {'report': cmd_report, 'guard': cmd_guard, 'apply': cmd_apply, 'autopilot': cmd_autopilot,
     'check': cmd_check}[cmd]()
