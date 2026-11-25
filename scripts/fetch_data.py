"""Collect prices for every asset from free APIs into data/market.json.

Sources (no API keys needed):
  * Binance public market data (data-api.binance.vision): top crypto by 24h volume,
    monthly klines since listing, live price and 24h change.
  * Yahoo Finance (yfinance): curated assets in data/assets.json (long crypto history,
    stocks, ETFs, gold, silver) + every S&P 500 company.
  * CoinGecko public API: coin names, logos and market-cap rank (optional; skipped if it fails).
  * GitHub datasets/s-and-p-500-companies: the S&P 500 list with company names and sectors.

Every source is optional: if one fails, the assets it feeds keep their previous data
from the last successful run, so the site never breaks because of one bad day.

Run: python3 scripts/fetch_data.py            (everything)
     python3 scripts/fetch_data.py --quick    (curated assets only, for testing)
"""
import csv, io, json, math, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINNED = os.path.join(ROOT, 'data/assets.json')
OUT = os.path.join(ROOT, 'data/market.json')
MIN_START = '2000-01'
TOP_CRYPTO = 4000   # owner 2026-11-21: top 1–4000 by market cap like CoinMarketCap/CryptoRank (2026-11-20: 2000); pages outside TOP_N are static only in uk+en, the rest on demand
CG_PAGES = 16       # CoinGecko /coins/markets pages of 250 = top 4000
# owner 2026-11-23: STOP adding new coins for now — bring the existing ones to full quality first. Coins already in
# market.json keep updating; a coin not there yet is skipped. Set False to grow again.
CRYPTO_FROZEN = True
NEW_HIST_BUDGET = 450   # new coins whose history is looked up per run (the rest wait for the next run) — keeps the workflow under ~1 h
CG_HIST_BUDGET = 40     # of those, at most this many via CoinGecko market_chart (365 days, keyless rate limit)
NOHIST = os.path.join(ROOT, 'data/crypto_nohist.json')   # coins with no history anywhere: retried after 7 days
MARKETS = os.path.join(ROOT, 'data/markets.json')   # ETFs + national stocks (Ukraine, Poland, Germany...)
FX_TICKER = {c: c + '=X' for c in 'PLN EUR GBP TRY JPY KRW INR BRL HKD CNY TWD IDR THB PHP VND SAR CHF CAD AUD MXN RUB'.split()}   # Yahoo: units per 1 USD
SUFFIX_CCY = {'.WA': 'PLN', '.DE': 'EUR', '.PA': 'EUR', '.MC': 'EUR', '.MI': 'EUR', '.AS': 'EUR', '.L': 'GBp', '.IS': 'TRY', '.T': 'JPY', '.KS': 'KRW',
              '.NS': 'INR', '.SA': 'BRL', '.HK': 'HKD', '.SS': 'CNY', '.SZ': 'CNY', '.TW': 'TWD', '.JK': 'IDR', '.BK': 'THB', '.PS': 'PHP', '.VN': 'VND',
              '.SR': 'SAR', '.SW': 'CHF', '.TO': 'CAD', '.AX': 'AUD', '.MX': 'MXN', 'MOEX:': 'RUB'}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n_ctry3 import SUFFIX3  # noqa: E402  (19 more markets, 2026-11-21)
SUFFIX_CCY.update({suf: v[1] for suf, v in SUFFIX3.items()})
CENT = {'GBp': 'GBP', 'ILA': 'ILS', 'ZAc': 'ZAR'}   # Yahoo quotes London in pence, Tel Aviv in agorot, Johannesburg in cents
FX_TICKER.update({c: c + '=X' for c in {CENT.get(v[1], v[1]) for v in SUFFIX3.values()} if c != 'EUR'})
CMDTY_T = {'brent': 'BZ=F', 'ng': 'NG=F', 'copper': 'HG=F'}   # for the world-assets page
CMDTY = {}
INFO_KEYS = ('ath', 'athd', 'mcap', 'cgid', 'circ', 'supply', 'maxs', 'fdv', 'vol', 'atl', 'atld', 'c7', 's7')   # c7/s7: 7-day change + 7-day sparkline
YW = {}   # Yahoo ticker -> (7-day change, last daily closes) for the 7d column and sparkline
COININFO = os.path.join(ROOT, 'data/coininfo.json')    # links/description per coin, filled a few hundred per day
STOCKINFO = os.path.join(ROOT, 'data/stockinfo.json')  # website/sector/summary per stock, filled gradually
INFO_LANGS = ('uk', 'ru', 'es', 'pt', 'de', 'fr', 'it', 'pl', 'tr', 'nl', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar')
WRAPPED = ('wrapped', 'staked', 'bridged', 'restaked', 'liquid staking', 'tokenized', 'binance-peg', 'savings', 'usd')
BINANCE = 'https://data-api.binance.vision/api/v3'
SP500_CSV = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv'
STABLE = set('USDT USDC FDUSD TUSD USDP DAI BUSD EUR EURI AEUR USDE PYUSD XUSD USD1 BFUSD RLUSD UST USTC GBP TRY BRL '
              'AUD JPY RUB UAH ZAR NGN PLN ARS MXN COP CZK IDR VAI SUSD LUSD FRAX GUSD USDS USDD PAXG XAUT WBTC WBETH BETH BNSOL'.split())
UA = {'User-Agent': 'WhatIfStack/1.0 (+https://whatifstack.com/)'}


def log(*a):
    print(*a, flush=True)


T0 = time.time()                      # run budget: optional extras (descriptions) stop after BUDGET seconds
BUDGET = 50 * 60


def get_json(url, tries=3, timeout=30):
    url = urllib.parse.quote(url, safe=':/?&=%,.-_~+')   # non-Latin tickers (e.g. 币安人生) → percent-encoded
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return json.load(r)
        except Exception as e:
            log(f"  GET failed ({k + 1}/{tries}) {url[:90]}: {e}")
            time.sleep(2 * (k + 1))
    return None


def get_text(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return r.read().decode('utf-8')
    except Exception as e:
        log(f"  GET failed {url}: {e}")
        return None


def ym2i(s):
    y, m = map(int, s.split('-'))
    return y * 12 + m - 1


def i2ym(i):
    return f"{i // 12}-{i % 12 + 1:02d}"


def to_series(points):
    """[(YYYY-MM, close)] -> {start,end,p} with every month present (forward-filled)."""
    by = {}
    for ym, c in points:
        try:
            c = float(c)
        except (TypeError, ValueError):
            continue
        if c > 0 and not math.isnan(c) and ym >= MIN_START:
            by[ym] = c
    if not by:
        return None
    ms = sorted(by)
    s, e = ym2i(ms[0]), ym2i(ms[-1])
    p, last = [], None
    for i in range(s, e + 1):
        last = by.get(i2ym(i), last)
        p.append(float(f"{last:.6g}"))
    return {'start': ms[0], 'end': ms[-1], 'p': p}


# ---------------- Binance ----------------
def binance_top():
    tick = get_json(f"{BINANCE}/ticker/24hr")
    if not tick:
        return []
    rows = []
    for t in tick:
        s = t.get('symbol', '')
        if not s.endswith('USDT'):
            continue
        base = s[:-4]
        if base in STABLE or base.endswith(('UP', 'DOWN', 'BULL', 'BEAR')) or not base.isalnum():
            continue
        qv = float(t.get('quoteVolume') or 0)
        if qv <= 0 or int(t.get('count') or 0) == 0:
            continue
        rows.append(dict(base=base, symbol=s, qv=qv, price=float(t['lastPrice']), chg=float(t['priceChangePercent']) / 100))
    rows.sort(key=lambda r: -r['qv'])
    return rows


def binance_monthly(symbol):
    k = get_json(f"{BINANCE}/klines?symbol={symbol}&interval=1M&limit=1000")
    if not k:
        return None
    pts = [(datetime.fromtimestamp(r[0] / 1000, timezone.utc).strftime('%Y-%m'), r[4]) for r in k]
    return to_series(pts)


def other_monthly(base):
    """Monthly USDT history for a coin not on Binance: Gate.io, then MEXC, then OKX."""
    d = get_json(f"https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair={base}_USDT&interval=30d&limit=1000", tries=1, timeout=10)
    if isinstance(d, list) and d:
        return to_series((datetime.fromtimestamp(int(r[0]), timezone.utc).strftime('%Y-%m'), r[2]) for r in d), 'gate'
    d = get_json(f"https://api.mexc.com/api/v3/klines?symbol={base}USDT&interval=1M&limit=1000", tries=1, timeout=10)
    if isinstance(d, list) and d:
        return to_series((datetime.fromtimestamp(r[0] / 1000, timezone.utc).strftime('%Y-%m'), r[4]) for r in d), 'mexc'
    d = get_json(f"https://www.okx.com/api/v5/market/history-candles?instId={base}-USDT&bar=1Mutc&limit=100", tries=1, timeout=10)
    if isinstance(d, dict) and d.get('data'):
        return to_series((datetime.fromtimestamp(int(r[0]) / 1000, timezone.utc).strftime('%Y-%m'), r[4]) for r in d['data']), 'okx'
    d = get_json(f"https://api.bybit.com/v5/market/kline?category=spot&symbol={base}USDT&interval=M&limit=1000", tries=1, timeout=10)
    rows = ((d or {}).get('result') or {}).get('list') if isinstance(d, dict) else None
    if rows:
        return to_series((datetime.fromtimestamp(int(r[0]) / 1000, timezone.utc).strftime('%Y-%m'), r[4]) for r in rows), 'bybit'
    # coins delisted from Binance/Gate/MEXC/OKX (Monero, Helium...): Kraken 15-day candles, then Yahoo <TK>-USD
    d = get_json(f"https://api.kraken.com/0/public/OHLC?pair={base}USD&interval=21600", tries=1, timeout=15)
    res = (d or {}).get('result') if isinstance(d, dict) else None
    if res and not (d.get('error') or []):
        rows = next((v for k, v in res.items() if k != 'last' and isinstance(v, list)), [])
        if len(rows) >= 6:
            return to_series((datetime.fromtimestamp(int(r[0]), timezone.utc).strftime('%Y-%m'), r[4]) for r in rows), 'kraken'
    try:
        ys = yahoo_monthly([f'{base}-USD']).get(f'{base}-USD')
        if ys and len(ys['p']) >= 6:
            return ys, 'yahoo-cc'
    except Exception as e:
        log(f"  yahoo {base}-USD: {e}")
    return None, None


def coingecko_monthly(cgid):
    """Last resort for coins on no exchange we read: CoinGecko daily prices for 365 days (the keyless limit) -> month-end closes."""
    if not cgid:
        return None
    d = get_json(f"https://api.coingecko.com/api/v3/coins/{cgid}/market_chart?vs_currency=usd&days=365&interval=daily", tries=1, timeout=15)
    pts = (d or {}).get('prices') if isinstance(d, dict) else None
    if not pts or len(pts) < 45:
        return None
    return to_series((datetime.fromtimestamp(t / 1000, timezone.utc).strftime('%Y-%m'), v) for t, v in pts)


MOEX = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities'


def moex_monthly(secid):
    pts, start = [], 0
    for _ in range(5):
        d = get_json(f"{MOEX}/{secid}/candles.json?interval=31&from=2000-01-01&start={start}&iss.meta=off", tries=2)
        rows = (d or {}).get('candles', {}).get('data') or []
        cols = (d or {}).get('candles', {}).get('columns') or []
        if not rows:
            break
        ic, ib = cols.index('close'), cols.index('begin')
        pts += [(r[ib][:7], r[ic]) for r in rows]
        if len(rows) < 500:
            break
        start += 500
    return to_series(pts)


def moex_last(secids):
    out = {}
    for i in range(0, len(secids), 80):   # ~300 MOEX shares since 2026-11-21: keep URLs short
        d = get_json(f"{MOEX}.json?securities={','.join(secids[i:i + 80])}&iss.only=marketdata&marketdata.columns=SECID,LAST,LASTTOPREVPRICE&iss.meta=off", tries=2)
        for sid, last, chg in ((d or {}).get('marketdata', {}).get('data') or []):
            if last:
                out[sid] = (float(last), (chg or 0) / 100)
    return out


def rub_fx_fallback():
    """Monthly USD/RUB from the Central Bank of Russia if Yahoo has no RUB=X."""
    import xml.etree.ElementTree as ET
    now = datetime.now(timezone.utc)
    txt = get_text(f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2000&date_req2={now:%d/%m/%Y}&VAL_NM_RQ=R01235")
    if not txt:
        return None
    try:
        root = ET.fromstring(txt.encode('utf-8') if isinstance(txt, str) else txt)
    except Exception:
        return None
    pts = []
    for rec in root.findall('Record'):
        dd, mm, yy = rec.get('Date').split('.')
        pts.append((f"{yy}-{mm}", float(rec.find('Value').text.replace(',', '.')) / float(rec.find('Nominal').text)))
    return to_series(pts)


def slug(t):
    import re, unicodedata
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:40] or 'x'


def extend_old(o, price, now):
    """Reuse a stored monthly series and roll it forward to this month with today's price (no need to re-download history)."""
    if not o or not o.get('p') or not price:
        return None
    p, end = list(o['p']), ym2i(o['start']) + len(o['p']) - 1
    cur = now.year * 12 + now.month - 1
    if cur - end > 3:
        return None
    p += [price] * (cur - end)
    p[-1] = float(f"{price:.6g}")
    return {'start': o['start'], 'end': i2ym(cur), 'p': p}


def to_usd(series, ccy, fxm):
    """Convert a monthly local-currency series to USD with monthly FX (units per USD)."""
    if not series or ccy == 'USD':
        return series
    div = 100.0 if ccy in CENT else 1.0
    fx = fxm.get(FX_TICKER.get(CENT.get(ccy, ccy)))
    if not fx:
        return None
    f0 = ym2i(fx['start'])
    out = []
    for k, v in enumerate(series['p']):
        j = min(max(ym2i(series['start']) + k - f0, 0), len(fx['p']) - 1)
        out.append(float(f"{v / div / fx['p'][j]:.6g}"))
    return dict(series, p=out)


def fix_x100(series):
    """London prices: Yahoo mixes pence and pounds month to month. Lift months that are ~100x below their neighbours."""
    if not series:
        return series
    p = list(series['p'])
    for i, v in enumerate(p):
        nb = sorted(x for x in p[max(0, i - 4):i] + p[i + 1:i + 5] if x > 0)
        if not nb or v <= 0:
            continue
        m = nb[len(nb) // 2]
        if abs(math.log(v * 100 / m)) + 2 < abs(math.log(v / m)):
            p[i] = float(f"{v * 100:.6g}")
    return dict(series, p=p)


def broken(series):
    """Redenominations / token swaps: a single month moving more than 30x makes DCA numbers meaningless."""
    p = series['p']
    return any(p[i - 1] > 0 and not (1 / 30 < p[i] / p[i - 1] < 30) for i in range(1, len(p)))


def trim_breaks(series):
    """Keep only the history after the last >30x one-month jump (old redenominations, unadjusted splits). None if < 12 months left."""
    p = series['p']
    cut = max([i for i in range(1, len(p)) if p[i - 1] > 0 and not (1 / 30 < p[i] / p[i - 1] < 30)] or [0])
    if not cut:
        return series
    if len(p) - cut < 12:
        return None
    s0 = ym2i(series['start']) + cut
    return dict(series, start=i2ym(s0), p=p[cut:])


def looks_stable(series):
    p = series['p'][-12:]
    return len(p) >= 3 and all(0.97 < x < 1.03 for x in p)


# ---------------- CoinGecko (names/logos) ----------------
CG_LIST = []   # symbols of the top coins by market cap, biggest first
BUBLIST = []   # top coins by market cap with 1h/24h/7d/30d/1y change, for the bubble map


def _spark7(pts, n=24):
    """168 hourly prices -> n evenly spaced points (4 significant digits) for a small 7-day chart."""
    pts = [x for x in pts if isinstance(x, (int, float)) and x > 0]
    if len(pts) < 8:
        return None
    return [float(f'{pts[round(k * (len(pts) - 1) / (n - 1))]:.4g}') for k in range(n)]


def coingecko_meta():
    meta = {}
    for page in range(1, CG_PAGES + 1):   # top 4000 by market cap
        if page > 1:
            time.sleep(8)   # stay under CoinGecko's free rate limit (2026-11-21: 4 s hit 429 at page 6 of 16)
        u = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={page}&price_change_percentage=1h,24h,7d,30d,1y&sparkline=true"
        d = get_json(u, tries=2)
        for wait in (45, 75):          # rate-limited: wait for the window to reset instead of stopping at ~1200 coins
            if isinstance(d, list):
                break
            log(f"  CoinGecko page {page}: waiting {wait} s")
            time.sleep(wait)
            d = get_json(u, tries=1)
        if not isinstance(d, list):
            break
        for c in d:
            sym = (c.get('symbol') or '').upper()
            if sym and sym not in meta:          # first = biggest market cap wins
                meta[sym] = dict(name=c.get('name'), logo=c.get('image'), rank=c.get('market_cap_rank'), mcap=c.get('market_cap'),
                                 ath=c.get('ath'), athd=(c.get('ath_date') or '')[:10] or None,
                                 cgid=c.get('id'), circ=c.get('circulating_supply'), supply=c.get('total_supply'), maxs=c.get('max_supply'),
                                 fdv=c.get('fully_diluted_valuation'), vol=c.get('total_volume'), atl=c.get('atl'), atld=(c.get('atl_date') or '')[:10] or None,
                                 price=c.get('current_price'), chg=(c['price_change_percentage_24h'] / 100 if isinstance(c.get('price_change_percentage_24h'), (int, float)) else None),
                                 c7=(round(c['price_change_percentage_7d_in_currency'] / 100, 5) if isinstance(c.get('price_change_percentage_7d_in_currency'), (int, float)) else None),
                                 s7=_spark7(((c.get('sparkline_in_7d') or {}).get('price')) or []))
                CG_LIST.append(sym)
            if page == 1 and sym and c.get('current_price'):
                r = lambda k: round(c[k] / 100, 5) if isinstance(c.get(k), (int, float)) else None
                BUBLIST.append(dict(s=sym, n=c.get('name'), l=(c.get('image') or '').replace('/large/', '/small/'),
                                    pr=c.get('current_price'), mc=c.get('market_cap'),
                                    h=r('price_change_percentage_1h_in_currency'), d=r('price_change_percentage_24h_in_currency'),
                                    w=r('price_change_percentage_7d_in_currency'), m=r('price_change_percentage_30d_in_currency'),
                                    y=r('price_change_percentage_1y_in_currency')))
        time.sleep(3)
    log(f"CoinGecko meta: {len(meta)} coins")
    return meta


def exchange_extras(cg, have):
    """Symbols from data/exchanges.json top pairs that are missing from the market-cap list (CryptoRank-style coverage).
    Skips stablecoins, tokenized stocks and wrapped/staked tokens. Adds their CoinGecko meta to cg."""
    try:
        ex = json.load(open(os.path.join(ROOT, 'data/exchanges.json'), encoding='utf-8'))
    except Exception:
        return []
    ids = {}
    for d in ex.get('detail', {}).values():
        for p in d.get('pairs', []):
            b, cid = (p.get('b') or '').upper(), p.get('cg') or ''
            if not cid or b in have or b in STABLE or not b.isalnum():
                continue
            if any(w in cid for w in ('stock', 'bstock', 'rstock', 'xstock', 'usd', 'staked', 'wrapped', 'bridged', 'peg', 'gold', 'etf')):
                continue
            ids[cid] = ids.get(cid, 0) + (p.get('usd') or 0)
    best = [c for c, _ in sorted(ids.items(), key=lambda z: -z[1])][:150]
    out = []
    for k in range(0, len(best), 100):
        d = get_json('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=' + ','.join(best[k:k + 100]), tries=2)
        for c in d if isinstance(d, list) else []:
            sym = (c.get('symbol') or '').upper()
            if not sym or sym in have or sym in cg or not c.get('current_price') or (c.get('total_volume') or 0) < 1e6:
                continue
            cg[sym] = dict(name=c.get('name'), logo=c.get('image'), rank=c.get('market_cap_rank'), mcap=c.get('market_cap'), cgid=c.get('id'),
                           ath=c.get('ath'), athd=(c.get('ath_date') or '')[:10] or None, circ=c.get('circulating_supply'), supply=c.get('total_supply'),
                           maxs=c.get('max_supply'), fdv=c.get('fully_diluted_valuation'), vol=c.get('total_volume'), price=c.get('current_price'),
                           chg=(c['price_change_percentage_24h'] / 100 if isinstance(c.get('price_change_percentage_24h'), (int, float)) else None))
            out.append(sym)
        time.sleep(3)
    log(f"exchange extras: {len(out)} coins ({', '.join(out[:20])})")
    return out


# ---------------- Yahoo ----------------
def yahoo_monthly(tickers):
    """{ticker: series} using batched yfinance downloads."""
    import yfinance as yf
    out = {}
    for k in range(0, len(tickers), 100):
        chunk = tickers[k:k + 100]
        try:
            df = yf.download(chunk, period='max', interval='1mo', auto_adjust=True, group_by='ticker',
                             threads=True, progress=False)
        except Exception as e:
            log(f"  yahoo batch failed: {e}")
            continue
        for t in chunk:
            try:
                col = df[t]['Close'] if len(chunk) > 1 else df['Close']
                if hasattr(col, 'columns'):
                    col = col.iloc[:, 0]
                s = to_series((ts.strftime('%Y-%m'), v) for ts, v in col.items())
                if s:
                    out[t] = s
            except Exception as e:
                log(f"  yahoo {t}: {e}")
    return out


def yahoo_daily(tickers):
    """{ticker: (last_price, change_vs_prev_close)}"""
    import yfinance as yf
    out = {}
    for k in range(0, len(tickers), 200):
        chunk = tickers[k:k + 200]
        try:
            df = yf.download(chunk, period='12d', interval='1d', auto_adjust=True, group_by='ticker', threads=True, progress=False)
        except Exception as e:
            log(f"  yahoo daily batch failed: {e}")
            continue
        for t in chunk:
            try:
                col = (df[t]['Close'] if len(chunk) > 1 else df['Close']).dropna()
                if hasattr(col, 'columns'):
                    col = col.iloc[:, 0]
                if len(col) >= 2:
                    out[t] = (float(col.iloc[-1]), float(col.iloc[-1] / col.iloc[-2] - 1))
                    wk = col.iloc[-6:]   # ~one trading week (5 sessions back)
                    if len(wk) >= 3:
                        YW[t] = (round(float(wk.iloc[-1] / wk.iloc[0] - 1), 5), [float(f'{float(v):.4g}') for v in col.iloc[-8:]])
            except Exception:
                pass
    return out


def sp500():
    txt = get_text(SP500_CSV)
    if not txt:
        return []
    return [dict(tk=r['Symbol'].strip(), name=r['Security'].strip(), sector=r.get('GICS Sector', '').strip())
            for r in csv.DictReader(io.StringIO(txt))]



# ---------------- market-wide widgets ----------------
def market_global(cg_meta):
    """Crypto market cap, BTC dominance, Fear & Greed, trending coins. Saved to data/global.json."""
    g = {}
    d = get_json('https://api.coingecko.com/api/v3/global', tries=2)
    if d and 'data' in d:
        x = d['data']
        g['mcap'] = x.get('total_market_cap', {}).get('usd')
        g['mcap_chg'] = x.get('market_cap_change_percentage_24h_usd')
        g['vol'] = x.get('total_volume', {}).get('usd')
        g['btc_dom'] = x.get('market_cap_percentage', {}).get('btc')
        g['eth_dom'] = x.get('market_cap_percentage', {}).get('eth')
        g['coins'] = x.get('active_cryptocurrencies')
    f = get_json('https://api.alternative.me/fng/?limit=31', tries=2)
    if f and f.get('data'):
        g['fng'] = [int(v['value']) for v in f['data']]          # newest first
    t = get_json('https://api.coingecko.com/api/v3/search/trending', tries=2)
    if t and t.get('coins'):
        g['trending'] = [c['item']['symbol'].upper() for c in t['coins'][:10]]
    return g


# ---------------- fiat exchange rates ----------------
FIATS = ('EUR UAH PLN GBP CHF CZK HUF RON SEK NOK DKK TRY RUB KZT GEL MDL BRL MXN ARS COP CLP INR IDR VND THB PHP '
         'MYR SGD JPY KRW CNY HKD TWD AED SAR ILS EGP NGN ZAR KES CAD AUD NZD PKR BDT').split()


def fx_rates():
    """Units of each currency per 1 USD (open.er-api.com, free, no key). Saved to data/fx.json."""
    d = get_json('https://open.er-api.com/v6/latest/USD', tries=3)
    if not d or d.get('result') != 'success':
        return None
    rates = {c: d['rates'][c] for c in FIATS if c in d.get('rates', {})}
    return rates if len(rates) > 20 else None

# ---------------- logos: downloaded once, stored as 64px webp in data/logos/ ----------------
LOGOS = os.path.join(ROOT, 'data/logos')


def get_bytes(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            if not (r.headers.get('Content-Type') or '').startswith('image'):
                return None
            return r.read()
    except Exception:
        return None


def logo_quality(im):
    """'ok' | 'white' (only white/near-white strokes: invisible on light UIs) | 'empty' (almost nothing visible)."""
    px = list(im.convert('RGBA').resize((32, 32)).getdata())
    vis = [p for p in px if p[3] > 100]
    if len(vis) < 20:
        return 'empty'
    if all(p[0] > 225 and p[1] > 225 and p[2] > 225 for p in vis):
        return 'white'
    return 'ok'


# company sites for stocks without a Yahoo profile (MOEX listings): the logo comes from the site's icon
LOGO_DOMAIN = {
    'sber': 'sberbank.com', 'gazp': 'gazprom.ru', 'lkoh': 'lukoil.ru', 'rosn': 'rosneft.ru', 'nvtk': 'novatek.ru',
    'gmkn': 'nornickel.ru', 'tatn': 'tatneft.ru', 'sngs': 'surgutneftegas.ru', 'plzl': 'polyus.com', 'ydex': 'yandex.ru',
    'mgnt': 'magnit.ru', 'chmf': 'severstal.com', 'nlmk': 'nlmk.com', 'mtss': 'mts.ru', 'alrs': 'alrosa.ru', 'vtbr': 'vtb.ru',
    'moex': 'moex.com', 'phor': 'phosagro.ru', 'rual': 'rusal.ru', 'ozon': 'ozon.ru', 't-ru': 'tbank.ru', 'irao': 'interrao.ru',
    'aflt': 'aeroflot.ru', 'pikk': 'pik.ru', 'magn': 'mmk.ru', 'x5': 'x5.ru', 'head': 'hh.ru', 'smlt': 'samolet.ru',
    'trnfp': 'transneft.ru', 'afks': 'sistema.ru',
    # owner 2026-11-25: stocks still without a logo (no Yahoo profile / website)
    'sibn': 'gazprom-neft.ru', 'domrf': 'domrf.ru', 'unac': 'uacrussia.ru', 'cbom': 'mkb.ru', 'vsmo': 'vsmpo.ru', 'hydr': 'rushydro.ru',
    'svcb': 'sovcombank.ru', 'irkt': 'yakovlev.ru', 'lent': 'lenta.com', 'fesh': 'fesco.ru', 'evrz': 'evraz.com', 'enpg': 'enplusgroup.com',
    'flot': 'scf-group.ru', 'bane': 'bashneft.ru', 'gche': 'cherkizovo.com', 'ugld': 'uzhuralzoloto.ru', 'rtkm': 'rostelecom.ru',
    'fees': 'rosseti.ru', 'nmtp': 'nmtp.info', 'vkco': 'vk.company', 'mgts': 'mgts.ru', 'bspb': 'bspb.ru', 'mdmg': 'mamadeti.ru',
    'posi': 'ptsecurity.com', 'lsrg': 'lsrgroup.ru', 'leas': 'europlan.ru', 'rasp': 'raspadskaya.ru', 'nknc': 'nknh.ru', 'cnru': 'cian.ru',
    'utar': 'utair.ru', 'upro': 'unipro.energy', 'trmk': 'tmk-group.com', 'ragr': 'rusagrogroup.ru', 'fixr': 'fix-price.com',
    'sgzh': 'segezha-group.com', 'akrn': 'acron.ru', 'kmaz': 'kamaz.ru', 'mbnk': 'mtsbank.ru', 'belu': 'novabev.com', 'selg': 'seligdar.ru',
    'mtlr': 'mechel.ru', 'sofl': 'softline.ru', 'etln': 'etalongroup.com', 'spbe': 'spbexchange.ru', 'mvid': 'mvideo.ru',
    'abrd': 'abraudurso.ru', 'deli': 'delimobil.ru', 'rgss': 'rgs.ru', 'kzos': 'kazanorgsintez.ru', 'aptk': 'apteka.ru', 'elmt': 'element-group.ru',
    'avan': 'avangard.ru', 'reni': 'renins.ru', 'ozph': 'ozonpharm.ru', 'uwgn': 'uwc.ru', 'dias': 'diasoft.ru', 'zaym': 'zaymer.ru',
    'hnfg': 'henderson.ru', 'mstt': 'mostotrest.ru', 'rkke': 'energia.ru', 'ivat': 'iva-tech.ru', 'glrx': 'glorax.com', 'svav': 'sollers-auto.com',
    'hpg': 'hoaphat.com.vn', 'mbb': 'mbbank.com.vn', 'mwg': 'mwg.vn', 'sbra': 'sabrahealth.com', 'strl': 'strlco.com', 'uthr': 'unither.com',
    'lcid': 'lucidmotors.com', 'wpc': 'wpcarey.com', 'edp': 'edp.com', 'edpr': 'edpr.com', 'richter': 'gedeonrichter.com', 'comi': 'cibeg.com',
    'tmgh': 'talaatmoustafa.com', 'etel': 'te.eg', 'c5h': 'cairnhomes.com', 'tabak': 'pmi.com', 'mtelekom': 'telekom.hu', 'hrho': 'efghermes.com',
    'swdy': 'elsewedyelectric.com', 'abuk': 'abuqir.com', 'ift': 'infratil.com', 'peoles': 'penoles.com.mx', 'sof': 'sofinagroup.com',
    'die': 'dieteren.com', 'titc': 'titan-cement.com', 'any': 'any.hu', 'efih': 'e-finance.com.eg', 'embj3': 'embraer.com',
    'livepolc-1': 'liverpool.com.mx', 'sands-china': 'sandschina.com', 'prox': 'proximus.com', 'cener': 'cenergyholdings.com',
    'phdc': 'palmhillsdevelopments.com', 'amoc': 'amoc.com.eg', 'mfpc': 'mopco-eg.com', 'irsa': 'irsa.com.ar', 'andina-b': 'koandina.com',
    'ra': 'banregio.com', 'tabgd': 'tabgida.com.tr', 'alteo': 'alteo.hu', 'cigpannonia': 'cigpannonia.hu', 'oras': 'orascom.com',
    'emfd': 'emaarmisr.com', 'jufo': 'juhayna.com', 'clho': 'cleopatrahospitals.com', 'mtln': 'metlengroup.com', 'genting': 'genting.com',
}


# official logos from Wikimedia Commons where the company site blocks foreign servers (Google favicon = blank globe)
LOGO_URL = {k: 'https://commons.wikimedia.org/wiki/Special:FilePath/' + v.replace(' ', '%20') + '?width=128' for k, v in {
    'gazp': 'Gazprom logo.svg', 'magn': 'Magnitogorsk Iron and Steel Works logo.svg', 'nlmk': 'NLMK Logo.svg', 'rosn': 'Rosneft 201x logo.svg'}.items()}


def fetch_logos(assets):
    try:
        from PIL import Image, ImageDraw
        import io
    except ImportError:
        log('logos: pillow not installed, skipped')
        return
    os.makedirs(LOGOS, exist_ok=True)
    have = {f[:-5] for f in os.listdir(LOGOS) if f.endswith('.webp')}
    # one-time repair: logos that are empty or white-only get re-fetched from other sources (list kept in data/logos/_checked.json)
    ck_path = os.path.join(LOGOS, '_checked.json')
    try:
        checked = set(json.load(open(ck_path)))
    except Exception:
        checked = set()
    redo = set()
    for aid in have - checked:
        try:
            if logo_quality(Image.open(os.path.join(LOGOS, aid + '.webp'))) != 'ok':
                redo.add(aid)
        except Exception:
            redo.add(aid)
    sinfo = {}
    try:
        sinfo = json.load(open(os.path.join(ROOT, 'data/stockinfo.json'), encoding='utf-8'))
    except Exception:
        pass
    # Moscow Exchange listings: the brand logo from the T-Bank investment app CDN, keyed by ISIN (ISIN list from MOEX ISS)
    isin = {}
    if any(a.get('mkt') == 'ru' and (aid not in have or aid in redo) for aid, a in assets.items()):
        try:
            d = get_json(MOEX + '.json?iss.meta=off&iss.only=securities&securities.columns=SECID,ISIN', tries=2) or {}
            isin = {r[0].lower(): r[1] for r in (d.get('securities') or {}).get('data') or [] if r[1]}
        except Exception as e:
            log(f'logos: MOEX ISIN list failed: {e}')
    n = fixed = 0
    for aid, a in assets.items():
        if aid in have and aid not in redo:
            continue
        tk = a.get('tk', '')
        urls = []
        if aid in LOGO_URL:
            urls.append(LOGO_URL[aid])
        if a.get('logo'):
            urls.append(a['logo'].replace('/large/', '/small/'))
        if a.get('mkt') == 'ru' and isin.get(aid):
            urls.append(f'https://invest-brands.cdn-tinkoff.ru/{isin[aid]}x160.png')
        if a.get('cat') == 'crypto':
            urls.append(f'https://bin.bnbstatic.com/static/assets/logos/{tk}.png')
        elif a.get('cat') in ('stock', 'etf'):
            urls.append(f'https://financialmodelingprep.com/image-stock/{(a.get("yahoo") if a.get("mkt") else tk.replace("-", "."))}.png')
            web = (sinfo.get(a.get('yahoo') or '', {}) or {}).get('web') or ''
            dom = web.split('//')[-1].split('/')[0].replace('www.', '') if web else ''
            dom = dom or LOGO_DOMAIN.get(aid, '')
            if dom:   # the company's own site icon (works for most companies, incl. Vietnam/Thailand/Saudi listings)
                urls.append(f'https://www.google.com/s2/favicons?domain={dom}&sz=128')
                urls.append(f'https://icons.duckduckgo.com/ip3/{dom}.ico')
        best = None
        for u in urls:
            b = get_bytes(u)
            if not b or len(b) < 200:
                continue
            try:
                im = Image.open(io.BytesIO(b)).convert('RGBA')
                if im.width < 32 and 'favicons' not in u and '.ico' not in u:
                    continue
                q = logo_quality(im)
                if q == 'empty':
                    continue
                best = (im, q)
                if q == 'ok':
                    break
            except Exception:
                continue
        if best:
            im, q = best
            im.thumbnail((64, 64))
            bg = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
            if q == 'white':   # white logo: bake in a dark round backing so it is visible everywhere
                ImageDraw.Draw(bg).ellipse((0, 0, 63, 63), fill=(31, 41, 55, 255))
                im.thumbnail((44, 44))
            bg.paste(im, ((64 - im.width) // 2, (64 - im.height) // 2), im)
            bg.save(os.path.join(LOGOS, aid + '.webp'), 'WEBP', quality=85)
            n += 1
            fixed += aid in redo
        elif aid in redo:
            try:
                os.remove(os.path.join(LOGOS, aid + '.webp'))   # a blank logo is worse than our initials badge
            except Exception:
                pass
        checked.add(aid)
        time.sleep(0.05)
    checked |= have - redo
    json.dump(sorted(checked), open(ck_path, 'w'))
    log(f'logos: {n} new/replaced ({fixed} repaired), {len(redo)} were bad')


def make_sprite(size=52, cols=16):
    """Pack the logos of the ~160 most visible assets (data/sprite_ids.json, written by build.py) into one image: one request instead of dozens."""
    from PIL import Image
    ids_f = os.path.join(ROOT, 'data/sprite_ids.json')
    if not os.path.exists(ids_f):
        return
    ids = [i for i in json.load(open(ids_f)) if os.path.exists(os.path.join(LOGOS, i + '.webp'))]
    if not ids:
        return
    rows = (len(ids) + cols - 1) // cols
    sheet = Image.new('RGBA', (cols * size, rows * size), (0, 0, 0, 0))
    for k, i in enumerate(ids):
        im = Image.open(os.path.join(LOGOS, i + '.webp')).convert('RGBA').resize((size, size), Image.LANCZOS)
        sheet.paste(im, (k % cols * size, k // cols * size), im)
    sheet.save(os.path.join(ROOT, 'data/logo-sprite.webp'), 'WEBP', quality=88, method=6)
    json.dump({'cols': cols, 'rows': rows, 'size': size, 'ids': {i: k for k, i in enumerate(ids)}}, open(os.path.join(ROOT, 'data/logo-sprite.json'), 'w'), separators=(',', ':'))
    log(f'sprite: {len(ids)} logos')


# ---------------- inflation (World Bank, annual CPI %) ----------------
CPI_COUNTRIES = ('USA UKR ESP BRA DEU FRA ITA POL TUR NLD RUS IDN VNM THA IND JPN KOR CHN ARE PHL GBR MEX ARG KAZ CAN AUS').split()


def inflation():
    """{ISO3: {year: inflation %}} annual consumer price inflation. Saved to data/cpi.json."""
    out = {}
    for c in CPI_COUNTRIES:
        d = get_json(f'https://api.worldbank.org/v2/country/{c}/indicator/FP.CPI.TOTL.ZG?format=json&per_page=80&date=1960:2030', tries=4)
        if isinstance(d, list) and len(d) > 1 and d[1]:
            v = {r['date']: round(r['value'], 3) for r in d[1] if r.get('value') is not None}
            if v:
                out[c] = v
        time.sleep(1.5)
    return out if len(out) > 10 else None


# ---------------- per-asset info (links, descriptions), incremental ----------------
def _clean(t, n=700):
    import re
    t = re.sub(r'<[^>]+>', '', t or '').replace('\r', '').strip()
    t = re.sub(r'\s+', ' ', t)
    return (t[:n].rsplit(' ', 1)[0] + '…') if len(t) > n else t


def coin_info(assets, budget=320):
    info = json.load(open(COININFO, encoding='utf-8')) if os.path.exists(COININFO) else {}
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    todo = sorted((a for a in assets.values() if a.get('cat') == 'crypto' and a.get('cgid')), key=lambda a: a.get('rank') or 9999)
    from datetime import timedelta
    cutoff = (datetime.now(timezone.utc) - timedelta(days=45)).strftime('%Y-%m-%d')
    todo = [a for a in todo if info.get(a['cgid'], {}).get('d', '') < cutoff]
    todo.sort(key=lambda a: (a['cgid'] in info, a.get('rank') or 9999))   # coins with no info at all first (the description task waits for them), then stale ones
    n = 0
    for a in todo[:budget]:
        if time.time() - T0 > BUDGET:
            break
        d = get_json(f"https://api.coingecko.com/api/v3/coins/{a['cgid']}?localization=true&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false", tries=2)
        time.sleep(2.6)
        if d is None:                                   # rate-limited: wait a minute and retry once
            time.sleep(65)
            d = get_json(f"https://api.coingecko.com/api/v3/coins/{a['cgid']}?localization=true&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false", tries=1)
            if d is None:
                break                                   # still limited: continue tomorrow
        if not isinstance(d, dict) or 'links' not in d:
            continue
        L = d.get('links') or {}
        first = lambda v: next((x for x in (v or []) if x), None)
        links = dict(web=first(L.get('homepage')), wp=L.get('whitepaper') or None, exp=first(L.get('blockchain_site')),
                     x=('https://x.com/' + L['twitter_screen_name']) if L.get('twitter_screen_name') else None,
                     tg=('https://t.me/' + L['telegram_channel_identifier']) if L.get('telegram_channel_identifier') else None,
                     rd=L.get('subreddit_url') if (L.get('subreddit_url') or '').rstrip('/') not in ('https://www.reddit.com', 'https://reddit.com') else None,
                     gh=first((L.get('repos_url') or {}).get('github')))
        desc = d.get('description') or {}
        ds = {'en': _clean(desc.get('en'))}
        for lg in INFO_LANGS:
            t = _clean(desc.get(lg))
            if t and t != ds['en']:
                ds[lg] = t
        info[a['cgid']] = dict(l={k: v for k, v in links.items() if v}, ds={k: v for k, v in ds.items() if v},
                               cat=[c for c in (d.get('categories') or []) if c][:6], d=today)
        n += 1
    json.dump(info, open(COININFO, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    log(f"coin info: +{n}, {len(info)} total")


def stock_info(assets, budget=450):
    try:
        import yfinance as yf
    except ImportError:
        return
    info = json.load(open(STOCKINFO, encoding='utf-8')) if os.path.exists(STOCKINFO) else {}
    todo = [a for a in assets.values() if a.get('cat') in ('stock', 'etf') and a.get('yahoo') and not a['yahoo'].startswith('MOEX:') and a['yahoo'] not in info]
    n = 0
    for a in todo[:budget]:
        if time.time() - T0 > BUDGET:
            break
        try:
            i = yf.Ticker(a['yahoo']).info or {}
        except Exception as e:
            log(f"  info {a['yahoo']}: {e}")
            time.sleep(2)
            continue
        info[a['yahoo']] = {k: v for k, v in dict(web=i.get('website'), sec=i.get('sector'), ind=i.get('industry'), cty=i.get('country'),
                                                   emp=i.get('fullTimeEmployees'), mcap=i.get('marketCap'),
                                                   ds={'en': _clean(i.get('longBusinessSummary'))} if i.get('longBusinessSummary') else None).items() if v}
        n += 1
        time.sleep(0.6)
    json.dump(info, open(STOCKINFO, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    log(f"stock info: +{n}, {len(info)} total")


# ---------------- main ----------------
def hot_stocks(mk, have, n=5):
    """Owner 2026-11-24: stocks everyone is talking about (new IPOs like SpaceX/Anthropic, trending tickers) join the site
    automatically. Yahoo's US trending list -> ordinary US shares worth >= $5B that we do not have yet -> appended to
    data/markets.json (at most n per run). Any failure just skips this step."""
    try:
        import yfinance as yf
        js = get_json('https://query1.finance.yahoo.com/v1/finance/trending/US?count=30')
        syms = [q['symbol'] for q in js['finance']['result'][0]['quotes']]
    except Exception as e:
        log(f"  hot stocks: trending list failed: {e}")
        return []
    added = []
    for s in syms:
        if len(added) >= n:
            break
        if s in have or not s.replace('-', '').isalpha() or '.' in s or '=' in s or '^' in s:
            continue
        try:
            inf = yf.Ticker(s).info or {}
        except Exception:
            continue
        if inf.get('quoteType') != 'EQUITY' or (inf.get('marketCap') or 0) < 5e9 or inf.get('exchange') not in ('NMS', 'NYQ', 'NGM', 'NCM', 'ASE', 'PCX', 'BTS'):
            continue
        name = (inf.get('shortName') or inf.get('longName') or s).replace(', Inc.', '').replace(' Inc.', '').replace(' Corporation', '').replace(' Corp.', '').strip()
        r = dict(tk=s, yahoo=s, name=name, cat='stock')
        mk.append(r)
        have.add(s)
        added.append(s)
    if added:
        log(f"  hot stocks added: {added}")
        with open(MARKETS, 'w', encoding='utf-8') as f:
            f.write('[\n' + ',\n'.join(json.dumps(x, ensure_ascii=False, indent=0) for x in mk) + '\n]\n')
    return added


def main():
    quick = '--quick' in sys.argv
    now = datetime.now(timezone.utc)
    pinned = json.load(open(PINNED, encoding='utf-8'))
    old = {}
    if os.path.exists(OUT):
        old = json.load(open(OUT, encoding='utf-8')).get('assets', {})
    assets = {}

    # 1) curated assets via Yahoo
    log('Yahoo: curated assets')
    yt = {a['yahoo']: a for a in pinned}
    ym = yahoo_monthly(list(yt))
    for a in pinned:
        s = ym.get(a['yahoo'])
        assets[a['id']] = dict(name=a['name'], tk=a['tk'], cat=a['cat'], yahoo=a['yahoo'], src='yahoo', **(s or {}))

    # 2) S&P 500 via Yahoo
    if not quick:
        lst = sp500()
        log(f"S&P 500 list: {len(lst)}")
        taken = {a['tk'] for a in pinned}
        todo = [r for r in lst if r['tk'] not in taken]
        ysym = {r['tk'].replace('.', '-'): r for r in todo}
        sm = yahoo_monthly(list(ysym))
        for y, r in ysym.items():
            aid = r['tk'].lower().replace('.', '-')
            assets[aid] = dict(name={'uk': r['name'], 'en': r['name']}, tk=r['tk'], cat='stock', sector=r['sector'],
                               sp500=True, yahoo=y, src='yahoo', **(sm.get(y) or {}))
        for a in pinned:
            if a['cat'] == 'stock' and any(r['tk'] == a['tk'] for r in lst):
                assets[a['id']]['sp500'] = True
                assets[a['id']]['sector'] = next(r['sector'] for r in lst if r['tk'] == a['tk'])

    # 2b) ETFs and national stocks (data/markets.json), prices converted to USD
    fxm = {}
    if not quick and os.path.exists(MARKETS):
        mk = json.load(open(MARKETS, encoding='utf-8'))
        hot_stocks(mk, {r['yahoo'] for r in mk} | {a.get('yahoo') for a in old.values() if isinstance(a, dict)} | {a.get('yahoo') for a in assets.values()})
        fxm = yahoo_monthly(list(FX_TICKER.values()))
        log(f"markets.json: {len(mk)} assets; fx series: {sorted(fxm)}")
        mm = yahoo_monthly([r['yahoo'] for r in mk if not r['yahoo'].startswith('MOEX:')])
        if 'RUB=X' not in fxm and any(r['yahoo'].startswith('MOEX:') for r in mk):
            rf = rub_fx_fallback()
            if rf:
                fxm['RUB=X'] = rf
        for r in mk:
            if r['yahoo'].startswith('MOEX:'):
                mm[r['yahoo']] = moex_monthly(r['tk'])
                time.sleep(0.3)
        for r in mk:
            ccy = next((c for suf, c in SUFFIX_CCY.items() if r['yahoo'].endswith(suf) or r['yahoo'].startswith(suf)), 'USD')
            base = slug(r['name'].split(' (')[0]) if r['tk'][:1].isdigit() else r['tk'].lower().replace('.', '-').replace('&', '')
            aid = r.get('id') or base   # explicit id in markets.json wins (e.g. spacex, anthropic: their tickers clash with crypto ids)
            if aid in assets or (aid in old and old[aid].get('yahoo') != r['yahoo'] and not r.get('id')):
                aid = f"{base}-{r.get('mkt') or 'etf'}"
            if aid in assets:
                continue
            raw = mm.get(r['yahoo'])
            ser = to_usd(fix_x100(raw) if ccy in CENT else raw, ccy, fxm)
            if ser and broken(ser):
                ser = trim_breaks(ser)
                log(f"  {r['yahoo']}: jump in history, kept from {ser['start'] if ser else '-'}")
                if not ser:
                    continue
            assets[aid] = dict(name={'uk': r['name'], 'en': r['name']}, tk=r['tk'], cat=r['cat'], yahoo=r['yahoo'], src='moex' if ccy == 'RUB' else 'yahoo', ccy=ccy,
                               **{k: r[k] for k in ('mkt', 'sector') if r.get(k)}, **(ser or {}))

    # 3) daily price/24h change for every Yahoo asset (local currency -> USD)
    ys = [a['yahoo'] for a in assets.values() if not a['yahoo'].startswith('MOEX:')] + list(FX_TICKER.values()) + list(CMDTY_T.values())
    yd = yahoo_daily(ys)
    mx = [a['tk'] for a in assets.values() if a['yahoo'].startswith('MOEX:')]
    if mx:
        yd.update({'MOEX:' + k: v for k, v in moex_last(mx).items()})
        if 'RUB=X' not in yd and fxm.get('RUB=X'):
            yd['RUB=X'] = (fxm['RUB=X']['p'][-1], 0)
    CMDTY.update({k: round(yd[t][0], 4) for k, t in CMDTY_T.items() if t in yd})
    for a in assets.values():
        if a['yahoo'] in yd:
            a['price'], a['chg'] = yd[a['yahoo']]
            if a['yahoo'] in YW:
                a['c7'], a['s7'] = YW[a['yahoo']]
            ccy = a.get('ccy', 'USD')
            if ccy != 'USD':
                rate = (yd.get(FX_TICKER[CENT.get(ccy, ccy)]) or [None])[0] or (fxm.get(FX_TICKER[CENT.get(ccy, ccy)], {}).get('p') or [None])[-1]
                a['lp'] = a['price']
                a['price'] = a['price'] / (100.0 if ccy in CENT else 1.0) / rate if rate else None

    # 4) crypto via Binance (+ CoinGecko names/logos)
    cg = coingecko_meta()
    try:   # stablecoins are not assets, but people convert them (USDT → UAH): keep their live price for the converter
        sb = {k: dict(name=cg[k]['name'], price=cg[k]['price'], chg=cg[k].get('chg'), logo=cg[k].get('logo'), mcap=cg[k].get('mcap'), cgid=cg[k].get('cgid'))
              for k in ('USDT', 'USDC', 'DAI', 'USDE', 'FDUSD', 'PYUSD') if k in cg and cg[k].get('price')}
        # every big stablecoin + gold-backed tokens, for the crypto table (CoinMarketCap order: USDT is #3)
        for k in CG_LIST[:400]:
            m = cg.get(k) or {}
            pr, mc = m.get('price') or 0, m.get('mcap') or 0
            gold = k in ('PAXG', 'XAUT')
            if k not in sb and mc >= 3e8 and (gold or ((k in STABLE or 'USD' in k) and 0.97 < pr < 1.03)):
                sb[k] = dict(name=m['name'], price=pr, chg=m.get('chg'), logo=m.get('logo'), mcap=mc, cgid=m.get('cgid'))
        for k, v in sb.items():
            m = cg.get(k) or {}
            v.update({f: m[f] for f in ('rank', 'vol', 'c7', 's7', 'circ') if m.get(f) is not None}, **({'gold': 1} if k in ('PAXG', 'XAUT') else {}))
        if sb:
            json.dump({'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 's': sb}, open(os.path.join(ROOT, 'data/stables.json'), 'w', encoding='utf-8'),
                      ensure_ascii=False, separators=(',', ':'))
    except Exception as e:
        log(f"stables failed: {e}")
    top = binance_top()
    log(f"Binance USDT pairs: {len(top)}")
    pinned_crypto = {a['tk']: a['id'] for a in pinned if a['cat'] == 'crypto'}
    stock_tk = {a['tk'] for a in assets.values() if a['cat'] in ('stock', 'etf')} | {'DRAM', 'MSTR', 'CRCL', 'SPCX', 'SOXL', 'SOXS', 'TQQQ', 'COIN', 'HOOD', 'KORU', 'BNC', 'BMNR', 'SKHY', 'SNXX', 'SNDK', 'QQQ', 'SPY', 'CRWV', 'PLTR'}
    bmap = {r['base']: r for r in top}
    order = CG_LIST or [r['base'] for r in top]          # by market cap; Binance volume if CoinGecko failed
    if not quick:
        order = order + exchange_extras(cg, set(order))     # coins traded on the big exchanges but outside the top-1000 list
    log(f"crypto candidates: {len(order)}")
    n, other = 0, 0
    try:
        nohist = json.load(open(NOHIST, encoding='utf-8'))
    except Exception:
        nohist = {}
    today = now.strftime('%Y-%m-%d')
    nohist = {k: v for k, v in nohist.items() if (datetime.strptime(today, '%Y-%m-%d') - datetime.strptime(v, '%Y-%m-%d')).days < 7}
    new_left, cg_left = NEW_HIST_BUDGET, CG_HIST_BUDGET
    for base in order:
        if n >= (20 if quick else TOP_CRYPTO):
            break
        m, r = cg.get(base, {}), bmap.get(base)
        low = (m.get('name') or base).lower()
        if base not in pinned_crypto:                 # pinned coins (BTC, ETH, BNB...) are never filtered: BNB looked like «BN» stock + B
            if base in STABLE or not base.isalnum() or any(w in low for w in WRAPPED + ('xstock',)):
                continue
            if ('USD' in base) or (base.endswith('B') and base[:-1] in stock_tk):
                continue                                # yield stablecoins and Binance tokenized stocks (NVDAB...)
        if base in pinned_crypto:                      # long Yahoo history already; take live price + logo
            a = assets[pinned_crypto[base]]
            if r:
                a['price'], a['chg'], a['binance'] = r['price'], r['chg'], r['symbol']
            a.update({k: m[k] for k in ('logo', 'rank') + INFO_KEYS if m.get(k)})
            s = binance_monthly(r['symbol']) if r else None   # use Binance if Yahoo failed or has a shorter history
            if s and ('p' not in a or s['start'] < a['start']):
                a.update(s, src='binance')
            continue
        prev = old.get(base.lower()) or old.get(base.lower() + '-token') or {}
        if CRYPTO_FROZEN and not quick and prev.get('tk') != base:
            continue                                      # frozen: no new coins
        if r:
            s, src = binance_monthly(r['symbol']), 'binance'
        elif quick:
            continue
        elif prev.get('tk') == base and prev.get('src') in ('gate', 'mexc', 'okx', 'kraken', 'yahoo-cc', 'bybit', 'coingecko') and extend_old(prev, m.get('price'), now):
            s, src = extend_old(prev, m.get('price'), now), prev['src']    # history already stored
        else:
            # owner 2026-11-21: every top-4000 coin gets a page; without any price history it starts as «spot only» (today's price,
            # live chart from TradingView, no DCA numbers yet) and keeps adding a month each run while we retry the history weekly
            spot = lambda: (to_series([(now.strftime('%Y-%m'), m['price'])]), 'cg-spot') if m.get('price') and (m.get('vol') or 0) >= 1e4 else (None, None)
            if (m.get('vol') or 0) < 1e4:
                continue                                  # dead volume
            if base in nohist or new_left <= 0:            # recently failed, or this run's budget is spent
                if prev.get('tk') == base and prev.get('src') == 'cg-spot' and extend_old(prev, m.get('price'), now):
                    s, src = extend_old(prev, m['price'], now), 'cg-spot'
                elif base in nohist:
                    s, src = spot()
                else:
                    continue
            else:
                new_left -= 1
                s, src = other_monthly(base)
                time.sleep(0.12)
                if not s and cg_left > 0 and m.get('cgid'):
                    cg_left -= 1
                    s, src = coingecko_monthly(m['cgid']), 'coingecko'
                    time.sleep(4)
                if not s:
                    nohist[base] = today
                    s, src = (extend_old(prev, m.get('price'), now), 'cg-spot') if prev.get('src') == 'cg-spot' and prev.get('tk') == base else spot()
        if not s or (len(s['p']) >= 3 and looks_stable(s)) or broken(s):
            continue
        if not r and m.get('price') and not (m['price'] / 3 < s['p'][-1] < m['price'] * 3):
            continue                                    # same ticker, different coin on that exchange
        aid = base.lower()
        if aid in assets:
            aid += '-token'
        nm = m.get('name') or base
        assets[aid] = dict(name={'uk': nm, 'en': nm}, tk=base, cat='crypto', src=src,
                           price=r['price'] if r else m.get('price'), chg=r['chg'] if r else m.get('chg'),
                           logo=m.get('logo'), rank=m.get('rank'), **({'binance': r['symbol']} if r else {}),
                           **{k: m[k] for k in INFO_KEYS if m.get(k)}, **s)
        n += 1
        other += not r
    log(f"crypto: {n} coins ({other} with history from Gate/MEXC/OKX/Bybit/CoinGecko); new-coin budget left {new_left}, CoinGecko history left {cg_left}, no history {len(nohist)}")
    if not quick:
        json.dump(nohist, open(NOHIST, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)

    # 5) keep yesterday's data for anything that failed today; drop empties
    final, kept, dropped = {}, 0, 0
    for aid, a in assets.items():
        if 'p' not in a and aid in old and 'p' in old[aid]:
            a.update({k: old[aid][k] for k in ('start', 'end', 'p', 'price', 'chg') if k in old[aid]})
            kept += 1
        if 'p' not in a:
            dropped += 1
            continue
        a.setdefault('price', a['p'][-1])
        a['price'] = float(f"{a['price']:.6g}")
        if a.get('chg') is not None:
            a['chg'] = round(a['chg'], 5)
        a.setdefault('chg', None)
        a = {k: v for k, v in a.items() if v is not None}
        if a.get('cat') == 'crypto':
            a['seen'] = now.strftime('%Y-%m-%d')
        final[aid] = a
    from datetime import timedelta
    stale = (now - timedelta(days=10)).strftime('%Y-%m-%d')
    for aid, a in old.items():                       # an asset that vanished from today's lists entirely
        if aid in final or quick:
            continue
        # crypto lists depend on CoinGecko paging, which is often rate-limited (429): keep a coin for 10 days
        # after it was last seen, so one bad run does not delete hundreds of pages
        if a.get('cat') != 'crypto' or a.get('seen', now.strftime('%Y-%m-%d')) >= stale:
            final[aid] = a
            kept += 1
    try:
        fx = fx_rates()
        if fx:
            json.dump({'updated': now.strftime('%Y-%m-%d'), 'source': 'open.er-api.com', 'rates': fx},
                      open(os.path.join(ROOT, 'data/fx.json'), 'w'), separators=(',', ':'))
            log(f"fx: {len(fx)} currencies")
    except Exception as e:
        log(f"fx failed: {e}")
    if not quick:
        for f in (coin_info, stock_info):
            try:
                f(final)
            except Exception as e:
                log(f"{f.__name__} failed: {e}")
    try:
        fetch_logos(final)
    except Exception as e:
        log(f"logos failed: {e}")

    try:
        cpi = inflation()
        cp = os.path.join(ROOT, 'data/cpi.json')
        if cpi and os.path.exists(cp):                      # keep countries that failed today
            cpi = {**json.load(open(cp)).get('c', {}), **cpi}
        if cpi:
            json.dump({'updated': now.strftime('%Y-%m-%d'), 'source': 'World Bank FP.CPI.TOTL.ZG', 'c': cpi},
                      open(os.path.join(ROOT, 'data/cpi.json'), 'w'), separators=(',', ':'))
            log(f"cpi: {len(cpi)} countries")
    except Exception as e:
        log(f"cpi failed: {e}")
    try:
        g = market_global(cg)
        if BUBLIST:
            g['bub'] = BUBLIST
        if CMDTY:
            g['cmdty'] = CMDTY
        gp = os.path.join(ROOT, 'data/global.json')
        if g:
            old_g = json.load(open(gp)) if os.path.exists(gp) else {}
            old_g.update({k: v for k, v in g.items() if v is not None})
            old_g['updated'] = now.strftime('%Y-%m-%d %H:%M UTC')
            json.dump(old_g, open(gp, 'w'), separators=(',', ':'))
            log(f"global: {sorted(g)}")
    except Exception as e:
        log(f"global widgets failed: {e}")
    if len(final) < 0.5 * max(1, len(old)):
        log(f"Only {len(final)} assets vs {len(old)} before; refusing to overwrite.")
        return 1
    json.dump({'updated': now.strftime('%Y-%m-%d'), 'assets': final}, open(OUT, 'w', encoding='utf-8'),
              ensure_ascii=False, separators=(',', ':'))
    cats = {}
    for a in final.values():
        cats[a['cat']] = cats.get(a['cat'], 0) + 1
    log(f"Saved {len(final)} assets {cats}; kept old for {kept}, dropped {dropped}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
