// Private click dashboard: /stats?key=<STATS_KEY>
async function redis(cmds) {
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const t = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !t) return null;
  const r = await fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + t, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  return (await r.json()).map(x => x.result);
}
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const pairs = a => { const o = {}; for (let i = 0; a && i < a.length; i += 2) o[a[i]] = +a[i + 1]; return Object.entries(o).sort((x, y) => y[1] - x[1]) };
const table = (title, rows, n = 25) => `<section><h2>${title}</h2><table>${rows.slice(0, n).map(([k, v]) => `<tr><td>${esc(k)}</td><td>${v}</td></tr>`).join('') || '<tr><td>—</td></tr>'}</table></section>`;

module.exports = async (req, res) => {
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.setHeader('Cache-Control', 'no-store');
  const key = process.env.STATS_KEY;
  if (!key || (req.query || {}).key !== key) { res.statusCode = 404; return res.end('Not found'); }
  const days = [...Array(30)].map((_, i) => new Date(Date.now() - i * 864e5).toISOString().slice(0, 10));
  const r = await redis([['HGETALL', 'clk:total'], ['HGETALL', 'clk:geo'], ['HGETALL', 'clk:page'], ['HGETALL', 'clk:lang'], ['HGETALL', 'clk:dev'],
    ['LRANGE', 'clk:recent', 0, 99], ['HGETALL', 'poll:v1'], ['HGETALL', 'poll:v1:geo'], ['HGETALL', 'yt:ch'], ['HGETALL', 'yt:total'], ['HGETALL', 'yt:geo'], ['LRANGE', 'yt:recent', 0, 49], ...days.map(d => ['HGETALL', `clk:day:${d}`])]);
  if (!r) { res.setHeader('Content-Type', 'text/plain; charset=utf-8'); return res.end('Storage is not connected yet (Upstash Redis / Vercel KV).') }
  const [tot, geo, page, lang, dev, recent, poll, pollGeo, ytCh, ytTot, ytGeo, ytRec, ...dd] = r;
  const ytr = (ytRec || []).map(x => { try { return JSON.parse(x) } catch (e) { return null } }).filter(Boolean);
  const daysRows = days.map((d, i) => { const p = pairs(dd[i]); return [d, p.reduce((s, x) => s + x[1], 0) + (p.length ? ' — ' + p.map(([k, v]) => `${k} ${v}`).join(', ') : '')] });
  const rec = (recent || []).map(x => { try { return JSON.parse(x) } catch (e) { return null } }).filter(Boolean);
  const html = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Clicks · WhatIfStack</title>
<style>body{font:14px/1.45 system-ui,sans-serif;margin:0;padding:24px;background:#f5f6f8;color:#161a23}h1{margin:0 0 16px}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
section{background:#fff;border:1px solid #e7e9ee;border-radius:12px;padding:14px 16px}h2{font-size:15px;margin:0 0 8px}table{width:100%;border-collapse:collapse}td{padding:4px 0;border-bottom:1px solid #f0f1f4}td:last-child{text-align:right;font-weight:600}</style></head>
<body><h1>Partner link clicks</h1><div class="g">${table('YouTube: clicks by channel', pairs(ytCh))}${table('YouTube: by video', pairs(ytTot))}${table('YouTube: countries', pairs(ytGeo))}<section><h2>YouTube: last clicks</h2><table>${ytr.map(x => `<tr><td>${new Date(x.t).toISOString().slice(0, 16).replace('T', ' ')} · <b>${esc(x.k)}</b> · ${esc(x.c)} · ${esc(x.d)}</td></tr>`).join('') || '<tr><td>—</td></tr>'}</table></section>${table('Poll: what would bring you back daily', pairs(poll))}${table('Poll by country', pairs(pollGeo))}${table('Total by partner', pairs(tot))}${table('Countries', pairs(geo))}${table('Pages', pairs(page))}${table('Languages', pairs(lang))}${table('Devices', pairs(dev))}${table('Last 30 days', daysRows, 30)}
<section style="grid-column:1/-1"><h2>Last 100 clicks</h2><table>${rec.map(x => `<tr><td>${new Date(x.t).toISOString().slice(0, 16).replace('T', ' ')} · <b>${esc(x.p)}</b> · ${esc(x.c)} ${esc(x.city || '')} · ${esc(x.d)} · ${esc(x.l)}</td><td>${esc(x.from)}</td></tr>`).join('')}</table></section></div></body></html>`;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.end(html);
};
