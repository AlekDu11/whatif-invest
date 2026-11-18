---
title: How I built a 19,000-page markets site in 20 languages with one Python script
published: false
tags: python, webdev, opensource, showdev
canonical_url:
cover_image: https://whatifstack.com/assets/og.jpg
---

<!-- Owner: paste everything below the front matter into dev.to/new (or paste the whole file in "Markdown" mode). Tags: python, webdev, opensource, showdev. Leave canonical_url empty: this article exists only on DEV. -->

Most markets sites are built for traders: dense terminals, ads everywhere, English only. I wanted the opposite: a site where an ordinary person in Kyiv, Madrid or Jakarta can open Bitcoin, Nvidia or gold and understand what is going on, in their own language and currency.

The result is [WhatIfStack](https://whatifstack.com/en/): about 19,000 static pages in 20 languages, covering 600+ cryptocurrencies, 1,200+ stocks from 27 markets, 100 crypto exchanges and the portfolios of famous investors. The code is [open source](https://github.com/AlekDu11/whatif-invest). Here is how it works and what I learned.

## The architecture: boring on purpose

```
GitHub Actions (daily)  →  data/*.json  →  scripts/build.py  →  dist/ (static HTML)  →  CDN
```

- **Data jobs** run on GitHub Actions on a schedule. Each writes a JSON file to the repo: prices (Binance, Yahoo Finance, CoinGecko), crypto exchanges and their trading pairs, proof-of-reserves data from DefiLlama, and SEC 13F filings for investor portfolios.
- **One build script**, `scripts/build.py`, uses only the Python standard library. It reads the JSON and writes every page for every language. No framework, no template engine, just f-strings and small helper functions.
- **The output is plain HTML** plus one JS file and one CSS file, served from a CDN. A handful of serverless functions handle the things that cannot be static: news headlines, newsletter signups, feedback.

Why static? Speed and cost. A page is a file, so it loads fast on a cheap phone, and a traffic spike costs nothing extra.

## 20 languages without a CMS

All interface and SEO strings live in Python dictionaries, one per feature:

```python
BR = {
    'en': dict(h='Market in 60 seconds', upd='Updated', ...),
    'uk': dict(h='Ринок за 60 секунд', upd='Оновлено', ...),
    # ... 18 more
}
```

The rule that keeps this sane: **a new string is added for every language in the same commit**, or the build fails with a `KeyError`. Every page gets `hreflang` alternates, and prices are shown in the visitor's local currency.

## Live data on a static site

Static does not have to mean stale:

- **Crypto prices are live.** The page opens a WebSocket to Binance's public market-data stream, only for the symbols visible on the page, and updates the numbers in place.
- **The personal home page has no accounts.** If you star assets or add holdings, they are stored in `localStorage`, and the home page renders "Your markets" first: portfolio value, today's change, and our news about your assets (from a small per-language JSON feed). Everyone else gets the normal page.
- **"Market in 60 seconds"** is generated at build time from the same data: is the market up or down, the biggest move among large assets, and a link to our brief explaining it, if there is one.

## Things that bit me

1. **Build time.** One function that generated converter pairs ran inside a loop for every page and pushed the build past 8 minutes. Caching it brought the full build back to about 80 seconds.
2. **Page weight.** Each converter page shipped the full list of assets in a `<select>`, 219 KB per page. A "light" option list for those pages cut it to 46 KB.
3. **Currencies in someone else's data.** Market caps for some Asian and Indian stocks arrived in local currency and showed up as trillions of dollars. Every number now gets converted by the listing currency before it is ranked.
4. **SEC 13F filings are messy.** Some funds report values in dollars, some in thousands. A total-value threshold broke for small funds; checking the median implied price per share works much better.
5. **Deploy limits.** Pushing data commits all day hit the hosting provider's daily deployment limit. Now git auto-deploys are off, and a scheduled workflow triggers a deploy hook at most every few hours, only when the site changed.

## What's next

Price alerts, a weekly email report, and a simple health score for every stock. If you have ideas, or you can break it, I would love to hear about it in the comments.

Site: https://whatifstack.com/en/ · Code: https://github.com/AlekDu11/whatif-invest

*Not investment advice: the site shows history and data, not forecasts.*
