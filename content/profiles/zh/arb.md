---
title: Arbitrum（ARB）通俗解读：以太坊二层网络、乐观Rollup与100亿枚ARB上限
description: 用大白话看Arbitrum：这个以太坊二层网络如何运作、ARB在DAO里有什么用、代币解锁、一路走来的历程，以及主要风险。
date: 2026-11-23
kind: analysis
---
**Arbitrum**是建立在以太坊之上的网络，让交易更快、成本低得多，同时安全性仍依靠以太坊，这类网络被称为"二层网络"（Layer 2）。它由美国公司Offchain Labs开发，代币**ARB**让持有人可以投票决定网络及其金库如何运营。ARB目前的市值为{{mcap:arb}}（在加密货币中排名{{rank:arb}}）。

> **要点**
> - ARB的总量永远不会超过100亿枚；2023年3月上线时，约42%分给DAO金库，约27%分给团队，17.5%分给投资者。
> - 历史最高价为{{ath:arb}}（{{athd:arb}}），当前价格距高点{{fromath:arb}}。
> - ARB是治理代币：在Arbitrum上的手续费用ETH支付，而不是ARB。
> - 自2024年3月起，团队和投资者的代币每月解锁，给市场带来新的供应。

## 它如何运作

Arbitrum是一种**乐观Rollup**（Optimistic Rollup）。它不让以太坊的每个节点都处理每一笔交易，而是在自己的链上执行交易，再把压缩后的数据批量写回以太坊。由Offchain Labs运营的唯一一个**排序器**（Sequencer）负责给交易排序，并在不到一秒内确认。只要没人提出异议，结果就被默认为正确（所以叫"乐观"）：任何验证者都可以提交**欺诈证明**（fraud proof），争议在以太坊上裁决。自2025年2月起，**BoLD**协议让任何人都能参与验证，只要有一个诚实的验证者就足以保护整条链。软件底层**Nitro**与以太坊应用兼容，**Orbit**计划则让其他项目可以用Arbitrum技术搭建自己的链。

## 代币有什么用

ARB主要是投票用的代币。持有人或他们选出的代表在**Arbitrum DAO**中投票，决定网络升级，以及如何使用DAO金库——金库里有数十亿枚ARB和排序器手续费收入。使用Arbitrum并不需要ARB：Gas费用ETH支付。因此，代币的价值取决于投票权以及DAO决定如何使用资金，而不是直接取决于网络的使用量。

## 最新数据

- 当前价格：{{price:arb}}
- 历史最高价：{{ath:arb}}（{{athd:arb}}），距高点{{fromath:arb}}
- 市值：{{mcap:arb}}（在加密货币中排名{{rank:arb}}）
- 12个月价格变化：{{chg1y:arb}}
- 每天10美元、坚持3年：投入{{dcainv:3}}，变成{{dca:arb:3}}（{{dcaroi:arb:3}}）

## 一路走来

Offchain Labs源于美国普林斯顿大学的研究。Arbitrum One于2021年8月底向公众开放，2022年8月的Nitro升级降低了手续费并提升了容量。2023年3月23日，ARB代币上线，并向用户进行了大规模空投。几天后，第一个提案AIP-1引发轩然大波，因为基金会在投票之前就已开始动用一笔7.5亿枚ARB的拨款；之后基金会把提案拆分，并让DAO获得更多控制权。ARB在2024年1月达到约2.39美元的高点。2024年3月16日，约11亿枚团队和投资者代币解锁，此后每月持续解锁。2025年BoLD上线，而价格在2025年至2026年间大幅下跌。

## 替代选择

Arbitrum与以太坊的其他二层网络竞争：[Optimism]({lang}/op/)以及基于其OP Stack的链，其中包括没有自己代币的Coinbase旗下Base；[ZKsync]({lang}/zk/)和[Starknet]({lang}/strk/)等零知识Rollup；还有[Mantle]({lang}/mnt/)和[POL (ex-MATIC)]({lang}/pol/)。[以太坊]({lang}/eth/)本身也是一种选择，因为它自身的升级让使用成本越来越低。

## 主要风险

- **新增供应：**团队和投资者的解锁仍在继续，DAO金库也持有全部ARB中的很大一部分。
- **中心化排序器：**交易顺序由一个运营方决定；一旦它宕机或作恶，用户只能依靠更慢的备用通道。
- **竞争：**Base和其他二层网络在争夺同一批用户、应用和手续费。
- **与使用量关联弱：**手续费用ETH支付，所以Arbitrum用得再多，也不会自动增加对ARB的需求。
- **监管：**关于代币、DAO及其背后公司的规则因国家而异，也可能改变。

## 对定投者意味着什么

ARB一生中的大部分时间都在从早期高点往下走，所以定投者在越来越低的价格上攒下了越来越多的代币——只有价格回升，这才有帮助。定期买入固定金额可以分散择时风险，但不能消除亏损风险。很多人只把这类代币当作储蓄中的一小部分。过去的表现不代表未来的收益。

*不构成投资建议。*

## 资料来源

- [A gentle introduction to Arbitrum（Arbitrum官方文档）](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO（Arbitrum Foundation）](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet（The Block，2025年2月12日）](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high（CoinGecko）](https://www.coingecko.com/en/coins/arbitrum)
