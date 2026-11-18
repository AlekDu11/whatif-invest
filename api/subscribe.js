// Weekly report signup: POST /api/subscribe {em, l, src} → Upstash: hash nl:subs (email → {l, at, src, c}), counter nl:count.
// Emails are sent later through the newsletter provider (subscribers are imported from nl:subs). 5 signups/day per IP.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.statusCode = 405; return res.end() }
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  const em = String(b.em || '').trim().toLowerCase().slice(0, 120), ua = String((req.headers || {})['user-agent'] || '');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em) || /bot|crawl|spider|headless/i.test(ua) || b.hp) { res.statusCode = 400; return res.end('{}') }
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL, k = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !k) { res.statusCode = 503; return res.end('{}') }
  const h = req.headers || {}, ip = String(h['x-forwarded-for'] || '').split(',')[0].trim() || '?', day = new Date().toISOString().slice(0, 10);
  const call = cmds => fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + k, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) }).then(r => r.json());
  try {
    const lim = await call([['INCR', `nl:rl:${day}:${ip}`], ['EXPIRE', `nl:rl:${day}:${ip}`, 90000]]);
    if ((lim[0] && lim[0].result) > 5) { res.statusCode = 429; return res.end('{}') }
    const meta = JSON.stringify({ l: String(b.l || '').slice(0, 5), at: new Date().toISOString(), src: String(b.src || '').slice(0, 120), c: String(h['x-vercel-ip-country'] || '??') });
    const r = await call([['HSETNX', 'nl:subs', em, meta]]);
    if (r[0] && r[0].result === 1) await call([['INCR', 'nl:count']]);
  } catch (e) { res.statusCode = 502; return res.end('{}') }
  res.statusCode = 200; res.setHeader('Content-Type', 'application/json'); res.end('{"ok":1}');
};
