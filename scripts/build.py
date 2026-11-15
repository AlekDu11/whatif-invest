"""Generate the static whatif.invest site into ./dist/whatif/ (Vercel runs this on every deploy).

Input:  data/market.json (prices, from scripts/fetch_data.py), data/assets.json (curated list),
        scripts/i18n*.py (20 languages).
Output: per language — home, compare and asset pages; index.js, per-asset price files, sitemaps.
Only the Python standard library is used, so it runs in Vercel's build image as is.
Run: python3 scripts/build.py
"""
import calendar, hashlib, html, json, os, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import LANGS as TR, ORDER, FULL, DEFAULT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
OUT = os.path.join(DIST, 'whatif')
BASE = '/whatif'
SITE = 'https://mytimebox.app'
AMOUNT = 10
TOP_N = 200            # asset pages in languages outside FULL

market = json.load(open(os.path.join(ROOT, 'data/market.json'), encoding='utf-8'))
pinned = json.load(open(os.path.join(ROOT, 'data/assets.json'), encoding='utf-8'))
UPDATED = market['updated']
END = UPDATED[:7]
END_DAY = int(UPDATED[8:10])
PIN_ORDER = {a['id']: k for k, a in enumerate(pinned)}
A = {aid: a for aid, a in market['assets'].items() if a.get('p')}
_gp = os.path.join(ROOT, 'data/global.json')
G = json.load(open(_gp, encoding='utf-8')) if os.path.exists(_gp) else {}
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


def has_page(lang, aid):
    return aid is None or aid == 'compare' or lang in FULL or aid in TOP


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


def shell(lang, p, title, desc, body, cfg, ver, jsonld=()):
    S = TR[lang]
    canon = SITE + url(lang, p)
    alts = ''.join(f'<link rel="alternate" hreflang="{TR[lg]["loc"]}" href="{SITE + url(lg, p)}">' for lg in ORDER if has_page(lg, p))
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + url("en", p)}">'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    nav = ''.join(f'<a href="{url(lang, k)}" class="{"on" if k == p else ""}">{v}</a>' for k, v in ((None, S['nav_rank']), ('compare', S['nav_cmp'])))
    i18n = dict(S['ui'], months=S['months'], intl=S['intl'])
    cfg = dict(cfg, lang=lang, prefix=url(lang).rstrip('/'), full=lang in FULL, topn=TOP_N,
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
<meta property="og:type" content="website"><meta property="og:site_name" content="whatif.invest"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:locale" content="{S['intl'].replace('-', '_')}">
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
  {lang_menu(lang, p)}
</div></div>
<main class="wrap">
{body}
<footer><span>{S['by']} <a href="{SITE}/">Timebox</a> · {S['sources']}</span><span>{S['disclaimer']}</span></footer>
<nav class="langs">{' · '.join(f'<a href="{url(lg, p) if has_page(lg, p) else url(lg)}" hreflang="{TR[lg]["loc"]}">{esc(TR[lg]["name"])}</a>' for lg in ORDER)}</nav>
</main>
<script>window.PAGE={json.dumps(cfg, ensure_ascii=False)};window.I18N={json.dumps(i18n, ensure_ascii=False)};</script>
<script src="{BASE}/assets/index.js?v={ver['index']}"></script>
<script src="{BASE}/assets/ref.js?v={ver['ref']}"></script>
<script src="{BASE}/assets/app.js?v={ver['js']}" defer></script>
</body>
</html>
"""


def calc_block(lang):
    u = TR[lang]['ui']
    return f"""<div id="calc">
<div class="card">
  <div class="controls">
    <div><label class="f">{u['amount']}</label><div class="inp"><span>$</span><input id="amt" type="number" min="1" step="1" value="{AMOUNT}" aria-label="{u['amount']}"></div></div>
    <div><label class="f">{u['freq']}</label><div class="seg" id="freq"><button data-v="d" class="on">{u['daily']}</button><button data-v="w">{u['weekly']}</button><button data-v="m">{u['monthly']}</button></div></div>
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
    # heatmap top 30 crypto
    hm_ids = [i for i in ids if A[i]['cat'] == 'crypto'][:30]
    tiles = ''
    for k, i in enumerate(hm_ids):
        c = METRICS[i]['chg'] or 0
        sz = 'h1' if k < 2 else 'h2' if k < 8 else 'h3'
        tiles += (f'<a class="tile {sz}{" dk" if abs(c) > 0.04 else ""}" data-h="{i}" href="{aurl(lang, i)}" style="background:{heat_color(c)}"><b>{esc(A[i]["tk"])}</b>'
                  f'<span data-c="{i}">{pct(METRICS[i]["chg"])}</span><small data-p="{i}">{price(METRICS[i]["price"])}</small></a>')
    heat = f'<section class="section"><div class="charthead"><h2>{w["heat"]}</h2><span class="livebadge"><i></i>{w["live"]}</span></div><div class="heat">{tiles}</div></section>'
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
            f'<div class="wgrid3">{w_up}{w_dn}{w_bat}</div>{heat}{banner}'
            f'<section class="section"><div class="hl">{"".join(cards)}</div></section>'
            f'<div class="tabs" id="tabs"></div>{filt}{table_block(lang, ids[:100])}'
            f'<section class="card section faq"><h2>{S["faq"]}</h2><details open><summary>{esc(S["q3"])}</summary><p>{esc(S["a3"])}</p></details></section>')
    jsonld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "whatif.invest", "url": SITE + url(lang),
               "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "inLanguage": S['loc'],
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}]
    return shell(lang, None, title, desc, body, dict(home=True), ver, jsonld)


def heat_color(c):
    c = max(-0.1, min(0.1, c))
    if c >= 0:
        k = c / 0.1
        return f"rgb({int(232 - 212 * k)},{int(246 - 82 * k)},{int(237 - 160 * k)})"
    k = -c / 0.1
    return f"rgb({int(253 - 24 * k)},{int(236 - 164 * k)},{int(236 - 159 * k)})"


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
    tv = (f'<section class="card section tvcard"><div class="charthead"><h2>{w["live_chart"]} · {esc(tk)}</h2><span class="livebadge"><i></i>{w["live"]}</span></div>'
          f'<div id="tv" data-sym="{esc(tv_symbol(a))}" data-loc="{TV_LOC.get(lang, "en")}"></div></section>')
    body = (f'{head}<p class="lead" style="margin-top:10px">{S["a_lead"].format(**fe)}</p>{tv}<div class="stats">{stat_cards}</div>{calc_block(lang)}'
            f'<div class="cols2 section"><section class="card"><h2>{S["a_periods"].format(**fe)}</h2>{ptable}</section>'
            f'<section class="card faq"><h2>{S["faq"]}</h2>' + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q, x in faq) + '</section></div>'
            f'<section class="section">{table_block(lang, sim, S["a_similar"] + ": " + esc(cat), interactive=False)}</section>'
            f'<p class="note">{esc(S["about"].format(**f))}</p>')
    jsonld = [{"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": S['loc'],
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": x}} for q, x in faq]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "whatif.invest", "item": SITE + url(lang)},
                  {"@type": "ListItem", "position": 2, "name": n, "item": SITE + url(lang, aid)}]}]
    sel = [aid] + list(bench(aid))[:2]
    return shell(lang, aid, title, desc, body, dict(sel=sel, since=since, asset=aid), ver, jsonld)


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
    index_js = 'window.WI=' + json.dumps({'u': UPDATED, 'v': dv, 'a': idx}, ensure_ascii=False, separators=(',', ':')) + ';'
    write('assets/index.js', index_js); write('assets/style.css', css); write('assets/app.js', js); write('assets/ref.js', ref)
    shutil.copy(os.path.join(ROOT, 'src/favicon.svg'), os.path.join(OUT, 'assets/favicon.svg'))
    ver = dict(css=h8(css), js=h8(js), ref=h8(ref), index=h8(index_js))
    per_lang = {}
    for lang in ORDER:
        pre = '' if lang == DEFAULT else lang + '/'
        pages = [None, 'compare'] + [aid for aid in ORDERED if has_page(lang, aid)]
        write(pre + 'index.html', home(lang, ver))
        write(pre + 'compare/index.html', compare(lang, ver))
        for aid in pages[2:]:
            write(f'{pre}{aid}/index.html', asset(aid, lang, ver))
        per_lang[lang] = pages
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
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}{BASE}/sitemap.xml\n')
    total = sum(len(p) for p in per_lang.values())
    print(f"built {total} pages in {len(ORDER)} languages · {len(A)} assets · data {UPDATED}")


if __name__ == '__main__':
    main()
