---
title: LayerZero（ZRO）通俗解读：10亿枚总量、2024年6月空投与跨链消息传递
description: 用大白话看LayerZero：它如何连接各条区块链、2024年ZRO空投、固定10亿枚总量、代币解锁、主要风险，以及买家需要了解的事。
date: 2026-11-24
kind: analysis
---
**LayerZero**是一种消息传递协议，让各条区块链可以相互"对话"：一条链上的应用能把数据、指令或代币发送给另一条链上的应用。它的代币ZRO于2024年6月20日通过向早期用户空投的方式推出，当前市值{{mcap:zro}}（在加密货币中排名{{rank:zro}}）。人们买ZRO，主要是押注LayerZero会继续充当区块链之间的主要"管道"，并且它自己的新网络Zero能被真正用起来。

> **要点**
> - ZRO总量永远不会超过10亿枚；其中8.5%（8500万枚）在2024年6月20日的首次空投中发给了用户。
> - 它的历史最高价为{{ath:zro}}（{{athd:zro}}），当前价格距高点{{fromath:zro}}。
> - 投资者和团队的代币（占总量57.7%）在锁仓一年后分两年按月解锁，因此到2027年年中前后都会有新的ZRO进入市场。
> - 2026年4月，基于LayerZero搭建的Kelp DAO rsETH跨链桥遭到攻击，损失约2.92亿美元。

## 它如何运作

以太坊、Solana或BNB Chain这样的区块链无法直接读取彼此的数据。LayerZero在每条链上部署一个小巧且不可更改的合约，称为endpoint。当应用发送消息时，名为DVN（去中心化验证者网络）的独立验证方会在另一端确认这条消息确实发生过，再由executor（执行者）把它送达。每个应用自己决定信任哪些DVN、需要多少个DVN同意——所以它的安全性取决于这个选择。在此之上是OFT（Omnichain Fungible Token，全链同质化代币）标准：代币在一条链上销毁或锁定，在另一条链上铸造或释放，总量因此保持不变。据LayerZero称，OFT已在160多条区块链上处理了超过2900亿美元的转账。用于转移稳定币和ETH的跨链桥Stargate，是第一个基于它构建的大型应用。

## 人们为什么认为它有价值

ZRO是治理代币：持有人投票决定协议如何运作。最受关注的问题是"fee switch"（费用开关）——对每条LayerZero消息收取一小笔费用，换成ZRO后销毁，从而减少供应。自2024年12月起，持有人每年就此投票两次，迄今为止的每一次投票（最近一次在2026年6月）都决定继续关闭费用。2026年ZRO的作用也变得更大：LayerZero宣布推出自己的区块链Zero，ZRO计划用作其Gas费、保障网络安全的质押代币，以及用其交易引擎ATLAS 75%的交易手续费（扣除给交易场所的返佣后）回购并销毁的资产。

## 最新数据

- 当前价格：{{price:zro}}
- 历史最高价：{{ath:zro}}（{{athd:zro}}），距高点{{fromath:zro}}
- 市值：{{mcap:zro}}（在加密货币中排名{{rank:zro}}）
- 12个月价格变化：{{chg1y:zro}}
- 每天10美元、坚持1年：投入{{dcainv:1}}，变成{{dca:zro:1}}（{{dcaroi:zro:1}}）

## 一路走来

LayerZero Labs由Bryan Pellegrino（CEO）、Ryan Zarick（CTO）和Caleb Banister创立。Stargate于2022年3月上线，同月公司以10亿美元估值从Sequoia、a16z和FTX Ventures等投资者那里融资1.35亿美元；2023年4月，又一轮1.2亿美元融资使其估值达到30亿美元。代币推出前，团队公开开展了"sybil hunt"（女巫猎杀），打击用大量钱包"撸"空投的人，最终约128万个钱包符合条件。领取于2024年6月20日开放，并附带一个名为"proof of donation"（捐赠证明）的特别条件：用户每领取1枚ZRO，须向以太坊开发者基金Protocol Guild捐赠0.10美元。许多用户对此不满，价格在最初几天从上线时的约4.40美元回落。ZRO在2024年12月创下历史最高价。2025年8月，尽管Wormhole提出了竞争报价，Stargate DAO仍以约95%的赞成票同意被LayerZero以约1.2亿美元的ZRO（每枚STG换0.08634枚ZRO）收购。2026年2月，LayerZero发布了面向金融市场的区块链Zero，获得Citadel Securities、DTCC、ICE和ARK Invest的支持；2026年10月，它将Zero主网和ATLAS的计划上线日期定为2026年11月30日。

## 替代选择

在跨链消息领域，LayerZero的竞争对手有[Wormhole]({lang}/w/)、拥有CCIP服务的[Chainlink]({lang}/link/)以及[Axelar]({lang}/axl/)。如果只是在链与链之间转移代币，用户也会选择[Across]({lang}/acx/)等跨链桥。[Stargate]({lang}/stg/)是LayerZero自己的跨链桥应用，如今归协议所有。

## 主要风险

- **大幅波动：** ZRO曾长时间远低于历史高点，小币种的跌速可能远快于比特币。
- **解锁：** 投资者和团队到2027年年中前后每月都会拿到新代币；如果他们卖出，可能压制价格。
- **黑客攻击：** 跨链桥是加密世界中最常遭受攻击的环节之一。2026年4月，只配置了一个DVN的Kelp DAO rsETH跨链桥损失约2.92亿美元；LayerZero将其归咎于朝鲜的Lazarus组织以及只用一个验证方的设置，之后一些项目转向了Chainlink。
- **竞争：** Chainlink、Wormhole和Axelar争夺的是同一批应用，应用也可以更换方案。
- **价值捕获：** 费用开关仍处于关闭状态，Zero和ATLAS也才刚起步——如果它们没人用，对ZRO的需求就仍然有限。

## 对定投者意味着什么

ZRO短暂的历史包括：备受炒作的空投、上线初期的急跌、2024年底的历史高点，以及夹杂着猛烈反弹的漫长下跌。定期买入固定金额，可以把买入价格分散到不同时间，而不是押注某一个时刻——但对于一个年轻的币种、再加上每月解锁，你仍可能亏掉大部分本金。很多人只把这类币当作加密资产中很小的一部分，而加密资产本身也只占储蓄的一小部分。过去的表现不代表未来的收益。

*不构成投资建议。*

## 资料来源

- [LayerZero V2 overview — LayerZero docs](https://docs.layerzero.network/v2/home/v2-overview)
- [LayerZero Foundation to begin ZRO token airdrop claims today (The Block, 2024年6月20日)](https://www.theblock.co/post/300951/layerzero-foundation-to-begin-zro-token-airdrop-claims-today)
- [LayerZero's proof-of-donation claiming mechanism (The Block, 2024年6月)](https://www.theblock.co/post/301043/layerzero-proof-of-donation-zro-claiming-mechanism)
- [Fee switch referendums — LayerZero Foundation](https://layerzero.foundation/fee-switch)
- [Stargate DAO approves LayerZero acquisition (The Block, 2025年8月24日)](https://www.theblock.co/post/368040/stargate-dao-approves-layerzero-acquisition-despite-last-minute-interest-from-wormhole-axelar-and-across)
- [LayerZero says Lazarus likely behind Kelp DAO exploit (The Block, 2026年4月20日)](https://www.theblock.co/post/398028/layerzero-kelp-dao-lazarus)
- [ZRO surges as LayerZero unveils ATLAS on Zero (The Block, 2026年8月25日)](https://theblock.co/news/ecosystems/2026-08-25-zro-token-layerzero-atlas-exchange-infrastructure-zero-blockchain-412736)
- [LayerZero sets November 30 launch for Zero mainnet and ATLAS (crypto.news, 2026年10月)](https://crypto.news/layerzero-zero-mainnet-atlas-november-30-launch/)
- [LayerZero Labs raises $135 million (Business Wire, 2022年3月30日)](https://www.businesswire.com/news/home/20220330005301/en/LayerZero-Labs-Raises-135-Million-to-Create-Omnichain-Crypto-Networks)
