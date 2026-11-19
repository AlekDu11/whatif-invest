# WhatIfStack (whatifstack.com) — project brief for Claude

Owner: AlekDu11. Claude acts as head of product + engineering, SEO, design, copywriting and data.
Full strategy doc: https://claude.ai/artifact/BWtJfaiRLWutsvaYkUqyoC

## Mission
The most useful and fastest markets site for ordinary people worldwide — a modern, better version of
CoinMarketCap, CoinGecko, CryptoRank and Investing.com — and a profitable business on top of it.
Positioning: "markets in plain language, with real numbers, for the whole world" — crypto, stocks and gold
in one place, fast, no ad clutter. Owner (2026-11-17): the essence is what people find interesting and useful
(price, chart, news, what's happening, tools) — not "$10 a day"/DCA; DCA is one useful tool among many, not the headline.

## Principles (check every decision against them)
1. Usefulness first — every page answers a real question ("what would I have…", "what to buy…", "what's the market doing").
2. Speed — <1 s load, no jank, works on every device (mobile first).
3. Simplicity — clear for a beginner on screen one; depth on screen two.
4. Honest data — real API prices, source + date visible, never promise profit, always "not investment advice".
5. Whole world — 20+ languages with local phrasing and local partners.
6. Search and trends — every feature is also an SEO page or a reason to share.
7. Money without hurting users — referrals, one honest Pro plan, native ads only; never become worse than competitors.

## Roadmap (next phase starts only when the previous gate is met)
1. Foundation (Nov–Dec 2026): domain whatifstack.com (done), Search Console (done 2026-11-15: domain property verified via Vercel DNS TXT, sitemap submitted), analytics, dark theme, PWA, local currencies, OG share images, referral links. Gate: site indexed.
2. Retention (Jan–Feb 2027): accounts, watchlist, price alerts (Telegram built 2026-11-18, waiting for the bot token; email later), portfolio tracker + backtest. Gate: 10k visitors/month.
3. Pro (Mar–Apr 2027): Pro ~$5/mo or $39/yr (ad-free, unlimited alerts, backtests, AI helper), exchange/broker ranking, dividends. Gate: 50k/month, 100 paying.
4. Scale (May 2027+): API + embeddable widgets, mobile app, native ads. Gate: 200k/month.

Content: 2–3 blog posts a week on trending queries (content/blog/<lang>/), weekly DCA market recap.

## Architecture (see README.md for details)
- data/market.json — daily via .github/workflows/update-prices.yml (scripts/fetch_data.py: Binance, Yahoo, CoinGecko, alternative.me)
- scripts/build.py — static site into dist/ (served at the domain root; old /whatif/* URLs redirect) (stdlib only; Vercel runs it on each push)
- scripts/i18n*.py — all UI/SEO strings for 20 languages; a new string must be added for every language
- src/app.js, src/style.css — front-end; src/ref.js — referral links
- Before pushing: run `python3 scripts/build.py` and check pages in a headless browser.
- Deploys (since 2026-11-18, after hitting the Hobby limit of 100 deployments/day): git auto-deploys are OFF (vercel.json git.deploymentEnabled=false), pushes cost nothing. .github/workflows/deploy.yml deploys at most once every 5 h 50 min (≈4 a day) when the site changed; it runs hourly by cron, on every push to main and after the data workflows (GitHub fires this repo's cron rarely), and POSTs the Vercel Deploy Hook (GitHub secret VERCEL_DEPLOY_HOOK, hook «scheduled» on main) and adds a «[deploy]» marker commit. Owner (2026-11-19): too many deploys fill the storage (one deploy >1 GB) — do NOT dispatch deploys for routine changes; wait for the slot. Only a real breakage on the live site: gh workflow run deploy.yml -f force=true (max 6 deploys/24 h).

## Partner links
src/ref.js (buy buttons) and PARTNERS / POLY in scripts/build.py (/exchanges/ page, Polymarket block). All /go/<id> targets: api/_partners.js. Also: TradingView ref on every live chart (tvref), pump.fun card on /memes/, monobank/Privat24 CTAs on OVDP broker pages (OB_GO), Inzhur REIT card on Ukrainian pages (INZ).

## Content quality (applies to every article, brief, guide, profile and post)
Follow content/STYLE.md: headline with a specific number, lead that answers the question, key-takeaways box, "what it means if you buy regularly", sources, local phrasing per language, `stat:`/`stat_label:` front matter.
Default share image per language: src/og/<lang>.jpg from scripts/og.py (re-run when positioning or asset count changes).
Every blog/news post needs a branded cover: run `python3 scripts/cover.py --missing` (pip install pillow fonttools) before building and commit content/covers/. Covers are the share image (og:image) and the article hero.

## Content automation
Scheduled tasks: daily Insights article (6 or 20 languages, category analytics/guides), monthly market report on the 1st (category reports).
Movers rubric «What's happening with X» (tag `movers`): twice a day 10:47/19:47 Kyiv, scripts/movers.py lists candidates, briefs in en/uk/ru/es show on the asset page.
Regional articles: daily 14:23 Kyiv, 3 languages per day about their own market (front matter `region: yes`).
Social media language (owner, 2026-11-18): ALL social accounts and syndication in English only. Medium: daily 17:19 Kyiv, 1–2 English articles imported automatically (paste-event method in social/syndication.md).
X @WhatIfStack: 5 posts/day via the built-in browser (style + log in social/x-log.md). Weekly growth report Mondays 10:37 → reports/growth/.
Stock deep-dives: 02:13 and 13:13 Kyiv, 15 stocks per run in en+uk (queue: scripts/analysis_todo.py; format = content/profiles/*/twlo.md, front matter `kind: analysis` → full block on the stock page). Key stats: data/stockstats.json via .github/workflows/stock-stats.yml (daily, rotating).
Stock coverage: daily 22:47 Kyiv a task adds up to 100 stocks to data/markets.json (Nasdaq-100 → S&P 400 → S&P 600 → index members of the 27 supported markets), removes symbols Yahoo can't fetch; cap 4000 stocks until deploy size/build time are re-checked.
Short «About» descriptions (data/desc/<lang>.json): every 4 h, 100 assets per run written straight in all 20 languages (scripts/desc_todo.py all N → scripts/desc_merge.py batch.json); English replaces the Yahoo/CoinGecko text.
Asset profiles: daily 16:52 Kyiv, 3 assets/day → content/profiles/<lang>/<asset id>.md (About block on the asset page).
Guide: content/guide/<lang>.md → /guide/ (every tool explained; keep it updated when a feature is added).
Free distribution: social/syndication.md (platform rules, communities per language, log); daily drafts in social/syndication/YYYY-MM-DD.md. RSS per language (/<lang>/blog/rss.xml, with cover images → Pinterest/Flipboard auto-publish) and Google News sitemap /sitemap-news.xml are built by scripts/build.py.
Partnerships: /partners/ page (en, uk) with partners@whatifstack.com; partner program list partners/programs.md (refresh only when the owner asks).
Offers: offer_card() in build.py (Telegram Wallet bonus, strings in scripts/i18n_offer.py) on home + crypto asset pages; clicks via /go/tgwallet?from=<placement>.
Crypto exchange rankings: data/exchanges.json via .github/workflows/exchanges.yml (CoinGecko, daily 03:11 UTC) → /crypto-exchanges/ (spot, by trust rank), /crypto-exchanges/derivatives/ (open interest), /crypto-exchanges/<id>/ (top 100, all 20 languages: 30-day volume, 100 pairs with quote tabs, facts + socials from CoinGecko /exchanges/{id}, proof-of-reserves block from DefiLlama api.llama.fi (category CEX: total, 7d/30d, by chain, top tokens, 1-year chart), partner CTA via XC_PARTNER).
Ukraine pages (uk, ru; scripts/i18n_ua.py): /ovdp/brokers/ ranking + /ovdp/brokers/<id>/ (OB list: fee, currencies, issues, score — refresh facts when tariffs change), /buy-stocks-ukraine/ guide (Freedom24 CTA via /go/freedom24). Portfolio /me/#bonds: OVDP holdings (localStorage wi_bonds, CSV import name;broker;currency;amount;rate;bought;matures, uk/ru/en).
Converter pair pages /converter/<asset>-<ccy>/ (cv_pairs in build.py, strings scripts/i18n_cv.py, currencies per language CV_CCY; top 40 crypto in uk/en, 20 elsewhere + gold/silver; light option list to keep pages small).
Coin markets (CryptoRank-style «where it trades», all quote currencies): data/coin_markets.json via .github/workflows/coin-markets.yml (scripts/fetch_coin_markets.py, daily 05:41 UTC, 150 stalest coins per run) → coin_markets_block on crypto pages; fallback = exchange snapshot pairs. Exchange pages show 100 pairs with quote tabs. fetch_data.py adds coins traded on big exchanges but missing from the top-1000 list (exchange_extras).
User suggestions: «💡 Suggest an improvement» form inside the AI assistant panel (strings scripts/i18n_fb.py) → api/feedback.js → Upstash list fb:v1 (LRANGE fb:v1 0 50; counter fb:count; 10/day per IP). Read them in the weekly growth report.
Price alerts in Telegram: «🔔» button on crypto / US stock / gold pages (alert_btn, strings scripts/i18n_al.py; shown only when TG_BOT in build.py is set) → t.me/<bot>?start=a_<aid>_<u|d>_<price, p = dot>_<lang> → api/tg.js webhook stores alerts in Upstash (al:items hash, al:chat:<id> sets, max 10 per chat; /list /del /stop) → api/alerts.js checker (CoinGecko simple price + Yahoo chart; map dist/assets/alerts-map.json) called every 10 min by .github/workflows/alerts.yml. Owner setup: bot in @BotFather, Vercel env TG_BOT_TOKEN + ALERTS_KEY, GitHub secret ALERTS_KEY, then open /api/tg?setup=<ALERTS_KEY>.
Weekly e-mail report signup: nl_block() on home + under every article/news (strings scripts/i18n_nl.py) → api/subscribe.js → Upstash hash nl:subs (email → {l, at, src, c}), counter nl:count. Sending waits for the owner's newsletter provider (Brevo/MailerLite) API key.
Daily health check task 07:43 Kyiv → reports/health.md, messages the owner only when something broke.
Famous investors: data/investors.json via .github/workflows/investors.yml (scripts/fetch_13f.py: SEC 13F-HR for 16 funds — Buffett, Ackman, Burry, Dalio, Wood…; CUSIP → ticker via OpenFIGI, cache data/cusip_map.json; weekly Tue) → /investors/ + /investors/<id>/ (20 languages, strings scripts/i18n_inv.py), in the Tools menu.
Home (2026-11-19, later): the «Market in 60 seconds» widget was REMOVED from home (owner) — replaced by the daily «Market wrap» article (scheduled 07:17 Kyiv → content/blog/<6 langs>/market-wrap-YYYY-MM-DD.md, category analytics, tag market-wrap). brief_block() is kept in build.py but not used. Live quotes for USD-listed stocks/ETFs/futures: api/quote.js (Yahoo 1-min bars incl. pre-/after-market, 30 s cache, page polls every 30 s) + index field y; crypto stays on the Binance stream. HOME IS APPROVED AS IS (owner, 2026-11-19 20:14): do not change the home first screen (hero, six-price top strip, DCA columns of the home table); only add things lower down. Other list pages use the CoinMarketCap-style market view (7d, market cap, volume, 7-day chart; strip with market totals). Order on home: hero (with the $10/day calculator) first, then «Your markets», then «Today in the markets» (owner, 2026-11-19). Same report posts daily 08:41 Kyiv in the Telegram channel. «Your markets» personal block my_block() (client-side from wi_watch/wi_hold, news from dist/assets/nf/<lang>.json; hidden for visitors without data) + «Market in 60 seconds» brief_block() under the hero (own data only); strings scripts/i18n_my.py (MY, BR).
Dropped assets (stale/delisted/renamed, e.g. ton → gram «prev. Toncoin»): build.py writes redirect stubs (meta refresh + canonical, noindex) to the renamed asset (RENAMED) or the category list, so known URLs never 404.
Calculators hub /calculators/ (scripts/i18n_ch.py); Tools menu keeps only the main tools. Asset lists paginate 50 per page: static numbered pages with real URLs via pager()/paged_path() (country stock pages /stocks-<c>/<n>/ sorted by market cap, /largest-companies/…/<n>/ top 300); JS tables use the same numbered pager (home: 20 per page).
News aggregator: api/news.js (Vercel function, RSS headlines only, links to originals).

## Backlog agreed with the owner (2026-11-17)
Taken from CompaniesMarketCap / StockAnalysis / Simply Wall St:
1. DONE 2026-11-17: /largest-companies/ rankings (market cap, revenue, earnings, employees, dividend, P/E) + 27 country pages, rank-change arrows, 20 languages (scripts/i18n_lc.py, lc_pages() in build.py); stock pages show "#N in the world" and 1-year change.
2. DONE 2026-11-18 (market cap for the top 1500 stocks in en+uk; revenue/earnings appear as stock_stats.py fills hy/hr/hn): per-stock metric pages /<id>/market-cap/, /<id>/revenue/, /<id>/earnings/ (en+uk first, light pages) with multi-year history: add annual income statement (4-5 years) and shares outstanding to scripts/stock_stats.py; market-cap history = monthly price x shares (labelled as an estimate); one-sentence answer ("As of <month> X is worth $..., #N in the world").
3. Then: a visual health score for each stock in our own style (valuation, growth, profit, debt, dividend), not a copy of Simply Wall St's snowflake; tags on stock pages (sector, index membership such as Dow Jones / S&P 500 / DAX).

## Ideas saved for later (owner, 2026-11-19: «do it when we find a sponsor»)
- Trading tournaments section on /activities/: live exchange/prop competitions (Binance, Bybit, OKX…), prize, dates, conditions, risk note, our referral links; 20 languages (like trading-tournaments.com, owner's friend's site).
- Free «Virtual portfolio league»: everyone gets virtual $10,000 in real assets, monthly leaderboard, share your rank; no real money; prizes from a sponsor/partner later. Needs nicknames + Upstash storage.

## Waiting on the owner
Done 2026-11-18: e-mail forwarding via ImprovMX (free; MX mx1/mx2.improvmx.com + SPF TXT in Vercel DNS) — any address @whatifstack.com, incl. partners@ (business, on /partners/) and support@ (readers, in the footer of every page), goes to the owner's mailbox. Partner programs to apply for: partners/programs.md (owner signs up himself; Claude wires the links). Done 2026-11-17: Kraken referral (crypto buy buttons on English pages via REF_LANG — Binance does not serve US/UK; Kraken row in /exchanges/ table, Pro 0.40%/0.80%, recurring buy 1%). Freedom24 referral (stocks/ETF buy buttons on uk/de/fr/it/es/pt/pl/nl pages via REF_LANG in src/ref.js; EU only, not US/UK) and FG Wallet (USDT TRC-20 wallet, /exchanges/ wallets). Done 2026-11-16: Vercel Web Analytics enabled (Hobby, free); deployment retention set to 1 day for all types (each deploy is ~200 MB, Hobby limit 10 GB).
