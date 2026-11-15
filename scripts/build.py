"""Generate the static whatif.invest site into ./dist/whatif/ (Vercel runs this on every deploy).

Input:  data/market.json (prices, from scripts/fetch_data.py), data/assets.json (curated list, UA names)
Output: home + compare + one page per asset per language, index.js, per-asset price files, sitemap.
Only the Python standard library is used, so it runs in Vercel's build image as is.
Run: python3 scripts/build.py
"""
import calendar, hashlib, html, json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
OUT = os.path.join(DIST, 'whatif')
BASE = '/whatif'
SITE = 'https://mytimebox.app'
LANGS = ['uk', 'en']
AMOUNT = 10

market = json.load(open(os.path.join(ROOT, 'data/market.json'), encoding='utf-8'))
pinned = json.load(open(os.path.join(ROOT, 'data/assets.json'), encoding='utf-8'))
UPDATED = market['updated']
END = UPDATED[:7]
END_DAY = int(UPDATED[8:10])
PIN_ORDER = {a['id']: k for k, a in enumerate(pinned)}

A = {}
for aid, a in market['assets'].items():
    if 'p' in a and a['p']:
        A[aid] = a

def order_key(item):
    aid, a = item
    if aid in PIN_ORDER:
        return (0, PIN_ORDER[aid], '')
    if a['cat'] == 'crypto':
        return (1, a.get('rank') or 9999, a['tk'])
    if a['cat'] in ('etf', 'metal'):
        return (2, 0, a['tk'])
    return (3, 0, nm(a, 'en').lower())

def nm(a, lang):
    n = a['name']
    return n.get(lang) or n.get('en') or a['tk'] if isinstance(n, dict) else n

ORDERED = [aid for aid, _ in sorted(A.items(), key=order_key)]
ORD = {aid: k for k, aid in enumerate(ORDERED)}

# ---------------- math (mirrors src/app.js) ----------------
def ym2i(s):
    y, m = map(int, s.split('-'))
    return y * 12 + m - 1

def i2ym(i):
    return f"{i // 12}-{i % 12 + 1:02d}"

END_I = ym2i(END)

def per_month(i):
    return END_DAY if i2ym(i) == END else calendar.monthrange(i // 12, i % 12 + 1)[1]

def simulate(aid, start_i, amt=AMOUNT):
    P = A[aid]
    s0, e = ym2i(P['start']), ym2i(P['end'])
    frm = max(start_i, s0)
    units = inv = 0.0
    for i in range(frm, e + 1):
        c = amt * per_month(i)
        units += c / P['p'][i - s0]
        inv += c
    val = units * P['p'][e - s0]
    return dict(inv=inv, val=val, roi=(val / inv - 1) if inv else None, frm=frm)

def dca_roi(aid, years):
    st = END_I - years * 12
    if ym2i(A[aid]['start']) > st:
        return None
    return simulate(aid, st)['roi']

METRICS = {}
for aid, a in A.items():
    p = a['p']
    METRICS[aid] = dict(r1=dca_roi(aid, 1), r3=dca_roi(aid, 3), r5=dca_roi(aid, 5), r10=dca_roi(aid, 10),
                        spark=p[-13:], price=a.get('price', p[-1]), chg=a.get('chg'))

# ---------------- formatting ----------------
MON = {'uk': ['січ', 'лют', 'бер', 'кві', 'тра', 'чер', 'лип', 'сер', 'вер', 'жов', 'лис', 'гру'],
       'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
MON_GEN = ['січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']

def mlabel(ym, lang, long=False):
    y, m = map(int, ym.split('-'))
    if long:
        return f"{MON_GEN[m-1]} {y}" if lang == 'uk' else f"{calendar.month_name[m]} {y}"
    return f"{MON[lang][m-1]} {y}"

def usd(v):
    if v is None:
        return '—'
    a = abs(v)
    s = f"{a/1e9:.2f}B" if a >= 1e9 else f"{a/1e6:.2f}M" if a >= 1e6 else f"{a:,.0f}" if a >= 1e4 else f"{a:,.2f}".rstrip('0').rstrip('.')
    return ('−$' if v < 0 else '$') + s

def price(v):
    if v is None:
        return '—'
    if v >= 1:
        return f"${v:,.2f}"
    return f"${v:.4f}" if v >= 0.01 else f"${v:.8f}".rstrip('0')

def pct(p):
    if p is None:
        return '—'
    a = abs(p * 100)
    s = f"{a:,.0f}" if a >= 100 else f"{a:.1f}" if a >= 10 else f"{a:.2f}"
    return ('+' if p >= 0 else '−') + s + '%'

def cls(p):
    return '' if p is None else ('good' if p >= 0 else 'bad')

def esc(s):
    return html.escape(str(s), quote=True)

def url(lang, aid=None):
    return BASE + ('/en' if lang == 'en' else '') + '/' + (aid + '/' if aid else '')

def hue(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 360
    return h

def icon(a, big=False):
    c = ' lg' if big else ''
    if a.get('logo'):
        return f'<span class="ic{c}"><img src="{esc(a["logo"])}" alt="" loading="lazy" width="26" height="26"></span>'
    return f'<span class="ic{c}" style="background:hsl({hue(a["tk"])} 55% 52%)">{esc(a["tk"][:2])}</span>'

def spark(arr, w=110, h=34):
    if not arr or len(arr) < 2:
        return ''
    mn, mx = min(arr), max(arr)
    r = (mx - mn) or 1
    pts = ' '.join(f"{i / (len(arr) - 1) * w:.1f},{h - 2 - (v - mn) / r * (h - 4):.1f}" for i, v in enumerate(arr))
    col = '#14a44d' if arr[-1] >= arr[0] else '#e5484d'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polyline points="{pts}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round"/></svg>'

CAT = {'uk': {'crypto': 'Криптовалюта', 'stock': 'Акція', 'etf': 'ETF', 'metal': 'Метал'},
       'en': {'crypto': 'Cryptocurrency', 'stock': 'Stock', 'etf': 'ETF', 'metal': 'Metal'}}

# ---------------- page shell ----------------
def write(rel, content):
    full = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)

def h8(s):
    return hashlib.md5(s.encode()).hexdigest()[:8]

SEARCH_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'

def strip(lang):
    items = []
    for aid, label in (('btc', 'BTC'), ('eth', 'ETH'), ('spy', 'S&P 500'), ('qqq', 'Nasdaq-100'), ('gold', 'Gold' if lang == 'en' else 'Золото'), ('silver', 'Silver' if lang == 'en' else 'Срібло')):
        if aid in A:
            m = METRICS[aid]
            items.append(f'<a href="{url(lang, aid)}">{label} <b>{price(m["price"])}</b> <span class="{cls(m["chg"])}">{pct(m["chg"])}</span></a>')
    n = len(A)
    lead = (f'Активів <b>{n}</b>' if lang == 'uk' else f'Assets <b>{n}</b>')
    upd = (f'Оновлено <b>{UPDATED}</b>' if lang == 'uk' else f'Updated <b>{UPDATED}</b>')
    return f'<div class="strip"><div class="in"><span>{lead}</span>{"".join(items)}<span>{upd}</span></div></div>'

def shell(lang, path_id, title, desc, body, cfg, ver, jsonld=(), alt_path=None):
    """path_id: url suffix ('' for home, 'compare', or asset id)."""
    p = path_id or None
    canon = SITE + url(lang, p)
    alts = ''.join(f'<link rel="alternate" hreflang="{lg}" href="{SITE + url(lg, p)}">' for lg in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + url("en", p)}">'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    navs = [('', 'Рейтинг DCA' if lang == 'uk' else 'DCA ranking'), ('compare', 'Порівняти' if lang == 'uk' else 'Compare')]
    nav = ''.join(f'<a href="{url(lang, k or None)}" class="{"on" if k == (path_id or "") else ""}">{v}</a>' for k, v in navs)
    by = 'Проєкт' if lang == 'uk' else 'A project by'
    disc = ('Це не інвестиційна порада. Минулі результати не гарантують майбутніх. Розрахунки за місячними цінами закриття, без комісій, податків і дивідендів.'
            if lang == 'uk' else 'Not investment advice. Past performance does not guarantee future results. Calculations use monthly closes and exclude fees, taxes and dividends.')
    src = ('Дані: Binance, Yahoo Finance, CoinGecko.' if lang == 'uk' else 'Data: Binance, Yahoo Finance, CoinGecko.')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:locale" content="{'uk_UA' if lang == 'uk' else 'en_US'}">
<meta name="twitter:card" content="summary"><meta name="theme-color" content="#ffffff">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/style.css?v={ver['css']}">
{ld}
</head>
<body>
{strip(lang)}
<div class="top"><div class="in">
  <a class="logo" href="{url(lang)}">what<b>if</b>.invest</a>
  <div class="gsearch">{SEARCH_ICON}<input id="gs" type="search" autocomplete="off" aria-label="search"><div class="gres" id="gres"></div></div>
  <nav class="nav">{nav}</nav>
  <nav class="lang"><a href="{url('uk', p)}" class="{'on' if lang == 'uk' else ''}" hreflang="uk">UA</a><a href="{url('en', p)}" class="{'on' if lang == 'en' else ''}" hreflang="en">EN</a></nav>
</div></div>
<main class="wrap">
{body}
<footer><span>{by} <a href="{SITE}/">Timebox</a> · {src}</span><span>{disc}</span></footer>
</main>
<script>window.PAGE={json.dumps(cfg)};</script>
<script src="{BASE}/assets/index.js?v={ver['index']}"></script>
<script src="{BASE}/assets/ref.js?v={ver['ref']}"></script>
<script src="{BASE}/assets/app.js?v={ver['js']}" defer></script>
</body>
</html>
"""

def calc_block(lang):
    t = {'uk': dict(amount='Сума', freq='Як часто', d='Щодня', w='Щотижня', m='Щомісяця', since='Починаючи з', on='Активи на графіку',
                    chart='Вартість портфеля в часі', log='Лог. шкала', copy='Копіювати'),
         'en': dict(amount='Amount', freq='How often', d='Daily', w='Weekly', m='Monthly', since='Starting from', on='Assets on the chart',
                    chart='Portfolio value over time', log='Log scale', copy='Copy')}[lang]
    return f"""<div id="calc">
<div class="card">
  <div class="controls">
    <div><label class="f">{t['amount']}</label><div class="inp"><span>$</span><input id="amt" type="number" min="1" step="1" value="{AMOUNT}" aria-label="{t['amount']}"></div></div>
    <div><label class="f">{t['freq']}</label><div class="seg" id="freq"><button data-v="d" class="on">{t['d']}</button><button data-v="w">{t['w']}</button><button data-v="m">{t['m']}</button></div></div>
    <div><label class="f">{t['since']}</label><div class="inp"><select id="since" aria-label="{t['since']}"></select></div></div>
  </div>
  <label class="f">{t['on']}</label>
  <div class="chips" id="chips"></div>
  <div class="picker" id="picker"><div class="filter">{SEARCH_ICON}<input id="pq" type="search" autocomplete="off"></div><div class="pool" id="pool"></div></div>
</div>
<div class="hero" id="hero"></div>
<div class="card chartcard" id="chartcard"><div class="charthead"><h2>{t['chart']}</h2><button class="toggle" id="logBtn">{t['log']}</button></div><div id="chart"></div><div class="tip" id="tip"></div></div>
<div class="card section"><div style="overflow-x:auto"><table class="rt" id="rt"></table></div>
<div class="share"><p id="shareText"></p><button class="btn ghost" id="copyBtn">{t['copy']}</button></div></div>
</div>"""

def row_html(aid, lang, n):
    a, m = A[aid], METRICS[aid]
    return (f'<tr><td class="l n hide-sm">{n}</td><td class="l"><a class="asset" href="{url(lang, aid)}">{icon(a)}<span><span class="nm">{esc(nm(a, lang))}</span>'
            f'<span class="tk">{esc(a["tk"])}</span></span></a></td><td></td><td class="num">{price(m["price"])}</td>'
            f'<td class="num {cls(m["chg"])}">{pct(m["chg"])}</td><td class="num hide-sm {cls(m["r1"])}">{pct(m["r1"])}</td>'
            f'<td class="num hide-sm {cls(m["r3"])}">{pct(m["r3"])}</td><td><span class="pill {cls(m["r5"])}">{pct(m["r5"])}</span></td>'
            f'<td class="hide-sm">{spark(m["spark"])}</td><td class="hide-sm"><a class="calc" href="{url(lang, aid)}">→</a></td></tr>')

def table_block(lang, ids, title=None, interactive=True):
    head = {'uk': ['#', 'Назва', '', 'Ціна', '24г', 'DCA 1 рік', 'DCA 3 роки', 'DCA 5 років', 'Ціна за рік', ''],
            'en': ['#', 'Name', '', 'Price', '24h', 'DCA 1Y', 'DCA 3Y', 'DCA 5Y', 'Price, 1Y', '']}[lang]
    hc = ['l n hide-sm', 'l', '', '', '', 'hide-sm', 'hide-sm', '', 'hide-sm', 'hide-sm']
    th = ''.join(f'<th class="{c}">{h}</th>' for h, c in zip(head, hc))
    rows = ''.join(row_html(aid, lang, k + 1) for k, aid in enumerate(ids))
    tid = ' id="mt"' if interactive else ''
    hid = ' id="mthead"' if interactive else ''
    more = '<div id="mtmore"></div>' if interactive else ''
    ttl = f'<h2>{title}</h2>' if title else ''
    return f'{ttl}<div class="tw"><table class="mt"><thead{hid}><tr>{th}</tr></thead><tbody{tid}>{rows}</tbody></table>{more}</div>'

# ---------------- pages ----------------
def best_by(key, ids, reverse=True):
    xs = [i for i in ids if METRICS[i][key] is not None]
    return sorted(xs, key=lambda i: METRICS[i][key], reverse=reverse)

def hl_card(lang, aid, label, key, sub):
    m = METRICS[aid]
    return (f'<a class="card" href="{url(lang, aid)}"><div class="k">{label}<span>{esc(A[aid]["tk"])}</span></div>'
            f'<div class="v {cls(m[key])}">{pct(m[key])}</div><div class="s">{esc(nm(A[aid], lang))} · {sub}</div>{spark(m["spark"], 220, 40)}</a>')

def home(lang, ver):
    ids = ORDERED
    b1 = best_by('r1', ids)
    b5 = best_by('r5', ids)
    big = [i for i in ids if A[i]['cat'] == 'crypto' and ORD[i] < 60]
    bc = best_by('r1', big)
    sub1 = '$10/день, 1 рік' if lang == 'uk' else '$10/day, 1 year'
    sub5 = '$10/день, 5 років' if lang == 'uk' else '$10/day, 5 years'
    cards = []
    if b1: cards.append(hl_card(lang, b1[0], 'Лідер DCA за рік' if lang == 'uk' else 'Top DCA, 1 year', 'r1', sub1))
    if b5: cards.append(hl_card(lang, b5[0], 'Лідер DCA за 5 років' if lang == 'uk' else 'Top DCA, 5 years', 'r5', sub5))
    if bc: cards.append(hl_card(lang, bc[0], 'Найкраща велика крипта' if lang == 'uk' else 'Best large-cap crypto', 'r1', sub1))
    for aid in ('btc', 'spy', 'gold'):
        if aid in A and len(cards) < 4:
            cards.append(hl_card(lang, aid, nm(A[aid], lang), 'r5', sub5))
    n = len(A)
    if lang == 'uk':
        title = 'Що якби я щодня вкладав $10? Рейтинг DCA для крипти, акцій і золота'
        desc = f'Скільки б ти мав, якби регулярно купував Bitcoin, Nvidia, Apple, золото чи ще {n} активів. Рейтинг DCA за 1, 3 і 5 років, калькулятор, щоденне оновлення.'
        h1 = 'Що якби я щодня вкладав <em>$10</em>?'
        lead = f'Рейтинг <b>{n} активів</b> за результатом регулярних покупок (DCA): крипта, акції S&P 500, ETF, золото і срібло. Колонки DCA показують дохідність, якби ти купував на $10 щодня протягом 1, 3 чи 5 років.'
    else:
        title = 'What if I invested $10 a day? DCA ranking for crypto, stocks and gold'
        desc = f'See what you would have if you had regularly bought Bitcoin, Nvidia, Apple, gold or {n} other assets. DCA returns over 1, 3 and 5 years, calculator, updated daily.'
        h1 = 'What if I invested <em>$10</em> every day?'
        lead = f'<b>{n} assets</b> ranked by dollar-cost averaging results: crypto, S&P 500 stocks, ETFs, gold and silver. DCA columns show the return of buying $10 every day for 1, 3 or 5 years.'
    filt = f'<div class="toolbar"><div class="filter">{SEARCH_ICON}<input id="flt" type="search" autocomplete="off"></div></div>'
    body = (f'<h1>{h1}</h1><p class="lead">{lead}</p><div class="hl">{"".join(cards)}</div>'
            f'<div class="tabs" id="tabs"></div>{filt}{table_block(lang, ids[:100])}')
    jsonld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "whatif.invest", "url": SITE + url(lang),
               "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "inLanguage": lang,
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}]
    return shell(lang, '', title, desc, body, dict(lang=lang), ver, jsonld)

def compare(lang, ver):
    sel = [i for i in ('btc', 'nvda', 'gold', 'spy', 'eth') if i in A]
    if lang == 'uk':
        title = 'Порівняти DCA: Bitcoin, акції, золото — калькулятор регулярних інвестицій'
        desc = 'Порівняй, скільки б ти заробив, регулярно купуючи до 8 активів одночасно: крипту, акції, ETF, золото і срібло.'
        h1 = 'Порівняти регулярні інвестиції'
        lead = 'Обери суму, частоту і дату старту, додай до 8 активів і подивись, як росла б вартість кожного портфеля.'
    else:
        title = 'Compare DCA: Bitcoin, stocks, gold — recurring investment calculator'
        desc = 'Compare what you would have earned by regularly buying up to 8 assets at once: crypto, stocks, ETFs, gold and silver.'
        h1 = 'Compare recurring investments'
        lead = 'Pick an amount, frequency and start date, add up to 8 assets and see how each portfolio would have grown.'
    body = f'<h1>{h1}</h1><p class="lead">{lead}</p>{calc_block(lang)}'
    return shell(lang, 'compare', title, desc, body, dict(lang=lang, sel=sel, since=f"{END_I // 12 - 5}-01"), ver)

PERIODS = [(1, {'uk': '1 рік', 'en': '1 year'}), (3, {'uk': '3 роки', 'en': '3 years'}),
           (5, {'uk': '5 років', 'en': '5 years'}), (10, {'uk': '10 років', 'en': '10 years'})]

def default_since(aid):
    s0 = ym2i(A[aid]['start'])
    st = max(s0, END_I - 60)
    y = (st + 11) // 12
    return f"{y}-01" if y * 12 < END_I - 6 else i2ym(s0)

def bench(aid):
    for b in ('btc', 'spy', 'qqq', 'gold'):
        if b != aid and b in A:
            yield b

def asset(aid, lang, ver):
    a, m = A[aid], METRICS[aid]
    n, tk = nm(a, lang), a['tk']
    since = default_since(aid)
    r = simulate(aid, ym2i(since))
    since_long = mlabel(i2ym(r['frm']), lang, long=True)
    upd = mlabel(END, lang, long=True)
    b1 = next(bench(aid))
    s5 = END_I - 60
    ra5 = simulate(aid, max(s5, ym2i(a['start'])))
    rb5 = simulate(b1, max(s5, ym2i(A[b1]['start'])))
    # period stats
    stats, rows = [], []
    s0 = ym2i(a['start'])
    for yrs, lab in PERIODS:
        st = END_I - yrs * 12
        if st < s0:
            continue
        x = simulate(aid, st)
        stats.append((lab[lang], x))
    full = simulate(aid, s0)
    lab_all = ('Від ' if lang == 'uk' else 'Since ') + mlabel(i2ym(s0), lang)
    rows = stats + [(lab_all, full)]
    stat_cards = ''.join(
        f'<div class="card stat"><div class="k">DCA $10/{"день" if lang == "uk" else "day"} · {lab}</div><div class="v">{usd(x["val"])}</div>'
        f'<div class="s {cls(x["roi"])}">{pct(x["roi"])} <span class="muted">· {"вкладено" if lang == "uk" else "invested"} {usd(x["inv"])}</span></div></div>'
        for lab, x in (stats[:4] if len(stats) >= 2 else rows[-4:]))
    hh = ['Період', 'Вкладено', 'Зараз', 'Результат'] if lang == 'uk' else ['Period', 'Invested', 'Now', 'Result']
    ptable = ('<table class="rt"><tr>' + ''.join(f'<th>{h}</th>' for h in hh) + '</tr>' +
              ''.join(f'<tr><td class="a">{lab}</td><td>{usd(x["inv"])}</td><td>{usd(x["val"])}</td><td class="{cls(x["roi"])}">{pct(x["roi"])}</td></tr>' for lab, x in rows) +
              '</table>')
    if lang == 'uk':
        title = f"$10 щодня в {n} ({tk}): скільки б ти мав зараз? DCA-калькулятор"
        desc = f"$10 щодня в {n} з {since_long}: вкладено {usd(r['inv'])}, зараз {usd(r['val'])} ({pct(r['roi'])}). Ціна {tk}, DCA за 1, 3, 5 і 10 років і порівняння з {len(A) - 1} активами."
        h1 = f"Що якби я щодня вкладав <em>$10</em> у {esc(n)}?"
        lead = (f"Якби ти з {since_long} щодня купував {esc(n)} на $10, то вклав би <b>{usd(r['inv'])}</b>, а зараз мав би <b>{usd(r['val'])}</b> "
                f"(<span class=\"{cls(r['roi'])}\">{pct(r['roi'])}</span>). Зміни суму, частоту чи дату старту і порівняй з іншими активами.")
        h2p, h2s, h2f = f"$10 щодня в {esc(n)}: результати за періоди", f"Схожі активи: {CAT[lang][a['cat']].lower()}", 'Часті питання'
        faq = [(f"Скільки б я мав, якби вкладав $10 щодня в {n} з {since_long}?",
                f"Ти вклав би {usd(r['inv'])}, а станом на {upd} мав би {usd(r['val'])} ({pct(r['roi'])}). Розрахунок за місячними цінами закриття, без комісій і податків."),
               (f"Що вигідніше для щоденних покупок за 5 років: {n} чи {nm(A[b1], lang)}?",
                f"$10 щодня протягом останніх 5 років дали б {pct(ra5['roi'])} для {n} і {pct(rb5['roi'])} для {nm(A[b1], lang)}. Минулі результати не гарантують майбутніх."),
               ("Що таке DCA (усереднення вартості)?",
                "DCA — це регулярна покупка активу на однакову суму незалежно від ціни. Коли ціна низька, купуєш більше, коли висока — менше. Так згладжується волатильність і не треба вгадувати момент входу.")]
    else:
        title = f"$10 a day in {n} ({tk}): what would it be worth now? DCA calculator"
        desc = f"$10 a day in {n} since {since_long}: {usd(r['inv'])} invested, worth {usd(r['val'])} today ({pct(r['roi'])}). {tk} price, DCA returns over 1, 3, 5 and 10 years, compared with {len(A) - 1} assets."
        h1 = f"What if I invested <em>$10</em> a day in {esc(n)}?"
        lead = (f"If you had bought $10 of {esc(n)} every day since {since_long}, you would have put in <b>{usd(r['inv'])}</b> and it would be worth <b>{usd(r['val'])}</b> today "
                f"(<span class=\"{cls(r['roi'])}\">{pct(r['roi'])}</span>). Change the amount, frequency or start date and compare with other assets.")
        h2p, h2s, h2f = f"$10 a day in {esc(n)}: results by period", f"Similar assets: {CAT[lang][a['cat']].lower()}", 'FAQ'
        faq = [(f"How much would I have if I invested $10 a day in {n} since {since_long}?",
                f"You would have invested {usd(r['inv'])}, and as of {upd} it would be worth {usd(r['val'])} ({pct(r['roi'])}). Based on monthly closing prices, before fees and taxes."),
               (f"Which was better to buy daily over the last 5 years: {n} or {nm(A[b1], lang)}?",
                f"$10 a day over the last 5 years would have returned {pct(ra5['roi'])} for {n} and {pct(rb5['roi'])} for {nm(A[b1], lang)}. Past performance does not guarantee future results."),
               ("What is DCA (dollar-cost averaging)?",
                "DCA means buying an asset for the same amount at regular intervals, whatever the price. You buy more when it is cheap and less when it is expensive, which smooths volatility and removes the need to time the market.")]
    sim = [i for i in ORDERED if A[i]['cat'] == a['cat'] and i != aid]
    if a.get('sector'):
        same = [i for i in sim if A[i].get('sector') == a['sector']]
        sim = same + [i for i in sim if i not in same]
    sim = sim[:10]
    crumbs = f'<nav class="crumbs"><a href="{url(lang)}">{"Рейтинг DCA" if lang == "uk" else "DCA ranking"}</a> / {esc(CAT[lang][a["cat"]])} / {esc(n)}</nav>'
    badges = f'<span class="badge">{esc(tk)}</span> <span class="badge">{esc(CAT[lang][a["cat"]])}</span>' + (f' <span class="badge">{esc(a["sector"])}</span>' if a.get('sector') else '')
    head = (f'{crumbs}<div class="ahead">{icon(a, True)}<div><h1>{h1}</h1><div style="margin-top:4px">{badges}</div></div>'
            f'<div class="price"><span class="v">{price(m["price"])}</span><span class="pill {cls(m["chg"])}">{pct(m["chg"])}</span><span id="buyslot" data-id="{aid}"></span></div></div>')
    body = (f'{head}<p class="lead" style="margin-top:10px">{lead}</p><div class="stats">{stat_cards}</div>{calc_block(lang)}'
            f'<div class="cols2 section"><section class="card"><h2>{h2p}</h2>{ptable}</section>'
            f'<section class="card faq"><h2>{h2f}</h2>' + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q, x in faq) + '</section></div>'
            f'<section class="section">{table_block(lang, sim, h2s, interactive=False)}</section>')
    jsonld = [{"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": x}} for q, x in faq]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "whatif.invest", "item": SITE + url(lang)},
                  {"@type": "ListItem", "position": 2, "name": n, "item": SITE + url(lang, aid)}]}]
    sel = [aid] + list(bench(aid))[:2]
    return shell(lang, aid, title, desc, body, dict(lang=lang, sel=sel, since=since, asset=aid), ver, jsonld)

# ---------------- build ----------------
def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(OUT)
    css = open(os.path.join(ROOT, 'src/style.css'), encoding='utf-8').read()
    js = open(os.path.join(ROOT, 'src/app.js'), encoding='utf-8').read()
    ref = open(os.path.join(ROOT, 'src/ref.js'), encoding='utf-8').read()
    dv = h8(json.dumps(market['assets'], sort_keys=True))[:8]
    idx = []
    for aid in ORDERED:
        a, m = A[aid], METRICS[aid]
        e = dict(i=aid, n=nm(a, 'uk'), t=a['tk'], c=a['cat'], o=ORD[aid], pr=m['price'], ch=m['chg'],
                 r1=m['r1'], r3=m['r3'], r5=m['r5'], sp=m['spark'], s=a['start'])
        if nm(a, 'en') != e['n']:
            e['ne'] = nm(a, 'en')
        if a.get('logo'):
            e['l'] = a['logo']
        e = {k: (round(v, 4) if isinstance(v, float) and k in ('ch', 'r1', 'r3', 'r5') else v) for k, v in e.items() if v is not None}
        idx.append(e)
        write(f'assets/p/{aid}.json', json.dumps({'start': a['start'], 'end': a['end'], 'p': a['p']}, separators=(',', ':')))
    index_js = 'window.WI=' + json.dumps({'u': UPDATED, 'v': dv, 'a': idx}, ensure_ascii=False, separators=(',', ':')) + ';'
    write('assets/index.js', index_js); write('assets/style.css', css); write('assets/app.js', js); write('assets/ref.js', ref)
    shutil.copy(os.path.join(ROOT, 'src/favicon.svg'), os.path.join(OUT, 'assets/favicon.svg'))
    ver = dict(css=h8(css), js=h8(js), ref=h8(ref), index=h8(index_js))
    urls = []
    for lang in LANGS:
        pre = 'en/' if lang == 'en' else ''
        write(pre + 'index.html', home(lang, ver)); urls.append((None, lang))
        write(pre + 'compare/index.html', compare(lang, ver)); urls.append(('compare', lang))
        for aid in ORDERED:
            write(f'{pre}{aid}/index.html', asset(aid, lang, ver)); urls.append((aid, lang))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p, lang in urls:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="{SITE + url(lg, p)}"/>' for lg in LANGS)
        sm.append(f'<url><loc>{SITE + url(lang, p)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
    sm.append('</urlset>')
    write('sitemap.xml', '\n'.join(sm))
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}{BASE}/sitemap.xml\n')
    cats = {}
    for a in A.values():
        cats[a['cat']] = cats.get(a['cat'], 0) + 1
    print(f"built {len(urls)} pages · {len(A)} assets {cats} · data {UPDATED}")

if __name__ == '__main__':
    main()
