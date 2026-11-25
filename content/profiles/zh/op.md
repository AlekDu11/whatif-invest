---
title: Optimism（OP）通俗解读：以太坊二层网络、支撑Base的OP Stack与超级链
description: 用大白话看Optimism：这个以太坊二层网络如何运作、OP代币有什么用、超级链与Base、代币回购、解锁，以及主要风险。
date: 2026-11-25
kind: analysis
---
**Optimism**是建立在以太坊之上的"二层网络"（Layer 2）：它让交易更快、成本低得多，同时安全性仍依靠以太坊。它的免费软件**OP Stack**还支撑着其他网络，包括Coinbase旗下的Base，这些网络合起来组成**超级链**（Superchain）。代币**OP**让持有人可以投票决定这一切如何运营，目前市值为{{mcap:op}}（在加密货币中排名{{rank:op}}）。

> **要点**
> - OP于2022年5月上线，初始供应量为4,294,967,296枚；治理投票每年最多可增发2%。
> - 历史最高价为{{ath:op}}（{{athd:op}}），当前价格距高点{{fromath:op}}。
> - 在Optimism上的手续费用ETH支付，而不是OP；自2026年1月起，超级链收入的一半用于回购OP。
> - 团队和早期投资者的代币按月解锁，持续带来新的供应。

## 它如何运作

Optimism是一种**乐观Rollup**（Optimistic Rollup）：它在自己的链上执行交易，再把压缩后的数据批量写回以太坊。由OP Labs运营的**排序器**（Sequencer）负责给交易排序，并在几秒内确认。只要没人证明有误，结果就被默认为正确（所以叫"乐观"）：自2024年6月起，任何人都可以提交**错误证明**（fault proof），争议在以太坊上裁决。这也是提现回以太坊需要大约一周的原因。由于OP Stack是开源的，其他公司也用它搭建自己的链——Base（Coinbase）、Unichain（Uniswap）、World Chain、Ink（Kraken）、Soneium（索尼）——其中许多会把部分手续费收入分给Optimism Collective。

## 代币有什么用

OP主要是治理代币。在**代币院**（Token House）中，OP持有人或他们的代表就升级、资助和金库进行投票；第二个议院**公民院**（Citizens' House）则决定对公共物品的奖励。使用网络并不需要OP：Gas费用ETH支付。OP与使用量的联系来自超级链：2026年1月，持有人批准了一项计划，把各条链支付给Collective的收入的50%用于回购OP。

## 最新数据

- 当前价格：{{price:op}}
- 历史最高价：{{ath:op}}（{{athd:op}}），距高点{{fromath:op}}
- 市值：{{mcap:op}}（在加密货币中排名{{rank:op}}）
- 12个月价格变化：{{chg1y:op}}
- 每天10美元、坚持3年：投入{{dcainv:3}}，变成{{dca:op:3}}（{{dcaroi:op:3}}）

## 一路走来

Optimism于2021年1月向部分应用开放主网，2021年12月向所有人开放。OP代币于2022年5月31日上线，并向用户空投；上线过程并不顺利，几天后做市商Wintermute把2000万枚OP发到错误地址而丢失，其中大部分后来被归还。2023年6月的**Bedrock**升级降低了成本；2023年8月，Coinbase基于OP Stack推出Base，Base很快成为最繁忙的二层网络。OP在2024年3月达到约4.84美元的高点，随后在2024年和2025年大幅下跌。2026年1月，持有人批准了回购计划。

## 替代选择

Optimism与以太坊的其他二层网络竞争：按锁仓价值计最大的[Arbitrum]({lang}/arb/)；[ZKsync]({lang}/zk/)和[Starknet]({lang}/strk/)等零知识Rollup；还有[Mantle]({lang}/mnt/)和[POL (ex-MATIC)]({lang}/pol/)。基于Optimism自身技术打造的Base没有代币，既是合作伙伴，也是竞争对手。[以太坊]({lang}/eth/)本身也是一种选择，因为它自身的升级让使用成本越来越低。

## 主要风险

- **新增供应：**团队和投资者的按月解锁仍在继续，治理每年最多还可增发2%。
- **依赖Base：**超级链收入中很大一部分来自Coinbase的这条链；如果Base离开或少付，OP将失去大部分收入。
- **中心化排序器：**在OP主网上由一个运营方给交易排序；一旦它宕机，用户只能依靠更慢的备用通道。
- **竞争：**Arbitrum和零知识Rollup在争夺同一批用户、应用和手续费。
- **监管：**关于代币、回购和DAO的规则因国家而异，也可能改变。

## 对定投者意味着什么

过去几年里，OP大部分时间都在从2024年的高点往下走，所以定投者在越来越低的价格上攒下了越来越多的代币——只有价格回升，这才有帮助。定期买入固定金额可以分散择时风险，但不能消除亏损风险。很多人只把这类代币当作储蓄中的一小部分。过去的表现不代表未来的收益。

*不构成投资建议。*

## 资料来源

- [Optimism官方文档：OP Stack与超级链（docs.optimism.io）](https://docs.optimism.io/)
- [OP代币回购（Optimism博客，2026年1月8日）](https://www.optimism.io/blog/op-token-buybacks)
- [OP代币持有人批准回购计划（The Block，2026年1月29日）](https://www.theblock.co/post/387660)
- [Optimism价格、市值与历史最高价（CoinGecko）](https://www.coingecko.com/en/coins/optimism)
