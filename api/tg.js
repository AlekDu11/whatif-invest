// Telegram bot webhook for price alerts. Deep link from the site: t.me/<bot>?start=a_<aid>_<u|d>_<price with p for the dot>_<lang>
// One-time setup after adding TG_BOT_TOKEN and ALERTS_KEY in Vercel env: open /api/tg?setup=<ALERTS_KEY>
const { kv, tg, amap, prices, fmt, T, tpl } = require('./_alerts');
module.exports = async (req, res) => {
  const q = req.query || {};
  const done = (c, o) => { res.statusCode = c; res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(o || {})) };
  if (!process.env.TG_BOT_TOKEN) return done(503, { e: 'no token' });
  if (q.setup) {
    if (q.setup !== process.env.ALERTS_KEY) return done(403, { e: 'key' });
    const host = 'https://' + (req.headers['x-forwarded-host'] || req.headers.host);
    const r = await tg('setWebhook', { url: host + '/api/tg', secret_token: process.env.ALERTS_KEY, allowed_updates: ['message'] });
    await tg('setMyCommands', { commands: [{ command: 'list', description: 'My alerts' }, { command: 'stop', description: 'Turn off all alerts' }] });
    return done(200, r);
  }
  if (req.method !== 'POST' || req.headers['x-telegram-bot-api-secret-token'] !== process.env.ALERTS_KEY) return done(403);
  let u = req.body || {};
  if (typeof u === 'string') { try { u = JSON.parse(u) } catch (e) { u = {} } }
  const m = u.message || {};
  const chat = m.chat && m.chat.id, text = String(m.text || '').trim();
  if (!chat || !text) return done(200);
  const lang = (m.from && m.from.language_code) || 'en';
  let t = T(lang);
  const say = (s, extra) => tg('sendMessage', Object.assign({ chat_id: chat, text: s, disable_web_page_preview: true }, extra || {}));
  try {
    const ids = await kv([['SMEMBERS', `al:chat:${chat}`]]).then(r => (r[0] || []).sort((a, b) => a - b));
    if (/^\/start a_/.test(text)) {
      const p = text.slice(9).split('_');            // aid (may contain _) _ dir _ price _ lang
      const lg = p.pop(), pr = p.pop(), dr = p.pop(), aid = p.join('_');
      const dir = dr === 'd' ? 'd' : 'u', price = parseFloat((pr || '').replace('p', '.'));
      p[3] = lg; if (lg) t = T(lg);
      const map = await amap(), src = map[aid];
      if (!src || !(price > 0)) return say(t.bad).then(() => done(200));
      if (ids.length >= 10) return say(t.lim).then(() => done(200));
      const now = (await prices([{ s: src[0], k: src[1] }]))[src[1]];
      const id = (await kv([['INCR', 'al:seq']]))[0];
      const al = { id, c: chat, a: aid, n: src[2] || aid.toUpperCase(), s: src[0], k: src[1], d: dir, p: price, l: p[3] || lang.slice(0, 2), t: Date.now() };
      await kv([['HSET', 'al:items', String(id), JSON.stringify(al)], ['SADD', `al:chat:${chat}`, String(id)], ['INCR', 'al:created']]);
      return say(tpl(t.set, { n: al.n, d: dir === 'u' ? t.up : t.dn, p: fmt(price), c: now ? fmt(now) : '—' })).then(() => done(200));
    }
    if (/^\/start/.test(text)) return say(t.hi).then(() => done(200));
    if (/^\/list/.test(text)) {
      if (!ids.length) return say(t.none).then(() => done(200));
      const rows = await kv([['HMGET', 'al:items', ...ids]]);
      const ls = (rows[0] || []).map((r, i) => { try { const a = JSON.parse(r); return `${i + 1}. ${a.n} ${a.d === 'u' ? t.up : t.dn} $${fmt(a.p)}` } catch (e) { return null } }).filter(Boolean);
      return say(t.list + '\n' + ls.join('\n') + '\n\n' + t.del).then(() => done(200));
    }
    if (/^\/del\s+\d+/.test(text)) {
      const k = parseInt(text.split(/\s+/)[1], 10) - 1, id = ids[k];
      if (id) await kv([['HDEL', 'al:items', id], ['SREM', `al:chat:${chat}`, id]]);
      return say(t.gone).then(() => done(200));
    }
    if (/^\/stop/.test(text)) {
      if (ids.length) await kv([['HDEL', 'al:items', ...ids], ['DEL', `al:chat:${chat}`]]);
      return say(t.stop).then(() => done(200));
    }
    return say(t.hi).then(() => done(200));
  } catch (e) { return done(200) }
};
