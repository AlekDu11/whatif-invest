// Smoke test for api/chart.js exchange candles (GitHub Actions). node scripts/test_chart.js
const h = require('../api/chart.js');
const call = q => new Promise(ok => { const res = { setHeader() {}, end(b) { ok({ code: this.statusCode, j: JSON.parse(b) }) } }; h({ query: q, headers: {} }, res) });
(async () => {
  for (const s of ['x:binance:BTC', 'x:gate:DIGI', 'x:mexc:CHOP', 'x:okx:OKB', 'x:bybit:MNT', 'x:gate:TENSET', 'D05.SI', '7203.T']) for (const r of ['5y', 'max']) {
    const t = Date.now(), x = await call({ s, r }); const d = x.j.d || [];
    console.log(s.padEnd(14), r, x.code, d.length, Date.now() - t + 'ms', JSON.stringify(d[d.length - 1] || x.j));
  }
})();
