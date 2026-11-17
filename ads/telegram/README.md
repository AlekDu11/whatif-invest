# Telegram Ads — автоматизація

## Як це працює
1. **GitHub Actions** (`.github/workflows/ads-telegram.yml`, 09:17 і 19:43 Київ) через офіційний Telegram Ads API:
   - `apply` — виконує дії з `approved.json`, які власник підтвердив словом «так» (нові оголошення, бюджет, CPM, пауза/старт);
   - `guard` — сам ставить на паузу збиткові оголошення (CTR < 0,3% після 3000 показів; 1,5 Gram без підписок; CPA > 2× медіани). Пауза не витрачає грошей;
   - `autopilot` — доливає бюджет переможцям (CPA ≤ цілі), **тільки якщо власник увімкнув** `autopilot.enabled` і задав `weekly_spend_cap` у `config.json`;
   - `check` — перевіряє нових кандидатів з `data/candidates.txt` по публічних сторінках t.me/s/ і додає в `channels.csv`;
   - `report` — `report.md`, `data/daily.csv`, `data/ads.json`, `data/subs.json`.
2. **Claude щодня** (scheduled task, вбудований браузер на комп'ютері власника):
   - читає `report.md`, пише власнику 3–5 рядків;
   - раз на 2–3 дні розширює базу: `tools/expand_similar.js` у кабінеті Ads від каналів-переможців → `data/candidates.txt`;
   - готує нові оголошення (переможця розбиває на підгрупи по 10–20 каналів, нові пачки каналів, новий текст замість гіршого) і просить «так»; після «так» дописує їх у `approved.json` → Actions запускає.

## Що потрібно від власника (один раз)
1. ads.telegram.org → API → **Copy Token**.
2. GitHub → репо whatif-invest → Settings → Secrets and variables → Actions → **New repository secret**: назва `TG_ADS_TOKEN`, значення — токен.
   (Токен не передавати в чат і не комітити.)
3. За бажанням — автопілот: у `config.json` поставити `weekly_spend_cap` (напр. 30) і `autopilot.enabled: true`. Тоді переможцям бюджет доливається без окремого «так», але не більше ліміту на тиждень.

## Стратегія масштабування
- Кластер → оголошення на 10–50 каналів. Через 3–4 дні: переможець (CPA ≤ медіани, ≥5 підписок) розбивається на 2–3 оголошення по підгрупах, щоб знайти найдешевші канали; програвшi — пауза.
- Від каналів-переможців — «similar channels» → нова пачка на тест.
- На переможцях пробуємо CPM −20% (дешевше) і +30% (більше охоплення), лишаємо кращий CPA.
- 2 тексти на кластер; гірший після 3 днів міняємо на новий.
- **Ніяких запитів через акаунт Telegram власника** (Telegram Web/MTProto) — це дало FLOOD_WAIT ~24 год. Тільки кабінет Ads, Ads API і публічні t.me/s/.

## Формат approved.json
```json
[{"id": "2026-11-21-c-split-1", "type": "create", "approved": "2026-11-21 owner «так» у чаті",
  "title": "WIS C split 1 T1", "text": "...", "cpm": 0.3, "budget": 5,
  "channels": ["CryptoZInsights", "Cryptos_Insights"]},
 {"id": "2026-11-21-ad2-plus5", "type": "increase_budget", "ad_id": 2, "amount": 5, "approved": "..."}]
```
Типи: `create`, `increase_budget`, `cpm`, `pause`, `unpause`. Кожна дія виконується один раз.
