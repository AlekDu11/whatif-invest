"""Generate the static whatif.invest site into ./dist/ (Vercel runs this on every deploy).

Input:  data/market.json (prices, from scripts/fetch_data.py), data/assets.json (curated list),
        scripts/i18n*.py (20 languages).
Output: per language — home, compare and asset pages; index.js, per-asset price files, sitemaps.
Only the Python standard library is used, so it runs in Vercel's build image as is.
Run: python3 scripts/build.py
"""
import calendar, hashlib, html, json, math, os, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import LANGS as TR, ORDER, FULL, DEFAULT  # noqa: E402
from i18n_t import T as TT  # noqa: E402
from i18n_e import E as EX  # noqa: E402
from i18n_n import N as NW, FOOT  # noqa: E402
from i18n_p import P as POLL, OPTS as POLL_OPTS  # noqa: E402
SOCIAL = []   # [(label, url)], e.g. ('Telegram', 'https://t.me/whatifstack'); the 'Follow us' column appears when filled
from i18n_h import H as HB, PRICES as HPRICE, SCEN as HSCEN, UNITS as HUNITS, CONV as HCONV  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
OUT = DIST
BASE = ''
SITE = 'https://whatifstack.com'
BRAND = 'WhatIfStack'
AMOUNT = 10
TOP_N = 200            # asset pages in languages outside FULL

market = json.load(open(os.path.join(ROOT, 'data/market.json'), encoding='utf-8'))
pinned = json.load(open(os.path.join(ROOT, 'data/assets.json'), encoding='utf-8'))
UPDATED = market['updated']
END = UPDATED[:7]
END_DAY = int(UPDATED[8:10])
PIN_ORDER = {a['id']: k for k, a in enumerate(pinned)}
RESERVED = set(ORDER) | {'assets', 'blog', 'compare', 'crypto', 'stocks', 'etfs', 'metals', 'converter', 'calendar', 'heatmap', 'news', 'bubbles', 'screener', 'habits', 'millionaire', 'compound-interest', 'inflation', 'ath', 'bitcoin-halving', 'exchanges'}
# asset ids that clash with a language folder or a section get a suffix (ko -> ko-stock, fil -> fil-crypto)
_END_I0 = (lambda s: int(s[:4]) * 12 + int(s[5:7]) - 1)(market['updated'][:7])
# delisted or stale series (last price older than a month) are dropped: "today" numbers would be false
A = {(f"{aid}-{a['cat']}" if aid in RESERVED else aid): a for aid, a in market['assets'].items()
     if a.get('p') and (lambda s: int(s[:4]) * 12 + int(s[5:7]) - 1)(a['end']) >= _END_I0 - 1}
_gp = os.path.join(ROOT, 'data/global.json')
G = json.load(open(_gp, encoding='utf-8')) if os.path.exists(_gp) else {}
_fp = os.path.join(ROOT, 'data/fx.json')
FX = json.load(open(_fp, encoding='utf-8')) if os.path.exists(_fp) else {'rates': {}}
_cp = os.path.join(ROOT, 'data/cpi.json')
CPI = json.load(open(_cp, encoding='utf-8')) if os.path.exists(_cp) else {'c': {}}
TV_LOC = {'en': 'en', 'uk': 'uk', 'ru': 'ru', 'es': 'es', 'pt': 'br', 'de': 'de_DE', 'fr': 'fr', 'it': 'it', 'pl': 'pl', 'tr': 'tr',
          'nl': 'nl_NL', 'id': 'id', 'vi': 'vi_VN', 'th': 'th_TH', 'hi': 'in', 'ja': 'ja', 'ko': 'kr', 'zh': 'zh_CN', 'ar': 'ar_AE', 'fil': 'en'}


def tv_symbol(a):
    if a['cat'] == 'crypto':
        return f"BINANCE:{a['tk']}USDT"
    if a['cat'] == 'metal':
        return 'OANDA:XAUUSD' if a['tk'] == 'XAU' else 'OANDA:XAGUSD'
    return a['tk'].replace('-', '.')


def nm(a, lang):
    n = a['name']
    if a['tk'] in ('XAU', 'XAG') and a.get('cat') == 'metal':
        return TR[lang]['gold' if a['tk'] == 'XAU' else 'silver']
    if not isinstance(n, dict):
        return n
    return n.get(lang) or n.get('en') or a['tk']


def order_key(item):
    aid, a = item
    if aid in PIN_ORDER:
        return (0, PIN_ORDER[aid], '')
    if a['cat'] == 'crypto':
        return (1, a.get('rank') or 9999, a['tk'])
    if a['cat'] in ('etf', 'metal'):
        return (2, 0, a['tk'])
    return (3, 0, nm(a, 'en').lower())


ORDERED = [aid for aid, _ in sorted(A.items(), key=order_key)]
ORD = {aid: k for k, aid in enumerate(ORDERED)}
TOP = set(ORDERED[:TOP_N])


HUBS = {'crypto': 'crypto', 'stocks': 'stock', 'etfs': 'etf', 'metals': 'metal'}
TOOLS = ['converter']
CALCS = ['millionaire', 'compound-interest', 'inflation', 'ath', 'bitcoin-halving', 'exchanges', 'news', 'about']
BLOG_LANGS = {l for l in ORDER if os.path.isdir(os.path.join(ROOT, 'content/blog', l)) and any(f.endswith('.md') for f in os.listdir(os.path.join(ROOT, 'content/blog', l)))}  # a language gets a blog once it has a post
assert not (set(HUBS) | set(TOOLS) | {'blog', 'compare'}) & set(A), 'asset id collides with a section slug'


def has_page(lang, aid):
    if aid is None or aid == 'compare' or aid in HUBS or aid in TOOLS:
        return True
    if aid in CALCS:
        if aid == 'about':
            return lang in ABOUT
        return aid != 'inflation' or bool(CPI['c'])
    if aid == 'habits' or (aid or '').startswith('habits/'):
        return True
    if (aid or '').startswith('news/'):
        return aid[5:] in NEWS.get(lang, {})
    if aid == 'blog' or (aid or '').startswith('blog/'):
        return lang in BLOG_LANGS and (aid == 'blog' or aid[5:] in POSTS.get(lang, {}))
    return lang in FULL or aid in TOP


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
    return None if ym2i(A[aid]['start']) > st else simulate(aid, st)['roi']


METRICS = {aid: dict(r1=dca_roi(aid, 1), r3=dca_roi(aid, 3), r5=dca_roi(aid, 5), spark=a['p'][-13:],
                     price=a.get('price', a['p'][-1]), chg=a.get('chg')) for aid, a in A.items()}


# ---------------- formatting ----------------
def mlabel(ym, lang, long=False):
    y, m = map(int, ym.split('-'))
    S = TR[lang]
    mon = (S['since_months'] if long else S['months'])[m - 1]
    return S['date'].format(m=mon, y=y)


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


def url(lang, p=None):
    pre = BASE + ('' if lang == DEFAULT else '/' + lang)
    return pre + '/' + (p + '/' if p else '')


def aurl(lang, aid):
    """Asset link: same language if that page exists, else English."""
    return url(lang if has_page(lang, aid) else 'en', aid)


LOGO_DIR = os.path.join(ROOT, 'data/logos')
_LOGOS = {f[:-5] for f in os.listdir(LOGO_DIR) if f.endswith('.webp')} if os.path.isdir(LOGO_DIR) else set()
for _aid, _a in A.items():                      # self-hosted logo (downloaded once by fetch_data.py) beats a remote one
    _src = _aid if _aid in _LOGOS else _aid.rsplit('-', 1)[0] if _aid.rsplit('-', 1)[0] in _LOGOS else None
    if _src:
        _a['logo'] = f'{BASE}/assets/logo/{_src}.webp'
METAL_IC = {'GC=F': ('#d4a017', 'Au'), 'SI=F': ('#9ea3ab', 'Ag')}


def hue(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 360
    return h


def icon(a, big=False):
    c = ' lg' if big else ''
    if a.get('cat') == 'metal' and not a.get('logo'):
        bg, t = METAL_IC.get(a.get('yahoo'), ('#b8a06a', a['tk'][:2]))
        return f'<span class="ic{c}" style="background:{bg}">{t}</span>'
    if a.get('logo'):
        return (f'<span class="ic{c}" style="background:hsl({hue(a["tk"])} 55% 52%)"><img src="{esc(a["logo"])}" alt="" loading="lazy" width="26" height="26" '
                f'onerror="this.parentNode.textContent=\'{esc(a["tk"][:2])}\'"></span>')
    return f'<span class="ic{c}" style="background:hsl({hue(a["tk"])} 55% 52%)">{esc(a["tk"][:2])}</span>'


def spark(arr, w=110, h=34):
    if not arr or len(arr) < 2:
        return ''
    mn, mx = min(arr), max(arr)
    r = (mx - mn) or 1
    pts = ' '.join(f"{i / (len(arr) - 1) * w:.1f},{h - 2 - (v - mn) / r * (h - 4):.1f}" for i, v in enumerate(arr))
    col = '#14a44d' if arr[-1] >= arr[0] else '#e5484d'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polyline points="{pts}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round"/></svg>'


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
    S = TR[lang]
    items = []
    for aid, label in (('btc', 'BTC'), ('eth', 'ETH'), ('spy', 'S&P 500'), ('qqq', 'Nasdaq-100'), ('gold', S['gold']), ('silver', S['silver'])):
        if aid in A:
            m = METRICS[aid]
            items.append(f'<a href="{aurl(lang, aid)}">{esc(label)} <b data-p="{aid}">{price(m["price"])}</b> <span class="{cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</span></a>')
    return (f'<div class="strip"><div class="in"><span>{S["assets_n"]} <b>{len(A)}</b></span>{"".join(items)}'
            f'<span>{S["updated"]} <b>{UPDATED}</b></span></div></div>')


def lang_menu(lang, p):
    opts = ''.join(f'<option value="{url(lg, p) if has_page(lg, p) else url(lg)}"{" selected" if lg == lang else ""}>{esc(TR[lg]["name"])}</option>' for lg in ORDER)
    return f'<select class="langsel" aria-label="Language" onchange="location.href=this.value">{opts}</select>'


def poll_block(lang):
    q, opts, thanks = POLL[lang]
    b = ''.join(f'<button data-o="{k}">{esc(v)}</button>' for k, v in zip(POLL_OPTS, opts.split('|')))
    return f'<section class="card section poll" id="poll" hidden data-thanks="{esc(thanks)}"><b>🗳 {esc(q)}</b><div class="pollb">{b}</div></section>'


def footer_cols(lang):
    S, n, f = TR[lang], NW[lang], FOOT[lang]
    blog_l = lang if lang in BLOG_LANGS else 'en'
    pop = [(aurl(lang, i), nm(A[i], lang)) for i in ('btc', 'eth', 'sol', 'xrp', 'nvda', 'aapl', 'tsla', 'gold', 'spy', 'qqq') if i in A]
    mk = [(url(lang), S['nav_rank']), (url(lang, 'compare'), S['nav_cmp'])] + [(url(lang, k), S['cat_' + v]) for k, v in HUBS.items()]
    tools = [(url(lang, k), v) for k, v in tools_menu(lang)]
    ins = [(url(lang, 'news'), n['n_nav']), (url(blog_l, 'blog'), n['i_nav']), (url(blog_l, 'blog') + 'rss.xml', 'RSS'),
           (url(lang, 'exchanges'), EX[lang]['nav']), (url(lang if lang in ABOUT else 'en', 'about'), n['about'])]
    cols = [(f[0], pop), (f[1], mk), (TR[lang]['x']['nav_tools'], tools), (n['i_nav'], ins)]
    if SOCIAL:
        cols.insert(0, (f[2], SOCIAL))
    return ('<div class="fcols">' + ''.join(f'<div><b>{esc(t)}</b>' + ''.join(f'<a href="{h}">{esc(l)}</a>' for h, l in items) + '</div>' for t, items in cols) + '</div>')


def shell(lang, p, title, desc, body, cfg, ver, jsonld=()):
    S = TR[lang]
    canon = SITE + url(lang, p)
    alts = ''.join(f'<link rel="alternate" hreflang="{TR[lg]["loc"]}" href="{SITE + url(lg, p)}">' for lg in ORDER if has_page(lg, p))
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + url("en", p)}">'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    X = S['x']
    blog_l = lang if lang in BLOG_LANGS else 'en'
    nav = (''.join(f'<a href="{url(lang, k)}" class="{"on" if k == p else ""}">{v}</a>' for k, v in ((None, S['nav_rank']), ('compare', S['nav_cmp'])))
           + f'<details class="dd"><summary class="{"on" if p in TOOLS or (p in CALCS and p not in ("exchanges", "news", "about")) or (p or "").startswith("habits") else ""}">{X["nav_tools"]}</summary><div>'
           + ''.join(f'<a href="{url(lang, k)}">{v}</a>' for k, v in tools_menu(lang)) + '</div></details>'
           + f'<a href="{url(lang, "exchanges")}" class="{"on" if p == "exchanges" else ""}">{EX[lang]["nav"]}</a>'
           + f'<a href="{url(lang, "news")}" class="{"on" if p == "news" else ""}">{NW[lang]["n_nav"]}</a>'
           + f'<a href="{url(blog_l, "blog")}" class="{"on" if (p or "").startswith("blog") else ""}">{NW[lang]["i_nav"]}</a>')
    i18n = dict(S['ui'], months=S['months'], intl=S['intl'])
    mnav = ''.join(f'<a href="{h}" class="{"on" if on else ""}"><span>{ic}</span>{esc(lb)}</a>' for h, ic, lb, on in (
        (url(lang), '◎', S['nav_rank'], p is None), (url(lang, 'news'), '▤', NW[lang]['n_nav'], p == 'news'),
        (url(lang, 'exchanges'), '₿', EX[lang]['nav'], p == 'exchanges'), (url(blog_l, 'blog'), '✎', NW[lang]['i_nav'], (p or '').startswith('blog'))))
    mnav += f'<button type="button" id="mmore"><span>☰</span>{esc(X["nav_tools"])}</button>'
    msheet = ('<div class="msheet" id="msheet" hidden>' + ''.join(f'<a href="{url(lang, k)}">{esc(v)}</a>' for k, v in
              [('compare', S['nav_cmp'])] + tools_menu(lang)) + '</div>')
    cfg = dict(cfg, lang=lang, base=BASE, prefix=url(lang).rstrip('/'), full=lang in FULL, topn=TOP_N,
               names={'gold': S['gold'], 'silver': S['silver']})
    return f"""<!DOCTYPE html>
<html lang="{S['loc']}" dir="{S['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:locale" content="{S['intl'].replace('-', '_')}">
<meta property="og:image" content="{SITE}/assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}/assets/og.jpg"><meta name="theme-color" content="#ffffff">
<script>(function(){{try{{var t=localStorage.getItem('wi_theme')}}catch(e){{}}if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';if(t==='dark'){{document.documentElement.dataset.theme='dark';document.querySelector('meta[name=theme-color]').content='#0e1014'}}}})()</script>
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{BASE}/assets/icon-192.png"><link rel="manifest" href="{BASE}/manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/style.css?v={ver['css']}">
{ld}
</head>
<body>
{strip(lang)}
<div class="top"><div class="in">
  <a class="logo" href="{url(lang)}">whatif<b>stack</b></a>
  <div class="gsearch">{SEARCH_ICON}<input id="gs" type="search" autocomplete="off" aria-label="search"><div class="gres" id="gres"></div></div>
  <nav class="nav">{nav}</nav>
  <button class="thm" id="thm" type="button" aria-label="theme"><span class="m">☾</span><span class="s">☀</span></button>
  {lang_menu(lang, p)}
</div></div>
<nav class="mnav">{mnav}</nav>{msheet}
<main class="wrap">
{body}
{footer_cols(lang)}<footer><span>{BRAND} · {S['by']} <a href="https://mytimebox.app/">Timebox</a> · {S['sources']} · <a href="{url(lang if lang in ABOUT else 'en', 'about')}">{NW[lang]['about']}</a></span><span>{S['disclaimer']}</span></footer>
<nav class="langs">{' · '.join(f'<a href="{url(lg, p) if has_page(lg, p) else url(lg)}" hreflang="{TR[lg]["loc"]}">{esc(TR[lg]["name"])}</a>' for lg in ORDER)}</nav>
</main>
<script>window.PAGE={json.dumps(cfg, ensure_ascii=False)};window.I18N={json.dumps(i18n, ensure_ascii=False)};</script>
<script src="{BASE}/assets/index.js?v={ver['index']}" defer></script>
<script src="{BASE}/assets/ref.js?v={ver['ref']}" defer></script>
<script src="{BASE}/assets/app.js?v={ver['js']}" defer></script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""


def tvw(kind, cfg, height):
    return f'<div class="tvw" style="height:{height}px" data-w="{kind}" data-cfg="{esc(json.dumps(cfg))}"></div>'


def calc_block(lang):
    u = TR[lang]['ui']
    return f"""<div id="calc">
<div class="card">
  <div class="seg modeseg" id="mode"><button data-v="dca" class="on">{u['x_mode_dca']}</button><button data-v="lump">{u['x_mode_lump']}</button></div>
  <div class="controls">
    <div><label class="f">{u['amount']}</label><div class="inp"><span>$</span><input id="amt" type="number" min="1" step="1" value="{AMOUNT}" aria-label="{u['amount']}"></div></div>
    <div id="freqbox"><label class="f">{u['freq']}</label><div class="seg" id="freq"><button data-v="d" class="on">{u['daily']}</button><button data-v="w">{u['weekly']}</button><button data-v="m">{u['monthly']}</button></div></div>
    <div><label class="f">{u['since']}</label><div class="inp"><select id="since" aria-label="{u['since']}"></select></div></div>
  </div>
  <label class="f">{u['onchart']}</label>
  <div class="chips" id="chips"></div>
  <div class="picker" id="picker"><div class="filter">{SEARCH_ICON}<input id="pq" type="search" autocomplete="off"></div><div class="pool" id="pool"></div></div>
</div>
<div class="hero" id="hero"></div>
<div class="card chartcard" id="chartcard"><div class="charthead"><h2>{u['chartTitle']}</h2><button class="toggle" id="logBtn">{u['log']}</button></div><div id="chart"></div><div class="tip" id="tip"></div></div>
<div class="card section"><div style="overflow-x:auto"><table class="rt" id="rt"></table></div>
<div class="share"><p id="shareText"></p><button class="btn ghost" id="copyBtn">{u['copy']}</button></div></div>
</div>"""


def row_html(aid, lang, n):
    a, m = A[aid], METRICS[aid]
    href = aurl(lang, aid)
    return (f'<tr><td class="l n hide-sm">{n}</td><td class="l"><a class="asset" href="{href}">{icon(a)}<span><span class="nm">{esc(nm(a, lang))}</span>'
            f'<span class="tk">{esc(a["tk"])}</span></span></a></td><td></td><td class="num" data-p="{aid}">{price(m["price"])}</td>'
            f'<td class="num {cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</td><td class="num hide-sm {cls(m["r1"])}">{pct(m["r1"])}</td>'
            f'<td class="num hide-sm {cls(m["r3"])}">{pct(m["r3"])}</td><td><span class="pill {cls(m["r5"])}">{pct(m["r5"])}</span></td>'
            f'<td class="hide-sm">{spark(m["spark"])}</td><td class="hide-sm"><a class="calc" href="{href}">→</a></td></tr>')


def table_block(lang, ids, title=None, interactive=True):
    u = TR[lang]['ui']
    head = ['#', u['name'], '', u['price'], u['chg'], u['d1'], u['d3'], u['d5'], u['spark'], '']
    hc = ['l n hide-sm', 'l', '', '', '', 'hide-sm', 'hide-sm', '', 'hide-sm', 'hide-sm']
    th = ''.join(f'<th class="{c}">{h}</th>' for h, c in zip(head, hc))
    rows = ''.join(row_html(aid, lang, k + 1) for k, aid in enumerate(ids))
    ttl = f'<h2>{title}</h2>' if title else ''
    if interactive:
        return f'{ttl}<div class="tw"><table class="mt"><thead id="mthead"><tr>{th}</tr></thead><tbody id="mt">{rows}</tbody></table><div id="mtmore"></div></div>'
    return f'{ttl}<div class="tw"><table class="mt"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>'


def best_by(key, ids):
    return sorted([i for i in ids if METRICS[i][key] is not None], key=lambda i: -METRICS[i][key])


def hl_card(lang, aid, label, key, sub):
    m = METRICS[aid]
    return (f'<a class="card" href="{aurl(lang, aid)}"><div class="k">{esc(label)}<span>{esc(A[aid]["tk"])}</span></div>'
            f'<div class="v {cls(m[key])}">{pct(m[key])}</div><div class="s">{esc(nm(A[aid], lang))} · {sub}</div>{spark(m["spark"], 220, 40)}</a>')


TEN = '<em>$10</em>'


def big_usd(v):
    if v is None:
        return '—'
    return f"${v/1e12:.2f}T" if v >= 1e12 else f"${v/1e9:.1f}B"


def mini_row(lang, aid, val_html):
    a = A[aid]
    return (f'<a class="mrow" href="{aurl(lang, aid)}">{icon(a)}<span class="mn"><b>{esc(a["tk"])}</b><span>{esc(nm(a, lang))}</span></span>'
            f'<span class="mp" data-p="{aid}">{price(METRICS[aid]["price"])}</span>{val_html}</a>')


def fng_gauge(v):
    import math
    if v is None:
        return ''
    ang = math.pi * (1 - v / 100)
    x, y = 100 + 78 * math.cos(ang), 100 - 78 * math.sin(ang)
    segs = ''
    cols = ['#e5484d', '#f59e0b', '#eab308', '#84cc16', '#14a44d']
    for k in range(5):
        a0, a1 = math.pi * (1 - k / 5), math.pi * (1 - (k + 1) / 5)
        x0, y0, x1, y1 = 100 + 78 * math.cos(a0), 100 - 78 * math.sin(a0), 100 + 78 * math.cos(a1), 100 - 78 * math.sin(a1)
        segs += f'<path d="M{x0:.1f} {y0:.1f} A78 78 0 0 1 {x1:.1f} {y1:.1f}" stroke="{cols[k]}" stroke-width="14" fill="none" stroke-linecap="butt"/>'
    return (f'<svg viewBox="0 0 200 110" width="180" height="99" id="fngsvg">{segs}'
            f'<circle id="fngdot" cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="#161a23" stroke-width="3"/></svg>')


def fng_label(lang, v):
    labs = TR[lang]['w']['fng_l'].split('|')
    return labs[0 if v < 25 else 1 if v < 45 else 2 if v < 56 else 3 if v < 76 else 4]


def home(lang, ver):
    S, w = TR[lang], TR[lang]['w']
    ids = ORDERED
    n = len(A)
    title, desc = S['home_title'], S['home_desc'].format(n=n)
    # --- hero with quick calculator
    qopts = ''.join(f'<option value="{aid}"{" selected" if aid == "btc" else ""}>{esc(nm(A[aid], lang))} ({esc(A[aid]["tk"])})</option>' for aid in ids[:120])
    yrs = ''.join(f'<button data-y="{y}" class="{"on" if y == 5 else ""}">{y}</button>' for y in (1, 3, 5, 10))
    b5 = simulate('btc', END_I - 60) if 'btc' in A else None
    cta_ref = f'<a class="btn" id="ctaBuy" href="{url(lang, "compare")}">{w["cta"]}</a>'
    hero = (f'<section class="herox"><div class="hx"><h1>{S["home_h1"].format(ten=TEN)}</h1><p class="lead">{S["home_lead"].format(n=n)}</p>'
            f'<div class="hxbtn">{cta_ref}<a class="btn ghost" href="{url(lang, "compare")}">{S["nav_cmp"]}</a></div></div>'
            f'<div class="card qcalc" id="qcalc"><div class="qt">{w["quick"]}</div>'
            f'<div class="qrow"><label class="f">{w["q_asset"]}<div class="inp"><select id="qa">{qopts}</select></div></label>'
            f'<label class="f">{S["ui"]["amount"]}<div class="inp"><span>$</span><input id="qm" type="number" min="1" value="{AMOUNT}"></div></label></div>'
            f'<label class="f">{w["q_years"]}</label><div class="seg" id="qy">{yrs}</div>'
            f'<div class="qres"><div class="k">{w["q_have"]}</div><div class="v" id="qv">{usd(b5["val"]) if b5 else "—"}</div>'
            f'<div class="s" id="qs">{pct(b5["roi"]) if b5 else ""} · {w["q_inv"]} {usd(b5["inv"]) if b5 else ""}</div><div id="qsp"></div></div>'
            f'<a class="calc" id="qmore" href="{aurl(lang, "btc")}">{w["q_more"]}</a></div></section>')
    # --- market widgets
    fv = (G.get('fng') or [None])[0]
    fhist = G.get('fng') or []
    def fh(k, lab):
        return f'<div class="fh"><span>{lab}</span><b>{fhist[k]}</b></div>' if len(fhist) > k else ''
    dom = G.get('btc_dom'); edom = G.get('eth_dom')
    w_mcap = (f'<div class="card wd"><div class="wt">{w["mcap"]}</div><div class="wv" id="gmcap">{big_usd(G.get("mcap"))}</div>'
              f'<div class="ws"><span class="{cls((G.get("mcap_chg") or 0) / 100)}" id="gmchg">{pct((G.get("mcap_chg") or 0) / 100) if G.get("mcap_chg") is not None else "—"}</span> · {w["vol"]} <b id="gvol">{big_usd(G.get("vol"))}</b></div>'
              f'{spark(METRICS["btc"]["spark"], 260, 44) if "btc" in A else ""}</div>')
    w_dom = (f'<div class="card wd"><div class="wt">{w["dom"]}</div><div class="wv" id="gdom">{f"{dom:.1f}%" if dom else "—"}</div>'
             f'<div class="dbar"><i style="width:{dom or 0:.1f}%;background:#f7931a"></i><i style="width:{edom or 0:.1f}%;background:#627eea"></i></div>'
             f'<div class="ws">BTC {f"{dom:.1f}%" if dom else "—"} · ETH {f"{edom:.1f}%" if edom else "—"}</div></div>')
    w_fng = (f'<div class="card wd fng"><div class="wt">{w["fng"]}</div><div class="fgw">{fng_gauge(fv)}<div class="fgv"><b id="fngv">{fv if fv is not None else "—"}</b>'
             f'<span id="fngl">{fng_label(lang, fv) if fv is not None else ""}</span></div></div>'
             f'<div class="fhs">{fh(1, w["yday"])}{fh(7, w["week"])}{fh(30, w["month"])}</div></div>')
    trend = [s.lower() for s in (G.get('trending') or []) if s.lower() in A][:5]
    if not trend:
        trend = [i for i in ids if A[i]['cat'] == 'crypto'][:5]
    w_tr = (f'<div class="card wd"><div class="wt">🔥 {w["trending"]}</div>' +
            ''.join(mini_row(lang, i, f'<span class="mc {cls(METRICS[i]["chg"])}" data-c="{i}">{pct(METRICS[i]["chg"])}</span>') for i in trend) + '</div>')
    movers = [i for i in ids if METRICS[i]['chg'] is not None and ORD[i] < 400]
    up = sorted(movers, key=lambda i: -METRICS[i]['chg'])[:6]
    dn = sorted(movers, key=lambda i: METRICS[i]['chg'])[:6]
    w_up = f'<div class="card wd"><div class="wt">🚀 {w["gainers"]}</div>' + ''.join(mini_row(lang, i, f'<span class="mc good" data-c="{i}">{pct(METRICS[i]["chg"])}</span>') for i in up) + '</div>'
    w_dn = f'<div class="card wd"><div class="wt">📉 {w["losers"]}</div>' + ''.join(mini_row(lang, i, f'<span class="mc bad" data-c="{i}">{pct(METRICS[i]["chg"])}</span>') for i in dn) + '</div>'
    bat = [i for i in ('btc', 'eth', 'nvda', 'aapl', 'spy', 'qqq', 'gold', 'silver') if i in A and METRICS[i]['r5'] is not None]
    bat.sort(key=lambda i: -METRICS[i]['r5'])
    mx = max([simulate(i, END_I - 60)['val'] for i in bat] or [1])
    rows = ''
    for i in bat:
        r = simulate(i, END_I - 60)
        rows += (f'<a class="brow" href="{aurl(lang, i)}"><span class="bn">{icon(A[i])}{esc(nm(A[i], lang))}</span>'
                 f'<span class="bb"><i style="width:{max(2, r["val"] / mx * 100):.1f}%" class="{cls(r["roi"])}"></i></span><b>{usd(r["val"])}</b></a>')
    inv5 = usd(simulate(bat[0], END_I - 60)['inv']) if bat else ''
    w_bat = f'<div class="card wd battle"><div class="wt">⚔️ {w["battle"]}</div><div class="ws">{w["q_inv"]}: {inv5}</div>{rows}</div>'
    X_ = S['x']
    banner = (f'<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div>'
              f'<a class="btn" id="ctaBuy2" href="{url(lang, "compare")}">{w["cta"]} →</a></section>')
    # DCA leaders cards (as before)
    cards = []
    b1, b5l = best_by('r1', ids), best_by('r5', ids)
    bc = best_by('r1', [i for i in ids if A[i]['cat'] == 'crypto' and ORD[i] < 60])
    if b1: cards.append(hl_card(lang, b1[0], S['hl1'], 'r1', S['sub1']))
    if b5l: cards.append(hl_card(lang, b5l[0], S['hl5'], 'r5', S['sub5']))
    if bc: cards.append(hl_card(lang, bc[0], S['hlc'], 'r1', S['sub1']))
    for aid in ('btc', 'spy', 'gold'):
        if aid in A and len(cards) < 4:
            cards.append(hl_card(lang, aid, nm(A[aid], lang), 'r5', S['sub5']))
    filt = f'<div class="toolbar"><div class="filter">{SEARCH_ICON}<input id="flt" type="search" autocomplete="off"></div></div>'
    body = (hero + f'<div class="wgrid">{w_mcap}{w_dom}{w_fng}{w_tr}</div>'
            f'<div class="wgrid3">{w_up}{w_dn}{w_bat}</div>{banner}{habits_strip(lang)}{poll_block(lang)}{poly_block(lang)}'
            f'<section class="section"><div class="hl">{"".join(cards)}</div></section>'
            f'<div class="tabs" id="tabs"></div>{filt}{table_block(lang, ids[:100])}'
            f'<section class="card section faq"><h2>{S["faq"]}</h2><details open><summary>{esc(S["q3"])}</summary><p>{esc(S["a3"])}</p></details></section>')
    jsonld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": BRAND, "url": SITE + url(lang),
               "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "inLanguage": S['loc'],
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}]
    return shell(lang, None, title, desc, body, dict(home=True), ver, jsonld)


def compare(lang, ver):
    S = TR[lang]
    sel = [i for i in ('btc', 'nvda', 'gold', 'spy', 'eth') if i in A]
    body = f'<h1>{S["cmp_h1"]}</h1><p class="lead">{S["cmp_lead"]}</p>{calc_block(lang)}'
    return shell(lang, 'compare', S['cmp_title'], S['cmp_desc'], body, dict(sel=sel, since=f"{END_I // 12 - 5}-01"), ver)


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
    S, u = TR[lang], TR[lang]['ui']
    a, m = A[aid], METRICS[aid]
    n, tk = nm(a, lang), a['tk']
    since = default_since(aid)
    r = simulate(aid, ym2i(since))
    since_l = mlabel(i2ym(r['frm']), lang, long=True)
    upd = mlabel(END, lang, long=True)
    b1 = next(bench(aid))
    s5 = END_I - 60
    ra5 = simulate(aid, max(s5, ym2i(a['start'])))
    rb5 = simulate(b1, max(s5, ym2i(A[b1]['start'])))
    s0 = ym2i(a['start'])
    stats = []
    for yrs, key in ((1, 'p1'), (3, 'p3'), (5, 'p5'), (10, 'p10')):
        st = END_I - yrs * 12
        if st >= s0:
            stats.append((S[key], simulate(aid, st)))
    rows = stats + [(S['p_since'].format(since=mlabel(i2ym(s0), lang)), simulate(aid, s0))]
    show = stats if len(stats) >= 2 else rows[-4:]
    X = S['x']
    lumps = []
    for yrs, key in ((1, 'p1'), (3, 'p3'), (5, 'p5'), (10, 'p10')):
        st = END_I - yrs * 12
        if st >= s0 and st - s0 < len(A[aid]['p']):
            k = A[aid]['p'][-1] / A[aid]['p'][st - s0]
            lumps.append((S[key], 1000 * k, k - 1))
    lump_cards = ''.join(f'<div class="card stat"><div class="k">{X["lump"].format(p=lab)}</div><div class="v">{usd(v)}</div>'
                         f'<div class="s {cls(r)}">{pct(r)}</div></div>' for lab, v, r in lumps)
    stat_cards = ''.join(
        f'<div class="card stat"><div class="k">{S["stat"].format(p=lab)}</div><div class="v">{usd(x["val"])}</div>'
        f'<div class="s {cls(x["roi"])}">{pct(x["roi"])} <span class="muted">· {S["invested_lc"]} {usd(x["inv"])}</span></div></div>' for lab, x in show)
    ptable = (f'<table class="rt"><tr><th>{S["period"]}</th><th>{u["invested"]}</th><th>{S["now"]}</th><th>{S["result"]}</th></tr>' +
              ''.join(f'<tr><td class="a">{lab}</td><td>{usd(x["inv"])}</td><td>{usd(x["val"])}</td><td class="{cls(x["roi"])}">{pct(x["roi"])}</td></tr>' for lab, x in rows) +
              '</table>')
    f = dict(name=n, tk=tk, since=since_l, inv=usd(r['inv']), val=usd(r['val']), roi=pct(r['roi']), n=len(A) - 1, upd=upd,
             bench=nm(A[b1], lang), ra=pct(ra5['roi']), rb=pct(rb5['roi']), r1=pct(m['r1']), r5=pct(m['r5']), ten=TEN)
    title, desc = S['a_title'].format(**f), S['a_desc'].format(**f)
    fe = dict(f, name=esc(n), roi=f'<span class="{cls(r["roi"])}">{pct(r["roi"])}</span>')
    faq = [(S['q1'].format(**f), S['a1'].format(**f)), (S['q2'].format(**f), S['a2'].format(**f)),
           (S['q4'].format(**f), S['a4'].format(**f)), (S['q3'], S['a3'])]
    if m['r1'] is None or m['r5'] is None:
        faq.pop(2)
    if lumps:
        lab, v, r5_ = lumps[min(2, len(lumps) - 1)]
        faq.insert(1, (X['q5'].format(name=n, p=lab), X['a5'].format(name=n, p=lab, v=usd(v), roi=pct(r5_))))
    sim = [i for i in ORDERED if A[i]['cat'] == a['cat'] and i != aid]
    if a.get('sector'):
        same = [i for i in sim if A[i].get('sector') == a['sector']]
        sim = same + [i for i in sim if i not in same]
    sim = sim[:10]
    cat = S['cat_' + a['cat']]
    crumbs = f'<nav class="crumbs"><a href="{url(lang)}">{S["nav_rank"]}</a> / {esc(cat)} / {esc(n)}</nav>'
    badges = f'<span class="badge">{esc(tk)}</span> <span class="badge">{esc(cat)}</span>' + (f' <span class="badge">{esc(a["sector"])}</span>' if a.get('sector') else '')
    head = (f'{crumbs}<div class="ahead">{icon(a, True)}<div><h1>{S["a_h1"].format(**fe)}</h1><div style="margin-top:4px">{badges}</div></div>'
            f'<div class="price"><span class="v" data-p="{aid}">{price(m["price"])}</span><span class="pill {cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</span><span id="buyslot" data-id="{aid}"></span></div></div>')
    w = S['w']
    loc = TV_LOC.get(lang, 'en')
    tv = (f'<section class="card section tvcard"><div class="charthead"><h2>{w["live_chart"]} · {esc(tk)}</h2><span class="livebadge"><i></i>{w["live"]}</span></div>'
          + tvw('advanced-chart', dict(autosize=True, symbol=tv_symbol(a), interval='D', timezone='Etc/UTC', theme='light', style='1', locale=loc,
                                       allow_symbol_change=False, hide_side_toolbar=True, withdateranges=True, save_image=False), 480) + '</section>')
    tech_news = (f'<div class="cols2 section"><section class="card"><h2>{X["tech"]} · {esc(tk)}</h2>'
                 + tvw('technical-analysis', dict(interval='1D', width='100%', height='100%', isTransparent=True, symbol=tv_symbol(a), showIntervalTabs=True,
                                                  displayMode='single', locale=loc, colorTheme='light'), 430)
                 + f'</section><section class="card"><h2>{X["news"]} · {esc(tk)}</h2>'
                 + tvw('timeline', dict(feedMode='symbol', symbol=tv_symbol(a), isTransparent=True, displayMode='regular', width='100%', height='100%',
                                        colorTheme='light', locale=loc), 430) + '</section></div>')
    if a['cat'] in ('stock', 'etf'):
        tech_news += (f'<div class="cols2 section"><section class="card"><h2>{X["fund"]} · {esc(tk)}</h2>'
                      + tvw('financials', dict(isTransparent=True, displayMode='regular', width='100%', height='100%', colorTheme='light', symbol=tv_symbol(a), locale=loc), 520)
                      + f'</section><section class="card"><h2>{X["prof"]} · {esc(tk)}</h2>'
                      + tvw('symbol-profile', dict(width='100%', height='100%', isTransparent=True, colorTheme='light', symbol=tv_symbol(a), locale=loc), 520) + '</section></div>')
    body = (f'{head}<p class="lead" style="margin-top:10px">{S["a_lead"].format(**fe)}</p>{tv}<div class="stats">{stat_cards}</div><div class="stats">{lump_cards}</div>{calc_block(lang)}{tech_news}'
            f'<div class="cols2 section"><section class="card"><h2>{S["a_periods"].format(**fe)}</h2>{ptable}</section>'
            f'<section class="card faq"><h2>{S["faq"]}</h2>' + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q, x in faq) + '</section></div>'
            f'<section class="section">{table_block(lang, sim, S["a_similar"] + ": " + esc(cat), interactive=False)}</section>'
            f'<p class="note">{esc(S["about"].format(**f))}</p>')
    jsonld = [{"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": S['loc'],
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": x}} for q, x in faq]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": BRAND, "item": SITE + url(lang)},
                  {"@type": "ListItem", "position": 2, "name": n, "item": SITE + url(lang, aid)}]}]
    sel = [aid] + list(bench(aid))[:2]
    return shell(lang, aid, title, desc, body, dict(sel=sel, since=since, asset=aid), ver, jsonld)



# ---------------- hubs, tools ----------------
# ---------------- habits -> money ----------------
HSLUG = {'coffee': 'coffee', 'cig': 'cigarettes', 'delivery': 'food-delivery', 'subs': 'subscriptions', 'save': 'save-daily'}
HASSETS = [i for i in ('spy', 'qqq', 'btc', 'gold') if i in A]
HICON = {'coffee': '☕', 'cig': '🚬', 'delivery': '🍔', 'subs': '📺', 'save': '🐷'}
CCY_SYM = {'USD': '$', 'EUR': '€', 'UAH': '₴', 'PLN': 'zł', 'BRL': 'R$', 'TRY': '₺', 'RUB': '₽', 'IDR': 'Rp', 'VND': '₫', 'THB': '฿',
           'INR': '₹', 'JPY': '¥', 'KRW': '₩', 'CNY': '¥', 'AED': 'AED', 'PHP': '₱'}
CCY_SUFFIX = {'PLN', 'UAH', 'RUB', 'VND', 'AED'}


def hccy(lang):
    c = LOCAL_CCY.get(lang, 'usd')
    code = c[3:] if c.startswith('fx:') else 'USD'
    rate = 1.0 if code == 'USD' else FX.get('rates', {}).get(code)
    return (code, rate) if rate else ('USD', 1.0)


def money(v, code):
    s = f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.2f}"
    sym = CCY_SYM.get(code, code)
    return f"{s} {sym}" if code in CCY_SUFFIX else f"{sym}{s}"


def hsim(lang, sc, years, aid, price=None, times=None, per=None):
    code, rate = hccy(lang)
    t0, p0 = HUNITS[sc]
    price = HPRICE[lang][HSCEN.index(sc)] if price is None else price
    times, per = times or t0, per or p0
    daily_usd = price * times / {'d': 1, 'w': 7, 'm': 30.4375}[per] / rate
    r = simulate(aid, END_I - years * 12, daily_usd)
    return dict(inv=r['inv'] * rate, val=r['val'] * rate, roi=r['roi'], code=code)


def habit_page(lang, sc, ver):
    S, h = TR[lang], HB[lang]
    phrase, h1, d = h[sc]
    code, rate = hccy(lang)
    t0, p0 = HUNITS[sc]
    price = HPRICE[lang][HSCEN.index(sc)]
    yl = {1: S['p1'], 3: S['p3'], 5: S['p5'], 10: S['p10']}
    r = hsim(lang, sc, 10, 'spy')
    sent = h['res'].format(y=yl[10], habit=phrase[:1].upper() + phrase[1:] if h['res'].startswith('{habit}') else phrase, spent=money(r['inv'], code), asset=nm(A['spy'], lang), val=money(r['val'], code), roi=pct(r['roi']))
    per_l = h['per'].split('|')
    per_opts = ''.join(f'<option value="{v}"{" selected" if v == p0 else ""}>{esc(t)}</option>' for v, t in zip('dwm', per_l))
    aseg = ''.join(f'<button data-v="{i}"{" class=on" if i == "spy" else ""}>{esc(nm(A[i], lang))}</button>' for i in HASSETS)
    yseg = ''.join(f'<button data-v="{y}"{" class=on" if y == 10 else ""}>{esc(yl[y])}</button>' for y in (1, 3, 5, 10))
    rows = ''
    for i in HASSETS:
        x = hsim(lang, sc, 10, i)
        rows += (f'<tr data-a="{i}"><td class="name"><a href="{aurl(lang, i)}">{icon(A[i])}{esc(nm(A[i], lang))}</a></td>'
                 f'<td class="mono">{money(x["inv"], code)}</td><td class="mono"><b>{money(x["val"], code)}</b></td><td class="mono {cls(x["roi"])}">{pct(x["roi"])}</td></tr>')
    u = S['ui']
    calc = (f'<div class="card hcalc" id="hcalc" data-sc="{sc}">'
            f'<div class="hrow"><label class="f">{h["price"]}<div class="inp"><input id="hp" type="number" min="0" step="any" value="{price:g}"><span class="muted">{CCY_SYM.get(code, code)}</span></div></label>'
            f'<label class="f">{h["times"]}<div class="inp"><input id="ht" type="number" min="0" step="any" value="{t0}" style="max-width:70px"><select id="hper">{per_opts}</select></div></label></div>'
            f'<div class="hrow"><div class="f">{h["inv"]}<div class="seg" id="has">{aseg}</div></div><div class="f">{h["yrs"]}<div class="seg" id="hy">{yseg}</div></div></div>'
            f'<div class="hres"><div class="v good" id="hval">{money(r["val"], code)}</div><p id="hsent">{esc(sent)}</p></div>'
            f'<h2>{h["tbl"]}</h2><div class="tw"><table class="mt"><thead><tr><th style="text-align:left">{u["name"]}</th><th>{u["invested"]}</th><th>{u["value"]}</th><th>%</th></tr></thead><tbody id="htb">{rows}</tbody></table></div>'
            f'<p class="muted" style="font-size:13px">{h["note"]}</p></div>')
    others = ''.join(f'<a class="card hcard" href="{url(lang, "habits/" + HSLUG[k])}"><span>{HICON[k]}</span><b>{esc(HB[lang][k][1])}</b></a>' for k in HSCEN if k != sc)
    body = (f'<div class="crumbs"><a href="{url(lang, "habits")}">{h["nav"]}</a></div><h1>{HICON[sc]} {esc(h1)}</h1><p class="lead">{esc(d)}</p>{calc}'
            f'<section class="section"><h2>{h["other"]}</h2><div class="hgrid">{others}</div></section>'
            f'<section class="banner section"><div><b>{esc(h["cta"])}</b></div><a class="btn" href="{url(lang, "compare")}">{esc(h["cta"])} →</a></section>')
    cfg = dict(habit=dict(sc=sc, code=code, rate=rate, res=h['res'], phrase=phrase, yl={str(k): v for k, v in yl.items()}, assets=HASSETS))
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": h1, "acceptedAnswer": {"@type": "Answer", "text": sent}}]}
    return shell(lang, 'habits/' + HSLUG[sc], f'{h1} | {BRAND}', d, body, cfg, ver, [faq])


def tools_menu(lang):
    t = TT[lang]
    items = [('habits', HB[lang]['nav']), ('millionaire', t['g_nav']), ('compound-interest', t['c_nav'])]
    if CPI['c']:
        items.append(('inflation', t['i_nav']))
    items += [('converter', HCONV[lang]), ('ath', t['a_nav']), ('bitcoin-halving', t['v_nav'])]
    return items


def nice(v):
    """Round to a friendly number (1, 2, 5 x 10^n)."""
    if v <= 0:
        return 0
    e = 10 ** math.floor(math.log10(v))
    return min((1, 2, 5, 10), key=lambda k: abs(k * e - v)) * e


def cagr(aid, years=10):
    a = A.get(aid)
    if not a or len(a['p']) < years * 12 + 1:
        return None
    return (a['p'][-1] / a['p'][-1 - years * 12]) ** (1 / years) - 1


GASSETS = [i for i in ('spy', 'qqq', 'gold') if cagr(i)]   # no Bitcoin: extrapolating its past 10-year return for decades would be misleading


def fv(p0, pmt, r, n_years):
    rm, n = (1 + r) ** (1 / 12) - 1, n_years * 12
    if abs(rm) < 1e-12:
        return p0 + pmt * n
    g = (1 + rm) ** n
    return p0 * g + pmt * (g - 1) / rm


def need_pmt(goal, p0, r, n_years):
    rm, n = (1 + r) ** (1 / 12) - 1, n_years * 12
    if abs(rm) < 1e-12:
        return max(0, (goal - p0) / n)
    g = (1 + rm) ** n
    return max(0, (goal - p0 * g) * rm / (g - 1))


def pct0(v):
    return f"{v * 100:.1f}%"


def rate_seg(lang, default='spy'):
    t = TT[lang]
    b = ''.join(f'<button data-r="{cagr(i):.4f}"{" class=on" if i == default else ""} data-a="{i}">{esc(nm(A[i], lang))} · {pct0(cagr(i))}</button>' for i in GASSETS)
    return (f'<div class="f">{t["g_ret"]}<div class="seg" id="gseg">{b}<button data-r="custom">{t["g_custom"]}</button></div></div>'
            f'<label class="f" id="gcw" hidden>%<div class="inp"><input id="gr" type="number" step="0.1" value="{cagr(default) * 100:.1f}"></div></label>')


def calc_page(lang, slug, ver):
    S, t, u = TR[lang], TT[lang], TR[lang]['ui']
    code, rate = hccy(lang)
    sym = CCY_SYM.get(code, code)
    inp = lambda i, lab, v: f'<label class="f">{lab}<div class="inp"><input id="{i}" type="number" min="0" step="any" value="{v:.0f}"><span class="muted">{sym}</span></div></label>'
    yrs = lambda v: f'<label class="f">{t["g_years"]}<div class="inp"><input id="gy" type="number" min="1" max="60" step="1" value="{v}"></div></label>'
    r0 = cagr('spy')
    cfg = dict(calc=dict(kind=slug, code=code, yr=t['yr'], names={i: nm(A[i], lang) for i in GASSETS}))
    if slug == 'millionaire':
        goal, p0, n = nice(1e6 * rate), 0, 20
        pmt = need_pmt(goal, p0, r0, n)
        sent = t['g_res'].format(goal=money(goal, code), n=n, yr=t['yr'], pmt=money(pmt, code), asset=nm(A['spy'], lang), r=pct0(r0))
        h1, d, cfg['calc']['res'] = t['g_h1'], t['g_d'], t['g_res']
        form = (f'<div class="hrow">{inp("gg", t["g_goal"], goal)}{yrs(n)}{inp("gp", t["g_have"], p0)}</div><div class="hrow">{rate_seg(lang)}</div>'
                f'<div class="hres"><div class="muted">{t["g_need"]}</div><div class="v good" id="gv">{money(pmt, code)}</div><p id="gsent">{esc(sent)}</p></div>')
    else:
        p0, pmt, n = nice(1000 * rate), nice(100 * rate), 20
        v = fv(p0, pmt, r0, n)
        inv = p0 + pmt * n * 12
        sent = t['c_res'].format(n=n, yr=t['yr'], fv=money(v, code), inv=money(inv, code), gain=money(v - inv, code))
        h1, d, cfg['calc']['res'] = t['c_h1'], t['c_d'], t['c_res']
        form = (f'<div class="hrow">{inp("gp", t["c_init"], p0)}{inp("gm", t["c_month"], pmt)}{yrs(n)}</div><div class="hrow">{rate_seg(lang)}</div>'
                f'<div class="hres"><div class="v good" id="gv">{money(v, code)}</div><p id="gsent">{esc(sent)}</p></div>')
    chart = (f'<div class="gbar" id="gbar"><i class="a" style="width:50%"></i><i class="b" style="width:50%"></i></div>'
             f'<div class="glg"><span><i class="a"></i>{t["g_inv"]}</span><span><i class="b"></i>{t["g_gain"]}</span></div>')
    other = 'compound-interest' if slug == 'millionaire' else 'millionaire'
    body = (f'<h1>{esc(h1)}</h1><p class="lead">{esc(d)}</p><div class="card hcalc" id="gcalc">{form}{chart}<p class="muted" style="font-size:13px">{t["g_note"]}</p></div>'
            f'<section class="section"><div class="hgrid"><a class="card hcard" href="{url(lang, other)}"><span>{"📈" if other == "compound-interest" else "🎯"}</span><b>{esc(t["c_h1"] if other == "compound-interest" else t["g_h1"])}</b></a>'
            f'<a class="card hcard" href="{url(lang, "habits")}"><span>☕</span><b>{esc(HB[lang]["h1"])}</b></a><a class="card hcard" href="{url(lang, "compare")}"><span>⇅</span><b>{esc(S["cmp_h1"])}</b></a></div></section>')
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": h1, "acceptedAnswer": {"@type": "Answer", "text": sent}}]}
    return shell(lang, slug, f'{h1} | {BRAND}', d, body, cfg, ver, [faq])


CPI_LANG = {'uk': 'UKR', 'en': 'USA', 'es': 'ESP', 'pt': 'BRA', 'de': 'DEU', 'fr': 'FRA', 'it': 'ITA', 'pl': 'POL', 'tr': 'TUR', 'nl': 'NLD',
            'ru': 'RUS', 'id': 'IDN', 'vi': 'VNM', 'th': 'THA', 'hi': 'IND', 'ja': 'JPN', 'ko': 'KOR', 'zh': 'CHN', 'ar': 'ARE', 'fil': 'PHL'}
CPI_CCY = {'USA': ('US', 'USD'), 'UKR': ('UA', 'UAH'), 'ESP': ('ES', 'EUR'), 'BRA': ('BR', 'BRL'), 'DEU': ('DE', 'EUR'), 'FRA': ('FR', 'EUR'),
           'ITA': ('IT', 'EUR'), 'POL': ('PL', 'PLN'), 'TUR': ('TR', 'TRY'), 'NLD': ('NL', 'EUR'), 'RUS': ('RU', 'RUB'), 'IDN': ('ID', 'IDR'),
           'VNM': ('VN', 'VND'), 'THA': ('TH', 'THB'), 'IND': ('IN', 'INR'), 'JPN': ('JP', 'JPY'), 'KOR': ('KR', 'KRW'), 'CHN': ('CN', 'CNY'),
           'ARE': ('AE', 'AED'), 'PHL': ('PH', 'PHP'), 'GBR': ('GB', 'GBP'), 'MEX': ('MX', 'MXN'), 'ARG': ('AR', 'ARS'), 'KAZ': ('KZ', 'KZT'),
           'CAN': ('CA', 'CAD'), 'AUS': ('AU', 'AUD')}


def infl(c, y0, amt):
    d = CPI['c'].get(c, {})
    if not d:
        return None
    last = max(int(y) for y in d)
    f = 1.0
    for y in range(y0 + 1, last + 1):
        f *= 1 + d.get(str(y), 0) / 100
    return dict(now=amt * f, f=f, last=last)


def inflation_page(lang, ver):
    t = TT[lang]
    c = CPI_LANG.get(lang, 'USA')
    c = c if c in CPI['c'] else 'USA' if 'USA' in CPI['c'] else next(k for k in CPI['c'] if k in CPI_CCY)
    code = CPI_CCY[c][1]
    rate = 1.0 if code == 'USD' else FX.get('rates', {}).get(code, 1.0)
    amt = 100 if rate < 100 else 10000 if rate < 5000 else 100000
    y0 = 2010
    r = infl(c, y0, amt)
    sent = t['i_res'].format(amt=money(amt, code), y0=y0, now=money(r['now'], code), pct=pct0(r['f'] - 1), lost=pct0(1 - 1 / r['f']))
    opts = ''.join(f'<option value="{k}"{" selected" if k == c else ""} data-cc="{CPI_CCY[k][0]}" data-ccy="{CPI_CCY[k][1]}">{CPI_CCY[k][1]} · {k}</option>' for k in CPI['c'] if k in CPI_CCY)
    years = ''.join(f'<option{" selected" if y == y0 else ""}>{y}</option>' for y in range(r['last'] - 1, 1969, -1))
    body = (f'<h1>{esc(t["i_h1"])}</h1><p class="lead">{esc(t["i_d"])}</p><div class="card hcalc" id="icalc">'
            f'<div class="hrow"><label class="f">{t["i_country"]}<div class="inp"><select id="ic">{opts}</select></div></label>'
            f'<label class="f">{t["i_amount"]}<div class="inp"><input id="ia" type="number" min="0" step="any" value="{amt}"><span class="muted" id="isym">{CCY_SYM.get(code, code)}</span></div></label>'
            f'<label class="f">{t["i_year"]}<div class="inp"><select id="iy">{years}</select></div></label></div>'
            f'<div class="hres"><div class="v bad" id="iv">{money(r["now"], code)}</div><p id="is">{esc(sent)}</p></div>'
            f'<p class="muted" style="font-size:13px" id="isrc">{t["i_src"].format(y=r["last"])}</p></div>'
            f'<section class="section"><div class="hgrid"><a class="card hcard" href="{url(lang, "compound-interest")}"><span>📈</span><b>{esc(t["c_h1"])}</b></a>'
            f'<a class="card hcard" href="{url(lang, "millionaire")}"><span>🎯</span><b>{esc(t["g_h1"])}</b></a><a class="card hcard" href="{url(lang, "habits")}"><span>☕</span><b>{esc(HB[lang]["h1"])}</b></a></div></section>')
    cfg = dict(infl=dict(res=t['i_res'], src=t['i_src'], c={k: v for k, v in CPI['c'].items() if k in CPI_CCY}))
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": t['i_h1'], "acceptedAnswer": {"@type": "Answer", "text": sent}}]}
    return shell(lang, 'inflation', f'{t["i_h1"]} | {BRAND}', t['i_d'], body, cfg, ver, [faq])


def ath_ok(a):
    ath = a.get('ath')
    return bool(ath) and ath >= max(a['p']) * 0.8 and a.get('price', a['p'][-1]) <= ath * 1.05


def btc_crashes():
    a = A['btc']
    p, s0 = a['p'], ym2i(a['start'])
    out, peak_i, i = [], 0, 1
    while i < len(p):
        if p[i] >= p[peak_i]:
            peak_i = i
            i += 1
            continue
        # in a drawdown from peak_i: find bottom and recovery
        j, bot = i, i
        while j < len(p) and p[j] < p[peak_i]:
            if p[j] < p[bot]:
                bot = j
            j += 1
        dd = p[bot] / p[peak_i] - 1
        if dd <= -0.4:
            out.append(dict(peak=i2ym(s0 + peak_i), pp=p[peak_i], bot=i2ym(s0 + bot), bp=p[bot], dd=dd, rec=(j - peak_i) if j < len(p) else None))
        if j >= len(p):
            break
        peak_i, i = j, j + 1
    return out


def ath_page(lang, ver):
    t, u = TT[lang], TR[lang]['ui']
    ids = [i for i in ORDERED if A[i]['cat'] == 'crypto' and A[i].get('rank') and ath_ok(A[i])]
    ids.sort(key=lambda i: A[i]['rank'])
    rows = ''
    for i in ids[:100]:
        a = A[i]
        pr = a.get('price', a['p'][-1])
        dd, back = pr / a['ath'] - 1, a['ath'] / pr - 1
        rows += (f'<tr><td class="rank">{a["rank"]}</td><td class="name"><a href="{aurl(lang, i)}">{icon(a)}<b>{esc(nm(a, lang))}</b> <span class="muted">{esc(a["tk"])}</span></a></td>'
                 f'<td class="mono" data-p="{i}">{price(pr)}</td><td class="mono {cls(dd)}"><b>{pct(dd)}</b></td><td class="mono hide-sm">{price(a["ath"])}</td>'
                 f'<td class="hide-sm">{esc(a.get("athd") or "")}</td><td class="mono good">{pct(back)}</td></tr>')
    table = (f'<div class="tw"><table class="mt"><thead><tr><th>#</th><th style="text-align:left">{u["name"]}</th><th>{u["price"]}</th><th>{t["a_from"]}</th>'
             f'<th class="hide-sm">{t["a_ath"]}</th><th class="hide-sm">{t["a_date"]}</th><th>{t["a_back"]}</th></tr></thead><tbody>{rows}</tbody></table></div>')
    cr = ''
    for c in reversed(btc_crashes()):
        cr += (f'<tr><td>{mlabel(c["peak"], lang)}</td><td class="mono">{price(c["pp"])}</td><td>{mlabel(c["bot"], lang)}</td><td class="mono">{price(c["bp"])}</td>'
               f'<td class="mono bad"><b>{pct(c["dd"])}</b></td><td>{(str(c["rec"]) + " " + t["h_mo"]) if c["rec"] else t["h_not"]}</td></tr>')
    hist = (f'<section class="card section"><h2>{t["h_hist"]}</h2><div class="tw"><table class="mt"><thead><tr><th style="text-align:left">{t["h_peak"]}</th><th></th>'
            f'<th style="text-align:left">{t["h_bottom"]}</th><th></th><th>{t["h_drop"]}</th><th>{t["h_rec"]}</th></tr></thead><tbody>{cr}</tbody></table></div>'
            f'<p class="muted" style="font-size:13px">{t["h_note"]}</p></section>')
    b = A.get('btc')
    lead = ''
    if b and ath_ok(b):
        pr = b.get('price', b['p'][-1])
        lead = (f'<div class="hl"><a class="card" href="{aurl(lang, "btc")}"><div class="t">Bitcoin · {t["a_from"]}</div><div class="v bad">{pct(pr / b["ath"] - 1)}</div>'
                f'<div class="s">{t["a_ath"]}: {price(b["ath"])} · {esc(b.get("athd") or "")}</div></a>'
                f'<a class="card" href="{url(lang, "bitcoin-halving")}"><div class="t">{t["v_nav"]}</div><div class="v">⏳</div><div class="s">{t["v_next"]} →</div></a></div>')
    body = f'<h1>{esc(t["a_h1"])}</h1><p class="lead">{esc(t["a_d"])}</p>{lead}{poly_block(lang)}<section class="section">{table}</section>{hist}'
    return shell(lang, 'ath', f'{t["a_h1"]} | {BRAND}', t['a_d'], body, {}, ver)


HALVINGS = [(210000, '2012-11-28', 50, 25), (420000, '2016-07-09', 25, 12.5), (630000, '2020-05-11', 12.5, 6.25), (840000, '2024-04-20', 6.25, 3.125)]
NEXT_H = 1050000


def halving_page(lang, ver):
    import datetime as _dt
    t = TT[lang]
    base = _dt.datetime(2024, 4, 20, 0, 9, tzinfo=_dt.timezone.utc)
    upd = _dt.datetime.strptime(UPDATED, '%Y-%m-%d').replace(tzinfo=_dt.timezone.utc)
    h_now = 840000 + int((upd - base).total_seconds() / 600)
    est = upd + _dt.timedelta(seconds=(NEXT_H - h_now) * 600)
    b = A.get('btc')
    rows = ''
    for blk, dt, r0, r1 in HALVINGS:
        ym = dt[:7]
        p0 = p1 = None
        if b:
            s0 = ym2i(b['start'])
            k = ym2i(ym) - s0
            if 0 <= k < len(b['p']):
                p0 = b['p'][k]
                if k + 12 < len(b['p']):
                    p1 = b['p'][k + 12]
        rows += (f'<tr><td>{dt}</td><td class="mono">{blk:,}</td><td class="mono">{r0:g} → {r1:g}</td><td class="mono">{price(p0) if p0 else "—"}</td>'
                 f'<td class="mono">{price(p1) if p1 else "—"}</td><td class="mono {cls(p1 / p0 - 1) if p0 and p1 else ""}">{pct(p1 / p0 - 1) if p0 and p1 else "—"}</td></tr>')
    dhm = t['v_dhm'].split('|')
    body = (f'<h1>{esc(t["v_h1"])}</h1><p class="lead">{esc(t["v_d"])}</p>'
            f'<div class="card hv" id="hv" data-next="{NEXT_H}" data-h="{h_now}" data-u="{upd.isoformat()}"><div class="muted">{t["v_next"]} · #{NEXT_H:,}</div>'
            f'<div class="cd"><div><b id="hd">—</b><span>{dhm[0]}</span></div><div><b id="hh">—</b><span>{dhm[1]}</span></div><div><b id="hm">—</b><span>{dhm[2]}</span></div></div>'
            f'<div class="hvs"><span>{t["v_left"]}: <b id="hleft">{NEXT_H - h_now:,}</b></span><span>{t["v_est"]}: <b id="hest">{mlabel(est.strftime("%Y-%m"), lang, long=True)}</b></span>'
            f'<span>{t["v_reward"].format(a="3.125", b="1.5625")}</span></div><div class="gbar"><i class="a" id="hprog" style="width:{(h_now - 840000) / 2100:.1f}%"></i></div></div>'
            f'<section class="card section"><h2>{t["v_past"]}</h2><div class="tw"><table class="mt"><thead><tr><th style="text-align:left"></th><th>#</th><th>BTC</th>'
            f'<th>{t["v_price"]}</th><th>{t["v_after"]}</th><th>%</th></tr></thead><tbody>{rows}</tbody></table></div><p class="muted" style="font-size:13px">{t["h_note"]}</p></section>'
            f'{poly_block(lang)}<section class="card section faq"><h2>{t["v_what"]}</h2><p>{esc(t["v_text"])}</p></section>'
            f'<section class="section"><div class="hgrid"><a class="card hcard" href="{url(lang, "ath")}"><span>📉</span><b>{esc(t["a_h1"])}</b></a>'
            f'<a class="card hcard" href="{aurl(lang, "btc")}"><span>₿</span><b>Bitcoin DCA</b></a></div></section>')
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": t['v_h1'], "acceptedAnswer": {"@type": "Answer", "text": f'{t["v_est"]}: {mlabel(est.strftime("%Y-%m"), lang, long=True)} (#{NEXT_H:,})'}},
        {"@type": "Question", "name": t['v_what'], "acceptedAnswer": {"@type": "Answer", "text": t['v_text']}}]}
    return shell(lang, 'bitcoin-halving', f'{t["v_h1"]} | {BRAND}', t['v_d'], body, {}, ver, [faq])


PARTNERS = {   # (name, /go/ id, tags, colour); real referral URLs are in api/_partners.js
    'cex': [('Binance', 'binance', 'Spot · Futures · Earn · P2P', '#F0B90B'),
            ('Bybit', 'bybit', 'Spot · Futures · Copy trading · Gold', '#17181E'),
            ('Gate', 'gate', 'Spot · Futures · Altcoins', '#2354E6'),
            ('BingX', 'bingx', 'Spot · Futures · Copy trading', '#2A5BFF'),
            ('MEXC', 'mexc', 'Spot · Futures · New listings', '#1972E2')],
    'dex': [('OKX Wallet', 'okx-wallet', 'Multichain wallet · DEX swaps', '#000000'),
            ('Hyperliquid', 'hyperliquid', 'On-chain perpetuals · Order book', '#0F3B36'),
            ('GMGN', 'gmgn', 'Memecoin trading · Wallet tracking', '#18C46B')],
}
POLY = '/go/polymarket'


def poly_block(lang, q='crypto'):
    e = EX[lang]
    return (f'<section class="card section pm" data-tag="{q}" hidden><div class="charthead"><h2>🔮 {e["pm_h"]}</h2>'
            f'<a class="calc" href="{POLY}?from=pm-block&l={lang}" target="_blank" rel="sponsored nofollow noopener">{e["pm_go"]} →</a></div>'
            f'<p class="muted" style="margin:0 0 10px">{e["pm_d"]}</p><div class="pml"></div><p class="muted" style="font-size:12px;margin:8px 0 0">{e["pm_note"]}</p></section>')


def exchanges_page(lang, ver):
    e = EX[lang]
    def cards(k):
        return ''.join(f'<a class="card xcard" href="/go/{u}?from=exchanges&l={lang}" target="_blank" rel="sponsored nofollow noopener"><span class="xl" style="background:{c}">{n[0]}</span>'
                       f'<div><b>{n}</b><small>{t}</small></div><span class="btn">{e["go"]}</span></a>' for n, u, t, c in PARTNERS[k])
    body = (f'<h1>{esc(e["h1"])}</h1><p class="lead">{esc(e["d"])}</p>'
            f'<section class="section"><h2>{e["cex"]}</h2><div class="xgrid">{cards("cex")}</div></section>'
            f'<section class="section"><h2>{e["dex"]}</h2><div class="xgrid">{cards("dex")}</div></section>'
            f'<p class="muted" style="font-size:13px">{e["note"]}</p>{poly_block(lang)}')
    return shell(lang, 'exchanges', f'{e["h1"]} | {BRAND}', e['d'], body, {}, ver)


NEWS_TAGS = ['bitcoin', 'ethereum', 'etf', 'regulation', 'defi', 'stablecoins', 'solana', 'xrp', 'markets', 'hacks']


def news_items(lang):
    return sorted(NEWS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)


def news_row(lang, slug, m, tl):
    tags = ''.join(f' <i class="badge">{esc(tl.get(t, t))}</i>' for t in (x.strip() for x in m.get('tags', '').split(',')) if t)
    g = ' '.join(x.strip() for x in m.get('tags', '').split(',') if x.strip())
    return (f'<a class="nrow" data-g="{esc(g)}" href="{url(lang, "news/" + slug)}"><b>{esc(m.get("title", ""))}</b>'
            f'<span class="muted">WhatIfStack · <time data-t="{esc(m.get("date", ""))}">{esc(m.get("date", "")[:16])}</time>{tags}</span></a>')


def news_page(lang, ver):
    n = NW[lang]
    tl = dict(zip(NEWS_TAGS, n['tags'].split('|')))
    chips = f'<button class="on" data-t="">{esc(n["n_all"])}</button>' + ''.join(f'<button data-t="{k}">{esc(v)}</button>' for k, v in tl.items())
    own = news_items(lang)[:60]
    own_html = (f'<section class="section"><h2>{esc(n["own"])}</h2><div class="card nlist own">' + ''.join(news_row(lang, k, m, tl) for k, m in own) + '</div></section>') if own else ''
    body = (f'<h1>{esc(n["n_h1"])}</h1><p class="lead">{esc(n["n_d"])}</p><div class="seg nchips" id="ntags">{chips}</div>{own_html}'
            f'<section class="section"><h2>{esc(n["live"])}</h2>'
            f'<div class="card nlist" id="nlist"><div class="bload"><i></i></div></div><button class="toggle" id="nmore" hidden>{esc(n["more"])}</button>'
            f'<p class="muted" style="font-size:13px">{esc(n["n_note"])}</p></section>{poly_block(lang)}')
    cfg = dict(news=dict(tags=tl))
    return shell(lang, 'news', f'{n["n_h1"]} | {BRAND}', n['n_d'], body, cfg, ver)


def news_article(lang, slug, ver):
    S, n = TR[lang], NW[lang]
    m = NEWS[lang][slug]
    tl = dict(zip(NEWS_TAGS, n['tags'].split('|')))
    title, desc = m.get('title', ''), m.get('description', '')
    tags = ''.join(f'<span class="badge">{esc(tl.get(t, t))}</span> ' for t in (x.strip() for x in m.get('tags', '').split(',')) if t)
    cards = ''.join(sc_block('card', [i], lang) for i in m['assets'][:3])
    rel = [(k, x) for k, x in news_items(lang) if k != slug][:6]
    rel_html = ''.join(news_row(lang, k, x, tl) for k, x in rel)
    w = S['w']
    about = url(lang if lang in ABOUT else 'en', 'about')
    body = (f'<nav class="crumbs"><a href="{url(lang, "news")}">{n["n_nav"]}</a></nav><article class="art"><h1>{esc(title)}</h1>'
            f'<div class="muted byline"><a href="{about}">WhatIfStack Research</a> · <time data-t="{esc(m.get("date", ""))}">{esc(m.get("date", ""))}</time> · {tags}</div>'
            f'<p class="lead">{esc(desc)}</p><div class="postcards">{cards}</div><div class="artbody">{md(m["body"], lang)}</div></article>'
            f'{poll_block(lang)}<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div><a class="btn" id="ctaBuy2" href="{url(lang, "exchanges")}">{EX[lang]["nav"]} →</a></section>'
            + (f'<section class="section"><h2>{esc(n["own"])}</h2><div class="card nlist own">{rel_html}</div></section>' if rel else ''))
    d = m.get('date', '').replace(' ', 'T')
    jsonld = [{"@context": "https://schema.org", "@type": "NewsArticle", "headline": title, "description": desc, "inLanguage": S['loc'],
               "datePublished": d, "dateModified": d, "mainEntityOfPage": SITE + url(lang, 'news/' + slug), "image": [SITE + '/assets/og.jpg'],
               "author": {"@type": "Organization", "name": "WhatIfStack Research", "url": SITE + about},
               "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + '/assets/icon-512.png'}}}]
    return shell(lang, 'news/' + slug, f'{title} | {BRAND}', desc, body, {}, ver, jsonld)


ABOUT = {
 'en': ('About WhatIfStack and our methodology', [
   ('Who we are', 'WhatIfStack is an independent markets site for ordinary investors. We show in plain language what regular (DCA) investing in crypto, stocks, ETFs and gold would have returned, with real prices, in 20 languages.'),
   ('Where the data comes from', 'Crypto prices: Binance public market data and CoinGecko (names, logos, market cap, all-time highs). Stocks, ETFs and metals: Yahoo Finance. Fear & Greed index: alternative.me. Exchange rates: open.er-api.com. Inflation: World Bank consumer price data. Prediction odds: Polymarket. Prices update daily, live crypto prices stream from Binance.'),
   ('How we calculate', 'DCA results use monthly closing prices: each month we buy the daily amount times the number of days in that month at the month’s close. Stock and ETF prices are adjusted for splits and include reinvested dividends. Fees and taxes are not included. Historical returns do not guarantee future results.'),
   ('How our articles are made', 'Articles are written by the WhatIfStack Research team with the help of AI tools. Every news fact is taken from the sources linked at the end of the article; numbers come from our own data and update automatically. We do not give buy or sell recommendations.'),
   ('Partner links', 'Some links to exchanges and services are partner (referral) links: we may earn a commission when you sign up, at no extra cost to you. This never changes the data or the rankings.')]),
 'uk': ('Про WhatIfStack і методологію', [
   ('Хто ми', 'WhatIfStack — незалежний сайт про ринки для звичайних інвесторів. Ми простою мовою показуємо, що дали б регулярні (DCA) інвестиції в крипту, акції, ETF і золото, на реальних цінах і 20 мовами.'),
   ('Звідки дані', 'Ціни крипти: публічні дані Binance і CoinGecko (назви, логотипи, капіталізація, історичні максимуми). Акції, ETF і метали: Yahoo Finance. Індекс страху й жадібності: alternative.me. Курси валют: open.er-api.com. Інфляція: дані Світового банку про споживчі ціни. Ймовірності прогнозів: Polymarket. Ціни оновлюються щодня, живі ціни крипти — з Binance.'),
   ('Як ми рахуємо', 'Результати DCA рахуються за місячними цінами закриття: щомісяця купуємо денну суму, помножену на кількість днів місяця, за ціною закриття місяця. Ціни акцій і ETF скориговані на спліти й враховують реінвестовані дивіденди. Комісії й податки не враховуються. Минулі результати не гарантують майбутніх.'),
   ('Як створюються статті', 'Статті пише команда WhatIfStack Research за допомогою інструментів штучного інтелекту. Кожен факт із новин взято з джерел, посилання на які є в кінці статті; цифри — з наших власних даних і оновлюються автоматично. Ми не даємо порад купувати чи продавати.'),
   ('Партнерські посилання', 'Частина посилань на біржі й сервіси — партнерські (реферальні): ми можемо отримати комісію, якщо ти зареєструєшся, для тебе це нічого не коштує. Це ніколи не впливає на дані чи рейтинги.')]),
}


def about_page(lang, ver):
    h1, secs = ABOUT[lang]
    body = f'<article class="art"><h1>{esc(h1)}</h1><div class="artbody">' + ''.join(f'<h2>{esc(h)}</h2><p>{esc(t)}</p>' for h, t in secs) + '</div></article>'
    org = {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + '/', "logo": SITE + '/assets/icon-512.png'}
    return shell(lang, 'about', f'{h1} | {BRAND}', secs[0][1], body, {}, ver, [org])


def habits_strip(lang):
    h = HB[lang]
    code, _ = hccy(lang)
    cards = ''.join(f'<a class="card hcard" href="{url(lang, "habits/" + HSLUG[k])}"><span>{HICON[k]}</span><b>{esc(h[k][1])}</b>'
                    f'<small>{esc(TR[lang]["p10"])} · {esc(nm(A["spy"], lang))}</small><em class="good">{money(hsim(lang, k, 10, "spy")["val"], code)}</em></a>' for k in HSCEN)
    return (f'<section class="section"><div class="charthead"><h2>{esc(h["h1"])}</h2><a class="calc" href="{url(lang, "habits")}">{esc(h["nav"])} →</a></div>'
            f'<div class="hgrid">{cards}</div></section>')


def habits_hub(lang, ver):
    h = HB[lang]
    code, _ = hccy(lang)
    cards = ''
    for k in HSCEN:
        r = hsim(lang, k, 10, 'spy')
        cards += (f'<a class="card hcard big" href="{url(lang, "habits/" + HSLUG[k])}"><span>{HICON[k]}</span><b>{esc(h[k][1])}</b>'
                  f'<small>{esc(TR[lang]["p10"])} · {esc(nm(A["spy"], lang))}</small><em class="good">{money(r["val"], code)}</em></a>')
    body = f'<h1>{esc(h["h1"])}</h1><p class="lead">{esc(h["d"])}</p><div class="hgrid">{cards}</div>'
    return shell(lang, 'habits', f'{h["h1"]} | {BRAND}', h['d'], body, {}, ver)


def hub(lang, slug, ver):
    S, X = TR[lang], TR[lang]['x']
    cat = HUBS[slug]
    ids = [i for i in ORDERED if A[i]['cat'] == cat]
    label = S['ui'][cat]
    title = X['hub_h1'].format(cat=label) + ' | ' + BRAND
    desc = X['hub_d'].format(n=len(ids), cat=label.lower())
    b5 = best_by('r5', ids)[:4]
    cards = ''.join(hl_card(lang, i, nm(A[i], lang), 'r5', S['sub5']) for i in b5)
    filt = f'<div class="toolbar"><div class="filter">{SEARCH_ICON}<input id="flt" type="search" autocomplete="off"></div></div>'
    body = (f'<nav class="crumbs"><a href="{url(lang)}">{S["nav_rank"]}</a> / {esc(label)}</nav><h1>{esc(X["hub_h1"].format(cat=label))}</h1>'
            f'<p class="lead">{esc(desc)}</p><div class="hl">{cards}</div><div class="tabs" id="tabs"></div>{filt}{table_block(lang, ids[:150])}')
    return shell(lang, slug, title, desc, body, dict(tab=cat), ver)


LOCAL_CCY = {'uk': 'fx:UAH', 'ru': 'fx:RUB', 'pl': 'fx:PLN', 'de': 'fx:EUR', 'fr': 'fx:EUR', 'es': 'fx:EUR', 'it': 'fx:EUR', 'nl': 'fx:EUR',
             'pt': 'fx:BRL', 'tr': 'fx:TRY', 'id': 'fx:IDR', 'vi': 'fx:VND', 'th': 'fx:THB', 'hi': 'fx:INR', 'ja': 'fx:JPY',
             'ko': 'fx:KRW', 'zh': 'fx:CNY', 'ar': 'fx:AED', 'fil': 'fx:PHP', 'en': 'usd'}


def tool(lang, slug, ver):
    S, X, u = TR[lang], TR[lang]['x'], TR[lang]['ui']
    loc = TV_LOC.get(lang, 'en')
    h1, d = {'screener': (X['scr_h1'], X['scr_d']), 'converter': (X['conv_h1'], X['conv_d']), 'calendar': (X['cal_h1'], X['cal_d']),
             'heatmap': (X['heat_h1'], X['heat_d']), 'news': (X['news_h1'], X['news_d'])}[slug]
    if slug == 'calendar':
        inner = '<div class="card">' + tvw('events', dict(colorTheme='light', isTransparent=True, width='100%', height='100%', locale=loc,
                                                           importanceFilter='0,1', countryFilter='us,eu,gb,cn,jp,de,ua'), 760) + '</div>'
    elif slug == 'heatmap':
        inner = ('<div class="card">' + tvw('stock-heatmap', dict(exchanges=[], dataSource='SPX500', grouping='sector', blockSize='market_cap_basic',
                                                                    blockColor='change', locale=loc, symbolUrl='', colorTheme='light', hasTopBar=True,
                                                                    isDataSetEnabled=True, isZoomEnabled=True, hasSymbolTooltip=True, width='100%', height='100%'), 640)
                 + '</div><div class="card section">' + tvw('crypto-coins-heatmap', dict(dataSource='Crypto', blockSize='market_cap_calc', blockColor='24h_close_change|5',
                                                                                         locale=loc, symbolUrl='', colorTheme='light', hasTopBar=True, isDataSetEnabled=True,
                                                                                         isZoomEnabled=True, hasSymbolTooltip=True, width='100%', height='100%'), 560) + '</div>')
    elif slug == 'screener':
        sc = dict(width='100%', height='100%', defaultColumn='overview', defaultScreen='general', showToolbar=True, colorTheme='light', locale=loc, isTransparent=True)
        inner = ('<div class="card">' + tvw('screener', dict(sc, market='america'), 620) + '</div><div class="card section">'
                 + tvw('screener', dict(sc, market='crypto', screener_type='crypto_mkt', displayCurrency='USD'), 620) + '</div>')
    elif slug == 'news':
        inner = '<div class="card">' + tvw('timeline', dict(feedMode='all_symbols', isTransparent=True, displayMode='regular', width='100%', height='100%',
                                                             colorTheme='light', locale=loc), 900) + '</div>'
    else:
        fiat = ''.join(f'<option value="fx:{c}">{c}</option>' for c in FX.get('rates', {}))
        opts = (f'<optgroup label="Fiat" data-g="fiat"><option value="usd">US Dollar (USD)</option>{fiat}</optgroup>'
                f'<optgroup label="Crypto" data-g="crypto">' + ''.join(f'<option value="{i}">{esc(nm(A[i], lang))} ({esc(A[i]["tk"])})</option>' for i in ORDERED if A[i]['cat'] == 'crypto') + '</optgroup>'
                f'<optgroup label="Stocks, ETFs, metals" data-g="other">' + ''.join(f'<option value="{i}">{esc(nm(A[i], lang))} ({esc(A[i]["tk"])})</option>' for i in ORDERED if A[i]['cat'] != 'crypto') + '</optgroup>')
        inner = (f'<div class="card conv"><div class="cvrow"><label class="f">{X["conv_from"]}<div class="inp"><input id="cva" type="number" value="1" min="0" step="any"></div></label>'
                 f'<label class="f">&nbsp;<div class="inp"><select id="cvf">{opts.replace(chr(34) + "btc" + chr(34), chr(34) + "btc" + chr(34) + " selected", 1)}</select></div></label>'
                 f'<button class="toggle" id="cvsw" aria-label="swap">⇄</button>'
                 f'<label class="f">{X["conv_to"]}<div class="inp"><select id="cvt" data-def="{LOCAL_CCY.get(lang, "usd")}">{opts}</select></div></label></div>'
                 f'<div class="cvres" id="cvres"></div><div class="muted" id="cvrate"></div></div>'
                 f'<section class="card section"><h2>{X["xrates"]}</h2>'
                 + tvw('forex-cross-rates', dict(width='100%', height='100%', currencies=['EUR', 'USD', 'GBP', 'JPY', 'CHF', 'CNY', 'PLN', 'UAH', 'TRY'],
                                                 isTransparent=True, colorTheme='light', locale=loc), 420) + '</section>')
    body = f'<h1>{esc(h1)}</h1><p class="lead">{esc(d)}</p>{inner}'
    return shell(lang, slug, f'{h1} | {BRAND}', d, body, dict(tool=slug), ver)


# ---------------- blog ----------------
import re as _re


def load_posts(sub='blog'):
    posts = {}
    root = os.path.join(ROOT, 'content', sub)
    if not os.path.isdir(root):
        return posts
    for lang in sorted(os.listdir(root)):
        for fn in sorted(os.listdir(os.path.join(root, lang))):
            if not fn.endswith('.md'):
                continue
            raw = open(os.path.join(root, lang, fn), encoding='utf-8').read()
            meta, body = {}, raw
            if raw.startswith('---'):
                head, body = raw[3:].split('\n---', 1)
                for line in head.strip().splitlines():
                    k, _, v = line.partition(':')
                    meta[k.strip()] = v.strip()
            meta['assets'] = [x.strip() for x in meta.get('assets', '').split(',') if x.strip() in A]
            meta['body'] = body.strip()
            posts.setdefault(lang, {})[fn[:-3]] = meta
    return posts


POSTS = load_posts()
NEWS = load_posts('news')   # own news briefs: content/news/<lang>/<slug>.md


def sc_value(kind, args, lang):
    """Shortcodes give numbers computed from today's data, so articles stay current."""
    if kind == 'dcainv':
        yrs = int(args[0]) if args else 5
        return usd(simulate('btc', END_I - yrs * 12)['inv'])
    aid = args[0] if args else None
    if aid and aid not in A:
        return '—'
    yrs = int(args[1]) if len(args) > 1 else 5
    st = max(END_I - yrs * 12, ym2i(A[aid]['start'])) if aid else END_I - yrs * 12
    if kind == 'dca':
        return usd(simulate(aid, st)['val'])
    if kind == 'dcaroi':
        return pct(simulate(aid, st)['roi'])
    if kind == 'dcainv':
        return usd(simulate(args[1] if len(args) > 1 and args[1] in A else 'btc', END_I - int(args[0]) * 12)['inv']) if args else '—'
    if kind in ('lump', 'lumproi'):
        k = A[aid]['p'][-1] / A[aid]['p'][min(st - ym2i(A[aid]['start']), len(A[aid]['p']) - 1)]
        return usd(1000 * k) if kind == 'lump' else pct(k - 1)
    if kind == 'price':
        return price(METRICS[aid]['price'])
    if kind == 'r':
        return pct(METRICS[aid]['r' + str(yrs)] if ('r' + str(yrs)) in METRICS[aid] else None)
    if kind == 'date':
        return mlabel(END, lang, long=True)
    return '—'


def sc_block(kind, args, lang):
    S = TR[lang]
    if kind == 'card' and args and args[0] in A:
        aid = args[0]; a = A[aid]; m = METRICS[aid]
        return (f'<a class="card postcard" href="{aurl(lang, aid)}">{icon(a, True)}<div><b>{esc(nm(a, lang))}</b> <span class="badge">{esc(a["tk"])}</span>'
                f'<div class="muted">{S["stat"].format(p=S["p5"])}: <b class="{cls(m["r5"])}">{pct(m["r5"])}</b> · {S["ui"]["price"]} <b data-p="{aid}">{price(m["price"])}</b></div></div>'
                f'<span class="calc">{S["ui"]["calc"]} →</span></a>')
    if kind == 'table' and args:
        ids = [i for i in args[0].split(',') if i in A]
        yrs = int(args[1]) if len(args) > 1 else 5
        hh = f'<tr><th>{S["ui"]["asset"]}</th><th>{S["ui"]["invested"]}</th><th>DCA · {S["p" + str(yrs)] if "p" + str(yrs) in S else yrs}</th><th>{S["result"]}</th><th>{S["x"]["lump"].format(p=S.get("p" + str(yrs), yrs))}</th></tr>'
        rows = ''
        for i in ids:
            st = max(END_I - yrs * 12, ym2i(A[i]['start']))
            r = simulate(i, st)
            k = A[i]['p'][-1] / A[i]['p'][min(st - ym2i(A[i]['start']), len(A[i]['p']) - 1)]
            rows += (f'<tr><td class="a"><a href="{aurl(lang, i)}">{esc(nm(A[i], lang))}</a></td><td>{usd(r["inv"])}</td><td>{usd(r["val"])}</td>'
                     f'<td class="{cls(r["roi"])}">{pct(r["roi"])}</td><td>{usd(1000 * k)}</td></tr>')
        return f'<div style="overflow-x:auto"><table class="rt">{hh}{rows}</table></div>'
    return ''


def inline_md(s, lang):
    s = esc(s)
    s = _re.sub(r'\{\{(\w+)(?::([^}]*))?\}\}', lambda m: sc_value(m.group(1), (m.group(2) or '').split(':') if m.group(2) else [], lang), s)
    s = _re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = _re.sub(r'(?<!\*)\*(?!\s)(.+?)\*', r'<em>\1</em>', s)
    s = _re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2).replace("{lang}", url(lang).rstrip("/"))}">{m.group(1)}</a>', s)
    return s


def md(text, lang):
    out, para, lst, ltag = [], [], [], None
    def flush():
        nonlocal para, lst, ltag
        if para:
            out.append('<p>' + inline_md(' '.join(para), lang) + '</p>'); para = []
        if lst:
            out.append(f'<{ltag}>' + ''.join(f'<li>{inline_md(x, lang)}</li>' for x in lst) + f'</{ltag}>'); lst = []
    for line in text.splitlines():
        s = line.strip()
        bm = _re.fullmatch(r'\{\{(card|table):([^}]*)\}\}', s)
        if not s:
            flush(); continue
        if bm:
            flush(); out.append(sc_block(bm.group(1), bm.group(2).split(':'), lang)); continue
        h = _re.match(r'(#{2,3})\s+(.*)', s)
        if h:
            flush(); lv = len(h.group(1)); out.append(f'<h{lv}>{inline_md(h.group(2), lang)}</h{lv}>'); continue
        if s.startswith('> '):
            flush(); out.append(f'<blockquote>{inline_md(s[2:], lang)}</blockquote>'); continue
        li = _re.match(r'(-|\d+\.)\s+(.*)', s)
        if li:
            if para:
                flush()
            ltag = 'ul' if li.group(1) == '-' else 'ol'
            lst.append(li.group(2)); continue
        if lst:
            flush()
        para.append(s)
    flush()
    return '\n'.join(out)


def post_meta_title(meta, lang):
    return _re.sub(r'\{\{(\w+)(?::([^}]*))?\}\}', lambda m: sc_value(m.group(1), (m.group(2) or '').split(':') if m.group(2) else [], lang), meta['title'])


def blog_index(lang, ver):
    X = TR[lang]['x']
    items = sorted(POSTS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)
    cl = NW[lang]['cats'].split('|')
    cmap = dict(zip(('analytics', 'guides', 'reports'), cl[1:]))
    cats = [c for c in ('analytics', 'guides', 'reports') if any(m.get('category', 'analytics') == c for _, m in items)]
    tabs = (f'<div class="seg nchips" id="bcats"><button class="on" data-c="">{esc(cl[0])}</button>' + ''.join(f'<button data-c="{c}">{esc(cmap[c])}</button>' for c in cats) + '</div>') if len(cats) > 1 else ''
    cards = ''.join(
        f'<a class="card post" data-c="{m.get("category", "analytics")}" href="{url(lang, "blog/" + slug)}"><div class="muted"><span class="badge">{esc(cmap.get(m.get("category", "analytics"), ""))}</span> {esc(m.get("date", ""))}</div><h2>{esc(post_meta_title(m, lang))}</h2>'
        f'<p>{esc(post_meta_title(dict(title=m.get("description", "")), lang))}</p>'
        + ''.join(f'<span class="badge">{esc(A[i]["tk"])}</span> ' for i in m['assets']) + '</a>' for slug, m in items)
    body = f'<h1>{esc(NW[lang]["i_nav"])}</h1><p class="lead">{esc(X["blog_d"])}</p>{tabs}<div class="posts">{cards}</div>'
    return shell(lang, 'blog', X['blog_h1'] + ' | ' + BRAND, X['blog_d'], body, {}, ver)


def blog_post(lang, slug, ver):
    S, X = TR[lang], TR[lang]['x']
    m = POSTS[lang][slug]
    title = post_meta_title(m, lang)
    desc = post_meta_title(dict(title=m.get('description', '')), lang)
    html_body = md(m['body'], lang)
    rel = [s for s in POSTS.get(lang, {}) if s != slug][:3]
    rel_html = ''.join(f'<a class="card post" href="{url(lang, "blog/" + s)}"><h3>{esc(post_meta_title(POSTS[lang][s], lang))}</h3></a>' for s in rel)
    cards = ''.join(sc_block('card', [i], lang) for i in m['assets'][:4])
    w = S['w']
    body = (f'<nav class="crumbs"><a href="{url(lang, "blog")}">{NW[lang]["i_nav"]}</a></nav><article class="art"><h1>{esc(title)}</h1>'
            f'<div class="muted byline"><a href="{url(lang if lang in ABOUT else "en", "about")}">WhatIfStack Research</a> · {esc(m.get("date", ""))} · {S["updated"]} {UPDATED}</div><div class="artbody">{html_body}</div></article>'
            f'<div class="postcards">{cards}</div>{poll_block(lang)}'
            f'<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div><a class="btn" id="ctaBuy2" href="{url(lang, "compare")}">{w["cta"]} →</a></section>'
            + (f'<section class="section"><h2>{X["related"]}</h2><div class="posts">{rel_html}</div></section>' if rel else ''))
    jsonld = [{"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": S['loc'],
               "datePublished": m.get('date'), "dateModified": UPDATED, "mainEntityOfPage": SITE + url(lang, 'blog/' + slug),
               "author": {"@type": "Organization", "name": "WhatIfStack Research", "url": SITE + url(lang if lang in ABOUT else 'en', 'about')},
               "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + '/assets/icon-512.png'}}}]
    return shell(lang, 'blog/' + slug, title, desc, body, {}, ver, jsonld)


def rss(lang):
    X = TR[lang]['x']
    items = sorted(POSTS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)
    it = ''.join(f'<item><title>{esc(post_meta_title(m, lang))}</title><link>{SITE + url(lang, "blog/" + s)}</link>'
                 f'<guid>{SITE + url(lang, "blog/" + s)}</guid><pubDate>{esc(m.get("date", ""))}</pubDate>'
                 f'<description>{esc(post_meta_title(dict(title=m.get("description", "")), lang))}</description></item>' for s, m in items)
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{esc(X["blog_h1"])}</title>'
            f'<link>{SITE + url(lang, "blog")}</link><description>{esc(X["blog_d"])}</description>{it}</channel></rss>')


# ---------------- build ----------------
def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(OUT)
    css = open(os.path.join(ROOT, 'src/style.css'), encoding='utf-8').read()
    js = open(os.path.join(ROOT, 'src/app.js'), encoding='utf-8').read()
    ref = open(os.path.join(ROOT, 'src/ref.js'), encoding='utf-8').read()
    dv = h8(json.dumps(market['assets'], sort_keys=True))
    idx = []
    for aid in ORDERED:
        a, m = A[aid], METRICS[aid]
        e = dict(i=aid, n=nm(a, 'uk'), t=a['tk'], c=a['cat'], o=ORD[aid], pr=m['price'], ch=m['chg'],
                 r1=m['r1'], r3=m['r3'], r5=m['r5'], sp=m['spark'], s=a['start'])
        if nm(a, 'en') != e['n']:
            e['ne'] = nm(a, 'en')
        if a.get('logo'):
            e['l'] = a['logo']
        idx.append({k: (round(v, 4) if isinstance(v, float) and k in ('ch', 'r1', 'r3', 'r5') else v) for k, v in e.items() if v is not None})
        write(f'assets/p/{aid}.json', json.dumps({'start': a['start'], 'end': a['end'], 'p': a['p']}, separators=(',', ':')))
    index_js = 'window.WI=' + json.dumps({'u': UPDATED, 'v': dv, 'a': idx, 'fx': FX.get('rates', {}), 'fxu': FX.get('updated')}, ensure_ascii=False, separators=(',', ':')) + ';'
    write('assets/index.js', index_js); write('assets/style.css', css); write('assets/app.js', js); write('assets/ref.js', ref)
    if _LOGOS:
        shutil.copytree(LOGO_DIR, os.path.join(OUT, 'assets/logo'))
    for f in ('favicon.svg', 'icon-192.png', 'icon-512.png', 'og.jpg'):
        shutil.copy(os.path.join(ROOT, 'src', f), os.path.join(OUT, 'assets', f))
    write('manifest.webmanifest', json.dumps({
        'name': 'WhatIfStack — DCA calculator & markets', 'short_name': 'WhatIfStack', 'start_url': '/', 'scope': '/',
        'display': 'standalone', 'background_color': '#0e1014', 'theme_color': '#0e1014',
        'icons': [{'src': '/assets/icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any maskable'},
                  {'src': '/assets/icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any maskable'}]}, ensure_ascii=False))
    # service worker: static assets cache-first, pages network-first with offline fallback to the cached copy
    write('sw.js', f"""const C='wi-{dv}';
self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{{const r=e.request,u=new URL(r.url);if(r.method!=='GET'||u.origin!==location.origin||u.pathname.startsWith('/_vercel'))return;
 if(u.pathname.startsWith('/assets/')&&u.search){{e.respondWith(caches.open(C).then(c=>c.match(r).then(m=>m||fetch(r).then(res=>{{if(res.ok)c.put(r,res.clone());return res}}))));return}}
 if(r.mode==='navigate'){{e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp));return res}}).catch(()=>caches.match(r).then(m=>m||caches.match('/'))))}}
}});""")
    ver = dict(css=h8(css), js=h8(js), ref=h8(ref), index=h8(index_js))
    per_lang = {}
    for lang in ORDER:
        pre = '' if lang == DEFAULT else lang + '/'
        assets_ = [aid for aid in ORDERED if has_page(lang, aid)]
        write(pre + 'index.html', home(lang, ver))
        write(pre + 'compare/index.html', compare(lang, ver))
        for aid in assets_:
            write(f'{pre}{aid}/index.html', asset(aid, lang, ver))
        for slug in HUBS:
            write(f'{pre}{slug}/index.html', hub(lang, slug, ver))
        for slug in TOOLS:
            write(f'{pre}{slug}/index.html', tool(lang, slug, ver))
        extra_pages = ['habits'] + ['habits/' + HSLUG[k] for k in HSCEN] + [c for c in CALCS if has_page(lang, c)]
        write(pre + 'millionaire/index.html', calc_page(lang, 'millionaire', ver))
        write(pre + 'compound-interest/index.html', calc_page(lang, 'compound-interest', ver))
        if CPI['c']:
            write(pre + 'inflation/index.html', inflation_page(lang, ver))
        write(pre + 'ath/index.html', ath_page(lang, ver))
        write(pre + 'bitcoin-halving/index.html', halving_page(lang, ver))
        write(pre + 'exchanges/index.html', exchanges_page(lang, ver))
        write(pre + 'news/index.html', news_page(lang, ver))
        for k in NEWS.get(lang, {}):
            write(f'{pre}news/{k}/index.html', news_article(lang, k, ver))
        extra_pages += ['news/' + k for k in NEWS.get(lang, {})]
        if lang in ABOUT:
            write(pre + 'about/index.html', about_page(lang, ver))
        write(pre + 'habits/index.html', habits_hub(lang, ver))
        for k in HSCEN:
            write(f'{pre}habits/{HSLUG[k]}/index.html', habit_page(lang, k, ver))
        if lang in BLOG_LANGS and POSTS.get(lang):
            write(pre + 'blog/index.html', blog_index(lang, ver))
            write(pre + 'blog/rss.xml', rss(lang))
            for s in POSTS[lang]:
                write(f'{pre}blog/{s}/index.html', blog_post(lang, s, ver))
            extra_pages += ['blog'] + ['blog/' + s for s in POSTS[lang]]
        per_lang[lang] = [None, 'compare'] + list(HUBS) + TOOLS + extra_pages + assets_
    # sitemaps: one per language + index
    for lang, pages in per_lang.items():
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
        for p in pages:
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{TR[lg]["loc"]}" href="{SITE + url(lg, p)}"/>' for lg in ORDER if has_page(lg, p))
            sm.append(f'<url><loc>{SITE + url(lang, p)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
        sm.append('</urlset>')
        write(f'sitemap-{lang}.xml', '\n'.join(sm))
    si = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    si += [f'<sitemap><loc>{SITE}{BASE}/sitemap-{lg}.xml</loc><lastmod>{UPDATED}</lastmod></sitemap>' for lg in ORDER]
    si.append('</sitemapindex>')
    write('sitemap.xml', '\n'.join(si))
    nf = {'uk': ('Сторінку не знайдено', 'Можливо, актив перейменовано або видалено. Знайди його через пошук угорі або перейди до рейтингу.'),
          'en': ('Page not found', 'The asset may have been renamed or removed. Use the search above or go to the ranking.')}
    body404 = ''.join(f'<h1>{a}</h1><p class="lead">{b}</p><p><a class="btn" href="{url(lg)}">{TR[lg]["nav_rank"]} →</a></p>' for lg, (a, b) in nf.items())
    write('404.html', shell('en', None, 'Page not found | ' + BRAND, nf['en'][1], body404, {}, ver).replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"'))
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /go/\nDisallow: /api/\nDisallow: /stats\nSitemap: {SITE}{BASE}/sitemap.xml\n')
    total = sum(len(p) for p in per_lang.values())
    print(f"built {total} pages in {len(ORDER)} languages · {len(A)} assets · data {UPDATED}")


if __name__ == '__main__':
    main()
