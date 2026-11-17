"""Key statistics for every stock / ETF (Yahoo Finance via yfinance) -> data/stockstats.json.

Rotating refresh: each run takes the stalest tickers first (never fetched, then oldest), within a time budget,
so all ~1,200 stocks are refreshed every few days. Run by .github/workflows/stock-stats.yml.
Fields (short keys, missing ones omitted):
  d date fetched · ccy price currency · fcy financial currency
  web sec ind cty city emp ds{en}   (profile)
  mcap pe fpe eps dy (dividend yield, fraction) dps (dividend per share) pr (payout ratio) beta h52 l52
  rev revg (fraction) gm pm (margins) ni (net income) fcf debt cash
  rec (recommendationKey) tgt (target mean) nan (analyst count) ern (next earnings, unix) exd (ex-dividend, unix)
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
               exd=g('exDividendDate'), d=date.today().isoformat())
    if g('longBusinessSummary'):
        out['ds'] = {'en': clean(g('longBusinessSummary'))}
    return {k: v for k, v in out.items() if v is not None and v != ''}


def main():
    import yfinance as yf
    assets = json.load(open(MARKET, encoding='utf-8'))['assets']
    stats = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    syms = sorted({a['yahoo'] for a in assets.values() if a.get('cat') in ('stock', 'etf') and a.get('yahoo') and ':' not in a['yahoo']})
    syms.sort(key=lambda s: (stats.get(s, {}).get('d', ''), s))      # never fetched first, then the stalest
    n = fail = 0
    for s in syms[:MAXN]:
        if time.time() - T0 > BUDGET:
            break
        try:
            i = yf.Ticker(s).info or {}
        except Exception as e:  # rate limit or unknown symbol: keep the old record
            print(f'  {s}: {str(e)[:80]}', flush=True)
            fail += 1
            if fail > 25:
                break
            time.sleep(5)
            continue
        rec = pick(i)
        if len(rec) > 2:
            stats[s] = rec
            n += 1
        time.sleep(0.5)
        if n % 50 == 0:
            json.dump(stats, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump(stats, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    print(f'stock stats: updated {n}, failed {fail}, total {len(stats)} of {len(syms)}')


if __name__ == '__main__':
    sys.exit(main())
