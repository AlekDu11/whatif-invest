"""Safety net for the Telegram channel: if a scheduled post did not go out (owner's computer off), post one automatically.

Runs from .github/workflows/tg-queue.yml at ~14:20 and ~20:20 Kyiv. Slot «day» (13:41 run) = a «💵 $10 a day» comparison of
3 assets computed from data/market.json; slot «eve» (19:41 run) = the newest English article not yet in the log (cover + lead).
Skips when social/telegram-log.md already has a row for today in that slot or the queue already holds an item.
Writes social/queue/tg/<date>-<HHMM>-auto-<slot>.json (tg_queue.py sends it) and appends the log row. stdlib + Pillow."""
import datetime, glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
LOG = os.path.join(ROOT, 'social', 'telegram-log.md')
Q = os.path.join(ROOT, 'social', 'queue', 'tg')
GROUPS = [('btc', 'eth', 'sol'), ('nvda', 'msft', 'aapl'), ('gold', 'silver', 'spy'), ('xrp', 'bnb', 'ada'), ('amzn', 'googl', 'meta'),
          ('qqq', 'spy', 'btc'), ('tsla', 'byd', 'nvda'), ('doge', 'shib', 'pepe'), ('v', 'ma', 'jpm'), ('tsm', 'avgo', 'amd'),
          ('ko', 'pep-stock', 'mcd'), ('gold', 'btc', 'qqq'), ('eth', 'bnb', 'trx'), ('nflx', 'dis', 'spot')]


def kyiv_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo('Europe/Kyiv'))
    except Exception:
        return datetime.datetime.utcnow() + datetime.timedelta(hours=2)


def logged(day, lo, hi):
    for ln in open(LOG, encoding='utf-8'):
        m = re.match(r'\|\s*(\d{4}-\d{2}-\d{2}) (\d{2}):\d{2}', ln)
        if m and m.group(1) == day and lo <= int(m.group(2)) < hi:
            return True
    return False


def money(v):
    return f'${v:,.0f}'


def day_post(b, now):
    recent = open(LOG, encoding='utf-8').read().lower()[-4000:]
    ok = [g for g in GROUPS if all(i in b.A for i in g)]
    fresh = [g for g in ok if not any(b.nm(b.A[i], 'en').lower() in recent for i in g)] or ok
    g = fresh[now.timetuple().tm_yday % len(fresh)]
    st = max([b.END_I - 60] + [b.ym2i(b.A[i]['start']) for i in g])   # same start for all three, so «each one» is true
    res = sorted(((i, b.simulate(i, st)) for i in g), key=lambda x: -(x[1]['roi'] or -9))
    lead, r0 = res[0]
    medals = ['🥇', '🥈', '🥉']
    name = lambda i: b.nm(b.A[i], 'en')
    yrs = (b.END_I - st) // 12 or 1
    lines = [['b', f"💵 $10 a day for {yrs} years: {name(lead)} {b.pct(r0['roi'])}"], '',
             f"What buying {', '.join(name(i) for i, _ in res[:-1])} and {name(res[-1][0])} every day would have made.", '',
             ['b', 'In numbers']]
    lines += [f"{medals[k]} {name(i)}  {b.pct(r['roi'])} → {money(r['val'])}" for k, (i, r) in enumerate(res)]
    lines += ['', f"Each one: {money(r0['inv'])} put in.", '', '👉 Try your own coin and amount: whatifstack.com/en/compare/']
    topic = f"auto: 5 years of $10/day: " + ', '.join(f"{name(i)} {b.pct(r['roi'])}" for i, r in res)
    card = dict(title=f"$10 a day in {name(lead)} for {yrs} years", stat=b.pct(r0['roi']), stat_label=f"{money(r0['inv'])} → {money(r0['val'])}",
                assets=','.join(g), label='$10 a day')
    return '💵 $10 a day', lines, topic, 'whatifstack.com/en/compare/', card, None


def eve_post(now):
    log = open(LOG, encoding='utf-8').read()
    posts = []
    for p in glob.glob(os.path.join(ROOT, 'content', 'blog', 'en', '*.md')):
        raw = open(p, encoding='utf-8').read()
        meta = dict(re.findall(r'^(\w+):\s*(.*)$', raw.split('\n---', 1)[0], re.M))
        slug = os.path.basename(p)[:-3]
        if slug not in log and meta.get('date'):
            posts.append((meta['date'], slug, meta))
    if not posts:
        return None
    date, slug, m = max(posts)
    title, desc = m.get('title', '').strip('"\''), m.get('description', '').strip('"\'')
    link = f'whatifstack.com/en/blog/{slug}/'
    lines = [['b', f'📰 {title}'], '', desc, '', f'👉 Read it: {link}']
    cover = f'content/covers/blog/en/{slug}.jpg'
    return '📰 Best of the day', lines, f'auto: article "{title}"', link, None, cover if os.path.exists(os.path.join(ROOT, cover)) else None


def main():
    now = kyiv_now()
    day = now.strftime('%Y-%m-%d')
    slot = sys.argv[1] if len(sys.argv) > 1 else ('day' if now.hour < 19 else 'eve')
    lo, hi = (13, 19) if slot == 'day' else (19, 24)
    # give the normal 13:41 / 19:41 run until :56 (lo:00 + 75 min + the run's own minutes)
    if now.hour * 60 + now.minute < lo * 60 + 75 or logged(day, lo, hi) or glob.glob(os.path.join(Q, '*.json')):
        print('nothing to do', slot, now.isoformat()); return
    if slot == 'day':
        import build as b
        b.set_numfmt('en')
        series, lines, topic, link, card, photo = day_post(b, now)
    else:
        r = eve_post(now)
        if not r:
            import build as b
            b.set_numfmt('en')
            r = day_post(b, now)
        series, lines, topic, link, card, photo = r
    stamp = now.strftime('%Y-%m-%d-%H%M')
    if card:
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'cover.py'), '--x', f'tg-{stamp}', '--lang', 'en', '--title', card['title'],
                              '--stat', card['stat'], '--stat-label', card['stat_label'], '--assets', card['assets'], '--label', card['label']],
                             capture_output=True, text=True).stdout.strip().splitlines()
        photo = os.path.relpath(out[-1], ROOT) if out and out[-1].endswith('.jpg') else None
    os.makedirs(Q, exist_ok=True)
    item = dict(lines=lines)
    if photo:
        item['photo'] = photo
    json.dump(item, open(os.path.join(Q, f'{stamp}-auto-{slot}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(f"| {now.strftime('%Y-%m-%d %H:%M')} | {series} | {topic} (backup bot) | {link} | |\n")
    print('queued', stamp, slot)


if __name__ == '__main__':
    main()
