// Calls api/_dex.js like Vercel would, for the memes extras (listings, narr, pulse, hype). Run by probe.yml.
const h = require('../api/_dex.js');
const call = q => new Promise(ok => { const res = { statusCode: 200, setHeader() {}, end(b) { ok([this.statusCode, b]) } }; h({ query: q }, res) });
(async () => {
  for (const q of [{ dex: 'listings' }, { dex: 'narr' }, { dex: 'pulse' }, { dex: 'hype', n: 'solana' }]) {
    const [c, b] = await call(q); console.log(`\n## ${q.dex}: ${c}`); console.log(String(b).slice(0, 700));
  }
})();
