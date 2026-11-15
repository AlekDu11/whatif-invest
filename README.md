# whatif.invest

"What if I invested $10 every day?" — a DCA calculator for crypto, stocks, ETFs, gold and silver.
Live at **https://mytimebox.app/whatif/** (Ukrainian) and **/whatif/en/** (English).

## How it works

```
data/assets.json        list of assets: id, names, category, Yahoo ticker
data/prices.json        monthly closing prices (generated)
src/app.js              the calculator (vanilla JS, no build step)
src/style.css           styles
src/ref.js              ← YOUR REFERRAL LINKS go here
scripts/update_prices.py  downloads prices from Yahoo Finance
scripts/build.py          generates static pages into whatif/
whatif/                   the generated site (what Vercel serves)
```

* Every asset gets its own page in each language, e.g. `/whatif/btc/` and `/whatif/en/btc/`,
  with a pre-rendered results table, FAQ, JSON-LD, canonical and hreflang tags.
* `whatif/sitemap.xml` lists every page.
* A GitHub Action runs every night: refreshes prices, rebuilds pages, commits. Vercel redeploys on each commit.

## Common changes

| I want to… | Do this |
|---|---|
| add referral links | edit `src/ref.js`, push |
| add an asset | add a line to `data/assets.json` (id, names, `cat`, `yahoo` ticker), push, then run the Action once |
| rebuild locally | `python3 scripts/build.py` then `python3 -m http.server` and open http://localhost:8000/whatif/ |

## Deploy (one time)

1. **Vercel → Add New → Project →** import this repo. Framework: *Other*, no build command, output directory: `.` (root).
   It deploys to `whatif-invest.vercel.app`.
2. **In the mytimebox.app project**, add these rewrites to its `vercel.json`
   (above any catch-all SPA rewrite):
   ```json
   { "source": "/whatif", "destination": "https://whatif-invest.vercel.app/whatif/" },
   { "source": "/whatif/:path*", "destination": "https://whatif-invest.vercel.app/whatif/:path*" }
   ```
3. Add `Sitemap: https://mytimebox.app/whatif/sitemap.xml` to mytimebox.app's `robots.txt`,
   and submit the sitemap in Google Search Console.
4. GitHub → Actions → "Update prices and rebuild" → **Run workflow** once to pull fresh prices for every asset.

Not investment advice. Calculations use monthly closes and ignore fees, taxes and dividends.
