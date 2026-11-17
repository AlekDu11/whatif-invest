#!/usr/bin/env python3
"""Animated "$100 a month in A vs B vs C" race video for X / Telegram (1080x1350, MP4, ~20 s).

  python3 scripts/race_video.py btc eth sol --amt 100 --since 2020-04 --lang en --out social/video/btc-eth-sol.mp4

Uses our monthly prices from data/market.json; logos from data/logo (or dist/assets/logo); brand fonts from scripts/fonts.
Needs: pillow, ffmpeg.
"""
import argparse, json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(ROOT, 'scripts', 'fonts')
F_BOLD, F_SEMI, F_TEXT = (os.path.join(FD, f) for f in ('geologica-700.ttf', 'geologica-600.ttf', 'onest.ttf'))
W, H, FPS = 1080, 1350, 30
BG, CARD, TEXT, MUTED, LINE, ACC = (12, 22, 18), (20, 34, 28), (236, 244, 240), (140, 160, 151), (40, 58, 50), (63, 209, 155)
PALETTE = [(247, 183, 51), (98, 160, 255), (63, 209, 155), (255, 122, 110), (190, 140, 255)]
MON = {
    'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'uk': ['січ', 'лют', 'бер', 'кві', 'тра', 'чер', 'лип', 'сер', 'вер', 'жов', 'лис', 'гру'],
    'ru': ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'],
}
TXT = {
    'en': dict(t='${amt} a month since {d}', inv='Invested', w='Winner'),
    'uk': dict(t='${amt} щомісяця з {d}', inv='Вкладено', w='Переможець'),
    'ru': dict(t='${amt} в месяц с {d}', inv='Вложено', w='Победитель'),
}


def ym(s):
    y, m = map(int, s.split('-'))
    return y * 12 + m - 1


def money(v):
    if v >= 1e6:
        return f'${v / 1e6:.2f}M'
    if v >= 1e4:
        return f'${v / 1e3:.1f}K'
    return f'${v:,.0f}'


def logo(aid, size):
    for d in (os.path.join(ROOT, 'data', 'logo'), os.path.join(ROOT, 'dist', 'assets', 'logo')):
        p = os.path.join(d, aid + '.webp')
        if os.path.exists(p):
            im = Image.open(p).convert('RGBA').resize((size, size), Image.LANCZOS)
            mask = Image.new('L', (size, size), 0)
            ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
            out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            out.paste(im, (0, 0), mask)
            return out
    return None


def badge(tk, color, size):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, size - 1, size - 1), fill=color)
    f = ImageFont.truetype(F_BOLD, int(size * .36))
    t = tk[:3]
    d.text(((size - d.textlength(t, font=f)) / 2, size * .3), t, font=f, fill=BG)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ids', nargs='+')
    ap.add_argument('--amt', type=float, default=100)
    ap.add_argument('--since', default=None, help='YYYY-MM; default = latest start of the chosen assets')
    ap.add_argument('--lang', default='en', choices=list(TXT))
    ap.add_argument('--secs', type=float, default=16)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    m = json.load(open(os.path.join(ROOT, 'data', 'market.json')))
    A = m.get('assets', m)
    ids = [i for i in a.ids if i in A][:5]
    if len(ids) < 2:
        sys.exit('need at least 2 known asset ids')
    start = max(ym(A[i]['start']) for i in ids)
    if a.since:
        start = max(start, ym(a.since))
    end = min(ym(A[i]['end']) for i in ids)
    months = list(range(start, end + 1))
    # simulate: buy $amt at each month's price
    S = {}
    for i in ids:
        s0, p = ym(A[i]['start']), A[i]['p']
        u, vals = 0.0, []
        for k in months:
            px = p[k - s0]
            u += a.amt / px
            vals.append(u * px)
        S[i] = vals
    inv = [a.amt * (j + 1) for j in range(len(months))]
    L, T = MON[a.lang], TXT[a.lang]
    name = lambda i: A[i].get('tk') or i.upper()
    col = {i: PALETTE[k % len(PALETTE)] for k, i in enumerate(ids)}
    lg = {i: logo(i, 64) or badge(name(i), col[i], 64) for i in ids}
    lg_big = {i: logo(i, 120) or badge(name(i), col[i], 120) for i in ids}
    f_title, f_big, f_mid, f_sm, f_xs = (ImageFont.truetype(F_BOLD, 52), ImageFont.truetype(F_BOLD, 40), ImageFont.truetype(F_SEMI, 32),
                                         ImageFont.truetype(F_SEMI, 26), ImageFont.truetype(F_TEXT, 22))
    d0 = f'{L[start % 12]} {start // 12}'
    title = T['t'].format(amt=f'{a.amt:,.0f}', d=d0)
    # chart box
    CX0, CX1, CY0, CY1 = 90, W - 230, 430, 1170
    n = len(months)
    anim = int(a.secs * FPS)
    hold = int(3.5 * FPS)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    proc = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-maxrate', '600k', '-bufsize', '1200k', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', a.out], stdin=subprocess.PIPE)
    ymax_s = None
    for fr in range(anim + hold):
        t = min(1.0, fr / anim)
        e = t * t * (3 - 2 * t) * 0.15 + t * 0.85          # gentle ease
        p0 = min(6, n - 1)
        pos = p0 + e * (n - 1 - p0)   # start a few months in: frame 0 is the X/Telegram thumbnail
        j = int(pos)
        fj = pos - j
        im = Image.new('RGB', (W, H), BG)
        d = ImageDraw.Draw(im, 'RGBA')
        # header
        d.text((60, 46), 'whatifstack', font=f_mid, fill=ACC)
        d.text((60, 92), title, font=f_title, fill=TEXT)
        # contenders row
        x = 60
        for k, i in enumerate(ids):
            if lg[i]:
                im.paste(lg[i], (int(x), 180), lg[i])
            d.text((x + 76, 192), name(i), font=f_big, fill=col[i])
            x += 76 + d.textlength(name(i), font=f_big) + 26
            if k < len(ids) - 1:
                d.text((x, 200), 'vs', font=f_sm, fill=MUTED)
                x += d.textlength('vs', font=f_sm) + 26
        # current date + invested
        cur = months[min(j + (1 if fj > .5 else 0), n - 1)]
        invd = inv[j] + (inv[min(j + 1, n - 1)] - inv[j]) * fj
        d.text((60, 290), f'{L[cur % 12]} {cur // 12}', font=f_title, fill=TEXT)
        d.text((60, 356), f'{T["inv"]}: {money(invd)}', font=f_sm, fill=MUTED)
        # values at pos
        val = lambda series: series[j] + (series[min(j + 1, n - 1)] - series[j]) * fj
        cur_vals = {i: val(S[i]) for i in ids}
        ymax_t = max(max(max(S[i][:j + 2]) for i in ids), invd) * 1.12
        ymax_s = ymax_t if ymax_s is None else ymax_s + (ymax_t - ymax_s) * 0.12
        ymax = max(ymax_s, invd * 1.05, max(cur_vals.values()) * 1.05)
        X = lambda q: CX0 + (CX1 - CX0) * q / max(1, n - 1)
        Y = lambda v: CY1 - (CY1 - CY0) * v / ymax
        # grid
        for g in range(5):
            gv = ymax * g / 4
            gy = Y(gv)
            d.line((CX0, gy, CX1, gy), fill=LINE, width=2)
            d.text((CX1 + 14, gy - 14), money(gv), font=f_xs, fill=MUTED)
        # invested line
        pts = [(X(q), Y(inv[q])) for q in range(j + 1)] + [(X(pos), Y(invd))]
        for q in range(len(pts) - 1):
            if q % 2 == 0:
                d.line(pts[q] + pts[q + 1], fill=MUTED, width=3)
        # asset lines
        order = sorted(ids, key=lambda i: cur_vals[i])
        for i in order:
            pts = [(X(q), Y(S[i][q])) for q in range(j + 1)] + [(X(pos), Y(cur_vals[i]))]
            d.line(pts, fill=col[i], width=6, joint='curve')
        # head labels (avoid overlaps)
        heads = sorted(((Y(cur_vals[i]), i) for i in ids))
        placed = []
        for yy, i in heads:
            ly = yy
            for py in placed:
                if abs(ly - py) < 70:
                    ly = py + 70
            placed.append(ly)
            hx = X(pos)
            sm = lg[i].resize((46, 46)) if lg[i] else None
            if sm:
                d.ellipse((hx - 27, yy - 27, hx + 27, yy + 27), fill=col[i])
                im.paste(sm, (int(hx) - 23, int(yy) - 23), sm)
            else:
                d.ellipse((hx - 12, yy - 12, hx + 12, yy + 12), fill=col[i])
            roi = cur_vals[i] / invd - 1 if invd else 0
            tx = min(int(hx) + 38, W - 200)
            if abs(ly - yy) > 4:
                d.line((hx + 27, yy, tx - 4, ly - 6), fill=col[i] + (160,), width=2)
            d.text((tx, ly - 36), money(cur_vals[i]), font=f_mid, fill=col[i])
            d.text((tx, ly + 2), f'{roi * 100:+.0f}%', font=f_xs, fill=(ACC if roi >= 0 else (255, 122, 110)))
        # footer
        d.text((60, H - 110), 'whatifstack.com', font=f_mid, fill=ACC)
        d.text((60, H - 64), {'en': 'Real prices · not investment advice', 'uk': 'Реальні ціни · не інвестпорада', 'ru': 'Реальные цены · не инвестсовет'}[a.lang], font=f_xs, fill=MUTED)
        # final overlay
        if fr >= anim:
            k = min(1.0, (fr - anim) / (0.6 * FPS))
            ov = Image.new('RGBA', (W, H - 400), BG + (int(255 * k),))
            im.paste(ov, (0, 270), ov)
            d = ImageDraw.Draw(im, 'RGBA')
            if k >= 1:
                rank = sorted(ids, key=lambda i: -S[i][-1])
                y = 430
                d.text((80, y - 110), f'{T["inv"]}: {money(inv[-1])}', font=f_mid, fill=MUTED)
                for r, i in enumerate(rank):
                    d.rounded_rectangle((70, y, W - 70, y + 150), radius=28, fill=CARD + (255,), outline=col[i] if r == 0 else None, width=4)
                    if lg_big[i]:
                        im.paste(lg_big[i].resize((96, 96)), (100, y + 27), lg_big[i].resize((96, 96)))
                    d.text((220, y + 28), f'{r + 1}. {name(i)}', font=f_big, fill=TEXT)
                    roi = S[i][-1] / inv[-1] - 1
                    d.text((220, y + 82), f'{roi * 100:+.0f}%', font=f_mid, fill=(ACC if roi >= 0 else (255, 122, 110)))
                    vt = money(S[i][-1])
                    d.text((W - 110 - d.textlength(vt, font=f_title), y + 46), vt, font=f_title, fill=col[i])
                    y += 175
                if rank:
                    d.text((80, y + 20), f'{T["w"]}: {name(rank[0])} 🏆'.replace(' 🏆', ''), font=f_big, fill=col[rank[0]])
        proc.stdin.write(im.tobytes())
    proc.stdin.close()
    proc.wait()
    res = {i: dict(val=round(S[i][-1]), roi=round(S[i][-1] / inv[-1] - 1, 4)) for i in ids}
    print(json.dumps(dict(out=a.out, since=d0, invested=inv[-1], months=n, res=res), ensure_ascii=False))


if __name__ == '__main__':
    main()
