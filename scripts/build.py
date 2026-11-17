"""Generate the static whatif.invest site into ./dist/ (Vercel runs this on every deploy).

Input:  data/market.json (prices, from scripts/fetch_data.py), data/assets.json (curated list),
        scripts/i18n*.py (20 languages).
Output: per language — home, compare and asset pages; index.js, per-asset price files, sitemaps.
Only the Python standard library is used, so it runs in Vercel's build image as is.
Run: python3 scripts/build.py
"""
import calendar, hashlib, html, json, math, os, re as _re, shutil, sys
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import LANGS as TR, ORDER, FULL, DEFAULT  # noqa: E402
from i18n_t import T as TT  # noqa: E402
from i18n_e import E as EX  # noqa: E402
from i18n_n import N as NW, FOOT, SHARE, HOT
from i18n_s import S as SEA  # noqa: E402
from i18n_i import I as INF  # noqa: E402
from i18n_world import W as WA, WN  # noqa: E402
from i18n_ctry import C as CTRY, MKTS, MKT_LANG, CCY_SIGN  # noqa: E402  # noqa: E402
from i18n_p import P as POLL, OPTS as POLL_OPTS  # noqa: E402
from i18n_ai import AI as AIS  # noqa: E402
from i18n_me import ME  # noqa: E402
from i18n_mem import MEM  # noqa: E402
from i18n_act import ACT  # noqa: E402
from i18n_prof import P as PROF_T  # noqa: E402
from i18n_pf import PF  # noqa: E402
from i18n_bp import BP  # noqa: E402
from i18n_ai import AIC  # noqa: E402
from i18n_emb import EMB, EXT  # noqa: E402
from i18n_ic import IC  # noqa: E402
from i18n_calc2 import DV, AV, OV  # noqa: E402
from i18n_ap import AP  # noqa: E402
from i18n_home2 import HM  # noqa: E402
from i18n_ks import KS, SECT  # noqa: E402
from i18n_offer import OFFER_TGW  # noqa: E402
from i18n_lc import LC  # noqa: E402
from i18n_xc import XC  # noqa: E402
from i18n_bpd import BPD, IDEA as BP_IDEA  # noqa: E402
from i18n_cmd import CMD, NAMES as CMD_NAMES, NOTE as CMD_NOTE, AB as AUTO_AB, CH as OWN_CH, CH2 as OWN_CH2  # noqa: E402
SOCIAL = [('Telegram', 'https://t.me/TradeMaster_insight'), ('X (Twitter)', 'https://x.com/WhatIfStack'), ('Bluesky', 'https://bsky.app/profile/whatifstack.bsky.social'), ('Instagram', 'https://www.instagram.com/whatifstack/'), ('Threads', 'https://www.threads.com/@whatifstack'),
          ('Pinterest', 'https://www.pinterest.com/whatifstack/'), ('Medium', 'https://medium.com/@whatifstack'),
          ('Flipboard', 'https://flipboard.com/@whatifstack'), ('Facebook', 'https://www.facebook.com/arti.trader.39'), ('Teletype', 'https://teletype.in/@whatifstack'),
          ('GitHub', 'https://github.com/AlekDu11/whatif-invest')]
CONTACT_EMAIL = ''   # public contact address shown under 'Follow us' (set when the owner confirms which mailbox)   # [(label, url)], e.g. ('Telegram', 'https://t.me/whatifstack'); the 'Follow us' column appears when filled
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
RESERVED = set(ORDER) | {'assets', 'blog', 'compare', 'crypto', 'stocks', 'etfs', 'metals', 'converter', 'calendar', 'heatmap', 'news', 'bubbles', 'screener', 'habits', 'millionaire', 'compound-interest', 'inflation', 'ath', 'bitcoin-halving', 'exchanges', 'ai', 'me', 'memes', 'stocks-ukraine', 'stocks-poland', 'stocks-germany', 'world-assets', 'guide', 'commodities', 'widgets', 'embed', 'dividends', 'average-price', 'ovdp', 'largest-companies', 'crypto-exchanges'}
RESERVED |= {v[0] for v in MKTS.values()} | {'world-assets', 'activities', 'editorial-policy', 'about', 'portfolios'}
# asset ids that clash with a language folder or a section get a suffix (ko -> ko-stock, fil -> fil-crypto)
_END_I0 = (lambda s: int(s[:4]) * 12 + int(s[5:7]) - 1)(market['updated'][:7])
# delisted or stale series (last price older than a month) are dropped: "today" numbers would be false
A = {(f"{aid}-{a['cat']}" if aid in RESERVED else aid): a for aid, a in market['assets'].items()
     if a.get('p') and (lambda s: int(s[:4]) * 12 + int(s[5:7]) - 1)(a['end']) >= _END_I0 - 1}
for _k, _a in A.items():
    _a['_id'] = _k
    if _a.get('cat') == 'stock' and not _a.get('mkt') and not any(c in (_a.get('yahoo') or '') for c in '.:'):
        _a['mkt'] = 'us'   # US-listed stocks -> /stocks-usa/
_SPF = os.path.join(ROOT, 'data/logo-sprite.json')
SPRITE = json.load(open(_SPF)) if os.path.exists(_SPF) and os.path.exists(os.path.join(ROOT, 'data/logo-sprite.webp')) else {'ids': {}}
SPRITE_CSS = ''
if SPRITE['ids']:
    _sv = hashlib.md5(open(os.path.join(ROOT, 'data/logo-sprite.webp'), 'rb').read()).hexdigest()[:8]
    SPRITE_CSS = (f'<style>.ic.sp{{background-image:url(/assets/logo-sprite.webp?v={_sv});background-size:{SPRITE["cols"] * 100}% {SPRITE["rows"] * 100}%;'
                  f'background-repeat:no-repeat;background-color:transparent}}</style>')
_gp = os.path.join(ROOT, 'data/global.json')
G = json.load(open(_gp, encoding='utf-8')) if os.path.exists(_gp) else {}
_fp = os.path.join(ROOT, 'data/fx.json')
FX = json.load(open(_fp, encoding='utf-8')) if os.path.exists(_fp) else {'rates': {}}
_cp = os.path.join(ROOT, 'data/cpi.json')
CPI = json.load(open(_cp, encoding='utf-8')) if os.path.exists(_cp) else {'c': {}}
TV_LOC = {'en': 'en', 'uk': 'uk', 'ru': 'ru', 'es': 'es', 'pt': 'br', 'de': 'de_DE', 'fr': 'fr', 'it': 'it', 'pl': 'pl', 'tr': 'tr',
          'nl': 'nl_NL', 'id': 'id', 'vi': 'vi_VN', 'th': 'th_TH', 'hi': 'in', 'ja': 'ja', 'ko': 'kr', 'zh': 'zh_CN', 'ar': 'ar_AE', 'fil': 'en'}


FUT_EX = {'COMEX': ('GC', 'SI', 'HG', 'ALI'), 'NYMEX': ('PL', 'PA', 'CL', 'NG', 'HO', 'RB'), 'CBOT': ('ZW', 'ZC', 'ZS', 'ZL', 'ZO', 'ZR'),
          'ICEUS': ('SB', 'KC', 'CC', 'CT', 'OJ'), 'CME': ('LE', 'HE'), 'ICEEUR': ('BZ',)}


FUT_TV = {'PL=F': 'OANDA:XPTUSD', 'PA=F': 'OANDA:XPDUSD', 'HG=F': 'OANDA:XCUUSD', 'ZW=F': 'OANDA:WHEATUSD', 'ZC=F': 'OANDA:CORNUSD',
          'ZS=F': 'OANDA:SOYBNUSD', 'SB=F': 'OANDA:SUGARUSD', 'NG=F': 'OANDA:NATGASUSD', 'CL=F': 'OANDA:WTICOUSD', 'BZ=F': 'OANDA:BCOUSD'}

# Exchanges whose charts TradingView does not allow in free embeds (they fall back to AAPL) -> our own chart
TV_NOCHART = ('LSE:', 'BIST:', 'TSE:', 'KRX:', 'HKEX:', 'TWSE:', 'SET:', 'HOSE:', 'TADAWUL:', 'BMV:')


def tv_symbol(a):
    if a['cat'] == 'crypto':
        ex = {'gate': 'GATEIO', 'mexc': 'MEXC', 'okx': 'OKX'}.get(a.get('src'), 'BINANCE')
        return f"{ex}:{a['tk']}USDT"
    if a['cat'] == 'metal' and a['tk'] in ('XAU', 'XAG'):
        return 'OANDA:XAUUSD' if a['tk'] == 'XAU' else 'OANDA:XAGUSD'
    if (a.get('yahoo') or '').endswith('=F'):   # exchange futures are not allowed in free embeds -> OANDA CFD or no widget
        return FUT_TV.get(a['yahoo'])
    y = a.get('yahoo') or ''
    if y.startswith('MOEX:'):
        return y
    for suf, ex in (('.WA', 'GPW'), ('.DE', 'XETR'), ('.L', 'LSE'), ('.PA', 'EURONEXT'), ('.AS', 'EURONEXT'), ('.MC', 'BME'), ('.MI', 'MIL'),
                    ('.IS', 'BIST'), ('.T', 'TSE'), ('.KS', 'KRX'), ('.NS', 'BSE'), ('.SA', 'BMFBOVESPA'), ('.HK', 'HKEX'), ('.SS', 'SSE'),
                    ('.SZ', 'SZSE'), ('.TW', 'TWSE'), ('.JK', 'IDX'), ('.BK', 'SET'), ('.PS', 'PSE'), ('.VN', 'HOSE'), ('.SR', 'TADAWUL'),
                    ('.SW', 'SIX'), ('.TO', 'TSX'), ('.AX', 'ASX'), ('.MX', 'BMV')):
        if y.endswith(suf):
            t = y[:-len(suf)]
            return f"{ex}:{t.lstrip('0') if suf == '.HK' else t.replace('-', '.')}"
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
    if a['cat'] in ('etf', 'metal', 'cmd'):
        return (2, 0, a['tk'])
    return (3, 0, nm(a, 'en').lower())


ORDERED = [aid for aid, _ in sorted(A.items(), key=order_key)]
# Home-table default order: what people look for first, mixed across classes; niche commodities later
_HOME_FIRST = ['btc', 'eth', 'spy', 'gold', 'nvda', 'aapl', 'msft', 'qqq', 'googl', 'amzn', 'meta', 'tsla', 'sol', 'xrp', 'bnb', 'silver', 'avgo',
               'tsm', 'vt', 'doge', 'jpm', 'v', 'lly', 'wmt', 'ada', 'trx', 'pltr', 'amd', 'nflx', 'orcl', 'schd', 'link', 'ko', 'ton', 'vti', 'smh', 'wti',
               'ltc', 'dot', 'brent', 'platinum', 'copper']
_hf = [i for i in _HOME_FIRST if i in A]
_niche = [i for i in ORDERED if i not in _hf and A[i]['cat'] in ('cmd', 'metal')]
_rest = [i for i in ORDERED if i not in _hf and i not in _niche]
HOME_ORDER = _hf + _rest[:150] + _niche + _rest[150:]
HOME_POS = {aid: k for k, aid in enumerate(HOME_ORDER)}
ORD = {aid: k for k, aid in enumerate(ORDERED)}
TOP = set(ORDERED[:TOP_N])


HUBS = {'crypto': 'crypto', 'stocks': 'stock', 'etfs': 'etf', 'metals': 'metal', 'commodities': 'cmd'}
for _lg in TR:   # commodities tab labels (scripts/i18n_cmd.py)
    TR[_lg]['ui'].update(cmd=CMD[_lg][0], u_cmd=CMD[_lg][2])
    TR[_lg]['cat_cmd'] = CMD[_lg][1]
CSLUG = {v[0]: k for k, v in MKTS.items()}   # 'stocks-poland' -> 'pl'
TOOLS = ['converter']
CALCS = ['millionaire', 'compound-interest', 'inflation', 'ath', 'bitcoin-halving', 'exchanges', 'news', 'about', 'widgets', 'dividends', 'average-price', 'ovdp']
BLOG_LANGS = {l for l in ORDER if os.path.isdir(os.path.join(ROOT, 'content/blog', l)) and any(f.endswith('.md') for f in os.listdir(os.path.join(ROOT, 'content/blog', l)))}  # a language gets a blog once it has a post
assert not (set(HUBS) | set(TOOLS) | {'blog', 'compare'}) & set(A), 'asset id collides with a section slug'


def has_page(lang, aid):
    if aid is None or aid == 'compare' or aid in HUBS or aid in TOOLS:
        return True
    if aid in ('ai', 'me', 'memes', 'world-assets', 'activities', 'portfolios', 'largest-companies') or (aid or '').startswith(('portfolios/', 'largest-companies/')):
        return True
    if aid == 'crypto-exchanges' or (aid or '').startswith('crypto-exchanges/'):
        return xc_has(lang, None if aid in ('crypto-exchanges', 'crypto-exchanges/derivatives') else aid.split('/', 1)[1])
    if aid == 'editorial-policy':
        return lang in POLICY
    if aid == 'guide':
        return lang in GUIDE
    if aid in CSLUG:
        return any(a.get('mkt') == CSLUG[aid] for a in A.values())
    if aid in CALCS:
        if aid == 'about':
            return lang in ABOUT
        if aid == 'ovdp':
            return lang in OV
        return aid != 'inflation' or bool(CPI['c'])
    if aid == 'habits' or (aid or '').startswith('habits/'):
        return True
    if (aid or '').startswith('news/'):
        return aid[5:] in NEWS.get(lang, {})
    if aid == 'blog' or (aid or '').startswith('blog/'):
        return lang in BLOG_LANGS and (aid == 'blog' or aid[5:] in POSTS.get(lang, {}))
    return lang in FULL or aid in TOP or (aid in A and MKT_LANG.get(A[aid].get('mkt')) == lang)


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
    anniv = frm == start_i and start_i < END_I and (END_I - start_i) % 12 == 0   # "N years" = exactly N*365 days
    for i in range(frm, e + 1):
        c = amt * (per_month(i) - (END_DAY if anniv and i == frm else 0))
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


# Number style per page language (set in the build loop): group sep, decimal sep, currency after the number, big-number words
NBSP, NNBSP = '\u00a0', '\u202f'
NUMFMT = {
    'en': (',', '.', False, ('K', 'M', 'B', 'T')), 'uk': (NBSP, ',', True, ('тис.', 'млн', 'млрд', 'трлн')), 'ru': (NBSP, ',', True, ('тыс.', 'млн', 'млрд', 'трлн')),
    'pl': (NBSP, ',', True, ('tys.', 'mln', 'mld', 'bln')), 'de': ('.', ',', True, ('Tsd.', 'Mio.', 'Mrd.', 'Bio.')), 'fr': (NNBSP, ',', True, ('k', 'M', 'Md', 'Bn')),
    'it': ('.', ',', True, ('mila', 'Mln', 'Mrd', 'Bln')), 'es': ('.', ',', True, ('mil', 'M', 'mil M', 'B')), 'pt': ('.', ',', False, ('mil', 'mi', 'bi', 'tri')),
    'tr': ('.', ',', False, ('B', 'Mn', 'Mr', 'Tn')), 'nl': ('.', ',', False, ('K', 'mln', 'mld', 'bln')), 'id': ('.', ',', False, ('rb', 'jt', 'M', 'T')),
    'vi': ('.', ',', True, ('N', 'Tr', 'T', 'NT')), 'th': (',', '.', False, ('K', 'M', 'B', 'T')), 'hi': (',', '.', False, ('K', 'M', 'B', 'T')),
    'ja': (',', '.', False, ('K', 'M', 'B', 'T')), 'ko': (',', '.', False, ('K', 'M', 'B', 'T')), 'zh': (',', '.', False, ('K', 'M', 'B', 'T')),
    'ar': (',', '.', False, ('K', 'M', 'B', 'T')), 'fil': (',', '.', False, ('K', 'M', 'B', 'T')),
}
CUR_FMT = ['en']


def set_numfmt(lang):
    CUR_FMT[0] = lang if lang in NUMFMT else 'en'


def _num(x, dec):
    g, d, _, _ = NUMFMT[CUR_FMT[0]]
    s = f"{x:,.{dec}f}"
    return s.replace(',', '\x00').replace('.', d).replace('\x00', g)


def _money(body, neg=False):
    after = NUMFMT[CUR_FMT[0]][2]
    sign = '−' if neg else ''
    return f"{sign}{body}{NBSP}$" if after else f"{sign}${body}"


def usd(v):
    if v is None:
        return '—'
    a = abs(v)
    w = NUMFMT[CUR_FMT[0]][3]
    if a >= 1e9:
        body = _num(a / 1e9, 2) + NBSP + w[2]
    elif a >= 1e6:
        body = _num(a / 1e6, 2) + NBSP + w[1]
    elif a >= 1e3:
        body = _num(a, 0)
    else:
        body = _num(a, 2)
        dsep = NUMFMT[CUR_FMT[0]][1]
        if body.endswith(dsep + '00'):
            body = body[:-3]
    return _money(body, v < 0)


def usd_h(v):
    """usd() for visible page text: the currency switcher converts it in the browser."""
    return f'<span data-u="{v:.6g}">{usd(v)}</span>' if v is not None else '—'


def price(v):
    if v is None:
        return '—'
    if v >= 1:
        return _money(_num(v, 2))
    return _money(_num(v, 4)) if v >= 0.01 else _money(_num(v, 8).rstrip('0'))


def pct(p):
    if p is None:
        return '—'
    a = abs(p * 100)
    s = _num(a, 0) if a >= 100 else _num(a, 1) if a >= 10 else _num(a, 2)
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
METAL_IC = {'GC=F': ('#d4a017', 'Au'), 'SI=F': ('#9ea3ab', 'Ag'), 'PL=F': ('#8d97a5', 'Pt'), 'PA=F': ('#7b8794', 'Pd'), 'HG=F': ('#c06a3c', 'Cu'),
            'ALI=F': ('#a7b1bb', 'Al'), 'ZW=F': ('#d9b45a', '🌾'), 'ZC=F': ('#e3b23c', '🌽'), 'ZS=F': ('#b9a35a', '🫘'), 'ZL=F': ('#c9a83c', '🫗'),
            'ZO=F': ('#cdb07a', '🌾'), 'ZR=F': ('#d8cfb8', '🍚'), 'SB=F': ('#d6d0c4', '🍬'), 'KC=F': ('#7a4a2a', '☕'), 'CC=F': ('#6b3e26', '🍫'),
            'CT=F': ('#cfd6dc', '☁'), 'OJ=F': ('#f0a030', '🍊'), 'LE=F': ('#9a6b4a', '🐄'), 'HE=F': ('#e3a0a0', '🐖'), 'CL=F': ('#333a44', '🛢'),
            'BZ=F': ('#3f4a58', '🛢'), 'NG=F': ('#4a7fc0', '🔥'), 'HO=F': ('#5a5f6a', '🛢'), 'RB=F': ('#c04a3a', '⛽')}


def hue(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 360
    return h


def icon(a, big=False):
    c = ' lg' if big else ''
    if a.get('cat') in ('metal', 'cmd') and not a.get('logo'):
        bg, t = METAL_IC.get(a.get('yahoo'), ('#b8a06a', a['tk'][:2]))
        return f'<span class="ic{c}" style="background:{bg}">{t}</span>'
    k = SPRITE['ids'].get(a.get('_id'))
    if k is not None:
        cols, rows = SPRITE['cols'], SPRITE['rows']
        return f'<span class="ic sp{c}" style="background-position:{k % cols * 100 / (cols - 1):.4g}% {k // cols * 100 / max(1, rows - 1):.4g}%"></span>'
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
    up = arr[-1] >= arr[0]
    return (f'<svg class="spk {"up" if up else "dn"}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
            f'<polygon points="0,{h} {pts} {w},{h}"/><polyline points="{pts}"/></svg>')


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
    for aid, label in (('btc', 'BTC'), ('eth', 'ETH'), ('spy', 'S&P 500 (SPY)'), ('qqq', 'Nasdaq-100 (QQQ)'), ('gold', S['gold']), ('silver', S['silver'])):
        if aid in A:
            m = METRICS[aid]
            items.append(f'<a href="{aurl(lang, aid)}">{esc(label)} <b data-p="{aid}">{price(m["price"])}</b> <span class="{cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</span></a>')
    return (f'<div class="strip"><div class="in">{"".join(items)}'
            f'<span>{S["updated"]} <b>{UPDATED}</b></span></div></div>')


def lang_menu(lang, p):
    opts = ''.join(f'<option value="{url(lg, p) if has_page(lg, p) else url(lg)}"{" selected" if lg == lang else ""}>{esc(TR[lg]["name"])}</option>' for lg in ORDER)
    return (f'<select class="ccysel" id="ccysel" aria-label="Currency"><option>USD</option></select>'
            f'<select class="langsel" aria-label="Language" onchange="location.href=this.value">{opts}</select>')


# Brand-coloured round icons for the "Follow us" block under every article (simple glyphs, no external files)
_G = {
    'Telegram': ('#229ED9', '<path d="M5 12.5 19 6.5 16.6 18.2 11.8 14.8 9.6 17 9.9 13.6 16.4 8.4 8.3 12.9z" fill="#fff"/>'),
    'X (Twitter)': ('#000', '<path d="M6.5 6h3.2l8 12h-3.2z" fill="#fff"/><path d="M17 6 7 18" stroke="#fff" stroke-width="1.6"/>'),
    'Instagram': ('#E1306C', '<rect x="6" y="6" width="12" height="12" rx="3.5" fill="none" stroke="#fff" stroke-width="1.7"/><circle cx="12" cy="12" r="2.9" fill="none" stroke="#fff" stroke-width="1.7"/><circle cx="15.6" cy="8.4" r=".9" fill="#fff"/>'),
    'Threads': ('#111', '<text x="12" y="16.6" text-anchor="middle" font-size="13" font-weight="700" fill="#fff" font-family="Arial">@</text>'),
    'Bluesky': ('#1185FE', '<path d="M12 11.2C10.6 8.5 7.6 6.3 6.2 6.9c-1.4.6-.4 4.4 1.6 5.1-2.2.6-2.4 2.6-.6 3.5 1.9.9 3.8-.9 4.8-3.3 1 2.4 2.9 4.2 4.8 3.3 1.8-.9 1.6-2.9-.6-3.5 2-.7 3-4.5 1.6-5.1-1.4-.6-4.4 1.6-5.8 4.3z" fill="#fff"/>'),
    'Facebook': ('#1877F2', '<path d="M13.2 19v-6h2l.3-2.4h-2.3V9.1c0-.7.2-1.2 1.2-1.2h1.2V5.8c-.2 0-1-.1-1.8-.1-1.8 0-3 1.1-3 3.1v1.8h-2V13h2v6z" fill="#fff"/>'),
    'Pinterest': ('#E60023', '<text x="12" y="17" text-anchor="middle" font-size="14" font-weight="800" fill="#fff" font-family="Georgia">P</text>'),
    'Medium': ('#000', '<ellipse cx="9" cy="12" rx="3.6" ry="3.8" fill="#fff"/><ellipse cx="15" cy="12" rx="1.7" ry="3.6" fill="#fff"/><ellipse cx="18" cy="12" rx=".7" ry="3.2" fill="#fff"/>'),
    'Flipboard': ('#E12828', '<path d="M7 7h10v3.3h-6.7v3.4H7z" fill="#fff"/><path d="M7 13.7h3.3V17H7z" fill="#fff" opacity=".8"/>'),
    'Teletype': ('#0c1613', '<text x="12" y="16.5" text-anchor="middle" font-size="12" font-weight="800" fill="#f2b632" font-family="Arial">T</text>'),
    'GitHub': ('#24292f', '<path d="M12 5.5a6.5 6.5 0 0 0-2 12.7c.3 0 .4-.1.4-.3v-1.2c-1.8.4-2.2-.8-2.2-.8-.3-.8-.7-1-.7-1-.6-.4 0-.4 0-.4.7 0 1 .7 1 .7.6 1 1.6.7 2 .6 0-.4.2-.7.4-.9-1.4-.2-3-.7-3-3.2 0-.7.3-1.3.7-1.7-.1-.2-.3-.8.1-1.7 0 0 .5-.2 1.8.7a6 6 0 0 1 3.2 0c1.2-.9 1.8-.7 1.8-.7.3.9.1 1.5 0 1.7.4.4.7 1 .7 1.7 0 2.5-1.5 3-3 3.2.3.2.5.6.5 1.2v1.8c0 .2.1.4.4.3A6.5 6.5 0 0 0 12 5.5z" fill="#fff"/>'),
}


def follow_block(lang):
    """'Follow us' card with round brand icons, shown under every article and news brief."""
    t = FOOT[lang][2]
    items = ''.join(f'<a class="fol" href="{u}" target="_blank" rel="me noopener" title="{esc(l)}"><svg viewBox="0 0 24 24" width="40" height="40" aria-hidden="true">'
                    f'<circle cx="12" cy="12" r="12" fill="{_G[l][0]}"/>{_G[l][1]}</svg><span>{esc(l.split(" ")[0])}</span></a>' for l, u in SOCIAL if l in _G)
    return f'<section class="card follow"><b>{esc(t)}</b><div class="folrow">{items}</div></section>'


def poll_block(lang):
    return ''   # poll hidden for now (owner, 2026-11-16)
    q, opts, thanks = POLL[lang]
    b = ''.join(f'<button data-o="{k}">{esc(v)}</button>' for k, v in zip(POLL_OPTS, opts.split('|')))
    return f'<section class="card section poll" id="poll" hidden data-thanks="{esc(thanks)}"><b>🗳 {esc(q)}</b><div class="pollb">{b}</div></section>'


def footer_cols(lang):
    S, n, f = TR[lang], NW[lang], FOOT[lang]
    blog_l = lang if lang in BLOG_LANGS else 'en'
    pop = [(aurl(lang, i), nm(A[i], lang)) for i in ('btc', 'eth', 'sol', 'xrp', 'nvda', 'aapl', 'tsla', 'gold', 'spy', 'qqq') if i in A]
    mk = [(url(lang), HM[lang]['nav']), (url(lang, 'compare'), S['nav_cmp'])] + [(url(lang, k), S['cat_' + v]) for k, v in HUBS.items()]
    mk += [(url(lang, sl), CTRY[lang][3][m][0]) for m, (sl, fl) in sorted(MKTS.items(), key=lambda kv: (MKT_LANG.get(kv[0]) != lang, kv[0] != 'ua')) if has_page(lang, sl)][:5]
    tools = [(url(lang, k), v) for k, v in [x for x in tools_menu(lang) if x]]
    ins = [(url(lang if lang in GUIDE else 'en', 'guide'), guide_meta(lang).get('nav', 'Guide')), (url(lang, 'news'), n['n_nav']), (url(blog_l, 'blog'), n['i_nav']), (url(blog_l, 'blog') + 'rss.xml', 'RSS'),
           (url(lang, 'activities'), ACT[lang]['nav']), (url(lang, 'exchanges'), EX[lang]['nav']), (url(lang if lang in ABOUT else 'en', 'about'), n['about']), (pol_url(lang), ACT[lang]['pol'])]
    cols = [(f[0], pop), (f[1], mk), (TR[lang]['x']['nav_tools'], tools), (n['i_nav'], ins)]
    if SOCIAL:
        cols.insert(0, (f[2], [(u, l) for l, u in SOCIAL] + ([('mailto:' + CONTACT_EMAIL, '✉ ' + CONTACT_EMAIL)] if CONTACT_EMAIL else [])))
    return ('<div class="fcols">' + ''.join(f'<details open><summary><b>{esc(t)}</b></summary><div>' + ''.join(f'<a href="{h}"{" rel=\"me noopener\" target=\"_blank\"" if h.startswith("https://") and "whatifstack.com" not in h else ""}>{esc(l)}</a>' for h, l in items) + '</div></details>' for t, items in cols) + '</div>')


def cover(kind, lang, slug):
    """Branded cover (content/covers/<kind>/<lang>/<slug>.jpg, made by scripts/cover.py); English cover as fallback."""
    for lg in (lang, 'en'):
        if os.path.exists(os.path.join(ROOT, 'content', 'covers', kind, lg, slug + '.jpg')):
            return f'/assets/covers/{kind}/{lg}/{slug}.jpg'
    return None


# Microsoft Clarity (heatmaps): loaded only after the page has finished loading and the browser is idle, so it never slows the first paint
CLARITY = ('<script>addEventListener("load",function(){var go=function(){(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};'
           't=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(window,document,"clarity","script","zekg137lbv")};window.requestIdleCallback?requestIdleCallback(go,{timeout:3000}):setTimeout(go,1500)})</script>')
AHREFS = ('<meta name="ahrefs-site-verification" content="f5a16ec7b7cfa87b5d531c2c5286aac58ddf73ffe836a8b623afe21b43719d5a">'
          '<meta name="p:domain_verify" content="a0820406d681ddd5d800b84175a15303">')   # + Pinterest site claim   # Ahrefs Webmaster Tools ownership


def ai_widget(lang, cfg):
    t = dict(AIC[lang])
    aid = cfg.get('asset')
    if aid and aid in A:
        t['n'] = nm(A[aid], lang)
    return f'<div id="aiw" data-cfg="{esc(json.dumps(t, ensure_ascii=False))}"></div>'


def embed_page():
    """/embed/?a=btc&amt=10&f=d|w|m&s=2021-01&l=uk&th=light|dark|auto&n=Name — iframe widget for other sites."""
    L = {lg: dict(share=TR[lg]['ui']['share'], inv=TR[lg]['ui']['invested'], per_d=TR[lg]['ui']['per_d'], per_w=TR[lg]['ui']['per_w'],
                  per_m=TR[lg]['ui']['per_m'], cta=EMB[lg]['cta'], intl=TR[lg]['intl'], dir=TR[lg]['dir'],
                  pre='' if lg == DEFAULT else '/' + lg) for lg in ORDER}
    return """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>WhatIfStack DCA widget</title><style>
:root{--bg:#fff;--tx:#10231b;--mu:#5d6f67;--ln:#e3ebe7;--ac:#0b7a55;--gd:#0f8a4e;--bd:#c8463d;--inv:#9aa8a2}
.dark{--bg:#0f1a16;--tx:#e8f1ed;--mu:#93a49c;--ln:#22332c;--ac:#3fd19b;--gd:#3fd19b;--bd:#ff7a6e;--inv:#5d6f67}
*{box-sizing:border-box}html,body{margin:0;background:transparent}
body{font:14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--tx)}
.w{background:var(--bg);border:1px solid var(--ln);border-radius:14px;padding:14px 16px 10px;max-width:520px}
.h{display:flex;align-items:center;gap:8px;font-weight:700;font-size:15px}.h img{width:24px;height:24px;border-radius:50%}
.h small{color:var(--mu);font-weight:600;font-size:12px;border:1px solid var(--ln);border-radius:6px;padding:0 5px}
.q{color:var(--mu);font-size:13px;margin:6px 0 2px}.v{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.v b{font-size:28px;letter-spacing:-.02em}.v i{font-style:normal;font-weight:700}.up{color:var(--gd)}.dn{color:var(--bd)}
.s{color:var(--mu);font-size:13px}svg{display:block;width:100%;height:64px;margin:8px 0 6px}
.f{display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--ln);padding-top:8px;font-size:13px}
.f a{color:var(--ac);font-weight:700;text-decoration:none}.f a:hover{text-decoration:underline}.f span{color:var(--mu)}
</style></head><body><div class="w" id="w"><div class="s">…</div></div><script>
const L=""" + json.dumps(L, ensure_ascii=False, separators=(',', ':')) + """;
const Q=new URLSearchParams(location.search),id=(Q.get('a')||'btc').replace(/[^a-z0-9-]/g,''),lg=L[Q.get('l')]?Q.get('l'):'en',T=L[lg];
const amt=Math.max(1,Math.min(1e6,+Q.get('amt')||10)),f=['d','w','m'].includes(Q.get('f'))?Q.get('f'):'d',th=Q.get('th')||'light';
if(th==='dark'||(th==='auto'&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.className='dark';
document.documentElement.lang=lg;document.documentElement.dir=T.dir;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ym=s=>{const[y,m]=s.split('-').map(Number);return y*12+m-1};
const money=v=>{try{return new Intl.NumberFormat(T.intl,{style:'currency',currency:'USD',currencyDisplay:'narrowSymbol',minimumFractionDigits:0,maximumFractionDigits:v>=100||Number.isInteger(v)?0:2}).format(v)}catch(e){return '$'+Math.round(v)}};
fetch('/assets/p/'+id+'.json').then(r=>r.json()).then(P=>{
  const s0=ym(P.start),e=ym(P.end),now=new Date(),qs=Q.get('s'),okS=qs&&/^\\d{4}-\\d{2}$/.test(qs);let from=okS?ym(qs):e-60;const anniv=!okS&&from>=s0;from=Math.max(from,s0);
  let u=0,inv=0;const pts=[];
  for(let i=from;i<=e;i++){const y=Math.floor(i/12),m=i%12+1;let d=new Date(y,m,0).getDate();if(i===e)d=Math.min(d,now.getDate());
    if(anniv&&i===from)d-=Math.min(d,now.getDate());const c=amt*(f==='d'?d:f==='w'?d/7:(i===e?0:1));u+=c/P.p[i-s0];inv+=c;pts.push([inv,u*P.p[i-s0]])}
  const val=u*P.p[e-s0],pct=inv?val/inv-1:0,name=Q.get('n')||P.n;
  let since;try{since=new Intl.DateTimeFormat(T.intl,{month:'short',year:'numeric'}).format(new Date(Math.floor(from/12),from%12,15))}catch(x){since=from}
  const pc=(pct>=0?'+':'')+(pct*100).toFixed(Math.abs(pct)<1?1:0)+'%';
  const sent=T.share.replace('${amt}',money(amt)).replace('{amt}',amt).replace('{per}',T['per_'+f]).replace('{asset}',name).replace('{since}',since).replace('{val}',money(val)).replace('{pct}',pc);
  const mx=Math.max(...pts.map(p=>Math.max(p[0],p[1])))||1,W=500,H=64,X=k=>(pts.length>1?k/(pts.length-1):0)*W,Y=v=>H-2-(v/mx)*(H-4);
  const line=j=>pts.map((p,k)=>X(k).toFixed(1)+','+Y(p[j]).toFixed(1)).join(' ');
  const href='https://whatifstack.com'+T.pre+'/'+id+'/?utm_source=embed&utm_medium=widget';
  document.getElementById('w').innerHTML=`<div class="h"><img src="/assets/logo/${id}.webp" alt="" onerror="this.remove()">${esc(name)} <small>${esc(P.t||'')}</small></div>
   <div class="q">${esc(sent)}</div><div class="v"><b>${money(val)}</b><i class="${pct>=0?'up':'dn'}">${pc}</i><span class="s">${esc(T.inv)} ${money(inv)}</span></div>
   <svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" aria-hidden="true"><polyline points="${line(0)}" fill="none" stroke="var(--inv)" stroke-width="1.5" stroke-dasharray="4 3" vector-effect="non-scaling-stroke"/>
   <polyline points="${line(1)}" fill="none" stroke="var(--${pct>=0?'gd':'bd'})" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>
   <div class="f"><a href="${href}" target="_blank" rel="noopener">${esc(T.cta)} →</a><span>WhatIfStack</span></div>`;
}).catch(()=>{document.getElementById('w').innerHTML='<div class="f"><a href="https://whatifstack.com/" target="_blank" rel="noopener">WhatIfStack</a></div>'});
</script></body></html>"""


def shell(lang, p, title, desc, body, cfg, ver, jsonld=()):
    og_img = SITE + (cfg.pop('_og', None) or '/assets/og.jpg')
    sec = cfg.pop('_sec', None) or p   # section to highlight in the nav
    S = TR[lang]
    canon = SITE + url(lang, p)
    alts = ''.join(f'<link rel="alternate" hreflang="{TR[lg]["loc"]}" href="{SITE + url(lg, p)}">' for lg in ORDER if has_page(lg, p))
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + url("en", p)}">'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    X = S['x']
    blog_l = lang if lang in BLOG_LANGS else 'en'
    news_on = p in ('news', 'ai') or sec == 'activities' or (sec or '').startswith('blog') or (p or '').startswith('news/')
    tools_on = p in TOOLS or (p in CALCS and p not in ("exchanges", "news", "about", "compound-interest")) or (p or "").startswith("habits") or p in ('memes', 'world-assets')
    nav = (''.join(f'<a href="{url(lang, k)}" class="{"on" if k == p else ""}">{v}</a>' for k, v in ((None, HM[lang]['nav']), ('portfolios', BP[lang]['nav']), ('compound-interest', IC[lang]['nav'])))
           + f'<a href="{url(lang, "exchanges")}" class="{"on" if p == "exchanges" else ""}">{EX[lang]["nav"]}</a>'
           + f'<details class="dd"><summary class="{"on" if news_on else ""}">{NW[lang]["n_nav"]}</summary><div>'
           + f'<a href="{url(lang, "news")}">{NW[lang]["n_nav"]}</a><a href="{url(blog_l, "blog")}">{NW[lang]["i_nav"]}</a>'
           + f'<a href="{url(lang, "ai")}">{AIS[lang]["nav"]}</a><a href="{url(lang, "activities")}">{ACT[lang]["nav"]}</a></div></details>'
           + f'<details class="dd"><summary class="{"on" if tools_on else ""}">{X["nav_tools"]}</summary><div>'
           + ''.join(f'<a href="{url(lang, k)}">{v}</a>' for k, v in [x for x in tools_menu(lang) if x]) + '</div></details>')
    i18n = dict(S['ui'], months=S['months'], intl=S['intl'])
    mnav = ''.join(f'<a href="{h}" class="{"on" if on else ""}"><span>{ic}</span>{esc(lb)}</a>' for h, ic, lb, on in (
        (url(lang), '◎', HM[lang]['nav'], p is None), (url(lang, 'news'), '▤', NW[lang]['n_nav'], p == 'news'),
        (url(lang, 'exchanges'), '₿', EX[lang]['nav'], p == 'exchanges'), (url(blog_l, 'blog'), '✎', NW[lang]['i_nav'], (p or '').startswith('blog'))))
    mnav += f'<button type="button" id="mmore"><span>☰</span>{esc(X["nav_tools"])}</button>'
    msheet = ('<div class="msheet" id="msheet" hidden>' + ''.join(f'<a href="{url(lang, k)}">{esc(v)}</a>' for k, v in
              [('me', PF[lang]['h1']), ('portfolios', BP[lang]['nav']), ('compound-interest', IC[lang]['nav']), ('activities', ACT[lang]['nav']), ('ai', AIS[lang]['h1'].split(':')[0])] + [x for x in tools_menu(lang) if x]) + '</div>')
    cfg = dict(cfg, lang=lang, base=BASE, prefix=url(lang).rstrip('/'), full=lang in FULL, topn=TOP_N,
               names={'gold': S['gold'], 'silver': S['silver'], **{k: v[lang] for k, v in CMD_NAMES.items()}})
    return f"""<!DOCTYPE html>
<html lang="{S['loc']}" dir="{S['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">{AHREFS if p is None else ""}
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}<link rel="alternate" type="application/rss+xml" title="{BRAND} RSS" href="{SITE + url(blog_l, 'blog')}rss.xml">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:locale" content="{S['intl'].replace('-', '_')}">
<meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{og_img}"><meta name="theme-color" content="#ffffff">
<script>(function(){{try{{var t=localStorage.getItem('wi_theme')}}catch(e){{}}if(!t)t='dark';if(t==='dark'){{document.documentElement.dataset.theme='dark';document.querySelector('meta[name=theme-color]').content='#080d0f'}}}})()</script>
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{BASE}/assets/icon-192.png"><link rel="manifest" href="{BASE}/manifest.webmanifest">
<link rel="preload" href="{BASE}/assets/onest.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{BASE}/assets/geologica-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}/assets/style.css?v={ver['css']}">{SPRITE_CSS}
{ld}
</head>
<body>
{strip(lang)}
<div class="top"><div class="in">
  <a class="logo" href="{url(lang)}"><svg class="mk" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="15" width="18" height="5" rx="2.5" fill="var(--gold)"/><rect x="5" y="9.5" width="14" height="4.5" rx="2.25" fill="var(--accent)"/><rect x="7.5" y="4" width="9" height="4.5" rx="2.25" fill="var(--text)"/></svg><span>whatif<b>stack</b></span></a>
  <div class="gsearch">{SEARCH_ICON}<input id="gs" type="search" autocomplete="off" aria-label="search"><div class="gres" id="gres"></div></div>
  <nav class="nav">{nav}</nav>
  <a class="thm me" href="{url(lang, 'me')}" title="{esc(PF[lang]['h1'])}" aria-label="{esc(PF[lang]['h1'])}">💼</a>
  <button class="thm" id="thm" type="button" aria-label="theme"><span class="m">☾</span><span class="s">☀</span></button>
  {lang_menu(lang, p)}
</div></div>
<nav class="mnav">{mnav}</nav>{msheet}
<main class="wrap">
{body}
<div class="sharebar" data-l="{esc(SHARE[lang])}"></div>{footer_cols(lang)}<footer><span>{BRAND} · {S['by']} <a href="https://mytimebox.app/">Timebox</a> · {S['sources']} · <a href="{url(lang if lang in ABOUT else 'en', 'about')}">{NW[lang]['about']}</a> · <a href="{pol_url(lang)}">{ACT[lang]['pol']}</a></span><span>{S['disclaimer']}</span></footer>
<nav class="langs">{' · '.join(f'<a href="{url(lg, p) if has_page(lg, p) else url(lg)}" hreflang="{TR[lg]["loc"]}">{esc(TR[lg]["name"])}</a>' for lg in ORDER)}</nav>
</main>
{ai_widget(lang, cfg)}
<script>window.PAGE={json.dumps(cfg, ensure_ascii=False)};window.I18N={json.dumps(i18n, ensure_ascii=False)};</script>
<script src="{BASE}/assets/index.js?v={ver['index']}" defer></script>
<script src="{BASE}/assets/ref.js?v={ver['ref']}" defer></script>
<script src="{BASE}/assets/app.js?v={ver['js']}" defer></script>
<script defer src="/_vercel/insights/script.js"></script>
{CLARITY}
</body>
</html>
"""


def tvw(kind, cfg, height):
    return f'<div class="tvw" style="height:{height}px" data-w="{kind}" data-cfg="{esc(json.dumps(cfg))}"></div>'


def own_chart(lang, a, aid):
    """Monthly price chart drawn from our own data (no TradingView symbol available). CSS-only range tabs."""
    ps, st = a.get('p') or [], a.get('start')
    if len(ps) < 3 or not st:
        return ''
    y0, m0 = map(int, st.split('-'))
    W, H, L, R, T, B = 720, 300, 8, 80, 12, 26
    uid = 'oc' + _re.sub(r'[^a-z0-9]', '', aid)
    rngs = [(n, n * 12) for n in (1, 3, 5, 10) if len(ps) > n * 12 - 1] + [(0, len(ps))]
    rngs = [r for i, r in enumerate(rngs) if r[1] not in [x[1] for x in rngs[:i]]]
    tabs, svgs = '', ''
    for i, (n, k) in enumerate(rngs):
        k = max(2, min(k, len(ps)))
        seg = ps[-k:]
        off = len(ps) - k
        lo, hi = min(seg), max(seg)
        pad = (hi - lo) * 0.08 or hi * 0.05 or 1
        lo, hi = max(0, lo - pad), hi + pad
        X = lambda j: L + (W - L - R) * j / (k - 1)
        Y = lambda v: T + (H - T - B) * (1 - (v - lo) / (hi - lo))
        pts = ' '.join(f'{X(j):.1f},{Y(v):.1f}' for j, v in enumerate(seg))
        up = seg[-1] >= seg[0]
        col = '#16a34a' if up else '#dc2626'
        grid = ''
        for g in range(5):
            v = lo + (hi - lo) * g / 4
            yy = Y(v)
            lv = f'${v:,.0f}' if v >= 100 else (f'${v:,.2f}' if v >= 1 else f'${v:.4g}')
            grid += f'<line x1="{L}" x2="{W - R}" y1="{yy:.1f}" y2="{yy:.1f}" class="g"/><text x="{W - R + 6}" y="{yy + 4:.1f}">{lv}</text>'
        step = max(1, round(k / 12 / 6)) * 12 if k > 24 else (3 if k > 6 else 1)
        for j in range(k):
            mi = m0 - 1 + off + j
            yy, mm = y0 + mi // 12, mi % 12 + 1
            if (k > 24 and mm == 1 and (yy % (step // 12) == 0)) or (k <= 24 and (mi % step == 0)):
                lab = str(yy) if k > 24 else f'{mm:02d}.{str(yy)[2:]}'
                if L + 18 < X(j) < W - R - 18:
                    grid += f'<text x="{X(j):.1f}" y="{H - 6}" text-anchor="middle">{lab}</text>'
        chg = (seg[-1] / seg[0] - 1) if seg[0] else 0
        lab = OWN_CH[lang][1] if n == 0 else BP[lang]['yrs'].format(n=n)
        tabs += (f'<input type="radio" name="{uid}" id="{uid}{i}"{" checked" if i == len(rngs) - 1 else ""}>'
                 f'<label for="{uid}{i}">{esc(lab)}</label>')
        svgs += (f'<div class="ocv"><div class="occhg {"up" if up else "dn"}">{pct(chg)}</div>'
                 f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(OWN_CH[lang][0])}">{grid}'
                 f'<polygon points="{X(0):.1f},{H - B} {pts} {X(k - 1):.1f},{H - B}" fill="{col}" opacity=".08"/>'
                 f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg></div>')
    lw = dict(y=a.get('yahoo') or '', t=OWN_CH2[lang][0], avg=OWN_CH2[lang][1], all=OWN_CH[lang][1],
              yrs=[BP[lang]['yrs'].format(n=n) for n in (1, 3, 5)], intl=TR[lang]['loc'])
    return (f'<section class="card tvcard ownchart" data-lw="{esc(json.dumps(lw, ensure_ascii=False))}"><div class="charthead"><h2>{esc(OWN_CH[lang][0])} · {esc(a["tk"])}</h2></div>'
            f'<div class="oc">{tabs}<div class="ocs">{svgs}</div></div></section>')


def emb_cfg(lang, aid=None):
    u = TR[lang]['ui']
    e = EMB[lang]
    return dict(a=aid or '', l=lang, t=dict(dlg=e['dlg'], help=e['help'], theme=e['theme'], light=e['light'], dark=e['dark'], auto=e['auto'],
                pick=e['pick'], anchor=e['anchor'], amount=u['amount'], freq=u['freq'], daily=u['daily'], weekly=u['weekly'],
                monthly=u['monthly'], since=u['since'], copy=u['copy'], copied=u['copied']))


def emb_block(lang, aid):
    e = EMB[lang]
    return (f'<details class="card emb section"><summary>{esc(e["btn"])} · {esc(e["dlg"])}</summary>'
            f'<div class="embuild" data-cfg="{esc(json.dumps(emb_cfg(lang, aid), ensure_ascii=False))}"></div></details>')


def widgets_page(lang, ver):
    e = EMB[lang]
    body = (f'<h1>{esc(e["h1"])}</h1><p class="lead">{esc(e["d"])}</p>'
            f'<section class="card section"><div class="embuild" data-cfg="{esc(json.dumps(emb_cfg(lang, "btc") | dict(pickable=1), ensure_ascii=False))}"></div></section>'
            f'<section class="card section"><h2>{esc(e["how"])}</h2><p>{esc(e["help"])}</p><p class="muted">{esc(e["why"])}</p></section>')
    return shell(lang, 'widgets', f'{e["h1"]} | {BRAND}', e['d'], body, {}, ver)


def ic_page(lang, ver):
    """Full investment calculator on /compound-interest/ (ported from invest.mytimebox.app, 20 languages)."""
    t, S, TTl, U = IC[lang], TR[lang], TT[lang], TR[lang]['ui']
    code, rate = hccy(lang)
    sym = CCY_SYM.get(code, code)
    c = CPI_LANG.get(lang, 'USA')
    cpi = CPI['c'].get(c) or CPI['c'].get('USA') or {}
    infl = round(cpi[max(cpi)], 1) if cpi else 3.0
    # (id, label, rate %, tax-free, icon, colour, small note)
    insts = []
    if lang == 'uk':
        insts += [('ovdp', t['bond'], 15.0, 1, '🏛️', '#f0b53a', 'ПДФО 0%'), ('dep', t['dep'], 13.7, 0, '🏦', '#4f8cff', 'ПДФО+ВЗ 23%')]
    else:
        insts += [('dep', t['dep'], 4.0, 0, '🏦', '#4f8cff', ''), ('bond', t['bond'], 4.0, 0, '🏛️', '#f0b53a', '')]
    for aid, ic, col in (('spy', '📈', '#16a34a'), ('qqq', '💻', '#8b5cf6'), ('gold', '🥇', '#d97706')):
        r = cagr(aid)
        if r:
            insts.append((aid, nm(A[aid], lang), round(r * 100, 1), 0, ic, col, 'Ø 10Y · USD'))
    insts += [('cash', t['cashi'], 0.0, 0, '💵', '#ef4444', ''), ('custom', t['custom'], 10.0, 0, '✏️', '#64748b', '')]
    sel = 'ovdp' if lang == 'uk' else 'spy'
    p0, pm, yrs = nice(1000 * rate), nice(100 * rate), 10
    tax = 23 if lang == 'uk' else 0
    iv = lambda v: int(v) if float(v).is_integer() else v
    num = lambda i, lab, v, extra='', unit=True: (f'<label class="f">{esc(lab)}<div class="inp"><input id="{i}" type="number" min="0" step="any" value="{iv(v)}"{extra}>'
                                                 + (f'<span class=muted>{esc(sym)}</span>' if unit else '') + '</div></label>')
    seg = lambda i, opts, v: f'<div class="seg full" id="{i}">' + ''.join(f'<button type="button" data-v="{k}"{" class=on" if k == v else ""}>{esc(l)}</button>' for k, l in opts) + '</div>'
    cards = ''.join(f'<button type="button" class="icard{" on" if k == sel else ""}" data-v="{k}" data-r="{r}" data-tf="{tf}" style="--c:{col}"><span class="ii">{ic}</span>'
                    f'<b>{esc(l)}</b><span class="ir">{r:g}%</span>{f"<small>{esc(nt)}</small>" if nt else ""}</button>' for k, l, r, tf, ic, col, nt in insts)
    opts = ''.join(f'<option value="{k}" data-r="{r}" data-tf="{tf}" data-c="{col}"{" selected" if k == sel else ""}>{esc(l)}</option>' for k, l, r, tf, ic, col, nt in insts)
    rows = lambda ks: ''.join(f'<div class="kv"><span>{esc(lab)}</span><b id="{i}">—</b></div>' for i, lab in ks)
    left = (f'<section class="card icl"><h2>⚙️ {esc(t["inst"])}</h2><select id="ici" hidden>{opts}</select>'
            f'{num("icp", t["init"], p0)}{num("icm", t["month"], pm)}'
            f'<label class="f">{esc(t["years"])}: <b id="icyl">{yrs}</b><div class="icy2"><input type="range" id="icys" min="1" max="40" value="{yrs}"><div class="inp"><input id="icy" type="number" min="1" max="60" step="1" value="{yrs}"></div></div></label>'
            f'{num("icr", t["rate"], dict((x[0], x[2]) for x in insts)[sel], " step=0.1", False)}'
            f'<div class="f">{esc(t["scen"])}{seg("ics", [("o", "😊 " + t["opt"]), ("r", "😐 " + t["real"]), ("p", "😟 " + t["pes"])], "r")}</div>'
            f'<div class="f">{esc(t["comp"])}{seg("icc", [("m", t["cm"]), ("q", t["cq"]), ("h", t["ch"]), ("y", t["cy"])], "m" if lang != "uk" else "y")}</div>'
            f'<div class="icchk"><label class="chk"><input type="checkbox" id="icre" checked> {esc(t["reinv"])}</label>'
            f'<label class="chk"><input type="checkbox" id="icin" checked> {esc(t["infl"])}</label><div class="sub">{num("icir", t["infl_r"], infl, " step=0.1", False)}</div>'
            f'<label class="chk"><input type="checkbox" id="ictx"{" checked" if tax else ""}> {esc(t["tax"])}</label><div class="sub">{num("ictr", t["tax_r"], tax or 15, " step=0.5", False)}</div></div>'
            f'<div class="icsum">{rows([("ic_p0", t["init"]), ("ic_contrib", t["contrib"]), ("ic_interest", t["interest"]), ("ic_taxes", t["taxes"])])}'
            f'<div class="kv big"><span>💰 {esc(t["final"])}</span><b id="icv">—</b></div>'
            f'{rows([("ic_realv", t["realv"]), ("ic_cash", t["cash"])])}<p class="muted icnote2" id="ic_cashs"></p></div>'
            f'<div class="icbox fire"><h3>🔥 {esc(t["fire_h"])}</h3>{num("icx", t["fire_exp"], nice(800 * rate))}'
            f'<div class="tri"><div><b id="icfn">—</b><span>{esc(t["fire_need"])}</span></div><div><b id="icfy">—</b><span>{esc(t["fire_yrs"])}</span></div></div></div>'
            f'<div class="icbox inc"><h3>📈 {esc(t["fire_inc"])}</h3><div class="tri3"><div><b id="icid">—</b><span>{esc(U["per_d"])}</span></div>'
            f'<div><b id="iciw">—</b><span>{esc(U["per_w"])}</span></div><div><b id="icfi">—</b><span>{esc(U["per_m"])}</span></div></div></div>'
            f'<div class="icbox"><h3>🔄 {esc(t["rev_h"])}</h3>{num("icg", t["rev_goal"], nice(1e5 * rate))}<div class="kv"><span>{esc(t["rev_need"])}</span><b class="good" id="icgv">—</b></div></div>'
            f'<button type="button" class="btn ghost full" id="icsh">🔗 {esc(t["share"])}</button></section>')
    right = (f'<section class="card icr2"><h2>📊 <span id="iccmph"></span></h2><div id="iccmp" class="iccmp"></div><hr>'
             f'<h3>{esc(t["tbl_h"])}</h3><div id="icchart" class="icchart"></div>'
             f'<div class="glg"><span><i class="tl"></i>{esc(t["total"])}</span><span><i class="cl"></i>{esc(t["contrib"])}</span></div><hr>'
             f'<div class="icdon"><div id="icdonut"></div><div class="glg col"><span><i class="b"></i>{esc(t["interest"])} <b id="icdi"></b></span><span><i class="a"></i>{esc(t["contrib"])} <b id="icdc"></b></span></div></div><hr>'
             f'<div class="tw"><table class="tbl ictab" id="ictable"></table></div></section>')
    body = (f'<div class="icpage"><div class="ichero"><h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["d"])}</p></div>'
            f'<div class="icards">{cards}</div><div class="icgrid2">{left}{right}</div>'
            f'<p class="note">{esc(t["note"])}</p>'
            f'<section class="section"><div class="hgrid"><a class="card hcard" href="{url(lang, "millionaire")}"><span>🎯</span><b>{esc(TTl["g_h1"])}</b></a>'
            f'<a class="card hcard" href="{url(lang, "inflation")}"><span>📉</span><b>{esc(TTl["i_nav"])}</b></a><a class="card hcard" href="{url(lang, "compare")}"><span>⇅</span><b>{esc(S["cmp_h1"])}</b></a></div></section></div>')
    cfg = dict(ic=dict(code=code, yr=TTl['yr'], t={k: t[k] for k in ('cmp_h', 'cash_t', 'fire_never', 'year', 'contrib', 'interest', 'total', 'taxes')}))
    faq = {"@context": "https://schema.org", "@type": "WebApplication", "name": t['h1'], "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
           "offers": {"@type": "Offer", "price": "0"}, "description": t['d']}
    return shell(lang, 'compound-interest', t['title'] + ' | ' + BRAND, t['d'], body, cfg, ver, [faq])


def _calc_shell(t, cards, left, right, links):
    return (f'<div class="icpage"><div class="ichero"><h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["d"])}</p></div>'
            f'{cards}<div class="icgrid2">{left}{right}</div><p class="note">{esc(t["note"])}</p>'
            f'<section class="section"><div class="hgrid">{links}</div></section></div>')


def _calc_links(lang, keys):
    lab = {'compound-interest': ('📈', IC[lang]['nav']), 'dividends': ('💸', DV[lang]['nav']), 'average-price': ('⚖️', AV[lang]['nav']),
           'ovdp': ('🏛️', OV.get(lang, OV['en'])['nav']), 'millionaire': ('🎯', TT[lang]['g_h1']), 'compare': ('⇅', TR[lang]['cmp_h1'])}
    return ''.join(f'<a class="card hcard" href="{url(lang, k)}"><span>{lab[k][0]}</span><b>{esc(lab[k][1])}</b></a>' for k in keys if has_page(lang, k))


def _app_ld(t):
    return {"@context": "https://schema.org", "@type": "WebApplication", "name": t['h1'], "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
            "offers": {"@type": "Offer", "price": "0"}, "description": t['d']}


def _cnum(i, lab, v, sym='', extra=''):
    v = int(v) if float(v).is_integer() else v
    return (f'<label class="f">{esc(lab)}<div class="inp"><input id="{i}" type="number" min="0" step="any" value="{v}"{extra}>'
            + (f'<span class=muted>{esc(sym)}</span>' if sym else '') + '</div></label>')


DIV_SETS = [('schd', 3.3, 9.0, '#16a34a'), ('vym', 2.2, 6.0, '#4f8cff'), ('spy', 1.2, 6.0, '#8b5cf6'), ('ko', 2.9, 4.5, '#ef4444'), ('o', 5.5, 3.5, '#f0b53a')]


def dividends_page(lang, ver):
    t, U = DV[lang], TR[lang]['ui']
    code, rate = hccy(lang)
    sym = CCY_SYM.get(code, code)
    sets = []
    for aid, y, dg, col in DIV_SETS:
        if aid in A and (r := cagr(aid)):
            sets.append((aid, nm(A[aid], lang), y, dg, round(max(0.0, r * 100 - y), 1), col))
    sel = sets[0] if sets else ('custom', '', 3.0, 5.0, 5.0, '#16a34a')
    cards = '<div class="icards">' + ''.join(
        f'<button type="button" class="icard{" on" if s is sel else ""}" data-y="{s[2]}" data-dg="{s[3]}" data-pg="{s[4]}" style="--c:{s[5]}"><span class="ii">💸</span>'
        f'<b>{esc(s[1])}</b><span class="ir">{s[2]:g}%</span><small>+{s[3]:g}%/{esc(TT[lang]["yr"])} · {esc(A[s[0]]["tk"])}</small></button>' for s in sets) + '</div>'
    cards += f'<p class="muted icnote2" style="margin:-10px 0 16px">{esc(t["pre"])}: {esc(t["pre_note"])}</p>'
    left = (f'<section class="card icl"><h2>⚙️ {esc(t["nav"])}</h2>'
            f'{_cnum("dvp", t["init"], nice(1000 * rate), sym)}{_cnum("dvm", t["month"], nice(100 * rate), sym)}'
            f'<label class="f">{esc(t["yrs"])}: <b id="dvyl">20</b><div class="icy2"><input type="range" id="dvys" min="1" max="40" value="20"><div class="inp"><input id="dvy" type="number" min="1" max="60" step="1" value="20"></div></div></label>'
            f'{_cnum("dvr", t["yld"], sel[2], "", " step=0.1")}{_cnum("dvg", t["dg"], sel[3], "", " step=0.1")}{_cnum("dvq", t["pg"], sel[4], "", " step=0.1")}'
            f'<div class="icchk"><label class="chk"><input type="checkbox" id="dvre" checked> {esc(t["reinv"])}</label>{_cnum("dvt", t["tax"], 15, "", " step=0.5")}</div>'
            f'<div class="icsum"><div class="kv"><span>{esc(t["contrib"])}</span><b id="dv_c">—</b></div><div class="kv"><span>{esc(t["divs"])}</span><b class="good" id="dv_d">—</b></div>'
            f'<div class="kv big"><span>💰 {esc(t["final"])}</span><b id="dv_v">—</b></div></div>'
            f'<div class="icbox inc"><h3>📈 {esc(t["inc_m"])}</h3><div class="tri3"><div><b id="dv_m">—</b><span>{esc(U["per_m"])}</span></div>'
            f'<div><b id="dv_y">—</b><span>{esc(t["inc_y"])}</span></div><div><b id="dv_o">—</b><span>{esc(t["yoc"])}</span></div></div></div></section>')
    right = (f'<section class="card icr2"><h3>{esc(t["chart"])}</h3><div id="dvchart" class="icchart"></div><hr>'
             f'<div class="tw"><table class="tbl ictab" id="dvtable"></table></div></section>')
    body = _calc_shell(t, cards, left, right, _calc_links(lang, ['compound-interest', 'average-price', 'ovdp', 'millionaire']))
    cfg = dict(dv=dict(code=code, t={k: t[k] for k in ('year', 'val', 'contrib', 'divy')}))
    return shell(lang, 'dividends', t['title'] + ' | ' + BRAND, t['d'], body, cfg, ver, [_app_ld(t)])


AVG_ASSETS = ['btc', 'eth', 'sol', 'bnb', 'xrp', 'doge', 'ton', 'spy', 'qqq', 'aapl', 'nvda', 'tsla', 'msft', 'amzn', 'gold', 'silver']


def avgprice_page(lang, ver):
    t = AV[lang]
    opts = f'<option value="">{esc(t["pick"])}</option>' + ''.join(f'<option value="{a}">{esc(nm(A[a], lang))} ({esc(A[a]["tk"])})</option>' for a in AVG_ASSETS if a in A)
    seg = (f'<div class="seg full" id="avmode"><button type="button" data-v="s" class=on>{esc(t["m_sum"])}</button><button type="button" data-v="q">{esc(t["m_qty"])}</button></div>')
    left = (f'<section class="card icl"><h2>🧾 {esc(t["buy"])}</h2><div class="f">{esc(t["mode"])}{seg}</div>'
            f'<div class="tw"><table class="tbl avt"><thead><tr><th>#</th><th>{esc(t["price"])}</th><th id="avh2">{esc(t["sum"])}</th><th></th></tr></thead><tbody id="avrows"></tbody></table></div>'
            f'<div class="avbtns"><button type="button" class="btn ghost" id="avadd">{esc(t["add"])}</button><button type="button" class="btn ghost" id="avclr">{esc(t["reset"])}</button></div>'
            f'<hr><label class="f">{esc(t["asset"])}<div class="inp"><select id="avasset">{opts}</select></div></label>{_cnum("avcur", t["cur"], 0)}</section>')
    right = (f'<section class="card icr2"><div class="icsum"><div class="kv big"><span>⚖️ {esc(t["avg"])}</span><b id="av_a">—</b></div>'
             f'<div class="kv"><span>{esc(t["tqty"])}</span><b id="av_q">—</b></div><div class="kv"><span>{esc(t["cost"])}</span><b id="av_c">—</b></div>'
             f'<div class="kv"><span>{esc(t["pl"])}</span><b id="av_p">—</b></div></div>'
             f'<div class="icbox"><h3>🔻 {esc(t["tgt_h"])}</h3>{_cnum("avtg", t["tgt"], 0)}{_cnum("avbp", t["buy_at"], 0)}'
             f'<div class="kv"><span>{esc(t["need"])}</span><b class="good" id="av_n">—</b></div><p class="muted icnote2" id="av_nq"></p></div></section>')
    body = _calc_shell(t, '', left, right, _calc_links(lang, ['compound-interest', 'dividends', 'compare', 'millionaire']))
    cfg = dict(av=dict(t={k: t[k] for k in ('del', 'need_qty', 'imp', 'price', 'sum', 'qty')}))
    return shell(lang, 'average-price', t['title'] + ' | ' + BRAND, t['d'], body, cfg, ver, [_app_ld(t)])


# (currency, bond %, deposit %)
OVDP_CCY = [('UAH', 14.9, 13.7, '₴', '#f0b53a'), ('USD', 3.7, 0.8, '$', '#16a34a'), ('EUR', 3.2, 0.3, '€', '#4f8cff')]


def ovdp_page(lang, ver):
    t = OV[lang]
    cards = '<div class="icards">' + ''.join(
        f'<button type="button" class="icard{" on" if i == 0 else ""}" data-c="{c}" data-b="{b}" data-d="{d}" data-s="{s}" style="--c:{col}"><span class="ii">{s}</span>'
        f'<b>{t["b"]} {c}</b><span class="ir">{b:g}%</span><small>{esc(t["dp"])} {d:g}%</small></button>' for i, (c, b, d, s, col) in enumerate(OVDP_CCY)) + '</div>'
    terms = ''.join(f'<button type="button" data-v="{m}"{" class=on" if m == 12 else ""}>{m} {esc(t["m"])}</button>' for m in (6, 12, 24, 36))
    left = (f'<section class="card icl"><h2>⚙️ {esc(t["h1"])}</h2>{_cnum("ova", t["amt"], 100000, "₴")}'
            f'<div class="f">{esc(t["term"])}<div class="seg full" id="ovt">{terms}</div></div>'
            f'{_cnum("ovb", t["yld"], 14.9, "", " step=0.01")}{_cnum("ovd", t["dep"], 13.7, "", " step=0.01")}'
            f'<p class="muted icnote2">{esc(t["tax"])}: 23%</p><div id="ovdevw">{_cnum("ovv", t["dev"], 8, "", " step=0.5")}</div></section>')
    right = (f'<section class="card icr2"><div class="icsum"><div class="kv big"><span>🏛️ {esc(t["res_b"])}</span><b id="ov_b">—</b></div>'
             f'<div class="kv"><span>🏦 {esc(t["res_d"])} ({esc(t["net"])})</span><b id="ov_d">—</b></div>'
             f'<div class="kv"><span>{esc(t["diff"])}</span><b class="good" id="ov_x">—</b></div>'
             f'<div class="kv"><span>{esc(t["per_m"])}</span><b id="ov_m">—</b></div></div>'
             f'<div class="iccmp" id="ovbars"></div><div class="icbox" id="ovusd" style="margin-top:14px"><h3>💵 {esc(t["in_usd"])}</h3><div class="kv"><span>UAH → USD</span><b id="ov_u">—</b></div></div>'
             f'<p class="muted icnote2">{esc(t["src"])}</p></section>')
    body = _calc_shell(t, cards, left, right, _calc_links(lang, ['compound-interest', 'dividends', 'average-price']))
    cfg = dict(ov=dict(b=t['b'], dp=t['dp']))
    return shell(lang, 'ovdp', t['title'] + ' | ' + BRAND, t['d'], body, cfg, ver, [_app_ld(t)])


# search aliases: local names / transliterations people type (uk, ru, pl, de...)
ALIAS = {
    'btc': 'біткоїн біткоін біткойн биткоин биткойн бітка битка bitcoin', 'eth': 'ефір ефіріум етеріум эфир эфириум эфириум ether',
    'sol': 'солана', 'xrp': 'ріпл рипл', 'doge': 'доге дог догекоїн догикоин', 'ada': 'кардано', 'bnb': 'бнб бінанс бинанс',
    'trx': 'трон', 'ton': 'тон', 'ltc': 'лайткоїн лайткоин', 'dot': 'полкадот', 'link': 'чейнлінк чейнлинк', 'avax': 'аваланч',
    'usdt': 'тезер тетер', 'shib': 'шиба', 'pepe': 'пепе',
    'aapl': 'епл еппл епл апл эпл эппл айфон', 'msft': 'майкрософт мікрософт', 'nvda': 'нвідіа нвидиа нвідія нвидия', 'tsla': 'тесла',
    'amzn': 'амазон', 'googl': 'гугл google alphabet', 'goog': 'гугл google', 'meta': 'мета фейсбук facebook', 'nflx': 'нетфлікс нетфликс',
    'amd': 'амд', 'intc': 'інтел интел', 'tsm': 'тсмс', 'pltr': 'палантир', 'ko': 'кока-кола кока кола', 'pep': 'пепсі пепси',
    'spy': 'с&п sp500 с&п500 снп s&p500 сп500', 'qqq': 'насдак nasdaq', 'vt': 'весь світ world',
    'gold': 'золото gold злото xau', 'silver': 'срібло серебро silver srebro', 'platinum': 'платина', 'copper': 'мідь медь',
    'wti': 'нафта нефть oil ропа', 'brent': 'брент нафта нефть', 'natgas': 'газ gas', 'wheat': 'пшениця пшеница', 'coffee': 'кава кофе',
}


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
            f'<span class="tk">{esc(a["tk"])}{'<i class="enb" title="English">EN</i>' if lang != 'en' and not has_page(lang, aid) else ''}</span></span></a></td><td class="hide-sm"></td><td class="num" data-p="{aid}">{price(m["price"])}</td>'
            f'<td class="num {cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</td><td class="num hide-sm {cls(m["r1"])}">{pct(m["r1"])}</td>'
            f'<td class="num hide-sm {cls(m["r3"])}">{pct(m["r3"])}</td><td><span class="pill {cls(m["r5"])}">{pct(m["r5"])}</span></td>'
            f'<td class="hide-sm">{spark(m["spark"])}</td><td class="hide-sm"><a class="calc" href="{href}">→</a></td></tr>')


def table_block(lang, ids, title=None, interactive=True):
    u = TR[lang]['ui']
    head = ['#', u['name'], '', u['price'], u['chg'], u['d1'], u['d3'], u['d5'], u['spark'], '']
    hc = ['l n hide-sm', 'l', 'hide-sm', '', '', 'hide-sm', 'hide-sm', '', 'hide-sm', 'hide-sm']
    th = ''.join(f'<th class="{c}">{h}</th>' for h, c in zip(head, hc))
    rows = ''.join(row_html(aid, lang, k + 1) for k, aid in enumerate(ids))
    ttl = f'<h2>{title}</h2>' if title else ''
    if interactive == 'top':
        rows = ''.join(row_html(aid, lang, k + 1) for k, aid in enumerate(ids[:10]))
        rows2 = ''.join(row_html(aid, lang, k + 11) for k, aid in enumerate(ids[10:]))
        top = f'<div class="tw"><table class="mt"><thead id="mthead"><tr>{th}</tr></thead><tbody id="mt">{rows}</tbody></table><div id="mttop"></div></div>'
        rest = (f'<section class="section" id="rank2"><h2>{title}</h2><div class="tw"><table class="mt"><thead id="mthead2"><tr>{th}</tr></thead>'
                f'<tbody id="mt2">{rows2}</tbody></table><div id="mtmore"></div></div></section>')
        return top, rest
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
    w = NUMFMT[CUR_FMT[0]][3]
    return _money(_num(v / 1e12, 2) + NBSP + w[3]) if v >= 1e12 else _money(_num(v / 1e9, 1) + NBSP + w[2])


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
    hm = HM[lang]
    title, desc = hm['title'], hm['desc'].format(n=n)
    # --- hero with quick calculator
    qopts = ''.join(f'<option value="{aid}"{" selected" if aid == "btc" else ""}>{esc(nm(A[aid], lang))} ({esc(A[aid]["tk"])})</option>' for aid in ids[:120])
    yrs = ''.join(f'<button data-y="{y}" class="{"on" if y == 5 else ""}">{y}</button>' for y in (1, 3, 5, 10))
    b5 = simulate('btc', END_I - 60) if 'btc' in A else None
    cta_ref = f'<a class="btn" id="ctaBuy" href="{url(lang, "exchanges")}">{w["cta"]}</a>'
    fv0 = (G.get('fng') or [None])[0]
    def ptile(i):
        mm = METRICS[i]
        return (f'<a class="pt" href="{aurl(lang, i)}"><span class="ptn">{icon(A[i])}<b>{esc(nm(A[i], lang))}</b></span>'
                f'<span class="ptp" data-p="{i}">{price(mm["price"])}</span><span class="ptc {cls(mm["chg"])}" data-c="{i}">{pct(mm["chg"])}</span>'
                f'{spark(mm["spark"], 120, 30)}</a>')
    pulse = ''.join(ptile(i) for i in ('btc', 'eth', 'spy', 'gold') if i in A)
    if fv0 is not None:
        pulse += (f'<a class="pt ptf" href="{url(lang, "news")}"><span class="ptn"><b>{w["fng"]}</b></span><span class="ptp">{fv0}<small>/100</small></span>'
                  f'<span class="ptc">{fng_label(lang, fv0)}</span><span class="fbar"><i style="left:{fv0}%"></i></span></a>')
    tools = [('compare', '⇅', S['nav_cmp']), ('compound-interest', '📈', IC[lang]['nav']), ('dividends', '💸', DV[lang]['nav']),
             ('portfolios', '🧺', BP[lang]['nav']), ('exchanges', '🏦', EX[lang]['nav'])]
    tchips = ''.join(f'<a class="tch" href="{url(lang, k)}"><span>{ic}</span>{esc(lb)}</a>' for k, ic, lb in tools)
    hero = (f'<section class="herox hx2"><div class="hx"><h1>{esc(hm["h1"])}</h1><p class="lead">{esc(hm["lead"])}</p>'
            f'<div class="pulse">{pulse}</div>{country_chips(lang, limit=8)}</div>'
            f'<div class="card qcalc" id="qcalc"><div class="qt qth">{S["home_h1"].format(ten=TEN)}</div>'
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
    trend = [s.lower() for s in (G.get('trending') or []) if s.lower() in A and (A[s.lower()].get('mcap') or 0) >= 1e8][:5]
    if not trend:
        trend = [i for i in ids if A[i]['cat'] == 'crypto'][:5]
    w_tr = (f'<div class="card wd"><div class="wt">🔥 {w["trending"]}</div>' +
            ''.join(mini_row(lang, i, f'<span class="mc {cls(METRICS[i]["chg"])}" data-c="{i}">{pct(METRICS[i]["chg"])}</span>') for i in trend) + '</div>')
    big = lambda i: A[i]['cat'] != 'crypto' or (A[i].get('mcap') or 0) >= 1e9   # no micro-caps on the home page
    movers = [i for i in ids if METRICS[i]['chg'] is not None and ORD[i] < 400 and big(i)]
    up = sorted(movers, key=lambda i: -METRICS[i]['chg'])[:6]
    dn = sorted(movers, key=lambda i: METRICS[i]['chg'])[:6]
    w_up = f'<div class="card wd"><div class="wt">🚀 {w["gainers"]}</div>' + ''.join(mini_row(lang, i, f'<span class="mc good">{pct(METRICS[i]["chg"])}</span>') for i in up) + '</div>'
    w_dn = f'<div class="card wd"><div class="wt">📉 {w["losers"]}</div>' + ''.join(mini_row(lang, i, f'<span class="mc bad">{pct(METRICS[i]["chg"])}</span>') for i in dn) + '</div>'
    bat = [i for i in ('btc', 'eth', 'nvda', 'aapl', 'spy', 'qqq', 'gold', 'silver') if i in A and METRICS[i]['r5'] is not None]
    bat.sort(key=lambda i: -METRICS[i]['r5'])
    mx = max([simulate(i, END_I - 60)['val'] for i in bat] or [1])
    rows = ''
    for i in bat:
        r = simulate(i, END_I - 60)
        rows += (f'<a class="brow" href="{aurl(lang, i)}"><span class="bn">{icon(A[i])}{esc(nm(A[i], lang))}</span>'
                 f'<span class="bb"><i style="width:{max(2, r["val"] / mx * 100):.1f}%" class="{cls(r["roi"])}"></i></span><b>{usd_h(r["val"])}</b></a>')
    inv5 = usd(simulate(bat[0], END_I - 60)['inv']) if bat else ''
    w_bat = f'<div class="card wd battle"><div class="wt">⚔️ {w["battle"]}</div><div class="ws">{w["q_inv"]}: {inv5}</div>{rows}</div>'
    X_ = S['x']
    banner = (f'<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div>'
              f'<a class="btn" id="ctaBuy2" href="{url(lang, "exchanges")}">{w["cta"]} →</a></section>')
    # DCA leaders cards (as before)
    cards = []
    b1, b5l = best_by('r1', [i for i in ids if big(i)]), best_by('r5', [i for i in ids if big(i)])
    bc = best_by('r1', [i for i in ids if A[i]['cat'] == 'crypto' and ORD[i] < 60 and big(i)])
    if b1: cards.append(hl_card(lang, b1[0], S['hl1'], 'r1', S['sub1']))
    if b5l: cards.append(hl_card(lang, b5l[0], S['hl5'], 'r5', S['sub5']))
    if bc: cards.append(hl_card(lang, bc[0], S['hlc'], 'r1', S['sub1']))
    for aid in ('btc', 'spy', 'gold'):
        if aid in A and len(cards) < 4:
            cards.append(hl_card(lang, aid, nm(A[aid], lang), 'r5', S['sub5']))
    filt = f'<div class="toolbar"><div class="filter">{SEARCH_ICON}<input id="flt" type="search" autocomplete="off"></div></div>'
    top10 = table_block(lang, HOME_ORDER[:20], None, interactive=True)
    rest = ''
    tl = news_tl(lang)
    nws = news_items(lang)[:4]
    w_news = (f'<div class="card wd wnews"><div class="wt">📰 {esc(hm["news"])}</div><div class="nlist own">' + ''.join(news_row(lang, k, m, tl) for k, m in nws)
              + f'</div><a class="calc" href="{url(lang, "news")}">{esc(hm["all"])} →</a></div>') if nws else w_tr
    def mv(cat, sign):
        pool = [i for i in ids if A[i]['cat'] == cat and METRICS[i]['chg'] is not None and big(i) and ORD[i] < (400 if cat == 'crypto' else 900)]
        pool.sort(key=lambda i: -sign * METRICS[i]['chg'])
        pool = [i for i in pool if sign * METRICS[i]['chg'] > 0][:5]
        ttl = f'{"🚀" if sign > 0 else "📉"} {S["ui"][cat]} · {w["gainers"] if sign > 0 else w["losers"]}'
        return (f'<div class="card wd"><div class="wt">{esc(ttl)}</div>'
                + ''.join(mini_row(lang, i, f'<span class="mc {"good" if sign > 0 else "bad"}">{pct(METRICS[i]["chg"])}</span>') for i in pool) + '</div>')
    today = (f'<section class="section today"><h2>{esc(hm["today"])}</h2><div class="tgrid">'
             f'{mv("crypto", 1)}{mv("crypto", -1)}{mv("stock", 1)}{mv("stock", -1)}{w_news}</div></section>')
    body = (hero + today + offer_card(lang, 'home') + f'<section class="section toprank"><div class="tabs" id="tabs"></div>{filt}{top10}</section>'
            f'<div class="wgrid3">{w_tr if nws else w_fng}<div class="wstack">{w_mcap}{w_dom}</div>{w_bat}</div>{banner}{habits_strip(lang)}{poll_block(lang)}{poly_block(lang)}'
            f'<section class="section"><div class="hl">{"".join(cards)}</div></section>'
            f'{rest}'
            f'<section class="card section faq"><h2>{S["faq"]}</h2><details open><summary>{esc(S["q3"])}</summary><p>{esc(S["a3"])}</p></details></section>')
    jsonld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": BRAND, "url": SITE + url(lang),
               "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "inLanguage": S['loc'],
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc},
              {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "alternateName": ["WhatIfStack", "whatifstack", "whatifstack.com", "What If Stack"],
               "url": SITE + '/', "inLanguage": S['loc'],
               "potentialAction": {"@type": "SearchAction", "target": SITE + url(lang) + '?q={search_term_string}', "query-input": "required name=search_term_string"}},
              {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "alternateName": "whatifstack", "url": SITE + '/',
               "logo": SITE + '/assets/icon-512.png', "sameAs": [u for _, u in SOCIAL],
               "description": "Independent markets site: live prices, news and calculators for crypto, stocks and gold, in plain language and 20 languages."}]
    return shell(lang, None, title, desc, body, dict(home=True, wa=WA[lang]['nav'], wau=url(lang, 'world-assets')), ver, jsonld)


def compare(lang, ver):
    S = TR[lang]
    sel = [i for i in ('btc', 'nvda', 'gold', 'spy', 'eth') if i in A]
    body = f'<h1>{S["cmp_h1"]}</h1><p class="lead">{S["cmp_lead"]}</p>{calc_block(lang)}'
    return shell(lang, 'compare', S['cmp_title'], S['cmp_desc'], body, dict(sel=sel, since=i2ym(END_I - 60)), ver)


def default_since(aid):
    """Site-wide default: the last 5 years (same as the DCA 5y column and the home calculator), or since launch."""
    s0 = ym2i(A[aid]['start'])
    return i2ym(max(s0, END_I - 60))


def bench(aid):
    for b in ('btc', 'spy', 'qqq', 'gold'):
        if b != aid and b in A:
            yield b


def _jload(name):
    f = os.path.join(ROOT, 'data', name)
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}


COININFO, STOCKINFO = _jload('coininfo.json'), _jload('stockinfo.json')
STOCKSTATS = _jload('stockstats.json')   # key stats from scripts/stock_stats.py (rotating daily refresh)


def to_usd(v, ccy):
    """Amount in a listing/report currency -> USD (None if the rate is unknown)."""
    if v is None:
        return None
    c, k = (ccy or 'USD'), 1.0
    if c in ('GBp', 'GBX'):
        c, k = 'GBP', 0.01
    elif c == 'ILA':
        c, k = 'ILS', 0.01
    elif c == 'ZAc':
        c, k = 'ZAR', 0.01
    if c == 'USD':
        return v * k
    rate = FX.get('rates', {}).get(c)
    return v * k / rate if rate else None


for _sym, _st in STOCKSTATS.items():   # stats refresh the older profile file; market cap always stored in USD
    _m = to_usd(_st.get('mcap'), _st.get('ccy'))
    STOCKINFO[_sym] = {**STOCKINFO.get(_sym, {}), **{k: v for k, v in _st.items() if k in ('web', 'sec', 'ind', 'cty', 'emp', 'ds')}}
    if _m:
        STOCKINFO[_sym]['mcap'] = _m


def fnum(v, money=False):
    if v is None:
        return '—'
    w = NUMFMT[CUR_FMT[0]][3]
    for d, k in ((1e12, 3), (1e9, 2), (1e6, 1)):
        if abs(v) >= d:
            body = _num(v / d, 2) + NBSP + w[k]
            return _money(body) if money else body
    return _money(_num(v, 0)) if money else _num(v, 0)


def fbig(v):
    return fnum(v, money=True)


def auto_about(lang, aid):
    """Plain-language facts from the monthly price series, for assets without a written profile (20 languages)."""
    a, T, S = A[aid], AUTO_AB[lang], TR[lang]
    p = [v for v in (a.get('p') or [])]
    if len(p) < 3:
        return ''
    y0, m0 = map(int, a['start'].split('-'))
    def lab(k):
        y, m = y0 + (m0 - 1 + k) // 12, (m0 - 1 + k) % 12 + 1
        return {'ja': f'{y}年{m}月', 'zh': f'{y}年{m}月', 'ko': f'{y}년 {m}월'}.get(lang) or f"{S['months'][m - 1]} {y}"
    ok = [(k, v) for k, v in enumerate(p) if v]
    if len(ok) < 3:
        return ''
    k0 = ok[0][0]
    out = []   # category sentence (T[0]) is covered by the 'What it is' paragraph
    kh, hi = max(ok, key=lambda kv: kv[1])
    last = ok[-1][1]
    out.append(T[2].format(hi=price(hi)) if kh == ok[-1][0] else T[1].format(hi=price(hi), hid=lab(kh), dd=f"{(1 - last / hi) * 100:.0f}%"))
    tail = ok[-13:]
    n = len(tail) - 1
    if n >= 6:
        out.append(T[3].format(n=n, pos=sum(1 for (_, x), (_, y) in zip(tail, tail[1:]) if y > x)))
    yr = {}
    for k, v in ok:
        yr.setdefault(y0 + (m0 - 1 + k) // 12, []).append((k, v))
    prev, rets = None, {}
    for y in sorted(yr):
        if prev is not None and (m0 - 1 + yr[y][-1][0]) % 12 == 11:   # full calendar years only
            rets[y] = yr[y][-1][1] / prev - 1
        prev = yr[y][-1][1]
    if len(rets) >= 2:
        by, wy = max(rets, key=rets.get), min(rets, key=rets.get)
        out.append(T[4].format(by=by, br=pct(rets[by]), wy=wy, wr=pct(rets[wy])))
    return ' '.join(out)


def side_block(lang, aid):
    """About card next to the chart (like CryptoRank): what the company/coin is and does, plus a few stable facts and links.
    No auto-generated, ever-changing numbers here (owner's request)."""
    a, t, T = A[aid], INF[lang], PROF_T[lang]
    rows, links, desc, dlang = [], [], None, lang
    def row(k, v):
        rows.append(f'<div class="ir"><span>{esc(k)}</span><b>{v}</b></div>')
    if a['cat'] == 'crypto':
        ci = COININFO.get(a.get('cgid') or '', {})
        if a.get('rank'): row('#', str(a['rank']))
        if a.get('mcap'): row(t['mcap'], fbig(a['mcap']))
        if a.get('circ'): row(t['circ'], f"{fnum(a['circ'])} {esc(a['tk'])}")
        row(t['max'], f"{fnum(a['maxs'])} {esc(a['tk'])}" if a.get('maxs') else '∞')
        if a.get('ath'): row(t['ath'], f"{price(a['ath'])} <small class=\"muted\">{esc(a.get('athd') or '')}</small>")
        L = ci.get('l', {})
        for k, lab in (('web', t['web']), ('wp', t['wp']), ('exp', t['exp']), ('x', 'X'), ('tg', 'Telegram'), ('gh', t['src'])):
            if L.get(k): links.append((L[k], lab))
        ds = ci.get('ds', {})
        desc = ds.get(lang) or ds.get('en')
        dlang = lang if ds.get(lang) else 'en'
    else:
        si = STOCKINFO.get(a.get('yahoo') or '', {})
        if si.get('sec') or a.get('sector'): row(t['sector'], esc(si.get('sec') or a.get('sector')))
        if si.get('ind'): row(t['industry'], esc(si['ind']))
        if si.get('cty'): row(t['country'], esc(si['cty']))
        if si.get('emp'): row(t['emp'], f"{si['emp']:,}".replace(',', ' '))
        if si.get('mcap'): row(t['mcap'], fbig(si['mcap']))
        if si.get('web'): links.append((si['web'], t['web']))
        desc = (si.get('ds') or {}).get('en')
        dlang = 'en'
    prof = PROFILES.get(lang, {}).get(aid)
    what = T['c_' + a['cat']].format(name=nm(a, lang), tk=a['tk'])
    own = DESC.get(lang, {}).get(aid)
    if own:                          # our localized short description wins over source texts
        desc, dlang = own, lang
    elif dlang != lang:              # never show a foreign-language text: generic line + facts until translated
        desc = None
    if own:
        body = f'<div class="sclip"><p>{esc(own)}</p></div>'
    elif prof and prof.get('kind') != 'analysis':
        body = f'<div class="artbody iprof sclip">{md(prof["body"], lang)}</div>'
    elif desc:
        body = f'<p class="swhat">{esc(what)}</p><div class="sclip"{"" if dlang == lang else f" lang=\"{dlang}\""}><p>{esc(desc)}</p></div>'
    elif a['cat'] in ('stock', 'etf') and tv_symbol(a) and lang == 'en':   # no English description fetched yet -> TradingView profile
        body = tvw('symbol-profile', dict(width='100%', height='100%', isTransparent=True, colorTheme='light', symbol=tv_symbol(a), locale=TV_LOC.get(lang, 'en')), 400)
    else:
        body = f'<p class="swhat">{esc(what)}</p>'
    lk = ''.join(f'<a class="chip" href="{esc(u)}" target="_blank" rel="nofollow noopener">{esc(l)} ↗</a>' for u, l in links)
    return (f'<aside class="card side"><h2>{esc(nm(a, lang))} <span class="muted">{esc(a["tk"])}</span></h2>{body}'
            f'<button class="smore" type="button" data-less="{esc(t["less"])}" hidden>{esc(t["more"])}</button>'
            + (f'<div class="srows">{"".join(rows)}</div>' if rows else '') + (f'<div class="ilinks">{lk}</div>' if lk else '') + '</aside>')


def long_block(lang, aid):
    """Full description lower on the page (CryptoRank-style): our hand-written profile, or the source text in the page language."""
    a, prof, own = A[aid], PROFILES.get(lang, {}).get(aid), DESC.get(lang, {}).get(aid)
    if prof and own:
        return (f'<section class="card section long"><h2>{esc(prof.get("title") or nm(a, lang))}</h2>'
                f'<div class="artbody iprof">{md(prof["body"], lang)}</div></section>')
    if a['cat'] == 'crypto':
        src = (COININFO.get(a.get('cgid') or '', {}).get('ds') or {}).get(lang)
    else:
        src = (STOCKINFO.get(a.get('yahoo') or '', {}).get('ds') or {}).get('en') if lang == 'en' else None
    if own and src and src.strip() != own.strip():
        return (f'<section class="card section long"><h2>{esc(INF[lang]["about"])} {esc(nm(a, lang))}</h2>'
                + ''.join(f'<p>{esc(x.strip())}</p>' for x in src.split('\n') if x.strip()) + '</section>')
    return ''


def info_block(lang, aid):
    a, t = A[aid], INF[lang]
    rows, links, desc = [], [], None
    def row(k, v, sub=''):
        rows.append(f'<div class="ir"><span>{esc(k)}</span><b>{v}</b>{sub}</div>')
    pr = METRICS[aid]['price']
    if a['cat'] == 'crypto':
        ci = COININFO.get(a.get('cgid') or '', {})
        if a.get('mcap'): row(t['mcap'], fbig(a['mcap']))
        if a.get('fdv'): row(t['fdv'], fbig(a['fdv']))
        if a.get('vol'):
            row(t['vol'], fbig(a['vol']))
            if a.get('mcap'): row(t['volm'], f"{a['vol'] / a['mcap']:.4f}")
        if a.get('circ'):
            bar = ''
            if a.get('maxs'):
                k = min(1, a['circ'] / a['maxs'])
                bar = f'<div class="ibar"><i style="width:{k * 100:.1f}%"></i></div><small class="muted">{k * 100:.1f}% / {esc(t["max"].lower())}</small>'
            row(t['circ'], f"{fnum(a['circ'])} {esc(a['tk'])}", bar)
        if a.get('supply'): row(t['total'], f"{fnum(a['supply'])} {esc(a['tk'])}")
        row(t['max'], f"{fnum(a['maxs'])} {esc(a['tk'])}" if a.get('maxs') else '∞')
        if a.get('ath'):
            row(t['ath'], f"{price(a['ath'])} <small class=\"muted\">{esc(a.get('athd') or '')}</small>", f'<small class="{cls(pr / a["ath"] - 1)}">{pct(pr / a["ath"] - 1)}</small>')
        if a.get('atl'):
            row(t['atl'], f"{price(a['atl'])} <small class=\"muted\">{esc(a.get('atld') or '')}</small>", f'<small class="good">{pct(pr / a["atl"] - 1)}</small>')
        L = ci.get('l', {})
        for k, lab in (('web', t['web']), ('wp', t['wp']), ('exp', t['exp']), ('x', 'X'), ('tg', 'Telegram'), ('rd', 'Reddit'), ('gh', t['src'])):
            if L.get(k):
                links.append((L[k], lab))
        ds = ci.get('ds', {})
        desc = ds.get(lang) or (ds.get('en') if lang == 'en' else None)   # never show English text on other-language pages
    else:
        si = STOCKINFO.get(a.get('yahoo') or '', {})
        if si.get('mcap'): row(t['mcap'], fbig(si['mcap']))
        if si.get('sec') or a.get('sector'): row(t['sector'], esc(si.get('sec') or a.get('sector')))
        if si.get('ind'): row(t['industry'], esc(si['ind']))
        if si.get('cty'): row(t['country'], esc(si['cty']))
        if si.get('emp'): row(t['emp'], f"{si['emp']:,}".replace(',', ' '))
        if si.get('web'): links.append((si['web'], t['web']))
        desc = (si.get('ds') or {}).get('en') if lang == 'en' else None
    prof = PROFILES.get(lang, {}).get(aid)
    auto = '' if prof else auto_about(lang, aid)
    if not rows and not links and not desc and not prof and not auto:
        return ''
    lk = ''.join(f'<a class="chip" href="{esc(u)}" target="_blank" rel="nofollow noopener">{esc(l)} ↗</a>' for u, l in links)
    about = ''
    if prof:
        about = (f'<section class="card iabout"><h2>{esc(prof.get("title") or (t["about"] + " " + nm(a, lang)))}</h2>'
                 f'<div class="artbody iprof">{md(prof["body"], lang)}</div>'
                 + (f'<h3>{esc(t["links"])}</h3><div class="ilinks">{lk}</div>' if lk else '') + '</section>')
    elif desc or lk or auto:
        T = PROF_T[lang]
        what = T['c_' + a['cat']].format(name=nm(a, lang), tk=a['tk'])
        if a['cat'] == 'crypto' and a.get('rank'):
            what += ' ' + T['rank'].format(rank=a['rank'])
        mc = a.get('mcap') if a['cat'] == 'crypto' else (STOCKINFO.get(a.get('yahoo') or '', {}) or {}).get('mcap')
        if mc:
            what += ' ' + T['mcap'].format(mcap=fbig(mc))
        about = (f'<section class="card iabout"><h2>{esc(t["about"])} {esc(nm(a, lang))}</h2>'
                 f'<div class="iprof"><h3>{esc(T["hw"])}</h3><p>{esc(what)}</p>'
                 + (f'<h3>{esc(T["hf"])}</h3><p class="iauto">{esc(auto)}</p>' if auto else '')
                 + f'<h3>{esc(T["hr"])}</h3><p>{esc(T["r_" + a["cat"]])}</p><p class="muted"><small>{esc(T["na"])}</small></p></div>'
                 + (f'<details class="idesc"><summary><span class="ip">{esc(desc[:220])}{"…" if len(desc) > 220 else ""}</span><span class="im">{esc(t["more"])}</span></summary><p>{esc(desc)}</p></details>' if desc else '')
                 + (f'<h3>{esc(t["links"])}</h3><div class="ilinks">{lk}</div>' if lk else '') + '</section>')
    stats = f'<section class="card istats"><h2>{esc(t["title"])}</h2>{"".join(rows)}</section>' if rows else ''
    return f'<div class="cols2 section info">{stats}{about}</div>'


def seas_block(lang, aid):
    a, t = A[aid], SEA[lang]
    cfg = esc(json.dumps(dict(id=aid, bn=(a.get('binance') or (a['tk'] + 'USDT' if a['cat'] == 'crypto' and a.get('src') == 'yahoo' else '')), t=t), ensure_ascii=False))
    return (f'<section class="section seas" id="seas" data-cfg="{cfg}"><div class="seasc" id="seasc"></div><div class="card seasbox">'
            f'<div class="seash"><h2>{esc(t["title"].format(name=nm(a, lang) + " (" + a["tk"] + ")"))}</h2><div class="seg" id="seasm"></div></div>'
            f'<div class="seasw" id="seasg"><div class="bload"><i></i></div></div></div></section>')


def local_price(a, lang):
    if not a.get('lp') or a.get('ccy', 'USD') == 'USD':
        return ''
    v, c = a['lp'], a['ccy']
    t = (f"{v:,.0f}" if v >= 1000 else f"{v:,.2f}").replace(',', ' ') + ' ' + CCY_SIGN.get(c, c)
    return f'<span class="lp" title="{esc(CTRY[lang][2])}">{esc(CTRY[lang][2])}: <b>{t}</b></span>'



def pctu(p):
    return pct(p).lstrip('+')


def stock_stats(a):
    return STOCKSTATS.get(a.get('yahoo') or '', {}) if a.get('cat') in ('stock', 'etf') else {}


def stock_ctry(lang, a, st):
    mk = a.get('mkt') or ('us' if (st.get('cty') or 'United States') == 'United States' else None)
    try:
        return CTRY[lang][3][mk][0] if mk else st.get('cty', '')
    except (KeyError, IndexError, TypeError):
        return st.get('cty', '')


def stock_facts(lang, aid):
    """Key numbers for a stock in display form (USD), or {} when there is no data."""
    a, m = A[aid], METRICS[aid]
    st = stock_stats(a)
    if not st:
        return {}
    k, c = KS[lang], st.get('ccy')
    cur = m['price']
    lc = to_usd(1.0, c) or None   # local listing currency -> USD factor for per-share values
    tgt = st['tgt'] * lc if st.get('tgt') and lc else None
    h52 = st['h52'] * lc if st.get('h52') and lc else None
    l52 = st['l52'] * lc if st.get('l52') and lc else None
    fc = st.get('fcy') or c
    # dividend yield from the dividend per share (yfinance's own yield field switched units between versions)
    dy = (st['dps'] * lc / cur) if st.get('dps') and lc and cur else (st.get('dy') if (st.get('dy') or 0) < 0.25 else None)
    f = dict(name=nm(a, lang), tk=a['tk'], sec=SECT[lang].get(st.get('sec'), st.get('sec') or ''), cty=stock_ctry(lang, a, st),
             mcap=to_usd(st.get('mcap'), c), rev=to_usd(st.get('rev'), fc), ni=to_usd(st.get('ni'), fc), revg=st.get('revg'), pm=st.get('pm'),
             pe=st.get('pe'), dy=dy, beta=st.get('beta'), tgt=tgt, h52=h52, l52=l52, cur=cur, n=st.get('nan'),
             rec=k.get(st.get('rec') or '', None), ern=st.get('ern'), emp=st.get('emp'), d=st.get('d', ''))
    return f


def _when(ts, lang):
    try:
        d = datetime.fromtimestamp(int(ts), timezone.utc).date()
    except (TypeError, ValueError, OSError):
        return None
    return d if d >= date.fromisoformat(UPDATED[:10]) else None


def stock_summary(lang, f):
    k = KS[lang]
    out = []
    if f.get('sec') and f.get('cty'):
        out.append(k['s_intro'].format(name=f['name'], tk=f['tk'], sec=f['sec'], cty=f['cty']))
    if f.get('mcap'):
        out.append(k['s_size'].format(mcap=usd(f['mcap'])))
    if f.get('rev') and f.get('revg') is not None:
        out.append(k['s_rev'].format(rev=usd(f['rev']), revg=pct(f['revg'])))
    if f.get('ni') is not None and f.get('rev'):
        if f['ni'] > 0 and f.get('pm'):
            out.append(k['s_profit'].format(pm=usd(100 * f['pm'])))
        elif f['ni'] < 0:
            out.append(k['s_loss'].format(ni=usd(-f['ni'])))
    if f.get('pe') and 0 < f['pe'] < 500:
        out.append(k['s_pe'].format(pe=_num(f['pe'], 0 if f['pe'] >= 10 else 1)))
    if f.get('h52') and f.get('l52') and f.get('cur') and f['h52'] > f['l52']:
        out.append(k['s_52'].format(below=pctu(max(0, 1 - f['cur'] / f['h52'])), above=pctu(max(0, f['cur'] / f['l52'] - 1))))
    if f.get('dy'):
        out.append(k['s_div'].format(dy=pctu(f['dy'])))
    elif f.get('mcap'):
        out.append(k['s_nodiv'])
    if f.get('rec') and f.get('n') and f.get('tgt') and f.get('cur'):
        out.append(k['s_an'].format(n=f['n'], rec=f['rec'], tgt=usd(f['tgt']), up=pct(f['tgt'] / f['cur'] - 1)))
    return out


def stock_block(lang, aid):
    """Key numbers + plain-language summary + analysts for stocks/ETFs with Yahoo stats (20 languages)."""
    f = stock_facts(lang, aid)
    if not f:
        return ''
    k = KS[lang]
    tiles = []
    def tile(lab, val, sub=''):
        tiles.append(f'<div class="ks"><span>{esc(lab)}</span><b>{val}</b>{f"<small>{sub}</small>" if sub else ""}</div>')
    wr = world_rank(aid)
    if f.get('mcap'): tile(k['mcap'], usd_h(f['mcap']), f'<a href="{url(lang, "largest-companies")}">{esc(LC[lang]["world"].format(n=wr))}</a>' if wr else '')
    yc = year_chg(aid)
    if yc is not None: tile(LC[lang]['year'], f'<span class="{cls(yc)}">{pct(yc)}</span>')
    if f.get('pe') and f['pe'] > 0: tile(k['pe'], _num(f['pe'], 1))
    tile(k['div'], pctu(f['dy']) if f.get('dy') else esc(k['divno']))
    if f.get('rev'): tile(k['rev'], usd_h(f['rev']), f'<span class="{cls(f.get("revg"))}">{pct(f["revg"])}</span>' if f.get('revg') is not None else '')
    if f.get('ni') is not None: tile(k['ni'], f'<span class="{cls(f["ni"])}">{"−" if f["ni"] < 0 else ""}{usd_h(abs(f["ni"]))}</span>', f'{esc(k["pm"])}: {pctu(f["pm"]) if f["pm"] >= 0 else pct(f["pm"])}' if f.get('pm') is not None else '')
    if f.get('beta') is not None:
        b = f['beta']
        tile(k['beta'], _num(b, 2), esc(k['b_lo'] if b < 0.8 else k['b_hi'] if b > 1.2 else k['b_mid']))
    if f.get('emp'): tile(k['emp'], _num(f['emp'], 0))
    if f.get('sec'): tile(k['sec'], esc(f['sec']))
    rng = ''
    if f.get('h52') and f.get('l52') and f['h52'] > f['l52'] and f.get('cur'):
        x = min(100, max(0, (f['cur'] - f['l52']) / (f['h52'] - f['l52']) * 100))
        rng = (f'<div class="k52"><span>{esc(k["r52"])}</span><div class="k52b"><i style="left:{x:.1f}%"></i></div>'
               f'<div class="k52l"><span>{esc(k["lo"])} {usd_h(f["l52"])}</span><span>{esc(k["hi"])} {usd_h(f["h52"])}</span></div></div>')
    an = ''
    if f.get('rec') and f.get('tgt') and f.get('cur'):
        up = f['tgt'] / f['cur'] - 1
        an = (f'<div class="kan"><span>{esc(k["an"])}{f" · {f[chr(110)]}" if f.get("n") else ""}</span><b>{esc(f["rec"])}</b>'
              f'<small>{esc(k["tgt"])}: {usd_h(f["tgt"])} <span class="{cls(up)}">({pct(up)})</span></small></div>')
    ed = _when(f.get('ern'), lang)
    ern = f'<div class="kan"><span>{esc(k["ern"])}</span><b>{ed.isoformat()}</b></div>' if ed else ''
    summ = stock_summary(lang, f)
    return (f'<section class="section kstats"><h2>{esc(k["h"])} · {esc(f["tk"])}</h2><div class="kgrid"><div class="card kcard"><div class="ktiles">{"".join(tiles)}</div>{rng}</div>'
            f'<div class="card kside">{an}{ern}<h3>{esc(k["sum_h"])}</h3><p>{esc(" ".join(summ))}</p><p class="muted ksrc">{esc(k["src"].format(d=f["d"]))} {esc(k["notadv"])}</p></div></div></section>')



def analysis_block(lang, aid):
    """Full written analysis of the asset (content/profiles/<lang>/<id>.md with `kind: analysis`), shown in full on the page."""
    prof = PROFILES.get(lang, {}).get(aid)
    if not prof or prof.get('kind') != 'analysis':
        return ''
    return (f'<section class="section card anl"><h2>{esc(prof.get("title", ""))}</h2>'
            f'<p class="muted anld">{esc(prof.get("date", ""))}</p><div class="artbody">{md(prof["body"], lang)}</div></section>')

def stock_faq(lang, aid):
    f = stock_facts(lang, aid)
    if not f:
        return []
    k, n = KS[lang], f['name']
    s = stock_summary(lang, f)
    out = []
    if s:
        out.append((k['q_what'].format(name=n), ' '.join(s[:3])))
    out.append((k['q_div'].format(name=n), k['s_div'].format(dy=pctu(f['dy'])) if f.get('dy') else k['s_nodiv']))
    if f.get('pe') and 0 < f['pe'] < 500:
        out.append((k['q_pe'].format(name=n), k['s_pe'].format(pe=_num(f['pe'], 1))))
    ed = _when(f.get('ern'), lang)
    if ed:
        out.append((k['q_ern'].format(name=n), ed.isoformat()))
    if f.get('rec') and f.get('n') and f.get('tgt') and f.get('cur'):
        out.append((k['q_an'].format(name=n), k['s_an'].format(n=f['n'], rec=f['rec'], tgt=usd(f['tgt']), up=pct(f['tgt'] / f['cur'] - 1)) + ' ' + k['notadv']))
    return out



LC_TABS = [('mcap', ''), ('rev', 'revenue'), ('ni', 'earnings'), ('emp', 'employees'), ('div', 'dividend'), ('pe', 'pe-ratio')]
_LCU = {}


def lc_universe():
    """Stocks with key stats: dict id -> numbers in USD (market cap, revenue, earnings, employees, dividend yield, P/E)."""
    if _LCU:
        return _LCU
    for aid, a in A.items():
        if a['cat'] != 'stock':
            continue
        st = stock_stats(a)
        mc = STOCKINFO.get(a.get('yahoo') or '', {}).get('mcap') if st else None
        if not mc:
            continue
        c, fc = st.get('ccy'), st.get('fcy') or st.get('ccy')
        lcf = to_usd(1.0, c)
        cur = METRICS[aid]['price']
        dy = (st['dps'] * lcf / cur) if st.get('dps') and lcf and cur else None
        _LCU[aid] = dict(mcap=mc, rev=to_usd(st.get('rev'), fc), ni=to_usd(st.get('ni'), fc), emp=st.get('emp'),
                         div=dy if dy and dy < 0.25 else None, pe=st.get('pe') if st.get('pe') and 0 < st['pe'] < 300 else None,
                         mkt=a.get('mkt') or 'us', web=(st.get('web') or '').lower().replace('https://', '').replace('http://', '').replace('www.', '').strip('/'))
    seen = {}   # one row per company: share classes / ADR + home listing share a website -> keep the better-known listing
    for aid in sorted(_LCU, key=lambda i: ORD.get(i, 1e9)):
        w = _LCU[aid]['web']
        if w and w in seen:
            del _LCU[aid]
        elif w:
            seen[w] = aid
    return _LCU


def world_rank(aid):
    u = lc_universe()
    if aid not in u:
        return None
    if '_rank' not in _LCU.get('__meta__', {}):
        order = sorted((i for i in u if i != '__meta__'), key=lambda i: -u[i]['mcap'])
        _LCU['__meta__'] = {'_rank': {i: k + 1 for k, i in enumerate(order)}}
    return _LCU['__meta__']['_rank'].get(aid)


def year_chg(aid):
    p = A[aid]['p']
    return p[-1] / p[-13] - 1 if len(p) >= 13 and p[-13] else None


def lc_slug(m):
    return MKTS[m][0].replace('stocks-', '') if m in MKTS else m


def lc_ids(tab, mkt=None):
    u = {i: v for i, v in lc_universe().items() if i != '__meta__' and (mkt is None or v['mkt'] == mkt)}
    if tab == 'pe':
        ids = sorted((i for i in u if u[i]['pe']), key=lambda i: u[i]['pe'])
    else:
        ids = sorted((i for i in u if u[i].get(tab)), key=lambda i: -u[i][tab])
    return ids


def lc_page(lang, tab='mcap', mkt=None, ver=None):
    t = LC[lang]
    u = lc_universe()
    ids = lc_ids(tab, mkt)
    if mkt is None:
        ids = ids[:100]
    # rank change vs yesterday (market cap tab only): yesterday's cap = today's / (1 + day change)
    moves = {}
    if tab == 'mcap':
        y = sorted(ids, key=lambda i: -u[i]['mcap'] / (1 + (METRICS[i]['chg'] or 0)))
        ry = {i: k for k, i in enumerate(y)}
        moves = {i: ry[i] - k for k, i in enumerate(ids)}
    cname = (lambda m: CTRY[lang][3][m][0] if m in CTRY[lang][3] else m.upper())
    val = {'mcap': lambda v: usd_h(v['mcap']), 'rev': lambda v: usd_h(v['rev']), 'ni': lambda v: usd_h(v['ni']),
           'emp': lambda v: _num(v['emp'], 0), 'div': lambda v: pctu(v['div']), 'pe': lambda v: _num(v['pe'], 1)}[tab]
    rows = ''
    for k, i in enumerate(ids):
        a, m, v = A[i], METRICS[i], u[i]
        mv = moves.get(i, 0)
        arr = f'<span class="rk {"up" if mv > 0 else "dn"}">{"▲" if mv > 0 else "▼"}{abs(mv)}</span>' if mv else ''
        yc = year_chg(i)
        extra = f'<td class="num hide-sm">{usd_h(v["mcap"])}</td>' if tab != 'mcap' else ''
        rows += (f'<tr><td class="l n">{arr}{k + 1}</td><td class="l"><a class="asset" href="{aurl(lang, i)}">{icon(a)}<span><span class="nm">{esc(nm(a, lang))}</span>'
                 f'<span class="tk">{esc(a["tk"])}</span></span></a></td><td class="num"><b>{val(v)}</b></td>{extra}'
                 f'<td class="num" data-p="{i}">{price(m["price"])}</td><td class="num {cls(m["chg"])}" data-c="{i}">{pct(m["chg"])}</td>'
                 f'<td class="num hide-sm {cls(yc)}">{pct(yc)}</td><td class="hide-sm">{spark(m["spark"])}</td>'
                 f'<td class="l hide-sm">{flag(v["mkt"])}{esc(cname(v["mkt"]))}</td></tr>')
    lab = t['t_' + tab]
    th = (f'<tr><th class="l n">{esc(t["rank"])}</th><th class="l">{esc(t["name"])}</th><th>{esc(lab)}</th>'
          + (f'<th class="hide-sm">{esc(t["t_mcap"])}</th>' if tab != 'mcap' else '')
          + f'<th>{esc(t["price"])}</th><th>{esc(t["day"])}</th><th class="hide-sm">{esc(t["year"])}</th><th class="hide-sm"></th><th class="l hide-sm">{esc(t["ctry"])}</th></tr>')
    base = 'largest-companies'
    if mkt is None:
        h1 = t['h_' + tab]
        path = base + ('/' + dict(LC_TABS)[tab] if tab != 'mcap' else '')
    else:
        h1 = t['h_ctry'].format(c=cname(mkt))
        path = base + '/' + lc_slug(mkt)
    tabs = ''.join(f'<a class="chip{" on" if k == tab and mkt is None else ""}" href="{url(lang, base + ("/" + s if s else ""))}">{esc(t["t_" + k])}</a>' for k, s in LC_TABS)
    mk = sorted({v['mkt'] for i, v in u.items() if i != '__meta__'}, key=lambda m: (MKT_LANG.get(m) != lang, -len(lc_ids('mcap', m))))
    ctry = ''.join(f'<a class="chip{" on" if m == mkt else ""}" href="{url(lang, base + "/" + lc_slug(m))}">{flag(m)}{esc(cname(m))}</a>' for m in mk if len(lc_ids('mcap', m)) >= 5)
    top = ids[:3]
    desc = (t['lead'] + ' ' + ', '.join(f'{nm(A[i], lang)}' for i in top)).strip()[:300]
    body = (f'<h1>{esc(h1)}</h1><p class="lead">{esc(t["lead"])}</p>'
            f'<div class="cchips lcchips"><b>{esc(t["by"])}:</b>{tabs}</div><div class="cchips lcchips"><b>{esc(t["ctry_h"])}:</b>{ctry}</div>'
            f'<section class="section"><div class="tw"><table class="mt lct"><thead>{th}</thead><tbody>{rows}</tbody></table></div></section>'
            f'<p class="note">{esc(t["note"])} {UPDATED[:10]}</p>')
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": h1,
          "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": nm(A[i], 'en'), "url": SITE + aurl(lang, i)} for k, i in enumerate(ids[:20])]}
    return path, shell(lang, path, f'{h1} ({UPDATED[:4]}) | {BRAND}', desc, body, {}, ver, [ld])


def lc_pages(lang, ver):
    out = [lc_page(lang, k, None, ver) for k, _ in LC_TABS]
    u = lc_universe()
    for m in sorted({v['mkt'] for i, v in u.items() if i != '__meta__'}):
        if len(lc_ids('mcap', m)) >= 5:
            out.append(lc_page(lang, 'mcap', m, ver))
    return out


XCH = _jload('exchanges.json') or {}
XC_PARTNER = {'binance': 'binance', 'bybit': 'bybit', 'gate': 'gate', 'bingx': 'bingx', 'mexc': 'mexc', 'kraken': 'kraken', 'hyperliquid': 'hyperliquid'}


def xc_partner(name):
    k = (name or '').lower().split()[0].replace('.io', '') if name else ''
    return XC_PARTNER.get(k)


def xc_has(lang, xid=None):
    if not XCH.get('spot'):
        return False
    return xid is None or (lang in FULL and xid in XCH.get('detail', {}))


def xc_url(lang, xid):
    return url(lang if lang in FULL else 'en', 'crypto-exchanges/' + xid)


def _xlogo(e):
    return (f'<span class="ic"><img src="{esc(e["img"])}" alt="" loading="lazy" width="26" height="26" referrerpolicy="no-referrer"></span>' if e.get('img')
            else f'<span class="ic">{esc((e.get("name") or "?")[0])}</span>')


def _xvsvg(pts, w=640, h=170):
    if len(pts) < 2:
        return ''
    mx = max(v for _, v in pts) or 1
    xy = [(i / (len(pts) - 1) * w, h - 4 - v / mx * (h - 12)) for i, (_, v) in enumerate(pts)]
    line = ' '.join(f'{x:.1f},{y:.1f}' for x, y in xy)
    return (f'<svg class="spk up xchart" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">'
            f'<polygon points="0,{h} {line} {w},{h}"/><polyline points="{line}"/></svg>')


def xc_spot_page(lang, ver):
    t, btc = XC[lang], METRICS['btc']['price'] if 'btc' in METRICS else 0
    sp = [e for e in XCH['spot'] if e.get('vol_btc')]
    tot = sum(e.get('nvol_btc') or 0 for e in sp) or 1
    rows = ''
    for k, e in enumerate(sp[:100]):
        det = e['id'] in XCH.get('detail', {})
        nm_ = f'<a class="asset" href="{xc_url(lang, e["id"])}">' if det else '<span class="asset">'
        ch = XCH.get('detail', {}).get(e['id'], {}).get('chart') or []
        go = xc_partner(e.get('name'))
        golink = f'<a class="buy" href="/go/{go}?from=xc-list&l={lang}" target="_blank" rel="sponsored noopener" title="{esc(t["aff"])}">↗</a>' if go else ''
        rows += (f'<tr><td class="l n">{k + 1}</td><td class="l">{nm_}{_xlogo(e)}<span><span class="nm">{esc(e["name"])}</span>'
                 f'<span class="tk">{esc(e.get("country") or "")}</span></span>{"</a>" if det else "</span>"}</td>'
                 f'<td class="num"><b>{usd_h((e.get("nvol_btc") or 0) * btc)}</b></td><td class="num hide-sm">{usd_h(e["vol_btc"] * btc)}</td>'
                 f'<td class="num">{pctu((e.get("nvol_btc") or 0) / tot)}</td><td class="num hide-sm">{e.get("trust") or "—"}/10</td>'
                 f'<td class="hide-sm">{spark([v for _, v in ch][-14:]) if ch else ""}</td>'
                 f'<td>{golink}</td></tr>')
    th = (f'<tr><th class="l n">#</th><th class="l">{esc(t["name"])}</th><th>{esc(t["nvol"])}</th><th class="hide-sm">{esc(t["vol"])}</th>'
          f'<th>{esc(t["share"])}</th><th class="hide-sm">{esc(t["trust"])}</th><th class="hide-sm"></th><th></th></tr>')
    return _xc_shell(lang, ver, 'spot', t['h_spot'], t['lead_spot'], th, rows)


def xc_der_page(lang, ver):
    t, btc = XC[lang], METRICS['btc']['price'] if 'btc' in METRICS else 0
    rows = ''
    for k, e in enumerate([e for e in XCH.get('derivatives', []) if e.get('oi_btc')][:60]):
        go = xc_partner(e.get('name'))
        rows += (f'<tr><td class="l n">{k + 1}</td><td class="l"><span class="asset">{_xlogo(e)}<span><span class="nm">{esc(e["name"])}</span>'
                 f'<span class="tk">{esc(e.get("country") or "")}</span></span></span></td><td class="num"><b>{usd_h(e["oi_btc"] * btc)}</b></td>'
                 f'<td class="num">{usd_h((e.get("vol_btc") or 0) * btc)}</td><td class="num hide-sm">{e.get("perp") or 0}</td><td class="num hide-sm">{e.get("fut") or 0}</td>'
                 f'<td>{f"<a class=buy href=/go/{go}?from=xc-der&l={lang} target=_blank rel=\"sponsored noopener\">↗</a>" if go else ""}</td></tr>')
    th = (f'<tr><th class="l n">#</th><th class="l">{esc(t["name"])}</th><th>{esc(t["oi"])}</th><th>{esc(t["vol"])}</th>'
          f'<th class="hide-sm">{esc(t["perp"])}</th><th class="hide-sm">{esc(t["fut"])}</th><th></th></tr>')
    return _xc_shell(lang, ver, 'derivatives', t['h_der'], t['lead_der'], th, rows)


def _xc_shell(lang, ver, kind, h1, lead, th, rows):
    t = XC[lang]
    path = 'crypto-exchanges' + ('/derivatives' if kind == 'derivatives' else '')
    tabs = (f'<a class="chip{" on" if kind == "spot" else ""}" href="{url(lang, "crypto-exchanges")}">{esc(t["tab_spot"])}</a>'
            f'<a class="chip{" on" if kind == "derivatives" else ""}" href="{url(lang, "crypto-exchanges/derivatives")}">{esc(t["tab_der"])}</a>'
            f'<a class="chip" href="{url(lang, "exchanges")}">{esc(EX[lang]["nav"])}</a>')
    body = (f'<h1>{esc(h1)}</h1><p class="lead">{esc(lead)}</p><div class="cchips lcchips">{tabs}</div>'
            f'<section class="section"><div class="tw"><table class="mt lct">{"<thead>" + th + "</thead>"}<tbody>{rows}</tbody></table></div></section>'
            f'<p class="note">{esc(t["src"].format(d=XCH.get("updated", "")))} {esc(t["aff"])}: ↗</p>')
    return path, shell(lang, path, f'{h1} | {BRAND}', lead, body, {}, ver)


def xc_detail_page(lang, xid, ver):
    t, btc = XC[lang], METRICS['btc']['price'] if 'btc' in METRICS else 0
    sp = XCH['spot']
    e = next(x for x in sp if x['id'] == xid)
    d = XCH['detail'][xid]
    tot = sum(x.get('nvol_btc') or 0 for x in sp) or 1
    name = e['name']
    cg2aid = {a.get('cgid'): i for i, a in A.items() if a.get('cgid')}
    cpart = f' ({e["country"]}{", " + str(e["year"]) if e.get("year") else ""})' if e.get('country') else ''
    lead = t['x_lead'].format(x=name, c=cpart, v=usd((e.get('vol_btc') or 0) * btc), s=pctu((e.get('nvol_btc') or 0) / tot), r=e.get('rank') or '—')
    go = xc_partner(name)
    fee = ''
    if go:
        fz = {'binance': ('0.10% / 0.10%', 'Auto-Invest'), 'bybit': ('0.10% / 0.10%', 'Auto-Invest'), 'kraken': ('0.40% / 0.80%', 'Recurring Buy (1%)'),
              'gate': ('0.10–0.20%', 'Auto-Invest'), 'bingx': ('0.10% / 0.10%', 'Recurring Buy'), 'mexc': ('0% / 0.05%', 'Spot DCA')}.get(go)
        if fz:
            fee = f'<div class="ks"><span>{esc(t["fees"])}</span><b>{fz[0]}</b><small>{esc(t["dca"])}: {esc(fz[1])}</small></div>'
    yr = f'<small>{esc(t["year"])}: {e["year"]}</small>' if e.get('year') else ''
    tiles = (f'<div class="ks"><span>{esc(t["vol"])}</span><b>{usd_h((e.get("vol_btc") or 0) * btc)}</b></div>'
             f'<div class="ks"><span>{esc(t["nvol"])}</span><b>{usd_h((e.get("nvol_btc") or 0) * btc)}</b><small>{esc(t["share"])}: {pctu((e.get("nvol_btc") or 0) / tot)}</small></div>'
             f'<div class="ks"><span>{esc(t["trust"])}</span><b>{e.get("trust") or "—"}/10</b><small>#{e.get("rank") or "—"}</small></div>'
             + (f'<div class="ks"><span>{esc(t["country"])}</span><b>{esc(e["country"])}</b>{yr}</div>' if e.get('country') else '')
             + fee)
    pr = ''
    for p in d.get('pairs', [])[:30]:
        aid = cg2aid.get(p.get('cg'))
        lab = f'{esc(p.get("b", ""))}/{esc(p.get("q", ""))}'
        lab = f'<a href="{aurl(lang, aid)}">{icon(A[aid])}{lab}</a>' if aid else lab
        pr += (f'<tr><td class="l">{lab}</td><td class="num">{_num(p["last"], 6 if (p.get("last") or 0) < 1 else 2) if p.get("last") is not None else "—"}</td>'
               f'<td class="num"><b>{usd_h(p.get("usd"))}</b></td><td class="num hide-sm">{pctu((p.get("spread") or 0) / 100) if p.get("spread") is not None else "—"}</td></tr>')
    cta = (f'<a class="btn" href="/go/{go}?from=xc-{xid}&l={lang}" target="_blank" rel="sponsored noopener">{esc(t["go"].format(x=name))}</a> <small class="muted">{esc(t["aff"])}</small>' if go
           else (f'<a class="btn ghost" href="{esc(e["url"])}" target="_blank" rel="nofollow noopener">{esc(t["site"])} ↗</a>' if e.get('url') else ''))
    h1 = t['x_h1'].format(x=name)
    body = (f'<nav class="crumbs"><a href="{url(lang, "crypto-exchanges")}">{esc(t["nav"])}</a> / {esc(name)}</nav>'
            f'<div class="ahead">{_xlogo(e)}<div><h1>{esc(h1)}</h1></div></div><p class="lead">{esc(lead)}</p><p>{cta}</p>'
            f'<section class="section"><div class="ktiles">{tiles}</div></section>'
            + (f'<section class="section card"><h2>{esc(t["chart"])}</h2>{_xvsvg([(ts, v * btc) for ts, v in d["chart"]])}</section>' if d.get('chart') else '')
            + (f'<section class="section"><h2>{esc(t["pairs_h"].format(x=name))}</h2><div class="tw"><table class="mt"><thead><tr><th class="l">{esc(t["pair"])}</th>'
               f'<th>{esc(t["price"])}</th><th>{esc(t["vol"])}</th><th class="hide-sm">{esc(t["spread"])}</th></tr></thead><tbody>{pr}</tbody></table></div></section>' if pr else '')
            + f'<p class="note">{esc(t["src"].format(d=XCH.get("updated", "")))}</p>')
    path = 'crypto-exchanges/' + xid
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": name, "url": e.get('url') or '', "foundingDate": str(e.get('year') or '')}
    return path, shell(lang, path, f'{h1} | {BRAND}', lead, body, {}, ver, [ld])


def xc_pages(lang, ver):
    if not xc_has(lang):
        return []
    out = [xc_spot_page(lang, ver), xc_der_page(lang, ver)]
    if lang in FULL:
        out += [xc_detail_page(lang, x, ver) for x in XCH.get('detail', {}) if any(e['id'] == x for e in XCH['spot'])]
    return out

def stock_peers(aid, k=8):
    a = A[aid]
    st = stock_stats(a)
    if not st or a['cat'] != 'stock':
        return []
    me = STOCKINFO.get(a.get('yahoo') or '', {}).get('mcap') or 0
    def sim(key):
        return [i for i, b in A.items() if i != aid and b['cat'] == 'stock' and stock_stats(b).get(key) and stock_stats(b).get(key) == st.get(key)]
    pool = sim('ind') if st.get('ind') else []
    if len(pool) < 4 and st.get('sec'):
        pool = list(dict.fromkeys(pool + sim('sec')))
    mc = lambda i: STOCKINFO.get(A[i].get('yahoo') or '', {}).get('mcap') or 0
    pool.sort(key=lambda i: abs(math.log10((mc(i) or 1e6) / (me or 1e9))))
    return pool[:k]


def offer_card(lang, src):
    """One native partner offer (Telegram Wallet bonus); clicks counted by /go/ with the placement in `from`."""
    o = OFFER_TGW[lang]
    return (f'<a class="offer section" href="/go/tgwallet?from={src}&l={lang}" target="_blank" rel="sponsored noopener">'
            f'<span class="ofi" aria-hidden="true">🎁</span><span class="oft"><b>{esc(o["t"])}</b><span>{esc(o["d"])}</span><small>{esc(o["note"])}</small></span>'
            f'<span class="btn">{esc(o["cta"])}</span></a>')

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
    lump_cards = ''.join(f'<div class="card stat"><div class="k">{X["lump"].format(p=lab)}</div><div class="v">{usd_h(v)}</div>'
                         f'<div class="s {cls(r)}">{pct(r)}</div></div>' for lab, v, r in lumps)
    stat_cards = ''.join(
        f'<div class="card stat"><div class="k">{S["stat"].format(p=lab)}</div><div class="v">{usd_h(x["val"])}</div>'
        f'<div class="s {cls(x["roi"])}">{pct(x["roi"])} <span class="muted">· {S["invested_lc"]} {usd_h(x["inv"])}</span></div></div>' for lab, x in show)
    ptable = (f'<table class="rt"><tr><th>{S["period"]}</th><th>{u["invested"]}</th><th>{S["now"]}</th><th>{S["result"]}</th></tr>' +
              ''.join(f'<tr><td class="a">{lab}</td><td>{usd_h(x["inv"])}</td><td>{usd_h(x["val"])}</td><td class="{cls(x["roi"])}">{pct(x["roi"])}</td></tr>' for lab, x in rows) +
              '</table>')
    f = dict(name=n, tk=tk, since=since_l, inv=usd(r['inv']), val=usd(r['val']), roi=pct(r['roi']), n=len(A) - 1, upd=upd,
             bench=nm(A[b1], lang), ra=pct(ra5['roi']), rb=pct(rb5['roi']), r1=pct(m['r1']), r5=pct(m['r5']), ten=TEN)
    _apf = dict(f, price=price(m['price']), ten=_re.sub(r'<[^>]+>', '', TEN))
    title, desc = AP[lang]['title'].format(**_apf), AP[lang]['desc'].format(**_apf)
    fe = dict(f, name=esc(n), inv=usd_h(r['inv']), val=usd_h(r['val']), roi=f'<span class="{cls(r["roi"])}">{pct(r["roi"])}</span>')
    faq = [(S['q1'].format(**f), S['a1'].format(**f)), (S['q2'].format(**f), S['a2'].format(**f)),
           (S['q4'].format(**f), S['a4'].format(**f)), (S['q3'], S['a3'])]
    if m['r1'] is None or m['r5'] is None:
        faq.pop(2)
    faq = stock_faq(lang, aid) + faq
    if lumps:
        lab, v, r5_ = lumps[min(2, len(lumps) - 1)]
        faq.insert(1, (X['q5'].format(name=n, p=lab), X['a5'].format(name=n, p=lab, v=usd(v), roi=pct(r5_))))
    sim = [i for i in ORDERED if A[i]['cat'] == a['cat'] and i != aid]
    if a.get('sector'):
        same = [i for i in sim if A[i].get('sector') == a['sector']]
        sim = same + [i for i in sim if i not in same]
    sim = sim[:10]
    cat = S['cat_' + a['cat']]
    crumbs = f'<nav class="crumbs"><a href="{url(lang)}">{HM[lang]["nav"]}</a> / {esc(cat)} / {esc(n)}</nav>'
    badges = f'<span class="badge">{esc(tk)}</span> <span class="badge">{esc(cat)}</span>' + (f' <span class="badge">{esc(a["sector"])}</span>' if a.get('sector') else '')
    head = (f'{crumbs}<div class="ahead">{icon(a, True)}<div><h1>{esc(AP[lang]["h1"].format(name=n, tk=tk))}</h1><div style="margin-top:4px">{badges}</div></div>'
            f'<div class="price"><span class="v" data-p="{aid}">{price(m["price"])}</span><span class="pill {cls(m["chg"])}" data-c="{aid}">{pct(m["chg"])}</span>{local_price(a, lang)}<span id="buyslot" data-id="{aid}"></span><button class="star big" data-s="{aid}" title="{esc(ME[lang]["star"])}">☆</button>'
            f'<button class="addpf" type="button" data-add="{aid}" data-cfg="{esc(json.dumps(dict(code=hccy(lang)[0], rate=hccy(lang)[1], me=url(lang, "me"), t={k: PF[lang][k] for k in ("addpf", "added", "open", "cancel", "qty_or_sum")}, d=ME[lang]["date"]), ensure_ascii=False))}">＋ {esc(PF[lang]["addpf"])}</button></div></div>')
    if (a.get('yahoo') or '').endswith('=F') and a['tk'] not in ('XAU', 'XAG'):
        head += f'<p class="note">{esc(CMD_NOTE[lang])}</p>'
    w = S['w']
    loc = TV_LOC.get(lang, 'en')
    tvs = tv_symbol(a)
    if tvs and tvs.startswith(TV_NOCHART):   # chart not embeddable: own chart, keep fundamentals
        tv = own_chart(lang, a, aid)
        tech_news = ''
        if a['cat'] in ('stock', 'etf'):
            tech_news = (f'<section class="card section"><h2>{X["fund"]} · {esc(tk)}</h2>'
                         + tvw('financials', dict(isTransparent=True, displayMode='regular', width='100%', height='100%', colorTheme='light', symbol=tvs, locale=loc), 520)
                         + '</section>')
    elif tvs:
        tv = (f'<section class="card tvcard"><div class="charthead"><h2>{w["live_chart"]} · {esc(tk)}</h2><span class="livebadge"><i></i>{w["live"]}</span></div>'
              + tvw('advanced-chart', dict(autosize=True, symbol=tv_symbol(a), interval='D', timezone='Etc/UTC', theme='light', style='1', locale=loc,
                                           allow_symbol_change=False, hide_side_toolbar=True, withdateranges=True, save_image=False), 480) + '</section>')
        tech_news = (f'<div class="cols2 section"><section class="card"><h2>{X["tech"]} · {esc(tk)}</h2>'
                     + tvw('technical-analysis', dict(interval='1D', width='100%', height='100%', isTransparent=True, symbol=tv_symbol(a), showIntervalTabs=True,
                                                      displayMode='single', locale=loc, colorTheme='light'), 430)
                     + f'</section><section class="card"><h2>{X["news"]} · {esc(tk)}</h2>' + own_news_rows(lang, aid)
                     + tvw('timeline', dict(feedMode='symbol', symbol=tv_symbol(a), isTransparent=True, displayMode='regular', width='100%', height='100%',
                                            colorTheme='light', locale=loc), 430) + '</section></div>')
        if a['cat'] in ('stock', 'etf'):
            tech_news += (f'<section class="card section"><h2>{X["fund"]} · {esc(tk)}</h2>'
                          + tvw('financials', dict(isTransparent=True, displayMode='regular', width='100%', height='100%', colorTheme='light', symbol=tv_symbol(a), locale=loc), 520)
                          + '</section>')
    else:   # no free live chart for this symbol -> our own monthly chart
        tv, tech_news = own_chart(lang, a, aid), ''
    body = (f'{head}<p class="lead" style="margin-top:10px">{S["a_lead"].format(**fe)}</p>{hot_block(lang, aid)}<div class="chartside section">{tv}{side_block(lang, aid)}</div>{'' if 'timeline' in tech_news else hot_more(lang, aid)}{stock_block(lang, aid)}{analysis_block(lang, aid)}{offer_card(lang, 'asset-' + aid) if a['cat'] == 'crypto' else ''}<div class="stats">{stat_cards}</div><div class="stats">{lump_cards}</div>{long_block(lang, aid)}{seas_block(lang, aid)}{calc_block(lang)}{tech_news}'
            f'<div class="cols2 section"><section class="card"><h2>{S["a_periods"].format(**fe)}</h2>{ptable}</section>'
            f'<section class="card faq"><h2>{S["faq"]}</h2>' + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q, x in faq) + '</section></div>'
            + (f'<section class="section">{table_block(lang, peers, esc(KS[lang]["peers"]), interactive=False)}</section>' if (peers := stock_peers(aid)) else '') +
            f'<section class="section">{table_block(lang, sim, S["a_similar"] + ": " + esc(cat), interactive=False)}</section>'
            f'{emb_block(lang, aid)}<p class="note">{esc(S["about"].format(**f))}</p>')
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
    items = [('compare', S['nav_cmp']) if (S := TR[lang]) else None, ('habits', HB[lang]['nav']), ('millionaire', t['g_nav'])]
    if CPI['c']:
        items.append(('inflation', t['i_nav']))
    if XCH.get('spot'):
        items.append(('crypto-exchanges', XC[lang]['nav']))
    items += [('largest-companies', LC[lang]['nav']), ('world-assets', WA[lang]['nav']), ('memes', MEM[lang]['nav']), ('converter', HCONV[lang]), ('ath', t['a_nav']), ('bitcoin-halving', t['v_nav']), ('dividends', DV[lang]['nav']), ('average-price', AV[lang]['nav'])]
    if lang in OV:
        items.append(('ovdp', OV[lang]['nav']))
    items.append(('widgets', EMB[lang]['nav']))
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
            ('Kraken', 'kraken', 'Spot · Stocks · Staking · US, UK & EU', '#7132F5'),
            ('Gate', 'gate', 'Spot · Futures · Altcoins', '#2354E6'),
            ('BingX', 'bingx', 'Spot · Futures · Copy trading', '#2A5BFF'),
            ('MEXC', 'mexc', 'Spot · Futures · New listings', '#1972E2')],
    'dex': [('OKX Wallet', 'okx-wallet', 'Multichain wallet · DEX swaps', '#000000'),
            ('Hyperliquid', 'hyperliquid', 'On-chain perpetuals · Order book', '#0F3B36'),
            ('GMGN', 'gmgn', 'Memecoin trading · Wallet tracking', '#18C46B'),
            ('Telegram Wallet', 'tgwallet', 'Crypto inside Telegram · New users: up to $50 bonus in gold', '#2AABEE'),
            ('FG Wallet', 'fgwallet', 'USDT (TRC-20) wallet · No TRX needed for fees', '#1B7F5F')],
    'brk': [('Freedom24', 'freedom24', 'Stocks & ETFs · EU residents (CySEC) · Recurring investment plan', '#2E7D32')],
}
BRK_H = {'uk': 'Брокер для акцій і ETF', 'en': 'Broker for stocks and ETFs', 'es': 'Bróker para acciones y ETF', 'pt': 'Corretora para ações e ETFs',
         'de': 'Broker für Aktien und ETFs', 'fr': 'Courtier pour actions et ETF', 'it': 'Broker per azioni ed ETF', 'pl': 'Broker do akcji i ETF',
         'tr': 'Hisse ve ETF için aracı kurum', 'nl': 'Broker voor aandelen en ETF’s', 'ru': 'Брокер для акций и ETF', 'id': 'Broker untuk saham dan ETF',
         'vi': 'Môi giới cổ phiếu và ETF', 'th': 'โบรกเกอร์หุ้นและ ETF', 'hi': 'शेयर और ETF के लिए ब्रोकर', 'ja': '株式・ETFの証券会社',
         'ko': '주식·ETF 증권사', 'zh': '股票和 ETF 券商', 'ar': 'وسيط للأسهم وصناديق ETF', 'fil': 'Broker para sa stocks at ETF'}
POLY = '/go/polymarket'
XDOM = {'binance': 'binance.com', 'bybit': 'bybit.com', 'gate': 'gate.com', 'bingx': 'bingx.com', 'mexc': 'mexc.com', 'okx-wallet': 'okx.com',
        'hyperliquid': 'hyperliquid.xyz', 'gmgn': 'gmgn.ai', 'freedom24': 'freedom24.com', 'kraken': 'kraken.com', 'fgwallet': 'fgwallet.io', 'tgwallet': 'wallet.tg'}


def xlogo(u, n, c, cls_='xl'):
    d = XDOM.get(u)
    img = (f'<img src="https://www.google.com/s2/favicons?domain={d}&sz=64" alt="" width="28" height="28" loading="lazy" '
           f'onerror="this.remove()">' if d else '')
    return f'<span class="{cls_} xlogo" style="background:{c}">{n[0]}{img}</span>'


def poly_block(lang, q='crypto'):
    e = EX[lang]
    return (f'<section class="card section pm" data-tag="{q}" hidden><div class="charthead"><h2>🔮 {e["pm_h"]}</h2>'
            f'<a class="calc" href="{POLY}?from=pm-block&l={lang}" target="_blank" rel="sponsored nofollow noopener">{e["pm_go"]} →</a></div>'
            f'<p class="muted" style="margin:0 0 10px">{e["pm_d"]}</p><div class="pml"></div><p class="muted" style="font-size:12px;margin:8px 0 0">{e["pm_note"]}</p></section>')


def exchanges_page(lang, ver):
    e = EX[lang]
    def cards(k):
        return ''.join(f'<a class="card xcard" href="/go/{u}?from=exchanges&l={lang}" target="_blank" rel="sponsored nofollow noopener">{xlogo(u, n, c)}'
                       f'<div><b>{n}</b><small>{t}</small></div><span class="btn">{e["go"]}</span></a>' for n, u, t, c in PARTNERS[k])
    x = EXT[lang]
    FEES = {'binance': ('0.10% / 0.10%', 'Auto-Invest'), 'bybit': ('0.10% / 0.10%', 'Auto-Invest'), 'kraken': ('0.40% / 0.80%', 'Recurring Buy (1%)'), 'gate': ('0.10–0.20%', 'Auto-Invest'),
            'bingx': ('0.10% / 0.10%', 'Recurring Buy'), 'mexc': ('0% / 0.05%', 'Spot DCA')}
    trows = ''.join(f'<tr><td class="l">{xlogo(u, n, c, "xl sm")}<b>{n}</b></td><td class="num">{FEES[u][0]}</td>'
                    f'<td>✓ {FEES[u][1]}</td><td class="hide-sm muted">{t}</td>'
                    f'<td><a class="btn" href="/go/{u}?from=exchanges-table&l={lang}" target="_blank" rel="sponsored nofollow noopener">{e["go"]}</a></td></tr>'
                    for n, u, t, c in PARTNERS['cex'] if u in FEES)
    table = (f'<div class="tw"><table class="mt xt"><thead><tr><th class="l"></th><th>{esc(x["fee"])}</th><th>{esc(x["dca"])}</th><th class="hide-sm">{esc(x["feat"])}</th><th></th></tr></thead>'
             f'<tbody>{trows}</tbody></table></div><p class="muted" style="font-size:13px">{esc(x["note2"])} {esc(x["src"])}.</p>')
    body = (f'<h1>{esc(e["h1"])}</h1><p class="lead">{esc(e["d"])}</p>'
            f'<section class="section card"><h2>{e["cex"]}</h2>{table}</section>'
            f'<section class="section"><h2>{esc(BRK_H[lang])}</h2><div class="xgrid">{cards("brk")}</div></section>'
            f'<section class="section"><h2>{e["dex"]}</h2><div class="xgrid">{cards("dex")}</div></section>'
            f'<p class="muted" style="font-size:13px">{e["note"]}</p>{poly_block(lang)}')
    return shell(lang, 'exchanges', f'{e["h1"]} | {BRAND}', e['d'], body, {}, ver)


NEWS_TAGS = ['movers', 'bitcoin', 'ethereum', 'etf', 'regulation', 'defi', 'stablecoins', 'solana', 'xrp', 'markets', 'hacks', 'ai']


def news_tl(lang):
    return dict(zip(NEWS_TAGS, [HOT[lang][0]] + NW[lang]['tags'].split('|') + [AIS[lang]['nav']]))


def hot_items(lang, aid):
    return [(k, m) for k, m in news_items(lang) if aid in m.get('assets', [])][:20]


def hot_block(lang, aid):
    items = hot_items(lang, aid)[:1]
    if not items:
        return ''
    tl = news_tl(lang)
    return (f'<section class="section hot"><h2>{esc(HOT[lang][1].format(name=nm(A[aid], lang)))}</h2><div class="card nlist own">'
            + ''.join(news_row(lang, k, m, tl) for k, m in items) + '</div></section>')


def hot_more(lang, aid):
    items = hot_items(lang, aid)[1:]
    if not items:
        return ''
    tl = news_tl(lang)
    return (f'<section class="section hotmore"><h2>{esc(NW[lang]["own"])} · {esc(A[aid]["tk"])}</h2><div class="card nlist own nscroll">'
            + ''.join(news_row(lang, k, m, tl) for k, m in items) + '</div></section>')


def own_news_rows(lang, aid):
    """Our own briefs about the asset, shown on top of the external headlines (one news block instead of two)."""
    items = hot_items(lang, aid)[1:4]
    if not items:
        return ''
    tl = news_tl(lang)
    return '<div class="nlist own nmerge">' + ''.join(news_row(lang, k, m, tl) for k, m in items) + '</div>'


def news_items(lang):
    return sorted(NEWS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)


def news_row(lang, slug, m, tl):
    tags = ''.join(f' <i class="badge">{esc(tl.get(t, t))}</i>' for t in (x.strip() for x in m.get('tags', '').split(',')) if t)
    g = ' '.join(x.strip() for x in m.get('tags', '').split(',') if x.strip())
    return (f'<a class="nrow" data-g="{esc(g)}" href="{url(lang, "news/" + slug)}"><b>{esc(m.get("title", ""))}</b>'
            f'<span class="muted">WhatIfStack · <time data-t="{esc(m.get("date", ""))}">{esc(m.get("date", "")[:16])}</time>{tags}</span></a>')


def news_page(lang, ver):
    n = NW[lang]
    tl = news_tl(lang)
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
    tl = news_tl(lang)
    title, desc = m.get('title', ''), m.get('description', '')
    tags = ''.join(f'<span class="badge">{esc(tl.get(t, t))}</span> ' for t in (x.strip() for x in m.get('tags', '').split(',')) if t)
    cards = ''.join(sc_block('card', [i], lang) for i in m['assets'][:3])
    rel = [(k, x) for k, x in news_items(lang) if k != slug][:6]
    rel_html = ''.join(news_row(lang, k, x, tl) for k, x in rel)
    w = S['w']
    about = url(lang if lang in ABOUT else 'en', 'about')
    cv = cover('news', lang, slug)
    body = (f'<nav class="crumbs"><a href="{url(lang, "news")}">{n["n_nav"]}</a></nav><article class="art"><h1>{esc(title)}</h1>'
            f'<div class="muted byline"><a href="{about}">WhatIfStack Research</a> · <time data-t="{esc(m.get("date", ""))}">{esc(m.get("date", ""))}</time> · {tags}</div>'
            + (f'<img class="cover" src="{cv}" alt="" width="1200" height="630">' if cv else '') +
            f'<p class="lead">{esc(desc)}</p><div class="postcards">{cards}</div><div class="artbody">{md(m["body"], lang)}</div>{follow_block(lang)}</article>'
            f'{poll_block(lang)}<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div><a class="btn" id="ctaBuy2" href="{url(lang, "exchanges")}">{EX[lang]["nav"]} →</a></section>'
            + (f'<section class="section"><h2>{esc(n["own"])}</h2><div class="card nlist own">{rel_html}</div></section>' if rel else ''))
    d = m.get('date', '').replace(' ', 'T')
    jsonld = [{"@context": "https://schema.org", "@type": "NewsArticle", "headline": title, "description": desc, "inLanguage": S['loc'],
               "datePublished": d, "dateModified": d, "mainEntityOfPage": SITE + url(lang, 'news/' + slug), "image": [SITE + (cv or '/assets/og.jpg')],
               "author": {"@type": "Organization", "name": "WhatIfStack Research", "url": SITE + about},
               "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + '/assets/icon-512.png'}}}]
    return shell(lang, 'news/' + slug, f'{title} | {BRAND}', desc, body, {'_og': cv} if cv else {}, ver, jsonld)


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
    body = f'<article class="art"><h1>{esc(h1)}</h1><div class="artbody">' + ''.join(f'<h2>{esc(h)}</h2><p>{esc(t)}</p>' for h, t in secs) + f'<p><a href="{pol_url(lang)}">{esc(ACT[lang]["pol"])} →</a></p></div></article>'
    org = {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + '/', "logo": SITE + '/assets/icon-512.png', "sameAs": [u for _, u in SOCIAL]}
    return shell(lang, 'about', f'{h1} | {BRAND}', secs[0][1], body, {}, ver, [org])


AI_STOCKS = [i for i in ('nvda', 'msft', 'goog', 'meta', 'amzn', 'avgo', 'tsm', 'amd', 'orcl', 'pltr', 'mu', 'anet', 'smci', 'dell', 'crwv', 'smh', 'soxx') if i in A]
AI_CRYPTO = [i for i in ('tao', 'near', 'render', 'fet', 'wld', 'icp', 'virtual', 'grt', 'ar', 'arkm', 'theta', 'io', 'kaito') if i in A]
AI_BASKET_S = [i for i in ('nvda', 'msft', 'goog', 'meta', 'avgo', 'tsm', 'amd') if i in A]
AI_BASKET_C = [i for i in ('near', 'fet', 'render', 'icp', 'grt', 'ar') if i in A]


def basket(ids, years, daily=AMOUNT):
    st = END_I - years * 12
    ok = [i for i in ids if ym2i(A[i]['start']) <= st]
    if not ok:
        return None
    rs = [simulate(i, st, daily / len(ok)) for i in ok]
    inv, val = sum(r['inv'] for r in rs), sum(r['val'] for r in rs)
    return dict(inv=inv, val=val, roi=val / inv - 1, ids=ok)


def ai_page(lang, ver):
    S, t = TR[lang], AIS[lang]
    yl = {1: S['p1'], 3: S['p3'], 5: S['p5']}
    cards, sents = '', []
    for key, ids, y in (('basket_s', AI_BASKET_S, 5), ('basket_c', AI_BASKET_C, 3)):
        b = basket(ids, y)
        if not b:
            continue
        spy = simulate('spy', END_I - y * 12)
        names = ', '.join(A[i]['tk'] for i in b['ids'])
        sent = t['res'].format(names=names, y=yl[y], inv=usd(b['inv']), val=usd(b['val']), roi=pct(b['roi']), spy=f'{usd(spy["val"])} ({pct(spy["roi"])})')
        sents.append(sent)
        cards += (f'<div class="card bk"><div class="k">{esc(t[key])} · {esc(yl[y])}</div><div class="v {cls(b["roi"])}">{pct(b["roi"])}</div>'
                  f'<div class="s">{esc(sent)}</div></div>')
    for aid in ('nvda', 'tao'):
        if aid in A:
            cards += hl_card(lang, aid, nm(A[aid], lang), 'r5' if METRICS[aid]['r5'] is not None else 'r1', S['sub5'] if METRICS[aid]['r5'] is not None else S['sub1'])
    tl = dict(zip(NEWS_TAGS, NW[lang]['tags'].split('|') + [t['nav']]))
    news = [(k, m) for k, m in news_items(lang) if 'ai' in [x.strip() for x in m.get('tags', '').split(',')]][:8]
    news_html = (f'<section class="section"><h2>{esc(t["news"])}</h2><div class="card nlist own">' + ''.join(news_row(lang, k, m, tl) for k, m in news) + '</div></section>') if news else ''
    bl = lang if lang in BLOG_LANGS else 'en'
    posts = sorted([(k, m) for k, m in POSTS.get(bl, {}).items() if m.get('category') == 'ai'], key=lambda kv: kv[1].get('date', ''), reverse=True)[:8]
    posts_html = (f'<section class="section"><h2>{esc(t["posts"])}</h2><div class="posts">' + ''.join(
        f'<a class="card post" href="{url(bl, "blog/" + k)}"><div class="muted">{esc(m.get("date", ""))}</div><h3>{esc(post_meta_title(m, bl))}</h3></a>' for k, m in posts) + '</div></section>') if posts else ''
    body = (f'<h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["d"])}</p><div class="hl">{cards}</div>'
            f'<section class="section">{table_block(lang, AI_STOCKS, t["stocks"], interactive=False)}</section>'
            f'<section class="section">{table_block(lang, AI_CRYPTO, t["crypto"], interactive=False)}</section>{news_html}{posts_html}{poll_block(lang)}{poly_block(lang)}')
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": t['h1'], "acceptedAnswer": {"@type": "Answer", "text": ' '.join(sents)}}]}
    return shell(lang, 'ai', f'{t["h1"]} | {BRAND}', t['d'], body, {}, ver, [faq])


def me_page(lang, ver):
    S, t = TR[lang], ME[lang]
    code, rate = hccy(lang)
    per = HB[lang]['per'].split('|')
    hold = (f'<section class="section"><h2 class="sr">{esc(t["hold"])}</h2><div class="hl" id="htot"></div><div class="abar" id="abar"></div><div id="hold"><p class="muted">{esc(t["hempty"])}</p></div>'
            f'<div class="card hcalc" id="holdform"><div class="hrow">'
            f'<label class="f">{S["w"]["q_asset"]}<div class="inp"><input id="ha" list="palist" autocomplete="off" placeholder="Bitcoin"></div></label>'
            f'<label class="f">&nbsp;<div class="inp"><select id="hmode"><option value="sum">{esc(t["by_sum"])}</option><option value="qty">{esc(t["by_qty"])}</option></select></div></label>'
            f'<label class="f">{esc(t["amount"])}<div class="inp"><input id="hamt" type="number" min="0" step="any" value="{nice(100 * rate):.0f}"><span class="muted" id="hunit">{CCY_SYM.get(code, code)}</span></div></label>'
            f'<label class="f">{esc(t["date"])}<div class="inp"><input id="hdate" type="month" value="{END}"></div></label></div>'
            f'<button class="btn" id="hsave">{esc(t["add"])}</button></div></section>')
    pf = PF[lang]
    body = (f'<h1>{esc(pf["h1"])}</h1><p class="lead">{esc(pf["d"])}</p>{hold}'
            f'<section class="section"><h2>☆ {esc(t["watch"])}</h2><div id="watch"><p class="muted">{esc(t["empty"])}</p></div></section>'
            f'<section class="section"><h2>📈 {esc(t["plans"])}</h2><div class="hl" id="metot"></div><div id="plans"></div>'
            f'<div class="card hcalc" id="planform"><div class="hrow">'
            f'<label class="f">{S["w"]["q_asset"]}<div class="inp"><input id="pa" list="palist" autocomplete="off" placeholder="Bitcoin"><datalist id="palist"></datalist></div></label>'
            f'<label class="f">{esc(t["amount"])}<div class="inp"><input id="pm" type="number" min="0" step="any" value="{nice(10 * rate):.0f}"><span class="muted">{CCY_SYM.get(code, code)}</span></div></label>'
            f'<label class="f">&nbsp;<div class="inp"><select id="pf"><option value="d">{esc(per[0])}</option><option value="w">{esc(per[1])}</option><option value="m" selected>{esc(per[2])}</option></select></div></label>'
            f'<label class="f">{esc(t["start"])}<div class="inp"><input id="ps" type="month" value="{END_I // 12 - 2}-01"></div></label></div>'
            f'<button class="btn" id="psave">{esc(t["save"])}</button></div></section>'
            f'<p class="muted" style="font-size:13px">{esc(t["note"])}</p>'
            f'<div class="pfbk"><button class="btn ghost" id="pfexp" type="button">⬇ {esc(pf["backup"])}</button>'
            f'<label class="btn ghost">⬆ {esc(pf["restore"])}<input type="file" id="pfimp" accept="application/json" hidden></label></div>')
    cfg = dict(me=dict(code=code, rate=rate, t=dict(t, **pf), per=dict(zip('dwm', per))))
    return shell(lang, 'me', f'{pf["h1"]} | {BRAND}', pf['d'], body, cfg, ver).replace('<link rel="canonical"', '<meta name="robots" content="noindex, follow"><link rel="canonical"', 1)   # personal page: keep out of search


MEME_IDS = [i for i in ('doge', 'shib', 'pepe', 'bonk', 'wif', 'floki', 'trump', 'pengu', 'neiro', 'bome', 'pnut') if i in A]


def memes_page(lang, ver):
    S, t, u = TR[lang], MEM[lang], TR[lang]['ui']
    chains = [('solana', 'Solana'), ('base', 'Base'), ('bsc', 'BNB Chain'), ('eth', 'Ethereum')]
    seg = ''.join(f'<button data-n="{k}"{" class=on" if k == "solana" else ""}>{v}</button>' for k, v in chains)
    head = (f'<tr><th class="l">{u["name"]}</th><th>{u["price"]}</th><th>1h</th><th>{u["chg"]}</th><th class="hide-sm">{esc(t["vol"])}</th>'
            f'<th class="hide-sm">{esc(t["liq"])}</th><th class="hide-sm">{esc(t["age"])}</th><th></th></tr>')
    body = (f'<h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["d"])}</p>'
            f'<div class="warnbox">⚠️ {esc(t["warn"])}</div>'
            f'<section class="section"><div class="charthead"><h2>🔥 {esc(t["live"])}</h2><span class="livebadge"><i></i>{S["w"]["live"]}</span></div>'
            f'<div class="seg" id="dexn">{seg}</div><div class="tw" style="margin-top:10px"><table class="mt" id="dext"><thead>{head}</thead><tbody id="dexb"><tr><td colspan="8" class="empty">…</td></tr></tbody></table></div>'
            f'<p class="muted" style="font-size:12px">{esc(t["src"])}</p></section>'
            f'<section class="section">{table_block(lang, MEME_IDS, "🐸 " + t["est"], interactive=False)}</section>'
            f'<section class="section"><div class="hgrid"><a class="card hcard" href="/go/gmgn?from=memes-card&l={lang}" target="_blank" rel="sponsored nofollow noopener"><span>🦎</span><b>GMGN</b><small>Memecoin trading · Wallet tracking</small></a>'
            f'<a class="card hcard" href="{url(lang, "exchanges")}"><span>₿</span><b>{esc(EX[lang]["h1"])}</b></a><a class="card hcard" href="{url(lang, "ath")}"><span>📉</span><b>{esc(TT[lang]["a_h1"])}</b></a></div></section>')
    cfg = dict(memes=dict(t=dict(trade=t['trade'], new=t['new'], lowliq=t['lowliq'], hot=t['hot'])))
    return shell(lang, 'memes', f'{t["h1"]} | {BRAND}', t['d'], body, cfg, ver)


SEC_ICON = {'guide': '<path d="M5 4h9a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h9M9 8h5"/>', 'memes': '<path d="M4 15c0-4.4 3.6-8 8-8s8 3.6 8 8v1a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3z"/><circle cx="9" cy="12" r="1.2"/><circle cx="15" cy="12" r="1.2"/>', 'ai': '<rect x="5" y="7" width="14" height="11" rx="3"/><path d="M12 3v4M9 12h.01M15 12h.01M9.5 15.5h5"/>', 'me': '<path d="m12 4 2.4 5 5.4.6-4 3.7 1.1 5.3L12 16l-4.9 2.6 1.1-5.3-4-3.7 5.4-.6z"/>', 'news': '<rect x="4" y="5" width="16" height="14" rx="2"/><path d="M8 9h8M8 12h8M8 15h5"/>', 'exchanges': '<path d="M7 7h11l-3-3M17 17H6l3 3"/>', 'habits': '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5zM16 10h1.5a2.5 2.5 0 0 1 0 5H16M8 3v3M11 3v3"/>'}


def sections_strip(lang):
    S = TR[lang]
    gm = guide_meta(lang)
    items = [('guide', '📘', gm.get('nav', 'Guide'), gm.get('short', '')), ('memes', '🐸', MEM[lang]['nav'], MEM[lang]['live']), ('ai', '🤖', AIS[lang]['nav'], AIS[lang]['stocks'] + ' · ' + AIS[lang]['crypto']),
             ('me', '☆', ME[lang]['nav'], ME[lang]['hold'] + ' · ' + ME[lang]['plans']), ('news', '📰', NW[lang]['n_nav'], NW[lang]['own']),
             ('exchanges', '₿', EX[lang]['nav'], EX[lang]['cex']), ('habits', '☕', HB[lang]['nav'], HB[lang]['h1'])]
    cards = ''.join(f'<a class="card sec" href="{url(lang if k != "guide" or lang in GUIDE else "en", k)}"><span class="si"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{SEC_ICON[k]}</svg></span><div><b>{esc(t)}</b><small>{esc(d)}</small></div></a>' for k, ic, t, d in items)
    return f'<section class="section"><div class="secgrid">{cards}</div></section>'


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
    body = (f'<nav class="crumbs"><a href="{url(lang)}">{HM[lang]["nav"]}</a> / {esc(label)}</nav><h1>{esc(X["hub_h1"].format(cat=label))}</h1>'
            f'<p class="lead">{esc(desc)}</p>{country_chips(lang) if cat == "stock" else ""}<div class="hl">{cards}</div><div class="tabs" id="tabs"></div>{filt}{table_block(lang, ids[:150])}')
    return shell(lang, slug, title, desc, body, dict(tab=cat), ver)


# ---------- world's largest assets ----------
OZ_PER_T = 32150.7466
WORLD_SRC = [  # (key, value or formula input, source label, url)
    ('re', 393.3e12, 'Savills, global real estate value at the start of 2025', 'https://www.savills.co.uk/insight-and-opinion/savills-news/381209/world-s-real-estate-worth-$393.3-trillion-and-is-the-world-s-largest-store-of-wealth'),
    ('gold', 224200, 'World Gold Council, above-ground stock end-Q3 2026: 224,200 t', 'https://www.gold.org/goldhub/data/above-ground-stocks'),
    ('silver', 19.3e9, 'Silver Institute, total above-ground silver end-2023: 19.3 bn oz', 'https://silverinstitute.org/new-report-analyzes-the-complexity-of-above-ground-silver-stocks/'),
    ('oil', 1732.4e9, 'Energy Institute Statistical Review, proved oil reserves (end-2020): 1,732 bn barrels', 'https://www.energyinst.org/statistical-review'),
    ('gas', 188.1e12, 'Energy Institute Statistical Review, proved gas reserves (end-2020): 188 tcm', 'https://www.energyinst.org/statistical-review'),
    ('usd', 23.4139e12, 'Federal Reserve H.6, US M2 September 2026: $23.41 tn', 'https://fred.stlouisfed.org/series/M2SL'),
    ('cny', 359.63e12, 'People\'s Bank of China, M2 end-September 2026: 359.63 tn yuan', 'https://www.pbc.gov.cn/en/'),
]


def world_items(lang):
    names = WN[lang].split('|')
    src = {k: v for k, v, _, _ in WORLD_SRC}
    cm = G.get('cmdty') or {}
    out = [(WA[lang]['types'].split('|')[0], src['re'], 0, None, '🏠')]
    if 'gold' in A: out.append((names[4], src['gold'] * OZ_PER_T * METRICS['gold']['price'], 1, 'gold', None))
    if 'silver' in A: out.append((names[5], src['silver'] * METRICS['silver']['price'], 1, 'silver', None))
    if cm.get('brent'): out.append((names[0], src['oil'] * cm['brent'], 1, None, '🛢️'))
    if cm.get('ng'): out.append((names[1], src['gas'] * 35.3147 * 0.001037 * cm['ng'], 1, None, '🔥'))
    out.append((names[2], src['usd'], 2, None, '💵'))
    cny = (FX.get('rates') or {}).get('CNY')
    if cny: out.append((names[3], src['cny'] / cny, 2, None, '💴'))
    seen = set()
    for aid in ORDERED:
        a = A[aid]
        if a['cat'] == 'stock':
            mc = (STOCKINFO.get(a.get('yahoo') or '', {}) or {}).get('mcap')
            first = nm(a, 'en').split(' ')[0].lower()
            if mc and mc > 2e11 and first not in seen:          # one row per company (GOOG/GOOGL, BRK-A/B...)
                seen.add(first); out.append((nm(a, lang).split(' (Class')[0], mc, 3, aid, None))
        elif a['cat'] == 'crypto' and (a.get('mcap') or 0) > 5e10:
            out.append((nm(a, lang), a['mcap'], 4, aid, None))
    return sorted(out, key=lambda x: -x[1])


def world_page(lang, ver):
    S, w = TR[lang], WA[lang]
    types = w['types'].split('|')
    items = world_items(lang)
    rows = ''
    for k, (n, v, t, aid, emo) in enumerate(items[:100]):
        ic = icon(A[aid]) if aid else f'<span class="wic">{emo}</span>'
        name = f'<a class="asset" href="{aurl(lang, aid)}">{ic}<span class="nm">{esc(n)}</span></a>' if aid else f'<span class="asset">{ic}<span class="nm">{esc(n)}</span></span>'
        rows += f'<tr><td class="n">{k + 1}</td><td class="l">{name}</td><td class="num"><b>{fbig(v)}</b></td><td class="hide-sm"><span class="badge t{t}">{esc(types[t])}</span></td></tr>'
    src = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="nofollow noopener">{esc(l)}</a></li>' for _, _, l, u in WORLD_SRC)
    body = (f'<h1>{esc(w["h1"])}</h1><p class="lead">{esc(w["lead"])}</p>'
            f'<section class="section"><div class="tw"><table class="mt wtab"><thead><tr><th class="l n">#</th><th class="l">{esc(w["asset"])}</th><th>{esc(w["value"])}</th><th class="hide-sm">{esc(w["type"])}</th></tr></thead><tbody>{rows}</tbody></table></div></section>'
            f'<section class="card section faq"><p>{esc(w["note"])}</p><ul class="wsrc">{src}</ul><p class="muted" style="font-size:13px">{UPDATED}</p></section>')
    jsonld = [{"@context": "https://schema.org", "@type": "ItemList", "name": w['h1'], "numberOfItems": min(100, len(items)),
               "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": it[0]} for k, it in enumerate(items[:50])]}]
    return shell(lang, 'world-assets', f'{w["h1"]} | {BRAND}', w['lead'], body, {}, ver, jsonld)


MKT_N = {}


def flag(m):
    return f'<img class="flag" src="/assets/flags/{m}.svg" alt="" width="18" height="18" loading="lazy">'


def country_chips(lang, cur=None, limit=None):
    if not MKT_N:
        for a in A.values():
            if a.get('mkt'):
                MKT_N[a['mkt']] = MKT_N.get(a['mkt'], 0) + 1
    mk = sorted(MKTS.items(), key=lambda kv: (MKT_LANG.get(kv[0]) != lang, kv[0] != 'ua', -MKT_N.get(kv[0], 0)))   # own country first
    ch = [(sl, f'{flag(m)}{esc(CTRY[lang][3][m][0])}') for m, (sl, fl) in mk if has_page(lang, sl)]
    if limit and len(ch) > limit:
        ch = ch[:limit] + [('stocks', '…')]
    if not ch:
        return ''
    return (f'<div class="cchips"><b>{esc(CTRY[lang][0])}:</b>' + ''.join(
        f'<a class="chip{" on" if sl == cur else ""}" href="{url(lang, sl)}">{t}</a>' for sl, t in ch) + '</div>')


def country_page(lang, slug, ver):
    S = TR[lang]
    mkt = CSLUG[slug]
    name, h1 = CTRY[lang][3][mkt]
    ids = [i for i in ORDERED if A[i].get('mkt') == mkt]
    key = 'r5' if sum(METRICS[i]['r5'] is not None for i in ids) >= 4 else 'r1'
    best = best_by(key, ids)[:4]
    cards = ''.join(hl_card(lang, i, nm(A[i], lang), key, S['sub5' if key == 'r5' else 'sub1']) for i in best)
    lead = CTRY[lang][1].format(n=len(ids))
    desc = f'{h1}. {lead}'
    body = (f'<nav class="crumbs"><a href="{url(lang)}">{HM[lang]["nav"]}</a> / <a href="{url(lang, "stocks")}">{esc(S["ui"]["stock"])}</a> / {esc(name)}</nav>'
            f'<h1>{esc(h1)}</h1><p class="lead">{esc(lead)}</p>{country_chips(lang, slug)}'
            + (f'<div class="hl">{cards}</div>' if cards else '')
            + f'<section class="section">{table_block(lang, ids[:200], None, interactive=False)}</section>'
            f'<p class="note">{esc(TR[lang]["x"]["hub_d"].format(n=len(ids), cat=S["ui"]["stock"].lower()))}</p>')
    jsonld = [{"@context": "https://schema.org", "@type": "ItemList", "name": h1, "numberOfItems": len(ids),
               "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": nm(A[i], lang), "url": SITE + aurl(lang, i)} for k, i in enumerate(ids[:50])]}]
    return shell(lang, slug, f'{h1} | {BRAND}', desc[:300], body, {}, ver, jsonld)


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
import re as _re  # noqa: E402


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
PROFILES = load_posts('profiles')   # own asset profiles: content/profiles/<lang>/<asset id>.md
DESC = {f[:-5]: json.load(open(os.path.join(ROOT, 'data', 'desc', f), encoding='utf-8'))   # short localized descriptions: data/desc/<lang>.json {id: text}
        for f in (os.listdir(os.path.join(ROOT, 'data', 'desc')) if os.path.isdir(os.path.join(ROOT, 'data', 'desc')) else []) if f.endswith('.json')}
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
        if m['r5'] is not None:
            pl, rv = S['p5'], m['r5']
        elif m['r1'] is not None:
            pl, rv = S['p1'], m['r1']
        else:
            pl, rv = S['p_since'].format(since=mlabel(a['start'], lang)), simulate(aid, ym2i(a['start']))['roi']
        return (f'<a class="card postcard" href="{aurl(lang, aid)}">{icon(a, True)}<div><b>{esc(nm(a, lang))}</b> <span class="badge">{esc(a["tk"])}</span>'
                f'<div class="muted">{S["stat"].format(p=pl)}: <b class="{cls(rv)}">{pct(rv)}</b> · {S["ui"]["price"]} <b data-p="{aid}">{price(m["price"])}</b></div></div>'
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
            rows += (f'<tr><td class="a"><a href="{aurl(lang, i)}">{esc(nm(A[i], lang))}</a></td><td>{usd_h(r["inv"])}</td><td>{usd_h(r["val"])}</td>'
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


def load_guides(sub='guide'):
    out, root = {}, os.path.join(ROOT, 'content', sub)
    for fn in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        if fn.endswith('.md'):
            raw = open(os.path.join(root, fn), encoding='utf-8').read()
            head, body = raw[3:].split('\n---', 1)
            meta = {k.strip(): v.strip() for k, _, v in (l.partition(':') for l in head.strip().splitlines())}
            meta['body'] = body.strip()
            out[fn[:-3]] = meta
    return out


GUIDE = load_guides()
POLICY = load_guides('policy')   # editorial policy: content/policy/<lang>.md


def pol_url(lang):
    return url(lang if lang in POLICY else 'en', 'editorial-policy')


def policy_page(lang, ver):
    g = POLICY[lang]
    body = f'<article class="art guide"><h1>{esc(g["title"])}</h1><p class="lead">{esc(g["description"])}</p><div class="artbody">{md(g["body"], lang)}</div></article>'
    org = {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + '/', "publishingPrinciples": SITE + url(lang, 'editorial-policy'),
           "logo": SITE + '/assets/icon-512.png', "sameAs": [u for _, u in SOCIAL]}
    return shell(lang, 'editorial-policy', f'{g["title"]} | {BRAND}', g['description'], body, {}, ver, [org])


RISK = ('low', 'medium', 'high')
STAT = ('live', 'expected', 'ended')


def act_facts(lang, m, src='activity'):
    a = ACT[lang]
    lv, st = dict(zip(RISK, a['lv'].split('|'))), dict(zip(STAT, a['st'].split('|')))
    r, sv = m.get('risk', 'medium'), m.get('status', 'live')
    rows = [(a['risk'], f'<span class="risk r-{r}">{esc(lv.get(r, r))}</span>'), (a['status'], f'<span class="ast s-{sv}">{esc(st.get(sv, sv))}</span>')]
    rows += [(a[k], esc(m[k])) for k in ('cost', 'time') if m.get(k)]
    go = ''
    if m.get('go'):
        go = (f'<a class="btn" href="/go/{esc(m["go"])}?from={src}&l={lang}" target="_blank" rel="sponsored nofollow noopener">{esc(m.get("go_label") or a["go"])} →</a>'
              f'<small class="muted">{esc(a["ad"])} <a href="{pol_url(lang)}">{esc(a["pol"])}</a></small>')
    return '<div class="card afacts">' + ''.join(f'<div><small>{k}</small><b>{v}</b></div>' for k, v in rows) + (f'<div class="ago">{go}</div>' if go else '') + '</div>'


def act_items(lang):
    for lg in (lang, 'en'):
        it = sorted([(k, m) for k, m in POSTS.get(lg, {}).items() if m.get('category') == 'activities'], key=lambda kv: kv[1].get('date', ''), reverse=True)
        it.sort(key=lambda kv: STAT.index(kv[1]['status']) if kv[1].get('status') in STAT else 0)   # live first, ended last
        if it:
            return lg, it
    return lang, []


# ---------------- best DCA portfolios ----------------
BP_SET = [('btc', {'btc': 1}), ('crypto', {'btc': .5, 'eth': .3, 'sol': .1, 'bnb': .1}), ('spy', {'spy': 1}), ('s6040', {'spy': .6, 'bnd': .4}),
          ('world', {'vt': 1}), ('tech', {'qqq': 1}), ('mag7', {k: 1 / 7 for k in ('aapl', 'msft', 'nvda', 'googl', 'amzn', 'meta', 'tsla')}),
          ('div', {'schd': 1}), ('mix', {'spy': .6, 'gold': .3, 'btc': .1}), ('metals', {'gold': .7, 'silver': .3})]


def bp_sets():
    out = [(k, {a: w for a, w in c.items() if a in A}) for k, c in BP_SET]
    for key, cat, extra in (('topc', 'crypto', lambda a: (a.get('rank') or 999) <= 100), ('tops', 'stock', lambda a: (STOCKINFO.get(a.get('yahoo') or '', {}) or {}).get('mcap', 0) >= 2e10)):
        best = sorted([i for i, a in A.items() if a['cat'] == cat and extra(a) and METRICS[i]['r5'] is not None], key=lambda i: -METRICS[i]['r5'])[:5]
        out.append((key, {i: .2 for i in best}))
    return [(k, c) for k, c in out if c and abs(sum(c.values()) - 1) < 1e-6]


def bp_sim(comp, years):
    st = END_I - years * 12
    if any(ym2i(A[a]['start']) > st for a in comp):
        return None
    inv = val = 0.0
    best = None
    for a, w in comp.items():
        r = simulate(a, st, AMOUNT * w)
        inv += r['inv']; val += r['val']
        if best is None or r['roi'] > best[1]:
            best = (a, r['roi'])
    return dict(inv=inv, val=val, roi=val / inv - 1, best=best)


def portfolios_page(lang, ver):
    t = BP[lang]
    sets = bp_sets()
    res = {k: {y: bp_sim(c, y) for y in (1, 3, 5, 10)} for k, c in sets}
    order = sorted(sets, key=lambda kc: -(res[kc[0]][5]['roi'] if res[kc[0]][5] else -9))
    rank = ''.join(f'<tr><td class="l"><b>{i + 1}. {esc(t[k])}</b>{" <small class=\"muted\">*</small>" if k in ("topc", "tops") else ""}</td>'
                   f'<td class="num">{usd(res[k][5]["inv"])}</td><td class="num"><b>{usd(res[k][5]["val"])}</b></td><td class="num"><span class="pill {cls(res[k][5]["roi"])}">{pct(res[k][5]["roi"])}</span></td></tr>'
                   for i, (k, c) in enumerate([kc for kc in order if res[kc[0]][5]]))
    cards = []
    for k, c in order:
        chips = ''.join(f'<a class="bpa" href="{url(lang, a)}">{icon(A[a])}<span>{esc(A[a]["tk"])} {w * 100:.0f}%</span></a>' for a, w in sorted(c.items(), key=lambda x: -x[1]))
        rows = ''.join(f'<tr><td class="l">{t["yrs"].format(n=y)}</td><td class="num">{usd_h(r["inv"])}</td><td class="num"><b>{usd_h(r["val"])}</b></td>'
                       f'<td class="num"><span class="pill {cls(r["roi"])}">{pct(r["roi"])}</span></td>'
                       f'<td class="num hide-sm">{esc(A[r["best"][0]]["tk"])} {pct(r["best"][1])}</td></tr>' for y in (1, 3, 5, 10) if (r := res[k][y]))
        cards.append(f'<section class="card bpc"><h2><a href="{url(lang, "portfolios/" + k)}">{esc(t[k])}</a></h2><div class="bpcomp">{chips}</div>'
                     f'<div class="tw"><table class="mt"><thead><tr><th class="l"></th><th>{esc(t["inv"])}</th><th>{esc(t["val"])}</th><th>{esc(t["roi"])}</th><th class="hide-sm">{esc(t["best_asset"])}</th></tr></thead><tbody>{rows}</tbody></table></div>'
                     + (f'<p class="muted bpnote">* {esc(t["hind"])}</p>' if k in ('topc', 'tops') else '')
                     + f'<a class="btn ghost bpmore" href="{url(lang, "portfolios/" + k)}">{esc(BPD[lang]["more"])}</a></section>')
    body = (f'<h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["d"])}</p>'
            f'<p class="muted bpnote">{esc(t["how"])}</p><div class="bpgrid section">{"".join(cards)}</div><p class="muted" style="font-size:13px">{esc(t["na"])}</p>')
    return shell(lang, 'portfolios', f'{t["h1"]} | {BRAND}', t['d'], body, {}, ver)


def bp_path(comp, st):
    """Monthly invested / value of a DCA portfolio from month index st to the end; per-asset final results."""
    months = list(range(st, END_I + 1))
    inv = [0.0] * len(months); val = [0.0] * len(months); per = {}
    for a, w in comp.items():
        P = A[a]; s0 = ym2i(P['start']); amt = AMOUNT * w; u = ii = 0.0
        anniv = (END_I - st) % 12 == 0
        for j, i in enumerate(months):
            c = amt * (per_month(i) - (END_DAY if anniv and j == 0 else 0))
            u += c / P['p'][i - s0]; ii += c
            val[j] += u * P['p'][i - s0]
        per[a] = dict(inv=ii, val=u * P['p'][END_I - s0])
    # cumulative invested (all assets)
    tot = 0.0
    for j, i in enumerate(months):
        tot += AMOUNT * (per_month(i) - (END_DAY if (END_I - st) % 12 == 0 and j == 0 else 0))
        inv[j] = tot
    return months, inv, val, per


def portfolio_detail(lang, k, comp, ver):
    t, d, S = BP[lang], BPD[lang], TR[lang]
    res = {y: bp_sim(comp, y) for y in (1, 3, 5, 10)}
    yrs = 5 if res[5] else (3 if res[3] else 1)
    st = END_I - yrs * 12
    months, inv, val, per = bp_path(comp, st)
    r = res[yrs]
    name = t[k]
    lead = d['dlead'].format(n=yrs, yr=TT[lang]['yr'], inv=f'<b>{usd_h(r["inv"])}</b>', val=f'<b>{usd_h(r["val"])}</b>', roi=f'<span class="{cls(r["roi"])}">{pct(r["roi"])}</span>')
    profit = sum(max(0, x['val'] - x['inv']) for x in per.values()) or 1
    rows = ''
    for a, w in sorted(comp.items(), key=lambda x: -(per[x[0]]['val'] - per[x[0]]['inv'])):
        x = per[a]; roi = x['val'] / x['inv'] - 1 if x['inv'] else 0
        sh = max(0, x['val'] - x['inv']) / profit
        rows += (f'<tr><td class="l"><a class="asset" href="{aurl(lang, a)}">{icon(A[a])}<span><span class="nm">{esc(nm(A[a], lang))}</span><span class="tk">{esc(A[a]["tk"])}</span></span></a></td>'
                 f'<td class="num">{w * 100:.0f}%</td><td class="num hide-sm">{usd_h(x["inv"])}</td><td class="num"><b>{usd_h(x["val"])}</b></td>'
                 f'<td class="num"><span class="pill {cls(roi)}">{pct(roi)}</span></td><td class="num hide-sm">{sh * 100:.0f}%</td></tr>')
    comp_tbl = (f'<div class="tw"><table class="mt"><thead><tr><th class="l"></th><th>{esc(d["weight"])}</th><th class="hide-sm">{esc(t["inv"])}</th><th>{esc(t["val"])}</th>'
                f'<th>{esc(t["roi"])}</th><th class="hide-sm">{esc(d["share"])}</th></tr></thead><tbody>{rows}</tbody></table></div>')
    res_rows = ''.join(f'<tr><td class="l">{t["yrs"].format(n=y)}</td><td class="num">{usd_h(x["inv"])}</td><td class="num"><b>{usd_h(x["val"])}</b></td>'
                       f'<td class="num"><span class="pill {cls(x["roi"])}">{pct(x["roi"])}</span></td></tr>' for y in (1, 3, 5, 10) if (x := res[y]))
    res_tbl = f'<div class="tw"><table class="mt"><thead><tr><th class="l"></th><th>{esc(t["inv"])}</th><th>{esc(t["val"])}</th><th>{esc(t["roi"])}</th></tr></thead><tbody>{res_rows}</tbody></table></div>'
    # chart
    W, H, L, R, T_, B = 720, 260, 8, 78, 12, 26
    mx = max(max(val), max(inv)) * 1.05 or 1
    X = lambda j: L + (W - L - R) * j / max(1, len(months) - 1)
    Y = lambda v: T_ + (H - T_ - B) * (1 - v / mx)
    line = lambda arr: ' '.join(f'{X(j):.1f},{Y(v):.1f}' for j, v in enumerate(arr))
    grid = ''.join(f'<line x1="{L}" x2="{W - R}" y1="{Y(mx * g / 4):.1f}" y2="{Y(mx * g / 4):.1f}" class="g"/><text x="{W - R + 6}" y="{Y(mx * g / 4) + 4:.1f}">{esc(usd(mx * g / 4))}</text>' for g in range(5))
    grid += ''.join(f'<text x="{X(j):.1f}" y="{H - 6}" text-anchor="middle">{i // 12}</text>' for j, i in enumerate(months) if i % 12 == 0)
    up = val[-1] >= inv[-1]
    col = '#16a34a' if up else '#dc2626'
    chart = (f'<svg viewBox="0 0 {W} {H}" class="bpchart" role="img" aria-label="{esc(d["chart"])}">{grid}'
             f'<polygon points="{X(0):.1f},{H - B} {line(val)} {X(len(val) - 1):.1f},{H - B}" fill="{col}" opacity=".1"/>'
             f'<polyline points="{line(val)}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linejoin="round"/>'
             f'<polyline points="{line(inv)}" fill="none" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="6 5"/></svg>'
             f'<div class="glg"><span><i style="background:{col}"></i>{esc(t["val"])}</span><span><i class="cl"></i>{esc(t["inv"])}</span></div>')
    # why: contributors + deepest drop of the portfolio's return (value / invested)
    ratio = [v / i if i else 1 for v, i in zip(val, inv)]
    peak, dd, ddm = ratio[0], 0.0, months[0]
    for j, x in enumerate(ratio):
        peak = max(peak, x)
        if x / peak - 1 < dd:
            dd, ddm = x / peak - 1, months[j]
    srt = sorted(per.items(), key=lambda kv: -(kv[1]['val'] - kv[1]['inv']))
    why = []
    if len(comp) > 1:
        a0, x0 = srt[0]; aL, xL = srt[-1]
        why.append(d['contrib'].format(a=nm(A[a0], lang), p=f'{max(0, x0["val"] - x0["inv"]) / profit * 100:.0f}%', r=pct(x0['val'] / x0['inv'] - 1)))
        why.append(d['weak'].format(a=nm(A[aL], lang), r=pct(xL['val'] / xL['inv'] - 1)))
    if dd < -0.05:
        why.append(d['dd'].format(d=pct(dd), m=mlabel(i2ym(ddm), lang)))
    idea = BP_IDEA.get(lang, {}).get(k)
    li = lambda xs: '<ul>' + ''.join(f'<li>{esc(x)}</li>' for x in xs) + '</ul>'
    chips = ''.join(f'<a class="bpa" href="{aurl(lang, a)}">{icon(A[a])}<span>{esc(A[a]["tk"])} {w * 100:.0f}%</span></a>' for a, w in sorted(comp.items(), key=lambda x: -x[1]))
    others = ''.join(f'<a class="bpa" href="{url(lang, "portfolios/" + kk)}"><span>{esc(t[kk])}</span></a>' for kk, _ in bp_sets() if kk != k)
    h1 = d['dh1'].format(name=name)
    body = (f'<p class="crumbs"><a href="{url(lang, "portfolios")}">{esc(d["back"])}</a></p><h1>{esc(h1)}</h1><p class="lead">{lead}</p><div class="bpcomp">{chips}</div>'
            + (f'<div class="card awarn">⚠️ {esc(d["hind"])}</div>' if k in ('topc', 'tops') else '')
            + (f'<section class="card section"><h2>💡 {esc(d["idea"])}</h2><p>{esc(idea)}</p></section>' if idea else '')
            + f'<section class="card section"><h2>{esc(d["chart"])}</h2>{chart}</section>'
            f'<div class="cols2 section"><section class="card"><h2>{esc(d["comp"])}</h2>{comp_tbl}</section><section class="card"><h2>{esc(d["res"])}</h2>{res_tbl}</section></div>'
            + (f'<section class="card section"><h2>🔍 {esc(d["why"])}</h2>{li(why)}</section>' if why else '')
            + f'<div class="cols2 section"><section class="card"><h2>✅ {esc(d["good"])}</h2>{li([d["g1"], d["g2"], d["g3"]])}</section>'
            f'<section class="card"><h2>⚠️ {esc(d["risks"])}</h2>{li([d["r1"], d["r2"], d["r3"]])}</section></div>'
            f'<p><a class="btn" href="{url(lang, "compare")}?sel={",".join(comp)}">⇅ {esc(d["try"])}</a></p>'
            f'<p class="muted bpnote">{esc(t["how"])}</p><section class="section"><h2>{esc(t["h1"].split(":")[0])}</h2><div class="bpcomp">{others}</div></section>')
    desc = _re.sub(r'<[^>]+>', '', lead)
    return shell(lang, 'portfolios/' + k, f'{h1} | {BRAND}', desc, body, {}, ver)


def activities_page(lang, ver):
    a = ACT[lang]
    lg, items = act_items(lang)
    lv, st = dict(zip(RISK, a['lv'].split('|'))), dict(zip(STAT, a['st'].split('|')))
    cards = ''.join(
        f'<a class="card post act" href="{url(lg, "blog/" + k)}">'
        + (f'<img class="thumb" src="{cover("blog", lg, k)}" alt="" width="600" height="315" loading="lazy">' if cover('blog', lg, k) else '')
        + f'<div class="muted"><span class="ast s-{m.get("status", "live")}">{esc(st.get(m.get("status", "live"), ""))}</span> <span class="risk r-{m.get("risk", "medium")}">{esc(a["risk"])}: {esc(lv.get(m.get("risk", "medium"), ""))}</span></div>'
        f'<h2>{esc(post_meta_title(m, lg))}</h2><p>{esc(post_meta_title(dict(title=m.get("description", "")), lg))}</p>'
        + (f'<div class="muted">{esc(a["cost"])}: {esc(m["cost"])}' + (f' · {esc(a["time"])}: {esc(m["time"])}' if m.get('time') else '') + '</div>' if m.get('cost') else '') + '</a>'
        for k, m in items)
    note = f'<p class="muted">{esc(a["en_note"])}</p>' if lg != lang else ''
    pmna = (f'<div class="card awarn" id="pmna" hidden>🌍 {esc(a["pmna"])}</div>'
            '<script>if(/[?&]pm=unavailable/.test(location.search))document.getElementById("pmna").hidden=false</script>')
    body = (f'<h1>{esc(a["h1"])}</h1><p class="lead">{esc(a["d"])}</p>{pmna}<div class="card awarn">⚠️ {esc(a["warn"])}</div>{note}'
            f'<div class="posts">{cards}</div><p class="muted" style="font-size:13px">{esc(a["ad"])} <a href="{pol_url(lang)}">{esc(a["pol"])}</a></p>')
    return shell(lang, 'activities', f'{a["h1"]} | {BRAND}', a['d'], body, {}, ver)


def guide_meta(lang):
    return GUIDE.get(lang) or GUIDE.get('en') or {}


def guide_page(lang, ver):
    g = GUIDE[lang]
    html = md(g['body'].replace('{n}', f'{len(A):,}'.replace(',', ' ' if lang != 'en' else ',')), lang)
    toc = []
    def anchor(m):
        t = _re.sub(r'<[^>]+>', '', m.group(1))
        sid = _re.sub(r'[^\w]+', '-', t.lower(), flags=_re.U).strip('-')[:50] or f's{len(toc)}'
        toc.append((sid, t))
        return f'<h2 id="{sid}">{m.group(1)}</h2>'
    html = _re.sub(r'<h2>(.*?)</h2>', anchor, html)
    nav = '<nav class="card gtoc">' + ''.join(f'<a href="#{i}">{esc(t)}</a>' for i, t in toc) + '</nav>'
    body = f'<article class="art guide"><h1>{esc(g["title"])}</h1><p class="lead">{esc(g["description"])}</p>{nav}<div class="artbody">{html}</div></article>'
    return shell(lang, 'guide', f'{g["title"]} | {BRAND}', g['description'], body, {}, ver)


def md(text, lang):
    out, para, lst, ltag, quote = [], [], [], None, []
    def flush():
        nonlocal para, lst, ltag
        if para:
            out.append('<p>' + inline_md(' '.join(para), lang) + '</p>'); para = []
        if lst:
            out.append(f'<{ltag}>' + ''.join(f'<li>{inline_md(x, lang)}</li>' for x in lst) + f'</{ltag}>'); lst = []
    for line in text.splitlines():
        s = line.strip()
        bm = _re.fullmatch(r'\{\{(card|table):([^}]*)\}\}', s)
        if quote and not s.startswith('>'):
            out.append(f'<blockquote>{md(chr(10).join(quote), lang)}</blockquote>' if len(quote) > 1 else f'<blockquote>{inline_md(quote[0], lang)}</blockquote>'); quote.clear()
        if not s:
            flush(); continue
        if bm:
            flush(); out.append(sc_block(bm.group(1), bm.group(2).split(':'), lang)); continue
        h = _re.match(r'(#{2,3})\s+(.*)', s)
        if h:
            flush(); lv = len(h.group(1)); out.append(f'<h{lv}>{inline_md(h.group(2), lang)}</h{lv}>'); continue
        if s.startswith('>'):
            flush(); quote.append(s[1:].strip()); continue
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
    if quote:
        out.append(f'<blockquote>{md(chr(10).join(quote), lang)}</blockquote>' if len(quote) > 1 else f'<blockquote>{inline_md(quote[0], lang)}</blockquote>'); quote.clear()
    return '\n'.join(out)


def post_meta_title(meta, lang):
    return _re.sub(r'\{\{(\w+)(?::([^}]*))?\}\}', lambda m: sc_value(m.group(1), (m.group(2) or '').split(':') if m.group(2) else [], lang), meta['title'])


def blog_index(lang, ver):
    X = TR[lang]['x']
    items = sorted(POSTS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)
    cl = NW[lang]['cats'].split('|')
    cmap = dict(zip(('analytics', 'guides', 'reports'), cl[1:]), ai=AIS[lang]['nav'], activities=ACT[lang]['nav'])
    cats = [c for c in ('analytics', 'ai', 'activities', 'guides', 'reports') if any(m.get('category', 'analytics') == c for _, m in items)]
    tabs = (f'<div class="seg nchips" id="bcats"><button class="on" data-c="">{esc(cl[0])}</button>' + ''.join(f'<button data-c="{c}">{esc(cmap[c])}</button>' for c in cats) + '</div>') if len(cats) > 1 else ''
    cards = ''.join(
        f'<a class="card post" data-c="{m.get("category", "analytics")}" href="{url(lang, "blog/" + slug)}">'
        + (f'<img class="thumb" src="{cover("blog", lang, slug)}" alt="" width="600" height="315" loading="lazy">' if cover('blog', lang, slug) else '') + f'<div class="muted"><span class="badge">{esc(cmap.get(m.get("category", "analytics"), ""))}</span> {esc(m.get("date", ""))}</div><h2>{esc(post_meta_title(m, lang))}</h2>'
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
    cv = cover('blog', lang, slug)
    crumb = (url(lang, 'activities'), ACT[lang]['nav']) if m.get('category') == 'activities' else (url(lang, 'blog'), NW[lang]['i_nav'])
    body = (f'<nav class="crumbs"><a href="{crumb[0]}">{crumb[1]}</a></nav><article class="art"><h1>{esc(title)}</h1>'
            + (f'<img class="cover" src="{cv}" alt="" width="1200" height="630">' if cv else '') +
            f'<div class="muted byline"><a href="{url(lang if lang in ABOUT else "en", "about")}">WhatIfStack Research</a> · {esc(m.get("date", ""))} · {S["updated"]} {UPDATED} · <a href="{pol_url(lang)}">{esc(ACT[lang]["pol"])}</a></div>'
            + (act_facts(lang, m) + f'<div class="card awarn">⚠️ {esc(ACT[lang]["warn"])}</div>' if m.get('category') == 'activities' else '') + f'<div class="artbody">{html_body}</div>{follow_block(lang)}</article>'
            f'<div class="postcards">{cards}</div>{poll_block(lang)}'
            f'<section class="banner section"><div><b>{w["cta"]}</b><p>{w["cta_text"]}</p></div><a class="btn" id="ctaBuy2" href="{url(lang, "exchanges")}">{w["cta"]} →</a></section>'
            + (f'<section class="section"><h2>{X["related"]}</h2><div class="posts">{rel_html}</div></section>' if rel else ''))
    jsonld = [{"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": S['loc'],
               "datePublished": m.get('date'), "dateModified": UPDATED, "mainEntityOfPage": SITE + url(lang, 'blog/' + slug),
               "author": {"@type": "Organization", "name": "WhatIfStack Research", "url": SITE + url(lang if lang in ABOUT else 'en', 'about')},
               "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + '/assets/icon-512.png'}}}]
    if cv:
        jsonld[0]['image'] = [SITE + cv]
    return shell(lang, 'blog/' + slug, title, desc, body, dict({'_og': cv} if cv else {}, _sec='activities' if m.get('category') == 'activities' else None), ver, jsonld)


def rfc822(d):
    """'2026-11-16' -> 'Mon, 16 Nov 2026 08:00:00 +0000' (RSS readers, Pinterest, Flipboard and Google News need RFC-822 dates)."""
    import email.utils, datetime as _dt
    try:
        y, m, dd = map(int, d[:10].split('-'))
        return email.utils.format_datetime(_dt.datetime(y, m, dd, 8, 0, tzinfo=_dt.timezone.utc))
    except Exception:
        return ''


def rss(lang):
    """Blog feed per language: valid RSS 2.0 with cover image per item (Pinterest auto-pins, Flipboard, Feedly, Substack/Medium imports)."""
    X = TR[lang]['x']
    items = sorted(POSTS.get(lang, {}).items(), key=lambda kv: kv[1].get('date', ''), reverse=True)[:50]
    self_u = SITE + url(lang, 'blog') + 'rss.xml'
    it = ''
    for s, m in items:
        link = SITE + url(lang, 'blog/' + s)
        cv = cover('blog', lang, s)
        img = (f'<enclosure url="{SITE + cv}" length="0" type="image/jpeg"/><media:content url="{SITE + cv}" medium="image" type="image/jpeg" width="1200" height="630"/>') if cv else ''
        it += (f'<item><title>{esc(post_meta_title(m, lang))}</title><link>{link}</link><guid isPermaLink="true">{link}</guid>'
               f'<pubDate>{rfc822(m.get("date", ""))}</pubDate>'
               + ''.join(f'<category>{esc(c)}</category>' for c in [m.get('category', '')] if c)
               + f'<description>{esc(post_meta_title(dict(title=m.get("description", "")), lang))}</description>{img}</item>')
    last = rfc822(items[0][1].get('date', '')) if items else ''
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/"><channel><title>{esc(X["blog_h1"])} | {BRAND}</title>'
            f'<link>{SITE + url(lang, "blog")}</link><atom:link href="{self_u}" rel="self" type="application/rss+xml"/><description>{esc(X["blog_d"])}</description>'
            f'<language>{TR[lang]["loc"]}</language><lastBuildDate>{last}</lastBuildDate><image><url>{SITE}/assets/og.jpg</url><title>{esc(X["blog_h1"])} | {BRAND}</title><link>{SITE + url(lang, "blog")}</link></image>{it}</channel></rss>')


def news_sitemap():
    """Google News sitemap: timely posts (not evergreen guides) and news briefs from the last 2 days, all languages (Google News only reads 48 h)."""
    import datetime as _dt
    cut = (_dt.date.fromisoformat(UPDATED[:10]) - _dt.timedelta(days=2)).isoformat()
    rows = []
    for kind, src in (('blog', POSTS), ('news', NEWS)):
        for lang, posts in src.items():
            if lang not in TR:
                continue
            for s, m in posts.items():
                d = m.get('date', '')[:10]
                if d >= cut and m.get('category') not in ('guides', 'activities') and has_page(lang, kind + '/' + s):
                    rows.append(f'<url><loc>{SITE + url(lang, kind + "/" + s)}</loc><news:news><news:publication><news:name>{BRAND}</news:name>'
                                f'<news:language>{TR[lang]["loc"].split("-")[0]}</news:language></news:publication><news:publication_date>{d}</news:publication_date>'
                                f'<news:title>{esc(post_meta_title(m, lang))}</news:title></news:news></url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n'
            + '\n'.join(rows) + '\n</urlset>')


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
                 r1=m['r1'], r3=m['r3'], r5=m['r5'], sp=[float(f'{v:.4g}') if isinstance(v, (int, float)) else v for v in (m['spark'] or [])] or None, s=a['start'])
        if nm(a, 'en') != e['n']:
            e['ne'] = nm(a, 'en')
        if a.get('logo'):
            e['l'] = 1 if a['logo'] == f'/assets/logo/{aid}.webp' else a['logo']   # 1 = standard path (expanded in app.js)
        if a.get('cat') in ('metal', 'cmd') and a.get('yahoo') in METAL_IC:
            e['mi'] = list(METAL_IC[a['yahoo']])
        if aid in ALIAS:
            e['al'] = ALIAS[aid]
        if aid in HOME_POS:
            e['h'] = HOME_POS[aid]   # missing = 9999 (app.js)
        if a.get('yahoo') in ('HG=F', 'ALI=F'):
            e['u'] = 1   # copper/aluminum are quoted per lb / tonne, not per oz
        if a.get('binance') or (a['cat'] == 'crypto' and a.get('src') == 'yahoo'):
            e['bn'] = 1
        idx.append({k: (round(v, 4) if isinstance(v, float) and k in ('ch', 'r1', 'r3', 'r5') else v) for k, v in e.items() if v is not None})
        write(f'assets/p/{aid}.json', json.dumps({'start': a['start'], 'end': a['end'], 'p': a['p'], 'n': nm(a, 'en'), 't': a['tk']}, separators=(',', ':')))
    json.dump(ORDERED[:160], open(os.path.join(ROOT, 'data/sprite_ids.json'), 'w'))   # next data run packs these logos into one sprite
    if SPRITE['ids']:
        shutil.copy(os.path.join(ROOT, 'data/logo-sprite.webp'), os.path.join(OUT, 'assets', 'logo-sprite.webp'))
    index_js = 'window.WI=' + json.dumps({'sp': SPRITE['ids'], 'spc': [SPRITE.get('cols'), SPRITE.get('rows')], 'u': UPDATED, 'v': dv, 'a': idx, 'fx': FX.get('rates', {}), 'fxu': FX.get('updated')}, ensure_ascii=False, separators=(',', ':')) + ';'
    write('assets/index.js', index_js); write('assets/style.css', css); write('assets/app.js', js); write('assets/ref.js', ref)
    if _LOGOS:
        shutil.copytree(LOGO_DIR, os.path.join(OUT, 'assets/logo'))
    shutil.copytree(os.path.join(ROOT, 'src', 'flags'), os.path.join(OUT, 'assets/flags'))
    shutil.copy(os.path.join(ROOT, 'src', 'x-relay.html'), os.path.join(DIST, 'x-relay.html'))
    if os.path.isdir(os.path.join(ROOT, 'content', 'video')):   # race videos for X / Telegram (handed over by x-relay.html)
        shutil.copytree(os.path.join(ROOT, 'content', 'video'), os.path.join(OUT, 'assets', 'video'), dirs_exist_ok=True)
    os.makedirs(os.path.join(DIST, 'embed'), exist_ok=True)
    open(os.path.join(DIST, 'embed', 'index.html'), 'w', encoding='utf-8').write(embed_page())
    shutil.copytree(os.path.join(ROOT, 'src', 'vendor'), os.path.join(OUT, 'assets', 'vendor'), dirs_exist_ok=True)   # Lightweight Charts (Apache-2.0, TradingView)
    shutil.copytree(os.path.join(ROOT, 'social', 'launch'), os.path.join(OUT, 'assets', 'press'), ignore=shutil.ignore_patterns('*.md'))   # press kit images   # hands covers to the X composer
    if os.path.isdir(os.path.join(ROOT, 'content', 'covers')):
        shutil.copytree(os.path.join(ROOT, 'content', 'covers'), os.path.join(OUT, 'assets/covers'))
    for f in ('favicon.svg', 'icon-192.png', 'icon-512.png', 'og.jpg', 'onest.woff2', 'geologica-600.woff2', 'geologica-700.woff2'):
        shutil.copy(os.path.join(ROOT, 'src', f), os.path.join(OUT, 'assets', f))
    shutil.copy(os.path.join(ROOT, 'src', 'favicon.ico'), os.path.join(OUT, 'favicon.ico'))   # Google's search favicon looks at /favicon.ico
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
        set_numfmt(lang)
        pre = '' if lang == DEFAULT else lang + '/'
        assets_ = [aid for aid in ORDERED if has_page(lang, aid)]
        extra_pages_c = []
        write(pre + 'index.html', home(lang, ver))
        write(pre + 'compare/index.html', compare(lang, ver))
        for aid in assets_:
            write(f'{pre}{aid}/index.html', asset(aid, lang, ver))
        for slug in HUBS:
            write(f'{pre}{slug}/index.html', hub(lang, slug, ver))
        for slug in CSLUG:
            if has_page(lang, slug):
                write(f'{pre}{slug}/index.html', country_page(lang, slug, ver))
                extra_pages_c.append(slug)
        for slug in TOOLS:
            write(f'{pre}{slug}/index.html', tool(lang, slug, ver))
        extra_pages = ['habits'] + ['habits/' + HSLUG[k] for k in HSCEN] + [c for c in CALCS if has_page(lang, c)] + ['portfolios/' + k for k, _ in bp_sets()]
        for k, c in bp_sets():
            write(f'{pre}portfolios/{k}/index.html', portfolio_detail(lang, k, c, ver))
        write(pre + 'millionaire/index.html', calc_page(lang, 'millionaire', ver))
        write(pre + 'compound-interest/index.html', ic_page(lang, ver))
        for _p, _h in xc_pages(lang, ver):
            write(f'{pre}{_p}/index.html', _h)
            extra_pages.append(_p)
        for _p, _h in lc_pages(lang, ver):
            write(f'{pre}{_p}/index.html', _h)
            extra_pages.append(_p)
        write(pre + 'dividends/index.html', dividends_page(lang, ver))
        write(pre + 'average-price/index.html', avgprice_page(lang, ver))
        if lang in OV:
            write(pre + 'ovdp/index.html', ovdp_page(lang, ver))
        write(pre + 'widgets/index.html', widgets_page(lang, ver))
        if CPI['c']:
            write(pre + 'inflation/index.html', inflation_page(lang, ver))
        write(pre + 'ath/index.html', ath_page(lang, ver))
        write(pre + 'bitcoin-halving/index.html', halving_page(lang, ver))
        write(pre + 'exchanges/index.html', exchanges_page(lang, ver))
        write(pre + 'ai/index.html', ai_page(lang, ver))
        write(pre + 'me/index.html', me_page(lang, ver))
        write(pre + 'memes/index.html', memes_page(lang, ver))
        write(pre + 'world-assets/index.html', world_page(lang, ver))
        write(pre + 'activities/index.html', activities_page(lang, ver))
        extra_pages.append('activities')
        write(pre + 'portfolios/index.html', portfolios_page(lang, ver))
        extra_pages.append('portfolios')
        if lang in POLICY:
            write(pre + 'editorial-policy/index.html', policy_page(lang, ver))
            extra_pages.append('editorial-policy')
        if lang in GUIDE:
            write(pre + 'guide/index.html', guide_page(lang, ver))
            extra_pages.append('guide')
        extra_pages.append('world-assets')
        extra_pages.append('memes')
        extra_pages.append('ai')
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
        per_lang[lang] = [None, 'compare'] + list(HUBS) + extra_pages_c + TOOLS + extra_pages + assets_
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
    write('sitemap-news.xml', news_sitemap())
    nf = {'uk': ('Сторінку не знайдено', 'Можливо, актив перейменовано або видалено. Знайди його через пошук угорі або перейди до рейтингу.'),
          'en': ('Page not found', 'The asset may have been renamed or removed. Use the search above or go to the ranking.')}
    body404 = ''.join(f'<h1>{a}</h1><p class="lead">{b}</p><p><a class="btn" href="{url(lg)}">{HM[lg]["nav"]} →</a></p>' for lg, (a, b) in nf.items())
    write('404.html', shell('en', None, 'Page not found | ' + BRAND, nf['en'][1], body404, {}, ver).replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"'))
    write('79eea7b784b383a4b1696da51540fdf0.txt', '79eea7b784b383a4b1696da51540fdf0')
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /go/\nDisallow: /api/\nDisallow: /stats\nSitemap: {SITE}{BASE}/sitemap.xml\nSitemap: {SITE}{BASE}/sitemap-news.xml\n')
    total = sum(len(p) for p in per_lang.values())
    print(f"built {total} pages in {len(ORDER)} languages · {len(A)} assets · data {UPDATED}")


if __name__ == '__main__':
    main()
