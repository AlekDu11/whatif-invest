"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) which pages changed. Google does not use IndexNow; it reads the sitemap."""
import json, os, re, subprocess, sys, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = open(os.path.join(ROOT, 'src', 'indexnow.txt')).read().strip()
SITE = 'https://whatifstack.com'
changed = subprocess.run(['git', 'diff', '--name-only', 'HEAD^', 'HEAD'], capture_output=True, text=True, cwd=ROOT).stdout.split()
urls = {SITE + '/', SITE + '/en/', SITE + '/world-assets/', SITE + '/en/world-assets/', SITE + '/news/', SITE + '/en/news/'}
for f in changed:
    parts = f.split('/')
    if len(parts) == 4 and parts[0] == 'content' and f.endswith('.md'):     # content/<blog|news|profiles>/<lang>/<slug>.md
        kind, lang, slug = parts[1], parts[2], parts[3][:-3]
        # profiles/analyses live on the asset page (/<lang>/<asset>/), not under /profiles/ (that URL 404s — growth report 2026-11-23)
        urls.add(f"{SITE}{'' if lang == 'uk' else '/' + lang}/{slug if kind == 'profiles' else kind + '/' + slug}/")
if '--all' in sys.argv:   # one-off: every URL in the live sitemaps (Bing had only 4.7K of ~76K, 2026-11-26)
    get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'WhatIfStack-IndexNow'}), timeout=60).read().decode()
    for sm in re.findall(r'<loc>([^<]+)</loc>', get(SITE + '/sitemap.xml')):
        urls |= set(re.findall(r'<loc>([^<]+)</loc>', get(sm)))
urls = sorted(urls)
for i in range(0, len(urls), 10000):
    body = json.dumps({'host': 'whatifstack.com', 'key': KEY, 'keyLocation': f'{SITE}/{KEY}.txt', 'urlList': urls[i:i + 10000]}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print('IndexNow', r.status, len(urls[i:i + 10000]), 'urls')
    except Exception as e:
        print('IndexNow failed:', e)
