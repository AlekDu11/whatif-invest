// Daily/weekly OHLC for our own Lightweight Charts: GET /api/chart?s=<yahoo symbol>&r=5y|max
// Yahoo Finance chart endpoint, cached on Vercel's CDN for an hour.
const G = require('./_guard');
const DEX = require('./_dex');   // ?dex=… → DEX memecoin data (kept in this function: Hobby allows 12 functions)
module.exports = async (req, res) => {
  const q = req.query || {};
  if (q.dex) return DEX(req, res);
  if (G.over(req, 60, 'chart')) { res.statusCode = 429; res.setHeader('Retry-After', '60'); return res.end('{"e":"limit"}') }
  const s = String(q.s || '');
  if (/^cg:[a-z0-9-]{1,80}$/.test(s)) {   // coins on no exchange we read: CoinGecko OHLC (365 days, 4-day candles), same shape as Yahoo
    try {
      const r = await fetch(`https://api.coingecko.com/api/v3/coins/${s.slice(3)}/ohlc?vs_currency=usd&days=365`, { headers: { Accept: 'application/json', 'User-Agent': 'Mozilla/5.0 (WhatIfStack chart)' } });
      const d = r.ok ? await r.json() : null;
      if (Array.isArray(d) && d.length > 1) {
        res.statusCode = 200; res.setHeader('Content-Type', 'application/json; charset=utf-8'); res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
        return res.end(JSON.stringify({ cur: 'USD', iv: '4d', d: d.map(x => [Math.round(x[0] / 1000), +(+x[1]).toPrecision(7), +(+x[2]).toPrecision(7), +(+x[3]).toPrecision(7), +(+x[4]).toPrecision(7)]) }));
      }
    } catch (e) { /* fall through */ }
    res.statusCode = 502; res.setHeader('Content-Type', 'application/json'); return res.end('{"e":"upstream"}');
  }
  // x:<exchange>:<TICKER> → that exchange's own daily (5y) / weekly (max) candles vs USDT (owner 2026-11-22: charts only from real exchange data)
  const xm = /^x:(binance|gate|mexc|okx|bybit):([A-Z0-9]{1,20})$/i.exec(s);
  if (xm) {
    const ex = xm[1].toLowerCase(), tk = xm[2].toUpperCase(), wk = q.r === 'max';
    const U = {
      binance: `https://data-api.binance.vision/api/v3/klines?symbol=${tk}USDT&interval=${wk ? '1w' : '1d'}&limit=1000`,
      mexc: `https://api.mexc.com/api/v3/klines?symbol=${tk}USDT&interval=${wk ? '1W' : '1d'}&limit=1000`,
      gate: `https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=${tk}_USDT&interval=${wk ? '7d' : '1d'}&limit=1000`,
      okx: `https://www.okx.com/api/v5/market/history-candles?instId=${tk}-USDT&bar=${wk ? '1W' : '1Dutc'}&limit=300`,
      bybit: `https://api.bybit.com/v5/market/kline?category=spot&symbol=${tk}USDT&interval=${wk ? 'W' : 'D'}&limit=1000`,
    }[ex];
    try {
      const r0 = await fetch(U, { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack chart)', Accept: 'application/json' } });
      const j = r0.ok ? await r0.json() : null;
      let rows = [];
      if (ex === 'binance' || ex === 'mexc') rows = (j || []).map(k => [Math.floor(+k[0] / 1000), +k[1], +k[2], +k[3], +k[4]]);
      else if (ex === 'gate') rows = (j || []).map(k => [+k[0], +k[5], +k[3], +k[4], +k[2]]);
      else if (ex === 'okx') rows = ((j || {}).data || []).map(k => [Math.floor(+k[0] / 1000), +k[1], +k[2], +k[3], +k[4]]);
      else if (ex === 'bybit') rows = (((j || {}).result || {}).list || []).map(k => [Math.floor(+k[0] / 1000), +k[1], +k[2], +k[3], +k[4]]);
      rows = rows.filter(k => k[0] && isFinite(k[4]) && k[4] > 0).sort((a, b) => a[0] - b[0]);
      if (rows.length > 1) {
        res.statusCode = 200; res.setHeader('Content-Type', 'application/json; charset=utf-8'); res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
        return res.end(JSON.stringify({ cur: 'USD', iv: wk ? '1wk' : '1d', src: ex, d: rows.map(k => [k[0], ...k.slice(1).map(v => +v.toPrecision(7))]) }));
      }
    } catch (e) { /* fall through */ }
    res.statusCode = 502; res.setHeader('Content-Type', 'application/json'); return res.end('{"e":"upstream"}');
  }
  const r = q.r === 'max' ? 'max' : '5y';
  const send = (code, obj, cache) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('Cache-Control', cache || 'no-store'); res.end(JSON.stringify(obj)) };
  if (!/^[A-Z0-9.\-=^]{1,20}$/i.test(s)) return send(400, { e: 'symbol' });
  const iv = r === 'max' ? '1wk' : '1d';
  for (const h of ['query1', 'query2']) {
    try {
      const y = await fetch(`https://${h}.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=${r}&interval=${iv}&includePrePost=false`,
        { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack chart)', Accept: 'application/json' } });
      if (!y.ok) continue;
      const j = await y.json();
      const c = ((j.chart || {}).result || [])[0];
      if (!c || !c.timestamp) continue;
      const k = (c.indicators.quote || [])[0] || {};
      let cur = (c.meta || {}).currency || 'USD';
      const f = cur === 'USX' ? 0.01 : 1;   // US cents (grains, softs, livestock) -> dollars
      if (f !== 1) cur = 'USD';
      const out = [];
      for (let i = 0; i < c.timestamp.length; i++) {
        const o = k.open[i], hi = k.high[i], lo = k.low[i], cl = k.close[i];
        if (cl == null || o == null || hi == null || lo == null) continue;
        out.push([c.timestamp[i], +(o * f).toPrecision(7), +(hi * f).toPrecision(7), +(lo * f).toPrecision(7), +(cl * f).toPrecision(7)]);
      }
      if (out.length < 2) continue;
      return send(200, { cur, iv, d: out }, 'public, s-maxage=3600, stale-while-revalidate=86400');
    } catch (e) { /* try the next host */ }
  }
  return send(502, { e: 'upstream' });
};
