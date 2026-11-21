// Live quotes for stocks, ETFs and futures (crypto is live via the Binance stream): GET /api/quote?s=SPY,QQQ,GC=F
// Yahoo chart endpoint (1-day range, 1-minute bars incl. pre-/post-market): latest trade + previous close.
// Outside regular US hours the price is the pre-/after-market trade (x: 1). Up to 25 symbols, CDN-cached for 30 s.
const G = require('./_guard');
async function one(s) {
  for (const h of ['query1', 'query2']) {
    try {
      const y = await fetch(`https://${h}.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=1d&interval=1m&includePrePost=true`,
        { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack quote)', Accept: 'application/json' } });
      if (!y.ok) continue;
      const r = (((await y.json()).chart || {}).result || [])[0] || {}, m = r.meta || {};
      let p = m.regularMarketPrice, t = m.regularMarketTime || null, x = 0;
      const pc = m.chartPreviousClose || m.previousClose;
      // newest 1-minute bar: if it is later than the last regular trade, it is a pre-/after-market price
      const ts = r.timestamp || [], cl = ((((r.indicators || {}).quote || [])[0] || {}).close) || [];
      for (let i = ts.length - 1; i >= 0; i--) { if (cl[i] != null) { if (ts[i] > (t || 0) + 60) { p = cl[i]; t = ts[i]; x = 1 } break } }
      if (p == null) continue;
      const ch = pc ? +(p / pc - 1).toFixed(5) : null;
      if (m.currency === 'USX') p /= 100;   // grains, sugar, coffee, cattle are quoted in US cents -> dollars, as on our pages
      return { p: +p.toPrecision(8), c: ch, t, x, cur: m.currency === 'USX' ? 'USD' : (m.currency || 'USD') };
    } catch (e) { /* next host */ }
  }
  return null;
}
// Home «Today in the markets» between deploys: GET /api/quote?mv=1&s=<our biggest US stocks> → live crypto movers (CoinGecko top 250),
// trending coins and the stocks' day change (Yahoo spark, 20 symbols per call). One CDN-cached answer (5 min) for every visitor.
const UA = { 'User-Agent': 'Mozilla/5.0 (WhatIfStack movers)', Accept: 'application/json' };
async function j(u) { try { const r = await fetch(u, { headers: UA }); return r.ok ? await r.json() : null } catch (e) { return null } }
async function spark(list) {
  const out = {};
  for (let i = 0; i < list.length; i += 20) {
    const part = list.slice(i, i + 20).join(',');
    let d = null;
    for (const h of ['query1', 'query2']) { d = await j(`https://${h}.finance.yahoo.com/v7/finance/spark?symbols=${encodeURIComponent(part)}&range=1d&interval=1d`); if (d) break }
    for (const r of (((d || {}).spark || {}).result || [])) {
      const m = ((r.response || [])[0] || {}).meta || {};
      const p = m.regularMarketPrice, pc = m.chartPreviousClose || m.previousClose;
      if (p != null && pc) out[r.symbol] = [+p.toPrecision(8), +(p / pc - 1).toFixed(5)];
    }
  }
  if (!Object.keys(out).length) {   // spark unavailable: the chart endpoint for the 40 biggest
    await Promise.all(list.slice(0, 40).map(async s => { const q = await one(s); if (q && q.cur === 'USD' && q.c != null) out[s] = [q.p, q.c] }));
  }
  return out;
}
async function movers(req, send) {
  const list = String((req.query || {}).s || '').split(',').map(x => x.trim()).filter(x => /^[A-Z0-9\-]{1,10}$/i.test(x)).slice(0, 160);
  const [cg, tr, st] = await Promise.all([
    j('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&price_change_percentage=24h'),
    j('https://api.coingecko.com/api/v3/search/trending'),
    list.length ? spark(list) : {}]);
  const c = (Array.isArray(cg) ? cg : []).filter(x => x.current_price != null && x.price_change_percentage_24h != null)
    .map(x => [String(x.symbol || '').toUpperCase(), x.id, +(+x.current_price).toPrecision(8), +(x.price_change_percentage_24h / 100).toFixed(5), Math.round(x.market_cap || 0)]);
  const t = (((tr || {}).coins) || []).map(x => x.item || {}).map(x => [String(x.symbol || '').toUpperCase(), x.id, (((x.data || {}).price_change_percentage_24h || {}).usd ?? null)]).slice(0, 15);
  if (!c.length && !Object.keys(st).length) return send(502, { e: 'upstream' }, 'public, s-maxage=30');
  return send(200, { at: Date.now(), c, t, s: st }, 'public, s-maxage=300, stale-while-revalidate=600, stale-if-error=3600');
}
module.exports = async (req, res) => {
  const send = (code, obj, cache) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('Cache-Control', cache || 'no-store'); res.end(JSON.stringify(obj)) };
  if (G.over(req, 30, 'quote')) return send(429, { e: 'limit' });
  if ((req.query || {}).mv) return movers(req, send);
  if ((req.query || {}).mx) {   // live prices of coins traded on MEXC (its WebSocket is protobuf-only): one ticker call, CDN 15 s
    const want = new Set(String(req.query.mx).toUpperCase().split(',').filter(x => /^[A-Z0-9]{1,15}$/.test(x)).slice(0, 60).map(x => x + 'USDT'));
    const d = await j('https://api.mexc.com/api/v3/ticker/24hr');
    if (!Array.isArray(d)) return send(502, { e: 'upstream' }, 'public, s-maxage=10');
    const out = {};
    for (const t of d) if (want.has(t.symbol) && +t.lastPrice > 0) out[t.symbol.slice(0, -4)] = [+t.lastPrice, +t.openPrice > 0 ? +(t.lastPrice / t.openPrice - 1).toFixed(5) : null];
    return send(200, out, 'public, s-maxage=15, stale-while-revalidate=60');
  }
  const list = String((req.query || {}).s || '').split(',').map(x => x.trim()).filter(x => /^[A-Z0-9.\-=^]{1,20}$/i.test(x)).slice(0, 25);
  if (!list.length) return send(400, { e: 'symbols' });
  const out = {};
  await Promise.all(list.map(async s => { const q = await one(s); if (q && q.cur === 'USD') out[s] = q }));
  return send(200, out, 'public, s-maxage=30, stale-while-revalidate=120');
};
