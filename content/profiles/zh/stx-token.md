---
title: Stacks（STX）通俗解读：为比特币带来智能合约，自2021年运行，奖励以BTC发放
description: 用大白话看Stacks：比特币二层如何运作、转移证明（Proof of Transfer）、锁仓赚BTC、sBTC、发展历程、主要风险，以及定投者需要了解的事。
date: 2026-11-24
kind: analysis
---
**Stacks**是一条建立在比特币之上的区块链，为比特币补上了它本身没有的东西：智能合约，以及借贷、交易、NFT等应用。它的交易锚定在比特币区块链上，目前STX代币的总市值为{{mcap:stx-token}}（在加密货币中排名{{rank:stx-token}}）。人们关注它，是因为它是让比特币不只是躺在钱包里、而能"发挥更多作用"的最早、规模最大的途径之一。

> **要点**
> - Stacks矿工用真金白银的比特币来竞争新发行的STX，而锁定STX的持有者可以获得这些比特币。
> - 2019年，其背后的公司Blockstack完成了首个获得美国SEC依据Regulation A+核准的代币发售。
> - 历史最高价为{{ath:stx-token}}（{{athd:stx-token}}）；当前价格距离该高点{{fromath:stx-token}}。
> - 自2024年10月的Nakamoto升级以来，出块只需几秒，已确认的交易与比特币本身一样难以被推翻。

## 它如何运作

Stacks采用名为转移证明（Proof of Transfer，PoX）的机制。Stacks矿工不像比特币矿工那样消耗电力，而是发送比特币来竞拍写入下一个Stacks区块的权利，并获得新产生的STX。这些比特币并不会消失：它们会流向参与"堆叠"（stacking）的人——这些人把STX锁定若干个周期（每个周期约两周），帮助保障网络安全。每个Stacks区块都记录在比特币上，因此要改写Stacks的历史，就得改写比特币的历史。应用使用Clarity编写，这是一种专为行为可预测、易于检查而设计的编程语言，还能读取比特币链上发生的事情。

## 人们为什么认为它有价值

在Stacks上支付交易手续费需要STX，矿工赚取的也是STX，而锁定STX是获得BTC奖励的途径——因此网络的需求与代币的需求直接挂钩。更宏大的设想是比特币DeFi：大多数比特币处于闲置状态，而Stacks提供了一种不离开比特币世界就能在应用中使用它们的方式。实现这一点的主要工具是sBTC，一种由比特币1:1支持的代币，可以转入Stacks应用使用，也可以再赎回为BTC。

## 最新数据

- 当前价格：{{price:stx-token}}
- 历史最高价：{{ath:stx-token}}（{{athd:stx-token}}），距高点{{fromath:stx-token}}
- 市值：{{mcap:stx-token}}（在加密货币中排名{{rank:stx-token}}）
- 12个月价格变化：{{chg1y:stx-token}}
- 每天10美元、坚持5年：投入{{dcainv:5}}，变成{{dca:stx-token:5}}（{{dcaroi:stx-token:5}}）

## 一路走来

Muneeb Ali和Ryan Shea在普林斯顿（Princeton）相识，于2013年创办了Blockstack。2017年，项目向投资者出售代币；2019年7月，它成为首家通过SEC核准的Regulation A+发售向公众提供代币的公司。2021年1月，带有转移证明和Clarity的Stacks 2.0主网上线，当年价格从约0.40美元涨到2美元以上。到2022年底跌至约0.20美元，随后借比特币"Ordinals"热潮反弹，并于2024年4月1日创下历史最高价。紧接着是2024年10月的Nakamoto升级，2024年12月开放sBTC存入，2025年4月开放提回比特币。尽管如此，价格在2025年一路下滑，2026年的大部分时间都低于0.40美元。

## 替代选择

在把应用带到比特币上的项目中，Rootstock运行一条由比特币矿工保护、兼容以太坊的侧链；[Core]({lang}/core/)是一条支持比特币质押的独立链；[Babylon]({lang}/baby/)则让人们质押比特币来保护其他网络。许多比特币持有者干脆改用[以太坊]({lang}/eth/)上的包装比特币。而对于只想持有比特币本身的人来说，[比特币]({lang}/btc/)就是最直接的选择。

## 主要风险

- **大幅波动：** 到2022年底，STX已较2021年的高点下跌超过90%；在2024年创下纪录后，类似的下跌再次发生。
- **新增供应：** 每天都会产生新的STX作为挖矿奖励，可能持续带来抛压。
- **竞争：** 许多更新的比特币二层在争夺同一批用户和同一批比特币。
- **技术：** sBTC依赖一组保管比特币的签名者；一旦那里出现漏洞或故障，可能损害人们对整个网络的信任。
- **保管与监管：** 交易所倒闭或丢失私钥，代币可能永久丢失；各国加密货币规则不同，且可能迅速变化。

## 对定投者意味着什么

Stacks的价格呈长波段起伏：2021年和2024年两次大顶，每次之后都是深度下跌。定期买入固定金额，意味着不必猜底也能在价格低时多买、价格高时少买——但正如上面的5年结果所示，它并不能让你免受长期下跌的影响。许多人只把像STX这样的小币种放在储蓄中很小的一部分，即使大跌也能承受。过去的表现不代表未来的回报。

*不构成投资建议。*

## 资料来源

- [Finally, Finality: the Nakamoto upgrade (Stacks Foundation)](https://stacks.org/nakamoto)
- [The sBTC mainnet release is live with Bitcoin deposits (Stacks blog)](https://www.stacks.co/blog/bitcoin-deposits-live)
- [sBTC withdrawal functionality is now live (Stacks blog)](https://www.stacks.co/blog/sbtc-withdrawals-live)
- [Stacks price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/stacks)
