// One-question poll: /api/poll?o=<option>&l=<lang>  → counts in Upstash (poll:v1)
const OPTS = ['alerts', 'plan', 'watchlist', 'summary', 'game', 'learn'];
module.exports = async (req, res) => {
  const q = req.query || {}, o = String(q.o || ''), l = String(q.l || '?').slice(0, 5);
  const u = process.env.KV_REST_API_URL, t = process.env.KV_REST_API_TOKEN;
  const ua = String((req.headers || {})['user-agent'] || '');
  if (OPTS.includes(o) && u && t && !/bot|crawl|spider|headless/i.test(ua)) {
    const c = String((req.headers || {})['x-vercel-ip-country'] || '??');
    try {
      await fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + t, 'Content-Type': 'application/json' },
        body: JSON.stringify([['HINCRBY', 'poll:v1', o, 1], ['HINCRBY', `poll:v1:lang:${l}`, o, 1], ['HINCRBY', 'poll:v1:geo', `${c}:${o}`, 1]]) });
    } catch (e) {}
  }
  res.setHeader('Cache-Control', 'no-store');
  res.statusCode = 204; res.end();
};
