---
title: Celestia（TIA）通俗解读：为Rollup服务的数据网络、2023年起运行、启动时10亿枚
description: Celestia通俗解读：数据可用性层如何运作、TIA有什么用、两次削减增发、一路走来、竞争对手、主要风险以及给定投者的提示。
date: 2026-11-24
kind: analysis
---
**Celestia**是一条只做一件事的区块链：保存并公开其他区块链（主要是"Rollup"）的交易数据，让任何人都能核查。它于2023年10月上线，是这一类"模块化"网络中的第一个，其代币TIA的总市值为{{mcap:tia}}（在加密货币中排名{{rank:tia}}）。关注它的人押注的是：未来许多区块链会租用这项服务，而不是自己搭建一层。

> **要点**
> - Celestia不运行应用或智能合约——它只保证数据已经公开，并以TIA出售这部分空间。
> - 启动时共有10亿枚TIA；没有固定上限，但年增发率在2025年7月从约7.2%降到约5%，在2025年11月又降到约2.5%。
> - 历史最高价为{{ath:tia}}（{{athd:tia}}），当前价格距高点{{fromath:tia}}。
> - 自2024年10月开始的早期投资者和团队代币大规模解锁，对价格造成了沉重压力。

## 它如何运作

Rollup是自行处理交易、再把压缩后的记录发布到另一条链上的网络，而Celestia就是发布这些记录的地方。Rollup付费把数据"blob"放进Celestia的区块，网络则确保这些数据真的存在。它的关键技术是数据可用性采样：在普通手机或笔记本上运行的轻节点，随机下载区块中的几小块数据，如果都能取到，就几乎可以确定整个区块已经公开。Celestia基于Cosmos SDK构建，采用权益证明（PoS）保障安全。2025年底的Matcha升级把最大区块从8MB提高到128MB。

## 代币有什么用

TIA有三种用途。Rollup和应用用TIA支付所占用blob空间的费用；持有者把TIA质押给负责出块的验证者，获得新增发的代币作为奖励；TIA持有者还能就网络变更投票，比如那两次削减增发。因此，代币需求取决于到底有多少Rollup选择Celestia、发布多少数据。

## 最新数据

- 当前价格：{{price:tia}}
- 历史最高价：{{ath:tia}}（{{athd:tia}}），距高点{{fromath:tia}}
- 市值：{{mcap:tia}}（在加密货币中排名{{rank:tia}}）
- 12个月价格变化：{{chg1y:tia}}
- 每天10美元、坚持3年：投入{{dcainv:3}}，变成{{dca:tia:3}}（{{dcaroi:tia:3}}）

## 一路走来

这个想法起源于2019年Mustafa Al-Bassam发表的研究论文LazyLedger，项目于2021年更名为Celestia。2023年10月31日主网Beta上线，同时向开发者和用户进行了大规模TIA空投。在2024年的加密市场上涨中，价格于2024年2月涨到约20美元。从2024年10月起，早期支持者的大额解锁开始，到2025年6月TIA跌到约1.32美元，跌幅约93%，2026年继续下滑。联合创始人Mustafa Al-Bassam当时表示，项目有1亿美元资金储备，足够运营六年。Lotus（2025年7月）和Matcha（2025年11月）升级逐步降低了增发率，长期目标是每年1.5%。

## 替代选择

Celestia最大的对手就是[以太坊]({lang}/eth/)本身：自2024年3月起，以太坊为Rollup提供了自己更便宜的"blob"空间。其他数据可用性网络包括[Avail]({lang}/avail/)、[EigenCloud]({lang}/eigen/)的EigenDA以及[NEAR]({lang}/near/)的数据层。[Arbitrum]({lang}/arb/)和[Optimism]({lang}/op/)等许多Rollup仍把数据发布在以太坊上。

## 主要风险

- **竞争：** 以太坊blob、Avail和EigenDA争夺同一批客户，费用因此一直很低。
- **手续费收入少：** 到目前为止，Rollup支付的费用与网络价值相比很小。
- **供应增长：** 没有固定上限，新的TIA持续发放给质押者。
- **解锁与集中：** 早期投资者、团队和基金会持有大量份额，他们的抛售可能推动价格。
- **剧烈波动：** TIA在约16个月内从2024年高点下跌超过90%。

## 对定投者意味着什么

TIA短暂的历史，大部分是早期高点之后的长期下跌，中间夹杂着几次急速反弹。定期定额买入能把成本分摊到不同时间点，但如果网络始终没有被广泛采用，它并不能帮你避免亏损；对于一个年轻的代币，三年的历史几乎说明不了未来三年。很多人只把这类币放在储蓄中很小的一部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [质押、治理与供应（Celestia官方文档）](https://docs.celestia.org/learn/TIA/staking-governance-supply/)
- [Matcha升级介绍：迈向128MB区块（Celestia博客）](https://blog.celestia.org/matcha/)
- [Celestia联合创始人称拥有1亿美元资金储备（The Block，2025年6月）](https://www.theblock.co/post/359387/celestia-co-founder-cites-100-million-war-chest-and-six-year-runway-to-play-the-long-game-as-native-token-drops-over-90-from-peak)
