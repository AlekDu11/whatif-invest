// Hyperliquid whale tracker (owner 2026-11-28): /trading/hyperliquid/ and /trading/ read GET /api/quote?hl=1,
// one trader: GET /api/quote?hl=u&a=0x… . Data = Hyperliquid's own public API (no key):
//   stats-data.hyperliquid.xyz/Mainnet/leaderboard (all traders, ~18 MB, cached 20 min per function instance)
//   api.hyperliquid.xyz/info clearinghouseState (open positions of one wallet), metaAndAssetCtxs (mark prices), userFills.
// Liquidations and big moves: each run compares the positions with the previous run (Upstash hl:prev) —
// a position that vanished while the mark price was at its liquidation price = liquidated. Events in Upstash list hl:ev.
const INFO = 'https://api.hyperliquid.xyz/info';
const LB_URL = 'https://stats-data.hyperliquid.xyz/Mainnet/leaderboard';
const KVU = () => (process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || '').replace(/\/$/, '');
const KVT = () => process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || '';
async function kv(cmds) {
  if (!KVU() || !KVT()) return null;
  try {
    const r = await fetch(KVU() + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + KVT(), 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
    return (await r.json()).map(x => x.result);
  } catch (e) { return null }
}
async function info(body) {
  for (let i = 0; i < 2; i++) {
    try {
      const r = await fetch(INFO, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      if (r.ok) return await r.json();
    } catch (e) { /* retry once */ }
  }
  return null;
}
const win = (r, k) => ((r.windowPerformances || []).find(x => x[0] === k) || [0, {}])[1] || {};
const n = x => (x == null || x === '' ? null : +x);
const r2 = x => (x == null ? null : +(+x).toPrecision(6));

let LB = null, LBT = 0;
async function leaderboard() {
  if (LB && Date.now() - LBT < 20 * 60e3) return LB;
  try {
    const j = await (await fetch(LB_URL)).json();
    LB = (j.leaderboardRows || []).map(r => ({ a: r.ethAddress, nm: r.displayName || null, av: +r.accountValue,
      d: n(win(r, 'day').pnl), w: n(win(r, 'week').pnl), m: n(win(r, 'month').pnl), t: n(win(r, 'allTime').pnl),
      rm: n(win(r, 'month').roi), vw: n(win(r, 'week').vlm) }));
    LBT = Date.now();
  } catch (e) { if (!LB) LB = [] }
  return LB;
}
function tracked(lb) {   // active big wallets: biggest accounts that traded this week + most active + best month
  const pick = new Map(), add = (arr, k) => arr.slice(0, k).forEach(r => pick.set(r.a, r));
  add(lb.filter(r => r.vw > 0).sort((a, b) => b.av - a.av), 120);
  add([...lb].sort((a, b) => (b.vw || 0) - (a.vw || 0)), 60);
  add([...lb].sort((a, b) => (b.m || 0) - (a.m || 0)), 40);
  add([...lb].sort((a, b) => (b.d || 0) - (a.d || 0)), 20);
  return [...pick.values()];
}
async function marks() {
  const m = await info({ type: 'metaAndAssetCtxs' });
  const out = {};
  if (Array.isArray(m)) m[0].universe.forEach((u, i) => { const c = m[1][i] || {}; out[u.name] = { p: n(c.markPx), pd: n(c.prevDayPx), oi: n(c.openInterest), f: n(c.funding), v: n(c.dayNtlVlm) } });
  return out;
}
function posOf(st, mk) {
  return ((st || {}).assetPositions || []).map(x => x.position).filter(p => p && +p.szi).map(p => {
    const mark = (mk[p.coin] || {}).p, liq = n(p.liquidationPx), long = +p.szi > 0;
    const dist = liq && mark ? (long ? (mark - liq) / mark : (liq - mark) / mark) : null;
    return { c: p.coin, s: long ? 'L' : 'S', sz: Math.abs(+p.szi), ntl: Math.round(+p.positionValue), e: r2(p.entryPx), mk: r2(mark),
      u: Math.round(+p.unrealizedPnl), roe: r2(p.returnOnEquity), liq: liq && liq > 0 ? r2(liq) : null, lev: (p.leverage || {}).value || null,
      dist: dist == null || dist < 0 ? null : +dist.toFixed(4) };
  });
}
async function snapshot() {
  const [lb, mk] = await Promise.all([leaderboard(), marks()]);
  const rows = tracked(lb), states = [];
  for (let i = 0; i < rows.length; i += 30) states.push(...await Promise.all(rows.slice(i, i + 30).map(r => info({ type: 'clearinghouseState', user: r.a }))));
  const pos = [], tr = [], cur = {};
  states.forEach((st, i) => {
    if (!st) return;
    const r = rows[i], ps = posOf(st, mk), av = n((st.marginSummary || {}).accountValue);
    let ntl = 0;
    for (const p of ps) { ntl += p.ntl; pos.push({ a: r.a, nm: r.nm, ...p }); cur[r.a + '|' + p.c] = [p.s, p.ntl, p.liq, p.e] }
    tr.push({ a: r.a, nm: r.nm, av: Math.round(av != null ? av : r.av), d: r.d, w: r.w, m: r.m, t: r.t, rm: r.rm, ntl, np: ps.length, lev: av ? +(ntl / av).toFixed(2) : null });
  });
  pos.sort((a, b) => b.ntl - a.ntl);
  // whales by coin: long vs short value among the tracked wallets
  const byc = {};
  for (const p of pos) { const b = byc[p.c] = byc[p.c] || { c: p.c, l: 0, s: 0, nl: 0, ns: 0 }; if (p.s === 'L') { b.l += p.ntl; b.nl++ } else { b.s += p.ntl; b.ns++ } }
  const coins = Object.values(byc).sort((a, b) => (b.l + b.s) - (a.l + a.s)).slice(0, 20).map(b => {
    const m = mk[b.c] || {};
    return { ...b, p: m.p, ch: m.p && m.pd ? +(m.p / m.pd - 1).toFixed(4) : null, oi: m.oi && m.p ? Math.round(m.oi * m.p) : null, f: m.f };
  });
  // moves since the previous run (needs Upstash)
  let ev = [];
  const prevRaw = await kv([['GET', 'hl:prev']]);
  const now = Date.now();
  if (prevRaw) {
    let prev = null; try { prev = JSON.parse(prevRaw[0] || 'null') } catch (e) {}
    const okAddr = new Set(states.map((s, i) => (s ? rows[i].a : null)).filter(Boolean));
    if (prev && prev.t && now - prev.t < 45 * 60e3) {
      const name = a => (rows.find(r => r.a === a) || {}).nm || null;
      for (const [k, v] of Object.entries(prev.p || {})) {
        const [a, c] = k.split('|');
        if (!okAddr.has(a) || cur[k] || v[1] < 500000) continue;
        const m = (mk[c] || {}).p, liq = v[2];
        const hit = liq && m && (v[0] === 'L' ? m <= liq * 1.015 : m >= liq * 0.985);
        ev.push({ k: hit ? 'liq' : 'close', a, nm: name(a), c, s: v[0], ntl: v[1], px: m || null, t: now });
      }
      for (const [k, v] of Object.entries(cur)) {
        const [a, c] = k.split('|'), p = (prev.p || {})[k];
        if (v[1] < 1000000) continue;
        if (!p || p[0] !== v[0]) ev.push({ k: 'open', a, nm: name(a), c, s: v[0], ntl: v[1], px: v[3], t: now });
        else if (v[1] > p[1] * 1.5 && v[1] - p[1] > 1000000) ev.push({ k: 'add', a, nm: name(a), c, s: v[0], ntl: v[1], px: v[3], t: now });
      }
    }
    const cmds = [['SET', 'hl:prev', JSON.stringify({ t: now, p: cur }), 'EX', '7200']];
    if (ev.length) cmds.push(['LPUSH', 'hl:ev', ...ev.slice(0, 40).map(e => JSON.stringify(e))], ['LTRIM', 'hl:ev', '0', '199']);
    cmds.push(['LRANGE', 'hl:ev', '0', '79']);
    const res = await kv(cmds);
    ev = ((res || [])[res ? res.length - 1 : 0] || []).map(x => { try { return JSON.parse(x) } catch (e) { return null } }).filter(Boolean);
  }
  const near = pos.filter(p => p.dist != null && p.dist < 0.15 && p.ntl >= 100000).sort((a, b) => a.dist - b.dist).slice(0, 40);
  const top = [...tr].sort((a, b) => b.av - a.av).slice(0, 100);
  return { at: now, n: rows.length, nw: tr.filter(t => t.np).length, tot: pos.reduce((s, p) => s + p.ntl, 0), coins, pos: pos.slice(0, 200), near, tr: top, ev,
    best: { d: [...lb].sort((a, b) => (b.d || 0) - (a.d || 0)).slice(0, 15), w: [...lb].sort((a, b) => (b.w || 0) - (a.w || 0)).slice(0, 15),
            m: [...lb].sort((a, b) => (b.m || 0) - (a.m || 0)).slice(0, 15), t: [...lb].sort((a, b) => (b.t || 0) - (a.t || 0)).slice(0, 15) },
    worst: { d: [...lb].sort((a, b) => (a.d || 0) - (b.d || 0)).slice(0, 10), w: [...lb].sort((a, b) => (a.w || 0) - (b.w || 0)).slice(0, 10) } };
}
async function trader(a) {
  const [st, fills, mk, pf] = await Promise.all([info({ type: 'clearinghouseState', user: a }), info({ type: 'userFills', user: a }), marks(), info({ type: 'portfolio', user: a })]);
  if (!st) return null;
  const hist = {};
  for (const [k, v] of (Array.isArray(pf) ? pf : [])) if (['day', 'week', 'month', 'allTime'].includes(k)) {
    const ph = (v.pnlHistory || []), avh = (v.accountValueHistory || []);
    hist[k] = { pnl: ph.length ? +ph[ph.length - 1][1] : null, av: avh.map(x => [x[0], +(+x[1]).toPrecision(6)]).filter((_, i, s) => s.length < 120 || i % Math.ceil(s.length / 120) === 0), vlm: n(v.vlm) };
  }
  const f = (Array.isArray(fills) ? fills : []).slice(0, 60).map(x => ({ c: x.coin, d: x.dir, px: r2(x.px), sz: +x.sz, ntl: Math.round(+x.px * +x.sz), pnl: r2(x.closedPnl), t: x.time, liq: !!x.liquidation }));
  const lb = LB ? LB.find(r => r.a === a.toLowerCase()) : null;
  return { at: Date.now(), a, nm: lb ? lb.nm : null, av: n((st.marginSummary || {}).accountValue), wd: n(st.withdrawable), pos: posOf(st, mk).sort((x, y) => y.ntl - x.ntl), fills: f, hist };
}
module.exports = async function hl(req, send) {
  const q = req.query || {};
  if (q.hl === 'u') {
    const a = String(q.a || '').toLowerCase();
    if (!/^0x[0-9a-f]{40}$/.test(a)) return send(400, { e: 'address' });
    const d = await trader(a);
    return d ? send(200, d, 'public, s-maxage=60, stale-while-revalidate=300') : send(502, { e: 'upstream' }, 'public, s-maxage=20');
  }
  try {
    const d = await snapshot();
    if (!d.tr.length) return send(502, { e: 'upstream' }, 'public, s-maxage=30');
    return send(200, d, 'public, s-maxage=120, stale-while-revalidate=600, stale-if-error=3600');
  } catch (e) {
    return send(502, { e: String(e && e.message || e) }, 'public, s-maxage=30');
  }
};
