// DEX memecoin data for /memes/ and /memes/token/: GET /api/chart?dex=<view>&n=<network>  or  /api/chart?dex=pool&n=<network>&p=<pool address>
// One server fetch from GeckoTerminal's keyless API serves every visitor (CDN cache), so visitors never hit GeckoTerminal's per-IP limit.
// Views: trend (trending pools), vol (top 24h volume), new (new pairs). Networks: all, solana, base, bsc, eth, ton.
const GT = 'https://api.geckoterminal.com/api/v2/networks';
const NETS = ['solana', 'base', 'bsc', 'eth', 'ton'];
const ADDR = /^[A-Za-z0-9_:\-]{20,80}$/;

const get = async u => {
  for (let i = 0; i < 2; i++) {
    const r = await fetch(u, { headers: { Accept: 'application/json;version=20230302', 'User-Agent': 'WhatIfStack (whatifstack.com)' } });
    if (r.ok) return r.json();
    if (r.status !== 429) throw new Error('gt ' + r.status);
    await new Promise(z => setTimeout(z, 1200));
  }
  throw new Error('gt 429');
};

function norm(d) {
  const toks = {};
  (d.included || []).forEach(x => { if (x.type === 'token') toks[x.id] = x.attributes || {}; });
  return (d.data || []).map(p => {
    const a = p.attributes || {}, pc = a.price_change_percentage || {}, tx = (a.transactions || {}).h24 || {};
    const bt = toks[((p.relationships || {}).base_token || {}).data && p.relationships.base_token.data.id] || {};
    const num = v => (v == null || v === '' ? null : +v);
    return {
      n: String(p.id || '').split('_')[0], p: a.address, a: bt.address || '', s: bt.symbol || String(a.name || '').split(' / ')[0], nm: bt.name || '',
      img: bt.image_url && bt.image_url !== 'missing.png' ? bt.image_url : '', pr: num(a.base_token_price_usd), mc: num(a.market_cap_usd) || num(a.fdv_usd),
      fdv: num(a.fdv_usd), c5: num(pc.m5), c1: num(pc.h1), c6: num(pc.h6), c24: num(pc.h24), liq: num(a.reserve_in_usd), vol: num((a.volume_usd || {}).h24),
      tx: (tx.buys || 0) + (tx.sells || 0), at: a.pool_created_at, q: String(a.name || '').split(' / ')[1] || '',
    };
  }).filter(r => r.s && r.p);
}

// ---- Binance Web3 public market data (owner 2026-11-22): faster and richer than GeckoTerminal for Solana / BNB Chain / Base.
// Trending / gainers / volume = unified rank; new / soon / done = Meme Rush launchpad lifecycle (bonding curve → about to migrate → on DEX).
const BN = 'https://web3.binance.com/bapi/defi';
const BNC = { solana: 'CT_501', bsc: '56', base: '8453' };
const BNN = { CT_501: 'solana', 56: 'bsc', 8453: 'base' };
const SKIP = new Set(['SOL', 'WSOL', 'ETH', 'WETH', 'BTC', 'WBTC', 'CBBTC', 'BNB', 'WBNB', 'USDC', 'USDT', 'USD1', 'DAI', 'FDUSD', 'USDE', 'PYUSD', 'JITOSOL', 'MSOL', 'STETH', 'CBETH', 'ZEC', 'HYPE', 'HSOL', 'BNSOL', 'JUPSOL', 'XRP', 'DOGE', 'ADA', 'TRX', 'SUI', 'LINK', 'LTC', 'BCH', 'TON', 'AVAX', 'DOT', 'XLM', 'USDS', 'USDG', 'RAY', 'JUP', 'ORCA', 'JTO', 'PYTH', 'CAKE', 'AERO', 'DRIFT', 'KMNO', 'MOOLAH', 'XVS', 'TWT']);
// look-alike tickers (Armenian / Cherokee / Lisu letters posing as USDT etc.) are scam clones
const FAKE = /[\u0530-\u058F\u13A0-\u13FF\uA4D0-\uA4FF\u2160-\u218F]/;
const bnPost = async (path, body) => {
  const r = await fetch(BN + path, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept-Encoding': 'identity', 'User-Agent': 'binance-web3/1.1 (Skill)' }, body: JSON.stringify(body) });
  if (!r.ok) throw new Error('bn ' + r.status);
  const j = await r.json();
  if (j.code !== '000000') throw new Error('bn ' + j.code);
  return j.data;
};
const icon = v => !v ? '' : /^https?:/.test(v) ? v : 'https://bin.bnbstatic.com' + v;
const num = v => (v == null || v === '' ? null : +v);
const iso = ms => (ms ? new Date(+ms).toISOString() : null);
const stockish = t => { const tg = t.tokenTag || {}; return Object.keys(tg).some(k => /stock/i.test(k)) || /securities|tokenized/i.test(((t.metaInfo || {}).name) || '') };
function bnUnified(t) {
  return { n: BNN[t.chainId] || t.chainId, p: '', a: t.contractAddress, s: t.symbol, nm: (t.metaInfo || {}).name || t.symbol, img: icon(t.icon), pr: num(t.price),
    mc: num(t.marketCap), c5: num(t.percentChange5m), c1: num(t.percentChange1h), c6: null, c24: num(t.percentChange24h), liq: num(t.liquidity), vol: num(t.volume24h),
    tx: num(t.count24h), at: iso(t.launchTime || (t.metaInfo || {}).createTime), h: num(t.holders), t10: num(t.holdersTop10Percent), risk: (t.auditInfo || {}).riskLevel, src: 'bn' };
}
function bnRush(t) {
  return { n: BNN[t.chainId] || t.chainId, p: '', a: t.contractAddress, s: t.symbol, nm: t.name || t.symbol, img: icon(t.icon), pr: num(t.price), mc: num(t.marketCap),
    c5: null, c1: null, c6: null, c24: num(t.priceChange), liq: num(t.liquidity), vol: num(t.volume), tx: num(t.count), at: iso(t.migrateTime || t.createTime),
    h: num(t.holders), t10: num(t.holdersTop10Percent), dev: num(t.holdersDevPercent), ins: num(t.holdersInsiderPercent), snp: num(t.holdersSniperPercent),
    prog: num(t.progress), src: 'bn' };
}
async function bnList(view, n) {
  const chains = n === 'all' ? ['CT_501', '56', '8453'] : [BNC[n]];
  const rush = { new: 10, soon: 20, done: 30 }[view];
  const out = [];
  await Promise.all(chains.map(async c => {
    try {
      if (rush) {
        if (c === '8453') return;   // Meme Rush covers Solana + BNB Chain launchpads
        const d = await bnPost('/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai', { chainId: c, rankType: rush, limit: 60 });
        out.push(...(d || []).map(bnRush));
      } else {
        const d = await bnPost('/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai',
          { rankType: 10, chainId: c, period: 50, sortBy: view === 'vol' ? 70 : 0, orderAsc: false, page: 1, size: 80 });
        out.push(...((d || {}).tokens || []).filter(t => !stockish(t)).map(bnUnified));
      }
    } catch (e) { /* other chains still count */ }
  }));
  const res = out.filter(r => r.s && r.a && !SKIP.has(String(r.s).toUpperCase()) && !FAKE.test(r.s));
  if (!res.length) throw new Error('bn empty');
  return res;
}
async function bnAudit(n, a) {
  const d = await bnPost('/v1/public/wallet-direct/security/token/audit', { binanceChainId: BNC[n], contractAddress: a, requestId: require('crypto').randomUUID() });
  if (!d || !d.hasResult || !d.isSupported) return null;
  const hits = [];
  (d.riskItems || []).forEach(it => (it.details || []).forEach(x => { if (x.isHit) hits.push(x.title) }));
  const ex = d.extraInfo || {};
  const lv = d.riskLevelEnum || (d.riskLevel == null ? null : d.riskLevel <= 1 ? 'LOW' : d.riskLevel <= 3 ? 'MEDIUM' : 'HIGH');
  return { lvl: lv, n: d.riskLevel, hits: hits.slice(0, 6), bt: ex.buyTax, st: ex.sellTax };
}

// candles for the token page chart (Binance Web3 kline service): [open, high, low, close, volume, ts_ms, count]
const KI = { '1m': '1min', '5m': '5min', '15m': '15min', '1h': '1h', '4h': '4h', '1d': '1d' };
// Official Binance Web3 API (owner's key, Market permission only): Vercel env BW3_KEY + BW3_SECRET. HMAC-SHA256 over
// timestamp + METHOD + '/build' + path + '?' + query (+ body), base64; headers X-OC-APIKEY / X-OC-TIMESTAMP / X-OC-SIGN.
const W3 = 'https://web3.binance.com/build';
async function w3get(path, params) {
  const key = process.env.BW3_KEY, sec = process.env.BW3_SECRET;
  if (!key || !sec) throw new Error('no key');
  const qs = new URLSearchParams(Object.entries(params).filter(([, v]) => v != null)).toString();
  const ts = new Date().toISOString();
  const sign = require('crypto').createHmac('sha256', sec).update(`${ts}GET/build${path}${qs ? '?' + qs : ''}`).digest('base64');
  const r = await fetch(`${W3}${path}${qs ? '?' + qs : ''}`, { headers: { 'X-OC-APIKEY': key, 'X-OC-TIMESTAMP': ts, 'X-OC-SIGN': sign, 'X-OC-RECV-WINDOW': '15000' } });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.code !== 0) throw new Error('w3 ' + r.status + ' ' + (j.code ?? '') + ' ' + (j.msg || ''));
  return j.data;
}
async function kline(n, a, i) {
  try {   // official Market API first, the public kline service as a fallback
    const d = await w3get('/api/v1/dex/market/candles', { binanceChainId: BNC[n], tokenContractAddress: a, bar: i, limit: 300 });
    const k = (d || []).map(c => [Math.floor(+c[5] / 1000), +c[0], +c[1], +c[2], +c[3], +c[4]]).filter(c => c[0] && isFinite(c[4]));
    if (k.length > 1) return k;
  } catch (e) { console.log('w3 candles', String(e.message || e)) }
  const r = await fetch(`https://dquery.sintral.io/u-kline/v1/k-line/candles?platform=${n === 'bsc' ? 'bsc' : n}&address=${encodeURIComponent(a)}&interval=${KI[i]}&limit=300&pm=p`,
    { headers: { 'Accept-Encoding': 'identity', 'User-Agent': 'binance-web3/1.1 (Skill)' } });
  if (!r.ok) throw new Error('kl ' + r.status);
  const j = await r.json(), d = Array.isArray(j) ? j : (j.data || []);
  return d.map(c => [Math.floor(+c[5] / 1000), +c[0], +c[1], +c[2], +c[3], +c[4]]).filter(c => c[0] && isFinite(c[4]));
}

// «Pick of the day» (owner 2026-11-22: Binance = the whole market, WhatIfStack = the quality filter).
// Trending lists of Solana / BNB Chain / Base → strict filter → social buzz from Binance's hype board → top 12.
const riskHigh = v => v != null && (/HIGH/i.test(String(v)) || (+v >= 4));
async function picks() {
  const chains = ['CT_501', '56', '8453'], rows = [], hype = {};
  await Promise.all(chains.map(async c => {
    try {
      const d = await bnPost('/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai',
        { rankType: 10, chainId: c, period: 50, sortBy: 70, orderAsc: false, page: 1, size: 200, liquidityMin: 50000, volumeMin: 100000 });
      ((d || {}).tokens || []).filter(t => !stockish(t)).forEach(t => rows.push(Object.assign(bnUnified(t), { rl: (t.auditInfo || {}).riskLevel })));
    } catch (e) { /* skip chain */ }
    try {
      const r = await fetch(`${BN}/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai?chainId=${c}&targetLanguage=en&timeRange=1`,
        { headers: { 'Accept-Encoding': 'identity', 'User-Agent': 'binance-web3/1.1 (Skill)' } });
      const j = await r.json();
      (((j.data || {}).leaderBoardList) || []).forEach(x => { const m = x.metaInfo || {}, h = x.socialHypeInfo || {};
        if (m.contractAddress) hype[String(m.contractAddress).toLowerCase()] = { b: h.socialSummaryBrief || '', s: h.sentiment || '', v: +h.socialHype || 0 } });
    } catch (e) { /* no buzz data */ }
  }));
  const day = 864e5, now = Date.now(), seen = new Set();
  const ok = rows.filter(r => {
    const k = String(r.a).toLowerCase(); if (seen.has(k)) return false; seen.add(k);
    const age = r.at ? now - Date.parse(r.at) : 0;
    return r.s && !SKIP.has(String(r.s).toUpperCase()) && !FAKE.test(r.s) && age >= day && (r.liq || 0) >= 50000 && (r.vol || 0) >= 100000
      && (r.h == null || r.h >= 500) && r.t10 != null && r.t10 <= 30 && !riskHigh(r.rl);
  });
  ok.forEach(r => { const h = hype[String(r.a).toLowerCase()]; if (h) { r.hb = h.b; r.hs = h.s; r.hv = h.v } delete r.rl; });
  ok.sort((a, b) => ((b.hv || 0) > 0) - ((a.hv || 0) > 0) || (b.hv || 0) - (a.hv || 0) || b.vol - a.vol);
  return ok.slice(0, 9);
}

async function list(view, n) {
  if ((n === 'all' || BNC[n]) && ['trend', 'vol', 'new', 'soon', 'done', 'gain'].includes(view)) {
    try { return await bnList(view === 'gain' ? 'trend' : view, n) } catch (e) { /* fall back to GeckoTerminal */ }
  }
  if (view === 'soon' || view === 'done') view = 'new';
  const nets = n === 'all' ? null : [n];
  const urls = [];
  if (view === 'vol') (nets || NETS.slice(0, 4)).forEach(x => urls.push(`${GT}/${x}/pools?sort=h24_volume_usd_desc&page=1&include=base_token`));
  else if (view === 'new') [1, 2].forEach(pg => urls.push(`${GT}/${nets ? nets[0] + '/' : ''}new_pools?page=${pg}&include=base_token`));
  else (nets ? [1, 2] : [1, 2, 3]).forEach(pg => urls.push(`${GT}/${nets ? nets[0] + '/' : ''}trending_pools?page=${pg}&include=base_token`));
  const out = [];
  for (const u of urls) { try { out.push(...norm(await get(u))); } catch (e) { /* keep what we have */ } }
  if (!out.length) throw new Error('empty');
  return out;
}

async function pool(n, p, a) {
  if (!p && a) {   // rows from Binance carry the token address: take its top pool on GeckoTerminal
    const t = await get(`${GT}/${n}/tokens/${a}/pools?page=1`);
    p = (((t.data || [])[0] || {}).attributes || {}).address;
    if (!p) throw new Error('no pool');
  }
  const d = await get(`${GT}/${n}/pools/${p}?include=base_token`);
  const r = norm({ data: [d.data], included: d.included })[0];
  if (!r) throw new Error('no pool');
  try {
    const i = (await get(`${GT}/${n}/tokens/${r.a}/info`)).data.attributes || {};
    r.info = { d: String(i.description || '').slice(0, 1200), web: (i.websites || []).slice(0, 2), x: i.twitter_handle || '', tg: i.telegram_handle || '', img: i.image_url || '' };
  } catch (e) { r.info = null; }
  if (BNC[n] && r.a) { try { r.risk = await bnAudit(n, r.a) } catch (e) { r.risk = null } }   // Binance security check (LOW / MEDIUM / HIGH)
  return r;
}

module.exports = async (req, res) => {
  if (req.query && req.query.w3test === process.env.ALERTS_KEY && process.env.ALERTS_KEY) {   // owner check: /api/chart?w3test=<ALERTS_KEY>
    let out; try { const d = await w3get('/api/v1/dex/market/supported/chain', {}); out = { ok: true, chains: (d || []).length } } catch (e) { out = { ok: false, e: String(e.message || e) } }
    res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store'); return res.end(JSON.stringify(out));
  }
  const q = req.query || {};
  const send = (code, obj, cache) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8'); res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Cache-Control', 'public, max-age=30'); res.setHeader('CDN-Cache-Control', cache); res.end(JSON.stringify(obj)); };
  const n = String(q.n || 'all');
  if (n !== 'all' && !NETS.includes(n) && !/^[a-z0-9_-]{2,30}$/.test(n)) return send(400, { e: 'network' }, 'no-store');
  try {
    if (q.dex === 'picks') return send(200, { t: Date.now(), d: await picks() }, 'public, s-maxage=300, stale-while-revalidate=1800, stale-if-error=86400');
    if (q.dex === 'kline') {
      const aa = String(q.a || ''), ii = KI[q.i] ? q.i : '15m';
      if (!BNC[n] || !ADDR.test(aa)) return send(400, { e: 'kline' }, 'no-store');
      return send(200, { i: ii, d: await kline(n, aa, ii) }, `public, s-maxage=${ii === '1m' ? 30 : 60}, stale-while-revalidate=300`);
    }
    if (q.dex === 'pool') {
      const pp = String(q.p || ''), aa = String(q.a || '');
      if (n === 'all' || !(ADDR.test(pp) || ADDR.test(aa))) return send(400, { e: 'pool' }, 'no-store');
      return send(200, await pool(n, ADDR.test(pp) ? pp : '', aa), 'public, s-maxage=60, stale-while-revalidate=600, stale-if-error=3600');
    }
    const view = ['trend', 'vol', 'new', 'soon', 'done'].includes(q.dex) ? q.dex : 'trend';
    return send(200, { t: Date.now(), d: await list(view, n) }, 'public, s-maxage=45, stale-while-revalidate=900, stale-if-error=3600');
  } catch (e) {
    return send(502, { e: 'upstream' }, 'no-store');
  }
};
