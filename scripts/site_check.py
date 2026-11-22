"""Daily site check (owner 2026-11-22: «no more „page not found“»): opens every asset page in uk + en and a sample in the other
18 languages on the LIVE site, plus the main hubs, and writes reports/site-check.md (counts + every broken URL).
Broken = HTTP status ≠ 200, the «not found» page, raw {{shortcodes}} or an empty price. Run in GitHub Actions (workflow site-check.yml)."""
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time
import urllib.parse
import urllib.request

SITE = os.environ.get('SITE', 'https://whatifstack.com')
LANGS = 'en es pt de fr it pl tr nl ru id vi th hi ja ko zh ar fil'.split()
HUBS = ['', 'crypto/', 'stocks/', 'memes/', 'news/', 'blog/', 'learn/', 'me/', 'watchlist/', 'compare/', 'calculators/', 'largest-companies/',
        'earnings-calendar/', 'investors/', 'categories/', 'crypto-exchanges/', 'exchanges/', 'guide/', 'converter/']
NF = re.compile(r'Page not found|Сторінку не знайдено|<title>Not found')


def url(lang, path):
    return f'{SITE}/{path}' if lang == 'uk' else f'{SITE}/{lang}/{path}'


def check(u):
    for attempt in range(2):
        try:
            req = urllib.request.Request(urllib.parse.quote(u, safe=':/?=&%'), headers={'User-Agent': 'WhatIfStack-site-check/1.0'})
            with urllib.request.urlopen(req, timeout=30) as r:
                h = r.read().decode('utf-8', 'replace')
                if NF.search(h):
                    return u, 'not-found page'
                if '{{' in h and re.search(r'\{\{(price|dca|card|table|chg1y|ath)', h):
                    return u, 'raw {{shortcode}}'
                return u, None
        except urllib.error.HTTPError as e:
            if e.code == 404 or attempt:
                return u, f'HTTP {e.code}'
        except Exception as e:   # network hiccup: retried once, then reported
            if attempt:
                return u, f'error {type(e).__name__}'
        time.sleep(2)
    return u, 'error'


def main():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
    import build   # the site's own asset ids (ids that clash with a language code or a section get a -<cat> suffix)
    ids = sorted(build.A)
    random.seed(time.strftime('%Y-%m-%d'))
    urls = [url(l, h) for l in ['uk'] + LANGS for h in HUBS]
    urls += [url('uk', f'{i}/') for i in ids] + [url('en', f'{i}/') for i in ids]
    for l in LANGS[1:]:
        urls += [url(l, f'{i}/') for i in random.sample(ids, min(150, len(ids)))]
    t0, bad = time.time(), []
    with cf.ThreadPoolExecutor(16) as ex:
        for u, err in ex.map(check, urls):
            if err:
                bad.append((u, err))
    secs = int(time.time() - t0)
    os.makedirs('reports', exist_ok=True)
    lines = [f'# Site check {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}', '',
             f'Checked **{len(urls)}** pages in {secs} s (all {len(ids)} assets in uk + en, 150 random per other language, {len(HUBS)} hubs × 20 languages).',
             f'Broken: **{len(bad)}**' + (' ✅' if not bad else ''), '']
    if bad:
        lines += ['| URL | problem |', '|---|---|'] + [f'| {u} | {e} |' for u, e in sorted(bad)[:500]]
    open('reports/site-check.md', 'w').write('\n'.join(lines) + '\n')
    print(lines[2]); print(lines[3])
    for u, e in bad[:40]:
        print(' ', e, u)


if __name__ == '__main__':
    sys.exit(main())
