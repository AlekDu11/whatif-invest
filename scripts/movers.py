#!/usr/bin/env python3
"""List today's big movers for the "What's happening with X" rubric.
Usage: python3 scripts/movers.py [min_abs_pct=12] [max_rank=200]
Prints movers from data/market.json and whether we already wrote a brief on them in the last 3 days."""
import json, os, sys, datetime as dt, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lim = float(sys.argv[1]) if len(sys.argv) > 1 else 12
mr = int(sys.argv[2]) if len(sys.argv) > 2 else 200
A = json.load(open(os.path.join(ROOT, 'data', 'market.json')))['assets']
since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=3)).strftime('%Y-%m-%d')
recent = set()
nd = os.path.join(ROOT, 'content', 'news', 'en')
for f in os.listdir(nd) if os.path.isdir(nd) else []:
    t = open(os.path.join(nd, f)).read()
    d = re.search(r'^date:\s*(\S+)', t, re.M); a = re.search(r'^assets:\s*(.+)$', t, re.M)
    if d and a and d.group(1) >= since and 'movers' in t.split('---')[1]:
        recent |= {x.strip() for x in a.group(1).split(',')}
rows = []
for aid, a in A.items():
    c = a.get('chg')
    if c is None: continue
    stock = a['cat'] in ('stock', 'etf')
    if (a['cat'] == 'crypto' and (a.get('rank') or 999) <= mr and abs(c) * 100 >= lim) or (stock and abs(c) * 100 >= lim * 0.6):
        rows.append((abs(c), aid, a['tk'], a['cat'], c, a.get('rank'), aid in recent))
for _, aid, tk, cat, c, rk, done in sorted(rows, reverse=True)[:15]:
    print(f"{aid:14} {tk:8} {cat:6} {c*100:+6.1f}%  rank={rk}  {'ALREADY COVERED' if done else ''}")
if not rows:
    print('no movers above threshold')
