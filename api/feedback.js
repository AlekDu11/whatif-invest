// «Suggest an improvement» form: POST /api/feedback {t, em, l, p} → Upstash list fb:v1 (newest first, max 5000).
// Read in Vercel → Storage → Upstash browser (LRANGE fb:v1 0 50) or by the weekly growth report.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.statusCode = 405; return res.end() }
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  const t = String(b.t || '').trim().slice(0, 2000), em = String(b.em || '').trim().slice(0, 120);
  const ua = String((req.headers || {})['user-agent'] || '');
  if (t.length < 3 || /bot|crawl|spider|headless/i.test(ua) || (em && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em))) { res.statusCode = 400; return res.end('{}') }
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL, k = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !k) { res.statusCode = 503; return res.end('{}') }
  const h = req.headers || {}, ip = String(h['x-forwarded-for'] || '').split(',')[0].trim() || '?';
  const day = new Date().toISOString().slice(0, 10);
  const row = JSON.stringify({ at: new Date().toISOString(), t, em, l: String(b.l || '').slice(0, 5), p: String(b.p || '').slice(0, 200), c: String(h['x-vercel-ip-country'] || '??') });
  try {
    const call = cmds => fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + k, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) }).then(r => r.json());
    const lim = await call([['INCR', `fb:rl:${day}:${ip}`], ['EXPIRE', `fb:rl:${day}:${ip}`, 90000]]);
    if ((lim[0] && lim[0].result) > 10) { res.statusCode = 429; return res.end('{}') }
    await call([['LPUSH', 'fb:v1', row], ['LTRIM', 'fb:v1', 0, 4999], ['INCR', 'fb:count']]);
  } catch (e) { res.statusCode = 502; return res.end('{}') }
  res.statusCode = 200; res.setHeader('Content-Type', 'application/json'); res.end('{"ok":1}');
};
