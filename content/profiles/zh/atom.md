---
title: Cosmos（ATOM）通俗解读：自2019年起的“区块链互联网”、IBC与Cosmos Hub
description: Cosmos通俗解读：Cosmos SDK和IBC如何连接区块链、ATOM有什么用、通胀、代币经济学之争、漫长下跌与主要风险。
date: 2026-11-24
kind: analysis
---
**Cosmos**是一套工具和一个网络，让人们可以搭建自己的区块链，并把它们连接起来，相互发送代币和消息——项目自称为“区块链互联网”。ATOM是Cosmos Hub的代币，Cosmos Hub是该网络的第一条链，于2019年3月上线。ATOM目前市值为{{mcap:atom}}（在加密货币中排名{{rank:atom}}）。

> **要点**
> - 包括Osmosis、dYdX、Injective、Celestia和Cronos在内的数百条区块链都是用免费的Cosmos SDK搭建的，但其中大多数并不需要ATOM。
> - 历史最高价为{{ath:atom}}（{{athd:atom}}）；当前价格距离该高点{{fromath:atom}}。
> - ATOM没有供应上限：每年都会为质押者新增代币，自2023年的一次投票以来，年通胀率为7%–10%。
> - 2025–2026年，Cosmos Labs开展了一项公开研究，重新设计ATOM的经济模型；截至2026年11月，尚未采用新模型。

## 它如何运作

Cosmos由三大组件构成。**Cosmos SDK**是一套免费工具包，用来搭建拥有自己规则和代币的区块链。**CometBFT**（原名Tendermint）是共识引擎，让一组验证者在几秒内就新区块达成一致。**IBC**即跨链通信协议（Inter-Blockchain Communication），于2021年启用，让彼此独立的链无需中心化的跨链桥运营方，就能相互传递代币和数据；它的第二版IBC Eureka于2025年推出，可以连接以太坊等Cosmos之外的网络。每条链保留自己的验证者和安全性——这一点不同于[波卡]({lang}/dot/)，后者的各条链共享同一套安全性。Cosmos Hub本身由180个质押ATOM的验证者运行。

## 代币有什么用

ATOM保障Cosmos Hub的安全：持有者把ATOM质押给验证者，获得新增的ATOM和手续费作为奖励。解除质押需要21天，作恶的验证者会被罚没部分质押。ATOM也是投票权——升级和社区资金池的使用都通过链上提案决定。它的弱点在于，其他Cosmos链使用各自的代币，因此生态的成功并不会自动带来对ATOM的需求。扩大ATOM作用的计划都没能成功：2022年11月，持有者否决了“ATOM 2.0”方案；从2023年起让Hub为小型链提供安全保障的Interchain Security（跨链安全），在最后一批相关链离开后，于2026年被移除。

## 最新数据

- 当前价格：{{price:atom}}
- 历史最高价：{{ath:atom}}（{{athd:atom}}），距高点{{fromath:atom}}
- 市值：{{mcap:atom}}（在加密货币中排名{{rank:atom}}）
- 12个月价格变化：{{chg1y:atom}}
- 每天10美元、坚持5年：投入{{dcainv:5}}，变成{{dca:atom:5}}（{{dcaroi:atom:5}}）

## 一路走来

Tendermint的创造者Jae Kwon与Ethan Buchman在2016年发布了Cosmos白皮书，2017年4月的代币发售募集了约1700万美元。Cosmos Hub于2019年3月13日上线，IBC在2021年启用。同年，ATOM在2021年9月涨到约44美元。2022年5月，用Cosmos SDK搭建的最大链之一Terra崩盘，重创整个生态。2023年11月，持有者投票把最高通胀率从20%降到10%。2025年，开发公司Interchain Labs更名为Cosmos Labs，Interchain Foundation（跨链基金会）开始与外部研究人员一起设计新的代币模型。ATOM持续下跌，并在2026年11月创下新低，较2021年高点下跌超过95%。

## 替代选择

在连接多条链这件事上，Cosmos最接近的对手是[波卡]({lang}/dot/)。作为应用开发平台，两者都与[以太坊]({lang}/eth/)及其二层网络竞争，也与[Solana]({lang}/sol/)、[Avalanche]({lang}/avax/)和[Sui]({lang}/sui/)等高速单链竞争。看好Cosmos技术的投资者，也可以关注用它搭建的链的代币，例如[Osmosis]({lang}/osmo/)、[Injective]({lang}/inj/)、[Celestia]({lang}/tia/)或[Cronos]({lang}/cro/)。

## 主要风险

- **大幅波动：** ATOM已从2021年高点下跌超过95%；即使技术一直有人在用，漫长的下跌也可能持续。
- **价值捕获薄弱：** Cosmos链不必使用ATOM或用ATOM付费，因此生态增长未必能让这个代币受益。
- **通胀：** 每年都有新的ATOM产生，不参与质押的持有者会被稀释。
- **治理与执行：** 代币模型正在重新设计，过去的大计划要么被否决、要么被放弃，结果难以预料。
- **竞争与监管：** 大多数用户被以太坊二层网络和高速单链吸引，而各国对代币和质押的规则也不同。

## 对定投者意味着什么

ATOM说明，被广泛使用的技术并不能保证代币价格上涨。定期定额买入意味着价格低时多买、价格高时少买，不必去猜底——但无法消除亏损的风险。很多人只把加密货币控制在储蓄中的一小部分，即便大跌也能承受。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Cosmos official site](https://cosmos.network/)
- [Cosmos (ATOM) review: tokenomics, staking and risks (Coin Bureau, September 2026)](https://coinbureau.com/review/cosmos-atom)
- [Cosmos powers the internet of blockchains. Can ATOM capture the value? (TipRanks, April 2026)](https://www.tipranks.com/news/cosmos-powers-the-internet-of-blockchains-can-atom-capture-the-value)
