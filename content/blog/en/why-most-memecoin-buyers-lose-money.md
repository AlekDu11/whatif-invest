---
title: "Why most memecoin buyers lose money: the maths of launches, slippage and fees"
description: Only 0.41% of pump.fun wallets realized over $10,000 profit. The simple maths of launches, slippage and fees that works against memecoin buyers.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0.41%
stat_label: of 13.55 million pump.fun wallets had realized over $10,000 profit (Dune data, January 2025)
---
**Why do most people who buy memecoins lose money?** Because the maths is against them before the price even moves: most new tokens die within a day, every buy and sell costs fees and slippage, and the earliest buyers (often bots and insiders) sell to the people who come later. To win, a token has to survive *and* rise far enough to cover all of that.

> **Key takeaways**
> - Dune data shared in January 2025 showed that only about **0.41%** of 13.55 million pump.fun wallets had realized more than **$10,000** profit.
> - CoinGecko found that **68.67%** of pump.fun tokens made their last trade on launch day (data January 2024 – June 2026).
> - Each round trip (buy + sell) on a new token can cost **2.5%+** in platform fees alone, plus network fees and slippage.

## Part 1 — The survival maths

Most memecoins are not "cheap" — they are short-lived.

- **Launch-day death.** CoinGecko counted 18.67 million pump.fun tokens; 68.67% had their last trade on the day they launched (reported June 25, 2026).
- **Few reach a real market.** "Graduation" means a token leaves pump.fun's starting curve and gets a normal trading pool. Dune data showed the weekly graduation rate stayed below **1%** for four weeks from February 17, 2025; its best week, in November 2024, was **1.67%**. In March 2026 it reached **2.01%**, the highest since July 2025.

So if you pick new launches at random, you will mostly hold coins that stop trading. A few big winners cannot pay for many coins that go to zero unless you pick very well — and on day one nobody knows which ones will survive.

## Part 2 — Fees: you pay on the way in and on the way out

pump.fun's help page (September 2025) lists a **1.25%** fee on every trade before graduation (0.95% to the platform, 0.30% to the creator). After graduation the fee falls as the token grows, from 1.25% for the smallest down to 0.30% for the largest. On top of that come Solana network fees and optional "priority" and MEV-protection fees (0.003–0.03 SOL per trade on their page).

**Worked example (illustration, not real prices):** you buy $50 of a new token and pay a 0.02 SOL priority fee each way. The 1.25% fee in and out is about $1.25, and two priority fees can be several dollars more. Just to get back to $50, the token must rise maybe **5–10%**. With $10 trades it is far worse: fixed fees eat a much bigger share.

## Part 3 — Slippage: the price moves while you buy

**Slippage** is the difference between the price you see and the price you get (see the [memecoin glossary]({lang}/memes/glossary/)). New tokens have tiny pools, so your own buy pushes the price up — and everyone else's buys in the same second too. If you set slippage to 10–20% (many apps suggest it for new coins), you agree to pay up to that much more. Selling has the same problem in reverse: in a thin pool, your sell pushes the price down.

## Part 4 — Who is on the other side

The earliest buyers are often snipers, bundlers and the dev wallet (see [snipers, bundlers and dev wallets]({lang}/blog/snipers-bundlers-dev-wallets/)). They buy at the lowest price and sell into the first wave of demand. If you buy after the first green candle, you are often the "exit liquidity" — the money they sell to.

## Step-by-step: check the maths before you press «Buy»

1. **Step 1 — Count the fees.** Look at the fee line in your swap screen and add the network/priority fee. Multiply by two (buy + sell).
2. **Step 2 — Check slippage.** Keep it as low as the trade allows (for example 1–3% on a coin with a big pool). If a coin needs 20% slippage, that is a warning.
3. **Step 3 — Check the pool size.** On our [memes page]({lang}/memes/) open the token and look at liquidity. Small pool = big slippage both ways.
4. **Step 4 — Run the safety check.** Use [how to check a memecoin before buying]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Step 5 — Decide your loss in advance.** Use only money you can lose completely, and decide the amount before you start.

> **⚠️ Watch out**
> - **"It's only $0.0001, it can go 1000×."** A low price means nothing; many tokens exist in billions. What matters is whether the token survives and who sells to you.
> - **Many tiny trades.** Fixed network and priority fees can eat 10%+ of a $10 trade before the price moves at all.
> - **Screenshots of winners.** You see the 0.41% who won big, not the millions who lost; "gurus" often sell the coins they promote.

## What it means if you buy regularly

Regular small buys work on assets that are still around years later — not on tokens that may stop trading tonight. If you want crypto, the usual beginner path is a large, liquid coin bought a little at a time; Solana's own coin SOL, for comparison, is at {{price:sol}} right now ({{chg1y:sol}} over 12 months) — past results, not a forecast. You can test «$10 a day» on any asset in our calculator and track it on your [portfolio page]({lang}/me/).

Previous lesson: [snipers, bundlers and dev wallets]({lang}/blog/snipers-bundlers-dev-wallets/). All lessons are on the [Learn page]({lang}/learn/).

## Sources

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (January 11, 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (March 14, 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, Dune data: pump.fun graduation rate hits 2.01% (March 17, 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / CoinGecko data: nearly 70% of pump.fun tokens disappear on launch day (June 25, 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun Help Center: Transaction fees on pump.fun (September 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Not investment advice.*
