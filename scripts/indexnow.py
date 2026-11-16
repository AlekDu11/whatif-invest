"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) which pages changed. Google does not use IndexNow; it reads the sitemap."""
import json, os, subprocess, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = open(os.path.join(ROOT, 'src', 'indexnow.txt')).read().strip()
SITE = 'https://whatifstack.com'
changed = subprocess.run(['git', 'diff', '--name-only', 'HEAD^', 'HEAD'], capture_output=True, text=True, cwd=ROOT).stdout.split()
urls = {SITE + '/', SITE + '/en/', SITE + '/world-assets/', SITE + '/en/world-assets/', SITE + '/news/', SITE + '/en/news/'}
for f in changed:
    parts = f.split('/')
    if len(parts) == 4 and parts[0] == 'content' and f.endswith('.md'):     # content/<blog|news>/<lang>/<slug>.md
        kind, lang, slug = parts[1], parts[2], parts[3][:-3]
        urls.add(f"{SITE}{'' if lang == 'uk' else '/' + lang}/{kind}/{slug}/")
body = json.dumps({'host': 'whatifstack.com', 'key': KEY, 'keyLocation': f'{SITE}/{KEY}.txt', 'urlList': sorted(urls)[:10000]}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print('IndexNow', r.status, len(urls), 'urls')
except Exception as e:
    print('IndexNow failed:', e)
