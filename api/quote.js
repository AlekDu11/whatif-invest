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
module.exports = async (req, res) => {
  const send = (code, obj, cache) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('Cache-Control', cache || 'no-store'); res.end(JSON.stringify(obj)) };
  if (G.over(req, 30, 'quote')) return send(429, { e: 'limit' });
  const list = String((req.query || {}).s || '').split(',').map(x => x.trim()).filter(x => /^[A-Z0-9.\-=^]{1,20}$/i.test(x)).slice(0, 25);
  if (!list.length) return send(400, { e: 'symbols' });
  const out = {};
  await Promise.all(list.map(async s => { const q = await one(s); if (q && q.cur === 'USD') out[s] = q }));
  return send(200, out, 'public, s-maxage=30, stale-while-revalidate=120');
};
