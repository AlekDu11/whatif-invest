// Telegram bot @WhatIfStack_Bot (webhook). Menu with the portfolio Mini App, prices by ticker, inline mode, sharing, channel, price alerts.
// Deep link for alerts from the site: t.me/<bot>?start=a_<aid>_<u|d>_<price with p for the dot>_<lang>
// One-time setup after adding TG_BOT_TOKEN and ALERTS_KEY in Vercel env: open /api/tg?setup=<ALERTS_KEY>
// (sets the webhook, commands, menu button «Portfolio», descriptions in uk/ru/en). Inline mode also needs /setinline in @BotFather.
const { kv, tg, amap, prices, fmt, T, tpl, M, LP, DG } = require('./_alerts');
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
const refUrl = (chat) => 'https://t.me/' + BOT + (chat ? '?start=r_' + chat : '');
const shareUrl = (m, chat) => `https://t.me/share/url?url=${encodeURIComponent(refUrl(chat))}&text=${encodeURIComponent(m.share)}`;
// Points (owner 2026-11-21): +RF per verified friend (human check + channel subscription), +WB welcome bonus. Sorted set tg:pts, names tg:name:<chat>.
// Exchange for gifts/crypto is announced later; points have no cash value yet.
const RF = 10, WB = 5;
const short = (f) => ((f.first_name || 'User').slice(0, 14) + (f.last_name ? ' ' + f.last_name[0] + '.' : '')).replace(/[<>@]/g, '');
const menu = (lang, chat) => { const m = M(lang); return { inline_keyboard: [
  [{ text: m.pf, web_app: { url: `${SITE}${LP(lang)}/me/?tgapp=1` } }],
  [{ text: m.px, callback_data: 'px' }, { text: m.al, callback_data: 'al' }],
  [{ text: m.dg, callback_data: 'dg' }, { text: m.pts, callback_data: 'pts' }],
  [{ text: m.ptsinv, url: shareUrl(m, chat) }, { text: m.ch, url: CH }],
  [{ text: m.nw, callback_data: 'nw' }, { text: m.sup, callback_data: 'sup' }],
  [{ text: m.lng, callback_data: 'lng' }, { text: m.site, url: `${SITE}${LP(lang)}/?utm_source=tg_bot` }]] } };
// Gate for new users (ads t.me/<bot>?start=ad_<tag>, referrals start=r_<chat>, plain /start):
// step 1 tap the named emoji, step 2 a sum written in words (answers stored server-side, <1.2 s taps rejected, 3 mistakes = 24 h ban),
// step 3 join @WhatIfStack (checked with getChatMember; the bot must be a channel admin) → the bot opens.
// Upstash: tg:cap:<chat> (current question), tg:gate:<chat>='sub', tg:ban:<chat>, tg:human, tg:src:<chat>, tg:refby:<chat>, tg:refs (hash),
// counters tg:ads <tag>:start|pass|fail|sub|subunk. Per-tag channel invite links tg:inv:<tag>. Stats: /api/tg?stats=<ALERTS_KEY>
const EMO = ['🪙', '🍎', '🚗', '🐶', '⚽', '🌙', '🎸', '🌵'];
const rnd = n => Math.floor(Math.random() * n);
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = rnd(i + 1); [a[i], a[j]] = [a[j], a[i]] } return a; };
function question(r, m) {
  if (r === 1) { const pick = shuffle(EMO).slice(0, 4), ok = pick[rnd(4)];
    return { a: ok, text: tpl(m.cap, { e: ok }), kb: { inline_keyboard: [pick.map(e => ({ text: e, callback_data: 'cap:' + e }))] } }; }
  const x = 1 + rnd(5), y = 1 + rnd(5), ans = x + y, opts = new Set([ans]);
  while (opts.size < 4) opts.add(2 + rnd(9));
  return { a: String(ans), text: tpl(m.cap2, { q: `${m.nums[x]} ${m.plus} ${m.nums[y]}` }), kb: { inline_keyboard: [shuffle([...opts]).map(n => ({ text: String(n), callback_data: 'cap:' + n }))] } };
}
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
    out.webhook = await tg('setWebhook', { url: host + '/api/tg/', secret_token: process.env.ALERTS_KEY, allowed_updates: ['message', 'callback_query', 'inline_query'] });
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
    const [ads, users, human, dg, pts, nwl] = await kv([['HGETALL', 'tg:ads'], ['SCARD', 'tg:users'], ['SCARD', 'tg:human'], ['SCARD', 'tg:dgusers'], ['ZCARD', 'tg:pts'], ['SMEMBERS', 'tg:nwlangs']]);
    const o = {}; for (let i = 0; i < (ads || []).length; i += 2) o[ads[i]] = +ads[i + 1];
    return done(200, { ads: o, users, human, daily_brief: dg, with_points: pts, news: nwl ? Object.fromEntries(await Promise.all(nwl.map(async l => [l, (await kv([['SCARD', `tg:nwu:${l}`]]))[0]]))) : {} });
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
    const ask = async (r, w, tag, pre) => { const qn = question(r, m);
      await kv([['SET', `tg:cap:${chat}`, JSON.stringify({ r, a: qn.a, w, tag, ts: Date.now() }), 'EX', 86400]]);
      return say((pre ? pre + '\n\n' : '') + qn.text, { reply_markup: qn.kb }); };
    const subMsg = async (tag, pre) => say((pre ? pre + '\n\n' : '') + m.sub, { reply_markup: { inline_keyboard: [[{ text: m.subbtn, url: await invite(tag) }], [{ text: m.subok, callback_data: 'sub' }]] } });
    const gateStart = async (tag) => { await kv([['DEL', `tg:gate:${chat}`], ['SET', `tg:src:${chat}`, tag], ['SET', `tg:lang:${chat}`, lang, 'NX']]); return ask(1, 0, tag); };
    const dgKb = async () => { const map = await amap(), [cur] = await kv([['SMEMBERS', `tg:dg:${chat}`]]), on = new Set(cur || []);
      const list = DG.filter(i => map[i]).map(i => ({ text: (on.has(i) ? '✅ ' : '') + (map[i][2] || i.toUpperCase()), callback_data: 'dg:' + i }));
      const rows = []; for (let i = 0; i < list.length; i += 4) rows.push(list.slice(i, i + 4));
      rows.push([{ text: m.dgdone, callback_data: 'dg:ok' }, { text: m.dgstop, callback_data: 'dg:off' }]);
      return { inline_keyboard: rows }; };
    const showPts = async () => {
      const [p, rk, n, top] = await kv([['ZSCORE', 'tg:pts', String(chat)], ['ZREVRANK', 'tg:pts', String(chat)], ['HGET', 'tg:refs', String(chat)], ['ZREVRANGE', 'tg:pts', 0, 9, 'WITHSCORES']]);
      const ids = [], sc = []; for (let i = 0; i < (top || []).length; i += 2) { ids.push(top[i]); sc.push(Math.round(+top[i + 1])); }
      const names = ids.length ? await kv(ids.map(c => ['GET', `tg:name:${c}`])) : [];
      const medal = ['🥇', '🥈', '🥉'];
      const board = ids.map((c, i) => `${medal[i] || (i + 1) + '.'} ${names[i] || 'User'} — ${sc[i]}${c === String(chat) ? ' ⬅️' : ''}`).join('\n');
      return say(tpl(m.ptsmsg, { p: Math.round(+p || 0), r: rk == null ? '—' : rk + 1, n: n || 0, rf: RF, wb: WB, u: refUrl(chat) }) + (board ? '\n\n' + m.ptstop + '\n' + board : ''),
        { reply_markup: { inline_keyboard: [[{ text: m.ptsinv, url: shareUrl(m, chat) }], [{ text: '⬅️ Menu', callback_data: 'menu' }]] } });
    };
    const [capRaw, gate, ban] = await kv([['GET', `tg:cap:${chat}`], ['GET', `tg:gate:${chat}`], ['GET', `tg:ban:${chat}`]]);
    const isAdmin = admin && String(chat) === String(admin);
    if (!isAdmin && (capRaw || gate || ban)) {                 // user is inside the gate: only gate answers count
      if (ban) { if (cb) await tg('answerCallbackQuery', { callback_query_id: cb.id }); return say(m.capban).then(() => done(200)); }
      let st = {}; try { st = JSON.parse(capRaw || '{}') } catch (e) {}
      if (cb && capRaw && /^cap:/.test(cb.data)) {
        await tg('answerCallbackQuery', { callback_query_id: cb.id });
        if (Date.now() - (st.ts || 0) < 1200) return say(m.capfast).then(() => done(200));
        if (cb.data.slice(4) === st.a) {
          if (st.r === 1) return ask(2, st.w, st.tag).then(() => done(200));
          await kv([['DEL', `tg:cap:${chat}`], ['SET', `tg:gate:${chat}`, 'sub', 'EX', 30 * 86400], ['HINCRBY', 'tg:ads', st.tag + ':pass', 1]]);
          return subMsg(st.tag).then(() => done(200));
        }
        const w = (st.w || 0) + 1;
        await kv([['HINCRBY', 'tg:ads', st.tag + ':fail', 1]]);
        if (w >= 3) { await kv([['DEL', `tg:cap:${chat}`], ['SET', `tg:ban:${chat}`, '1', 'EX', 86400]]); return say(m.capban).then(() => done(200)); }
        return ask(st.r, w, st.tag, m.capbad).then(() => done(200));
      }
      if (cb && gate === 'sub' && cb.data === 'sub') {
        await tg('answerCallbackQuery', { callback_query_id: cb.id });
        const [src, refby] = await kv([['GET', `tg:src:${chat}`], ['GET', `tg:refby:${chat}`]]); const tag = src || 'organic';
        const r = await tg('getChatMember', { chat_id: '@WhatIfStack', user_id: from.id });
        const st2 = r && r.result && r.result.status, inCh = ['member', 'administrator', 'creator'].includes(st2) || (st2 === 'restricted' && r.result.is_member);
        if (r && r.ok && !inCh) return subMsg(tag, m.subno).then(() => done(200));
        await kv([['DEL', `tg:gate:${chat}`], ['SADD', 'tg:human', String(chat)], ['HINCRBY', 'tg:ads', tag + (r && r.ok ? ':sub' : ':subunk'), 1],
          ['ZINCRBY', 'tg:pts', WB, String(chat)], ['SET', `tg:name:${chat}`, short(from)]]);
        if (refby) {
          const [n, p, rl] = await kv([['HINCRBY', 'tg:refs', refby, 1], ['ZINCRBY', 'tg:pts', RF, refby], ['GET', `tg:lang:${refby}`]]);
          await tg('sendMessage', { chat_id: refby, text: tpl(M(rl || 'en').refok, { rf: RF, p: Math.round(p), n }), reply_markup: { inline_keyboard: [[{ text: M(rl || 'en').pts, callback_data: 'pts' }]] } });
        }
        await say(m.welcome + '\n\n' + m.hi, { reply_markup: menu(lang, chat) });
        return say(m.dgask, { reply_markup: await dgKb() }).then(() => done(200));
      }
      if (cb) await tg('answerCallbackQuery', { callback_query_id: cb.id });
      if (gate === 'sub') return subMsg(st.tag || 'organic').then(() => done(200));
      return ask(st.r || 1, st.w || 0, st.tag || 'organic').then(() => done(200));
    }
    const ids = await kv([['SMEMBERS', `al:chat:${chat}`]]).then(r => (r[0] || []).sort((a, b) => a - b));
    const listAlerts = async () => {
      if (!ids.length) return say(t.none + '\n\n' + t.hi);
      const rows = await kv([['HMGET', 'al:items', ...ids]]);
      const ls = (rows[0] || []).map((r, i) => { try { const a = JSON.parse(r); return `${i + 1}. ${a.n} ${a.d === 'u' ? t.up : t.dn} $${fmt(a.p)}` } catch (e) { return null } }).filter(Boolean);
      return say(t.list + '\n' + ls.join('\n') + '\n\n' + t.del);
    };
    const topPrices = async () => {
      const qs = (await Promise.all(TOP.map(i => quote(lang, i)))).filter(x => x && x.p);
      return say(m.top + '\n' + qs.map(x => `• ${x.n}: $${fmt(x.p)}`).join('\n') + '\n\n' + m.nf.split('.')[1].trim(), { reply_markup: menu(lang, chat) });
    };
    if (cb) {
      await tg('answerCallbackQuery', { callback_query_id: cb.id });
      if (cb.data === 'nw' || /^nw:/.test(cb.data)) {           // news from the site → this chat (sent by api/alerts.js from data/feed/<lang>.json)
        const v = cb.data.slice(3), fl = lang.slice(0, 2), [old] = await kv([['GET', `tg:nwl:${chat}`]]);
        if (!v) { await say(m.nwask, { reply_markup: { inline_keyboard: [[{ text: m.nwall, callback_data: 'nw:all' }], [{ text: m.nwmy, callback_data: 'nw:my' }], [{ text: m.nwoff, callback_data: 'nw:off' }]] } }); return done(200); }
        const cmds = old ? [['SREM', `tg:nwu:${old}`, String(chat)]] : [];
        if (v === 'off') { await kv([...cmds, ['DEL', `tg:nw:${chat}`, `tg:nwl:${chat}`]]); await say(m.nwoffok, { reply_markup: menu(lang, chat) }); return done(200); }
        const [cur] = await kv([['SMEMBERS', `tg:dg:${chat}`]]);
        if (v === 'my' && !(cur && cur.length)) { await say(m.nwnone, { reply_markup: await dgKb() }); return done(200); }
        await kv([...cmds, ['SET', `tg:nw:${chat}`, v], ['SET', `tg:nwl:${chat}`, fl], ['SADD', `tg:nwu:${fl}`, String(chat)], ['SADD', 'tg:nwlangs', fl]]);
        const map = await amap();
        await say(v === 'all' ? m.nwonall : tpl(m.nwonmy, { l: cur.map(i => (map[i] || [])[2] || i.toUpperCase()).join(', ') }), { reply_markup: menu(lang, chat) });
        return done(200);
      }
      if (cb.data === 'menu') { await say(m.hi, { reply_markup: menu(lang, chat) }); return done(200); }
      if (cb.data === 'pts') { await showPts(); return done(200); }
      if (cb.data === 'dg') { await say(m.dgask, { reply_markup: await dgKb() }); return done(200); }
      if (/^dg:/.test(cb.data)) {
        const v = cb.data.slice(3);
        if (v === 'off') { await kv([['DEL', `tg:dg:${chat}`], ['SREM', 'tg:dgusers', String(chat)]]); await say(m.dgoff, { reply_markup: menu(lang, chat) }); return done(200); }
        if (v === 'ok') { const [cur] = await kv([['SMEMBERS', `tg:dg:${chat}`]]), map = await amap();
          await say(cur && cur.length ? tpl(m.dgon, { l: cur.map(i => (map[i] || [])[2] || i.toUpperCase()).join(', ') }) : m.dgoff, { reply_markup: menu(lang, chat) }); return done(200); }
        const [has, cnt] = await kv([['SISMEMBER', `tg:dg:${chat}`, v], ['SCARD', `tg:dg:${chat}`]]);
        if (has) await kv([['SREM', `tg:dg:${chat}`, v]]);
        else if (cnt < 5) await kv([['SADD', `tg:dg:${chat}`, v], ['SADD', 'tg:dgusers', String(chat)], ['SET', `tg:lang:${chat}`, lang, 'NX']]);
        const [left] = await kv([['SCARD', `tg:dg:${chat}`]]); if (!left) await kv([['SREM', 'tg:dgusers', String(chat)]]);
        await tg('editMessageReplyMarkup', { chat_id: chat, message_id: msg.message_id, reply_markup: await dgKb() });
        return done(200);
      }
      if (cb.data === 'px') await topPrices(); else if (cb.data === 'al') await listAlerts();
      else if (cb.data === 'sup') { await kv([['SET', `tg:sup:${chat}`, '1', 'EX', 3600]]); await say(m.supask, { reply_markup: { force_reply: true } }); }
      else if (cb.data === 'lng') await say(m.lng, { reply_markup: { inline_keyboard: [LANGS.slice(0, 4), LANGS.slice(4)].map(r => r.map(([c, n]) => ({ text: n, callback_data: 'l:' + c }))) } });
      else if (/^l:[a-z]{2}$/.test(cb.data)) { lang = cb.data.slice(2); await kv([['SET', `tg:lang:${chat}`, lang]]); m = M(lang); t = T(lang); await say(m.lngok + '\n\n' + m.hi, { reply_markup: menu(lang, chat) }); }
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
      return say(m.supok, { reply_markup: menu(lang, chat) }).then(() => done(200));
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
      return say(tpl(t.set, { n: al.n, d: dir === 'u' ? t.up : t.dn, p: fmt(price), c: now ? fmt(now) : '—' }), { reply_markup: menu(lg || lang, chat) }).then(() => done(200));
    }
    if (/^\/start (ad|r)_[\w-]{1,20}$/.test(text) || text === '/start') {   // new visitor from an ad, a friend's link or plain start → gate
      const arg = text.slice(7), [isNew, hum] = await kv([['SADD', 'tg:users', String(chat)], ['SISMEMBER', 'tg:human', String(chat)]]);
      if (!isNew || hum) return say(m.hi, { reply_markup: menu(lang, chat) }).then(() => done(200));
      let tag = 'organic';
      if (/^ad_/.test(arg)) tag = arg.slice(3);
      else if (/^r_\d+$/.test(arg) && arg.slice(2) !== String(chat)) { tag = 'ref'; await kv([['SET', `tg:refby:${chat}`, arg.slice(2)]]); }
      await kv([['HINCRBY', 'tg:ads', tag + ':start', 1]]);
      return gateStart(tag).then(() => done(200));
    }
    if (/^\/news/.test(text)) return say(m.nwask, { reply_markup: { inline_keyboard: [[{ text: m.nwall, callback_data: 'nw:all' }], [{ text: m.nwmy, callback_data: 'nw:my' }], [{ text: m.nwoff, callback_data: 'nw:off' }]] } }).then(() => done(200));
    if (/^\/(invite|points)/.test(text)) return showPts().then(() => done(200));
    if (/^\/(start|menu|help)\b/.test(text)) { await kv([['SADD', 'tg:users', String(chat)]]); return say(m.hi, { reply_markup: menu(lang, chat) }).then(() => done(200)); }
    if (/^\/portfolio/.test(text)) return say(m.pf, { reply_markup: { inline_keyboard: [[{ text: m.pf, web_app: { url: `${SITE}${LP(lang)}/me/?tgapp=1` } }]] } }).then(() => done(200));
    if (/^\/share/.test(text)) return say(m.share + '\n' + refUrl(chat), { reply_markup: { inline_keyboard: [[{ text: m.sh, url: `https://t.me/share/url?url=${encodeURIComponent(refUrl(chat))}&text=${encodeURIComponent(m.share)}` }]] } }).then(() => done(200));
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
    if (!aid) return say(tpl(m.nf, { q: qtext.slice(0, 30) }), { reply_markup: menu(lang, chat) }).then(() => done(200));
    const x = await quote(lang, aid);
    return say(`${x.n}: ${x.p ? '$' + fmt(x.p) : '—'}`, { reply_markup: { inline_keyboard: [[{ text: tpl(m.page, { n: x.n }), url: x.url }], [{ text: '🔔 ' + m.al.replace(/^\S+\s/, ''), url: x.url }]] } }).then(() => done(200));
  } catch (e) { return done(200) }
};
