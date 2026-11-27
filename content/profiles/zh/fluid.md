---
title: Fluid（FLUID）通俗解读：Instadapp的借贷与交易协议、1亿枚上限
description: 用大白话看Fluid：借贷与交易共享的流动性层如何运作、智能抵押与智能债务、从INST更名、竞争对手和风险。
date: 2026-11-27
kind: analysis
---
**Fluid**是一个去中心化金融（DeFi）协议，人们可以在同一个共享资金池里借出、借入和兑换加密货币。它由以太坊上最老牌的DeFi应用之一Instadapp的团队打造，2025年初，原来的INST代币更名为FLUID。当前市值{{mcap:fluid}}（在加密货币中排名{{rank:fluid}}）。

> **要点**
> - FLUID代币总量为1亿枚；从INST更名时，供应量和代币地址都保持不变。
> - 历史最高价是在INST时期创下的{{ath:fluid}}（{{athd:fluid}}）；当前价格距离该高点{{fromath:fluid}}。
> - 在Fluid上，同一笔存款可以同时发挥两种作用——既是借款抵押品，又是交易流动性——因此用户能同时赚取借贷和交易手续费。
> - 2024年12月，上线仅三周，它的交易所就处理了超过10亿美元的交易。

## 它如何运作

大多数DeFi应用把借贷和交易放在不同的资金池里。Fluid把所有存款放进一个"流动性层"，货币市场、金库（vault）和去中心化交易所（DEX）等不同应用都从中调用资金。借助"智能抵押"，你为借款抵押的币同时会作为DEX上的交易流动性，赚取兑换手续费。借助"智能债务"，你借来的资金也会被用作流动性，交易手续费可以抵掉一部分利息。一切都由智能合约（运行在区块链上的程序）执行，主要在以太坊上，也支持Arbitrum和Base等二层网络。2025年，Solana上的交易所Jupiter推出了基于Fluid技术的借贷应用Jupiter Lend。

## 代币有什么用

FLUID是治理代币：持有者对手续费、新市场以及金库资金的使用进行投票。2024年12月的更名提案还计划，在协议年收入达到约1000万美元后回购代币，让Fluid赚到的部分手续费回流到代币上。FLUID不派发分红，它的价值取决于协议能赚多少钱，以及其中有多少能落到持有者手里。

## 最新数据

- 当前价格：{{price:fluid}}
- 历史最高价：{{ath:fluid}}（{{athd:fluid}}），距高点{{fromath:fluid}}
- 市值：{{mcap:fluid}}（在加密货币中排名{{rank:fluid}}）
- 12个月价格变化：{{chg1y:fluid}}
- 每天10美元、坚持1年：投入{{dcainv:1}}，变成{{dca:fluid:1}}（{{dcaroi:fluid:1}}）

## 一路走来

Instadapp由Sowmay Jain和Samyak Jain兄弟于2018年创立，最初是一个能同时使用多个DeFi应用的简单控制面板。它的治理代币INST在DeFi热潮最高峰的2021年6月推出，当月涨到约24美元，随后到2022年底下跌超过95%。经过约两年的开发，团队在2024年推出了Fluid的借贷协议，并在2024年11月推出DEX，后者很快就成为以太坊上交易量最大的交易所之一。之后，持有者批准将INST按1:1转换为FLUID，代币从2025年起以FLUID的名义交易，价格大多在约1.50美元到6美元之间。

## 替代选择

[Aave]({lang}/aave/)是最大的DeFi借贷协议，[Morpho]({lang}/morpho/)是快速成长的竞争对手。在交易方面，Fluid的DEX与[Uniswap]({lang}/uni/)和[Curve DAO]({lang}/crv/)竞争。在Solana上，[Jupiter]({lang}/jup/)既是合作伙伴，也是竞争对手。

## 主要风险

- **大幅波动：** 这枚代币曾经跌掉超过95%的价值；DeFi代币在熊市中可能快速下跌。
- **智能合约风险：** 共享流动性层一旦出现漏洞或遭到黑客攻击，借贷和交易可能同时受到冲击。
- **清算：** 用波动大的币作抵押的借款在价格下跌时会被自动卖出，在暴跌中可能引发连锁反应。
- **持有者能获得的价值：** 回购取决于收入目标和治理投票，手续费可能无法如预期那样回流到代币。
- **集中与监管：** 团队和早期投资者持有很大比例，而许多国家的DeFi规则仍在制定中。

## 对定投者意味着什么

以FLUID的身份来看，这枚代币的历史很短，2025年以来的定期买入大多发生在价格下跌的过程中。定期投入固定金额可以分散择时风险，但结果仍取决于协议能否持续增加手续费收入。很多人只把储蓄中很小、即使大跌也能承受的一部分用来买DeFi代币。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Fluid官方网站与文档（fluid.io）](https://fluid.io/)
- [Instadapp proposes rebrand and new tokenomics following Fluid launch（The Defiant，2024年12月4日）](https://thedefiant.io/news/defi/instadapp-proposes-rebrand-and-new-tokenomics-following-fluid-launch)
- [DeFi superapp Fluid is coming for Aave and Uniswap's lunch（Blockworks）](https://blockworks.co/news/defi-superapp-competitor-to-aave-uniswap)
- [Fluid价格、市值与历史最高价（CoinGecko）](https://www.coingecko.com/en/coins/instadapp)
