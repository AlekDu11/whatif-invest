// Daily/weekly OHLC for our own Lightweight Charts: GET /api/chart?s=<yahoo symbol>&r=5y|max
// Yahoo Finance chart endpoint, cached on Vercel's CDN for an hour.
const G = require('./_guard');
const DEX = require('./_dex');   // ?dex=… → DEX memecoin data (kept in this function: Hobby allows 12 functions)
module.exports = async (req, res) => {
  const q = req.query || {};
  if (q.dex) return DEX(req, res);
  if (G.over(req, 60, 'chart')) { res.statusCode = 429; res.setHeader('Retry-After', '60'); return res.end('{"e":"limit"}') }
  const s = String(q.s || '');
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
