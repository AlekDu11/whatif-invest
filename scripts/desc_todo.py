#!/usr/bin/env python3
"""List assets that still need a short localized description in data/desc/<lang>.json.

Usage: python3 scripts/desc_todo.py <lang> [N]   -> JSON list [{id, name, ticker, cat, sector, industry, country, source}]
Order: biggest first (crypto by rank, stocks by market cap), metals/commodities/ETFs early.
`source` is the English text from data/stockinfo.json / data/coininfo.json (may be empty: then write from general knowledge,
facts only, no numbers that change).
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lang = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 120
A = json.load(open(os.path.join(ROOT, 'data', 'market.json')))['assets']
SI = json.load(open(os.path.join(ROOT, 'data', 'stockinfo.json')))
CI = json.load(open(os.path.join(ROOT, 'data', 'coininfo.json')))
p = os.path.join(ROOT, 'data', 'desc', lang + '.json')
done = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def score(k, a):
    if a['cat'] in ('metal', 'cmd', 'etf'):
        return 1e15
    if a['cat'] == 'crypto':
        return 1e14 / (a.get('rank') or 5000)
    return (SI.get(a.get('yahoo') or '', {}) or {}).get('mcap') or 1


out = []
for k, a in sorted(A.items(), key=lambda kv: -score(*kv)):
    if k in done or not a.get('p'):
        continue
    si = SI.get(a.get('yahoo') or '', {}) or {}
    ci = CI.get(a.get('cgid') or '', {}) or {}
    name = a.get('name')
    name = name.get('en') if isinstance(name, dict) else name
    out.append(dict(id=k, name=name, ticker=a['tk'], cat=a['cat'], sector=si.get('sec') or a.get('sector'), industry=si.get('ind'),
                    country=si.get('cty'), source=((si.get('ds') or ci.get('ds') or {}).get('en') or '')[:900]))
    if len(out) >= n:
        break
print(json.dumps(out, ensure_ascii=False, indent=1))
print(f'# {len(done)} done in {lang}, showing {len(out)} next', file=sys.stderr)
