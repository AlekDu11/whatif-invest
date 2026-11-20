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

// Bot menu, prices, sharing (api/tg.js)
const MENU = {
  en: { hi: '👋 Hi! I am the WhatIfStack bot.\n\n💼 Your portfolio and watchlist — right here in Telegram\n📈 Prices: send a ticker, e.g. btc, eth, nvda, gold\n🔔 Price alerts: press 🔔 on any asset page at whatifstack.com\n📣 Daily market wrap in our channel',
        pf: '💼 My portfolio', px: '📈 Prices', al: '🔔 My alerts', ch: '📣 Our channel', sh: '🤝 Share the bot', site: '🌐 whatifstack.com',
        top: 'Prices now:', nf: 'I do not know «{q}». Try a ticker: btc, eth, sol, nvda, aapl, gold.', page: 'Open {n} on WhatIfStack', share: 'Markets in plain language: prices, portfolio and price alerts in Telegram',
        cmd: { start: 'Menu', portfolio: 'My portfolio', price: 'Price: /price btc', list: 'My price alerts', share: 'Share the bot', stop: 'Turn off all alerts' }, menu: 'Portfolio',
        about: 'Prices of crypto, stocks and gold, your portfolio and price alerts. whatifstack.com', desc: 'WhatIfStack: markets in plain language.\n\n💼 Portfolio and watchlist in Telegram\n📈 Prices of crypto, stocks, gold\n🔔 Price alerts\n📣 Daily market wrap' },
  uk: { hi: '👋 Привіт! Я бот WhatIfStack.\n\n💼 Твій портфель і список стеження — прямо в Telegram\n📈 Ціни: напиши тікер, наприклад btc, eth, nvda, gold\n🔔 Сповіщення про ціну: натисни 🔔 на сторінці активу на whatifstack.com\n📣 Щоденний огляд ринку — у нашому каналі',
        pf: '💼 Мій портфель', px: '📈 Ціни', al: '🔔 Мої сповіщення', ch: '📣 Наш канал', sh: '🤝 Поділитися ботом', site: '🌐 whatifstack.com',
        top: 'Ціни зараз:', nf: 'Не знаю «{q}». Спробуй тікер: btc, eth, sol, nvda, aapl, gold.', page: 'Відкрити {n} на WhatIfStack', share: 'Ринки простою мовою: ціни, портфель і сповіщення про ціну в Telegram',
        cmd: { start: 'Меню', portfolio: 'Мій портфель', price: 'Ціна: /price btc', list: 'Мої сповіщення', share: 'Поділитися ботом', stop: 'Вимкнути всі сповіщення' }, menu: 'Портфель',
        about: 'Ціни крипти, акцій і золота, твій портфель і сповіщення про ціну. whatifstack.com', desc: 'WhatIfStack: ринки простою мовою.\n\n💼 Портфель і список стеження в Telegram\n📈 Ціни крипти, акцій, золота\n🔔 Сповіщення про ціну\n📣 Щоденний огляд ринку' },
  ru: { hi: '👋 Привет! Я бот WhatIfStack.\n\n💼 Твой портфель и список отслеживания — прямо в Telegram\n📈 Цены: напиши тикер, например btc, eth, nvda, gold\n🔔 Уведомления о цене: нажми 🔔 на странице актива на whatifstack.com\n📣 Ежедневный обзор рынка — в нашем канале',
        pf: '💼 Мой портфель', px: '📈 Цены', al: '🔔 Мои уведомления', ch: '📣 Наш канал', sh: '🤝 Поделиться ботом', site: '🌐 whatifstack.com',
        top: 'Цены сейчас:', nf: 'Не знаю «{q}». Попробуй тикер: btc, eth, sol, nvda, aapl, gold.', page: 'Открыть {n} на WhatIfStack', share: 'Рынки простым языком: цены, портфель и уведомления о цене в Telegram',
        cmd: { start: 'Меню', portfolio: 'Мой портфель', price: 'Цена: /price btc', list: 'Мои уведомления', share: 'Поделиться ботом', stop: 'Выключить все уведомления' }, menu: 'Портфель',
        about: 'Цены крипты, акций и золота, твой портфель и уведомления о цене. whatifstack.com', desc: 'WhatIfStack: рынки простым языком.\n\n💼 Портфель и список отслеживания в Telegram\n📈 Цены крипты, акций, золота\n🔔 Уведомления о цене\n📣 Ежедневный обзор рынка' },
};
const M = l => MENU[l] || MENU[(l || '').slice(0, 2)] || MENU.en;
const LP = l => { l = (l || '').slice(0, 2); const ok = 'uk en ru es pt de fr it pl tr nl id vi th hi ja ko zh ar'.split(' '); return l === 'uk' ? '' : '/' + (ok.includes(l) ? l : 'en'); };
module.exports.M = M; module.exports.LP = LP;
