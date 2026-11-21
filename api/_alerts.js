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
  en: { nw: '📰 News', nwask: '📰 Get our news here as soon as it is published on whatifstack.com. What to send?', nwall: '📰 All news', nwmy: '⭐ Only my assets (from the daily brief)', nwoff: '🔕 Off', nwonall: '✅ You will get every new article right here.', nwonmy: '✅ You will get news about your assets: {l}. Change the list in ☀️ Daily brief.', nwoffok: 'News is off.', nwread: '📖 Read', nwnone: 'First pick assets in ☀️ Daily brief.', pts: '🎁 My points', ptsmsg: '🎁 Your points: {p}\n🏆 Place: {r}\n👥 Friends invited: {n}\n\nHow to earn:\n• +{rf} for each friend who joins via your link (counted after the human check and channel subscription)\n• +{wb} welcome bonus\n\nWe plan to let you exchange points for gifts and crypto — the rules will be announced in @WhatIfStack.\n\nYour link: {u}', ptstop: '🏆 Top 10:', refok: '🎉 +{rf} points: a friend joined via your link! Balance: {p}. Friends: {n}.', ptsinv: '🤝 Invite and earn', cap: '🤖 Step 1 of 3 — quick check that you are a human (we keep bots out). Tap the {e}:', cap2: '🤖 Step 2 of 3 — how much is {q}?', capbad: 'Not quite — once more.', capban: 'Too many wrong answers. Try again tomorrow.', capfast: 'Too fast 🙂 Take a second and tap again.', sub: '✅ Check passed!\n\nStep 3 of 3 — join our channel @WhatIfStack (daily market wrap, charts, «what if» numbers). Then press «I joined» and the bot opens for you.', subbtn: '📣 Join the channel', subok: '✅ I joined', subno: 'I don\'t see you in the channel yet. Join and press «I joined» again.', welcome: '🎉 Welcome! The bot is open for you.', join: '📣 Join the channel — daily market wrap', dg: '☀️ Daily brief', dgask: '☀️ Pick up to 5 assets — every morning at 9:00 (Kyiv) I send their prices and 24h change.', dgon: '✅ Daily brief is on: {l}', dgoff: 'Daily brief is off.', dghi: '☀️ Good morning! Your markets, 24h:', dgdone: 'Done', dgstop: 'Turn off', wrap: '📰 Today in the markets', inv: '🤝 Invite friends: {u}\nFriends joined: {n}', nums: ['zero','one','two','three','four','five','six','seven','eight','nine','ten'], plus: 'plus', sup: '💬 Support', supask: 'Write your question or idea in one message — the team will reply here.', supok: '✅ Thanks! Your message is with the team, we will reply in this chat.', lng: '🌐 Language', lngok: '✅ Language: English', hi: '👋 Hi! I am the WhatIfStack bot.\n\n💼 Your portfolio and watchlist — right here in Telegram\n📈 Prices: send a ticker, e.g. btc, eth, nvda, gold\n🔔 Price alerts: press 🔔 on any asset page at whatifstack.com\n📣 Daily market wrap in our channel',
        pf: '💼 My portfolio', px: '📈 Prices', al: '🔔 My alerts', ch: '📣 Our channel', sh: '🤝 Share the bot', site: '🌐 whatifstack.com',
        top: 'Prices now:', nf: 'I do not know «{q}». Try a ticker: btc, eth, sol, nvda, aapl, gold.', page: 'Open {n} on WhatIfStack', share: 'Markets in plain language: prices, portfolio and price alerts in Telegram',
        cmd: { start: 'Menu', news: 'News from the site', points: 'My points and invite link', portfolio: 'My portfolio', price: 'Price: /price btc', list: 'My price alerts', share: 'Share the bot', support: 'Support', lang: 'Language', stop: 'Turn off all alerts' }, menu: 'Portfolio',
        about: 'Prices of crypto, stocks and gold, your portfolio and price alerts. whatifstack.com', desc: 'WhatIfStack: markets in plain language.\n\n💼 Portfolio and watchlist in Telegram\n📈 Prices of crypto, stocks, gold\n🔔 Price alerts\n📣 Daily market wrap' },
  uk: { nw: '📰 Новини', nwask: '📰 Отримуй наші новини тут, щойно вони виходять на whatifstack.com. Що надсилати?', nwall: '📰 Усі новини', nwmy: '⭐ Лише мої активи (з ранкового огляду)', nwoff: '🔕 Вимкнути', nwonall: '✅ Кожна нова стаття прийде сюди.', nwonmy: '✅ Надсилатиму новини про твої активи: {l}. Список змінюється в ☀️ Ранковому огляді.', nwoffok: 'Новини вимкнено.', nwread: '📖 Читати', nwnone: 'Спершу вибери активи в ☀️ Ранковому огляді.', pts: '🎁 Мої бали', ptsmsg: '🎁 Твої бали: {p}\n🏆 Місце: {r}\n👥 Запрошено друзів: {n}\n\nЯк заробити:\n• +{rf} за кожного друга, який прийде за твоїм посиланням (зараховуємо після перевірки і підписки на канал)\n• +{wb} вітальний бонус\n\nБали плануємо дати обміняти на подарунки і криптовалюту — правила оголосимо в @WhatIfStack.\n\nТвоє посилання: {u}', ptstop: '🏆 Топ-10:', refok: '🎉 +{rf} балів: друг прийшов за твоїм посиланням! Баланс: {p}. Друзів: {n}.', ptsinv: '🤝 Запросити і заробити', cap: '🤖 Крок 1 з 3 — перевірка, що ти людина (ботів не пускаємо). Натисни {e}:', cap2: '🤖 Крок 2 з 3 — скільки буде {q}?', capbad: 'Не те — ще раз.', capban: 'Забагато помилок. Спробуй завтра.', capfast: 'Занадто швидко 🙂 Секунду і натисни ще раз.', sub: '✅ Перевірку пройдено!\n\nКрок 3 з 3 — підпишись на наш канал @WhatIfStack (щоденний огляд ринку, графіки, цифри «а що якби»). Потім натисни «Я підписався» — і бот відкриється.', subbtn: '📣 Підписатися на канал', subok: '✅ Я підписався', subno: 'Поки не бачу тебе в каналі. Підпишись і натисни «Я підписався» ще раз.', welcome: '🎉 Вітаю! Бот відкритий для тебе.', join: '📣 Підписатися на канал — щоденний огляд ринку', dg: '☀️ Ранковий огляд', dgask: '☀️ Обери до 5 активів — щоранку о 9:00 (Київ) надсилатиму їхні ціни і зміну за добу.', dgon: '✅ Ранковий огляд увімкнено: {l}', dgoff: 'Ранковий огляд вимкнено.', dghi: '☀️ Доброго ранку! Твої ринки за добу:', dgdone: 'Готово', dgstop: 'Вимкнути', wrap: '📰 Сьогодні на ринках', inv: '🤝 Запроси друзів: {u}\nДрузів прийшло: {n}', nums: ['нуль','один','два','три','чотири','пʼять','шість','сім','вісім','девʼять','десять'], plus: 'плюс', sup: '💬 Підтримка', supask: 'Напиши питання чи ідею одним повідомленням — команда відповість тут.', supok: '✅ Дякуємо! Повідомлення вже в команди, відповімо в цьому чаті.', lng: '🌐 Мова', lngok: '✅ Мова: українська', hi: '👋 Привіт! Я бот WhatIfStack.\n\n💼 Твій портфель і список стеження — прямо в Telegram\n📈 Ціни: напиши тікер, наприклад btc, eth, nvda, gold\n🔔 Сповіщення про ціну: натисни 🔔 на сторінці активу на whatifstack.com\n📣 Щоденний огляд ринку — у нашому каналі',
        pf: '💼 Мій портфель', px: '📈 Ціни', al: '🔔 Мої сповіщення', ch: '📣 Наш канал', sh: '🤝 Поділитися ботом', site: '🌐 whatifstack.com',
        top: 'Ціни зараз:', nf: 'Не знаю «{q}». Спробуй тікер: btc, eth, sol, nvda, aapl, gold.', page: 'Відкрити {n} на WhatIfStack', share: 'Ринки простою мовою: ціни, портфель і сповіщення про ціну в Telegram',
        cmd: { start: 'Меню', news: 'Новини з сайту', points: 'Мої бали і посилання', portfolio: 'Мій портфель', price: 'Ціна: /price btc', list: 'Мої сповіщення', share: 'Поділитися ботом', support: 'Підтримка', lang: 'Мова', stop: 'Вимкнути всі сповіщення' }, menu: 'Портфель',
        about: 'Ціни крипти, акцій і золота, твій портфель і сповіщення про ціну. whatifstack.com', desc: 'WhatIfStack: ринки простою мовою.\n\n💼 Портфель і список стеження в Telegram\n📈 Ціни крипти, акцій, золота\n🔔 Сповіщення про ціну\n📣 Щоденний огляд ринку' },
  ru: { nw: '📰 Новости', nwask: '📰 Получай наши новости здесь, как только они выходят на whatifstack.com. Что присылать?', nwall: '📰 Все новости', nwmy: '⭐ Только мои активы (из утреннего обзора)', nwoff: '🔕 Выключить', nwonall: '✅ Каждая новая статья придёт сюда.', nwonmy: '✅ Буду присылать новости о твоих активах: {l}. Список меняется в ☀️ Утреннем обзоре.', nwoffok: 'Новости выключены.', nwread: '📖 Читать', nwnone: 'Сначала выбери активы в ☀️ Утреннем обзоре.', pts: '🎁 Мои баллы', ptsmsg: '🎁 Твои баллы: {p}\n🏆 Место: {r}\n👥 Приглашено друзей: {n}\n\nКак заработать:\n• +{rf} за каждого друга, который придёт по твоей ссылке (засчитываем после проверки и подписки на канал)\n• +{wb} приветственный бонус\n\nБаллы планируем дать обменять на подарки и криптовалюту — правила объявим в @WhatIfStack.\n\nТвоя ссылка: {u}', ptstop: '🏆 Топ-10:', refok: '🎉 +{rf} баллов: друг пришёл по твоей ссылке! Баланс: {p}. Друзей: {n}.', ptsinv: '🤝 Пригласить и заработать', cap: '🤖 Шаг 1 из 3 — проверка, что ты человек (ботов не пускаем). Нажми {e}:', cap2: '🤖 Шаг 2 из 3 — сколько будет {q}?', capbad: 'Не то — ещё раз.', capban: 'Слишком много ошибок. Попробуй завтра.', capfast: 'Слишком быстро 🙂 Секунду и нажми ещё раз.', sub: '✅ Проверка пройдена!\n\nШаг 3 из 3 — подпишись на наш канал @WhatIfStack (ежедневный обзор рынка, графики, цифры «а что если»). Потом нажми «Я подписался» — и бот откроется.', subbtn: '📣 Подписаться на канал', subok: '✅ Я подписался', subno: 'Пока не вижу тебя в канале. Подпишись и нажми «Я подписался» ещё раз.', welcome: '🎉 Добро пожаловать! Бот открыт для тебя.', join: '📣 Подписаться на канал — ежедневный обзор рынка', dg: '☀️ Утренний обзор', dgask: '☀️ Выбери до 5 активов — каждое утро в 9:00 (Киев) пришлю их цены и изменение за сутки.', dgon: '✅ Утренний обзор включён: {l}', dgoff: 'Утренний обзор выключен.', dghi: '☀️ Доброе утро! Твои рынки за сутки:', dgdone: 'Готово', dgstop: 'Выключить', wrap: '📰 Сегодня на рынках', inv: '🤝 Пригласи друзей: {u}\nДрузей пришло: {n}', nums: ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять','десять'], plus: 'плюс', sup: '💬 Поддержка', supask: 'Напиши вопрос или идею одним сообщением — команда ответит здесь.', supok: '✅ Спасибо! Сообщение уже у команды, ответим в этом чате.', lng: '🌐 Язык', lngok: '✅ Язык: русский', hi: '👋 Привет! Я бот WhatIfStack.\n\n💼 Твой портфель и список отслеживания — прямо в Telegram\n📈 Цены: напиши тикер, например btc, eth, nvda, gold\n🔔 Уведомления о цене: нажми 🔔 на странице актива на whatifstack.com\n📣 Ежедневный обзор рынка — в нашем канале',
        pf: '💼 Мой портфель', px: '📈 Цены', al: '🔔 Мои уведомления', ch: '📣 Наш канал', sh: '🤝 Поделиться ботом', site: '🌐 whatifstack.com',
        top: 'Цены сейчас:', nf: 'Не знаю «{q}». Попробуй тикер: btc, eth, sol, nvda, aapl, gold.', page: 'Открыть {n} на WhatIfStack', share: 'Рынки простым языком: цены, портфель и уведомления о цене в Telegram',
        cmd: { start: 'Меню', news: 'Новости с сайта', points: 'Мои баллы и ссылка', portfolio: 'Мой портфель', price: 'Цена: /price btc', list: 'Мои уведомления', share: 'Поделиться ботом', support: 'Поддержка', lang: 'Язык', stop: 'Выключить все уведомления' }, menu: 'Портфель',
        about: 'Цены крипты, акций и золота, твой портфель и уведомления о цене. whatifstack.com', desc: 'WhatIfStack: рынки простым языком.\n\n💼 Портфель и список отслеживания в Telegram\n📈 Цены крипты, акций, золота\n🔔 Уведомления о цене\n📣 Ежедневный обзор рынка' },
};
const M = l => MENU[l] || MENU[(l || '').slice(0, 2)] || MENU.en;
const LP = l => { l = (l || '').slice(0, 2); const ok = 'uk en ru es pt de fr it pl tr nl id vi th hi ja ko zh ar'.split(' '); return l === 'uk' ? '' : '/' + (ok.includes(l) ? l : 'en'); };
module.exports.M = M; module.exports.LP = LP;

// Prices with 24h change for the daily brief: items [{s,k}] -> {k: [price, change %]}
async function changes(items) {
  const out = {};
  const cg = [...new Set(items.filter(i => i.s === 'c').map(i => i.k))];
  if (cg.length) try {
    const j = await (await fetch('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&include_24hr_change=true&ids=' + cg.join(','), { headers: { Accept: 'application/json' } })).json();
    for (const [k, v] of Object.entries(j || {})) if (v && v.usd) out[k] = [v.usd, v.usd_24h_change];
  } catch (e) {}
  await Promise.all([...new Set(items.filter(i => i.s === 'y').map(i => i.k))].map(async s => {
    try {
      const j = await (await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=1d&interval=5m`, { headers: { 'User-Agent': 'Mozilla/5.0 (WhatIfStack brief)' } })).json();
      const m = ((j.chart || {}).result || [])[0].meta, d = m.currency === 'USX' ? 100 : 1;
      if (m && m.regularMarketPrice) out[s] = [m.regularMarketPrice / d, m.chartPreviousClose ? (m.regularMarketPrice / m.chartPreviousClose - 1) * 100 : null];
    } catch (e) {}
  }));
  return out;
}
const DG = ['btc', 'eth', 'sol', 'xrp', 'ton', 'doge', 'gold', 'silver', 'spy', 'qqq', 'nvda', 'aapl', 'tsla', 'msft'];
module.exports.changes = changes; module.exports.DG = DG;
