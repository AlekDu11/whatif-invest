"""All site languages. Order = order in the language menu. uk and en get every asset page;
other languages get pages for the top assets only (see TOP_N in build.py)."""
from i18n_a import L as _a
from i18n_b import L as _b
from i18n_c import L as _c
from i18n_w import W as _w
from i18n_x import X as _x, BUB as _bub, BP as _bp, TVX as _tvx

LANGS = {**_a, **_b, **_c}
ORDER = ['uk', 'en', 'es', 'pt', 'de', 'fr', 'it', 'pl', 'tr', 'nl', 'ru', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar', 'fil']
FULL = {'uk', 'en'}          # languages with a page for every asset
DEFAULT = 'uk'               # served at /whatif/ ; other languages at /whatif/<code>/


def split12(s):
    parts = s.split('|') if '|' in s else s.split()
    assert len(parts) == 12, s
    return parts


for code, d in LANGS.items():
    d['w'] = _w[code]
    d['x'] = dict(_x[code], bub_h1=_bub[code][0], bub_d=_bub[code][1], fund=_tvx[code][0], prof=_tvx[code][1], scr_h1=_tvx[code][2], scr_d=_tvx[code][3], xrates=_tvx[code][4])
    d['ui'].update({'x_' + k: v for k, v in _x[code].items()})
    d['ui']['bp'] = _bp[code]
    assert len(_bp[code].split('|')) == 6, code
    d['ui'].update({'w_' + k: v for k, v in _w[code].items()})
    d['months'] = split12(d['months']) if isinstance(d['months'], str) else d['months']
    d['since_months'] = split12(d['since_months']) if isinstance(d['since_months'], str) else d['since_months']

_ref = LANGS['en']
for code in ORDER:
    d = LANGS[code]
    miss = [k for k in _ref if k not in d] + [k for k in _ref['ui'] if k not in d['ui']]
    assert not miss, (code, miss)
