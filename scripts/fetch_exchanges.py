"""Crypto exchange rankings from the CoinGecko public API (no key) -> data/exchanges.json.

  spot:        top 120 exchanges (trust rank, 24h volume in BTC, normalized volume, country, year, site, logo)
  detail:      for the top 100: 30-day daily volume (BTC), the top 100 trading pairs (USD volume, last price, spread, trust)
               and profile facts (socials, centralized, number of coins/pairs listed) from /exchanges/{id}
  reserves:    proof-of-reserves wallets tracked by DefiLlama (category CEX): total, 1d/7d/30d change, by chain, top tokens
  derivatives: top 60 derivatives venues (open interest, 24h volume in BTC, perpetual / futures pair counts)
Run daily by .github/workflows/exchanges.yml. Public rate limit is tight, so calls are spaced out.
"""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exchange_apis   # pairs straight from the big exchanges' own public APIs
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


def _get_url(u, timeout=60):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'whatifstack.com data bot', 'Accept': 'application/json'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except Exception as e:
        print(f'  {u}: {e}', flush=True)
        return None


def _norm(x):
    return ''.join(ch for ch in (x or '').lower() if ch.isalnum()).replace('cex', '').replace('exchange', '').replace('global', '')


ALIAS = {'okx': 'okex', 'gateio': 'gate', 'gate': 'gate', 'cryptocom': 'crypto_com', 'htx': 'huobi', 'bitfinex': 'bitfinex', 'kucoin': 'kucoin',
         'coinbase': 'gdax', 'bitget': 'bitget', 'mexc': 'mxc', 'binance': 'binance', 'bybit': 'bybit_spot', 'kraken': 'kraken', 'bingx': 'bingx',
         'deribit': 'deribit', 'bitmex': 'bitmex', 'gemini': 'gemini', 'bitstamp': 'bitstamp', 'upbit': 'upbit', 'bithumb': 'bithumb', 'whitebit': 'whitebit'}


def reserves(spot):
    """Proof-of-reserves wallets tracked by DefiLlama (api.llama.fi, free, no key), matched to CoinGecko exchange ids."""
    ps = _get_url('https://api.llama.fi/protocols', 120)
    if not isinstance(ps, list):
        return {}
    by_norm = {_norm(e['name']): e['id'] for e in spot}
    by_norm.update({_norm(e['id']): e['id'] for e in spot})
    ids = {e['id'] for e in spot}
    out = {}
    for p in ps:
        if p.get('category') != 'CEX' or not p.get('tvl'):
            continue
        n = _norm(p.get('name'))
        xid = ALIAS.get(n) if ALIAS.get(n) in ids else by_norm.get(n)
        if not xid or xid in out:
            continue
        ch = {k: v for k, v in (p.get('chainTvls') or {}).items() if '-' not in k and isinstance(v, (int, float)) and v > 0}
        out[xid] = {k: v for k, v in dict(tvl=round(p['tvl']), d1=num(p.get('change_1d')), d7=num(p.get('change_7d')), m1=num(p.get('change_1m')),
                                          slug=p.get('slug'), name=p.get('name'),
                                          chains=[[c, round(v)] for c, v in sorted(ch.items(), key=lambda z: -z[1])[:8]] or None).items() if v is not None}
    for xid in sorted(out, key=lambda i: -out[i]['tvl'])[:25]:      # token breakdown for the biggest ones
        d = _get_url(f"https://api.llama.fi/protocol/{out[xid]['slug']}", 120)
        try:
            last = (d.get('tokensInUsd') or [])[-1]['tokens']
            tot = sum(v for v in last.values() if isinstance(v, (int, float)) and v > 0) or 1
            out[xid]['tokens'] = [[k, round(v), round(v / tot, 4)] for k, v in sorted(last.items(), key=lambda z: -(z[1] or 0))[:10] if v and v > 0]
            hist = d.get('tvl') or []
            out[xid]['hist'] = [[int(h['date']), round(h['totalLiquidityUSD'])] for h in hist[-365::7]]
        except Exception:
            pass
        time.sleep(1.5)
    return out


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
    out['reserves'] = reserves(out['spot']) or old.get('reserves', {})     # fast (DefiLlama) — before the slow CoinGecko loop
    api = exchange_apis.fetch_all()     # Binance, OKX, Bybit, Gate, KuCoin, MEXC, Bitget: all spot pairs from the exchange itself
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
    btc = next((x.get('price') for x in [((json.load(open(os.path.join(ROOT, 'data/market.json'))).get('assets') or {}).get('btc') or {})]), None) if os.path.exists(os.path.join(ROOT, 'data/market.json')) else None
    cgv = {e['id']: (e.get('vol_btc') or 0) * (btc or 0) for e in out['spot']}
    for xid, v in list(api.items()):
        if cgv.get(xid) and v['vol_usd'] > 4 * cgv[xid]:   # sanity: the exchange's own total must be close to CoinGecko's
            print(f'  {xid}: API volume ${v["vol_usd"]:,.0f} vs CoinGecko ${cgv[xid]:,.0f} — ignored', flush=True)
            del api[xid]
    for xid in exchange_apis.SOURCES:   # API skipped/ignored today: let CoinGecko refresh that exchange instead of keeping stale API pairs
        if xid not in api and (out['detail'].get(xid) or {}).get('src') == 'api':
            for k in ('src', 'api', 'tp'):
                out['detail'][xid].pop(k, None)
    for xid, v in api.items():
        d = out['detail'].setdefault(xid, {})
        d.update(pairs=v['pairs'], src='api', tp=now)
        d['api'] = {'pairs': v['n_pairs'], 'coins': v['n_coins'], 'vol_usd': v['vol_usd']}
    t0 = time.time()
    budget = float(os.environ.get('XC_BUDGET', 35 * 60))
    top = out['spot'][:100]
    # exchanges with no pairs/profile yet come first, then the stalest
    top = sorted(top, key=lambda e: (bool(out['detail'].get(e['id'], {}).get('pairs')), out['detail'].get(e['id'], {}).get('t', ''), top.index(e)))
    for e in top:
        if time.time() - t0 > budget:
            print('time budget reached; the rest is refreshed next run', flush=True)
            break
        d = dict(out['detail'].get(e['id'], {}))   # keep what we had if a call fails (rate limits): never wipe pairs/profile
        ch = get(f"/exchanges/{e['id']}/volume_chart?days=30")
        if ch:
            d['chart'] = [[int(t / 1000), num(v)] for t, v in ch][-31:]
        tk = get(f"/exchanges/{e['id']}")
        if tk:
            soc = {k: v for k, v in dict(tw=tk.get('twitter_handle'), tg=tk.get('telegram_url'), fb=tk.get('facebook_url'), rd=tk.get('reddit_url'),
                                         o1=tk.get('other_url_1'), o2=tk.get('other_url_2')).items() if v}
            d['prof'] = {k: v for k, v in dict(cen=tk.get('centralized'), soc=soc or None, coins=tk.get('coins'), pairs=tk.get('pairs'),
                                               notice=(tk.get('public_notice') or '')[:300] or None, alert=(tk.get('alert_notice') or '')[:300] or None).items() if v is not None}
            tk['tickers'] = sorted(tk.get('tickers') or [], key=lambda t: -((t.get('converted_volume') or {}).get('usd') or 0))
        if tk and not tk.get('tickers'):   # big exchanges: the profile call sometimes comes back without tickers
            tt = get(f"/exchanges/{e['id']}/tickers?order=volume&depth=false&page=1")
            if tt and tt.get('tickers'):
                tk['tickers'] = sorted(tt['tickers'], key=lambda t: -((t.get('converted_volume') or {}).get('usd') or 0))
        if tk:
            d['t'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
        if tk and tk.get('tickers') and e['id'] not in api:
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
    print(f"reserves: {len(out['reserves'])} exchanges")
    print(f"exchanges: spot {len(out['spot'])}, detail {len(out['detail'])}, derivatives {len(out['derivatives'])}")


if __name__ == '__main__':
    main()
