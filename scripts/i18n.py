"""All site languages. Order = order in the language menu. uk and en get every asset page;
other languages get pages for the top assets only (see TOP_N in build.py)."""
from i18n_a import L as _a
from i18n_b import L as _b
from i18n_c import L as _c

LANGS = {**_a, **_b, **_c}
ORDER = ['uk', 'en', 'es', 'pt', 'de', 'fr', 'it', 'pl', 'tr', 'nl', 'ru', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar', 'fil']
FULL = {'uk', 'en'}          # languages with a page for every asset
DEFAULT = 'uk'               # served at /whatif/ ; other languages at /whatif/<code>/


def split12(s):
    parts = s.split('|') if '|' in s else s.split()
    assert len(parts) == 12, s
    return parts


for code, d in LANGS.items():
    d['months'] = split12(d['months']) if isinstance(d['months'], str) else d['months']
    d['since_months'] = split12(d['since_months']) if isinstance(d['since_months'], str) else d['since_months']

_ref = LANGS['en']
for code in ORDER:
    d = LANGS[code]
    miss = [k for k in _ref if k not in d] + [k for k in _ref['ui'] if k not in d['ui']]
    assert not miss, (code, miss)
