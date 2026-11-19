#!/usr/bin/env python3
"""Merge a batch of short asset descriptions into data/desc/<lang>.json.

Usage: python3 scripts/desc_merge.py batch.json
batch.json = {"<asset id>": {"en": "...", "uk": "...", ...}, ...}
Never overwrites an existing text, skips unknown asset ids and unknown languages, prints what was added.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ['en', 'uk', 'ru', 'es', 'de', 'pt', 'pl', 'tr', 'fr', 'it', 'nl', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar', 'fil']
A = json.load(open(os.path.join(ROOT, 'data', 'market.json')))['assets']
B = json.load(open(sys.argv[1], encoding='utf-8'))
added = {}
for lg in LANGS:
    p = os.path.join(ROOT, 'data', 'desc', lg + '.json')
    d = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    n = 0
    for aid, tx in B.items():
        t = (tx or {}).get(lg)
        if aid in A and t and aid not in d:
            d[aid] = ' '.join(str(t).split())
            n += 1
    if n:
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=1, sort_keys=True)
            f.write('\n')
        added[lg] = n
bad = [k for k in B if k not in A]
print('added: ' + (', '.join(f'{k} +{v}' for k, v in added.items()) or 'nothing') + (f'; unknown ids skipped: {bad}' if bad else ''))
