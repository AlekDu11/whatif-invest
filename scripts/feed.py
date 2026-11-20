#!/usr/bin/env python3
"""Fresh posts between deploys (owner, 2026-11-20: the site deploys once a day, news must not wait).

Writes data/feed/<lang>.json with the news briefs and blog posts of the last 4 days, already rendered to HTML by
build.py's own markdown + shortcodes (numbers from today's data). The site's JS loads these files from GitHub raw:
new items appear in /news/ and /blog/ right away and open in /<lang>/read/?k=news&s=<slug> until the next deploy
builds their real pages. Run by .github/workflows/feed.yml on every push that touches content/news or content/blog.
"""
import datetime as dt
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build as B  # noqa: E402  (loads the data; the site is not built on import)

DAYS = 4
cut = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=DAYS)).strftime('%Y-%m-%d')
RAW = 'https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/content/covers'
out_dir = os.path.join(ROOT, 'data', 'feed')
os.makedirs(out_dir, exist_ok=True)
langs = set(B.POSTS) | set(B.NEWS)
for lang in sorted(langs):
    if lang not in B.TR:
        continue
    items = []
    for kind, src in (('news', B.NEWS), ('blog', B.POSTS)):
        for slug, m in (src.get(lang) or {}).items():
            d = (m.get('date') or '')[:16]
            if d[:10] < cut:
                continue
            cv = None
            for lg in (lang, 'en'):
                if os.path.exists(os.path.join(ROOT, 'content', 'covers', kind, lg, slug + '.jpg')):
                    cv = f'{RAW}/{kind}/{lg}/{slug}.jpg'
                    break
            try:
                html = B.md(m['body'], lang)
            except Exception as e:   # one bad post must not stop the feed
                print(f'  {lang}/{kind}/{slug}: {e}', file=sys.stderr)
                continue
            items.append(dict(k=kind, s=slug, t=B.post_meta_title(m, lang), d=d, c=m.get('category', ''),
                              g=[x.strip() for x in (m.get('tags') or '').split(',') if x.strip()],
                              x=B.post_meta_title(dict(title=m.get('description', '')), lang), cv=cv, h=html))
    items.sort(key=lambda r: r['d'], reverse=True)
    items = items[:40]
    # small index for the lists + one HTML file per item for the reader (only the last DAYS days are kept)
    hd = os.path.join(out_dir, lang)
    os.makedirs(hd, exist_ok=True)
    keep = set()
    for r in items:
        fn = f'{r["k"]}-{r["s"]}.html'
        keep.add(fn)
        open(os.path.join(hd, fn), 'w', encoding='utf-8').write(r.pop('h'))
    for fn in os.listdir(hd):
        if fn not in keep:
            os.remove(os.path.join(hd, fn))
    json.dump({'u': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M'), 'items': items},
              open(os.path.join(out_dir, lang + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(f'{lang}: {len(items)} items')
