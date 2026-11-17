#!/usr/bin/env python3
"""Ready-to-paste JavaScript that renders + encodes the race video INSIDE a page (for X, whose CSP blocks our MP4).
  python3 scripts/race_snippet.py btc gold spy --amt 100 --since 2016-01 > /tmp/race.js
Paste the whole output into the browser javascript tool on x.com; it leaves the MP4 in window.__wisRaceFile."""
import argparse, base64, io, json, os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from race_video import ROOT, PALETTE, MON, TXT, ym  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('ids', nargs='+'); ap.add_argument('--amt', type=float, default=100); ap.add_argument('--since')
ap.add_argument('--lang', default='en', choices=list(TXT)); ap.add_argument('--secs', type=float, default=16)
a = ap.parse_args()
m = json.load(open(os.path.join(ROOT, 'data', 'market.json'))); A = m.get('assets', m)
ids = [i for i in a.ids if i in A][:5]
start = max(ym(A[i]['start']) for i in ids)
if a.since:
    start = max(start, ym(a.since))
end = min(ym(A[i]['end']) for i in ids)
months = list(range(start, end + 1)); L, T = MON[a.lang], TXT[a.lang]
S = {}
for i in ids:
    s0, p, u, v = ym(A[i]['start']), A[i]['p'], 0.0, []
    for k in months:
        u += a.amt / p[k - s0]; v.append(round(u * p[k - s0]))
    S[i] = v


def logo(aid):
    for d in (os.path.join(ROOT, 'data', 'logo'), os.path.join(ROOT, 'dist', 'assets', 'logo')):
        f = os.path.join(d, aid + '.webp')
        if os.path.exists(f):
            b = io.BytesIO(); Image.open(f).convert('RGBA').resize((72, 72), Image.LANCZOS).save(b, 'WEBP', quality=70)
            return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
    return ''


hexc = lambda c: '#%02x%02x%02x' % c
R = dict(ids=ids, slug='-'.join(ids), secs=a.secs, months=[f'{L[k % 12]} {k // 12}' for k in months], inv=[a.amt * (j + 1) for j in range(len(months))], S=S,
         tk={i: A[i].get('tk') or i.upper() for i in ids}, col={i: hexc(PALETTE[k % len(PALETTE)]) for k, i in enumerate(ids)}, logo={i: logo(i) for i in ids},
         title=T['t'].format(amt=f'{a.amt:,.0f}', d=f'{L[start % 12]} {start // 12}'), invLabel=T['inv'], winLabel=T['w'],
         foot={'en': 'Real prices · not investment advice', 'uk': 'Реальні ціни · не інвестпорада', 'ru': 'Реальные цены · не инвестсовет'}[a.lang])
js = open(os.path.join(ROOT, 'social', 'race_canvas.js'), encoding='utf-8').read().strip().rstrip(';')
body = js[js.index('(async () =>'):]
print('const RACE = ' + json.dumps(R, ensure_ascii=False, separators=(',', ':')) + ';\nawait ' + body + ';')
