---
title: What is a DEX and how is it different from a crypto exchange?
description: What is a DEX? A plain-language guide to decentralised exchanges: AMMs, liquidity pools, wallets, gas fees, and the pros and cons compared with a CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**What is a DEX?** A DEX (decentralised exchange) is a set of smart contracts on a blockchain that lets you swap one token for another directly from your own wallet. There is no company holding your money, no account and usually no identity check. Uniswap on Ethereum, and Raydium, Orca and Meteora on Solana, are well-known examples.

A regular crypto exchange such as Binance, Coinbase or Kraken is a **CEX** (centralised exchange): a company that holds your funds, matches buyers and sellers in its own system and has to follow financial rules.

## How a DEX works

### Automated market makers (AMMs)

Most DEXs do not have an order book with buyers and sellers. Instead they use an **automated market maker** — a formula that sets the price.

The classic version, used by Uniswap v2, is the "constant product" rule: a pool holds two tokens, and the amount of token A multiplied by the amount of token B must stay the same after every trade. When you buy token A, you add token B to the pool and remove token A, so A becomes scarcer in the pool and its price goes up.

You do not need to do the maths. The key idea: **the bigger the pool, the less your trade moves the price.**

### Liquidity pools

The tokens in the pool come from **liquidity providers** — people who deposit pairs of tokens and earn a share of the trading fees (often 0.05–1% per swap). Their risk is that the prices of the two tokens drift apart, which can leave them worse off than simply holding ("impermanent loss").

For newly launched tokens, the creator usually sets up the first pool. That is why liquidity locks matter: whoever controls the pool can withdraw it.

### Your wallet is your account

To use a DEX you connect a self-custody wallet such as MetaMask (Ethereum and similar chains) or Phantom (Solana). Every trade is a transaction you sign yourself. Your **seed phrase** is the master key — lose it and the money is gone; share it and someone else takes the money.

### Gas and fees

Every DEX trade pays a network fee, called **gas** on Ethereum. On Ethereum it rises when the network is busy; Layer-2 networks and Solana are usually much cheaper — Solana's base fee is 0.000005 SOL per signature. On top of gas you pay the pool fee, and you may face **slippage** and **price impact** on small or fast-moving tokens.

## DEX vs CEX: the main differences

- **Who holds your funds:** on a DEX, you do (your wallet); on a CEX, the exchange does.
- **Account and ID check:** a DEX usually needs none; a CEX requires identity checks (KYC).
- **Token choice:** a DEX offers almost any token, including brand-new ones; a CEX only lists selected tokens.
- **Buying with a card or bank:** usually not possible directly on a DEX; standard on a CEX.
- **Fees:** DEX — gas, pool fee and slippage; CEX — trading fee, spread and withdrawal fee.
- **Help if something goes wrong:** a DEX has no support line; a CEX has customer support and sometimes protection schemes.
- **Main risks:** DEX — scam tokens, bad approvals and your own mistakes; CEX — hacks, account freezes and insolvency.

## Pros of a DEX

- **Self-custody.** No one can freeze your account or lose your money in a bankruptcy.
- **Open access.** Anyone with a wallet can trade, from almost anywhere.
- **New tokens first.** Tokens appear on DEXs long before (or instead of) any exchange listing.
- **Transparency.** Pools, trades and holders are visible on the blockchain.

## Cons of a DEX

- **You are the bank.** One mistake — a wrong address, a fake site, a malicious approval — and funds are lost for good.
- **Scam tokens.** Anyone can create a token and a pool in minutes. Most new tokens lose almost all their value; see our [rug pull checklist]({lang}/blog/how-to-spot-a-rug-pull/).
- **Hidden costs.** Slippage and price impact can cost more than the visible fee.
- **No easy on-ramp.** You usually need to buy crypto on a CEX first and send it to your wallet.
- **Smart-contract risk.** Bugs or hacks in DEX code have caused large losses.

## Which one should a beginner use?

Many people use both: a licensed CEX to turn local currency into crypto, and a DEX for tokens that are only available on-chain. For regular, long-term buying of large assets such as Bitcoin or Ethereum, a CEX with low fees is usually simpler — compare options on our [exchanges page]({lang}/exchanges/).

If you want to explore memecoins and other on-chain tokens, start with tiny amounts, a separate wallet, and the most established coins on our [memecoins page]({lang}/memes/). Our step-by-step guide [how to buy a memecoin on Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) shows the full process, including tools such as [GMGN](/go/gmgn?from=blog&l=en).

## Common DEX terms

- **Swap** — exchanging one token for another.
- **Pair** — the two tokens in a pool, such as SOL/USDC.
- **Slippage tolerance** — the maximum price change you accept.
- **Approve** — permission for a contract to move a token from your wallet (mainly on Ethereum-style chains). Revoke old approvals you no longer need.
- **Aggregator** — a service that splits your trade across several DEXs for a better price, such as Jupiter on Solana or 1inch on Ethereum.

## FAQ

### Is a DEX safer than a CEX?

It removes the risk of the exchange losing or freezing your funds, but adds the risk of your own mistakes and scam tokens. Neither is risk-free.

### Do I need ID to use a DEX?

Usually not, because you trade from your own wallet. Local laws and taxes still apply to you.

### Why did my DEX trade fail?

Common reasons: not enough native coin for gas, slippage set too low for a fast-moving price, or a token that blocks selling.

### Are DEX trades taxable?

In many countries, yes — a swap from one token to another can count as a sale. Keep records of your trades.

## Sources

- [How Uniswap works (Uniswap docs)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas and fees (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Solana docs: fee structure](https://solana.com/docs/core/fees/fee-structure)

*Not investment advice. This guide explains how DEXs work and does not recommend any platform or token.*
