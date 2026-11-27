---
title: "Snipers, bundlers and dev wallets: how insiders profit at a memecoin launch"
description: Bots and insiders buy many new memecoins in the first second and sell within minutes. How snipers, bundlers and dev wallets work and how to spot them.
date: 2026-11-27T09:30:00Z
category: learn
track: memes
step: 16
assets: sol, bnb
stat: 87%
stat_label: of deployer-linked snipes on pump.fun were profitable (Pine Analytics, April 2025)
---
**Who buys a new memecoin before you can even see it?** Often bots and insiders: **snipers** buy in the very first block, **bundlers** buy with many wallets at once, and the **dev wallet** (the creator's own wallet) can hold a big share from the start. They buy cheapest and often sell within minutes — to the people who arrive later.

> **Key takeaways**
> - Pine Analytics found that over **50%** of pump.fun tokens were sniped in the same block they were created (report of April 21, 2025).
> - In one month (from March 15, 2025) it counted **15,000+** snipes by wallets funded directly by the token's creator; **87%** were profitable and about **85%** fully sold within **5 minutes**.
> - CoinGecko found that **68.67%** of 18.67 million pump.fun tokens made their last trade on launch day (January 2024 – June 2026, reported June 25, 2026).

## The three insiders, in plain words

All three words are in our [memecoin glossary]({lang}/memes/glossary/).

- **Sniper** — a wallet, almost always a bot, that buys in the first 0–3 blocks (a block is one "page" of the blockchain, under a second on Solana). It uses special tools to get in before ordinary buyers, takes a big position cheaply and sells into the first wave of demand.
- **Bundler** — one person who buys with many wallets in the same block or the same transaction. On the chart it looks like 20 different buyers; in fact it is one. Goal: hide how much one person owns and fake demand.
- **Dev wallet** — the wallet that created the token. If it keeps a large share, or quietly sends tokens to fresh wallets, it can sell on everyone at any moment.

Pine Analytics' report "Exit Liquidity Machines" (exit liquidity = the late buyers whose money insiders sell into) showed how this works on pump.fun: creators sent SOL to fresh "burner" wallets, those wallets bought in the creation block, and most sold in one or two trades. Over 55% of these snipes were fully closed in under a minute.

## Step 1 — Look at the first buyers

Open the token on a tracker (on our [memes page]({lang}/memes/) the token page shows holders and a safety check; tools like GMGN or Solscan show the first trades). If many wallets bought **in the same second as the launch**, with **similar amounts**, that is sniping or bundling.

## Step 2 — Check how much the top holders own

Look at the **top-10 holders** without the liquidity pool. Data provider Mobula describes top-10 under **30%** and a dev share under **5%** (or locked/burned) as healthy, and top-10 above **50%** as a red flag. Several sniper wallets holding over 20% together is another one.

## Step 3 — Check the dev wallet

Find the creator ("dev", "deployer" or "creator" on the token page). Did it sell already? Did it send tokens to new wallets just before or after launch? Has the same wallet launched many tokens that all died? A dev who launches dozens of coins a week is running a machine, not a project.

## Step 4 — Look for fresh wallets funded from one place

Bundles often come from wallets created minutes before launch and funded by the same source. Bubble-map tools draw them as one connected cluster. If the "community" is one cluster, the price is in one person's hands.

## Step 5 — Never chase the first candle

The jump in the first minutes is when snipers sell. If you still want to buy, wait, run the full check from [how to check a memecoin before buying]({lang}/blog/how-to-check-a-memecoin-before-buying/), use a small amount and set your limit in advance.

> **⚠️ Watch out**
> - **"Lots of holders = safe."** Bundlers create hundreds of holders with one wallet. Look at who funded them, not how many there are.
> - **"The dev burned/locked tokens."** Check it on-chain yourself; a locked pool does not stop sniper wallets from selling.
> - **Copy-trading "smart money" bots.** Wallets that look like geniuses are often the snipers themselves, or the dev; by the time you copy them, they are selling.

## What beginners can learn from it

At a launch you are usually not early — the bots are. Nearly 7 in 10 pump.fun tokens stopped trading on their first day, so the safest choice is often not to play at all. If you do, treat it as money you can lose completely. Regular buying works on assets that survive years; Solana's own coin SOL, for comparison, is at {{price:sol}} right now ({{chg1y:sol}} over 12 months) — past results, not a forecast.

Previous lesson: [how Binance Alpha works]({lang}/blog/how-binance-alpha-works/). Next: why most memecoin buyers lose money. All lessons are on the [Learn page]({lang}/learn/).

## Sources

- [Pine Analytics: Exit Liquidity Machines — dissecting pump.fun farming (April 21, 2025)](https://pineanalytics.substack.com/p/exit-liquidity-machines)
- [BeInCrypto: Pump.fun meme coin snipers are a systematic problem (April 22, 2025)](https://beincrypto.com/pump-fun-meme-coin-snipers-systematic-problem)
- [Mobula docs: Detecting snipers and bundlers](https://docs.mobula.io/almanac/detecting-snipers-bundlers)
- [KuCoin News / CoinGecko data: nearly 70% of pump.fun tokens disappear on launch day (June 25, 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)

*Not investment advice.*
