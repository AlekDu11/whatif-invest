// Price-alert checker: GET /api/alerts?key=<ALERTS_KEY>. Called every ~10 minutes by .github/workflows/alerts.yml.
const { kv, tg, prices, fmt, T, tpl } = require('./_alerts');
module.exports = async (req, res) => {
  const done = (c, o) => { res.statusCode = c; res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store'); res.end(JSON.stringify(o || {})) };
  if (!process.env.TG_BOT_TOKEN || (req.query || {}).key !== process.env.ALERTS_KEY) return done(403);
  const all = (await kv([['HGETALL', 'al:items']]))[0] || [];
  const items = [];
  for (let i = 0; i < all.length; i += 2) { try { items.push(JSON.parse(all[i + 1])) } catch (e) {} }
  if (!items.length) return done(200, { alerts: 0 });
  const px = await prices(items);
  let sent = 0;
  for (const a of items) {
    const now = px[a.k];
    if (!now || !((a.d === 'u' && now >= a.p) || (a.d === 'd' && now <= a.p))) continue;
    const t = T(a.l), path = (a.l && a.l !== 'uk' ? '/' + a.l : '') + '/' + a.a + '/';
    await tg('sendMessage', { chat_id: a.c, text: tpl(t.hit, { n: a.n, d: a.d === 'u' ? t.up : t.dn, p: fmt(a.p), c: fmt(now) }),
      reply_markup: { inline_keyboard: [[{ text: tpl(t.open, { n: a.n }), url: 'https://whatifstack.com' + path + '?utm_source=tg_alert' }]] } });
    await kv([['HDEL', 'al:items', String(a.id)], ['SREM', `al:chat:${a.c}`, String(a.id)], ['INCR', 'al:sent']]);
    sent++;
  }
  return done(200, { alerts: items.length, priced: Object.keys(px).length, sent });
};
