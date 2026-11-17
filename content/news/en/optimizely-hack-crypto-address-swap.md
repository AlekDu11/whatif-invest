---
title: Optimizely hack put a crypto address-swapping script on 178 big websites
description: A flaw in Optimizely's testing tool let an attacker swap crypto wallet addresses on sites like CNN, BBC and Zoom on November 16. How to stay safe.
date: 2026-11-17 10:40
tags: hacks, bitcoin
assets: btc, eth, sol
---
On Monday, November 16, an attacker abused a flaw in Optimizely Web Experimentation, an A/B-testing tool used by large companies, and slipped malicious JavaScript onto the websites of at least 178 organisations, including CNN, the BBC, Zoom, HSBC and the hardware-wallet maker Ledger. The script quietly replaced crypto wallet addresses with the attacker's own.

## What happened

- **A supply-chain attack.** The code was served from Optimizely's own CDN with a valid certificate, so affected sites looked normal. Security firm Report URI found it in 188 of 1,611 snippets it checked, and says the true number is likely higher.
- **Addresses swapped everywhere.** The script targeted bitcoin, ether and other EVM chains, Tron, Solana, TON, Litecoin, Bitcoin Cash and Dogecoin addresses — in page text, forms, links and even the clipboard.
- **Cards and iPhones too.** A card skimmer was added at 13:43 UTC, and a hidden frame tried to load exploit kits aimed at older iOS versions. No iPhone has been confirmed compromised.
- **Small haul so far.** The attacker's wallets received about $7,040 within roughly nine hours, most of it in BTC. Optimizely says it has removed the code and secured affected accounts.

## What it means for you

If you sent crypto on Monday after copying an address from a website, check that it reached the right wallet. A good habit for every transfer: compare the first and last characters of the address, and confirm it on your hardware wallet's screen. Update iPhones to iOS 18.7.3 / 26.3 or later. Bitcoin trades at {{price:btc}}, far below its $126,080 record — see where every coin stands on our [from-ATH page]({lang}/ath/), and pick a platform carefully with our [exchange comparison]({lang}/exchanges/).

## Sources

- [Report URI — World's largest brands infected with malware via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [The Hacker News — Hijacked Optimizely scripts served card skimmer and iOS exploit kits](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html)
- [U.Today — Crypto-stealing exploit in JavaScript emerges](https://u.today/major-crypto-stealing-exploit-in-javascript-emerges-zoom-cnn-hsbc-affected)

*Not investment advice. WhatIfStack articles are prepared with the help of AI tools, including Anthropic's Claude.*
