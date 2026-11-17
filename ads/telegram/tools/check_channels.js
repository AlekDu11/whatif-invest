// Run in the built-in browser on any https://t.me/s/<channel> page (same-origin fetch of public previews).
// Public pages only: no account calls. Checks ~20 latest posts per channel.
// Usage: window.LIST = ["user1", ...]; run repeatedly (it stops after ~38 s) until done === total,
// then JSON.stringify(Object.values(SIG)) → ads/telegram/data/check_YYYY-MM-DD.json
window.SIG = window.SIG || {};
window.ci = window.ci || 0;
const pv = v => { if (!v) return 0; v = v.replace(',', '.'); const m = parseFloat(v); return /K/i.test(v) ? m * 1e3 : /M/i.test(v) ? m * 1e6 : m; };
async function sig(u) {
  try {
    const r = await fetch('/s/' + u); if (!r.ok) return SIG[u] = { u, err: r.status };
    const d = new DOMParser().parseFromString(await r.text(), 'text/html');
    const msgs = [...d.querySelectorAll('.tgme_widget_message')];
    const txt = msgs.map(m => m.querySelector('.tgme_widget_message_text')?.innerText || '').join(' \n ');
    const views = msgs.map(m => pv(m.querySelector('.tgme_widget_message_views')?.innerText)).filter(x => x > 0).sort((a, b) => a - b);
    const dates = msgs.map(m => m.querySelector('time')?.getAttribute('datetime')).filter(Boolean).sort();
    const subsTxt = [...d.querySelectorAll('.tgme_channel_info_counter')].find(c => /subscriber/.test(c.innerText))?.querySelector('.counter_value')?.innerText;
    const lat = (txt.match(/[A-Za-z]/g) || []).length, cyr = (txt.match(/[Ѐ-ӿ]/g) || []).length;
    const oth = (txt.match(/[^\x00-\x7FЀ-ӿ\s\p{Emoji}\p{P}\p{S}\d]/gu) || []).length;
    const scam = [...new Set((txt.match(/zooab|movanft|daily (return|income|profit)|vip (investment|plan)|invite code|three-tier|team reward|referral (reward|rebate)|withdraw/gi) || []).map(s => s.toLowerCase()))].join(',');
    const med = views.length ? views[Math.floor(views.length / 2)] : 0;
    const subs = Math.round(pv(subsTxt));
    return SIG[u] = { u, subs, posts: msgs.length, last: dates[dates.length - 1] || null, mv: Math.round(med),
      err: subs ? Math.round(100 * med / subs) : null,
      lang: lat > cyr * 2 && lat > oth * 2 ? 'en' : (cyr > lat ? 'ru/uk' : 'other'), scam };
  } catch (e) { return SIG[u] = { u, err: String(e) }; }
}
const t0 = Date.now();
while (ci < LIST.length && Date.now() - t0 < 38000) { await sig(LIST[ci]); ci++; }
({ done: ci, total: LIST.length });
