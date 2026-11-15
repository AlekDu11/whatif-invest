# whatif.invest

"What if I invested $10 every day?" — a DCA calculator for crypto, stocks, ETFs, gold and silver.
Live at **https://whatifstack.com/** (Ukrainian at the root, other languages at /en/, /es/ …).

## How it works

```
data/assets.json         curated assets (Ukrainian names, Yahoo tickers)
data/market.json         all prices — written daily by the GitHub Action
scripts/fetch_data.py    Binance (top-200 crypto), Yahoo Finance (S&P 500, ETFs, metals), CoinGecko (names, logos)
scripts/build.py         generates dist/whatif/ — Vercel runs it on every deploy (stdlib only)
src/app.js, style.css    front-end: ranking table, search, calculator
src/ref.js               ← YOUR REFERRAL LINKS go here
```

Daily: Action fetches data → commits `data/market.json` → Vercel rebuilds all pages.
Locally: `python3 scripts/build.py && cd dist && python3 -m http.server` → http://localhost:8000/whatif/

## Deploy (one time)

1. **Vercel → Add New → Project →** import this repo. Settings come from `vercel.json` (build: `python3 scripts/build.py`, output: `dist`).
   It deploys to `whatif-invest.vercel.app`.
2. **In the mytimebox.app project**, add these rewrites to its `vercel.json`
   (above any catch-all SPA rewrite):
   ```json
   { "source": "/whatif", "destination": "https://whatif-invest.vercel.app/whatif/" },
   { "source": "/whatif/:path*", "destination": "https://whatif-invest.vercel.app/whatif/:path*" }
   ```
3. Add `Sitemap: https://mytimebox.app/whatif/sitemap.xml` to mytimebox.app's `robots.txt`,
   and submit the sitemap in Google Search Console.
4. GitHub → Actions → "Fetch market data" → **Run workflow** to refresh data any time.

Not investment advice. Calculations use monthly closes and ignore fees, taxes and dividends.

## Blog

Posts live in `content/blog/<lang>/<slug>.md` (uk and en; use the same slug in both languages so they link to each other).

```
---
title: $10 a day in Bitcoin for 5 years is now worth {{dca:btc:5}}
description: One-line summary for Google
date: 2026-11-15
assets: btc, spy, gold
---
Markdown text: ## headings, - lists, **bold**, [links]({lang}/btc/), > quotes.
```

Numbers stay current — shortcodes are recalculated on every build:
`{{dca:btc:5}}` value of $10/day over 5 years · `{{dcaroi:btc:5}}` its return · `{{dcainv:5}}` amount invested ·
`{{lump:btc:5}}` $1,000 invested 5 years ago · `{{lumproi:btc:5}}` · `{{price:btc}}` · `{{date}}`.
On their own line: `{{card:btc}}` asset card, `{{table:btc,eth,spy,gold:5}}` comparison table.


## Own news briefs
content/news/<lang>/<slug>.md → /news/<slug>/ (NewsArticle). Front matter: title, description, date `YYYY-MM-DD HH:MM` (UTC), tags (bitcoin, ethereum, etf, regulation, defi, stablecoins, solana, xrp, markets, hacks), assets. Body in our own words + `## Sources` list; the same shortcodes as the blog work. Same English slug in every language.
