---
title: EigenCloud（EIGEN）通俗解读：以太坊再质押、2024年质押空投与a16z的7000万美元押注
description: EigenCloud（原EigenLayer）通俗解读：再质押如何运作、EIGEN有什么用、罚没机制、a16z交易、竞争对手、主要风险以及定投的意义。
date: 2026-11-28
kind: analysis
---
**EigenCloud**（2025年6月前名为**EigenLayer**）是以太坊上的一个项目，让人们可以“再质押”（restaking）：把已经用于保护以太坊的ETH再用一次，同时保护其他服务，换取额外奖励。它由总部位于美国西雅图的Eigen Labs开发，首席执行官是华盛顿大学前教授Sreeram Kannan。EIGEN是该项目的代币，目前市值为{{mcap:eigen}}（在加密货币中{{rank:eigen}}）。

> **要点**
> - 再质押于2023年在以太坊上线，2024年6月存入资金一度超过200亿美元，达到顶峰。
> - EIGEN的历史最高价为{{ath:eigen}}（{{athd:eigen}}），当前价格较其{{fromath:eigen}}。
> - EIGEN在2024年通过“质押空投”（stakedrop）发给早期用户，直到2024年9月30日才可以转账。
> - 2025年6月项目更名为EigenCloud重新出发时，a16z crypto又买入了价值7000万美元的EIGEN。

## 它如何运作

质押者把ETH或Lido的stETH等流动性质押代币存入EigenLayer的智能合约，并委托给运营商——为外部服务运行软件的公司。这些“主动验证服务”（AVS），例如为Rollup提供的数据存储（EigenDA）、价格预言机和跨链桥，会为安全性向运营商和质押者付费。运营商一旦违反某项服务的规则，部分再质押的资金可能被罚没（slashing）；罚没机制于2025年4月在主网上线，各项服务的惩罚彼此隔离。2025年6月项目更名为EigenCloud，成为一个“可验证”应用平台，把EigenDA与用于运行代码的EigenCompute、用于解决争议的EigenVerify结合在一起。

## 代币有什么用

再质押者锁定的是ETH，而不是EIGEN，所以EIGEN另有用途。它被质押用来防范仅靠代码无法证明的错误，比如预言机报出假价格：这时EIGEN持有者可以把代币分叉，让作恶者蒙受损失——EigenVerify正依赖这一机制。EIGEN也作为奖励发给质押者和运营商。初始供应约16.7亿枚，并通过每年的激励增发持续增加，团队和投资人的份额则在数年内逐步解锁。

## 最新数据

- 当前价格：{{price:eigen}}
- 历史最高价：{{ath:eigen}}（{{athd:eigen}}），距高点{{fromath:eigen}}
- 市值：{{mcap:eigen}}（在加密货币中排名{{rank:eigen}}）
- 12个月价格变化：{{chg1y:eigen}}
- 每天10美元、坚持2年：投入{{dcainv:2}}，变成{{dca:eigen:2}}（{{dcaroi:eigen:2}}）

## 一路走来

2023年3月，Eigen Labs完成由Blockchain Capital领投的5000万美元A轮融资，同年再质押在以太坊主网开放。为了积分和未来的空投，用户蜂拥而至；2024年2月，a16z crypto领投了1亿美元的B轮。2024年团队宣布EIGEN质押空投：起初代币无法转移，美国等部分国家的用户被排除在外，因而受到批评。EIGEN于2024年9月30日开放转账，并在当年12月创下历史最高价。存入资金从2024年中的高点回落，到2025年6月约为120亿美元；当时a16z又买入7000万美元的EIGEN，项目也更名为EigenCloud。2025年7月，Eigen Labs裁员约25%，以集中精力发展EigenCloud。

## 替代选择

最简单的替代方式是直接在[以太坊]({lang}/eth/)上普通质押，或通过[Lido DAO]({lang}/ldo/)做流动性质押。[ether.fi]({lang}/ethfi/)提供建立在EigenLayer之上的流动性再质押。与之竞争的再质押协议还有Symbiotic和Karak，它们接受的资产种类更多。

## 主要风险

- **价格大起大落：** EIGEN远低于2024年12月的最高价，年轻的代币还可能继续下跌。
- **风险层层叠加：** 再质押的ETH既有以太坊本身的质押风险，又叠加智能合约漏洞和额外服务带来的罚没风险。
- **真实需求：** 奖励取决于各项服务是否愿意为安全付费；付得少，再质押就失去吸引力。
- **供应：** 每年的激励增发以及团队和早期投资人的解锁，会把新代币带入市场。
- **竞争和监管：** 竞争协议在争夺同一批存款，而各国对质押和代币的规定各不相同。

## 对定投者意味着什么

EIGEN自2024年秋季开始交易以来大多在下跌，所以到目前为止定投的人大多是在价格下行时买入。按计划定期投入固定金额可以分散选错时机的风险，但并不能让一枚下跌的代币变得赚钱；结果取决于EigenCloud的服务能否赢得付费客户。很多人只把这类代币控制在储蓄中即使大跌也能承受的一小部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [a16z crypto invests $70 million in direct EigenLayer token deal to back EigenCloud (The Block, 17 June 2025)](https://www.theblock.co/news/deals/2025-06-17-a16z-crypto-eigen-token-eigencloud-358511)
- [EigenLayer gets $70M from a16z to launch off-chain verifiability platform (Decrypt, 17 June 2025)](https://decrypt.co/325503/eigenlayer-70m-a16z-verifiability-platform)
- [Eigen Labs lays off 25% of workforce to focus on EigenCloud (The Block, 9 July 2025)](https://www.theblock.co/news/business/2025-07-09-eigen-layoffs-361731)
- [EigenCloud (EIGEN) — CoinGecko](https://www.coingecko.com/en/coins/eigenlayer)
