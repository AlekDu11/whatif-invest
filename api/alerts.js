// Price-alert checker: GET /api/alerts?key=<ALERTS_KEY>. Called every ~10 minutes by .github/workflows/alerts.yml.
const { kv, tg, amap, prices, changes, fmt, T, tpl, M, LP } = require('./_alerts');
// Daily brief (users pick up to 5 assets in the bot): from 9:00 Kyiv the first run of the day queues everyone in tg:dgusers,
// every run sends up to 150 from the queue tg:dgq. Users who blocked the bot are removed.
// News push: every run, for each language with subscribers (tg:nwlangs → tg:nwu:<lang>), new items of data/feed/<lang>.json
// (refreshed by feed.yml on every content push) go to the chats right away. tg:nw:<chat> = all | my (only tags matching the daily-brief assets).
// First run per language only remembers what exists (no flood of old posts). Seen = tg:nws:<lang> (keys of the newest 30 items), tg:nwlast:<lang> marks the language as initialised.
async function news() {
  const [langs] = await kv([['SMEMBERS', 'tg:nwlangs']]);
  let sent = 0;
  for (const l of langs || []) {
    let F; try { F = await (await fetch(`https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/data/feed/${l}.json?t=${Date.now()}`)).json() } catch (e) { continue }
    const items = (F.items || []).filter(x => x.s && x.d).sort((a, b) => b.d.localeCompare(a.d)).slice(0, 30);
    const [init, seen] = await kv([['GET', `tg:nwlast:${l}`], ['SMEMBERS', `tg:nws:${l}`]]);
    const have = new Set(seen || []), key = x => x.k + '/' + x.s;
    const fresh = init ? items.filter(x => !have.has(key(x))).slice(0, 3).reverse() : [];   // at most 3 per run, the rest is marked as seen
    if (items.length) await kv([['SET', `tg:nwlast:${l}`, items[0].d], ['DEL', `tg:nws:${l}`], ['SADD', `tg:nws:${l}`, ...items.map(key)]]);
    if (!fresh.length) continue;
    const [us] = await kv([['SMEMBERS', `tg:nwu:${l}`]]);
    if (!us || !us.length) continue;
    const modes = await kv(us.flatMap(c => [['GET', `tg:nw:${c}`], ['SMEMBERS', `tg:dg:${c}`]]));
    const m = M(l), lp = LP(l);
    for (const x of fresh) {
      const url = `https://whatifstack.com${lp}/read/?k=${x.k}&s=${encodeURIComponent(x.s)}&utm_source=tg_news`;
      const esc = v => String(v || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      const cap = `<b>${esc(x.t)}</b>\n\n${esc((x.x || '').slice(0, 600))}`;
      const kb = { inline_keyboard: [[{ text: m.nwread, url }], [{ text: m.nw, callback_data: 'nw' }]] };
      const to = us.filter((c, i) => modes[2 * i] === 'all' || (modes[2 * i] === 'my' && (modes[2 * i + 1] || []).some(a => (x.g || []).includes(a))));
      for (let i = 0; i < to.length; i += 25) await Promise.all(to.slice(i, i + 25).map(async c => {
        let r = x.cv ? await tg('sendPhoto', { chat_id: c, photo: x.cv, caption: cap, parse_mode: 'HTML', reply_markup: kb }) : null;
        if (!r || !r.ok) r = await tg('sendMessage', { chat_id: c, text: cap, parse_mode: 'HTML', reply_markup: kb });
        if (r && r.ok) sent++; else if (r && r.error_code === 403) await kv([['SREM', `tg:nwu:${l}`, String(c)], ['DEL', `tg:nw:${c}`, `tg:nwl:${c}`]]);
      }));
    }
  }
  return sent;
}
async function brief() {
  const now = new Date(), h = +now.toLocaleString('en-GB', { timeZone: 'Europe/Kyiv', hour: '2-digit', hour12: false });
  const day = now.toLocaleDateString('en-CA', { timeZone: 'Europe/Kyiv' });
  if (h >= 9) {
    const [first] = await kv([['SET', `tg:dgday:${day}`, '1', 'NX', 'EX', 172800]]);
    if (first === 'OK') { const [us] = await kv([['SMEMBERS', 'tg:dgusers']]); if (us && us.length) await kv([['RPUSH', 'tg:dgq', ...us]]); }
  }
  const [batch] = await kv([['LPOP', 'tg:dgq', 150]]);
  const chats = batch ? [].concat(batch) : [];
  if (!chats.length) return 0;
  const map = await amap();
  const rows = await kv(chats.flatMap(c => [['SMEMBERS', `tg:dg:${c}`], ['GET', `tg:lang:${c}`]]));
  const subs = chats.map((c, i) => ({ c, a: (rows[2 * i] || []).filter(x => map[x]), l: rows[2 * i + 1] || 'en' })).filter(x => x.a.length);
  const px = await changes([...new Set(subs.flatMap(x => x.a))].map(a => ({ s: map[a][0], k: map[a][1] })));
  let sent = 0;
  for (let i = 0; i < subs.length; i += 25) await Promise.all(subs.slice(i, i + 25).map(async x => {
    const m = M(x.l), lp = LP(x.l);
    const lines = x.a.map(a => { const v = px[map[a][1]]; if (!v) return null; const ch = v[1];
      return `${ch == null ? '•' : ch >= 0 ? '🟢' : '🔴'} ${map[a][2] || a.toUpperCase()}: $${fmt(v[0])}${ch == null ? '' : ` (${ch >= 0 ? '+' : ''}${ch.toFixed(1)}%)`}`; }).filter(Boolean);
    if (!lines.length) return;
    const r = await tg('sendMessage', { chat_id: x.c, text: m.dghi + '\n\n' + lines.join('\n'), disable_web_page_preview: true, reply_markup: { inline_keyboard: [
      [{ text: m.wrap, url: `https://whatifstack.com${lp}/blog/?utm_source=tg_brief` }], [{ text: m.ch, url: 'https://t.me/WhatIfStack' }, { text: m.dg, callback_data: 'dg' }]] } });
    if (r && r.ok) sent++; else if (r && r.error_code === 403) await kv([['SREM', 'tg:dgusers', String(x.c)], ['DEL', `tg:dg:${x.c}`]]);
  }));
  return sent;
}
module.exports = async (req, res) => {
  const done = (c, o) => { res.statusCode = c; res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store'); res.end(JSON.stringify(o || {})) };
  if (!process.env.TG_BOT_TOKEN || (req.query || {}).key !== process.env.ALERTS_KEY) return done(403);
  const all = (await kv([['HGETALL', 'al:items']]))[0] || [];
  const items = [];
  for (let i = 0; i < all.length; i += 2) { try { items.push(JSON.parse(all[i + 1])) } catch (e) {} }
  let briefs = 0, newsSent = 0; try { briefs = await brief() } catch (e) {} try { newsSent = await news() } catch (e) {}
  if (!items.length) return done(200, { alerts: 0, briefs, news: newsSent });
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
  return done(200, { alerts: items.length, priced: Object.keys(px).length, sent, briefs, news: newsSent });
};
