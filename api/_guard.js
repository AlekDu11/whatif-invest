// Cheap abuse guard for open endpoints: per-IP request budget per minute, kept in the function instance's memory
// (no storage calls, so a flood cannot burn the Upstash quota). Imperfect across instances, but stops simple floods.
const HITS = new Map();
const ip = req => String((req.headers || {})['x-forwarded-for'] || '').split(',')[0].trim() || '?';
const isBot = req => { const ua = String((req.headers || {})['user-agent'] || ''); return !ua || /bot|crawl|spider|slurp|preview|facebookexternalhit|headless|python-requests|curl|wget|httpclient|scrapy/i.test(ua) };
function over(req, perMin, key) {
  const k = (key || '') + ip(req), now = Date.now(), w = HITS.get(k);
  if (!w || now - w.t > 60000) { HITS.set(k, { t: now, n: 1 }); if (HITS.size > 5000) HITS.clear(); return false }
  return ++w.n > perMin;
}
module.exports = { ip, isBot, over };
