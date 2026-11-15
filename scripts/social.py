"""Post newly added news briefs and Insights articles to Telegram and X.
Runs in GitHub Actions after a push that adds files under content/news or content/blog.
Secrets (any missing one just skips that channel):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_UK (e.g. @whatifstack_ua), TELEGRAM_CHAT_EN (e.g. @whatifstack)
  X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET  (English posts)
stdlib only."""
import base64, hashlib, hmac, json, os, subprocess, sys, time, urllib.parse, urllib.request, uuid

SITE = 'https://whatifstack.com'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def front(path):
    raw = open(path, encoding='utf-8').read()
    meta = {}
    if raw.startswith('---'):
        head = raw[3:].split('\n---', 1)[0]
        for line in head.strip().splitlines():
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
    return meta


def added_files(before, after):
    rng = [before, after] if before and set(before) != {'0'} else [after + '~1', after]
    out = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=A', *rng, '--', 'content/news', 'content/blog'],
                         capture_output=True, text=True, cwd=ROOT).stdout
    return [f for f in out.split() if f.endswith('.md')]


def page_url(f):
    _, kind, lang, name = f.split('/')
    pre = '' if lang == 'uk' else '/' + lang
    return f'{SITE}{pre}/{kind}/{name[:-3]}/'


def telegram(chat, text):
    tok = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not tok or not chat:
        return
    data = urllib.parse.urlencode({'chat_id': chat, 'text': text, 'parse_mode': 'HTML', 'disable_web_page_preview': 'false'}).encode()
    try:
        urllib.request.urlopen(f'https://api.telegram.org/bot{tok}/sendMessage', data, timeout=20).read()
        print('telegram ok', chat)
    except Exception as e:
        print('telegram failed', chat, e)


def x_post(text):
    k, ks, t, ts = (os.environ.get(n) for n in ('X_API_KEY', 'X_API_SECRET', 'X_ACCESS_TOKEN', 'X_ACCESS_SECRET'))
    if not all((k, ks, t, ts)):
        return
    url = 'https://api.twitter.com/2/tweets'
    oa = {'oauth_consumer_key': k, 'oauth_nonce': uuid.uuid4().hex, 'oauth_signature_method': 'HMAC-SHA1',
          'oauth_timestamp': str(int(time.time())), 'oauth_token': t, 'oauth_version': '1.0'}
    q = lambda s: urllib.parse.quote(str(s), safe='')
    base = '&'.join(['POST', q(url), q('&'.join(f'{q(a)}={q(b)}' for a, b in sorted(oa.items())))])
    oa['oauth_signature'] = base64.b64encode(hmac.new(f'{q(ks)}&{q(ts)}'.encode(), base.encode(), hashlib.sha1).digest()).decode()
    auth = 'OAuth ' + ', '.join(f'{q(a)}="{q(b)}"' for a, b in sorted(oa.items()))
    req = urllib.request.Request(url, json.dumps({'text': text}).encode(), {'Authorization': auth, 'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req, timeout=20).read()
        print('x ok')
    except Exception as e:
        print('x failed', e, getattr(e, 'read', lambda: b'')()[:300])


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def main():
    files = added_files(os.environ.get('BEFORE', ''), os.environ.get('AFTER', 'HEAD'))
    print('new files:', files)
    for f in files[:12]:
        lang = f.split('/')[2]
        if lang not in ('uk', 'en'):
            continue
        m = front(os.path.join(ROOT, f))
        title, desc = m.get('title', ''), m.get('description', '')
        if '{{' in title:          # titles with live shortcodes are rendered on the site only
            title = title.split('{{')[0].strip(' —:-')
        link = page_url(f) + '?utm_source=telegram'
        emoji = '📰' if '/news/' in f else '📊'
        msg = f'{emoji} <b>{esc(title)}</b>\n\n{esc(desc)}\n\n{link}'
        telegram(os.environ.get('TELEGRAM_CHAT_UK' if lang == 'uk' else 'TELEGRAM_CHAT_EN'), msg)
        if lang == 'en':
            tags = ' '.join('#' + t.strip().capitalize() for t in m.get('tags', '').split(',') if t.strip())[:60]
            x_post(f'{title}\n\n{page_url(f)}?utm_source=x {tags}'.strip()[:280])
        time.sleep(3)


if __name__ == '__main__':
    sys.exit(main())
