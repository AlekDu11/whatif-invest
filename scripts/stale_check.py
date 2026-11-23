"""Which full analyses (content/profiles/<lang>/<id>.md, kind: analysis) need a refresh so they never show stale numbers.
Owner 2026-11-23: «bitcoin peaked at $125K; a year later it is $150K — the article must not still say $125K».

Live shortcodes ({{price}}, {{ath}}, {{fromath}}, {{mcap}}, {{chg1y}}, {{dca}}…) keep numbers current by themselves; this lists the
analyses whose PLAIN TEXT may be out of date:
  new-record  the asset set a new record high after the analysis date (text like «record $126,080» is now wrong)
  old         the analysis is older than 90 days (results, CEO, products may have changed)
  title       the English title/description holds a volatile plain number (record, market value, price, % from peak)
Usage: python3 scripts/stale_check.py [N]   → JSON list, most urgent first (default 20)
"""
import json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(os.path.join(ROOT, 'data', 'market.json'), encoding='utf-8'))['assets']
VOLATILE = re.compile(r'(record|all-time|peak|trillion|market (value|cap)|worth|crossed|below its|from its high|\$\d[\d,.]*\s*(k|K)\b)', re.I)


def front(path):
    t = open(path, encoding='utf-8').read()
    if not t.startswith('---'):
        return {}
    fm = {}
    for line in t.split('---', 2)[1].splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip().strip('"\'')
    return fm


def rec_month(a):
    if a.get('athd'):
        return a['athd'][:7]
    P = a.get('p') or []
    if not P:
        return ''
    i = max(range(len(P)), key=lambda k: P[k] or 0)
    y, m = map(int, a['start'].split('-'))
    k = y * 12 + m - 1 + i
    return f'{k // 12}-{k % 12 + 1:02d}'


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    today = date.today()
    d = os.path.join(ROOT, 'content', 'profiles', 'en')
    out = []
    for f in sorted(os.listdir(d)):
        fm = front(os.path.join(d, f))
        if fm.get('kind') != 'analysis':
            continue
        aid = f[:-3]
        a = M.get(aid)
        if not a:
            continue
        written = (fm.get('date') or '')[:10]
        why = []
        if written and rec_month(a) > written[:7]:
            why.append('new-record')
        try:
            age = (today - date.fromisoformat(written)).days
        except ValueError:
            age = 999
        if age > 90:
            why.append('old')
        if VOLATILE.search(fm.get('title', '') + ' ' + fm.get('description', '')):
            why.append('title')
        if why:
            langs = [l for l in os.listdir(os.path.join(ROOT, 'content', 'profiles')) if os.path.exists(os.path.join(ROOT, 'content', 'profiles', l, f))]
            out.append(dict(id=aid, cat=a.get('cat'), written=written, age_days=age, why=why, languages=len(langs),
                            rank=a.get('rank') or 9999))
    pri = {'new-record': 0, 'title': 1, 'old': 2}
    out.sort(key=lambda r: (min(pri[w] for w in r['why']), r['rank']))
    print(f'# {len(out)} analyses need a refresh', file=sys.stderr)
    print(json.dumps(out[:n], ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
