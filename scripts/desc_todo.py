#!/usr/bin/env python3
"""List assets that still need a short localized description in data/desc/<lang>.json.

Usage: python3 scripts/desc_todo.py <lang> [N]   -> JSON list [{id, name, ticker, cat, sector, industry, country, source}]
       python3 scripts/desc_todo.py all [N]      -> the next N assets missing in ANY of the 20 languages, each with
                                                    `missing` (languages to write) and `have` ({lang: existing text}, reuse its facts)
Order: biggest first (crypto by rank, stocks by market cap), metals/commodities/ETFs early.
`source` is the English text from data/stockinfo.json / data/coininfo.json (may be empty: then write from general knowledge,
facts only, no numbers that change).
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lang = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 120
LANGS = ['en', 'uk', 'ru', 'es', 'de', 'pt', 'pl', 'tr', 'fr', 'it', 'nl', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar', 'fil']
A = json.load(open(os.path.join(ROOT, 'data', 'market.json')))['assets']
# stablecoins + gold tokens have their own pages (/<ticker>/) but are not market.json assets: queue them first
try:
    for _tk, _v in (json.load(open(os.path.join(ROOT, 'data', 'stables.json'))).get('s') or {}).items():
        if _tk.lower() not in A and _v.get('price'):
            A[_tk.lower()] = dict(name=_v.get('name'), tk=_tk, cat='stable', p=[1], cgid=_v.get('cgid'), gold=_v.get('gold'))
except Exception:
    pass
SI = json.load(open(os.path.join(ROOT, 'data', 'stockinfo.json')))
CI = json.load(open(os.path.join(ROOT, 'data', 'coininfo.json')))
def load(lg):
    p = os.path.join(ROOT, 'data', 'desc', lg + '.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


D = {lg: load(lg) for lg in LANGS} if lang == 'all' else {lang: load(lang)}
done = {} if lang == 'all' else D[lang]


def score(k, a):
    if a['cat'] == 'stable':
        return 1e16
    if a['cat'] in ('metal', 'cmd', 'etf'):
        return 1e15
    if a['cat'] == 'crypto':
        return 1e14 / (a.get('rank') or 5000)
    mc = (SI.get(a.get('yahoo') or '', {}) or {}).get('mcap') or 1
    if a.get('lp') and a.get('price'):   # local-currency market cap -> USD
        mc *= a['price'] / a['lp']
    return mc


def has_source(a):
    si = SI.get(a.get('yahoo') or '', {}) or {}
    ci = CI.get(a.get('cgid') or '', {}) or {}
    return bool(((si.get('ds') or ci.get('ds') or {}).get('en') or '').strip())


def key(kv):
    # owner 2026-11-23: obscure coins with no source text kept blocking the head of the queue every run — they go to the
    # end until data/coininfo.json gets their CoinGecko text (top-300 coins stay: they can be described from general knowledge)
    k, a = kv
    blocked = a['cat'] == 'crypto' and (a.get('rank') or 9999) > 300 and not has_source(a)
    return (blocked, -score(k, a))


out = []
for k, a in sorted(A.items(), key=key):
    if k in done or not a.get('p'):
        continue
    miss = [lg for lg in D if k not in D[lg]]
    if not miss:
        continue
    si = SI.get(a.get('yahoo') or '', {}) or {}
    ci = CI.get(a.get('cgid') or '', {}) or {}
    name = a.get('name')
    name = name.get('en') if isinstance(name, dict) else name
    out.append(dict(id=k, name=name, ticker=a['tk'], cat=a['cat'], sector=si.get('sec') or a.get('sector'), industry=si.get('ind'),
                    country=si.get('cty'), source=((si.get('ds') or ci.get('ds') or {}).get('en') or '')[:900]))
    if lang == 'all':
        out[-1].update(missing=miss, have={lg: D[lg][k] for lg in ('en', 'uk', 'ru') if k in D[lg]})
    if len(out) >= n:
        break
print(json.dumps(out, ensure_ascii=False, indent=1))
if lang == 'all':
    full = sum(1 for k, a in A.items() if a.get('p') and all(k in D[lg] for lg in LANGS))
    print(f'# {full} assets complete in all 20 languages, ' + ', '.join(f'{lg} {len(D[lg])}' for lg in LANGS) + f'; showing {len(out)} next', file=sys.stderr)
else:
    print(f'# {len(done)} done in {lang}, showing {len(out)} next', file=sys.stderr)
