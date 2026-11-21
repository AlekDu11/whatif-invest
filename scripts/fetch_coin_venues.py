"""Where can we get a live quote and a TradingView chart for coins that are on none of the exchanges fetch_data.py reads?
(owner 2026-11-21: no home-made charts — find the exchange the coin trades on, take its quote by API and its TradingView chart.)

For crypto assets in data/market.json with src «coingecko» or «cg-spot» (no Binance/Gate/MEXC/OKX/Bybit pair):
  1. KuCoin, Bitget, HTX, BingX — one «all tickers» call each; a BASE/USDT pair whose price is within 3x of CoinGecko's counts
     (the same ticker can be a different coin) → venue {"x": "kucoin|bitget|htx|bingx", "s": "<exchange symbol>"}.
  2. Otherwise the coin is DEX-only: its contract from CoinGecko /coins/{id} → the most liquid pool on GeckoTerminal
     → venue {"dex": [network, pool]} (GeckoTerminal's TradingView-based chart; price from /api/chart?dex=pool).
Result: data/coin_venues.json {cgid: {..., "t": "YYYY-MM-DD"}}; rechecked after 14 days. stdlib only.
Usage: python3 scripts/fetch_coin_venues.py [max coins per run, default 120]
"""
import datetime, json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'coin_venues.json')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 120
UA = {'User-Agent': 'whatifstack.com data bot', 'Accept': 'application/json'}
# CoinGecko asset platform -> GeckoTerminal network id
NET = {'solana': 'solana', 'ethereum': 'eth', 'binance-smart-chain': 'bsc', 'base': 'base', 'arbitrum-one': 'arbitrum',
       'polygon-pos': 'polygon_pos', 'avalanche': 'avax', 'tron': 'tron', 'sui': 'sui-network', 'the-open-network': 'ton',
       'optimistic-ethereum': 'optimism', 'sonic': 'sonic', 'berachain': 'berachain', 'hyperevm': 'hyperevm', 'linea': 'linea',
       'zksync': 'zksync', 'blast': 'blast', 'mantle': 'mantle', 'aptos': 'aptos', 'near-protocol': 'near', 'cronos': 'cro', 'abstract': 'abstract'}


def get(url, timeout=30):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return json.load(r)
    except Exception as e:
        print('  GET failed', url.split('?')[0], e, flush=True)
        return None


def cex_tickers():
    """{exchange: {BASE: (price, symbol)}} for USDT pairs."""
    out = {}
    d = get('https://api.kucoin.com/api/v1/market/allTickers')
    out['kucoin'] = {t['symbol'][:-5]: (float(t['last']), t['symbol']) for t in ((d or {}).get('data') or {}).get('ticker') or []
                     if t.get('symbol', '').endswith('-USDT') and t.get('last')}
    d = get('https://api.bitget.com/api/v2/spot/market/tickers')
    out['bitget'] = {t['symbol'][:-4]: (float(t['lastPr']), t['symbol']) for t in (d or {}).get('data') or []
                     if t.get('symbol', '').endswith('USDT') and t.get('lastPr')}
    d = get('https://api.huobi.pro/market/tickers')
    out['htx'] = {t['symbol'][:-4].upper(): (float(t['close']), t['symbol']) for t in (d or {}).get('data') or []
                  if t.get('symbol', '').endswith('usdt') and t.get('close')}
    d = get('https://open-api.bingx.com/openApi/spot/v1/ticker/24hr?timestamp=%d' % int(time.time() * 1000))
    out['bingx'] = {t['symbol'][:-5]: (float(t['lastPrice']), t['symbol']) for t in (d or {}).get('data') or []
                    if t.get('symbol', '').endswith('-USDT') and t.get('lastPrice')}
    print('CEX pairs:', {k: len(v) for k, v in out.items()}, flush=True)
    return out


def dex_pool(cgid):
    d = get(f'https://api.coingecko.com/api/v3/coins/{cgid}?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false')
    time.sleep(6)   # CoinGecko keyless rate limit
    plats = (d or {}).get('platforms') or {}
    for plat, addr in plats.items():
        net = NET.get(plat)
        if not net or not addr:
            continue
        g = get(f'https://api.geckoterminal.com/api/v2/networks/{net}/tokens/{addr}/pools?page=1')
        time.sleep(2.5)   # GeckoTerminal ~30 calls/min
        pools = (g or {}).get('data') or []
        best = max(pools, key=lambda p: float((p.get('attributes') or {}).get('reserve_in_usd') or 0), default=None)
        if best and float(best['attributes'].get('reserve_in_usd') or 0) >= 5000:
            return [net, best['attributes']['address']]
    return None


def main():
    market = json.load(open(os.path.join(ROOT, 'data', 'market.json'), encoding='utf-8'))['assets']
    try:
        V = json.load(open(OUT, encoding='utf-8'))
    except Exception:
        V = {}
    today = datetime.date.today()
    fresh = lambda v: v and (today - datetime.date.fromisoformat(v.get('t', '2000-01-01'))).days < 14
    todo = [a for a in sorted(market.values(), key=lambda a: a.get('rank') or 99999)
            if a.get('cat') == 'crypto' and a.get('src') in ('coingecko', 'cg-spot') and a.get('cgid') and not fresh(V.get(a['cgid']))][:N]
    print('coins to check:', len(todo), flush=True)
    if not todo:
        return
    T = cex_tickers()
    n_cex = n_dex = 0
    for a in todo:
        base, cg, px = a['tk'].upper(), a['cgid'], (a.get('p') or [None])[-1]
        v = None
        for ex in ('kucoin', 'bitget', 'htx', 'bingx'):
            hit = T.get(ex, {}).get(base)
            if hit and px and px / 3 < hit[0] < px * 3:
                v = {'x': ex, 's': hit[1]}
                n_cex += 1
                break
        if not v:
            pool = dex_pool(cg)
            if pool:
                v = {'dex': pool}
                n_dex += 1
        V[cg] = dict(v or {}, t=today.isoformat())
    json.dump(V, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    print(f'venues: {n_cex} on KuCoin/Bitget/HTX/BingX, {n_dex} DEX pools, {len(todo) - n_cex - n_dex} not found', flush=True)


if __name__ == '__main__':
    main()
