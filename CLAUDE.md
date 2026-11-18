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
2. Retention (Jan–Feb 2027): accounts, watchlist, price alerts (email/Telegram), portfolio tracker + backtest. Gate: 10k visitors/month.
3. Pro (Mar–Apr 2027): Pro ~$5/mo or $39/yr (ad-free, unlimited alerts, backtests, AI helper), exchange/broker ranking, dividends. Gate: 50k/month, 100 paying.
4. Scale (May 2027+): API + embeddable widgets, mobile app, native ads. Gate: 200k/month.

Content: 2–3 blog posts a week on trending queries (content/blog/<lang>/), weekly DCA market recap.

## Architecture (see README.md for details)
- data/market.json — daily via .github/workflows/update-prices.yml (scripts/fetch_data.py: Binance, Yahoo, CoinGecko, alternative.me)
- scripts/build.py — static site into dist/ (served at the domain root; old /whatif/* URLs redirect) (stdlib only; Vercel runs it on each push)
- scripts/i18n*.py — all UI/SEO strings for 20 languages; a new string must be added for every language
- src/app.js, src/style.css — front-end; src/ref.js — referral links
- Before pushing: run `python3 scripts/build.py` and check pages in a headless browser.
- Deploys (owner-approved 2026-11-17, Vercel storage limit): Vercel builds ONLY commits with `[deploy]` in the message (scripts/vercel_ignore.sh). .github/workflows/deploy.yml adds such a commit every 4 hours if the site changed. Put `[deploy]` in a commit message only for urgent fixes the owner is waiting for.

## Partner links
src/ref.js (buy buttons) and PARTNERS / POLY in scripts/build.py (/exchanges/ page, Polymarket block).

## Content quality (applies to every article, brief, guide, profile and post)
Follow content/STYLE.md: headline with a specific number, lead that answers the question, key-takeaways box, "what it means if you buy regularly", sources, local phrasing per language, `stat:`/`stat_label:` front matter.
Every blog/news post needs a branded cover: run `python3 scripts/cover.py --missing` (pip install pillow fonttools) before building and commit content/covers/. Covers are the share image (og:image) and the article hero.

## Content automation
Scheduled tasks: daily Insights article (6 or 20 languages, category analytics/guides), monthly market report on the 1st (category reports).
Movers rubric «What's happening with X» (tag `movers`): twice a day 10:47/19:47 Kyiv, scripts/movers.py lists candidates, briefs in en/uk/ru/es show on the asset page.
Regional articles: daily 14:23 Kyiv, 3 languages per day about their own market (front matter `region: yes`).
Social media language (owner, 2026-11-18): ALL social accounts and syndication in English only. Medium: daily 17:19 Kyiv, 1–2 English articles imported automatically (paste-event method in social/syndication.md).
X @WhatIfStack: 5 posts/day via the built-in browser (style + log in social/x-log.md). Weekly growth report Mondays 10:37 → reports/growth/.
Stock deep-dives: 02:13 and 13:13 Kyiv, 15 stocks per run in en+uk (queue: scripts/analysis_todo.py; format = content/profiles/*/twlo.md, front matter `kind: analysis` → full block on the stock page). Key stats: data/stockstats.json via .github/workflows/stock-stats.yml (daily, rotating).
Stock coverage: daily 22:47 Kyiv a task adds up to 100 stocks to data/markets.json (Nasdaq-100 → S&P 400 → S&P 600 → index members of the 27 supported markets), removes symbols Yahoo can't fetch; cap 4000 stocks until deploy size/build time are re-checked.
Asset profiles: daily 16:52 Kyiv, 3 assets/day → content/profiles/<lang>/<asset id>.md (About block on the asset page).
Guide: content/guide/<lang>.md → /guide/ (every tool explained; keep it updated when a feature is added).
Free distribution: social/syndication.md (platform rules, communities per language, log); daily drafts in social/syndication/YYYY-MM-DD.md. RSS per language (/<lang>/blog/rss.xml, with cover images → Pinterest/Flipboard auto-publish) and Google News sitemap /sitemap-news.xml are built by scripts/build.py.
Partnerships: /partners/ page (en, uk) with partners@whatifstack.com; partner program list partners/programs.md (refresh only when the owner asks).
Offers: offer_card() in build.py (Telegram Wallet bonus, strings in scripts/i18n_offer.py) on home + crypto asset pages; clicks via /go/tgwallet?from=<placement>.
Crypto exchange rankings: data/exchanges.json via .github/workflows/exchanges.yml (CoinGecko, daily 03:11 UTC) → /crypto-exchanges/ (spot, by trust rank), /crypto-exchanges/derivatives/ (open interest), /crypto-exchanges/<id>/ (en+uk: 30-day volume, top pairs, partner CTA via XC_PARTNER).
Ukraine pages (uk, ru; scripts/i18n_ua.py): /ovdp/brokers/ ranking + /ovdp/brokers/<id>/ (OB list: fee, currencies, issues, score — refresh facts when tariffs change), /buy-stocks-ukraine/ guide (Freedom24 CTA via /go/freedom24). Portfolio /me/#bonds: OVDP holdings (localStorage wi_bonds, CSV import name;broker;currency;amount;rate;bought;matures, uk/ru/en).
Converter pair pages /converter/<asset>-<ccy>/ (cv_pairs in build.py, strings scripts/i18n_cv.py, currencies per language CV_CCY; top 40 crypto in uk/en, 20 elsewhere + gold/silver; light option list to keep pages small).
Coin markets (CryptoRank-style «where it trades», all quote currencies): data/coin_markets.json via .github/workflows/coin-markets.yml (scripts/fetch_coin_markets.py, daily 05:41 UTC, 150 stalest coins per run) → coin_markets_block on crypto pages; fallback = exchange snapshot pairs. Exchange pages show 100 pairs with quote tabs. fetch_data.py adds coins traded on big exchanges but missing from the top-1000 list (exchange_extras).
User suggestions: «💡 Suggest an improvement» form inside the AI assistant panel (strings scripts/i18n_fb.py) → api/feedback.js → Upstash list fb:v1 (LRANGE fb:v1 0 50; counter fb:count; 10/day per IP). Read them in the weekly growth report.
News aggregator: api/news.js (Vercel function, RSS headlines only, links to originals).

## Backlog agreed with the owner (2026-11-17)
Taken from CompaniesMarketCap / StockAnalysis / Simply Wall St:
1. DONE 2026-11-17: /largest-companies/ rankings (market cap, revenue, earnings, employees, dividend, P/E) + 27 country pages, rank-change arrows, 20 languages (scripts/i18n_lc.py, lc_pages() in build.py); stock pages show "#N in the world" and 1-year change.
2. DONE 2026-11-18 (market cap for the top 1500 stocks in en+uk; revenue/earnings appear as stock_stats.py fills hy/hr/hn): per-stock metric pages /<id>/market-cap/, /<id>/revenue/, /<id>/earnings/ (en+uk first, light pages) with multi-year history: add annual income statement (4-5 years) and shares outstanding to scripts/stock_stats.py; market-cap history = monthly price x shares (labelled as an estimate); one-sentence answer ("As of <month> X is worth $..., #N in the world").
3. Then: a visual health score for each stock in our own style (valuation, growth, profit, debt, dividend), not a copy of Simply Wall St's snowflake; tags on stock pages (sector, index membership such as Dow Jones / S&P 500 / DAX).

## Waiting on the owner
Done 2026-11-18: e-mail forwarding via ImprovMX (free; MX mx1/mx2.improvmx.com + SPF TXT in Vercel DNS) — any address @whatifstack.com, incl. partners@ (business, on /partners/) and support@ (readers, in the footer of every page), goes to the owner's mailbox. Partner programs to apply for: partners/programs.md (owner signs up himself; Claude wires the links). Done 2026-11-17: Kraken referral (crypto buy buttons on English pages via REF_LANG — Binance does not serve US/UK; Kraken row in /exchanges/ table, Pro 0.40%/0.80%, recurring buy 1%). Freedom24 referral (stocks/ETF buy buttons on uk/de/fr/it/es/pt/pl/nl pages via REF_LANG in src/ref.js; EU only, not US/UK) and FG Wallet (USDT TRC-20 wallet, /exchanges/ wallets). Done 2026-11-16: Vercel Web Analytics enabled (Hobby, free); deployment retention set to 1 day for all types (each deploy is ~200 MB, Hobby limit 10 GB).
