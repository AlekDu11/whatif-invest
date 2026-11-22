// Click tracker + redirect: /go/<partner>?from=<page>&l=<lang>[&e=<polymarket event slug>]
// Counts go to Upstash Redis (Vercel KV) when KV_REST_API_URL / KV_REST_API_TOKEN are set; otherwise it just redirects.
const P = require('./_partners');
const G = require('./_guard');
// Polymarket is not available (Polymarket geoblock incl. close-only) or blocked by the government in these countries
// (coinperps.com check of 27 Oct 2026 + government block list). Visitors from them go to our explainer instead.
const PM_BLOCKED = new Set(('CU IR KP SY BY BE FR DE IT PL RU SK GB US UM BR NI VE AU MM NZ SG TW TH BI CF CD ET IQ LB LY SO SS SD YE ZW '
  + 'IE MT NL JP KR CH CO RO UA HU PT AR PH IN ID ES CZ TR DK LT').split(' '));
const PM_BLOCKED_REGIONS = new Set(['CA-AB', 'CA-BC', 'CA-ON', 'CA-QC']);

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
  // memecoin pages: open the exact token on GMGN with our referral code (gmgn.ai/<chain>/token/<code>_<address>)
  const GMC = { solana: 'sol', base: 'base', bsc: 'bsc', eth: 'eth', tron: 'tron' };
  if (id === 'gmgn' && GMC[q.c] && /^[A-Za-z0-9]{20,70}$/.test(String(q.a || ''))) {
    const code = (P.gmgn.match(/\/r\/([A-Za-z0-9]+)/) || [])[1];
    if (code) dest = `https://gmgn.ai/${GMC[q.c]}/token/${code}_${q.a}`;
  }
  // Binance Wallet: open the exact token page with our referral code attached (ref=…); without a token → the referral landing page
  const BNW = { solana: 'sol', bsc: 'bsc', base: 'base' };
  if (id === 'binance-web3' && BNW[q.c] && /^[A-Za-z0-9]{20,70}$/.test(String(q.a || ''))) {
    const ref = (P['binance-web3'].match(/ref=([A-Za-z0-9]+)/) || [])[1];
    if (ref) dest = `https://web3.binance.com/en/token/${BNW[q.c]}/${q.a}?ref=${ref}`;
  }
  const h = req.headers || {};
  if (id === 'polymarket') {
    const c = String(h['x-vercel-ip-country'] || '').toUpperCase(), r = String(h['x-vercel-ip-country-region'] || '').toUpperCase();
    if (PM_BLOCKED.has(c) || PM_BLOCKED_REGIONS.has(c + '-' + r)) {
      await redis([['HINCRBY', 'clk:total', 'polymarket-geo', 1], ['HINCRBY', 'clk:geo:polymarket-geo', c, 1]]);
      const l = String(q.l || '').replace(/[^a-z]/g, '').slice(0, 3);
      res.statusCode = 302; res.setHeader('Location', (l && l !== 'uk' ? '/' + l : '') + '/activities/?pm=unavailable');
      res.setHeader('Cache-Control', 'no-store'); return res.end();
    }
  }
  const ua = String(h['user-agent'] || '');
  const bot = /bot|crawl|spider|slurp|preview|facebookexternalhit|headless/i.test(ua) || !ua || G.over(req, 20, 'go');
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
