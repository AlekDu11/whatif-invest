# Free distribution (syndication) playbook

Goal: free traffic and backlinks from platforms where our readers already are, without hurting SEO or getting banned.
Daily drafts land in `social/syndication/YYYY-MM-DD.md` (scheduled task "WhatIfStack: syndication"); log every published item in the table at the bottom.

## Golden rules
0. **English only (owner, 2026-11-18).** Every social account and every syndicated copy is in English.
1. **Canonical first.** Full copies only where the platform sets a canonical link to whatifstack.com (Medium "Import a story" does this). Everywhere else: a short, useful summary (3–6 numbers) + link to the full article.
2. **Value in the post itself.** The post must be worth reading without clicking. Numbers, a table, the honest downside.
3. **Reddit 90/10.** At most 1 in 10 of the account's posts/comments links to us; the rest are helpful comments. Read each subreddit's rules before posting; some ban links in posts — then post the text and add the link only if someone asks. Never post the same link in several subs on the same day.
4. **Native language.** Each regional article goes to that region's communities in its language.
5. **No advice, no hype.** Same as the site: real numbers, "past results, not a forecast", "not investment advice".
6. **Transparency.** The account is clearly WhatIfStack (or the owner saying "I run whatifstack.com"). Never pose as a random user praising the site.

## How to post to Instagram / Threads / Bluesky / Facebook (tested 2026-11-17, built-in browser, video)
- Hand-off: navigate to `https://whatifstack.com/x-relay.html?vid=/assets/video/<slug>.mp4&to=<ig|th|bs|fb>&hash=1`; first javascript_tool call decodes `location.hash` into `window.__wisFile` (File video/mp4), clears the hash, defines `window.__setF(input)` (DataTransfer → `.files` + `change`) and patches `HTMLInputElement.prototype.click` for file inputs. (The tool sometimes reports "page navigated" — just re-run it on the platform page.)
- Typing: `execCommand('insertText')` does NOT work in these editors. Focus the editor with JS (`ed.focus()`, caret to end via Range) and then use computer `type` + `key Enter` line by line. Never press Escape in a composer (FB asks "save as draft?" — close that prompt with its `[aria-label=Закрыть]`, not "Удалить черновик").
- Screenshots often time out (pane hidden) — work with javascript_tool / find refs.
- **Instagram** (UI in Ukrainian): click the `svg[aria-label="Новий допис"]`'s parent link → dialog; `__setF(dialog input[type=file])`; click "OK" on the Reels notice; crop button `svg[aria-label="Вибрати тип обтинання"]` → "Оригінал" (keeps 4:5); "Далі" ×2; click caption textbox ref "Додайте підпис…" and type; click "Поширити"; wait for "Відео Reels опубліковано". URL: open https://www.instagram.com/whatifstack/ and read the first `a[href*="/reel/"]`.
- **Threads**: click `[role=button][aria-label^="Порожнє текстове"]` → dialog; `__setF(dialog input[type=file])` (video preview appears); focus dialog `[contenteditable=true]` via JS (clicking the inline box behind the dialog closes it) and type; click the dialog's "Опублікувати" via a `find` ref (JS `.click()` didn't fire). URL from https://www.threads.com/@whatifstack (`a[href*="/post/"]`).
- **Bluesky**: click `[aria-label="Новий пост"]`; click `[aria-label="Add media to post"]` (or `__setF` on the single input[type=file]); wait until "Обробка відео..." disappears; focus editor via JS and type; click `[aria-label="Publish post"]`. URL: `fetch('https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=whatifstack.bsky.social&limit=5')`.
- Image cards (2026-11-18): paste wisSquare() from social/igcard.js into each platform page (window state is lost on every navigate — re-run it after navigating), pass `input:'#__none__'` so it only builds `window.__wisFile`, then attach as above. IG: the "Де поширити → Threads" switch is off by default — keep it off (Threads is posted separately).
- Threads typing fix: `computer type` right after a JS `ed.focus()` closed the dialog (twice). Instead `find "textbox"` → click the ref whose label starts "Порожнє текстове…" that lives inside the dialog (the inline one is a role=button), then type. Publish = the second "Опублікувати" ref (the dialog's).
- Bluesky images: JS `.click()` on "Add media to post" does nothing (RN Pressable) — click it via its `find` ref with the patched `HTMLInputElement.prototype.click`; setting `.files` on the input / paste events queued up and all landed at once (3 copies) — remove extras via "Видалити зображення" refs and check `[role=dialog] img[src^=data:]` count = 1 before publishing.
- Video not deployed yet (videos go live only with the next `[deploy]` build; the relay then hands over the 404 HTML page — check `__wisFile.size` > 100 KB): run `python3 scripts/race_snippet.py <ids> --amt 100 --since YYYY-MM` and paste its output into javascript_tool on each platform page (add `window.__wisFile = window.__wisRaceFile` + the __setF / click patch); ~5 MB 1080x1350 H.264, accepted by IG Reels, Threads and Bluesky (2026-11-18). Bluesky: the patched click on "Add media to post" did nothing this time — `__setF` on the last `input[type=file]` worked. FB: a Messenger "create PIN" dialog may also be open — pick the composer dialog by its `[contenteditable=true]`, ignore the PIN one.
- 2026-11-19: Bluesky — the patched "Add media to post" click created no input this time; ONE synthetic `paste` (ClipboardEvent with DataTransfer holding `__wisFile`) on the focused editor attached the image twice → removed one via a "Видалити зображення" ref. Clicking the "Як справи?" ref does not focus the editor: focus `[role=dialog] [contenteditable=true]` via JS (Range to end), then `computer type`. Publishing waits ~20 s on «Завантаження зображень…» while the pane is hidden. The composer tags posts as `langs: ["uk"]` (UI language) — switch the language picker (bottom bar, «українська») to English next time. Threads: the first dialog opened by JS `.click()` closed on the next screenshot — open it via the `find` ref click instead, then `__setF` on the dialog's input.
- 2026-11-19 20:47: Bluesky video — no file input appears (neither JS nor the patched "Add media" ref click); ONE synthetic `paste` on the focused editor attached the video exactly once. Language picker: click the «українська» ref → menuitem «Select англійська» → post gets langs ["en"]. To avoid pasting the 21 KB race snippet three times, the render code can be kept as one `eval`-able string; `logo` data is empty in race_snippet output (falls back to coloured circles with tickers).
- **Facebook** (UI in Russian, audience already "Доступно всем"): click the `[role=button]` "Фото/видео" on the home feed — the patched click attaches the video automatically; focus the dialog's `[contenteditable=true]` and type; click `[role=button]` "Опубликовать". A video becomes a Reel; it shows on the profile after ~30 s — read `a[href*="/reel/"]` there.

## Platforms (account status: owner creates the account once, as WhatIfStack)

| Platform | What we post | How | Account |
|---|---|---|---|
| Google News (Publisher Center) | the whole site | add publication https://publishercenter.google.com, sections = /en/news/ and /en/blog/ RSS; sitemap-news.xml is live | ✅ publication created (Google builds sections automatically) |
| Bing Webmaster | sitemap + IndexNow (already automatic) | — | ✅ |
| Pinterest (business) | every article cover as a pin, automatically | Settings → Bulk create Pins → Auto-publish from RSS: add https://whatifstack.com/en/blog/rss.xml (+ /es/, /de/, /pt/ … one board per language) | ✅ pinterest.com/whatifstack, site verified, 5 boards en/es/de/pt/uk auto-publish from RSS (2026-11-16) |
| Flipboard | magazine "WhatIfStack Insights" | RSS auto-import needs Flipboard publisher status (not granted yet) → new EN articles are added by URL in the magazine editor (X task, last run of the day) | ✅ flipboard.com/@whatifstack/whatifstack-insights-b316n978y |
| Medium | full article via Import (canonical set automatically), en + es/de/pt | medium.com/p/import → paste the URL → tags → publish. Max 1–2 a day. Fully automatic since 2026-11-18: typing into the import field does nothing, but a synthetic paste works — in the page run JS: focus #editor_7 (div.js-importUrl), select its contents, dispatch ClipboardEvent('paste') with a DataTransfer holding the URL → click Import → «See your story» → Publish → topics one by one with Enter (commas don't split, max 25 chars, 5 topics) → Publish. The article must already be live on whatifstack.com | ✅ medium.com/@whatifstack |
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
| 2026-11-16 | Telegram | WhatIfStack — DCA & markets (ex @TradeMaster_insight, 5.1k subs) | renamed, new description + logo, intro post with card (formatted) | https://t.me/WhatIfStack | username change and pin need the channel owner |
| 2026-11-18 | Telegram | @WhatIfStack | username changed by the owner: t.me/TradeMaster_insight → t.me/WhatIfStack; site footer link updated | https://t.me/WhatIfStack | — |
| 2026-11-16 | Teletype | @whatifstack | profile: name, RU bio, logo, link to /ru/ | https://teletype.in/@whatifstack | articles next |
| 2026-11-16 | Teletype | @whatifstack | weekly-dca-recap-2026-11-16 (ru) | https://teletype.in/@whatifstack/weekly-dca-recap-2026-11-16 | canonical link ✓, follow-us footer |
| 2026-11-17 | Teletype | @whatifstack | ethereum-10-dollars-a-day-5-years (ru) | https://teletype.in/@whatifstack/ethereum-10-dollars-a-day-5-years | canonical link ✓ |
| 2026-11-18 | Medium | @whatifstack | fed-rate-hike-december-2026 (en) | https://medium.com/@whatifstack/fed-rate-hike-odds-hit-100-what-hikes-did-to-bitcoin-stocks-and-gold-b4330d6cba2c | canonical ✓, imported by Claude without the owner (paste event) |
| 2026-11-18 | Medium | @whatifstack | anthropic-ipo-what-ai-ipos-did-next (en) | https://medium.com/@whatifstack/anthropics-1-4-trillion-ipo-6-of-2026-s-7-biggest-listings-trade-below-offer-ab4a99396c26 | canonical ✓ |
| 2026-11-18 | Medium | @whatifstack | ai-stocks-sell-off-four-pressures (en) | — not published | ⛔ ACCOUNT SUSPENDED: Medium showed "Your account was found in violation of the Medium Rules" on Publish (profile isSuspended=true). Medium automation paused until the owner resolves it |
| 2026-11-18 | Teletype | @whatifstack | ai-stocks-sell-off-four-pressures (en) | https://teletype.in/@whatifstack/ai-stocks-sell-off-four-pressures | canonical link ✓ |
| 2026-11-19 | Teletype | @whatifstack | gold-price-falls-14-month-low (en) | https://teletype.in/@whatifstack/gold-price-falls-14-month-low | canonical link ✓ |
