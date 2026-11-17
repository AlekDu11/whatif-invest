"""Next stocks that still need a full written analysis (content/profiles/<lang>/<id>.md with `kind: analysis`).

Usage: python3 scripts/analysis_todo.py [N]   -> JSON list of N candidates (default 15) with the facts to start from.
Order: site order (popular first), stocks with Yahoo key stats only, a few non-US names mixed in every batch.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 15


def done(aid):
    p = os.path.join(ROOT, 'content/profiles/en', aid + '.md')
    return os.path.exists(p) and 'kind: analysis' in open(p, encoding='utf-8').read(600)


def main():
    m = json.load(open(os.path.join(ROOT, 'data/market.json'), encoding='utf-8'))
    A = m['assets']
    st = json.load(open(os.path.join(ROOT, 'data/stockstats.json'), encoding='utf-8'))
    ids = [i for i, a in A.items() if a.get('cat') == 'stock' and st.get(a.get('yahoo') or '') and not done(i)]
    us = [i for i in ids if not A[i].get('mkt')]
    intl = [i for i in ids if A[i].get('mkt')]
    pick, k = [], 0
    while len(pick) < N and (us or intl):     # 2 US : 1 international
        src = intl if (k % 3 == 2 and intl) or not us else us
        pick.append(src.pop(0))
        k += 1
    out = []
    for i in pick:
        a, s = A[i], st[A[i]['yahoo']]
        out.append(dict(id=i, name=a['name'].get('en'), ticker=a['tk'], yahoo=a['yahoo'], market=a.get('mkt') or 'us',
                        sector=s.get('sec'), industry=s.get('ind'), country=s.get('cty'), website=s.get('web'),
                        currency=s.get('ccy'), stats={k: s.get(k) for k in ('mcap', 'pe', 'dps', 'rev', 'revg', 'pm', 'ni', 'h52', 'l52', 'rec', 'tgt', 'nan', 'emp')},
                        yahoo_summary=(s.get('ds') or {}).get('en')))
    left = len(ids) - len(out)
    print(json.dumps({'todo_after_this_batch': left, 'batch': out}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
