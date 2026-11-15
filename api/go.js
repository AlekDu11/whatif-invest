// Click tracker + redirect: /go/<partner>?from=<page>&l=<lang>[&e=<polymarket event slug>]
// Counts go to Upstash Redis (Vercel KV) when KV_REST_API_URL / KV_REST_API_TOKEN are set; otherwise it just redirects.
const P = require('./_partners');

async function redis(cmds) {
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const t = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !t) return;
  try {
    await fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + t, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  } catch (e) {}
}

module.exports = async (req, res) => {
  const q = req.query || {};
  const id = String(q.p || '').toLowerCase();
  let dest = P[id];
  if (!dest) { res.statusCode = 302; res.setHeader('Location', '/'); return res.end(); }
  if (id === 'polymarket' && q.e && /^[a-z0-9-]{1,200}$/.test(q.e)) dest = `https://polymarket.com/event/${q.e}?via=alek-du`;
  const h = req.headers || {};
  const ua = String(h['user-agent'] || '');
  const bot = /bot|crawl|spider|slurp|preview|facebookexternalhit|headless/i.test(ua) || !ua;
  if (!bot) {
    const day = new Date().toISOString().slice(0, 10);
    const country = String(h['x-vercel-ip-country'] || '??');
    const city = decodeURIComponent(String(h['x-vercel-ip-city'] || '')).slice(0, 40);
    const from = String(q.from || h.referer || '').replace(/^https?:\/\/[^/]+/, '').slice(0, 120) || '(direct)';
    const lang = String(q.l || '').slice(0, 5) || '?';
    const dev = /mobile|android|iphone/i.test(ua) ? 'mobile' : /ipad|tablet/i.test(ua) ? 'tablet' : 'desktop';
    const rec = JSON.stringify({ t: Date.now(), p: id, c: country, city, from, l: lang, d: dev });
    await redis([
      ['HINCRBY', `clk:day:${day}`, id, 1], ['EXPIRE', `clk:day:${day}`, 60 * 60 * 24 * 400],
      ['HINCRBY', 'clk:total', id, 1],
      ['HINCRBY', `clk:geo:${id}`, country, 1], ['HINCRBY', 'clk:geo', country, 1],
      ['HINCRBY', 'clk:page', from, 1], ['HINCRBY', `clk:page:${id}`, from, 1],
      ['HINCRBY', 'clk:lang', lang, 1], ['HINCRBY', 'clk:dev', dev, 1],
      ['LPUSH', 'clk:recent', rec], ['LTRIM', 'clk:recent', 0, 499],
    ]);
  }
  res.statusCode = 302;
  res.setHeader('Location', dest);
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.end();
};
