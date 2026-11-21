---
title: Bitcoin Core fixes AI-found bug that could stall nodes; update to 30.5 or 31.3
description: Bitcoin Core 30.5 and 31.3 patch a medium-severity bug, found by an AI scanner at Block's Spiral, that let one peer freeze a node for over 10 seconds at a time.
date: 2026-11-21 14:30
tags: bitcoin, hacks, ai
assets: btc
---
Bitcoin's main software got a security fix for a flaw that an AI tool found first. Bitcoin Core versions 30.5 and 31.3, released on Friday, November 20, close a bug that let a single peer make a node stop working for more than ten seconds per message.

## What happened

- **The bug.** Tracked as CVE-2026-117348 and rated medium severity. A peer could repeat one transaction ID up to 50,000 times in a single announcement; the node checked every copy and froze, ignoring even new blocks.
- **Who found it.** Loupe, an open-source scanner from Block's Spiral team that uses AI agents, flagged it; the advisory credits an automated AI scan through Elias Rohrer's Project Loupe.
- **The fix.** Patched nodes now handle each announced transaction only once. The retired 29.x branch gets no fix, per The Defiant.
- **Risk.** No funds or coins were at risk. CoinDesk notes the realistic harm was delay — an exchange slower to credit deposits, or a miner briefly working on a stale chain.

## Our angle

This is not the cause of Saturday's sell-off; bitcoin fell with stocks and crypto leverage. It is a sign that AI is now finding bugs in core crypto code, for attackers and defenders alike. If you run a node, update to 30.5 or 31.3. If you just hold bitcoin, nothing changes. Bitcoin trades at {{price:btc}}, more than 50% below its record — see the [from-ATH page]({lang}/ath/) and our [AI markets page]({lang}/ai/). $10 a day for 5 years ({{dcainv:5}}) is now worth {{dca:btc:5}} ({{dcaroi:btc:5}}). History, not a forecast.

## Sources

- [CoinDesk — Bitcoin nodes could be stalled by repeating one ID 50,000 times](https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug)
- [The Defiant — Bitcoin Core fixes AI-found bug that could stall nodes](https://thedefiant.io/news/security/bitcoin-core-fixes-ai-found-bug-that-could-stall-nodes)
- [Coinotag — Bitcoin Core patches node-stalling bug in 30.5, 31.3](https://en.coinotag.com/bitcoin-core-fixes-node-stall-cve-2026-117348)

*Not investment advice.*
