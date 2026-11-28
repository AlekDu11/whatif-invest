# Race videos ("$100 a month in A vs B vs C") — X + Telegram, every 2 days

Made with `python3 scripts/race_video.py <ids...> --amt 100 [--since YYYY-MM] --lang en --out content/video/<slug>.mp4`
(ids from data/market.json; 2–4 assets; default start = the youngest asset's first month). Inspired by animated "since launch"
comparisons that get thousands of views on crypto X. Keep the matchup a real question people argue about.

TEMPLATE v2 (owner 2026-11-25: «top — keep this template»): real logos in coloured rings (big in the header, at each line end and on the final ranking), crown + pulsing glow on the current leader, subtle $ / coin symbols drifting up in the background, labels stacked so they never overlap. Do not change the look without the owner. Check the extracted frame: every asset must show its real logo (not a 3-letter badge) — if one is missing, pick another matchup or note it.

## How to post (tested 2026-11-17)
- **X** blocks downloads from other sites (CSP), and the built-in browser opens popups in the same tab. Hand-off via URL
  fragment: navigate the tab to `https://whatifstack.com/x-relay.html?vid=/assets/video/<slug>.mp4&to=x&hash=1` (the video
  must be deployed: content/video/ -> /assets/video/). It redirects to `x.com/compose/post#wisf=<name>:<base64>`. Then in ONE
  javascript_tool call: decode `location.hash` into a File (video/mp4) right away, wait for `[role=dialog]
  input[data-testid=fileInput]` (only the dialog's input — the home page has its own), set `.files` via DataTransfer and
  dispatch `change` (the dialog input can take ~30 s to appear in a hidden pane — keep the File in window and retry); wait until `[role=dialog] [data-testid=attachments]` says "Ready". Type the text by clicking the
  dialog's "What's happening?" box and typing line by line (Enter for new lines), then click `[role=dialog]
  [data-testid=tweetButton]`. If the video is not deployed yet (Vercel skips commits without `[deploy]`), do the relay step yourself: on any whatifstack.com page fetch the raw.githubusercontent.com MP4, base64 it and set location.href to `https://x.com/compose/post#wisf=<slug>.mp4:<base64>`. Tested 2026-11-20 and 2026-11-21 (works: fetch on whatifstack.com/en/, then location.href to the hash URL, one JS call decodes+attaches): raw URL by commit SHA (raw.githubusercontent.com/.../<sha>/content/video/...) works right after push while /main/ still 404s for a few minutes (CDN cache); in Telegram the JS .click() on the modal send button did nothing — a real left_click on it sends. Tested again 2026-11-22: in a hidden pane the dialog's fileInput can need ~60 s — store the File in window.__wisFile in a short JS call (≤40 s, the tool times out at 45 s), then attach in a second call; the profile timeline may not render in a hidden pane — read the new status id from the UserOriginalsTimeline response (read_network_requests) and views from each /status/ page's analytics link. Tested 2026-11-23: on x.com/compose/post in a hidden pane the composer had no [role=dialog] wrapper — the dialog selector never matched; the page's only `input[data-testid=fileInput]` was the composer's and worked (Ready in ~5 s). Tested 2026-11-23 evening: same route worked; this time the composer DID have [role=dialog] (two tweetTextarea_0 on the page — use the one inside the dialog); X views of all posts at once: on x.com/WhatIfStack scroll and read a[href$=/analytics] aria-labels (works in a hidden pane). Telegram: after send the list may not show the new message until you reopen the channel from the chat list. Tested 2026-11-24 morning: same route; the page's only fileInput took the video (Ready), then a [role=dialog] composer appeared holding it — type into the dialog's textbox (find "Post text" gives 2 refs; use the one inside the dialog). Profile timeline stayed empty in the hidden pane; views via each /status/<id> page's a[href$=/analytics] innerText (works hidden); new status id from the UserOriginalsTimeline response. Tested 2026-11-26: same route (raw by SHA, fetch on whatifstack.com/en/, hash decode, page's only fileInput → Ready in seconds); the dialog appears after attach and earlier find refs go stale — re-run find, the dialog's "Post" is the first generic "Post" match. Tested 2026-11-27: same route; after the dialog appeared, clicking the dialog textbox by find ref left focus elsewhere (typed text went nowhere) — a coordinate left_click on the dialog's "What's happening?" line worked; verify with [role=dialog] [data-testid=tweetTextarea_0] after the first line. Post button: coordinate click from its getBoundingClientRect × (screenshot frame / innerWidth). Status pages showed views for older posts but "none" for a post ~7 h old. Telegram: the modal send button had class "disabled" but a real left_click on it sent. Tested 2026-11-28 evening: same route again (Post coordinate click; status id from the CreateTweet response body via read_network_requests). Telegram list showed old messages until the scroll-to-bottom arrow was clicked. Tested 2026-11-28: same route (raw by SHA, hash decode, page's only fileInput → Ready in seconds; Post by coordinate click); profile timeline still empty in the hidden pane, status pages give views. Fallback if the hash route fails: `python3 scripts/race_snippet.py ...` prints JS that renders
  and encodes the same video inside the page (WebCodecs) into window.__wisRaceFile.
- **Telegram Web** can fetch it directly: `fetch('https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/content/video/<slug>.mp4')`,
  File -> window.__wisNext + the patched HTMLInputElement.prototype.click from the Telegram task -> Attach -> "Photo or Video",
  caption with the KeyboardEvent/execCommand method (airy layout, bold headline + "In numbers"), click send.

## Queue (take the first unused line; mark it with the date when posted; add new ideas at the end)
- ✅ 2026-11-17 btc gold spy --since 2016-01 | Bitcoin vs gold vs S&P 500
- ✅ 2026-11-17 okb bnb cro | exchange tokens since launch
- ✅ 2026-11-18 btc eth sol | the big three L1s
- ✅ 2026-11-19 nvda amd intc | chip makers
- ✅ 2026-11-20 aapl msft googl | big tech classics
- ✅ 2026-11-21 spy qqq vt | ETF trio
- ✅ 2026-11-21 gold silver platinum | precious metals
- ✅ 2026-11-22 doge shib pepe | memecoins
- ✅ 2026-11-22 eth sol ada --since 2021-01 | "ETH killers" since the 2021 cycle
- ✅ 2026-11-23 tsla byd toyota | car makers
- ✅ 2026-11-23 link uni aave | DeFi blue chips
- ✅ 2026-11-24 btc nvda --since 2019-01 | Bitcoin vs Nvidia
- ✅ 2026-11-24 schd spy --since 2014-01 | dividends vs S&P 500
- ⏭ 2026-11-25 skipped (repeats okb bnb cro of 2026-11-17) bnb okb | exchange token duel
- ✅ 2026-11-25 xrp xlm hbar | payment coins
- ✅ 2026-11-25 meta nflx amzn | consumer tech
- ✅ 2026-11-26 btc spy wti (BTC data starts 2014-09, so since Sep 2014; WTI shows a text badge — no real logo for a commodity) | Bitcoin vs stocks vs oil
- ✅ 2026-11-26 jpm bac gs | US banks
- ✅ 2026-11-27 sol avax near | L1 challengers
- ✅ 2026-11-27 ko pep (since Jan 2000; --secs 14 to stay under 1.3 MB) | cola war
- ✅ 2026-11-28 btc eth --since 2017-08 | BTC vs ETH since ETH data start
- coffee cocoa sugar | breakfast commodities (2026-11-28: rendered, but all three show text badges — no real logos; skip until commodity logos exist)
- ✅ 2026-11-28 pltr crwd orcl (since Sep 2020; --secs 14) | software growth
- ltc bch etc | old-school forks
- wheat corn soybeans | grains
- ma v axp | card networks
- xom cvx shel | oil majors
- nvda tsm asml | AI chip supply chain
- wmt cost tgt | big-box retail
- sui apt sei | new L1s
- arb op pol | Ethereum L2s
- mcd sbux cmg | fast food
- voo gld --since 2005-01 | stocks vs gold ETF
- dot atom kas | interoperability vs proof-of-work
- lly pfe | pharma duel
- brk-b spy --since 2000-01 | Buffett vs the index
- copper silver gold | industrial vs precious metals

## Log
| date | ids | X URL | Telegram | views |
|---|---|---|---|---|
| 2026-11-17 | btc gold spy (since 2016-01) | https://x.com/WhatIfStack/status/2122690567314292871 | msg 1474 | X 18 · TG 101 (2026-11-27 18:45) |
| 2026-11-17 | okb bnb cro (since 2020-02) | https://x.com/WhatIfStack/status/2122729649189044275 | msg 1475 | X 19 · TG 152 (2026-11-27 18:45) |
| 2026-11-18 | btc eth sol (since 2020-04) | https://x.com/WhatIfStack/status/2123077127801298975 | msg 1479 | X 16 · TG 1.2K (2026-11-27 18:45) |
| 2026-11-19 | nvda amd intc (since 2000-01) | https://x.com/WhatIfStack/status/2123439207024910576 | msg 1483 | X 13 · TG 1.4K (2026-11-27 18:45) |
| 2026-11-20 18:35 | aapl msft googl (since 2004-08) | https://x.com/WhatIfStack/status/2123801362022707579 | msg 1488 | X 12 · TG 1.5K (2026-11-27 18:45) |
| 2026-11-21 11:30 | spy qqq vt (since 2008-06) | https://x.com/WhatIfStack/status/2124072647394750506 | — | X 25 (2026-11-27 18:45) |
| 2026-11-21 18:30 | gold silver platinum (since 2000-08) | https://x.com/WhatIfStack/status/2124163264862884319 | msg 1493 | X 12 · TG 1.4K (2026-11-27 18:45) |
| 2026-11-22 11:30 | doge shib pepe (since 2023-05) | https://x.com/WhatIfStack/status/2124435401335042107 | — | X 17 (2026-11-27 18:45) |
| 2026-11-22 17:35 | eth sol ada (since 2021-01) | https://x.com/WhatIfStack/status/2124525885826990369 | msg 1496 | X 14 · TG 981 (2026-11-27 18:45) |
| 2026-11-23 11:32 | tsla byd toyota (since 2010-06) | https://x.com/WhatIfStack/status/2124798172388020641 | — | X 16 (2026-11-27 18:45) |
| 2026-11-23 18:30 | link uni aave (since 2020-10) | https://x.com/WhatIfStack/status/2124888140607320551 | msg 1500 | X 18 · TG 685 (2026-11-27 18:45) |
| 2026-11-24 11:29 | btc nvda (since 2019-01) | https://x.com/WhatIfStack/status/2125159914225992139 | — | X 10 (2026-11-27 18:45) |
| 2026-11-24 18:30 | schd spy (since 2014-01) | https://x.com/WhatIfStack/status/2125250410118361290 | msg 1504 | X 21 · TG 418 (2026-11-27 18:45) |
| 2026-11-25 11:36 | xrp xlm hbar (since 2019-09) | https://x.com/WhatIfStack/status/2125522302678815122 | — | X 21 (2026-11-27 18:45) |
| 2026-11-25 18:33 | meta nflx amzn (since May 2012) | https://x.com/WhatIfStack/status/2125612912735920536 | msg 1508 | X 8 · TG 267 (2026-11-27 18:45) |
| 2026-11-26 11:30 | btc spy wti (since 2014-09) | https://x.com/WhatIfStack/status/2125884916575748434 | — | X 15 (2026-11-27 18:45) |
| 2026-11-26 18:33 | jpm bac gs (since 2000-01) | https://x.com/WhatIfStack/status/2125975547045896350 | msg 1511 | X 8 · TG 122 (2026-11-28 18:35) |
| 2026-11-27 11:29 | sol avax near (since 2020-10) | https://x.com/WhatIfStack/status/2126247126342500665 | — | X 6 (2026-11-28 18:35) |
| 2026-11-27 18:38 | ko pep (since 2000-01) | https://x.com/WhatIfStack/status/2126337965001707852 | msg 1514 | X 9 · TG 60 (2026-11-28 18:35) |
| 2026-11-28 11:31 | btc eth (since 2017-08) | https://x.com/WhatIfStack/status/2126609507136540678 | — | X 1 (2026-11-28 18:35) |
| 2026-11-28 18:30 | pltr crwd orcl (since 2020-09) | https://x.com/WhatIfStack/status/2126700303562977735 | msg 1517 | |
