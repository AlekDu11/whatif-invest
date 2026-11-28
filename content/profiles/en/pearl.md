---
title: Pearl (PEARL) explained: GPU mining with Proof of Useful Work, 2.1 billion max supply
description: Pearl in plain language: how its GPU mining is tied to AI computing, the 2.1 billion supply, the April 2026 launch, the criticism, rivals and main risks.
date: 2026-11-28
kind: analysis
---
**Pearl** is a new layer-1 blockchain mined with Nvidia graphics cards. Instead of the pointless hash puzzles that Bitcoin miners solve, its "Proof of Useful Work" asks miners to do matrix multiplication — the same maths that runs AI models — so in theory one GPU can serve AI customers and secure the network at the same time. It was built by Pearl Research Labs, co-founded by computer scientist Omri Weinstein, and its main network launched on 27 April 2026. Its market value today is {{mcap:pearl}} ({{rank:pearl}} among cryptocurrencies).

> **Key takeaways**
> - There will never be more than 2.1 billion coins, 100 times Bitcoin's 21 million; the mining reward shrinks smoothly instead of halving.
> - Its record high is {{ath:pearl}} ({{athd:pearl}}); today the price is {{fromath:pearl}} from it.
> - The project says there was no premine, no investor allocation and no team treasury: all coins come from mining.
> - A June 2026 research paper found that the mining done at that time produced no useful AI work at all.

## How it works

Miners run "noisy" matrix multiplications on their GPUs, hash small pieces of the result and wrap the work in a zero-knowledge proof, so anyone can check it quickly without redoing it. The method comes from a 2025 cryptography paper co-written by Weinstein. The official miner plugs into vLLM, popular software for serving AI models, on data-centre cards such as Nvidia's H100 and H200, while community-made miners also run on gaming RTX cards. Under the hood Pearl works much like Bitcoin: it is based on btcd, a Bitcoin node program, and a new block arrives every few minutes. The coin is often listed under the ticker PRL, and another, unrelated token uses the same ticker on some price sites.

## What the token is used for

Coins are created only as rewards for miners, and they are used to pay transaction fees. The first commercial example came in May 2026: the AI cloud company Together AI offered a Gemma model running on Pearl miners for more than 25% below its usual price, with the discount paid for by PRL rewards. If AI customers really use the network this way, mining stops being pure energy spending; if they do not, Pearl is simply another proof-of-work coin with a large supply.

## The numbers right now

- Price today: {{price:pearl}}
- Record high: {{ath:pearl}} ({{athd:pearl}}), {{fromath:pearl}} from it
- Market value: {{mcap:pearl}} ({{rank:pearl}} among cryptocurrencies)
- Price change over 12 months: {{chg1y:pearl}}

## Its story so far

The underlying paper was published in April 2025, and the main network went live on 27 April 2026 with no coins handed out in advance. In late May, after the Together AI deal, a rush of gamers and GPU owners started mining, and within weeks the daily earnings of a top RTX 5090 card fell by about half as competition grew. At first the coin traded only on small exchanges with thin liquidity, such as MEXC. In June 2026 an arXiv paper, "The Usefulness Gap in Proof-of-Useful-Work", reported that the network's thousands of miners were producing no useful AI computation and that the most popular mining software contained no AI code. Pearl added support for mixture-of-experts AI models in a June hard fork, and by October 2026 about 16% of the maximum supply had been mined.

## Alternatives

[Bitcoin]({lang}/btc/) is the classic proof-of-work coin, mined with specialised chips rather than GPUs. Among AI and computing projects, [Bittensor]({lang}/tao/) rewards people who run AI models, while [Render]({lang}/render/), [Akash Network]({lang}/akt/) and [io.net]({lang}/io/) rent out GPU power directly. Pearl's idea is different: the mining itself is supposed to be the useful AI work.

## Main risks

- **Very new:** the coin has only a few months of price history, and young coins can lose most of their value quickly.
- **Usefulness not proven:** independent researchers found little real AI work so far; the main selling point may not hold.
- **Mining economics:** rising difficulty and a falling reward cut miners' earnings, and miners often sell coins to pay for power.
- **Concentration:** coins were cheap to mine in the first weeks, so early participants hold a large share.
- **Liquidity and look-alikes:** trading is thinner than for big coins, and a different token with the same PRL ticker exists — check the contract and exchange carefully.

## What it means if you buy regularly

Pearl has traded for only a few months, so there is no meaningful record of what regular buying would have done. Buying a fixed amount on a schedule spreads the risk of bad timing, but with a brand-new coin it does not remove the risk of losing most of the money. Many people keep experimental coins like this to a very small part of their savings. Past results do not guarantee future returns.

*Not investment advice.*

## Sources

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
