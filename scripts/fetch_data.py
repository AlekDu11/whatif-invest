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
import csv, io, json, math, os, sys, time, urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINNED = os.path.join(ROOT, 'data/assets.json')
OUT = os.path.join(ROOT, 'data/market.json')
MIN_START = '2000-01'
TOP_CRYPTO = 200
BINANCE = 'https://data-api.binance.vision/api/v3'
SP500_CSV = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv'
STABLE = set('USDT USDC FDUSD TUSD USDP DAI BUSD EUR EURI AEUR USDE PYUSD XUSD USD1 BFUSD RLUSD UST USTC GBP TRY BRL '
              'AUD JPY RUB UAH ZAR NGN PLN ARS MXN COP CZK IDR VAI SUSD LUSD FRAX GUSD USDS USDD PAXG XAUT WBTC WBETH BETH BNSOL'.split())
UA = {'User-Agent': 'WhatIfStack/1.0 (+https://whatifstack.com/)'}


def log(*a):
    print(*a, flush=True)


def get_json(url, tries=3):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
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


def looks_stable(series):
    p = series['p'][-12:]
    return len(p) >= 3 and all(0.97 < x < 1.03 for x in p)


# ---------------- CoinGecko (names/logos) ----------------
def coingecko_meta():
    meta = {}
    for page in (1, 2):
        d = get_json(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={page}", tries=2)
        if not isinstance(d, list):
            break
        for c in d:
            sym = (c.get('symbol') or '').upper()
            if sym and sym not in meta:          # first = biggest market cap wins
                meta[sym] = dict(name=c.get('name'), logo=c.get('image'), rank=c.get('market_cap_rank'), mcap=c.get('market_cap'))
        time.sleep(3)
    log(f"CoinGecko meta: {len(meta)} coins")
    return meta


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
            df = yf.download(chunk, period='7d', interval='1d', auto_adjust=True, group_by='ticker', threads=True, progress=False)
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

# ---------------- main ----------------
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

    # 3) daily price/24h change for every Yahoo asset
    ys = [a['yahoo'] for a in assets.values()]
    yd = yahoo_daily(ys)
    for a in assets.values():
        if a['yahoo'] in yd:
            a['price'], a['chg'] = yd[a['yahoo']]

    # 4) crypto via Binance (+ CoinGecko names/logos)
    cg = coingecko_meta()
    top = binance_top()
    log(f"Binance USDT pairs: {len(top)}")
    pinned_crypto = {a['tk']: a['id'] for a in pinned if a['cat'] == 'crypto'}
    stock_tk = {a['tk'] for a in assets.values() if a['cat'] in ('stock', 'etf')} | {'DRAM', 'MSTR', 'CRCL', 'SPCX', 'SOXL', 'SOXS', 'TQQQ', 'COIN', 'HOOD', 'KORU', 'BNC', 'BMNR', 'SKHY', 'SNXX', 'SNDK', 'QQQ', 'SPY', 'CRWV', 'PLTR'}
    n = 0
    for r in top:
        if n >= (20 if quick else TOP_CRYPTO):
            break
        base = r['base']
        m = cg.get(base, {})
        if ('USD' in base and not m) or (base.endswith('B') and base[:-1] in stock_tk):
            continue                                    # yield stablecoins and Binance tokenized stocks (NVDAB...)
        if base in pinned_crypto:                      # long Yahoo history already; take live price + logo
            a = assets[pinned_crypto[base]]
            a['price'], a['chg'] = r['price'], r['chg']
            a.update({k: v for k, v in (('logo', m.get('logo')), ('rank', m.get('rank'))) if v})
            s = binance_monthly(r['symbol'])         # use Binance if Yahoo failed or has a shorter history
            if s and ('p' not in a or s['start'] < a['start']):
                a.update(s, src='binance')
            continue
        s = binance_monthly(r['symbol'])
        time.sleep(0.15)
        if not s or looks_stable(s):
            continue
        aid = base.lower()
        if aid in assets:
            aid += '-token'
        nm = m.get('name') or base
        assets[aid] = dict(name={'uk': nm, 'en': nm}, tk=base, cat='crypto', src='binance', binance=r['symbol'],
                           price=r['price'], chg=r['chg'], logo=m.get('logo'), rank=m.get('rank'), **s)
        n += 1

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
        final[aid] = a
    for aid, a in old.items():                       # an asset that vanished from today's lists entirely
        if aid not in final and not quick and a.get('cat') != 'crypto':
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
    try:
        g = market_global(cg)
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
