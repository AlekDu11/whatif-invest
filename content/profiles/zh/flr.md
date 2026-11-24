---
title: Flare（FLR）通俗解读：1000亿枚代币、2023年向XRP持有者空投，以及FXRP
description: 用大白话看Flare：内置价格预言机的数据区块链、让XRP进入DeFi的FXRP、2023年空投、供应量、风险，以及买家需要了解的事。
date: 2026-11-24
kind: analysis
---
**Flare**是一条为数据而生的区块链：它为应用提供来自其他区块链和互联网的可靠价格与信息，让XRP这类没有自己智能合约的币也能在DeFi中使用。它的代币FLR于2023年1月9日通过向XRP持有者空投进入市场，当前网络市值{{mcap:flr}}（在加密货币中排名{{rank:flr}}）。人们买FLR，主要是押注Flare会成为XRP及其他没有智能合约的币赚取收益的主要场所。

> **要点**
> - Flare初始发行1000亿枚FLR，其中15%（42.8亿枚）于2023年1月9日空投给XRP持有者。
> - 历史最高价为{{ath:flr}}（{{athd:flr}}）；当前价格距离该高点{{fromath:flr}}。
> - 2025年9月推出的FXRP以真实XRP一比一支撑，让XRP可以在Flare上的应用中使用。
> - 每月发放的FlareDrop已于2026年1月30日结束；2026年新增发行量削减到每年约30亿枚FLR。

## 它如何运作

Flare是一条兼容EVM的一层网络，为[以太坊]({lang}/eth/)编写的应用几乎不用改动就能在上面运行。它的特别之处在于协议本身内置的两套数据系统。Flare Time Series Oracle（FTSO）发布加密货币、股票等资产的价格：每个喂价约有100个独立数据提供者支持，最快的喂价每个区块更新一次，大约每1.1秒一次，应用可以免费读取。Flare Data Connector（FDC）负责确认其他区块链和网络上发生的事件——例如XRP Ledger上的某笔付款确实已经完成。在这两者之上是FAssets：独立代理人锁定抵押品，用户存入XRP，网络按一比一铸造FXRP，之后可以拿去借出、兑换或赚取收益。

## 人们为什么认为它有价值

FLR用于支付网络手续费、与验证者一起质押，以及委托给运行预言机的数据提供者，两者都能获得奖励。它还代表Flare治理中的投票权。这个代币背后的核心逻辑是来自XRP的需求：XRP是最大的加密货币之一，但单靠自己在DeFi里能做的事很少。如果更多XRP以FXRP的形式转到Flare上，手续费、质押和预言机使用量也会随之增长。2026年，Flare开始向FAssets和Data Connector收取协议费用，并提高了基础交易手续费，其中一部分会被销毁。

## 最新数据

- 当前价格：{{price:flr}}
- 历史最高价：{{ath:flr}}（{{athd:flr}}），距高点{{fromath:flr}}
- 市值：{{mcap:flr}}（在加密货币中排名{{rank:flr}}）
- 12个月价格变化：{{chg1y:flr}}
- 每天10美元、坚持1年：投入{{dcainv:1}}，变成{{dca:flr:1}}（{{dcaroi:flr:1}}）
- 每天10美元、坚持3年：投入{{dcainv:3}}，变成{{dca:flr:3}}（{{dcaroi:flr:3}}）

## 一路走来

Flare由Hugo Philion（CEO）和Sean Rowan（CTO）于2020年8月发布。2020年12月，项目对XRP钱包进行快照，承诺按一比一向持有者发放代币（当时名为Spark），许多交易所为用户支持了这次领取。代币于2022年10月更名为FLR，在推迟约两年之后，首批15%终于在2023年1月9日空投。价格在上线当天创下纪录，随后因大量领取者抛售，几天内下跌超过75%。其余85%的空投通过为期36个月的每月FlareDrop发放，已于2026年1月30日结束。FTSOv2带来了更快的喂价，FXRP于2025年9月在主网上线；2026年春，社区投票（FIP.16，98%赞成）将年发行量从最多50亿枚削减到约30亿枚FLR。

## 替代选择

在预言机领域，Flare的对手是市场龙头[Chainlink]({lang}/link/)，以及[Pyth]({lang}/pyth/)、[Band Protocol]({lang}/band/)和[API3]({lang}/api3/)。若想在DeFi中使用XRP，其他选择包括XRP Ledger自身的功能和其他链上的封装XRP——或者干脆直接持有[XRP]({lang}/xrp/)。[Songbird]({lang}/sgb/)是Flare的"金丝雀"测试网络，FAssets等新功能会先在那里运行。

## 主要风险

- **大幅波动：** FLR一生中大部分时间都远低于上线当天的纪录，小币种的下跌速度可能远快于比特币。
- **供应：** 每年仍有新的FLR发行；如果使用量不增长，以新代币支付的奖励可能压制价格。
- **依赖XRP：** 计划很大程度上取决于XRP持有者把币转到Flare；如果他们不这么做，FLR的需求仍会很小。
- **竞争：** Chainlink等预言机规模大得多，已被大多数大型DeFi应用采用。
- **技术：** FAssets依赖代理人、抵押品和跨链桥——即便经过审计，漏洞或抵押品暴跌仍可能造成损失。

## 对定投者意味着什么

FLR不长的历史，大部分是高调起步之后的漫长下滑，其间夹杂着剧烈反弹。定期投入固定金额，可以把买入价格分散到不同时间，而不是押注某一个时点——但对于一个年轻的小币种，这样做仍可能亏掉大部分资金。很多人只把这类币限制在加密资产中很小的一部分，而加密资产本身也只占储蓄的一小部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [FTSOv2 overview — Flare developer docs](https://dev.flare.network/ftso/overview)
- [Flare token airdrop finally happens after two-year wait (The Block, 9 January 2023)](https://www.theblock.co/post/200258/flare-token-airdrop-finally-happens-after-two-year-wait)
- [Flare Network launches FXRP to let XRP be used in DeFi apps (The Block, 24 September 2025)](https://www.theblock.co/post/372161/flare-network-fxrp-xrp-defi)
- [Flare's tokenomics revamp: the transition to activity-linked economics (DefiLlama Research)](https://defillama.com/research/spotlight/flare-tokenomics-revamp-transition-activity-linked-economics)
- [Flare price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/flare-networks)
