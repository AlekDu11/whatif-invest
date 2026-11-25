---
title: Starknet（STRK）通俗解读：StarkWare打造的Ethereum二层网络，2021年上线，如今支持比特币质押
description: 用大白话看Starknet：这个ZK-STARK二层网络如何让Ethereum更便宜、STRK有什么用、比特币质押、发展历程、竞争对手和主要风险。
date: 2026-11-25
kind: analysis
---
**Starknet**是运行在[Ethereum]({lang}/eth/)之上的"二层"网络：它把成千上万笔交易打包在一起，用密码学证明这些交易全部正确，再把这份证明提交到Ethereum上。这样一来，使用应用的成本只有直接在Ethereum上操作的一小部分。它由以色列公司StarkWare开发，于2021年11月上线。其代币STRK的总市值为{{mcap:strk}}（在加密货币中排名{{rank:strk}}）。

> **要点**
> - 2024年2月代币推出时共创造了100亿枚STRK；质押奖励还会在此基础上增发新币。
> - 自2025年9月起，封装比特币的持有者可以在Starknet上质押，并有一项1亿枚STRK的激励计划作为支持。
> - 历史最高价为{{ath:strk}}（{{athd:strk}}）；当前价格距离该高点{{fromath:strk}}。
> - Starknet使用自己的编程语言Cairo，而不是Ethereum的Solidity。

## 它如何运作

Starknet是一种"ZK Rollup"。交易在Starknet上执行，随后由证明者生成一份STARK——一份简短的数学证明，表明每一步计算都正确无误。Ethereum只需检查这份证明，而不必把工作重做一遍，于是许多笔交易可以分摊一次低成本的检查，同时依然依托Ethereum的安全性。StarkWare联合创始人Eli Ben-Sasson是发明STARK证明的科学家之一；项目方表示，这种证明还能抵御未来的量子计算机。开发者用Cairo编写Starknet应用，这门语言的设计目标就是让程序易于证明。

## STRK有什么用

STRK用于支付Starknet上的交易手续费，用于对网络升级进行投票，还可以用来质押：持有者把STRK委托给验证者，帮助保障网络安全，并获得新的STRK作为奖励。质押于2024年11月开启。2025年8月，一次链上投票（SNIP-31，约93.6%赞成）允许封装比特币——WBTC、tBTC、LBTC和SolvBTC——与STRK一起质押，比特币质押于2025年9月30日正式上线。2026年2月，Starknet发布了strkBTC，这是一种以比特币为支撑的代币，余额可以保密，转账内容也可以隐藏。

## 最新数据

- 当前价格：{{price:strk}}
- 历史最高价：{{ath:strk}}（{{athd:strk}}），距高点{{fromath:strk}}
- 市值：{{mcap:strk}}（在加密货币中排名{{rank:strk}}）
- 12个月价格变化：{{chg1y:strk}}
- 每天10美元、坚持1年：投入{{dcainv:1}}，变成{{dca:strk:1}}（{{dcaroi:strk:1}}）

## 一路走来

StarkWare成立于2018年，最初以StarkEx的形式出售技术，这是dYdX、Immutable等交易所使用的引擎。通用型网络Starknet于2021年11月开放。STRK代币于2024年2月20日推出，同时向用户和开发者进行了大规模空投；它的最高价出现在上线的头几天，之后两年的大部分时间里一路下跌，因为早期投资者和团队持有的大量代币在逐步解锁。2025–2026年，项目把Starknet重新定位为不仅能用Ethereum、也能用比特币的地方。

## 替代选择

Starknet与其他Ethereum二层网络竞争：[Arbitrum]({lang}/arb/)和[Optimism]({lang}/op/)（乐观Rollup）、Coinbase的Base，以及[ZKsync]({lang}/zk/)、Scroll、Linea等其他ZK Rollup。它的独特之处在于STARK证明和Cairo语言；缺点是Ethereum开发者必须学习一门新语言。

## 主要风险

- **竞争：** 众多二层网络争夺同一批用户和应用，而使用最多的几个网络拿走了大部分活跃度。
- **代币供应：** 质押会增发STRK，早期投资者和贡献者的代币也在数年间陆续解锁。
- **技术：** 复杂的密码学、跨链桥和封装比特币的发行方都可能出故障或遭黑客攻击；网络的部分环节仍由少数运营方掌控。
- **价值捕获：** 低廉的手续费对用户有利，但能支撑代币价格的收入也随之减少。
- **大幅波动：** 和大多数年轻代币一样，STRK曾经从高点跌去大部分价值。

## 对定投者意味着什么

STRK是一种年轻、波动剧烈的代币，价格历史很短，因此到目前为止在这里定投的人经历的主要是不断下跌的价格。定期投入固定金额可以分散买在坏时机的风险，但无法防范长期下跌。很多人只把这类代币控制在加密资产持仓中很小的一部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Starknet扩展BTCFi，推出比特币质押和收益产品（The Block）](https://www.theblock.co/post/372720/starknet-bitcoin-staking-100m-strk-incentives-re7-btc-yield)
- [Starknet推出strkBTC，把"隐私比特币"带到其二层网络（The Block）](https://www.theblock.co/post/391420/starknet-introduces-strkBTC-to-bring-private-bitcoin-and-confidential-defi-transactions-to-its-layer-2-network)
- [Starknet在二层网络上推出比特币质押（ForkLog）](https://forklog.com/en/starknet-introduces-bitcoin-staking-on-l2-network/)
- [Starknet力图让比特币"动起来"（Blockworks）](https://www.blockworks.co/news/starknet-making-btc-productive)
- [Starknet博客（starknet.io）](https://www.starknet.io/blog/all/)
