"""Which TradingView symbols really exist (owner 2026-11-22: «only real charts — never someone else's»).
The free TradingView widget shows Apple when a symbol is unknown, so every asset's tv_symbol() is checked against
TradingView's public symbol search and the result kept in data/tv_ok.json ({symbol: [ok 0/1, checked YYYY-MM-DD]}).
build.py draws our own chart (exchange / Yahoo data) for symbols that are not confirmed. Re-checks entries older than 30 days.
Usage: python3 scripts/tv_check.py [max_requests]   (GitHub Actions: workflow tv-check.yml)"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'tv_ok.json')
H = {'Origin': 'https://www.tradingview.com', 'Referer': 'https://www.tradingview.com/', 'User-Agent': 'Mozilla/5.0 (WhatIfStack tv-check)'}


def exists(sym):
    ex, tk = sym.split(':', 1)
    q = urllib.parse.urlencode({'text': tk, 'exchange': ex, 'hl': '0', 'lang': 'en', 'domain': 'production'})
    req = urllib.request.Request('https://symbol-search.tradingview.com/symbol_search/v3/?' + q, headers=H)
    with urllib.request.urlopen(req, timeout=20) as r:
        j = json.loads(r.read())
    for s in j.get('symbols', []):
        name = (s.get('symbol') or '').replace('<em>', '').replace('</em>', '')
        if name.upper() == tk.upper() and (s.get('exchange') or '').upper() == ex.upper() or (s.get('prefix') or '').upper() == ex.upper() and name.upper() == tk.upper():
            return 1
    return 0


def main():
    if os.environ.get('TV_TEST'):   # TV_TEST="GATEIO:DIGIUSDT BINANCE:BTCUSDT" → print the verdicts only
        for s in os.environ['TV_TEST'].split():
            print('TEST', s, exists(s))
        return
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    db = json.load(open(OUT)) if os.path.exists(OUT) else {}
    today = time.strftime('%Y-%m-%d')
    old = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 30 * 86400))
    syms = sorted({s for a in build.A.values() for s in [build.tv_symbol(a)] if s and ':' in s and not s.startswith(('CG:', 'GT:'))})
    todo = [s for s in syms if s not in db or db[s][1] < old]
    print(f'{len(syms)} symbols, {len(todo)} to check, budget {budget}')
    n = bad = 0
    for s in todo[:budget]:
        try:
            ok = exists(s)
        except Exception as e:
            print('skip', s, type(e).__name__)
            time.sleep(3)
            continue
        db[s] = [ok, today]
        n += 1
        bad += not ok
        if not ok and bad <= 60:
            print('  not on TradingView:', s)
        time.sleep(0.35)
    json.dump(dict(sorted(db.items())), open(OUT, 'w'), separators=(',', ':'))
    print(f'checked {n}, not found {bad}; file has {len(db)} symbols, {sum(1 for v in db.values() if not v[0])} not found')


if __name__ == '__main__':
    main()
