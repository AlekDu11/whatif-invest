"""Refresh data/prices.json from Yahoo Finance (monthly closes, split-adjusted).

Runs daily in GitHub Actions. For every asset in data/assets.json it downloads
the full monthly history of its `yahoo` ticker. If a download fails or looks
broken, the asset keeps its previous series, so one bad ticker never breaks
the site.
Run: python3 scripts/update_prices.py
"""
import json, os, sys, time
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'data/assets.json')
PRICES = os.path.join(ROOT, 'data/prices.json')
MIN_START = '2000-01'


def ym2i(s):
    y, m = map(int, s.split('-'))
    return y * 12 + m - 1


def i2ym(i):
    return f"{i // 12}-{i % 12 + 1:02d}"


def to_monthly(points):
    """points: iterable of (YYYY-MM, close). Returns {start, end, p} with every month filled."""
    by_month = {}
    for ym, close in points:
        if close is None or close != close or close <= 0:   # skip None/NaN/zero
            continue
        if ym >= MIN_START:
            by_month[ym] = float(close)                     # later rows in a month win
    if not by_month:
        return None
    months = sorted(by_month)
    s, e = ym2i(months[0]), ym2i(months[-1])
    p, last = [], None
    for i in range(s, e + 1):
        last = by_month.get(i2ym(i), last)                  # forward-fill rare gaps
        p.append(round(last, 8))
    return {'start': months[0], 'end': months[-1], 'p': p}


def fetch(ticker):
    import yfinance as yf
    h = yf.Ticker(ticker).history(period='max', interval='1mo', auto_adjust=True)
    if h is None or h.empty or 'Close' not in h:
        return None
    return to_monthly((ts.strftime('%Y-%m'), c) for ts, c in h['Close'].items())


def looks_ok(new, old, now_ym):
    if not new:
        return False, 'empty'
    if ym2i(now_ym) - ym2i(new['end']) > 1:
        return False, f"stale (ends {new['end']})"
    if old:
        # the last price should not jump wildly against what we already had for the same month
        k = ym2i(old['end']) - ym2i(new['start'])
        if 0 <= k < len(new['p']):
            ratio = new['p'][k] / old['p'][-1]
            if not (0.5 < ratio < 2):
                return False, f"price mismatch x{ratio:.2f}"
    return True, ''


def main():
    assets = json.load(open(ASSETS, encoding='utf-8'))
    data = json.load(open(PRICES, encoding='utf-8')) if os.path.exists(PRICES) else {'assets': {}}
    old = data.get('assets', {})
    now = datetime.now(timezone.utc)
    now_ym = now.strftime('%Y-%m')
    out, report = {}, []
    for a in assets:
        aid, tk = a['id'], a['yahoo']
        new = None
        for attempt in range(3):
            try:
                new = fetch(tk)
                break
            except Exception as e:  # network hiccup, rate limit
                report.append(f"{aid}: attempt {attempt + 1} failed: {e}")
                time.sleep(3 * (attempt + 1))
        ok, why = looks_ok(new, old.get(aid), now_ym)
        if ok:
            out[aid] = new
            report.append(f"{aid}: ok {new['start']}..{new['end']} last={new['p'][-1]}")
        elif aid in old:
            out[aid] = old[aid]
            report.append(f"{aid}: KEPT OLD ({why})")
        else:
            report.append(f"{aid}: SKIPPED ({why})")
    fresh = sum(1 for r in report if ': ok ' in r)
    print('\n'.join(report))
    if fresh == 0:
        print('No asset refreshed; leaving prices.json untouched.', file=sys.stderr)
        return 1
    data = {'updated': now.strftime('%Y-%m-%d'), 'source': 'Yahoo Finance via yfinance', 'assets': out}
    json.dump(data, open(PRICES, 'w', encoding='utf-8'), separators=(',', ':'))
    print(f"updated {fresh}/{len(assets)} assets")
    return 0


if __name__ == '__main__':
    sys.exit(main())
