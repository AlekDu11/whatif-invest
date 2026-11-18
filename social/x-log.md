# X (@WhatIfStack) — post log

One line per post, newest at the bottom. Filled by the scheduled task "WhatIfStack: X posts".
Columns: date-time (Kyiv) | format | topic | link? | post URL | views / likes / reposts / replies (updated on later runs)

**Read social/playbook.md first (daily/weekly series, templates, cadence).** On X put the site link in the first reply to our own post ("Full numbers: <url>"), never in the main post.

Style (studied from @CryptoRank_io, 10–16k views/post): emoji + Title Case headline, blank line, 2–4 short lines with exact numbers, one context line, "Past results, not a forecast." No link in the main post (X cuts reach); the site link lives in the profile. Charts/images get more reach when we can attach them.

**Every post gets an image (required since 2026-11-16).** X's CSP blocks loading files from other sites, so the card is drawn on the x.com page itself:
1. Open https://x.com/compose/post in the built-in browser.
2. In javascript_tool paste the whole of social/xcard.js, then on the last line call `await wisCard({title, stat, statLabel, label, series, date})`:
   - title = the post headline without emoji (≤ 70 chars); stat = the one big number (e.g. `−14%`, `10`, `$83.85M`); statLabel = 3–6 words for it; label = format name (Market, Mover, DCA, Activities, News).
   - series = 30–60 recent values of the main asset (from data/market.json `assets.<id>.p`, rounded), so the card shows its price line.
3. It must return `{ok:true}`; take a small screenshot to check the preview, then type the text and post as before.
4. Log `img` in the link column (e.g. `no+img`) so we can compare reach with and without images.
For a post about one of our articles, use the article's title and `stat` from its front matter.

**Cross-post to Bluesky (@whatifstack.bsky.social, logged in in the built-in browser).** After each X post, open https://bsky.app, press "New post", paste the same text (≤300 chars; shorten if needed, keep the numbers) and attach the same card: Bluesky opens a native file picker, so before clicking the image button run in javascript_tool a patch of `HTMLInputElement.prototype.click` (and `EventTarget.prototype.dispatchEvent` for `click` on file inputs) that sets `input.files` to the card blob (drawn with social/xcard.js's canvas code, or fetched from https://whatifstack.com/assets/covers/…) and fires `change`. Only our own posts — no likes, follows, replies or DMs. Log `+bsky` in the log row.

**Flipboard (last run of the day only):** open https://flipboard.com/@whatifstack/magazines/sid%2Fb316n978y%2Fwhatifstack/edit, and for each new English article published today (content/blog/en/, newest first, max 3) type its URL into the "Add a URL" field and press Enter. Skip URLs already in the magazine.

Formats to rotate and compare: dca-whatif, mover, market-pulse, chart-fact, country-stocks, article-link, poll, prediction-odds.

**prediction-odds (Polymarket, our partner — up to 1 post a day, English only):** a live market's odds from polymarket.com (e.g. "Bitcoin above $X by Dec 31?": Yes 34%), 2–3 lines of context with our numbers, then one honest line such as "Polymarket has confirmed a POLY token and airdrop; no date or rules yet." Never say users "will get" or "can get" an airdrop, never promise rewards, no betting encouragement, add "Not available in every country." Do not post this format in Ukrainian, Polish, Russian or other languages whose main countries block Polymarket (see PM_BLOCKED in api/go.js).

| when | format | topic | link | url | views | likes | reposts | replies |
|---|---|---|---|---|---|---|---|---|
| 2026-11-16 02:58 | dca-whatif | Gold vs S&P 500 vs Bitcoin, $10/day 5y | no | https://x.com/WhatIfStack/status/2122116675558355111 | 26 | 0 | 0 | 0 |
| 2026-11-16 09:18 | market-pulse | Fear & Greed 10, BTC/ETH weekly drop, gold | no | https://x.com/WhatIfStack/status/2122227869095223565 | 17 | 0 | 0 | 0 |
| 2026-11-16 12:16 | mover | Kava Lend exploit, KAVA −40% | no | https://x.com/WhatIfStack/status/2122272638718329107 | 20 | 0 | 0 | 0 |
| 2026-11-16 15:23 | chart-fact | BTC −16.5% in November so far vs best/worst Novembers | no+img | https://x.com/WhatIfStack/status/2122319572535763138 | 18 | 0 | 0 | 0 |
| 2026-11-16 18:19 | dca-whatif | Palantir vs Nvidia vs Ethereum, $10/day 5y (PLTR +729%) | no+img | https://x.com/WhatIfStack/status/2122363783330894225 | 10 | 0 | 0 | 0 |
| 2026-11-16 21:17 | mover | Internet Computer +15% in 24h as crypto slides (ICP $2.50, 99.6% below ATH, $10/day 3y $11,120 → $6,370) | no+img | https://x.com/WhatIfStack/status/2122408622227337401 | 7 | 0 | 0 | 0 |
| 2026-11-17 09:27 | dca-whatif | AMD vs Apple vs Tesla, $10/day 5y (AMD +290% → $71,873) | no+img | https://x.com/WhatIfStack/status/2122589805674635428 | 4 | 0 | 0 | 0 |
| 2026-11-17 12:17 | country-stocks | South Korea 5y DCA leaders (SK hynix +601%, Hanwha Aerospace +332%, vs S&P 500 +52%) | no+img | https://x.com/WhatIfStack/status/2122635304012005721 | 5 | 0 | 0 | 0 |
| 2026-11-17 15:21 | market-pulse | Dollar 19-month high, Fed hike bets >90%; BTC $64,250/ETH $1,813 −14% w/w, gold $3,870, S&P −1.9%, F&G 12 | no+img | https://x.com/WhatIfStack/status/2122681457277558810 | 10 | 0 | 0 | 0 |
| 2026-11-17 18:18 | chart-fact | ETH 3rd-worst November so far (−19.6%; worse 2018 −42.8%, 2025 −22.3%; $10/day 5y $18,260 → $15,091) | no+img | https://x.com/WhatIfStack/status/2122726051398754536 | 8 | 1 | 0 | 0 |
| 2026-11-17 21:17 | mover | Backpack BP +30.5% in 24h on CFTC approval of its US derivatives exchange + clearing ($1.09, mcap $273M, 34% below $1.65 peak) | no+img | https://x.com/WhatIfStack/status/2122771047841730783 | 10 | 1 | 0 | 0 |
| 2026-11-18 09:30 | dca-whatif | Big Tech $10/day 5y: Meta +95% ($35,552), Google +78%, Amazon +60%, Microsoft +43% | no+img | https://x.com/WhatIfStack/status/2122952235613126909 | 5 | 0 | 0 | 0 |
| 2026-11-18 12:20 | market-pulse | Gold −2.5% to lowest in over a year ($3,769); BTC $64,718 +0.6%, ETH $1,811, S&P −1.0%, F&G 11 | no | https://x.com/WhatIfStack/status/2122997462545596718 | 6 | 0 | 0 | 0 |
| 2026-11-18 15:21 | world-assets | All above-ground gold $27.2T > US M2 $23.4T; Apple $5.1T, Bitcoin $1.3T (gold at 1-year low $3,769) | no+img | https://x.com/WhatIfStack/status/2123043887803691467 | 4 | 0 | 0 | 0 |
| 2026-11-18 18:24 | chart-fact | Nvidia 2nd-worst November since 2000 (−24.0% so far, $204.64 → $155.46; only Nov 2000 −34.8% worse; +4% after hours on $115.8B quarter) | no+img | https://x.com/WhatIfStack/status/2123088135764709415 |  |  |  |  |

Week notes (2026-11-16): first week, 3 posts with stats (dca-whatif 15, mover 6, market-pulse 4 views) — dca-whatif leads but samples are tiny. Keep rotating formats to collect data; market-pulse tested today during the Extreme Fear sell-off.
Note (2026-11-16 12:16): posting with a $KAVA cashtag (X attached a price card) failed twice with "Your account may not be allowed to perform this action"; the same text without the cashtag went through after a reload. Avoid cashtags for now. Profile/search timelines don't render in the pane — read the post URL from the SearchTimeline network response.
Week notes update (2026-11-16 18:19): dca-whatif still leads (22 views) vs mover 15, market-pulse 13, chart-fact+img 12 — post more dca-whatif, try single-stock contrasts (PLTR/NVDA/ETH). Bluesky cross-post for this post was skipped: the browser permission check blocked the file-input patch (the Bluesky step is in this log, not in the task prompt) — owner may add it to the scheduled prompt.
Week notes update (2026-11-16 21:17): views now dca-whatif 23 (+4 for the fresh PLTR post), mover 17, market-pulse 15, chart-fact+img 14 — averages are within noise (~14–17); mover posted again (ICP bounce, 2nd-best format). Bluesky cross-post skipped again (not in the scheduled prompt; file-input patch was blocked last run).
Note (2026-11-17 12:17): avg views so far — market-pulse 16 (1 post), chart-fact 16 (1), mover 11 (2), dca-whatif 10 (3; AMD post at 0 after 3 h). First country-stocks test (experimental slot). Stocks returns on country pages are in local currency — say so in the post.
Note (2026-11-17 15:21): avg views (2 weeks) — market-pulse 16 (1), chart-fact 16 (1), mover 11 (2), dca-whatif 10 (3), country-stocks 0 (1). Reach is falling: the last 4 posts got 7, 4, 0, 0 views (the 0s after 3–6 h) — possible reach limit on the account (the earlier "may not be allowed" error). Posted market-pulse (top average) on the Fed-hike / strong-dollar news.
Note (2026-11-17 18:18): avg views (2 weeks) — chart-fact 16 (1), mover 12 (2), dca-whatif 11 (3), market-pulse 10 (2), country-stocks 2 (1). Reach still low (latest 5 posts 8/6/2/2/4). Posted chart-fact (top average). Metals series in data/market.json is flat Jan–Mar 2026 (gold 4745.1, silver 78.3 three months running) — looks like a data gap; avoid metals peak/drawdown claims until fixed.

Note (2026-11-17 21:17): avg views (2 weeks) — mover 12 (2), dca-whatif 12 (3), market-pulse 12 (2), chart-fact 9 (2), country-stocks 3 (1). Posted mover (top average, Backpack/CFTC). Profile timeline renders again in the pane, so stats can be read from article [role=group] aria-labels there in one pass. Two posts on the profile are not in this log (status/2122690567314292871, 2122729649189044275 — likely from another routine).

Note (2026-11-18 09:30): avg views (2 weeks) — market-pulse 13 (2), dca-whatif 13 (3), chart-fact 12 (2), mover 11 (3), country-stocks 5 (1). Reach still ~5–10 per post; first likes (ETH chart-fact, Backpack mover). Posted dca-whatif (Big Tech ranking, not in last 3 formats). Profile timeline did not render this run; stats read from each status page.

Note (2026-11-18 12:20): avg views (2 weeks) — market-pulse 13 (2), chart-fact 12 (2), mover 11 (3), dca-whatif 10 (4; Big Tech post 0 views after 3 h), country-stocks 5 (1). Other stats unchanged. Posted market-pulse (top average) on gold's drop to a 1-year low; text only (no card) to compare reach with the +img posts. Profile timeline still doesn't render — stats read per status page.

Note (2026-11-18 15:21): avg views (2 weeks) — chart-fact 12 (2), mover 11.3 (3), dca-whatif 10 (4), market-pulse 9.7 (3; text-only gold post 3 views after 3 h), country-stocks 5 (1). Profile timeline rendered again (stats read there in one pass). Experimental slot: first world-assets post. BUG for the owner: /world-assets/ (world_items in build.py) uses Yahoo mcap in local currency for non-US stocks — Reliance shows $18.5T (INR), KEPCO $16.1T (KRW), TCS $8.7T, Agricultural Bank of China $2.7T and Kweichow Moutai $1.8T (CNY) — they rank above Apple; needs FX conversion. Post used only gold/M2/Apple/Bitcoin, which are correct.

Note (2026-11-18 18:24): avg views (2 weeks) — chart-fact 13 (2), mover 12.3 (3), dca-whatif 11.3 (4), market-pulse 11 (3), country-stocks 5 (1), world-assets 4 (1). Profile timeline rendered (stats read in one pass). Posted chart-fact (top average): Nvidia's November drawdown from data/market.json monthly closes (Tuesday close, before the after-hours earnings bounce). One more post not in this log: status/2123077127801298975 (1 view, likely another routine).
