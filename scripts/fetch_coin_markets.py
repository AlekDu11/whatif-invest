"""Where each coin trades (CryptoRank-style «Markets»): CoinGecko /coins/{id}/tickers -> data/coin_markets.json.

Rotating: each run refreshes the N stalest coins from data/market.json (crypto with a cgid, biggest market cap first
on the first pass), so all ~600 coins are refreshed every few days within the public rate limit.
Per coin keeps up to 40 markets across all quote currencies (USDT, USD, EUR, BTC, TRY, KRW...), sorted by 24h USD volume.
  {"updated": "...", "c": {cgid: {"t": "YYYY-MM-DD", "m": [[exchange_id, exchange_name, base, quote, price_usd, vol_usd, spread, trust, url], ...]}}}
"""
import json, os, sys, time, urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/coin_markets.json')
API = 'https://api.coingecko.com/api/v3'
GAP = float(os.environ.get('CG_GAP', 7))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
BUDGET = float(os.environ.get('CM_BUDGET', 35 * 60))   # seconds
KEEP = 40


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


def r6(v):
    try:
        return float(f'{float(v):.6g}')
    except (TypeError, ValueError):
        return None


def main():
    t0 = time.time()
    old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cm = old.get('c', {})
    assets = json.load(open(os.path.join(ROOT, 'data/market.json'), encoding='utf-8'))['assets']
    assets = {k: a for k, a in assets.items() if not (a.get('cat') == 'crypto' and a.get('src') in ('cg-spot', 'coingecko'))}   # owner 2026-11-23: no-exchange coins are off the site
    assets = assets.values() if isinstance(assets, dict) else assets
    coins = sorted({(a.get('rank') or 99999, a['cgid']) for a in assets if a.get('cat') == 'crypto' and a.get('cgid')})
    ids = [c for _, c in coins]
    todo = sorted(ids, key=lambda c: (cm.get(c, {}).get('t', ''), ids.index(c)))[:N]
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    done = 0
    for cid in todo:
        if time.time() - t0 > BUDGET:
            break
        d = get(f'/coins/{cid}/tickers?order=volume_desc&depth=true&include_exchange_logo=false')
        if not d or 'tickers' not in d:
            continue
        rows, seen = [], set()
        for t in d['tickers']:
            if t.get('is_anomaly') or t.get('is_stale'):
                continue
            mk = t.get('market') or {}
            vol = r6((t.get('converted_volume') or {}).get('usd'))
            px = r6((t.get('converted_last') or {}).get('usd'))
            if not vol or not px:
                continue
            key = (mk.get('identifier'), t.get('base'), t.get('target'))
            if key in seen:
                continue
            seen.add(key)
            rows.append([mk.get('identifier'), mk.get('name'), t.get('base'), t.get('target'), px, round(vol), r6(t.get('bid_ask_spread_percentage')),
                         t.get('trust_score'), t.get('trade_url') or ''])
        rows.sort(key=lambda r: -r[5])
        cm[cid] = {'t': today, 'm': rows[:KEEP]}
        done += 1
    ids_set = set(ids)
    out = {'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 'c': {k: v for k, v in cm.items() if k in ids_set}}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(f'coin markets: refreshed {done}/{len(todo)}, stored {len(out["c"])} coins', flush=True)


if __name__ == '__main__':
    main()
