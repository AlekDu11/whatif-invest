"""Trading pairs straight from the exchanges' own public market-data APIs (no keys, no sign-up).

CoinGecko's /exchanges/{id} returns at most 100 tickers and often nothing at all for the biggest venues (Binance),
so for the largest exchanges we read every spot pair from the exchange itself and keep the 100 biggest by USD volume.
Each entry: b (base), q (quote), cg (CoinGecko id of the base, when we list the coin), last, usd (24h volume in USD),
spread (% between best bid and ask). Exchange ids are CoinGecko's.
"""
import json, os, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STABLE = {'USDT', 'USDC', 'FDUSD', 'TUSD', 'DAI', 'USD1', 'USDE', 'PYUSD', 'RLUSD', 'BUSD', 'USDD', 'USD', 'USDS', 'USDG'}
# quote currencies for exchanges that glue the symbol together (BTCUSDT): longest first
QUOTES = sorted(STABLE | {'BTC', 'ETH', 'BNB', 'EUR', 'TRY', 'BRL', 'JPY', 'GBP', 'AUD', 'PLN', 'UAH', 'RUB', 'ARS', 'MXN', 'ZAR',
                          'IDR', 'SOL', 'XRP', 'DOGE', 'TRX', 'KRW', 'COP', 'CZK', 'RON'}, key=len, reverse=True)


def _get(u, timeout=40):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'whatifstack.com data bot', 'Accept': 'application/json'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except Exception as e:
        print(f'  {u}: {e}', flush=True)
        return None


def _f(v):
    try:
        v = float(v)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def _split(sym):
    for q in QUOTES:
        if sym.endswith(q) and len(sym) > len(q):
            return sym[:-len(q)], q
    return None, None


STOCKS = set()


def _ctx():
    """USD value of a quote currency (stablecoins 1, fiat from fx.json, coins from market.json) + symbol -> CoinGecko id."""
    usd, cg = {s: 1.0 for s in STABLE}, {}
    try:
        for c, r in json.load(open(os.path.join(ROOT, 'data/fx.json')))['rates'].items():
            if r:
                usd.setdefault(c, 1 / r)
    except Exception:
        pass
    try:
        A = json.load(open(os.path.join(ROOT, 'data/market.json')))['assets']
        STOCKS.update((a.get('tk') or '').upper() for a in A.values() if a.get('cat') in ('stock', 'etf'))
        for a in sorted((a for a in A.values() if a.get('cat') == 'crypto'), key=lambda a: -(a.get('rank') or 99999)):
            tk = (a.get('tk') or '').upper()   # the best-ranked coin wins a shared ticker (sorted worst first, overwritten)
            if a.get('price') and tk not in STABLE:
                usd[tk] = a['price']
            if a.get('cgid'):
                cg[tk] = a['cgid']
    except Exception:
        pass
    return usd, cg


def _row(b, q, last, qvol, bid, ask, usd, cg):
    b, q = (b or '').upper(), (q or '').upper()
    if b.startswith('R') and len(b) > 2 and b[1:] in STOCKS:   # Bitget's tokenized US stocks (RNVDA, RSPY...) are not crypto
        return None
    if b.endswith('B') and len(b) > 2 and b[:-1] in STOCKS:     # Binance's tokenized stocks (NVDAB, SOXLB...)
        return None
    last, qvol, bid, ask = _f(last), _f(qvol), _f(bid), _f(ask)
    if not b or not q or not last or not qvol or q not in usd:
        return None
    r = {'b': b, 'q': q, 'last': round(last, 10), 'usd': round(qvol * usd[q], 2)}
    if cg.get(b):
        r['cg'] = cg[b]
    if bid and ask and ask >= bid > 0:
        r['spread'] = round((ask - bid) / ask * 100, 4)
    return r


def binance(usd, cg):   # data-api.binance.vision = Binance's public market-data mirror (also reachable from US servers)
    d = _get('https://data-api.binance.vision/api/v3/ticker/24hr') or []
    return [_row(*_split(t['symbol']), t.get('lastPrice'), t.get('quoteVolume'), t.get('bidPrice'), t.get('askPrice'), usd, cg) for t in d if t.get('count')]


def mexc(usd, cg):
    d = _get('https://api.mexc.com/api/v3/ticker/24hr') or []
    return [_row(*_split(t['symbol']), t.get('lastPrice'), t.get('quoteVolume'), t.get('bidPrice'), t.get('askPrice'), usd, cg) for t in d]


def okx(usd, cg):
    d = (_get('https://www.okx.com/api/v5/market/tickers?instType=SPOT') or {}).get('data') or []
    out = []
    for t in d:
        b, q = (t.get('instId') or '-').split('-')[:2]
        out.append(_row(b, q, t.get('last'), t.get('volCcy24h'), t.get('bidPx'), t.get('askPx'), usd, cg))
    return out


def gate(usd, cg):
    d = _get('https://api.gateio.ws/api/v4/spot/tickers') or []
    out = []
    for t in d:
        b, _, q = (t.get('currency_pair') or '').partition('_')
        out.append(_row(b, q, t.get('last'), t.get('quote_volume'), t.get('highest_bid'), t.get('lowest_ask'), usd, cg))
    return out


def kucoin(usd, cg):
    d = ((_get('https://api.kucoin.com/api/v1/market/allTickers') or {}).get('data') or {}).get('ticker') or []
    out = []
    for t in d:
        b, _, q = (t.get('symbol') or '').partition('-')
        out.append(_row(b, q, t.get('last'), t.get('volValue'), t.get('buy'), t.get('sell'), usd, cg))
    return out


def bitget(usd, cg):
    d = (_get('https://api.bitget.com/api/v2/spot/market/tickers') or {}).get('data') or []
    # usdtVolume = 24h turnover in USDT; quoteVolume comes back inflated for tokenized-stock pairs (RNVDA...)
    return [_row(*_split(t.get('symbol') or ''), t.get('lastPr'), t.get('usdtVolume'), t.get('bidPr'), t.get('askPr'), usd, cg)
            if _split(t.get('symbol') or '')[1] in ('USDT', 'USDC') else None for t in d]


def bybit(usd, cg):
    d = ((_get('https://api.bybit.com/v5/market/tickers?category=spot') or {}).get('result') or {}).get('list') or []
    return [_row(*_split(t.get('symbol') or ''), t.get('lastPrice'), t.get('turnover24h'), t.get('bid1Price'), t.get('ask1Price'), usd, cg) for t in d]


SOURCES = {'binance': binance, 'okex': okx, 'gate': gate, 'kucoin': kucoin, 'mxc': mexc, 'bitget': bitget, 'bybit_spot': bybit}


def fetch_all():
    """{exchange id: {'pairs': top 100 by USD volume, 'n_pairs': active pairs, 'n_coins': listed coins, 'vol_usd': total}}"""
    usd, cg = _ctx()
    res = {}
    for xid, fn in SOURCES.items():
        try:
            rows = [r for r in fn(usd, cg) if r and r['usd'] > 0]
        except Exception as e:
            print(f'  {xid}: {e}', flush=True)
            rows = []
        if len(rows) < 20:   # blocked or broken answer: keep CoinGecko's data
            print(f'  {xid}: direct API gave {len(rows)} pairs — skipped', flush=True)
            continue
        rows.sort(key=lambda r: -r['usd'])
        res[xid] = {'pairs': rows[:100], 'n_pairs': len(rows), 'n_coins': len({r['b'] for r in rows}),
                    'vol_usd': round(sum(r['usd'] for r in rows))}
        print(f'  {xid}: {len(rows)} pairs from its own API', flush=True)
    return res


if __name__ == '__main__':
    r = fetch_all()
    print({k: (v['n_pairs'], v['pairs'][:2]) for k, v in r.items()})
