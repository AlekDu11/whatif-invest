// Telegram bot @WhatIfStack_Bot (webhook). Menu with the portfolio Mini App, prices by ticker, inline mode, sharing, channel, price alerts.
// Deep link for alerts from the site: t.me/<bot>?start=a_<aid>_<u|d>_<price with p for the dot>_<lang>
// One-time setup after adding TG_BOT_TOKEN and ALERTS_KEY in Vercel env: open /api/tg?setup=<ALERTS_KEY>
// (sets the webhook, commands, menu button «Portfolio», descriptions in uk/ru/en). Inline mode also needs /setinline in @BotFather.
const { kv, tg, amap, prices, fmt, T, tpl, M, LP } = require('./_alerts');
const SITE = 'https://whatifstack.com', BOT = 'WhatIfStack_bot', CH = 'https://t.me/WhatIfStack';
const TOP = ['btc', 'eth', 'sol', 'gold', 'spy', 'nvda'];

function find(map, q) {
  q = String(q || '').toLowerCase().replace(/^[$/]/, '').trim();
  if (!q) return null;
  if (map[q]) return q;
  const alias = { bitcoin: 'btc', ethereum: 'eth', solana: 'sol', 'золото': 'gold', 'біткоїн': 'btc', 'биткоин': 'btc', 'ефір': 'eth', 'эфир': 'eth', silver: 'silver', 'срібло': 'silver' };
  if (alias[q] && map[alias[q]]) return alias[q];
  return Object.keys(map).find(k => (map[k][2] || '').toLowerCase() === q) || null;
}
async function quote(lang, aid) {
  const map = await amap(), s = map[aid];
  if (!s) return null;
  const px = await prices([{ s: s[0], k: s[1] }]);
  return { aid, n: s[2] || aid.toUpperCase(), p: px[s[1]], url: `${SITE}${LP(lang)}/${aid}/?utm_source=tg_bot` };
}
const menu = (lang) => { const m = M(lang); return { inline_keyboard: [
  [{ text: m.pf, web_app: { url: `${SITE}${LP(lang)}/me/?tgapp=1` } }],
  [{ text: m.px, callback_data: 'px' }, { text: m.al, callback_data: 'al' }],
  [{ text: m.ch, url: CH }, { text: m.sh, url: `https://t.me/share/url?url=${encodeURIComponent('https://t.me/' + BOT)}&text=${encodeURIComponent(m.share)}` }],
  [{ text: m.sup, callback_data: 'sup' }, { text: m.lng, callback_data: 'lng' }],
  [{ text: m.site, url: `${SITE}${LP(lang)}/?utm_source=tg_bot` }]] } };
// Bot filter for ad traffic: t.me/<bot>?start=ad_<tag> → one-tap human check → menu + a per-tag channel invite link
// (Telegram counts joins per invite link). Counters in Upstash hash tg:ads: <tag>:start, <tag>:pass, <tag>:fail. Stats: /api/tg?stats=<ALERTS_KEY>
const CAP = [['🪙', 'coin'], ['🍎', 'apple'], ['🚗', 'car'], ['🐶', 'dog'], ['⚽', 'ball'], ['🌙', 'moon']];
const capKb = (tag, n) => { const pick = CAP.slice().sort(() => Math.random() - 0.5).slice(0, 4), ok = pick[Math.floor(Math.random() * 4)];
  return { e: ok[0], kb: { inline_keyboard: [pick.map(([e]) => ({ text: e, callback_data: `cap:${e === ok[0] ? 1 : 0}:${n}:${tag}` }))] } }; };
async function invite(tag) {
  const [have] = await kv([['GET', `tg:inv:${tag}`]]);
  if (have) return have;
  const r = await tg('createChatInviteLink', { chat_id: '@WhatIfStack', name: ('bot ' + tag).slice(0, 32) });
  const url = r && r.result && r.result.invite_link;
  if (url) { await kv([['SET', `tg:inv:${tag}`, url]]); return url; }
  return CH;
}
const LANGS = [['uk', '🇺🇦 Українська'], ['en', '🇬🇧 English'], ['ru', 'Русский'], ['es', '🇪🇸 Español'], ['de', '🇩🇪 Deutsch'], ['pl', '🇵🇱 Polski'], ['tr', '🇹🇷 Türkçe'], ['pt', '🇧🇷 Português']];

module.exports = async (req, res) => {
  const q = req.query || {};
  const done = (c, o) => { res.statusCode = c; res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(o || {})) };
  if (!process.env.TG_BOT_TOKEN) return done(503, { e: 'no token' });
  if (q.setup) {
    if (q.setup !== process.env.ALERTS_KEY) return done(403, { e: 'key' });
    const host = 'https://' + (req.headers['x-forwarded-host'] || req.headers.host);
    const out = {};
    out.webhook = await tg('setWebhook', { url: host + '/api/tg', secret_token: process.env.ALERTS_KEY, allowed_updates: ['message', 'callback_query', 'inline_query'] });
    for (const l of ['en', 'uk', 'ru']) {
      const m = M(l), lc = l === 'en' ? {} : { language_code: l };
      await tg('setMyCommands', { commands: Object.entries(m.cmd).map(([command, description]) => ({ command, description })), ...lc });
      await tg('setMyDescription', { description: m.desc, ...lc });
      await tg('setMyShortDescription', { short_description: m.about, ...lc });
    }
    out.menu = await tg('setChatMenuButton', { menu_button: { type: 'web_app', text: M('en').menu, web_app: { url: SITE + '/en/me/?tgapp=1' } } });
    return done(200, out);
  }
  if (q.stats) {
    if (q.stats !== process.env.ALERTS_KEY) return done(403, { e: 'key' });
    const [ads, users, human] = await kv([['HGETALL', 'tg:ads'], ['SCARD', 'tg:users'], ['SCARD', 'tg:human']]);
    const o = {}; for (let i = 0; i < (ads || []).length; i += 2) o[ads[i]] = +ads[i + 1];
    return done(200, { ads: o, users, human });
  }
  if (req.method !== 'POST' || req.headers['x-telegram-bot-api-secret-token'] !== process.env.ALERTS_KEY) return done(403);
  let u = req.body || {};
  if (typeof u === 'string') { try { u = JSON.parse(u) } catch (e) { u = {} } }
  try {
    if (u.inline_query) {                                     // @WhatIfStack_Bot btc → a price card you can send to any chat
      const iq = u.inline_query, lang = (iq.from && iq.from.language_code) || 'en', m = M(lang), map = await amap();
      const words = String(iq.query || '').split(/[\s,]+/).filter(Boolean).slice(0, 5);
      const ids = (words.length ? words.map(w => find(map, w)).filter(Boolean) : TOP.filter(i => map[i]));
      const qs = (await Promise.all([...new Set(ids)].map(i => quote(lang, i)))).filter(x => x && x.p);
      const results = qs.map(x => ({ type: 'article', id: x.aid, title: `${x.n}: $${fmt(x.p)}`, description: 'WhatIfStack',
        input_message_content: { message_text: `${x.n}: $${fmt(x.p)}\n\n${x.url}`, disable_web_page_preview: false },
        reply_markup: { inline_keyboard: [[{ text: tpl(m.page, { n: x.n }), url: x.url }], [{ text: '🤖 @' + BOT, url: 'https://t.me/' + BOT }]] } }));
      await tg('answerInlineQuery', { inline_query_id: iq.id, results, cache_time: 60, is_personal: false });
      return done(200);
    }
    const cb = u.callback_query;
    const msg = u.message || (cb && cb.message) || {};
    const chat = msg.chat && msg.chat.id;
    const from = (cb && cb.from) || msg.from || {};
    if (!chat) return done(200);
    const [saved] = await kv([['GET', `tg:lang:${chat}`]]);
    let lang = saved || from.language_code || 'en';
    let t = T(lang); let m = M(lang);
    const admin = process.env.TG_ADMIN_CHAT;
    const say = (s, extra) => tg('sendMessage', Object.assign({ chat_id: chat, text: s, disable_web_page_preview: true }, extra || {}));
    const ids = await kv([['SMEMBERS', `al:chat:${chat}`]]).then(r => (r[0] || []).sort((a, b) => a - b));
    const listAlerts = async () => {
      if (!ids.length) return say(t.none + '\n\n' + t.hi);
      const rows = await kv([['HMGET', 'al:items', ...ids]]);
      const ls = (rows[0] || []).map((r, i) => { try { const a = JSON.parse(r); return `${i + 1}. ${a.n} ${a.d === 'u' ? t.up : t.dn} $${fmt(a.p)}` } catch (e) { return null } }).filter(Boolean);
      return say(t.list + '\n' + ls.join('\n') + '\n\n' + t.del);
    };
    const topPrices = async () => {
      const qs = (await Promise.all(TOP.map(i => quote(lang, i)))).filter(x => x && x.p);
      return say(m.top + '\n' + qs.map(x => `• ${x.n}: $${fmt(x.p)}`).join('\n') + '\n\n' + m.nf.split('.')[1].trim(), { reply_markup: menu(lang) });
    };
    if (cb) {
      await tg('answerCallbackQuery', { callback_query_id: cb.id });
      if (/^cap:/.test(cb.data)) {
        const [, ok, n, tag] = cb.data.split(':');
        if (ok === '1') {
          const [was] = await kv([['SADD', 'tg:human', String(chat)]]);
          if (was) await kv([['HINCRBY', 'tg:ads', tag + ':pass', 1]]);
          const inv = await invite(tag);
          await say(m.capok + '\n\n' + m.hi, { reply_markup: { inline_keyboard: [[{ text: m.join, url: inv }], ...menu(lang).inline_keyboard] } });
        } else {
          await kv([['HINCRBY', 'tg:ads', tag + ':fail', 1]]);
          if (+n < 2) { const c = capKb(tag, +n + 1); await say(tpl(m.capbad, { e: c.e }), { reply_markup: c.kb }); }
        }
        return done(200);
      }
      if (cb.data === 'px') await topPrices(); else if (cb.data === 'al') await listAlerts();
      else if (cb.data === 'sup') { await kv([['SET', `tg:sup:${chat}`, '1', 'EX', 3600]]); await say(m.supask, { reply_markup: { force_reply: true } }); }
      else if (cb.data === 'lng') await say(m.lng, { reply_markup: { inline_keyboard: [LANGS.slice(0, 4), LANGS.slice(4)].map(r => r.map(([c, n]) => ({ text: n, callback_data: 'l:' + c }))) } });
      else if (/^l:[a-z]{2}$/.test(cb.data)) { lang = cb.data.slice(2); await kv([['SET', `tg:lang:${chat}`, lang]]); m = M(lang); t = T(lang); await say(m.lngok + '\n\n' + m.hi, { reply_markup: menu(lang) }); }
      return done(200);
    }
    const text = String(msg.text || msg.caption || '').trim();
    if (admin && String(chat) === String(admin) && msg.reply_to_message) {      // the owner answers a forwarded support message → back to the user
      const [to] = await kv([['GET', `tg:supmap:${msg.reply_to_message.message_id}`]]);
      if (to) { await tg('copyMessage', { chat_id: to, from_chat_id: chat, message_id: msg.message_id }); return say('↩️ sent').then(() => done(200)); }
    }
    const [inSup] = await kv([['GET', `tg:sup:${chat}`]]);
    if (inSup && !/^\//.test(text)) {                                        // support message: keep it and pass it to the owner
      await kv([['DEL', `tg:sup:${chat}`], ['LPUSH', 'tg:support', JSON.stringify({ c: chat, u: from.username || '', n: from.first_name || '', l: lang, t: Date.now(), m: text.slice(0, 2000) })], ['LTRIM', 'tg:support', 0, 999]]);
      if (admin) { const f = await tg('forwardMessage', { chat_id: admin, from_chat_id: chat, message_id: msg.message_id });
        if (f && f.result) await kv([['SET', `tg:supmap:${f.result.message_id}`, String(chat), 'EX', 30 * 86400]]); }
      return say(m.supok, { reply_markup: menu(lang) }).then(() => done(200));
    }
    if (!text) return done(200);
    if (/^\/support/.test(text)) { await kv([['SET', `tg:sup:${chat}`, '1', 'EX', 3600]]); return say(m.supask, { reply_markup: { force_reply: true } }).then(() => done(200)); }
    if (/^\/lang/.test(text)) return say(m.lng, { reply_markup: { inline_keyboard: [LANGS.slice(0, 4), LANGS.slice(4)].map(r => r.map(([c, n]) => ({ text: n, callback_data: 'l:' + c }))) } }).then(() => done(200));
    if (/^\/myid/.test(text)) return say(String(chat)).then(() => done(200));
    if (/^\/start a_/.test(text)) {                           // price alert from the site
      const p = text.slice(9).split('_');
      const lg = p.pop(), pr = p.pop(), dr = p.pop(), aid = p.join('_');
      const dir = dr === 'd' ? 'd' : 'u', price = parseFloat((pr || '').replace('p', '.'));
      if (lg) t = T(lg);
      const map = await amap(), src = map[aid];
      if (!src || !(price > 0)) return say(t.bad).then(() => done(200));
      if (ids.length >= 10) return say(t.lim).then(() => done(200));
      const now = (await prices([{ s: src[0], k: src[1] }]))[src[1]];
      const id = (await kv([['INCR', 'al:seq']]))[0];
      const al = { id, c: chat, a: aid, n: src[2] || aid.toUpperCase(), s: src[0], k: src[1], d: dir, p: price, l: lg || lang.slice(0, 2), t: Date.now() };
      await kv([['HSET', 'al:items', String(id), JSON.stringify(al)], ['SADD', `al:chat:${chat}`, String(id)], ['INCR', 'al:created']]);
      return say(tpl(t.set, { n: al.n, d: dir === 'u' ? t.up : t.dn, p: fmt(price), c: now ? fmt(now) : '—' }), { reply_markup: menu(lg || lang) }).then(() => done(200));
    }
    if (/^\/start ad_[\w-]{1,20}$/.test(text)) {               // visitor from an ad → human check first
      const tag = text.slice(10);
      const [isNew] = await kv([['SADD', 'tg:users', String(chat)]]);
      if (isNew) await kv([['HINCRBY', 'tg:ads', tag + ':start', 1], ['SET', `tg:src:${chat}`, tag]]);
      const [hum] = await kv([['SISMEMBER', 'tg:human', String(chat)]]);
      if (hum) return say(m.hi, { reply_markup: menu(lang) }).then(() => done(200));
      const c = capKb(tag, 0);
      return say(tpl(m.cap, { e: c.e }), { reply_markup: c.kb }).then(() => done(200));
    }
    if (/^\/(start|menu|help)\b/.test(text)) { await kv([['SADD', 'tg:users', String(chat)]]); return say(m.hi, { reply_markup: menu(lang) }).then(() => done(200)); }
    if (/^\/portfolio/.test(text)) return say(m.pf, { reply_markup: { inline_keyboard: [[{ text: m.pf, web_app: { url: `${SITE}${LP(lang)}/me/?tgapp=1` } }]] } }).then(() => done(200));
    if (/^\/share/.test(text)) return say(m.share + '\nhttps://t.me/' + BOT, { reply_markup: { inline_keyboard: [[{ text: m.sh, url: `https://t.me/share/url?url=${encodeURIComponent('https://t.me/' + BOT)}&text=${encodeURIComponent(m.share)}` }]] } }).then(() => done(200));
    if (/^\/list/.test(text)) return listAlerts().then(() => done(200));
    if (/^\/del\s+\d+/.test(text)) {
      const k = parseInt(text.split(/\s+/)[1], 10) - 1, id = ids[k];
      if (id) await kv([['HDEL', 'al:items', id], ['SREM', `al:chat:${chat}`, id]]);
      return say(t.gone).then(() => done(200));
    }
    if (/^\/stop/.test(text)) {
      if (ids.length) await kv([['HDEL', 'al:items', ...ids], ['DEL', `al:chat:${chat}`]]);
      return say(t.stop).then(() => done(200));
    }
    if (/^\/price\s*$/.test(text)) return topPrices().then(() => done(200));
    const qtext = text.replace(/^\/price\s+/, '');           // «btc», «/price nvda» → price + link
    const map = await amap(), aid = find(map, qtext.split(/\s+/)[0]);
    if (!aid) return say(tpl(m.nf, { q: qtext.slice(0, 30) }), { reply_markup: menu(lang) }).then(() => done(200));
    const x = await quote(lang, aid);
    return say(`${x.n}: ${x.p ? '$' + fmt(x.p) : '—'}`, { reply_markup: { inline_keyboard: [[{ text: tpl(m.page, { n: x.n }), url: x.url }], [{ text: '🔔 ' + m.al.replace(/^\S+\s/, ''), url: x.url }]] } }).then(() => done(200));
  } catch (e) { return done(200) }
};
