// Shared helpers for Telegram price alerts (api/tg.js webhook, api/alerts.js checker).
// Env (Vercel → Settings → Environment Variables): TG_BOT_TOKEN, ALERTS_KEY, KV_REST_API_URL / KV_REST_API_TOKEN (Upstash).
const KVU = () => (process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || '').replace(/\/$/, '');
const KVT = () => process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || '';
async function kv(cmds) {
  const r = await fetch(KVU() + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + KVT(), 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  return (await r.json()).map(x => x.result);
}
async function tg(method, body) {
  const r = await fetch(`https://api.telegram.org/bot${process.env.TG_BOT_TOKEN}/${method}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  return r.json().catch(() => ({}));
}
let MAP = null;   // aid -> ['c', cgid] | ['y', yahoo symbol], built by scripts/build.py
async function amap() {
  if (MAP) return MAP;
  try { MAP = await (await fetch('https://whatifstack.com/assets/alerts-map.json')).json() } catch (e) { MAP = {} }
  return MAP;
}
async function prices(items) {   // items: [{s:'c'|'y', k: cgid|yahoo}] -> {k: usd price}
  const out = {};
  const cg = [...new Set(items.filter(i => i.s === 'c').map(i => i.k))];
  for (let i = 0; i < cg.length; i += 200) {
    try {
      const j = await (await fetch('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=' + cg.slice(i, i + 200).join(','), { headers: { Accept: 'application/json' } })).json();
      for (const [k, v] of Object.entries(j || {})) if (v && v.usd) out[k] = v.usd;
    } catch (e) {}
  }
  const ys = [...new Set(items.filter(i => i.s === 'y').map(i => i.k))].slice(0, 60);
  await Promise.all(ys.map(async s => {
    try {
      const j = await (await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=1d&interval=5m`, { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack alerts)' } })).json();
      const m = ((j.chart || {}).result || [])[0].meta;
      if (m && m.regularMarketPrice) out[s] = m.regularMarketPrice / (m.currency === 'USX' ? 100 : 1);   // US cents -> dollars
    } catch (e) {}
  }));
  return out;
}
const fmt = v => v >= 1000 ? Math.round(v).toLocaleString('en-US') : v >= 1 ? (+v.toFixed(2)).toString() : (+v.toPrecision(4)).toString();
const TXT = {
  en: { hi: 'Hi! I send price alerts from whatifstack.com. Open any coin or stock there and press 🔔 Price alert.', set: '✅ Alert set: {n} {d} ${p}. Now ${c}.', up: 'rises above', dn: 'falls below',
        hit: '🔔 {n} {d} ${p}: now ${c}.', open: 'Open {n}', list: 'Your alerts:', none: 'You have no alerts.', del: 'Delete: /del <number>', gone: 'Deleted.', stop: 'All your alerts are off.', lim: 'Limit: 10 alerts. Delete one with /del <number>.', bad: 'Could not read this alert. Set it again on whatifstack.com.' },
  uk: { hi: 'Привіт! Я надсилаю сповіщення про ціну з whatifstack.com. Відкрий там будь-яку монету чи акцію і натисни 🔔 Сповіщення.', set: '✅ Сповіщення увімкнено: {n} {d} ${p}. Зараз ${c}.', up: 'вище', dn: 'нижче',
        hit: '🔔 {n} {d} ${p}: зараз ${c}.', open: 'Відкрити {n}', list: 'Твої сповіщення:', none: 'Сповіщень немає.', del: 'Видалити: /del <номер>', gone: 'Видалено.', stop: 'Усі сповіщення вимкнено.', lim: 'Ліміт — 10 сповіщень. Видали одне: /del <номер>.', bad: 'Не вдалося прочитати сповіщення. Створи його ще раз на whatifstack.com.' },
  ru: { hi: 'Привет! Я присылаю уведомления о цене с whatifstack.com. Открой там любую монету или акцию и нажми 🔔 Уведомление.', set: '✅ Уведомление включено: {n} {d} ${p}. Сейчас ${c}.', up: 'выше', dn: 'ниже',
        hit: '🔔 {n} {d} ${p}: сейчас ${c}.', open: 'Открыть {n}', list: 'Твои уведомления:', none: 'Уведомлений нет.', del: 'Удалить: /del <номер>', gone: 'Удалено.', stop: 'Все уведомления выключены.', lim: 'Лимит — 10 уведомлений. Удали одно: /del <номер>.', bad: 'Не удалось прочитать уведомление. Создай его снова на whatifstack.com.' },
};
const T = l => TXT[l] || TXT[(l || '').slice(0, 2)] || TXT.en;
const tpl = (s, o) => s.replace(/\{(\w+)\}/g, (_, k) => o[k] == null ? '' : o[k]);
module.exports = { kv, tg, amap, prices, fmt, T, tpl };
