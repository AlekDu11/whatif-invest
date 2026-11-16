# X (@WhatIfStack) — post log

One line per post, newest at the bottom. Filled by the scheduled task "WhatIfStack: X posts".
Columns: date-time (Kyiv) | format | topic | link? | post URL | views / likes / reposts / replies (updated on later runs)

Style (studied from @CryptoRank_io, 10–16k views/post): emoji + Title Case headline, blank line, 2–4 short lines with exact numbers, one context line, "Past results, not a forecast." No link in the main post (X cuts reach); the site link lives in the profile. Charts/images get more reach when we can attach them.

**Every post gets an image (required since 2026-11-16).** X's CSP blocks loading files from other sites, so the card is drawn on the x.com page itself:
1. Open https://x.com/compose/post in the built-in browser.
2. In javascript_tool paste the whole of social/xcard.js, then on the last line call `await wisCard({title, stat, statLabel, label, series, date})`:
   - title = the post headline without emoji (≤ 70 chars); stat = the one big number (e.g. `−14%`, `10`, `$83.85M`); statLabel = 3–6 words for it; label = format name (Market, Mover, DCA, Activities, News).
   - series = 30–60 recent values of the main asset (from data/market.json `assets.<id>.p`, rounded), so the card shows its price line.
3. It must return `{ok:true}`; take a small screenshot to check the preview, then type the text and post as before.
4. Log `img` in the link column (e.g. `no+img`) so we can compare reach with and without images.
For a post about one of our articles, use the article's title and `stat` from its front matter.

Formats to rotate and compare: dca-whatif, mover, market-pulse, chart-fact, country-stocks, article-link, poll.

| when | format | topic | link | url | views | likes | reposts | replies |
|---|---|---|---|---|---|---|---|---|
| 2026-11-16 02:58 | dca-whatif | Gold vs S&P 500 vs Bitcoin, $10/day 5y | no | https://x.com/WhatIfStack/status/2122116675558355111 | 11 | 0 | 0 | 0 |
| 2026-11-16 09:18 | market-pulse | Fear & Greed 10, BTC/ETH weekly drop, gold | no | https://x.com/WhatIfStack/status/2122227869095223565 | 0 | 0 | 0 | 0 |
| 2026-11-16 12:16 | mover | Kava Lend exploit, KAVA −40% | no | https://x.com/WhatIfStack/status/2122272638718329107 |  |  |  |  |

Week notes (2026-11-16): first week, only 1 post with stats (dca-whatif, 11 views) — no winner yet. Keep rotating formats to collect data; market-pulse tested today during the Extreme Fear sell-off.
Note (2026-11-16 12:16): posting with a $KAVA cashtag (X attached a price card) failed twice with "Your account may not be allowed to perform this action"; the same text without the cashtag went through after a reload. Avoid cashtags for now. Profile/search timelines don't render in the pane — read the post URL from the SearchTimeline network response.
