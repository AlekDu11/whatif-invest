// Live quotes for stocks, ETFs and futures (crypto is live via the Binance stream): GET /api/quote?s=SPY,QQQ,GC=F
// Yahoo chart endpoint (1-day range): last price + previous close. Up to 25 symbols, CDN-cached for 60 s.
const G = require('./_guard');
async function one(s) {
  for (const h of ['query1', 'query2']) {
    try {
      const y = await fetch(`https://${h}.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=1d&interval=5m&includePrePost=false`,
        { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack quote)', Accept: 'application/json' } });
      if (!y.ok) continue;
      const m = ((((await y.json()).chart || {}).result || [])[0] || {}).meta || {};
      const p = m.regularMarketPrice, pc = m.chartPreviousClose || m.previousClose;
      if (p == null) continue;
      return { p: +p.toPrecision(8), c: pc ? +(p / pc - 1).toFixed(5) : null, t: m.regularMarketTime || null, cur: m.currency || 'USD' };
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
  return send(200, out, 'public, s-maxage=60, stale-while-revalidate=300');
};
