// YouTube / video link tracker: /v/<channel>[/<video>] -> site page with UTM; clicks counted in Upstash Redis.
// Optional ?to=/path/ (our own path only). Channel default landing pages are below.
const CH = {
  artitrade: '/', aleksdu: '/', keepthespark: '/en/', growthecoin: '/en/', samestart: '/en/',
};
const G = require('./_guard');
async function redis(cmds) {
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const t = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !t) return;
  try { await fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + t, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) }) } catch (e) {}
}
module.exports = async (req, res) => {
  const q = req.query || {};
  const ch = String(q.ch || '').toLowerCase().replace(/[^a-z0-9-]/g, '').slice(0, 30) || 'other';
  const vid = String(q.vid || '').toLowerCase().replace(/[^a-z0-9_-]/g, '').slice(0, 40);
  let to = String(q.to || '');
  if (!/^\/[a-z0-9/_-]*$/i.test(to)) to = CH[ch] || '/';
  const h = req.headers || {}, ua = String(h['user-agent'] || '');
  const bot = /bot|crawl|spider|slurp|preview|facebookexternalhit|headless/i.test(ua) || !ua || G.over(req, 20, 'v');
  if (!bot) {
    const day = new Date().toISOString().slice(0, 10), key = vid ? `${ch}/${vid}` : ch;
    const country = String(h['x-vercel-ip-country'] || '??');
    const dev = /mobile|android|iphone/i.test(ua) ? 'mobile' : /ipad|tablet/i.test(ua) ? 'tablet' : 'desktop';
    await redis([['HINCRBY', 'yt:total', key, 1], ['HINCRBY', 'yt:ch', ch, 1], ['HINCRBY', `yt:day:${day}`, key, 1], ['EXPIRE', `yt:day:${day}`, 60 * 60 * 24 * 400],
      ['HINCRBY', 'yt:geo', country, 1], ['LPUSH', 'yt:recent', JSON.stringify({ t: Date.now(), k: key, c: country, d: dev })], ['LTRIM', 'yt:recent', 0, 499]]);
  }
  const u = new URLSearchParams({ utm_source: 'youtube', utm_medium: 'video', utm_campaign: ch });
  if (vid) u.set('utm_content', vid);
  res.statusCode = 302;
  res.setHeader('Location', `${to}${to.includes('?') ? '&' : '?'}${u}`);
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.end();
};
