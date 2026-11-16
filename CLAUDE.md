# WhatIfStack (whatifstack.com) — project brief for Claude

Owner: AlekDu11. Claude acts as head of product + engineering, SEO, design, copywriting and data.
Full strategy doc: https://claude.ai/artifact/BWtJfaiRLWutsvaYkUqyoC

## Mission
The most useful and fastest markets site for ordinary people worldwide — a modern, better version of
CoinMarketCap, CoinGecko, CryptoRank and Investing.com — and a profitable business on top of it.
Positioning: "markets in plain language, with real numbers, for the whole world" — crypto, stocks and gold
in one place, fast, no ad clutter, focused on regular (DCA) investing.

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

## Partner links
src/ref.js (buy buttons) and PARTNERS / POLY in scripts/build.py (/exchanges/ page, Polymarket block).

## Content quality (applies to every article, brief, guide, profile and post)
Follow content/STYLE.md: headline with a specific number, lead that answers the question, key-takeaways box, "what it means if you buy regularly", sources, local phrasing per language, `stat:`/`stat_label:` front matter.
Every blog/news post needs a branded cover: run `python3 scripts/cover.py --missing` (pip install pillow fonttools) before building and commit content/covers/. Covers are the share image (og:image) and the article hero.

## Content automation
Scheduled tasks: daily Insights article (6 or 20 languages, category analytics/guides), monthly market report on the 1st (category reports).
Movers rubric «What's happening with X» (tag `movers`): twice a day 10:47/19:47 Kyiv, scripts/movers.py lists candidates, briefs in en/uk/ru/es show on the asset page.
Regional articles: daily 14:23 Kyiv, 3 languages per day about their own market (front matter `region: yes`).
X @WhatIfStack: 5 posts/day via the built-in browser (style + log in social/x-log.md). Weekly growth report Mondays 10:37 → reports/growth/.
Asset profiles: daily 16:52 Kyiv, 3 assets/day → content/profiles/<lang>/<asset id>.md (About block on the asset page).
Guide: content/guide/<lang>.md → /guide/ (every tool explained; keep it updated when a feature is added).
News aggregator: api/news.js (Vercel function, RSS headlines only, links to originals).

## Waiting on the owner
A stock broker referral link (Freedom24). Done 2026-11-16: Vercel Web Analytics enabled (Hobby, free); deployment retention set to 1 day for all types (each deploy is ~200 MB, Hobby limit 10 GB).
