# WhatIfStack social playbook (modelled on CryptoRank, in our own style)

Studied 2026-11-16: CryptoRank's X (@CryptoRank_io, ~550k followers) and Telegram (@CryptoRankNews, ~680k).
Read this before every scheduled social run. Per-platform how-to (images, cross-posting) stays in x-log.md / syndication.md.

## What CryptoRank does (and why it works)
1. **One number per post.** Headline = a claim or question built around a figure ("Fear & Greed drops to 20", "Tokenized stocks cross $4B").
2. **A branded chart on every post.** Never a bare text post with data. Same template, same colours → recognisable in the feed.
3. **Short body:** 1–3 sentences of context, key figures in bold (Telegram), then one CTA line `👉 link`.
4. **On X the link goes in the first reply** ("Read our full analysis: …"), not in the main post — X cuts reach of posts with links.
5. **Fixed weekly rhythm** (people come back for series):
   - daily morning market overview (prices, Fear & Greed, top news, gainers) ~07:00–08:00;
   - weekly "most visited projects" digest (Sunday), weekly top gainers (Monday), weekly token unlocks;
   - 2–3 research/stat posts a day built on their own data pages.
6. **Engagement bait that is still data:** fill-in-the-blank posts ("BTC price at the 1st halving $12 … 5th halving: $___ ?").
7. **Every link goes to their own data page** (price page, category, calendar, report) — the social post is a teaser, the site is the answer.
8. **3–5 posts a day**, spread 2–3 h apart, 07:00–20:00 audience time.
9. **Telegram extras:** buttons under posts (Discuss → chat, Get API → site), a separate community chat, separate language channels (EN, RU).

## Our version (same mechanics, our identity)
**Voice:** plain language, honest numbers, DCA angle ("what if you had bought $10 a day"), never signals, never profit promises, always "Not investment advice / past results, not a forecast".
**Look:** dark green card (#0c1613), gold big number, green line chart, `whatifstack` logo — social/xcard.js (16:9, X/Bluesky/Telegram) and social/igcard.js (4:5, Instagram/Facebook/Threads).

### Daily series (Kyiv time)
| time | series | example headline | link to |
|---|---|---|---|
| 08:30 | ☀️ Market pulse | "Bitcoin −16% in November: Fear & Greed at 10" + BTC/ETH/S&P/gold lines | /fear-greed or home |
| 12:30 | 💵 $10 a day | "$10 a day in Palantir for 5 years: $18.4k in → $152k" | asset page |
| 16:30 | 📊 Chart fact | "Gold just had its worst week since …" / commodity of the day | asset/commodities page |
| 19:30 | 📰 Article / Mover | today's Insights article or "What's happening with X" | article |

### Weekly series
- **Monday:** 🏆 Top 5 DCA winners & losers of the week (all assets) → /lead
- **Wednesday:** 🌍 Country stocks of the week (rotate: US, Ukraine, Poland, Germany, India…) → /stocks-<country>/
- **Friday:** 🔐 Airdrop/scam safety or Activities update (Polymarket rules in x-log.md) → /activities/
- **Sunday:** 🔎 Most-viewed assets on WhatIfStack this week (Vercel Analytics) + weekly recap article
- **1st of month:** 📅 Monthly report card (best/worst assets of the month)
- Fill-in-the-blank once a week ("$10/day in BTC since 2015 = $___ ?" answer in reply next day).

### Post template
X / Bluesky / Threads (no link in main post on X):
```
<emoji> <Title Case claim with a number>

<1–2 short lines of context with exact figures>
<1 line: what it means if you buy regularly>

Past results, not a forecast.
```
+ card image; first reply: `Full numbers: https://whatifstack.com/en/<page>/`

Telegram (link in the post, bold key figures):
```
<emoji> **<Claim with a number>**

<2–3 sentences, **bold** numbers>
• bullet with figure
• bullet with figure

👉 whatifstack.com/en/<page>/
_Not investment advice._
```
Instagram / Facebook: same card (4:5), caption = Telegram text without markdown, 3–6 hashtags (#dca #investing #bitcoin #stocks #gold …), link in bio (IG) or in text (FB).

### Platform cadence
| platform | posts/day | notes |
|---|---|---|
| X | 4 | series above; link in reply; card on every post |
| Telegram (WhatIfStack channel) | 2–3 | morning pulse + best post of the day; bold + 👉 link; pin the intro post |
| Bluesky | = X | cross-post, link allowed in post |
| Threads / Instagram | 1 | best card of the day (4:5) |
| Facebook | 1 | article link post with preview |
| Pinterest / Flipboard | auto | RSS / last run of day |
| Medium / Teletype | 2–3 / week | republish EN (Medium) and RU (Teletype) articles with a canonical link to the site |

### Measure
Log every post (x-log.md, syndication.md). Each Monday growth report: views per series, best 3 posts, clicks from Vercel Analytics referrers — double the series that win, drop the ones that don't.
