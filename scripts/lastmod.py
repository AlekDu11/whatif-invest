#!/usr/bin/env python3
"""Real «last changed» dates for asset pages, for the sitemaps (owner 2026-11-24).

Google ignores <lastmod> when every URL says «today», so it never knew which pages we had just filled.
This keeps data/lastmod.json = {"<lang>|<asset id>": [signature, "YYYY-MM-DD"]}: the signature is a hash of the
page's own text (the short description + the profile/analysis file). When the text changes, the date becomes today;
otherwise it stays. Runs in the daily data workflow (update-prices.yml) right before the data commit; build.py reads it.
stdlib only.
"""
import hashlib
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'lastmod.json')


def main():
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    desc_dir, prof_dir = os.path.join(ROOT, 'data', 'desc'), os.path.join(ROOT, 'content', 'profiles')
    langs = sorted(f[:-5] for f in os.listdir(desc_dir) if f.endswith('.json'))
    new, changed = {}, 0
    for lang in langs:
        desc = json.load(open(os.path.join(desc_dir, lang + '.json'), encoding='utf-8'))
        pdir = os.path.join(prof_dir, lang)
        profs = {f[:-3] for f in os.listdir(pdir) if f.endswith('.md')} if os.path.isdir(pdir) else set()
        for aid in set(desc) | profs:
            txt = desc.get(aid, '')
            if aid in profs:
                txt += '\n' + open(os.path.join(pdir, aid + '.md'), encoding='utf-8').read()
            sig = hashlib.sha1(txt.encode('utf-8')).hexdigest()[:10]
            k = f'{lang}|{aid}'
            if k in old and old[k][0] == sig:
                new[k] = old[k]
            else:
                new[k] = [sig, today]
                changed += 1
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(new, f, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
        f.write('\n')
    print(f'lastmod: {len(new)} pages, {changed} changed today')


if __name__ == '__main__':
    main()
