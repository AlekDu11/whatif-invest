# Ads log — WhatIfStack

Журнал реклами. Один рядок на день на оголошення. Ціна підписника = витрата / приріст підписників.

## Telegram Ads

Кабінет: ads.telegram.org · оплата в Gram · промо: https://t.me/WhatIfStack

### 2026-11-17 — підготовка
- Баланс кабінету: 0 Gram (поповнення — власник, через Fragment).
- База каналів: `ads/telegram/channels.csv` — 372 канали, 200 у статусі TEST; план — `ads/telegram/test_plan.md`, набори каналів — `ads/telegram/test_sets.json`.
- Увага: масовий збір через акаунт Telegram Web дав FLOOD_WAIT ~23,6 год на contacts.resolveUsername (до ~2026-11-18 20:30 Київ). Далі збирати тільки через кабінет Ads (getSimilarChannels) і публічні t.me/s/, без MTProto-запитів з акаунта власника.
- Цифри для текстів звірено з data/market.json (оновлено 2026-11-17): $100/міс з 01.2016 — внесено $13,100; BTC $216,841, S&P 500 (SPY) $30,223, золото $28,881.

| Дата | Оголошення | Кластер | CPM | Покази | Кліки | CTR | Витрата, Gram | +Підписники | Ціна підп., Gram | Нотатки |
|---|---|---|---|---|---|---|---|---|---|---|

### 2026-11-17 21:10–21:12 — запуск (за «так» власника, 5 Gram на оголошення)
Баланс 30 Gram → 5 оголошень × 5 Gram = 25, залишок 5. CPM 0,3, 1 показ/користувач, WhatIfStack виключено з показу.
- WIS A network T1 — 9 каналів (мережа seed + Digital Asset Compass, Trippier Encryption від власника) — Active
- WIS C small T1 — 50 малих каналів — Active
- WIS C small T2 — ті самі 50, текст T2 — Active
- WIS BD mid-large T1 — 40 середніх/великих — Active
- WIS Topics control T1 — EN, теми Cryptocurrencies + Investments — In Review
