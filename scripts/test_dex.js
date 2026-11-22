// Smoke test for api/_dex.js (runs in GitHub Actions: the sandbox can't reach Binance). node scripts/test_dex.js
const h = require('../api/_dex.js');
const call = q => new Promise(ok => { const res = { h: {}, setHeader(k, v) { this.h[k] = v }, end(b) { ok({ code: this.statusCode, j: JSON.parse(b) }) } }; h({ query: q }, res) });
(async () => {
  { const t = Date.now(), r = await call({ dex: 'picks' }); const d = r.j.d || []; console.log('picks', r.code, d.length, Date.now() - t + 'ms', d.map(x => `${x.s}/${x.n} t10=${Math.round(x.t10)} h=${x.h} liq=${Math.round(x.liq)} hype=${x.hv || 0}`).join(' | '), JSON.stringify(d[0] || {}).slice(0, 600)); }
  for (const v of ['trend', 'vol', 'new', 'soon', 'done']) for (const n of ['all', 'solana', 'bsc']) {
    const t = Date.now(), r = await call({ dex: v, n }); const d = r.j.d || [];
    console.log(v.padEnd(5), n.padEnd(6), r.code, d.length, (d[0] || {}).src || 'gt', Date.now() - t + 'ms', d.slice(0, 3).map(x => `${x.s} mc=${Math.round(x.mc || 0)} prog=${x.prog ?? ''}`).join(' | '));
  }
  const r = await call({ dex: 'trend', n: 'solana' }); const a = ((r.j.d || [])[0] || {}).a;
  if (a) { const p = await call({ dex: 'pool', n: 'solana', a }); for (const i of ['1m','15m','1d']) { const k = await call({ dex: 'kline', n: 'solana', a, i }); console.log('kline', i, k.code, (k.j.d||[]).length, JSON.stringify((k.j.d||[]).slice(-1)), k.j.e||''); }
    console.log('pool by a', p.code, p.j.s, p.j.p, JSON.stringify(p.j.risk)); }
})();
