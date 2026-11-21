// Accounts: sign in by e-mail link or Telegram, then sync the visitor's portfolios/watchlists/bonds between devices.
// Called through /api/forms?k=login|verify|tg|me|data|logout (one function: Hobby allows 12).
// Storage: Upstash Redis (same env as the forms). No passwords are stored anywhere.
//   au:tok:<token>  → e-mail, 20 min (one-time login link)
//   au:ses:<sid>    → uid, 180 days (session; the browser keeps sid in localStorage wi_sid)
//   au:user:<uid>   → {name, em|tg, at}
//   au:data:<uid>   → {v: timestamp, d: {wi_pfs, wi_wls, wi_bonds, wi_pfccy}} (max 300 KB)
// Env: KV_REST_API_URL/TOKEN (Upstash), BREVO_KEY + AUTH_FROM (e-mail links), TG_BOT_TOKEN (Telegram login check), GOOGLE_CLIENT_ID (Google sign-in).
const crypto = require('crypto');
const SES_TTL = 180 * 86400;
const LANGS = new Set('uk en ru es pt de fr it pl tr nl id vi th hi ja ko zh ar fil'.split(' '));
const MAIL = {
  uk: ['Вхід на WhatIfStack', 'Натисни кнопку, щоб увійти. Посилання діє 20 хвилин і спрацює один раз.', 'Увійти', 'Якщо ти не просив вхід — просто проігноруй цей лист.'],
  ru: ['Вход на WhatIfStack', 'Нажми кнопку, чтобы войти. Ссылка действует 20 минут и сработает один раз.', 'Войти', 'Если ты не запрашивал вход — просто проигнорируй это письмо.'],
  en: ['Sign in to WhatIfStack', 'Tap the button to sign in. The link works once and expires in 20 minutes.', 'Sign in', 'If you did not ask to sign in, just ignore this e-mail.'],
};

async function redis(cmds) {
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL, k = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!u || !k) throw new Error('no-db');
  const r = await fetch(u.replace(/\/$/, '') + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + k, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  return (await r.json()).map(x => x.result);
}
const rnd = n => crypto.randomBytes(n).toString('base64url');
const sha = s => crypto.createHash('sha256').update(s).digest('hex').slice(0, 32);

async function session(uid, prof) {
  const sid = rnd(32);
  await redis([['SET', 'au:ses:' + sid, uid, 'EX', SES_TTL], ['HSETNX', 'au:users', uid, JSON.stringify({ ...prof, at: new Date().toISOString() })], ['INCR', 'au:logins']]);
  return { sid, uid, name: prof.name || '' };
}
async function whoami(req) {
  const sid = String((req.headers || {})['x-sid'] || '');
  if (!/^[A-Za-z0-9_-]{30,60}$/.test(sid)) return null;
  const [uid] = await redis([['GET', 'au:ses:' + sid]]);
  return uid ? { sid, uid } : null;
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const send = (code, obj) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json; charset=utf-8'); res.end(JSON.stringify(obj || {})); };
  const q = req.query || {}, k = q.k, h = req.headers || {};
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  const ip = String(h['x-forwarded-for'] || '').split(',')[0].trim() || '?', hour = new Date().toISOString().slice(0, 13);
  try {
    if (k === 'login') {                       // 1. e-mail → one-time link
      const em = String(b.em || '').trim().toLowerCase().slice(0, 120), l = LANGS.has(b.l) ? b.l : 'en';
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em) || b.hp) return send(400, { e: 'email' });
      if (!process.env.BREVO_KEY) return send(503, { e: 'mail-off' });
      const [ni, ne] = await redis([['INCR', `au:rl:${hour}:${ip}`], ['INCR', `au:rl:${hour}:${sha(em)}`], ['EXPIRE', `au:rl:${hour}:${ip}`, 3700], ['EXPIRE', `au:rl:${hour}:${sha(em)}`, 3700]]);
      if (ni > 8 || ne > 3) return send(429, { e: 'limit' });
      const tok = rnd(24);
      await redis([['SET', 'au:tok:' + tok, em, 'EX', 1200]]);
      const pre = l === 'uk' ? '' : '/' + l;
      const link = `https://whatifstack.com${pre}/me/?login=${tok}`;
      const m = MAIL[l] || MAIL.en;
      const html = `<div style="font-family:Arial,sans-serif;max-width:460px;margin:auto;padding:24px"><h2 style="margin:0 0 12px">${m[0]}</h2><p>${m[1]}</p>`
        + `<p><a href="${link}" style="display:inline-block;background:#10b981;color:#fff;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:bold">${m[2]}</a></p>`
        + `<p style="color:#667;font-size:13px">${m[3]}</p><p style="color:#667;font-size:12px">WhatIfStack · whatifstack.com</p></div>`;
      const r = await fetch('https://api.brevo.com/v3/smtp/email', { method: 'POST', headers: { 'api-key': process.env.BREVO_KEY, 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ sender: { email: process.env.AUTH_FROM || 'login@whatifstack.com', name: 'WhatIfStack' }, to: [{ email: em }], subject: m[0], htmlContent: html }) });
      return r.ok ? send(200, { ok: 1 }) : send(502, { e: 'mail' });
    }
    if (k === 'verify') {                      // 2. link opened → session
      const tok = String(b.t || '');
      if (!/^[A-Za-z0-9_-]{20,40}$/.test(tok)) return send(400, { e: 'token' });
      const [em] = await redis([['GETDEL', 'au:tok:' + tok]]);
      if (!em) return send(410, { e: 'expired' });
      return send(200, await session('e:' + sha(em), { em, name: em.split('@')[0] }));
    }
    if (k === 'tg') {                          // Telegram Login Widget data, checked with the bot token
      const bot = process.env.TG_BOT_TOKEN;
      if (!bot) return send(503, { e: 'tg-off' });
      const d = {}; ['id', 'first_name', 'last_name', 'username', 'photo_url', 'auth_date'].forEach(x => { if (b[x] != null && b[x] !== '') d[x] = String(b[x]); });
      const check = Object.keys(d).sort().map(x => `${x}=${d[x]}`).join('\n');
      const hash = crypto.createHmac('sha256', crypto.createHash('sha256').update(bot).digest()).update(check).digest('hex');
      if (hash !== String(b.hash || '') || Date.now() / 1000 - +d.auth_date > 86400) return send(401, { e: 'tg' });
      return send(200, await session('t:' + d.id, { tg: d.username || d.id, name: d.first_name || d.username || 'Telegram' }));
    }
    if (k === 'tgapp') {                       // inside the Telegram Mini App (bot menu «Portfolio»): signed initData → session, no button needed
      const bot = process.env.TG_BOT_TOKEN;
      if (!bot) return send(503, { e: 'tg-off' });
      const p = new URLSearchParams(String(b.d || '')), hash = p.get('hash') || '';
      p.delete('hash');
      const check = [...p.entries()].map(([x, v]) => `${x}=${v}`).sort().join('\n');
      const secret = crypto.createHmac('sha256', 'WebAppData').update(bot).digest();
      const calc = crypto.createHmac('sha256', secret).update(check).digest('hex');
      if (calc !== hash || Date.now() / 1000 - +(p.get('auth_date') || 0) > 86400) return send(401, { e: 'tg' });
      let usr = {}; try { usr = JSON.parse(p.get('user') || '{}'); } catch (e) {}
      if (!usr.id) return send(400, { e: 'user' });
      return send(200, await session('t:' + usr.id, { tg: usr.username || String(usr.id), name: usr.first_name || usr.username || 'Telegram' }));
    }
    if (k === 'google') {                      // «Sign in with Google» (Google Identity Services): ID token checked by Google, same account as the e-mail link
      const cid = process.env.GOOGLE_CLIENT_ID;
      if (!cid) return send(503, { e: 'google-off' });
      const r = await fetch('https://oauth2.googleapis.com/tokeninfo?id_token=' + encodeURIComponent(String(b.c || '')));
      const g = r.ok ? await r.json() : {};
      if (g.aud !== cid || !['accounts.google.com', 'https://accounts.google.com'].includes(g.iss) || String(g.email_verified) !== 'true' || !g.email) return send(401, { e: 'google' });
      const em = String(g.email).toLowerCase();
      return send(200, await session('e:' + sha(em), { em, name: g.given_name || g.name || em.split('@')[0] }));
    }
    const me = await whoami(req);
    if (!me) return send(401, { e: 'session' });
    if (k === 'me') { const [u] = await redis([['HGET', 'au:users', me.uid]]); return send(200, { uid: me.uid, ...(u ? JSON.parse(u) : {}) }); }
    if (k === 'logout') { await redis([['DEL', 'au:ses:' + me.sid]]); return send(200, { ok: 1 }); }
    if (k === 'data') {
      if (req.method === 'POST') {
        const body = JSON.stringify({ v: Date.now(), d: b.d || {} });
        if (body.length > 300000) return send(413, { e: 'size' });
        await redis([['SET', 'au:data:' + me.uid, body]]);
        return send(200, { v: JSON.parse(body).v });
      }
      const [raw] = await redis([['GET', 'au:data:' + me.uid]]);
      return send(200, raw ? JSON.parse(raw) : { v: 0, d: null });
    }
    return send(400, { e: 'k' });
  } catch (e) {
    return send(e.message === 'no-db' ? 503 : 502, { e: 'server' });
  }
};
