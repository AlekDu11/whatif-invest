---
title: Kaspa（KAS）通俗解读：2021年起的工作量证明blockDAG、每秒10个区块、287亿枚上限
description: Kaspa通俗解读：blockDAG和GHOSTDAG如何运作、无预挖的公平启动、Crescendo和Toccata升级、发展历程与主要风险。
date: 2026-11-24
kind: analysis
---
**Kaspa**是一种工作量证明加密货币，像比特币一样靠挖矿产生，但设计得快得多：它不是只有一条区块链，而是使用"blockDAG"，可以同时加入许多区块。它于2021年11月启动，没有预挖，也没有代币销售，其币种**KAS**当前市值{{mcap:kas}}（在加密货币中排名{{rank:kas}}）。

> **要点**
> - KAS总量永远不会超过约287亿枚，截至2026年底已有约97%被挖出。
> - 历史最高价为{{ath:kas}}（{{athd:kas}}），当前价格距高点{{fromath:kas}}。
> - 自2025年5月的Crescendo升级以来，网络每秒产生10个区块，而此前只有1个。
> - Kaspa没有预挖、没有预售，也没有给创始人预留币——每一枚KAS都来自挖矿。

## 它如何运作

在比特币中，如果两个矿工同时找到区块，其中一个会被丢弃，所以出块必须很慢（大约每10分钟一个）。Kaspa保留所有这些并行区块，并把它们连接成一张图，也就是**blockDAG**（有向无环图）。随后，基于Yonatan Sompolinsky和Aviv Zohar学术研究的**GHOSTDAG**协议把所有区块和交易排成统一认可的顺序。这样Kaspa可以非常频繁地出块，几秒内确认付款，同时保留比特币式的挖矿，使用自己的kHeavyHash算法。发行量平滑减少：挖矿奖励每月略降一点，大约每年减半一次。

## 人们为什么认为它有价值

支持者把Kaspa看作"快速的数字白银"：它保留了比特币受欢迎的特点——工作量证明、固定供应、没有公司、没有预先分配的币——但付款在几秒而不是几分钟内完成。公平启动对很多持有者很重要，因为没有任何团队或基金拿到便宜的币留待日后抛售。2026年网络还开始具备可编程性：Toccata升级带来了契约（规定币如何被花费的规则）、零知识证明验证和原生代币，开发者有望在Kaspa上构建应用。

## 最新数据

- 当前价格：{{price:kas}}
- 历史最高价：{{ath:kas}}（{{athd:kas}}），距高点{{fromath:kas}}
- 市值：{{mcap:kas}}（在加密货币中排名{{rank:kas}}）
- 12个月价格变化：{{chg1y:kas}}
- 每天10美元、坚持3年：投入{{dcainv:3}}，变成{{dca:kas:3}}（{{dcaroi:kas:3}}）

## 一路走来

Kaspa诞生于学术研究和DAGlabs公司，主网于2021年11月7日上线。第一年它只在小型交易所以不到一美分的价格交易。2023年较大的交易所上线后，价格上涨了许多倍，并在2024年年中创下约0.21美元的历史高点。开发者用Rust重写了节点软件（"Rusty Kaspa"），使速度的飞跃成为可能：2025年5月5日，Crescendo硬分叉把网络从每秒1个区块提升到10个。2025至2026年价格大幅下跌，2026年Toccata硬分叉让Kaspa成为可编程的第一层网络。

## 替代选择

Kaspa最直接的竞争对手是其他工作量证明支付币，如[比特币]({lang}/btc/)、[莱特币]({lang}/ltc/)和[比特币现金]({lang}/bch/)。对于快速、便宜的转账和应用，人们也会使用[Solana]({lang}/sol/)等权益证明网络；日常支付方面，很多人干脆使用美元稳定币。

## 主要风险

- **大幅波动：** KAS曾从2024年的高点下跌超过80%，类似跌幅可能再次出现。
- **挖矿集中：** 少数大型矿池和ASIC矿机厂商掌握着大部分算力。
- **团队规模小：** 开发依靠一小群核心开发者，资金主要来自社区捐赠，而不是大公司。
- **实际使用：** 速度本身不会带来需求，Toccata上的应用和真实支付还有待普及。
- **市场准入：** 大部分交易发生在中型交易所，各国对加密货币的规则也可能变化。

## 对定投者意味着什么

Kaspa是一种历史较短、涨跌非常剧烈的币。定期买入固定金额，可以把买入价格分摊到好月份和坏月份，但无法避免长期下跌。大部分KAS已经被挖出，因此未来价格主要取决于需求。很多人只把这类币控制在加密资产中很小的比例。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Kaspa — official website (kaspa.org)](https://kaspa.org/)
- [PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus — Sompolinsky, Wyborski, Zohar (IACR ePrint 2018/104)](https://eprint.iacr.org/2018/104.pdf)
- [Kaspa Covenants++ «Toccata» hard-fork outlook — Michael Sutton, Kaspa core developer (Medium)](https://medium.com/@michaelsuttonil/kaspa-covenants-toccata-hard-fork-outlook-a4d81a40900c)
- [Kaspa price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/kaspa)
