# Free distribution (syndication) playbook

Goal: free traffic and backlinks from platforms where our readers already are, without hurting SEO or getting banned.
Daily drafts land in `social/syndication/YYYY-MM-DD.md` (scheduled task "WhatIfStack: syndication"); log every published item in the table at the bottom.

## Golden rules
1. **Canonical first.** Full copies only where the platform sets a canonical link to whatifstack.com (Medium "Import a story" does this). Everywhere else: a short, useful summary (3–6 numbers) + link to the full article.
2. **Value in the post itself.** The post must be worth reading without clicking. Numbers, a table, the honest downside.
3. **Reddit 90/10.** At most 1 in 10 of the account's posts/comments links to us; the rest are helpful comments. Read each subreddit's rules before posting; some ban links in posts — then post the text and add the link only if someone asks. Never post the same link in several subs on the same day.
4. **Native language.** Each regional article goes to that region's communities in its language.
5. **No advice, no hype.** Same as the site: real numbers, "past results, not a forecast", "not investment advice".
6. **Transparency.** The account is clearly WhatIfStack (or the owner saying "I run whatifstack.com"). Never pose as a random user praising the site.

## Platforms (account status: owner creates the account once, as WhatIfStack)

| Platform | What we post | How | Account |
|---|---|---|---|
| Google News (Publisher Center) | the whole site | add publication https://publishercenter.google.com, sections = /en/news/ and /en/blog/ RSS; sitemap-news.xml is live | ✅ publication created (Google builds sections automatically) |
| Bing Webmaster | sitemap + IndexNow (already automatic) | — | ✅ |
| Pinterest (business) | every article cover as a pin, automatically | Settings → Bulk create Pins → Auto-publish from RSS: add https://whatifstack.com/en/blog/rss.xml (+ /es/, /de/, /pt/ … one board per language) | ✅ pinterest.com/whatifstack, site verified, 5 boards en/es/de/pt/uk auto-publish from RSS (2026-11-16) |
| Flipboard | magazine "WhatIfStack Insights" | RSS auto-import needs Flipboard publisher status (not granted yet) → new EN articles are added by URL in the magazine editor (X task, last run of the day) | ✅ flipboard.com/@whatifstack/whatifstack-insights-b316n978y |
| Medium | full article via Import (canonical set automatically), en + es/de/pt | medium.com/p/import → paste the URL → tags → publish. Max 1–2 a day. NB: the import URL field ignores Claude's typing — the owner pastes the URL and presses Import, Claude does tags + publish | ✅ medium.com/@whatifstack |
| LinkedIn (personal + page) | 1 analytic post a day: 3–5 numbers + link in the first comment | — | ⏸ skipped by owner (2026-11-16) |
| Reddit | regional articles in local subs, data posts | drafts in social/syndication/; owner posts manually (reddit.com is blocked in Claude's built-in browser) | ☐ owner |
| Quora | answers to "what if I invested $X in Y" questions with our numbers + link | — | ☐ owner |
| Threads / Bluesky | same posts as X | Bluesky: X task cross-posts each post (see social/x-log.md) · Threads: needs Instagram first | Bluesky ✅ @whatifstack.bsky.social · Threads ✅ @whatifstack · Instagram ✅ @whatifstack |
| Telegram channel @whatifstack | daily: 1 article + 1 number | — | ☐ owner |
| TradingView Ideas / Binance Square / CMC Community | crypto articles as short ideas (links limited → brand mention) | — | ☐ owner |

## Where each language goes (communities)
Candidates — before the first post in a community, open it, check it is active and read its self-promotion rules; drop it from this list if links are banned.
- **de:** r/Finanzen, r/mauerstrassenwetten (only data posts, no ads), r/Aktien; LinkedIn DE
- **es:** r/SpainFIRE, r/eupersonalfinance, r/BolsaEspanola, r/Mexico_Finanzas (for mx); Rankia foro (comentarios, sin spam)
- **pt:** r/investimentos, r/farialimabets (humor, careful); TabNews (pt-BR, articles allowed with source)
- **en:** r/dividends, r/Bogleheads (no self-promo links — comments only), r/CryptoCurrency (data posts, follow their source rules), r/eupersonalfinance, r/UKPersonalFinance (no links)
- **uk:** r/Ukraine_UA, Telegram finance chats (only with admin permission)
- **ru:** vc.ru (полный пост с ссылкой на источник), Дзен (статьи), Smart-Lab (блог)
- **pl:** r/inwestowanie, Wykop (Finanse), Bankier forum
- **tr:** r/Borsa, r/Turkey (no ads), Ekşi Sözlük (entries, no links)
- **fr:** r/vosfinances (strict rules), r/FrugalFR
- **it:** r/ItaliaPersonalFinance
- **nl:** r/DutchFIRE, r/beleggen
- **ja / ko / zh / hi / id / vi / th / ar / fil:** start with Pinterest + Medium; local platforms later (note.com, Naver Blog, Zhihu, Kaskus, Pantip …)

## Log
| Date | Platform | Community | Article | URL | Result (views/upvotes/clicks) |
|---|---|---|---|---|---|
| 2026-11-16 | Medium | @whatifstack | bitcoin-crash-65000-dca (en) | https://medium.com/@whatifstack/why-is-bitcoin-crashing-btc-below-65-000-49-off-its-high-what-dca-buyers-have-now-92e2ed802495 | canonical ✓ |
| 2026-11-16 | Medium | @whatifstack | dax-schwergewichte-10-dollar-am-tag-5-jahre (de) | https://medium.com/@whatifstack/10-am-tag-in-5-dax-schwergewichte-65-in-5-jahren-mehr-als-s-p-500-und-bitcoin-29a0ac901b1a | canonical ✓ |
| 2026-11-16 | Medium | @whatifstack | ibex-35-gigantes-10-dolares-al-dia-5-anos (es) | https://medium.com/@whatifstack/10-al-d%C3%ADa-en-5-gigantes-del-ibex-35-169-en-5-a%C3%B1os-frente-al-52-del-s-p-500-21ec089ac88a | canonical ✓ |
| 2026-11-16 | Bluesky | @whatifstack.bsky.social | intro: $10/day BTC 5y +49% | https://bsky.app/profile/whatifstack.bsky.social | first post |
| 2026-11-16 | Instagram | @whatifstack | intro card 4:5 (social/igcard.js) + caption | https://www.instagram.com/whatifstack/ | bio + avatar set; website field is app-only |
| 2026-11-16 | Threads | @whatifstack | intro + card | https://www.threads.com/@whatifstack | bio, link, avatar set |
| 2026-11-16 | Facebook | Arti Trader (personal profile) | intro + /en/, weekly recap, airdrop safety rules (3 link posts) | https://www.facebook.com/arti.trader.39 | bio + website link set; 2021 photo posts set to Only me; Page creation failed (server error, new account) |

Next: Teletype (teletype.in, login via Telegram) and Dzen (dzen.ru, Yandex/VK ID) — ru articles with canonical links; owner logs in.
| 2026-11-16 | Telegram | WhatIfStack — DCA & markets (ex @TradeMaster_insight, 5.1k subs) | renamed, new description + logo, intro post with card (formatted) | https://t.me/TradeMaster_insight | username change and pin need the channel owner |
| 2026-11-16 | Teletype | @whatifstack | profile: name, RU bio, logo, link to /ru/ | https://teletype.in/@whatifstack | articles next |
| 2026-11-16 | Teletype | @whatifstack | weekly-dca-recap-2026-11-16 (ru) | https://teletype.in/@whatifstack/weekly-dca-recap-2026-11-16 | canonical link ✓, follow-us footer |
| 2026-11-17 | Teletype | @whatifstack | ethereum-10-dollars-a-day-5-years (ru) | https://teletype.in/@whatifstack/ethereum-10-dollars-a-day-5-years | canonical link ✓ |
