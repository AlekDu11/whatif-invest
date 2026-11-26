---
title: THORChain (RUNE) explained: swaps of native bitcoin and other coins across blockchains, no wrapped tokens
description: THORChain in plain language: how cross-chain swaps and RUNE liquidity pools work, node bonds, the 2021 hacks, the 2025 lending freeze, main risks and regular buying.
date: 2026-11-26
kind: analysis
---
**THORChain (RUNE)** is a blockchain that lets people swap coins between different networks — for example real bitcoin for real ether — without a central exchange and without "wrapped" copies of the coins. RUNE is the token at the centre of it: every trading pool is paired with RUNE, and the computers that run the network must lock RUNE as a security deposit. All RUNE in circulation is worth {{mcap:rune}} today ({{rank:rune}} among cryptocurrencies).

> **Key takeaways**
> - THORChain swaps native assets across chains such as Bitcoin, Ethereum, BNB Chain, Dogecoin and others in one step.
> - Every liquidity pool is paired with RUNE, and node operators bond RUNE that can be taken away if they misbehave.
> - Its record high is {{ath:rune}} ({{athd:rune}}); today the price is {{fromath:rune}} from it.
> - The network was hacked twice in 2021 and froze its lending and savings products in January 2025.

## How it works

THORChain is built with the Cosmos SDK. A group of independent nodes jointly controls "vaults" — addresses on Bitcoin, Ethereum and the other connected chains — using threshold signatures, so no single node can move the funds. When you swap BTC for ETH, you send bitcoin to a vault; the network sells it for RUNE in the BTC pool and then sells that RUNE for ETH in the ETH pool, and a vault sends you real ether. Prices come from the pool balances, as on [Uniswap]({lang}/uni/). Liquidity providers deposit coins into pools and earn a share of swap fees. Nodes must bond RUNE worth more than the funds they help guard, which is meant to make stealing unprofitable.

## Why people think it has value

Moving value between blockchains is usually slow, risky or requires a centralised exchange with account checks. THORChain offers a direct route between native coins, which is why many crypto wallets and swap apps route trades through it. RUNE demand comes from three places: it is half of every pool, it is the bond nodes must post, and part of swap fees goes to those who hold and stake it. Higher trading volume therefore means more fees for RUNE holders.

## The numbers right now

- Price today: {{price:rune}}
- Record high: {{ath:rune}} ({{athd:rune}}), {{fromath:rune}} from it
- Market value: {{mcap:rune}} ({{rank:rune}} among cryptocurrencies)
- Price change over 12 months: {{chg1y:rune}}
- $10 a day for 5 years: {{dca:rune:5}} from {{dcainv:5}} invested ({{dcaroi:rune:5}})

## Its story so far

RUNE first went on sale through Binance Launchpad in July 2019. A "chaosnet" with real money, deliberately capped, went live in 2020, and multi-chain trading followed in April 2021. In the 2021 boom RUNE reached about $20 in May 2021, but in July 2021 the network suffered two exploits worth millions of dollars. The full mainnet was declared in June 2022. In January 2025 THORChain paused its lending and "savers" products after they built up around $200 million in obligations; the debt was later converted into a separate TCY token. In February 2025 hackers behind the $1.4 billion theft from the Bybit exchange used THORChain to swap stolen ether into bitcoin, bringing record volumes and sharp criticism.

## Alternatives

Centralised exchanges remain the easiest way to swap between chains. On-chain rivals include bridge-and-aggregator services and Maya Protocol, a THORChain fork. For swaps within one network, people use decentralised exchanges like [Uniswap]({lang}/uni/) or [PancakeSwap]({lang}/cake/). For connecting blockchains in general, [Cosmos]({lang}/atom/) and [Chainlink]({lang}/link/) offer other approaches.

## Main risks

- **Big swings:** RUNE has fallen by more than 80% from its peak more than once.
- **Hacks:** cross-chain vaults hold large sums and have been attacked before; a new bug could cost users money.
- **Product failures:** the 2025 lending freeze showed that new features can create losses for users and pressure on RUNE.
- **Regulation:** use by hackers to launder funds draws attention from regulators and could lead to restrictions.
- **Dependence on RUNE:** because every pool is paired with RUNE, a sharp RUNE drop hits the whole system.

## What it means if you buy regularly

RUNE is a bet that people will keep using THORChain for cross-chain swaps, and its history includes hacks and a frozen product as well as fast rallies. Buying a fixed amount regularly evens out your entry price, but it does not protect you from project-specific shocks. Many people keep a specialised token like RUNE to a small part of their savings. Past results do not guarantee future returns.

*Not investment advice.*

## Sources

- [THORChain documentation — introduction (docs.thorchain.org)](https://docs.thorchain.org/)
- [RUNE rallies 15% as THORChain restarts most swaps after outage (Cointelegraph)](https://cointelegraph.com/markets/rune-rallies-15-as-thorchain-restarts-most-swaps-after-outage)
- [THORChain price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/thorchain)
