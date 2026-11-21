"""Key statistics for every stock / ETF (Yahoo Finance via yfinance) -> data/stockstats.json.

Rotating refresh: each run takes the stalest tickers first (never fetched, then oldest), within a time budget,
so all ~1,200 stocks are refreshed every few days. Run by .github/workflows/stock-stats.yml.
Fields (short keys, missing ones omitted):
  d date fetched · ccy price currency · fcy financial currency
  web sec ind cty city emp ds{en}   (profile)
  mcap pe fpe eps dy (dividend yield, fraction) dps (dividend per share) pr (payout ratio) beta h52 l52
  rev revg (fraction) gm pm (margins) ni (net income) fcf debt cash
  rec (recommendationKey) tgt (target mean) nan (analyst count) ern (next earnings, unix) exd (ex-dividend, unix)
  sh (shares outstanding) · stocks only: hy [fiscal years] hr [total revenue] hn [net income] (annual income statement, oldest first)
"""
import json, os, sys, time
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/stockstats.json')
MARKET = os.path.join(ROOT, 'data/market.json')
BUDGET = int(os.environ.get('STATS_BUDGET', 40 * 60))
MAXN = int(os.environ.get('STATS_MAX', 600))
T0 = time.time()


def clean(s, n=900):
    s = ' '.join((s or '').split())
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'


def num(v):
    try:
        v = float(v)
        return None if v != v or v in (float('inf'), float('-inf')) else (int(v) if v.is_integer() and abs(v) > 1e6 else round(v, 6))
    except (TypeError, ValueError):
        return None


def pick(i):
    g = i.get
    dy = g('dividendYield')
    if dy is not None and dy > 1:      # yfinance >=0.2.5x reports percent (3.1) instead of fraction (0.031)
        dy = dy / 100
    out = dict(ccy=g('currency'), fcy=g('financialCurrency'), web=g('website'), sec=g('sector'), ind=g('industry'), cty=g('country'),
               city=g('city'), emp=g('fullTimeEmployees'), mcap=num(g('marketCap')), pe=num(g('trailingPE')), fpe=num(g('forwardPE')),
               eps=num(g('trailingEps')), dy=num(dy), dps=num(g('dividendRate')), pr=num(g('payoutRatio')), beta=num(g('beta')),
               h52=num(g('fiftyTwoWeekHigh')), l52=num(g('fiftyTwoWeekLow')), rev=num(g('totalRevenue')), revg=num(g('revenueGrowth')),
               gm=num(g('grossMargins')), pm=num(g('profitMargins')), ni=num(g('netIncomeToCommon')), fcf=num(g('freeCashflow')),
               debt=num(g('totalDebt')), cash=num(g('totalCash')), rec=g('recommendationKey') if g('recommendationKey') not in (None, 'none') else None,
               tgt=num(g('targetMeanPrice')), nan=g('numberOfAnalystOpinions'), ern=g('earningsTimestamp') or g('earningsTimestampStart'),
               exd=g('exDividendDate'), sh=num(g('sharesOutstanding')), d=date.today().isoformat())
    if g('longBusinessSummary'):
        out['ds'] = {'en': clean(g('longBusinessSummary'))}
    return {k: v for k, v in out.items() if v is not None and v != ''}


def history(t):
    """Annual revenue and net income for the last 4-5 fiscal years, oldest first."""
    try:
        df = t.income_stmt
    except Exception:
        return {}
    if df is None or getattr(df, 'empty', True):
        return {}
    row = lambda *names: next((df.loc[n] for n in names if n in df.index), None)
    rv, ni = row('Total Revenue', 'Operating Revenue'), row('Net Income', 'Net Income Common Stockholders')
    ys, hr, hn = [], [], []
    for col in sorted(df.columns):
        r = num(rv[col]) if rv is not None else None
        n_ = num(ni[col]) if ni is not None else None
        if r is None and n_ is None:
            continue
        ys.append(col.year if hasattr(col, 'year') else int(str(col)[:4]))
        hr.append(r)
        hn.append(n_)
    return dict(hy=ys, hr=hr, hn=hn) if len(ys) >= 2 else {}


def moex(sec):
    """Russian stocks are not on Yahoo: key numbers from the Moscow Exchange ISS API (free, no key) — market cap, shares,
    52-week range from weekly candles, dividends of the last 12 months. Revenue/earnings are not in ISS (left empty)."""
    import urllib.request
    def iss(path):
        with urllib.request.urlopen(urllib.request.Request('https://iss.moex.com/iss/' + path, headers={'User-Agent': 'whatifstack.com data bot'}), timeout=30) as r:
            return json.load(r)
    def rows(d, block):
        b = d.get(block) or {}
        return [dict(zip(b.get('columns') or [], r)) for r in b.get('data') or []]
    d = iss(f'engines/stock/markets/shares/boards/TQBR/securities/{sec}.json?iss.meta=off&iss.only=securities,marketdata')
    se, md = (rows(d, 'securities') or [{}])[0], (rows(d, 'marketdata') or [{}])[0]
    price = md.get('LAST') or md.get('LCURRENTPRICE') or se.get('PREVPRICE')
    sh = se.get('ISSUESIZE')
    rec = {'ccy': 'RUB', 'cty': 'Russia', 'd': time.strftime('%Y-%m-%d')}
    if sh:
        rec['sh'] = int(sh)
    cap = md.get('ISSUECAPITALIZATION') or (price * sh if price and sh else None)
    if cap:
        rec['mcap'] = int(cap)
    since = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 366 * 86400))
    c = rows(iss(f'engines/stock/markets/shares/boards/TQBR/securities/{sec}/candles.json?iss.meta=off&interval=7&from={since}'), 'candles')
    if c:
        rec['h52'], rec['l52'] = max(x['high'] for x in c), min(x['low'] for x in c)
    dv = [x for x in rows(iss(f'securities/{sec}/dividends.json?iss.meta=off'), 'dividends')
          if (x.get('registryclosedate') or '') >= since and x.get('currencyid') in (None, 'RUB', 'SUR')]
    if dv and price:
        dps = sum(x.get('value') or 0 for x in dv)
        rec['dps'], rec['dy'] = round(dps, 4), round(dps / price * 100, 2)
    return rec


def main():
    import yfinance as yf
    assets = json.load(open(MARKET, encoding='utf-8'))['assets']
    stats = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    syms = sorted({a['yahoo'] for a in assets.values() if a.get('cat') in ('stock', 'etf') and a.get('yahoo') and ':' not in a['yahoo']})
    is_stock = {a['yahoo'] for a in assets.values() if a.get('cat') == 'stock' and a.get('yahoo')}
    syms.sort(key=lambda s: (stats.get(s, {}).get('d', ''), s))      # never fetched first, then the stalest
    n = fail = 0
    for s in syms[:MAXN]:
        if time.time() - T0 > BUDGET:
            break
        try:
            tk = yf.Ticker(s)
            i = tk.info or {}
        except Exception as e:  # rate limit or unknown symbol: keep the old record
            print(f'  {s}: {str(e)[:80]}', flush=True)
            fail += 1
            if fail > 25:
                break
            time.sleep(5)
            continue
        rec = pick(i)
        if s in is_stock and len(rec) > 2:
            h = history(tk)
            if h:
                rec.update(h)
            elif stats.get(s, {}).get('hy'):        # keep the older history if this fetch had none
                rec.update({k: stats[s][k] for k in ('hy', 'hr', 'hn')})
        if len(rec) > 2:
            stats[s] = rec
            n += 1
        time.sleep(0.5)
        if n % 50 == 0:
            json.dump(stats, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    for s in sorted({a['yahoo'] for a in assets.values() if a.get('cat') == 'stock' and (a.get('yahoo') or '').startswith('MOEX:')}):
        try:
            rec = moex(s.split(':', 1)[1])
            if len(rec) > 3:
                stats[s] = dict(stats.get(s, {}), **rec)
                n += 1
        except Exception as e:
            print(f'  {s}: {str(e)[:80]}', flush=True)
        time.sleep(0.3)
    json.dump(stats, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    print(f'stock stats: updated {n}, failed {fail}, total {len(stats)} of {len(syms)}')


if __name__ == '__main__':
    sys.exit(main())
