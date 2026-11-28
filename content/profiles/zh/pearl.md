---
title: Pearl（PEARL）通俗解读：用GPU挖矿的有用工作量证明，上限21亿枚
description: Pearl通俗解读：GPU挖矿如何与AI计算挂钩、21亿枚供应上限、2026年4月上线、外界批评、竞争对手和主要风险。
date: 2026-11-28
kind: analysis
---
**Pearl**是一条用英伟达显卡挖矿的新一层区块链。比特币矿工解的是毫无用处的哈希难题，而Pearl的“有用工作量证明”（Proof of Useful Work）要求矿工做矩阵乘法——也就是运行AI模型所用的同一种数学运算。理论上，一块GPU可以同时为AI客户提供服务并保护网络。它由计算机科学家Omri Weinstein联合创办的Pearl Research Labs开发，主网于2026年4月27日上线。目前市值为{{mcap:pearl}}（在加密货币中{{rank:pearl}}）。

> **要点**
> - 币的总量永远不超过21亿枚，是比特币2100万枚的100倍；挖矿奖励平滑递减，而不是按周期减半。
> - 历史最高价为{{ath:pearl}}（{{athd:pearl}}），当前价格较其{{fromath:pearl}}。
> - 项目方称没有预挖、没有投资人份额，也没有团队金库：所有币都来自挖矿。
> - 2026年6月的一篇研究论文发现，当时的挖矿完全没有产生有用的AI计算。

## 它如何运作

矿工在GPU上做“加噪”的矩阵乘法，对结果的小块做哈希，再把整个工作打包进零知识证明，这样任何人都能快速验证，而不必重算一遍。这种方法来自2025年的一篇密码学论文，Weinstein是作者之一。官方挖矿程序接入常用的AI模型服务软件vLLM，运行在英伟达H100、H200等数据中心显卡上；社区开发的挖矿程序也能在游戏用的RTX显卡上运行。在底层，Pearl与比特币很像：它基于比特币节点程序btcd，每隔几分钟出一个新区块。这枚币常以PRL为代码上市，而在一些行情网站上，另一枚毫不相关的代币也使用同样的代码。

## 代币有什么用

币只作为矿工奖励产生，用于支付交易手续费。第一个商业案例出现在2026年5月：AI云服务公司Together AI推出了在Pearl矿机上运行的Gemma模型，价格比平常低25%以上，折扣部分由PRL奖励补贴。如果AI客户真的这样使用网络，挖矿就不只是耗电；如果没有，Pearl就只是又一枚供应量很大的工作量证明币。

## 最新数据

- 当前价格：{{price:pearl}}
- 历史最高价：{{ath:pearl}}（{{athd:pearl}}），距高点{{fromath:pearl}}
- 市值：{{mcap:pearl}}（在加密货币中排名{{rank:pearl}}）
- 12个月价格变化：{{chg1y:pearl}}

## 一路走来

作为基础的论文于2025年4月发表，主网在没有任何预先分发的情况下于2026年4月27日上线。5月底，在与Together AI合作之后，游戏玩家和显卡持有者蜂拥挖矿，随着竞争加剧，几周内一块RTX 5090的每日收益大约减半。起初，这枚币只能在MEXC等流动性很差的小型交易所交易。2026年6月，arXiv上的论文《The Usefulness Gap in Proof-of-Useful-Work》指出，网络中数千名矿工并没有进行有用的AI计算，最流行的挖矿软件里甚至没有AI代码。Pearl在6月的一次硬分叉中加入了对混合专家（mixture-of-experts）AI模型的支持；到2026年10月，最大供应量中约16%已被挖出。

## 替代选择

[比特币]({lang}/btc/)是经典的工作量证明币，用专用芯片而不是GPU挖矿。在AI与算力项目中，[Bittensor]({lang}/tao/)奖励运行AI模型的人，[Render]({lang}/render/)、[Akash Network]({lang}/akt/)和[io.net]({lang}/io/)则直接出租GPU算力。Pearl的思路不同：挖矿本身就应该是有用的AI工作。

## 主要风险

- **非常新：** 这枚币只有几个月的价格历史，年轻的币可能很快失去大部分价值。
- **用处尚未证明：** 独立研究人员至今几乎没发现真正的AI工作，最大的卖点可能站不住脚。
- **挖矿收益：** 难度上升、奖励下降会压缩矿工收入，而矿工常常卖币来付电费。
- **持有集中：** 最初几周挖矿成本很低，所以早期参与者持有很大一部分。
- **流动性和同名币：** 交易比大币清淡，而且还有另一枚使用PRL代码的代币——务必仔细核对合约和交易所。

## 对定投者意味着什么

Pearl上市交易才几个月，还没有能说明问题的定投记录。按计划定期投入固定金额，可以分散选错时机的风险，但对一枚全新的币来说，并不能消除亏掉大部分本金的风险。很多人只把这类试验性的币控制在储蓄中很小的一部分。过往表现不代表未来收益。

*不构成投资建议。*

## 资料来源

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
