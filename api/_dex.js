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

async function list(view, n) {
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

async function pool(n, p) {
  const d = await get(`${GT}/${n}/pools/${p}?include=base_token`);
  const r = norm({ data: [d.data], included: d.included })[0];
  if (!r) throw new Error('no pool');
  try {
    const i = (await get(`${GT}/${n}/tokens/${r.a}/info`)).data.attributes || {};
    r.info = { d: String(i.description || '').slice(0, 1200), web: (i.websites || []).slice(0, 2), x: i.twitter_handle || '', tg: i.telegram_handle || '', img: i.image_url || '' };
  } catch (e) { r.info = null; }
  return r;
}

module.exports = async (req, res) => {
  const q = req.query || {};
  const send = (code, obj, cache) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8'); res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Cache-Control', 'public, max-age=30'); res.setHeader('CDN-Cache-Control', cache); res.end(JSON.stringify(obj)); };
  const n = String(q.n || 'all');
  if (n !== 'all' && !NETS.includes(n) && !/^[a-z0-9_-]{2,30}$/.test(n)) return send(400, { e: 'network' }, 'no-store');
  try {
    if (q.dex === 'pool') {
      if (n === 'all' || !ADDR.test(String(q.p || ''))) return send(400, { e: 'pool' }, 'no-store');
      return send(200, await pool(n, String(q.p)), 'public, s-maxage=60, stale-while-revalidate=600, stale-if-error=3600');
    }
    const view = ['trend', 'vol', 'new'].includes(q.dex) ? q.dex : 'trend';
    return send(200, { t: Date.now(), d: await list(view, n) }, 'public, s-maxage=90, stale-while-revalidate=900, stale-if-error=3600');
  } catch (e) {
    return send(502, { e: 'upstream' }, 'no-store');
  }
};
