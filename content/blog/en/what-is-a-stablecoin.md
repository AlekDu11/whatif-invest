---
title: What is a stablecoin (USDT, USDC) and why it matters
description: Stablecoins like USDT and USDC explained simply: how they try to stay at $1, what backs them, where people use them and what risks to understand.
date: 2026-11-15
category: learn
track: crypto
step: 4
assets: btc, eth
stat: $1
stat_label: the price a stablecoin like USDT or USDC is designed to hold
---
A **stablecoin** is a crypto token designed to keep a steady price — usually exactly **$1**. It moves like crypto (fast, 24/7, across borders) but is meant to hold its value like ordinary money.

The two best-known examples are **USDT** (Tether) and **USDC** (Circle). Together they make up most of the stablecoin market, and on many exchanges they are the main currency for trading Bitcoin and other coins.

> **Key takeaways**
> - A stablecoin is a crypto token that tries to stay worth exactly $1 — USDT and USDC are the biggest.
> - On an exchange it works as a "waiting room" for your money: you can step out of Bitcoin without sending money back to the bank.
> - It is not a bank deposit: it can briefly lose its $1 price, the issuer can freeze it, and sending it on the wrong network can lose it.

## Why stablecoins exist

Bitcoin and most coins move up and down a lot. Bitcoin right now costs {{price:btc}}, and it can change by several percent in a day. That is a problem if you just want to:

- park money between trades without converting back to a bank,
- send a payment and be sure it is worth the same when it arrives,
- price something in dollars on a blockchain.

Stablecoins solve this by tying the token to a currency people already trust — most often the US dollar, sometimes the euro or gold.

## How stablecoins keep $1

There are three main designs.

### 1. Backed by cash and bonds (fiat-backed)

This is how USDT and USDC work. A company issues one token for every dollar it receives and holds reserves — mostly cash, bank deposits and short-term US government bonds (Treasury bills).

- You give the issuer $1 → it creates 1 token.
- You return 1 token → it destroys it and pays you $1 (usually only for verified large customers).

Because big traders can always swap tokens for dollars, the price on exchanges stays very close to $1. If it falls to $0.99, traders buy cheap tokens and redeem them for $1, pushing the price back up.

Issuers publish reserve reports or attestations from accounting firms. How detailed and frequent these are differs between issuers — this is one of the main things to compare.

### 2. Backed by other crypto (crypto-collateralised)

Here a smart contract holds more crypto than the stablecoins it issues — for example, $150 of Ether locked for every $100 of stablecoins. If the collateral price falls too far, it is automatically sold. DAI (now part of the Sky ecosystem) is the best-known example. No company holds dollars, but the system depends on the code and on the price of the collateral.

### 3. Algorithmic

These try to hold $1 using code and a second "partner" token, with little or no real reserves. The best-known case, **TerraUSD (UST)**, collapsed in May 2022 and wiped out tens of billions of dollars in days. Most people now treat purely algorithmic designs as very high risk.

## What people use stablecoins for

- **Trading.** On many exchanges, coins are priced against USDT or USDC. Traders move into stablecoins to "step out" of the market without leaving the exchange.
- **Sending money abroad.** A transfer can arrive in minutes, any day of the week, often with a low network fee.
- **Saving in dollars.** In countries with high inflation or a falling currency, some people hold stablecoins as a digital dollar account.
- **Payments and business.** Freelancers and companies use them to pay and get paid across borders.
- **Decentralised finance (DeFi).** Stablecoins are lent, borrowed and used as collateral in on-chain apps.

For a regular investor following a DCA plan, a stablecoin can be a waiting room: money that is deposited on an exchange but not yet invested. It is not an investment that grows on its own — the target is always $1.

## The risks you should understand

A stablecoin is only as good as what stands behind it. Key risks:

- **De-pegging.** The price can drop below $1 if people doubt the reserves. In March 2023 USDC briefly fell to about $0.88 when part of its reserves was stuck at the failed Silicon Valley Bank; it recovered after the bank's deposits were guaranteed.
- **Issuer risk.** With fiat-backed coins you trust a company: its reserves, its bank partners and its honesty.
- **Freezes.** Issuers can freeze tokens at specific addresses, for example at the request of law enforcement.
- **Regulation.** Rules are tightening. In the EU, the MiCA regulation sets requirements for stablecoin issuers, and some coins were delisted for EU users. The US passed federal stablecoin rules in 2025 (the GENIUS Act). Rules differ by country and keep changing.
- **Smart-contract and platform risk.** Bugs, hacks or an exchange failure can affect your funds even if the stablecoin itself is fine.
- **No deposit insurance.** In most countries stablecoins are not covered by bank deposit guarantees.
- **"Yield" offers.** Platforms that pay high interest on stablecoins take risks with your money somewhere. High promised returns are a warning sign.

## USDT vs USDC in simple terms

Without recommending either:

- **USDT (Tether)** — the largest by market value and the most widely traded, especially in Asia and on many global exchanges. It has faced criticism in the past about reserve transparency and now publishes quarterly attestations.
- **USDC (Circle)** — the second largest, issued by a US company, with monthly reserve reports; authorised under MiCA in the EU.

Both run on several blockchains (Ethereum, Tron, Solana and others). Always send a stablecoin on the **same network** the receiver supports — sending USDT on the wrong network can lose the funds.

## How to use a stablecoin carefully

1. Use regulated exchanges and check which stablecoins they support in your country.
2. Double-check the network and address before every transfer; send a small test first.
3. Do not keep more on any single platform than you can afford to have frozen.
4. Read the issuer's latest reserve report.
5. Remember: holding a stablecoin is holding dollars-in-crypto, not an investment with expected growth.

> **⚠️ Watch out**
> - **Wrong network.** Sending USDT on a network the receiver does not support (for example TRC-20 to an ERC-20 address) can lose the money for good. Send a small test first.
> - **"Guaranteed" interest.** Offers of 10–30% a year on stablecoins are a classic scam or a hidden risk.
> - **Look-alike tokens.** Anyone can create a token called "USDT". Only the official contract on the exchange or in your wallet counts.

Next step: find an exchange that works in your country on our [exchanges page]({lang}/exchanges/), and see all lessons in [Learn]({lang}/learn/).

If your goal is long-term regular investing, compare how assets actually performed with our [DCA calculator]({lang}/compare/) and read [what DCA is]({lang}/blog/what-is-dca/).

## FAQ

### Is a stablecoin the same as a dollar in the bank?

No. It aims to be worth $1, but it is a claim on a private issuer or a smart contract, usually without deposit insurance.

### Can a stablecoin lose its value?

Yes. Prices can drop below $1 during a crisis of trust, and algorithmic stablecoins such as UST have collapsed completely.

### Do stablecoins pay interest?

The token itself does not. Platforms that offer interest lend or invest your coins, which adds risk.

### Why do exchanges use USDT and USDC?

They let traders hold a dollar value inside crypto without bank transfers, and they work 24/7 across borders.

## Sources

- [Tether — Transparency and reserves](https://tether.to/en/transparency/)
- [Circle — USDC transparency](https://www.circle.com/transparency)
- [ESMA — Markets in Crypto-Assets Regulation (MiCA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)
- [DefiLlama — Stablecoins by market cap](https://defillama.com/stablecoins)

*Not investment advice. This article explains how stablecoins work and does not recommend any coin, issuer or platform.*
