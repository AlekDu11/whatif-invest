# Race videos ("$100 a month in A vs B vs C") — X + Telegram, every 2 days

Made with `python3 scripts/race_video.py <ids...> --amt 100 [--since YYYY-MM] --lang en --out content/video/<slug>.mp4`
(ids from data/market.json; 2–4 assets; default start = the youngest asset's first month). Inspired by animated "since launch"
comparisons that get thousands of views on crypto X. Keep the matchup a real question people argue about.

## How to post (tested 2026-11-17)
- **X** blocks downloads from other sites (CSP), and the built-in browser opens popups in the same tab. Hand-off via URL
  fragment: navigate the tab to `https://whatifstack.com/x-relay.html?vid=/assets/video/<slug>.mp4&to=x&hash=1` (the video
  must be deployed: content/video/ -> /assets/video/). It redirects to `x.com/compose/post#wisf=<name>:<base64>`. Then in ONE
  javascript_tool call: decode `location.hash` into a File (video/mp4) right away, wait for `[role=dialog]
  input[data-testid=fileInput]` (only the dialog's input — the home page has its own), set `.files` via DataTransfer and
  dispatch `change` (the dialog input can take ~30 s to appear in a hidden pane — keep the File in window and retry); wait until `[role=dialog] [data-testid=attachments]` says "Ready". Type the text by clicking the
  dialog's "What's happening?" box and typing line by line (Enter for new lines), then click `[role=dialog]
  [data-testid=tweetButton]`. If the video is not deployed yet (Vercel skips commits without `[deploy]`), do the relay step yourself: on any whatifstack.com page fetch the raw.githubusercontent.com MP4, base64 it and set location.href to `https://x.com/compose/post#wisf=<slug>.mp4:<base64>`. Fallback if the hash route fails: `python3 scripts/race_snippet.py ...` prints JS that renders
  and encodes the same video inside the page (WebCodecs) into window.__wisRaceFile.
- **Telegram Web** can fetch it directly: `fetch('https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/content/video/<slug>.mp4')`,
  File -> window.__wisNext + the patched HTMLInputElement.prototype.click from the Telegram task -> Attach -> "Photo or Video",
  caption with the KeyboardEvent/execCommand method (airy layout, bold headline + "In numbers"), click send.

## Queue (take the first unused line; mark it with the date when posted; add new ideas at the end)
- ✅ 2026-11-17 btc gold spy --since 2016-01 | Bitcoin vs gold vs S&P 500
- ✅ 2026-11-17 okb bnb cro | exchange tokens since launch
- ✅ 2026-11-18 btc eth sol | the big three L1s
- nvda amd intc | chip makers
- aapl msft googl | big tech classics
- spy qqq vt | ETF trio
- gold silver platinum | precious metals
- doge shib pepe | memecoins
- eth sol ada --since 2021-01 | "ETH killers" since the 2021 cycle
- tsla byd toyota | car makers
- link uni aave | DeFi blue chips
- btc nvda --since 2019-01 | Bitcoin vs Nvidia
- schd spy --since 2014-01 | dividends vs S&P 500
- bnb okb | exchange token duel
- xrp xlm hbar | payment coins
- meta nflx amzn | consumer tech
- btc spy wti --since 2010-01 | Bitcoin vs stocks vs oil
- jpm bac gs | US banks
- sol avax near | L1 challengers
- ko pep | cola war
- coffee cocoa sugar | breakfast commodities
- btc eth --since 2017-08 | BTC vs ETH since ETH data start
- pltr crwd orcl | software growth
- ltc bch etc | old-school forks
- wheat corn soybeans | grains

## Log
| date | ids | X URL | Telegram | views |
|---|---|---|---|---|
| 2026-11-17 | btc gold spy (since 2016-01) | https://x.com/WhatIfStack/status/2122690567314292871 | msg 1474 | X 10 · TG 39 (2026-11-18) |
| 2026-11-17 | okb bnb cro (since 2020-02) | https://x.com/WhatIfStack/status/2122729649189044275 | msg 1475 | X 11 · TG 83 (2026-11-18) |
| 2026-11-18 | btc eth sol (since 2020-04) | https://x.com/WhatIfStack/status/2123077127801298975 | msg 1479 | |
