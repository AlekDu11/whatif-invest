"""Crypto exchange rankings from the CoinGecko public API (no key) -> data/exchanges.json.

  spot:        top 120 exchanges (trust rank, 24h volume in BTC, normalized volume, country, year, site, logo)
  detail:      for the top 50: 30-day daily volume (BTC) and the top 100 trading pairs (USD volume, last price, spread, trust)
  derivatives: top 60 derivatives venues (open interest, 24h volume in BTC, perpetual / futures pair counts)
Run daily by .github/workflows/exchanges.yml. Public rate limit is tight, so calls are spaced out.
"""
import json, os, time, urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/exchanges.json')
API = 'https://api.coingecko.com/api/v3'
GAP = float(os.environ.get('CG_GAP', 7))   # seconds between calls (public API ~10/min)


def get(path, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(API + path, headers={'User-Agent': 'whatifstack.com data bot', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            print(f'  {path}: {e}', flush=True)
            time.sleep(GAP * (k + 2))
        finally:
            time.sleep(GAP)
    return None


def num(v):
    try:
        return round(float(v), 6)
    except (TypeError, ValueError):
        return None


def main():
    old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    spot = get('/exchanges?per_page=120&page=1') or []
    out = {'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 'spot': [], 'detail': old.get('detail', {}), 'derivatives': old.get('derivatives', [])}
    for e in spot:
        out['spot'].append({k: v for k, v in dict(id=e.get('id'), name=e.get('name'), year=e.get('year_established'), country=e.get('country'),
                                                     url=e.get('url'), img=e.get('image'), trust=e.get('trust_score'), rank=e.get('trust_score_rank'),
                                                     vol_btc=num(e.get('trade_volume_24h_btc')), nvol_btc=num(e.get('trade_volume_24h_btc_normalized'))).items() if v is not None})
    if not out['spot']:
        out['spot'] = old.get('spot', [])
    for e in out['spot'][:50]:
        d = {}
        ch = get(f"/exchanges/{e['id']}/volume_chart?days=30")
        if ch:
            d['chart'] = [[int(t / 1000), num(v)] for t, v in ch][-31:]
        tk = get(f"/exchanges/{e['id']}/tickers?order=volume_desc&page=1")
        if tk and tk.get('tickers'):
            d['pairs'] = [{k: v for k, v in dict(b=t.get('base'), q=t.get('target'), cg=t.get('coin_id'), last=num(t.get('last')),
                                                    usd=num((t.get('converted_volume') or {}).get('usd')), spread=num(t.get('bid_ask_spread_percentage')),
                                                    trust=t.get('trust_score'), stale=t.get('is_stale') or None).items() if v is not None}
                          for t in tk['tickers'] if not t.get('is_anomaly')][:100]
        if d:
            out['detail'][e['id']] = d
    der = get('/derivatives/exchanges?order=open_interest_btc_desc&per_page=60&page=1')
    if der:
        out['derivatives'] = [{k: v for k, v in dict(id=e.get('id'), name=e.get('name'), year=e.get('year_established'), country=e.get('country'),
                                                      url=e.get('url'), img=e.get('image'), oi_btc=num(e.get('open_interest_btc')),
                                                      vol_btc=num(e.get('trade_volume_24h_btc')), perp=e.get('number_of_perpetual_pairs'),
                                                      fut=e.get('number_of_futures_pairs')).items() if v is not None} for e in der]
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(f"exchanges: spot {len(out['spot'])}, detail {len(out['detail'])}, derivatives {len(out['derivatives'])}")


if __name__ == '__main__':
    main()
