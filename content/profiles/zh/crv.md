---
title: Curve DAO（CRV）通俗解读：稳定币交易所、veCRV锁仓与30亿枚总量上限
description: 用大白话看Curve：稳定币交易所和crvUSD如何运作、为什么要把CRV锁成veCRV、Curve战争、黑客事件、竞争对手、主要风险，以及定投须知。
date: 2026-11-24
kind: analysis
---
**Curve Finance**是一个去中心化交易所，专为兑换价值应当大致相同的币而设计——主要是USDT、USDC、DAI等美元稳定币，也包括不同版本的ETH或比特币。它于2020年上线，由迈克尔·叶戈罗夫（Michael Egorov）创建，运行在以太坊和许多其他链上。**CRV**是它的治理代币，总市值{{mcap:crv}}（在加密货币中排名{{rank:crv}}）。

> **要点**
> - CRV总供应量上限约为30.3亿枚；新代币发放给流动性提供者，年发行量逐步递减。
> - 历史最高价为{{ath:crv}}（{{athd:crv}}），出现在2020年8月刚开始交易的头几天；当前价格距离该高点{{fromath:crv}}。
> - 人们把CRV锁定为veCRV，最长四年，用来投票并分享协议的手续费收入。
> - Curve还发行自己的美元稳定币crvUSD，于2023年推出。

## 它如何运作

Curve不用订单簿，而是用资金池：用户存入两种或多种币，交易者与资金池进行兑换。当池中各币价值几乎相同时，它的公式能把价格维持得非常紧，所以即使大额把USDC换成USDT，成本也很低。存入币的人可以赚取交易手续费和CRV奖励。crvUSD是以加密资产为抵押铸造的稳定币；它不采用突然清算，而是用"软清算"机制，在价格下跌时逐步转换抵押品。许多其他DeFi应用都在幕后使用Curve的资金池和借贷市场。

## CRV代币有什么用

CRV的主要用途要在锁定为**veCRV**（"投票托管CRV"）后才体现出来。锁得越久——最长四年——投票权就越大。veCRV持有者可以就升级以及哪些资金池获得最多CRV奖励进行投票，分得一部分交易手续费和crvUSD利息，还能提高自己的奖励。由于决定奖励流向很有价值，其他项目会争相购买或"贿选"veCRV的投票权——这就是所谓的"Curve战争"。

## 最新数据

- 当前价格：{{price:crv}}
- 历史最高价：{{ath:crv}}（{{athd:crv}}），距高点{{fromath:crv}}
- 市值：{{mcap:crv}}（在加密货币中排名{{rank:crv}}）
- 12个月价格变化：{{chg1y:crv}}
- 每天10美元、坚持5年：投入{{dcainv:5}}，变成{{dca:crv:5}}（{{dcaroi:crv:5}}）

## 一路走来

Curve于2020年1月起步，CRV代币于2020年8月上线；在头几天的炒作中，价格一度短暂冲上15美元以上，随后迅速回落。2021年，Curve战争使它成为最重要的DeFi协议之一，Convex等协议聚集了大量veCRV。2023年5月，crvUSD推出。2023年7月，攻击者利用Vyper编程语言的一个漏洞，从多个资金池盗走约7000万美元，其中一部分后来被归还。2024年6月，创始人以CRV为抵押借入的大额贷款遭到清算，导致价格大跌。2025年，DAO批准向Yield Basis提供6000万美元的crvUSD信贷额度，这是叶戈罗夫基于Curve资金池打造的新协议。

## 替代选择

[Uniswap]({lang}/uni/)是最大的通用型去中心化交易所，也承担了大量稳定币交易。[Balancer]({lang}/bal/)提供类似的多币资金池；在借贷和稳定币领域，Curve的对手是[Aave]({lang}/aave/)以及发行USDS和DAI的[Sky]({lang}/sky/)（原Maker）。对大多数人来说，简单兑换稳定币的主要场所仍是中心化交易所。

## 主要风险

- **大幅波动：** CRV较2020年高点已下跌超过90%；危机中DeFi代币可能迅速下跌。
- **智能合约风险：** 2023年的漏洞攻击表明，哪怕是编程语言里的一个漏洞，也可能让资金被盗。
- **集中：** 少数协议和大户掌握了大部分veCRV投票权，创始人自己的仓位也已经影响过一次价格。
- **供应：** 新的CRV作为奖励不断进入市场，很多拿到奖励的人会卖出。
- **监管：** 美国、欧盟等地针对DeFi交易所和稳定币的规则正在变化，可能限制使用。

## 对定投者意味着什么

Curve是一个运行多年、使用广泛的协议，但它的代币走势自2020年以来大体是一路向下。定期投入固定金额可以把买入时点分散开，不用猜底部也能在价格低时买得更多——但这并不能消除亏损的风险。很多人只把储蓄中很小的一部分放进DeFi代币。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Curve Finance——官方网站与文档（curve.finance）](https://curve.finance/)
- [Curve技术文档：CRV、veCRV与crvUSD（docs.curve.finance）](https://docs.curve.finance/)
- [Yield Basis clears Curve DAO vote hurdle (Blockworks)](https://blockworks.co/news/yield-basis-curve-dao-vote)
- [Curve DAO Token price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/curve-dao-token)
