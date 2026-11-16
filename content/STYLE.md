# WhatIfStack editorial standard

Read this before writing any article, news brief, guide, profile or post. The goal: pieces people finish, trust and want to share.

## 1. The reader and the promise
- Reader: an ordinary person who invests small amounts regularly or is thinking about it. Smart, busy, not a trader.
- Every piece answers one clear question in the first two sentences ("Why is bitcoin falling?", "What would $10 a day in Toyota have made?").
- Our edge is real numbers: what regular buying actually returned, computed from our data. Use the shortcodes ({{dca}}, {{dcainv}}, {{dcaroi}}, {{price}}, {{table}}, {{card}}) or numbers from scripts/build.py simulate(), never estimates.

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
