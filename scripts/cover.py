#!/usr/bin/env python3
"""Branded cover images (1200x630 JPEG) for articles and news briefs.

Usage:
  python3 scripts/cover.py --missing          # render covers for every post that has none yet
  python3 scripts/cover.py --all              # re-render everything (after a design change)
  python3 scripts/cover.py blog en my-slug    # one cover

Output: content/covers/<blog|news>/<lang>/<slug>.jpg (build.py uses it as the share image and the article hero).
Optional front matter: `stat: +52%` (big gold number) and `stat_label: $10 a day for 5 years` (small line under it).
Languages whose script the brand fonts do not cover (ja, ko, zh, th, hi, ar) fall back to the English cover.
Needs Pillow (pip install pillow).
"""
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from i18n_n import N  # noqa: E402
from i18n_ai import AI  # noqa: E402
from i18n_act import ACT  # noqa: E402

FD = os.path.join(ROOT, 'scripts', 'fonts')
F_BOLD, F_SEMI, F_TEXT = (os.path.join(FD, f) for f in ('geologica-700.ttf', 'geologica-600.ttf', 'onest.ttf'))
CMAP = set(TTFont(F_BOLD).getBestCmap()) & set(TTFont(F_TEXT).getBestCmap())
W, H = 1200, 630
BG, CARD, LINE = (12, 22, 19), (18, 32, 27), (24, 42, 36)
TEXT, MUTED, GREEN, GOLD = (236, 244, 240), (150, 172, 163), (63, 209, 155), (240, 181, 58)
LOGOS = os.path.join(ROOT, 'data', 'logos')
_B = None
# Non-Latin scripts: system fonts (Noto CJK, TLWG, FreeFont, DejaVu; libraqm shapes Arabic/Devanagari). Skipped when missing.
_CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
SCRIPT_FONTS = {'ja': (_CJK, 0), 'ko': (_CJK, 1), 'zh': (_CJK, 2), 'th': ('/usr/share/fonts/opentype/tlwg/Loma-Bold.otf', 0),
                'hi': ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 0), 'ar': ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 0)}
CHAR_WRAP = {'ja', 'zh'}   # no spaces between words


def script_font(lang):
    f = SCRIPT_FONTS.get(lang)
    return f if f and os.path.exists(f[0]) else None


def B():
    """build.py resolves {{shortcodes}} in titles to today's numbers and holds the price series."""
    global _B
    if _B is None:
        sys.argv = sys.argv[:1]
        import build as _b
        _B = _b
    return _B


def front(path):
    raw = open(path, encoding='utf-8').read()
    if not raw.startswith('---'):
        return {}
    head = raw[3:].split('\n---', 1)[0]
    return {k.strip(): v.strip().strip('"') for k, _, v in (l.partition(':') for l in head.strip().splitlines()) if k.strip()}


def fits(text):
    return all(ord(c) in CMAP or c in ' \n' for c in text)


def wrap(draw, text, font, width, chars=False):
    words, lines, cur = (re.findall(r'[A-Za-z0-9.,%$~+\-–]+|.', text) if chars else text.split()), [], ''
    for w in words:
        t = (cur + w) if chars else (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if chars:   # CJK: a line never starts with closing punctuation
        for i in range(1, len(lines)):
            while lines[i] and lines[i][0] in '？！、。，）」』：；?!,.):;%':
                lines[i - 1] += lines[i][0]
                lines[i] = lines[i][1:]
        lines = [ln.strip() for ln in lines if ln.strip()]
    return lines


def stack(d, x, y, s):
    for bx, by, bw, bh, c in ((3, 15, 18, 5, GOLD), (5, 9.5, 14, 4.5, GREEN), (7.5, 4, 9, 4.5, TEXT)):
        X, Y = x + bx * s, y + by * s
        d.rounded_rectangle([X, Y, X + bw * s, Y + bh * s], radius=bh * s / 2, fill=c)


def label(kind, lang, cat):
    n = N.get(lang) or N['en']
    if kind == 'news':
        return n['n_nav']
    cats = n['cats'].split('|')
    return {'analytics': cats[1], 'guides': cats[2], 'reports': cats[3], 'ai': (AI.get(lang) or AI['en'])['nav'], 'activities': (ACT.get(lang) or ACT['en'])['nav']}.get(cat, cats[1])


def render(kind, lang, slug, meta, out):
    title = meta.get('title', '')
    if '{{' in title:
        title = B().post_meta_title(dict(meta), lang)
    title = re.sub(r'\s+', ' ', title).strip()
    stat, stat_l = meta.get('stat', ''), meta.get('stat_label', '')
    sf_ = None
    if not title or not fits(title + stat + stat_l + label(kind, lang, meta.get('category', 'analytics'))):
        sf_ = script_font(lang) if title else None
        if not sf_:
            return False
    rtl = sf_ is not None and lang == 'ar'
    kw = {'direction': 'rtl'} if rtl else {}
    def TF(path, size):   # title/label font: the script font when the text is not Latin/Cyrillic
        return ImageFont.truetype(sf_[0], size, index=sf_[1]) if sf_ else ImageFont.truetype(path, size)
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 60):
        d.line([(x, 0), (x, H)], fill=(16, 28, 24))
    d.rectangle([0, 0, 10, H], fill=GOLD)
    ids = [a.strip() for a in meta.get('assets', '').split(',') if a.strip()]
    try:
        A = B().A
        ser = next((A[i]['p'][-61:] for i in ids if i in A and len(A[i].get('p', [])) > 12), None)
    except Exception:
        ser = None
    if ser:
        lo, hi = min(ser), max(ser)
        band = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        bd = ImageDraw.Draw(band)
        pts = [(40 + k * (W - 80) / (len(ser) - 1), 600 - (v - lo) / ((hi - lo) or 1) * 230) for k, v in enumerate(ser)]
        up = ser[-1] >= ser[0]
        col = (63, 209, 155) if up else (240, 110, 110)
        bd.polygon(pts + [(W - 40, 630), (40, 630)], fill=col + (22,))
        bd.line(pts, fill=col + (110,), width=4, joint='curve')
        im.paste(band, (0, 0), band)
        d = ImageDraw.Draw(im)
    # brand + category
    stack(d, 64, 46, 2.1)
    d.text((120, 52), 'whatifstack', font=ImageFont.truetype(F_BOLD, 30), fill=TEXT)
    cf = TF(F_SEMI, 24)
    cat = meta.get('label') or label(kind, lang, meta.get('category', 'analytics'))
    cw = d.textlength(cat, font=cf, **kw)
    d.rounded_rectangle([W - 64 - cw - 36, 46, W - 64, 92], radius=23, fill=CARD, outline=LINE, width=2)
    d.text((W - 64 - cw - 18, 55 if not sf_ else 53), cat, font=cf, fill=GREEN, **kw)
    # title: largest size that fits in 4 lines
    right = 64 + (360 if stat else 0)
    tw = W - 128 - (380 if stat else 0)
    for size in (68, 62, 56, 50, 46, 42):
        f = TF(F_BOLD, size)
        lines = wrap(d, title, f, tw, chars=sf_ is not None and lang in CHAR_WRAP)
        if len(lines) <= 4:
            break
    lines = lines[:4]
    y = 150 + (4 - len(lines)) * size * 0.28
    for ln in lines:
        x0 = (64 + tw - d.textlength(ln, font=f, **kw)) if rtl else 64
        d.text((x0, y), ln, font=f, fill=TEXT, **kw)
        y += size * (1.14 if not sf_ else 1.3)
    # optional big number on the right
    if stat:
        for ss in (96, 84, 72, 62, 54, 46):   # shrink long stats so they never run into the title
            sf = ImageFont.truetype(F_BOLD, ss)
            sw = d.textlength(stat, font=sf)
            if sw <= 370:
                break
        d.text((W - 64 - sw, 230), stat, font=sf, fill=GOLD if not stat.startswith(('-', '−')) else (240, 110, 110))
        if stat_l:
            lf = TF(F_TEXT, 24)
            for k, ln in enumerate(wrap(d, stat_l, lf, 330, chars=sf_ is not None and lang in CHAR_WRAP)[:2]):
                d.text((W - 64 - d.textlength(ln, font=lf, **kw), 350 + k * 32), ln, font=lf, fill=MUTED, **kw)
    # bottom: asset logos + date + site
    x = 64
    for aid in [a.strip() for a in meta.get('assets', '').split(',') if a.strip()][:4]:
        p = os.path.join(LOGOS, aid + '.webp')
        if os.path.exists(p):
            lg = Image.open(p).convert('RGBA').resize((56, 56), Image.LANCZOS)
            mask = Image.new('L', (56, 56), 0)
            ImageDraw.Draw(mask).ellipse([0, 0, 55, 55], fill=255)
            d.ellipse([x - 3, 527, x + 59, 589], fill=TEXT)
            im.paste(lg, (x, 530), mask)
            x += 70
    bf = ImageFont.truetype(F_TEXT, 24)
    date = meta.get('date', '')[:10]
    d.text((x + (16 if x > 64 else 0), 545), date, font=bf, fill=MUTED)
    site = 'whatifstack.com'
    d.text((W - 64 - d.textlength(site, font=bf), 545), site, font=bf, fill=MUTED)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, 'JPEG', quality=84, optimize=True, progressive=True)
    return True


def posts():
    for kind in ('blog', 'news'):
        base = os.path.join(ROOT, 'content', kind)
        for lang in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            for fn in sorted(os.listdir(os.path.join(base, lang))):
                if fn.endswith('.md'):
                    yield kind, lang, fn[:-3], os.path.join(base, lang, fn)


def out_path(kind, lang, slug):
    return os.path.join(ROOT, 'content', 'covers', kind, lang, slug + '.jpg')


def main():
    args = sys.argv[1:]
    if args[:1] == ['--x']:   # card for an X post: --x <slug> --lang en --title ... [--stat ..] [--stat-label ..] [--assets btc,eth] [--label ..]
        import argparse, datetime
        ap = argparse.ArgumentParser()
        ap.add_argument('--x'); ap.add_argument('--lang', default='en'); ap.add_argument('--title', required=True)
        ap.add_argument('--stat', default=''); ap.add_argument('--stat-label', default=''); ap.add_argument('--assets', default=''); ap.add_argument('--label', default='')
        o = ap.parse_args(args)
        meta = dict(title=o.title, stat=o.stat, stat_label=o.stat_label, assets=o.assets, label=o.label, date=datetime.date.today().isoformat())
        path = out_path('x', o.lang, o.x)
        print(path if render('x', o.lang, o.x, meta, path) else 'skipped (unsupported script)')
        return
    if len(args) == 3:
        kind, lang, slug = args
        ok = render(kind, lang, slug, front(os.path.join(ROOT, 'content', kind, lang, slug + '.md')), out_path(kind, lang, slug))
        print('rendered' if ok else 'skipped (unsupported script or no title)')
        return
    every = '--all' in args
    n = 0
    for kind, lang, slug, path in posts():
        o = out_path(kind, lang, slug)
        if every or not os.path.exists(o):
            n += render(kind, lang, slug, front(path), o)
    print(f'covers rendered: {n}')


if __name__ == '__main__':
    main()
