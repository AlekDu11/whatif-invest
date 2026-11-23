# SEO quality log — «quality + SEO» task

Rules: ≤ 5 pages per run; each page changed at most once per 30 days; never URLs/slugs; only that page's own title / description / lead (asset pages: only the asset's own data). After 14 days fill «result» (clicks / CTR / position before → after); revert if clearly worse.

date | url | query | impressions | position | CTR | what changed | result after 14 days
---|---|---|---|---|---|---|---
2026-11-23 | /ja/blog/how-to-buy-bitcoin/ | 仮想通貨 買い方 (17 / 15.5); 暗号資産 買い方 15 / 24.5; ビットコイン 購入 15 / 30.1; ビットコイン 買い方 23 / 71.1 | 195 | 49.9 | 0 % (0 clicks) | title «ビットコインの買い方:仮想通貨(暗号資産)を1,000円から購入する6ステップ», description (6 steps, 1,000円), lead answers in 2 sentences (6 steps, 金融庁 registered exchange → KYC → JPY → buy); new cover. Live check OK (no raw {{ }}, 390 px OK) | due 2026-12-07
2026-11-23 | /en/blog/how-to-invest-in-sp500/ | how to invest in s&p 500 (19 / 45.5); how to invest in s&p 500 index fund 9 / 70.7; buy s&p 500 7 / 66.3 | 151 | 60.6 | 0 % | title «How to invest in the S&P 500: 5 steps, the 3 main ETFs and what it costs», description with 5 steps + SPY/VOO/IVV, new lead that answers how (ETF via regulated broker, fractional shares); new cover. Live check OK | due 2026-12-07
2026-11-23 | /ja/blog/what-is-ethereum/ | イーサリアム (18 / 25.7); ethとは 9 / 20.0; イーサリアムとは 8 / 37.9 | 94 | 42.6 | 0 % | title «イーサリアム(ETH)とは?仕組みとビットコインとの違いをわかりやすく解説», description (2015, smart contracts, gas, staking), first sentence «イーサリアム(ETH)とは…»; new cover. Live check OK | due 2026-12-07
2026-11-23 | /th/blog/how-to-invest-in-sp500/ | วิธีซื้อกองทุน s&p 500 (13 / 16.8); s p500 etf 10 / 6.5; sp 500 etf 6 / 8.0 | 76 | 32.8 | 0 % | title «วิธีซื้อกองทุน S&P 500 สำหรับคนไทย: 2 ทางเลือก, ETF อย่าง SPY/VOO และค่าใช้จ่าย», description, new first paragraph answering the 2 ways (Thai fund in THB / foreign broker ETF); new cover. Live check OK | due 2026-12-07
2026-11-23 | /es/blog/what-is-a-dex/ | dex crypto (13 / 32.1); que es un dex crypto 12 / 32.2; dex cripto 10 / 32.3; dex criptomonedas 8 / 35.4 | 52 | 33.6 | 0 % | title «Qué es un DEX en cripto: cómo funciona un exchange descentralizado frente a un CEX», description (0,05–1 % per swap), first sentence «¿Qué es un DEX en cripto?»; new cover. Live check OK | due 2026-12-07
2026-11-23 | /ru/largest-companies/ + /tr/largest-companies/ (world page, all 20 languages) | крупнейшие компании мира по капитализации (87 / 8.8); dünyanın en büyük şirketleri 2026 (14 / 7.2) | 87 + 52 | 8.8 / 16.8 | 0 % | owner «так»: own meta description per language (scripts/i18n_lcw.py LCW: year + top 3 + number of companies) instead of the shared generic lead | due 2026-12-07

## Notes (not changed — template/code pages, for the owner)
- 2026-11-23: converter hubs /it/ /fr/ /es/ /ru/ /ja/converter/ have the most impressions (290 / 226 / 166 / 158 / 132, pos 9–16, 0 clicks) but only for junk queries («<bank> mobile apps», operator searches) — no real demand to target.
- 2026-11-23: /en/crypto-exchanges/ 89 impr / pos 25 («biggest / largest crypto exchanges») is noindex by the owner's choice (hidden since 2026-11-20).
- 2026-11-23: /ru/largest-companies/ 87 / 8.8 («крупнейшие компании мира по капитализации») and /tr/largest-companies/ 52 / 16.8 («dünyanın en büyük şirketleri 2026» 14 / 7.2) — title already matches; the meta description is the shared generic `lead` in scripts/i18n_lc.py, → done 2026-11-23 (owner «так», LCW).
- 2026-11-23: /en/largest-companies/uk/ 92 / 24.6 — ranking wrong (GBp market caps ÷100), already reported.
