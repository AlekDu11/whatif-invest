---
title: Lighter（LIT）通俗解读：以太坊zk-rollup上的零手续费永续合约，以及什么在推动代币价格
description: 用大白话看Lighter：运行在自有以太坊zk-rollup上的永续合约交易所，散户零手续费，LIT代币的作用与主要风险。
date: 2026-11-25
kind: analysis
---
**Lighter**是一家去中心化的永续合约交易所。永续合约可以让你用杠杆押注比特币、以太币等资产的价格涨跌。Lighter运行在以太坊之上自建的zk-rollup上，普通交易者不付交易手续费，每一次订单撮合都用零知识证明来验证。它的代币**LIT**于2025年12月30日推出，当前市值{{mcap:lit}}（在加密货币中排名{{rank:lit}}）。

> **要点**
> - LIT总量为10亿枚；50%分配给生态，其中25%在2025年12月空投给早期用户。
> - 历史最高价为{{ath:lit}}（{{athd:lit}}）；当前价格距离该高点{{fromath:lit}}。
> - 团队（26%）和投资者（24%）的代币在上线后锁定一年，之后分三年逐步解锁。
> - 散户通过网站和App交易免费；手续费由使用API和高频交易的专业交易者支付。

## 它如何运作

Lighter是以太坊的二层网络（Layer 2）。交易在Lighter自己的高速订单簿里完成，专门设计的零知识电路证明订单是按价格和时间优先原则公平撮合的，清算、资金费率支付和风险检查也都按规则执行。用户资金存放在以太坊智能合约中，只有证明在以太坊上通过验证后，网络状态才会更新。如果运营方停摆或审查用户，用户可以直接向以太坊提交请求，或通过名为"Desert Mode"的紧急通道撤出资金。

## 它怎么赚钱，LIT有什么用

Lighter的商业模式很特别：通过界面交易的人一分钱不付，而通过API和高频交易进来的订单流，也就是做市商和交易公司，要支付"高级"手续费。团队表示，交易所及未来产品的收入都可以在链上查看，并会根据市场情况用于业务增长和回购LIT；手续费和回购可以在Lighter区块浏览器的金库账户中追踪。

LIT由Lighter的美国公司发行。2026年1月，质押成为它的第一个重要用途：要向Lighter流动性池（LLP）存款——该池能产生收益，并在清算时充当保险基金——每10 USDC需要质押1枚LIT。质押至少100枚LIT的用户免收提现和转账手续费，质押还能抵扣高级手续费。团队还计划把交易和公平性验证基础设施与LIT质押挂钩。

## 最新数据

- 当前价格：{{price:lit}}
- 历史最高价：{{ath:lit}}（{{athd:lit}}），距高点{{fromath:lit}}
- 市值：{{mcap:lit}}（在加密货币中排名{{rank:lit}}）
- 总供应量：10亿枚LIT（生态50%、团队26%、投资者24%）

## 一路走来

Lighter由弗拉基米尔·诺瓦科夫斯基（Vladimir Novakovski）于2022年创立，他16岁进入哈佛，18岁开始在城堡投资（Citadel）工作。项目脱胎于他在2017年联合创办的AI社交网络应用Lunchclub，原团队大部分转到了Lighter。2024年，Lighter在Haun Ventures和Craft Ventures领投的一轮中融资2100万美元。经过约八个月、约18.8万个账户参与的封闭测试后，公开主网于2025年10月上线。

增长非常迅速：2025年11月中旬，周交易量达到749亿美元的峰值；Lighter公布2025年11月交易量为2925亿美元，超过Aster和Hyperliquid。同月，它在Founders Fund和Ribbit Capital领投、Haun Ventures和Robinhood参投的一轮中融资6800万美元，据报道估值约15亿美元。2025年12月初，平台增加了现货交易。

LIT于2025年12月30日开始交易；面向2025年前两季积分持有者的空投当时价值约6.75亿美元。2026年1月初，金库账户开始累积LIT，市场将其解读为回购；2026年1月14日，平台宣布向LLP存款必须质押LIT。空投结束后，大量刷积分的用户离开：到2026年1月中旬，周交易量降至约253亿美元，约为峰值的三分之一，Hyperliquid重回第一。

## 替代选择

最大的对手是[Hyperliquid]({lang}/hype/)，它运行在自己的一层区块链上而不是以太坊上，并有代币HYPE。[Aster]({lang}/aster/)在2025年底与Lighter争夺交易量第一，[dYdX]({lang}/dydx/)则是最早的去中心化永续合约交易所之一。目前大部分加密期货交易仍发生在币安、OKX等大型中心化交易所。

## 主要风险

- **奖励驱动的交易量：** 2025年的大量活跃来自空投前刷积分；空投后几周内交易量缩水约三分之二。
- **代币解锁：** 一半供应量属于团队和投资者；锁定一年后分三年解锁，可能带来抛压。
- **竞争：** Hyperliquid、Aster和中心化交易所争夺同一批交易者，而零手续费很容易被模仿。
- **技术：** 拥有自建订单簿和证明系统的新zk-rollup，即使有以太坊退出通道，也可能出现漏洞或故障。
- **监管：** 杠杆衍生品在许多国家受到严格监管，针对去中心化交易所的规则也可能改变。
- **剧烈波动：** LIT是新代币，上线后的大幅下跌本身就是它历史的一部分。

## 对定投者意味着什么

LIT上线交易还不到一年，所以还没有长期的"每天10美元"记录可看——任何结果都只覆盖一段很短、波动极大的时期。定期定额买入能把买入价格分散到不同时间，而不是押注某一个时点，但并不能消除亏损风险，尤其是面对一个新代币和即将到来的解锁。如果要买，很多人只把这类代币控制在储蓄中很小的一部分，即使大跌也承受得起。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Lighter launches native token LIT, allocates half to ecosystem growth（The Block，2025年12月30日）](https://www.theblock.co/post/383940/lighter-native-token-lit)
- [Lighter introduces mandatory LIT staking for liquidity pool access（The Block，2026年1月14日）](https://www.theblock.co/post/385696/lighter-lit-staking)
- [Lighter opens public mainnet with Ethereum-settled zk perps（Blockworks）](https://blockworks.co/news/lighter-opens-public-mainnet)
- [DeFi founder who graduated Harvard at 18 raises $68 million for crypto trading protocol Lighter（Fortune，2025年11月11日）](https://fortune.com/2025/11/11/lighter-fundraise-founders-fund-ribbit-capital-haun-ventures-robinhood-vladimir-novakovski/)
- [Trading volume on Lighter plummets threefold after airdrop（ForkLog，2026年1月19日）](https://forklog.com/en/news/trading-volume-on-lighter-exchange-plummets-threefold-after-airdrop)
- [Lighter价格、市值与历史最高价（CoinGecko）](https://www.coingecko.com/en/coins/lighter)
