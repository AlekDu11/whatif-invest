"""Backup poster for the Telegram channel: works without the owner's computer.

Scheduled tasks that normally post through Telegram Web in the owner's browser fall back to this queue when the browser
is unreachable: they commit social/queue/tg/<YYYY-MM-DD-HHMM>-<slug>.json and the workflow tg-queue.yml sends it with
the bot (@WhatIfStack_Bot must be an admin of the channel with «Post messages»).

Item: {"lines": ["text", ["b", "bold line"], "", ...], "photo": "content/covers/x/en/<slug>.jpg" | "video": "content/video/<x>.mp4",
       "at": "2026-11-21T11:41:00Z" (optional, not before), "chat": "@WhatIfStack" (optional)}
Sent items move to social/queue/tg/sent/ with the message id. GitHub secrets: TG_BOT_TOKEN (same token as in Vercel; passed as env TELEGRAM_BOT_TOKEN),
TG_CHANNEL (optional, default @WhatIfStack). Not TELEGRAM_BOT_TOKEN: that name would switch on the old social.yml auto-poster. stdlib only."""
import datetime, glob, html, json, os, sys, urllib.request, uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(ROOT, 'social', 'queue', 'tg')


def caption(lines):
    out = []
    for ln in lines:
        if isinstance(ln, list) and ln and ln[0] == 'b':
            out.append(f'<b>{html.escape(ln[1])}</b>')
        else:
            out.append(html.escape(ln or ''))
    return '\n'.join(out)


def call(token, method, fields, file_field=None, path=None):
    url = f'https://api.telegram.org/bot{token}/{method}'
    if not path:
        req = urllib.request.Request(url, json.dumps(fields).encode(), {'Content-Type': 'application/json'})
    else:
        b = uuid.uuid4().hex
        body = b''
        for k, v in fields.items():
            body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
        body += (f'--{b}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{os.path.basename(path)}"\r\n'
                 f'Content-Type: application/octet-stream\r\n\r\n').encode() + open(path, 'rb').read() + f'\r\n--{b}--\r\n'.encode()
        req = urllib.request.Request(url, body, {'Content-Type': f'multipart/form-data; boundary={b}'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        print('TELEGRAM_BOT_TOKEN not set — nothing sent'); return
    chat = os.environ.get('TELEGRAM_CHANNEL') or '@WhatIfStack'
    if '--check' in sys.argv:   # is the bot an admin of the channel with the right to post?
        me = call(token, 'getMe', {})['result']
        m = call(token, 'getChatMember', dict(chat_id=chat, user_id=me['id']))['result']
        print('bot', me['username'], 'in', chat, '→', m.get('status'), 'can_post_messages =', m.get('can_post_messages'))
        return
    now = datetime.datetime.now(datetime.timezone.utc)
    os.makedirs(os.path.join(Q, 'sent'), exist_ok=True)
    sent = 0
    for f in sorted(glob.glob(os.path.join(Q, '*.json'))):
        it = json.load(open(f, encoding='utf-8'))
        if it.get('at') and datetime.datetime.fromisoformat(it['at'].replace('Z', '+00:00')) > now:
            continue
        cap = caption(it.get('lines') or [])
        base = dict(chat_id=it.get('chat') or chat, parse_mode='HTML')
        media = it.get('video') or it.get('photo')
        try:
            if media:
                kind = 'video' if it.get('video') else 'photo'
                r = call(token, 'sendVideo' if kind == 'video' else 'sendPhoto', dict(base, caption=cap), kind, os.path.join(ROOT, media))
            else:
                r = call(token, 'sendMessage', dict(base, text=cap, disable_web_page_preview=False))
        except Exception as e:  # keep the item for the next run
            print('failed', os.path.basename(f), e); continue
        it['sent'] = now.isoformat(timespec='seconds'); it['message_id'] = (r.get('result') or {}).get('message_id')
        json.dump(it, open(os.path.join(Q, 'sent', os.path.basename(f)), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        os.remove(f); sent += 1
        print('sent', os.path.basename(f), it['message_id'])
    print('sent', sent)


if __name__ == '__main__':
    main()
