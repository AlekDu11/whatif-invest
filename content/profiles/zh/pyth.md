---
title: Pyth Network（PYTH）通俗解读：服务100多条区块链的价格预言机、100亿枚上限、2021年起运行
description: Pyth Network通俗解读：价格如何上链、PYTH有什么用、解锁时间表、发展历程、主要风险，以及定投者需要了解的内容。
date: 2026-11-24
kind: analysis
---
**Pyth Network**是一种"预言机"：把加密货币、股票、外汇、大宗商品等真实市场价格送上区块链的服务，让借贷应用、交易所和其他智能合约知道东西值多少钱。这些价格不是从网站抓取的，而是直接来自交易所和交易公司。它于2021年在Solana上线，如今服务100多条区块链，PYTH代币总市值为{{mcap:pyth}}（在加密货币中排名{{rank:pyth}}）。

> **要点**
> - Pyth把来自交易所、做市商、交易公司等一手来源的价格，发送到100多条区块链。
> - PYTH永远不会超过100亿枚；85%在发行时被锁定，到2027年5月前每年解锁一次，共分四批。
> - 2025年8月，美国商务部选择Pyth与Chainlink一起，在链上发布官方GDP数据。
> - 历史最高价为{{ath:pyth}}（{{athd:pyth}}），当前价格距高点{{fromath:pyth}}。

## 它如何运作

数据"发布者"每秒多次把自己的报价发送到Pyth的专用网络。Pyth将它们合成一个价格，并附上置信区间，显示各来源之间分歧有多大。Pyth不会持续把每个价格写到每条链上，而是采用"拉取"模式：应用只在需要时取用最新的签名价格，并支付一小笔费用。这样成本低，同一份数据也能同时送达许多条链。

## 代币有什么用

PYTH主要是治理和安全代币。质押PYTH的持有者在Pyth DAO中就费用、奖励和新的价格源投票。通过"Oracle Integrity Staking"，他们还可以把PYTH质押在特定发布者身后：数据好可获得奖励，数据差可能受罚。自2025年底起，Pyth Pro以订阅方式向银行和交易公司出售高级市场数据；2025年12月，DAO推出了"PYTH Reserve"，每月动用由网络收入充实的金库的三分之一，在市场上买入PYTH。

## 最新数据

- 当前价格：{{price:pyth}}
- 历史最高价：{{ath:pyth}}（{{athd:pyth}}），距高点{{fromath:pyth}}
- 市值：{{mcap:pyth}}（在加密货币中排名{{rank:pyth}}）
- 12个月价格变化：{{chg1y:pyth}}
- 每天10美元、坚持1年：投入{{dcainv:1}}，变成{{dca:pyth:1}}（{{dcaroi:pyth:1}}）

## 一路走来

Pyth于2021年在Solana上起步，背后是一批交易公司和交易所，Jump Crypto是早期贡献者之一。PYTH代币于2023年11月发行，并向使用Pyth数据的应用用户空投。价格在2024年3月见顶，约1.20美元，此后两年大部分时间都在下跌，2024年5月和2025年5月的大规模解锁增加了供应。2025年8月28日，美国GDP数据上链的消息让PYTH一天内上涨超过70%。2025年9月推出Pyth Pro，2025年12月推出回购储备。

## 替代选择

最大的对手遥遥领先：[Chainlink]({lang}/link/)，最老牌、使用最广的预言机。其他还有[RedStone]({lang}/red/)、[API3]({lang}/api3/)和[Band]({lang}/band/)。在传统金融领域，Pyth Pro还与彭博（Bloomberg）、伦交所集团（LSEG）等老牌数据商竞争。

## 主要风险

- **代币解锁：**最后一次大规模解锁定于2027年5月，新增供应此前就曾压制价格。
- **竞争：**Chainlink在预言机领域占主导，许多应用会同时使用多家服务商。
- **数据故障：**错误或延迟的价格可能引发不公平的清算，损害信任。
- **使用量与价格关联弱：**网络在增长，代币却可能下跌；回购规模相对代币价值很小。
- **集中度与监管：**早期投资者和内部人士持有大量代币，加密货币和市场数据的规则也可能变化。

## 对定投者意味着什么

PYTH是一个年轻的代币，价格历史短，而且大多在下跌。定期买入固定金额可以分散买入价格，但无法消除未来解锁带来的压力，也无法消除代币继续贬值的风险。很多人只把这类代币控制在储蓄的一小部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [Understanding the PYTH tokenomics (Pyth Network)](https://www.pyth.network/blog/understanding-the-pyth-tokenomics)
- [Pyth launches token buyback program, allocating 33% of DAO treasury to monthly PYTH purchases (The Block, 12 December 2025)](https://www.theblock.co/news/business/2025-12-12-pyth-token-buyback-program-33-dao-treasury-monthly-pyth-purchases-382357)
- [Pyth Network token surges after US Commerce Department puts data onchain (Cointelegraph, 28 August 2025)](https://cointelegraph.com/news/pyth-network-token-surges-us-commerce-onchain-data)
- [Pyth Network price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/pyth-network)
