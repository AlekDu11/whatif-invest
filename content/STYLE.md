# WhatIfStack editorial standard

Read this before writing any article, news brief, guide, profile or post. The goal: pieces people finish, trust and want to share.

## 1. The reader and the promise
- Reader: an ordinary person who invests small amounts regularly or is thinking about it. Smart, busy, not a trader.
- Every piece answers one clear question in the first two sentences ("Why is bitcoin falling?", "What would $10 a day in Toyota have made?").
- Our edge is real numbers: what regular buying actually returned, computed from our data. Use the shortcodes ({{dca}}, {{dcainv}}, {{dcaroi}}, {{price}}, {{table}}, {{card}}) or numbers from scripts/build.py simulate(), never estimates.
- ALWAYS-CURRENT RULE (owner 2026-11-23: «bitcoin peaked at $125K; a year later it is $150K — the article must not still say $125K»): an analysis must stay true a year later without anyone touching it.
  - Title and description (plain text, cannot hold shortcodes): ONLY stable facts — what it is, supply cap, founding year, a FY result with its year («$478.8 billion revenue in fiscal 2026»). NEVER a record price, market value, price, rank, «% below its high» or «just crossed $X».
  - In the body, everything that changes goes through shortcodes: record high {{ath:<id>}} ({{athd:<id>}}), distance from the record {{fromath:<id>}}, market value {{mcap:<id>}}, rank {{rank:<id>}}, price {{price:<id>}}, 12-month change {{chg1y:<id>}}, «$10 a day» {{dca}}/{{dcaroi}}/{{dcainv}}. Never «the record is $126,080» or «worth about $1.2 trillion» as plain text.
  - Historical facts stay plain text but always with their date and in the past tense («it reached about $69,000 in November 2021», «revenue was $114.5 billion in the September 2026 quarter»). Never «the record so far is…», «currently», «just», «now» next to a plain number.
  - scripts/stale_check.py lists analyses to refresh (new record since written, older than 90 days, volatile number in the title); the analysis tasks fix those first.
- LIVE NUMBERS RULE (owner 2026-11-22): never write today's price, today's market value, a recent % change or a «$10 a day» result as plain text — they go stale. Use the live shortcodes, which the page updates in real time and links to the calculator: {{price:<id>}} (live price + 24h change), {{chg1y:<id>}} (live 12-month change), {{ath:<id>}} + {{athd:<id>}} (record high and its month, refreshed daily), {{dca:<id>:<years>}} / {{dcaroi:<id>:<years>}} / {{dcainv:<years>}} (live «$10 a day» result). Plain-text numbers are only for dated facts from reports and history («revenue $478.8 billion in fiscal 2026», «about $20,000 in late 2017»).
- WHALES WEB (owner 2026-11-28): every crypto news brief, article or analysis about a coin that trades on Hyperliquid (BTC, ETH, SOL, HYPE, XRP, DOGE, SUI, BNB, ZEC and most big coins) ties the story to what the big traders are doing: put the live box {{whales:<TICKER>}} (e.g. {{whales:BTC}}) on its own line right after the paragraph about the price move, and one plain sentence that links the tracker, e.g. «What are the biggest traders doing? Whales' long and short positions on BTC, live: [Hyperliquid whale tracker](/<lang>/trading/hyperliquid/)» (uk: /trading/hyperliquid/). Whale numbers themselves never go into the text as plain numbers (they change every minute) — only via the box, or as a dated fact («on 28 November a wallet opened a $60 million BTC short»). A box is also added automatically under every post whose first crypto asset trades on Hyperliquid, so one {{whales}} in the body is enough. News worth its own brief: a single position or liquidation over ~$50 million, or whales flipping from mostly long to mostly short on BTC/ETH (data: https://whatifstack.com/api/quote?hl=1 — fields coins, pos, near, ev).

## 2. Headlines (title)
- Specific fact or number + the reader's angle. 55–75 characters is ideal.
  Good: "Bitcoin fell 15% in a week: what it did to people who buy $10 a day"
  Good: "Gold beat Bitcoin and the S&P 500 over five years of monthly buys"
  Bad: "Bitcoin price analysis", "Everything you need to know about…", "Is it time to buy?"
- No clickbait the text does not deliver, no ALL CAPS, no "shocking", no emoji in titles.
- Description (meta): one sentence with the key number and why it matters to the reader, 140–160 characters.

## 3. Structure
1. **Lead (2–3 sentences):** the answer and the key number up front. No warm-up ("In the world of crypto…").
2. **Key takeaways box:** 3 bullets, each a fact with a number — this is what people screenshot and share.
3. **Body:** short sections with H2 headings that are statements, not labels ("Leverage made the drop worse", not "Analysis"). Paragraphs of 2–4 sentences. One idea per paragraph.
4. **What it means if you buy regularly:** always — our signature section. Concrete DCA numbers, both sides, no advice.
5. **Sources** (links) and the "Not investment advice" line in the article's language.
- Length: news 250–450 words; analysis 700–1200; guides 900–1500; profiles 220–400.

## 4. Voice
- Plain, confident, warm. Write like a smart friend who checked the numbers.
- Short sentences. Active voice. Concrete nouns. Explain any term the first time in a few words.
- No filler and no clichés: "delve", "landscape", "in today's fast-paced world", "it's worth noting", "game-changer", "to the moon", "navigate", "unlock".
- Never promise profit or tell people to buy or sell. Show history and risks honestly: "past results, not a forecast".
- Facts need a source; if no asset-specific reason for a move is found, say so.

## 5. Make it shareable
- One striking, checkable number in the lead and the title ("−49% from the top", "$18,410 became $29,455").
- One sentence per piece written to be quoted on its own (clear, numeric, surprising).
- Add front matter `stat:` (e.g. `+60%`, `−49%`) and `stat_label:` (e.g. `gold, $10 a day for 5 years`) — they go big on the cover image.
- Link 2–4 of our tools where they help the reader go further (asset page, compare, country page, world assets, calculators).

## 6. Local, not translated
- Write each language for its readers: local phrasing, local examples (local stocks via /stocks-<country>/, local currency for context, local exchanges where relevant). Never word-for-word translation.
- Keep numbers, dates and facts identical across languages.

## 7. Cover image (required)
- After writing, run `python3 scripts/cover.py --missing` (needs `pip install pillow fonttools`). It renders the branded 1200×630 cover for every post without one into content/covers/. Commit the covers with the post.
- Check one cover visually: title readable, `stat` correct.

## 8. Final check before commit
- Title delivers on the promise; lead answers the question; numbers come from data or sources; takeaways box present; "what it means if you buy regularly" present; sources listed; cover rendered; `python3 scripts/build.py` succeeds.
