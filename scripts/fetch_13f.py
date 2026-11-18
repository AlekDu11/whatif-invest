"""Famous investors' portfolios from SEC 13F filings -> data/investors.json (run weekly by .github/workflows/investors.yml).

For each fund: the latest two 13F-HR filings (holdings at the end of a quarter, filed up to 45 days later), aggregated by CUSIP,
CUSIP -> ticker through OpenFIGI (free, cached in data/cusip_map.json). Options (put/call) are skipped.
  {"updated": ..., "inv": {id: {name, fund, cik, period, filed, value, n, top: [[ticker, issuer, value, weight, shares, change]], sold: [[ticker, issuer, value_before]]}}}
change: fraction of shares added/cut vs the previous quarter, "new" for a new position.
"""
import json, os, re, sys, time, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/investors.json')
MAP = os.path.join(ROOT, 'data/cusip_map.json')
UA = 'WhatIfStack research support@whatifstack.com'

# id, person, fund, CIK (SEC)
FUNDS = [
    ('buffett', 'Warren Buffett', 'Berkshire Hathaway', 1067983),
    ('ackman', 'Bill Ackman', 'Pershing Square Capital', 1336528),
    ('burry', 'Michael Burry', 'Scion Asset Management', 1649339),
    ('dalio', 'Ray Dalio', 'Bridgewater Associates', 1350694),
    ('wood', 'Cathie Wood', 'ARK Investment Management', 1697748),
    ('druckenmiller', 'Stanley Druckenmiller', 'Duquesne Family Office', 1536411),
    ('tepper', 'David Tepper', 'Appaloosa', 1656456),
    ('klarman', 'Seth Klarman', 'Baupost Group', 1061768),
    ('li-lu', 'Li Lu', 'Himalaya Capital', 1709323),
    ('gates', 'Bill Gates', 'Gates Foundation Trust', 1166559),
    ('smith', 'Terry Smith', 'Fundsmith', 1569205),
    ('loeb', 'Dan Loeb', 'Third Point', 1040273),
    ('icahn', 'Carl Icahn', 'Icahn Enterprises', 921669),
    ('coleman', 'Chase Coleman', 'Tiger Global Management', 1167483),
    ('einhorn', 'David Einhorn', 'Greenlight Capital', 1079114),
    ('marks', 'Howard Marks', 'Oaktree Capital Management', 949509),
]


def get(url, data=None, headers=None, tries=3):
    for k in range(tries):
        try:
            h = {'User-Agent': UA, 'Accept-Encoding': 'identity'}
            h.update(headers or {})
            req = urllib.request.Request(url, data=data, headers=h)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print(f'  {url[:90]}: {e}', flush=True)
            time.sleep(2 * (k + 1))
        finally:
            time.sleep(0.3)   # SEC fair access: < 10 requests a second
    return None


def jget(url, **kw):
    b = get(url, **kw)
    try:
        return json.loads(b) if b else None
    except ValueError:
        return None


def filings(cik):
    d = jget(f'https://data.sec.gov/submissions/CIK{cik:010d}.json')
    if not d:
        return None, []
    r = d.get('filings', {}).get('recent', {})
    out = [(acc, fd, pd) for acc, form, fd, pd in zip(r.get('accessionNumber', []), r.get('form', []), r.get('filingDate', []), r.get('reportDate', []))
           if form == '13F-HR']
    # one filing per period (amendments 13F-HR/A are skipped; a later 13F-HR for the same period wins)
    seen, uniq = set(), []
    for acc, fd, pd in out:
        if pd in seen:
            continue
        seen.add(pd)
        uniq.append((acc, fd, pd))
    return d.get('name'), uniq[:2]


def holdings(cik, acc):
    base = f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-", "")}/'
    idx = jget(base + 'index.json')
    if not idx:
        return None
    files = [f['name'] for f in idx.get('directory', {}).get('item', []) if f['name'].lower().endswith('.xml') and 'primary_doc' not in f['name'].lower()]
    for fn in files:
        raw = get(base + fn)
        if not raw or b'infoTable' not in raw:
            continue
        txt = re.sub(rb'<(/?)[A-Za-z0-9_]+:', rb'<\1', raw)        # drop namespaces prefixes
        txt = re.sub(rb'\sxmlns(:\w+)?="[^"]*"', b'', txt)
        txt = re.sub(rb'\s[A-Za-z_]+:[A-Za-z_]+="[^"]*"', b'', txt)      # prefixed attributes (xsi:schemaLocation) whose namespace is gone
        try:
            root = ET.fromstring(txt)
        except ET.ParseError as e:
            print(f'  {fn}: {e}', flush=True)
            continue
        agg = {}
        for it in root.iter('infoTable'):
            g = lambda t: (it.findtext(t) or '').strip()
            if g('putCall'):
                continue
            cusip = g('cusip').upper()
            try:
                val = float(g('value') or 0)
                sh = float(it.findtext('shrsOrPrnAmt/sshPrnamt') or 0)
            except ValueError:
                continue
            a = agg.setdefault(cusip, {'issuer': g('nameOfIssuer'), 'value': 0.0, 'shares': 0.0})
            a['value'] += val
            a['shares'] += sh
        return agg
    return None


def figi(cusips, cache):
    todo = [c for c in cusips if c not in cache]
    for k in range(0, len(todo), 10):
        chunk = todo[k:k + 10]
        body = json.dumps([{'idType': 'ID_CUSIP', 'idValue': c, 'exchCode': 'US'} for c in chunk]).encode()
        d = None
        for _ in range(3):
            raw = get('https://api.openfigi.com/v3/mapping', data=body, headers={'Content-Type': 'application/json'})
            try:
                d = json.loads(raw) if raw else None
            except ValueError:
                d = None
            if d is not None:
                break
            time.sleep(10)
        for c, r in zip(chunk, d or []):
            data = (r or {}).get('data') or []
            cache[c] = (data[0].get('ticker') or '') if data else ''
        time.sleep(2.6)      # ~25 requests a minute without an API key
    return cache


def main():
    cache = json.load(open(MAP)) if os.path.exists(MAP) else {}
    old = json.load(open(OUT)) if os.path.exists(OUT) else {'inv': {}}
    out = {'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 'inv': {}}
    for fid, person, fund, cik in FUNDS:
        name, fl = filings(cik)
        if not fl:
            print(f'{fid}: no 13F-HR filings (CIK {cik})')
            if fid in old.get('inv', {}):
                out['inv'][fid] = old['inv'][fid]
            continue
        cur = holdings(cik, fl[0][0])
        prev = holdings(cik, fl[1][0]) if len(fl) > 1 else {}
        if not cur:
            print(f'{fid}: could not read the information table')
            if fid in old.get('inv', {}):
                out['inv'][fid] = old['inv'][fid]
            continue
        for h in (cur, prev or {}):     # some filers still report values in thousands: then value / shares is a tiny "price"
            px = sorted(v['value'] / v['shares'] for v in h.values() if v['shares'] > 0 and v['value'] > 0)
            if px and px[len(px) // 2] < 0.5:
                for v in h.values():
                    v['value'] *= 1000
        figi(list(cur) + list(prev or {}), cache)
        total = sum(v['value'] for v in cur.values()) or 1
        top = []
        for c, v in sorted(cur.items(), key=lambda z: -z[1]['value']):
            p = (prev or {}).get(c)
            chg = 'new' if prev and not p else (round(v['shares'] / p['shares'] - 1, 4) if p and p['shares'] else None)
            top.append([cache.get(c, ''), v['issuer'], round(v['value']), round(v['value'] / total, 5), round(v['shares']), chg])
        sold = [[cache.get(c, ''), v['issuer'], round(v['value'])] for c, v in sorted((prev or {}).items(), key=lambda z: -z[1]['value']) if c not in cur][:15]
        out['inv'][fid] = dict(name=person, fund=fund, entity=name, cik=cik, period=fl[0][2], filed=fl[0][1], prev=fl[1][2] if len(fl) > 1 else None,
                               value=round(total), n=len(cur), top=top[:60], sold=sold)
        print(f'{fid}: {name} {fl[0][2]} — {len(cur)} positions, ${total / 1e9:.2f} bn')
    json.dump(cache, open(MAP, 'w'), separators=(',', ':'), sort_keys=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(f'investors: {len(out["inv"])}')


if __name__ == '__main__':
    sys.exit(main())
