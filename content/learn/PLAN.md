# «Learn» curriculum (owner 2026-11-22)

Plain step-by-step lessons for complete beginners: «what to press, in what order, what to watch out for». Every lesson is a blog post
`content/blog/<lang>/<slug>.md` with front matter `category: learn`, `track: <start|stocks|crypto|trading|memes>` (owner 2026-11-23: /learn/ shows 5 folders — start = «Investing basics», stocks, crypto, trading, memes; old `safety` lessons show in the crypto folder), `step: <n>` — in ALL 20 languages.
The hub /learn/ lists them by track and step; each lesson links to the next one. Mark a line `✅ <date>` when it is published in all 20 languages.

## start — First steps
1. ✅ 2026-11-22 What investing is, in plain words (what-is-investing, all 20 languages; saving vs investing, inflation eats cash; link {lang}/inflation/)
2. ✅ 2026-11-23 Buying a little every month (DCA) (dca-buying-a-little-every-month, all 20 languages): why it works for beginners ({{dca}} shortcodes, link {lang}/compare/)
3. ✅ 2026-11-23 (investment-risk-in-plain-words, all 20 languages) Risk in plain words: why prices fall, how much you can lose, «only money you can afford to lose»
4. ✅ 2026-11-23 (diversification-dont-put-everything-in-one-coin, all 20 languages) Diversification: don't put everything in one coin or one stock
5. ✅ 2026-11-23 (how-to-read-a-price-chart, all 20 languages) How to read a price chart in 2 minutes (our asset page as the example)

## crypto — Crypto: buy, store, sell
1. What Bitcoin is (short; link to {lang}/btc/ analysis)
2. How to register on a crypto exchange: email, password, 2FA, ID check (KYC) — generic steps, which exchanges work in your country ({lang}/exchanges/)
3. How to buy your first Bitcoin with a bank card (step by step, fees)
4. Stablecoins and USDT: what they are and what they are for
5. How to set up a recurring buy (auto-DCA) on an exchange
6. How to withdraw crypto to your own wallet (networks, addresses, test transfer)
7. How to sell crypto and get money to your bank account
8. Crypto fees explained: trading fee, spread, network fee

## safety — Safety
1. Seed phrase: what it is and the 5 rules to keep it safe
2. Two-factor authentication (2FA): how to turn it on, why SMS is weaker
3. The most common crypto scams (fake support, giveaways, «investment managers», fake apps)
4. Exchange vs your own wallet: who controls your coins
5. What to do if you were scammed (first hour checklist)

## stocks — Stocks and ETFs
1. What a stock is, in plain words
2. ETFs and index funds: the simplest way to own hundreds of companies
3. How to buy your first stock or ETF (brokers by country: link {lang}/stocks-<country>/ and our broker pages)
4. Dividends: how companies pay you
5. What the S&P 500 is and why everyone compares to it ({lang}/spy/)

## memes — Memecoins: lessons and stories
1. ✅ 2026-11-22 What memecoins are and why 95%+ of new ones die (what-are-memecoins, all 20 languages; CoinGecko/Dune/Solidus stats, cited)
2. ✅ 2026-11-22 How to buy memecoins on Solana (how-to-buy-memecoins-on-solana, all 20 languages)
3. ✅ How to trade memecoins on a DEX (exists: how-to-trade-memecoins — translate to all 20)
4. ✅ Memecoin scams and rug pulls (exists: memecoin-scams-rug-pull — translate to all 20)
5. ✅ 2026-11-23 (how-to-create-binance-wallet, all 20 languages) (owner 2026-11-22: «everything from Binance for now») How to create a Binance Wallet (Web3 wallet in the Binance app) step by step: install/open, create wallet, back up, fund it, find a token by contract, buy with the Meme Rush / swap screen, check Binance's security audit first; link /go/binance-web3 as the sign-up link
5b. ✅ 2026-11-23 (connect-binance-wallet-to-dex, all 20 languages; front matter step: 6 because step must be an integer — later memes lessons sort after it by date) How to connect Binance Wallet to a DEX site and move coins between Binance and the wallet (networks, test transfer)
6. ✅ 2026-11-23 (how-to-check-a-memecoin-before-buying, all 20 languages; step: 6, sorts after 5b by date) How to check a memecoin before buying: liquidity, holders, top-10 share, age, Binance security audit (and WhatIfStack's traffic light on /memes/)
7. ✅ 2026-11-23 (dogecoin-story, all 20 languages) Story: Dogecoin — the joke that became a top-10 coin
8. Story: Shiba Inu — from «Dogecoin killer» to one of the largest memecoins
9. Story: PEPE, BONK, WIF — the 2023–2024 memecoin wave
10. Story: pump.fun — the token factory and its survival numbers
11. Story: celebrity and political memecoins (what happened to holders)
12. Story: PEPE — the frog meme that became a multi-billion coin (separate deep story)
13. Story: BONK and WIF — how Solana memecoins took off in 2023–2024
14. Story: TRUMP and MELANIA — what happened to buyers of political memecoins
15. How Binance Alpha works and why a listing there moves memecoins (link {lang}/memes/ «Just listed» block)
16. Snipers, bundlers and dev wallets: how insiders profit at launch and how to spot them (link {lang}/memes/glossary/)
17. Why most memecoin buyers lose money: the maths of launches, slippage and fees (use the launch pulse on {lang}/memes/)

## memes — recurring (owner 2026-11-23)
- GLOSSARY: data/glossary/en.json is the memecoin glossary (/memes/glossary/). Every run, translate it into 2 languages that do not have data/glossary/<lang>.json yet (same ids and order; natural native phrasing; keep terms like «rug pull» in Latin script where locals use them, explain them). Done: uk ru es pt (2026-11-23). A language without its own file shows English with noindex, so each translation makes a new indexable page.
- GUIDE (owner 2026-11-24): content/guide/<lang>.md is the beginner's guide in all 20 languages (done). When a feature is added or removed, update en.md and the other 19 in the same run.
- MONTHLY (first run on or after the 2nd of each month): «Memecoin hall of fame and graveyard — <Month YYYY>»: the 5 memecoins that rose most and the 5 loudest collapses/rug pulls of the past month, dated facts with sources, «what beginners can learn», links to {lang}/memes/; category learn, track memes, in all 20 languages.


## Trading folder (owner 2026-11-23: new folder, track: trading — fill it after the current queue, plain language, risks first)
- step 1: What trading is and how it differs from investing (fees, time, why most day traders lose)
- step 2: Order types: market, limit, stop-loss — with a worked example
- step 3: How to read a price chart: candles, volume, timeframes
- step 4: Support, resistance and trends in plain words
- step 5: Leverage and futures: how liquidation works and why beginners lose money fast
- step 6: Risk management: position size, the 1% rule, a trading journal
