"""Add every sizeable Moscow Exchange share (board TQBR) to data/markets.json.

Owner (2026-11-21): a country page must list all its known stocks, not only the top 30.
Runs weekly in .github/workflows/moex-list.yml (ISS is not reachable from the Claude sandbox).
Rule: ordinary shares with market cap >= MIN_CAP_RUB; a preferred share only when the company
has no ordinary share on TQBR (e.g. Transneft). New entries get mkt=ru; prices, history and
key numbers then come from fetch_data.py / stock_stats.py like the existing MOEX stocks.
"""
import json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKETS = os.path.join(ROOT, 'data/markets.json')
MIN_CAP_RUB = float(os.environ.get('MOEX_MIN_CAP', 5e9))   # ~$60M
MAX_NEW = int(os.environ.get('MOEX_MAX_NEW', 300))
URL = ('https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off'
       '&iss.only=securities,marketdata&securities.columns=SECID,SHORTNAME,LATNAME,SECTYPE,ISIN'
       '&marketdata.columns=SECID,ISSUECAPITALIZATION,VALTODAY')


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'whatifstack.com data bot'})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def clean(n):
    n = re.sub(r'\b(PAO|PJSC|OAO|OJSC|AO|JSC|MKPAO|IPJSC|PLC|ao|ap|-ao|-ap)\b\.?', '', n or '', flags=re.I)
    n = re.sub(r'\b(ORD SHS|Public JS Com\w*|Ltd\.?|Corp\.)', '', n, flags=re.I)
    n = re.sub(r'-\d+$', '', n.strip())                      # «MGTS-5», «Yakovlev-3» = share issue numbers
    n = re.sub(r'\s+(ord|pref|ao|ap)$', '', n.strip(), flags=re.I)
    return re.sub(r'\s{2,}', ' ', n.replace('"', '')).strip(' ,.-«»') or None


def main():
    d = get(URL)
    sec = {r[0]: dict(zip(d['securities']['columns'], r)) for r in d['securities']['data']}
    for r in d['marketdata']['data']:
        m = dict(zip(d['marketdata']['columns'], r))
        if m['SECID'] in sec:
            sec[m['SECID']].update(m)
    mk = json.load(open(MARKETS, encoding='utf-8'))
    have = {r['yahoo'] for r in mk}
    # company key = ISIN issuer part (RU000A0JP5V6 -> same company for ord/pref is not guaranteed), so use the ticker stem:
    # preferred tickers are the ordinary ticker + 'P' (SBERP, TATNP, SNGSP)
    ords = {s for s, v in sec.items() if v.get('SECTYPE') == '1'}
    cand = []
    for s, v in sec.items():
        cap = v.get('ISSUECAPITALIZATION') or 0
        if cap < MIN_CAP_RUB or 'MOEX:' + s in have:
            continue
        if v.get('SECTYPE') == '2' and s.endswith('P') and s[:-1] in ords:
            continue                     # company already has an ordinary share
        if v.get('SECTYPE') not in ('1', '2'):
            continue
        name = clean(v.get('LATNAME')) or clean(v.get('SHORTNAME')) or s
        cand.append((cap, s, name))
    cand.sort(reverse=True)
    new = [{'tk': s, 'yahoo': 'MOEX:' + s, 'name': n, 'cat': 'stock', 'mkt': 'ru'} for _, s, n in cand[:MAX_NEW]]
    if not new:
        print('moex_list: nothing new')
        return
    mk += new
    with open(MARKETS, 'w', encoding='utf-8') as f:
        json.dump(mk, f, ensure_ascii=False, indent=0)
        f.write('\n')
    print(f"moex_list: +{len(new)} ({', '.join(r['tk'] for r in new[:40])}{' …' if len(new) > 40 else ''})")


if __name__ == '__main__':
    sys.exit(main())
