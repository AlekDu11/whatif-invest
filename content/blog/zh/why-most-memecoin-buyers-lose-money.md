---
title: "为什么大多数买Meme币的人会亏钱：发行、滑点和手续费的数学"
description: pump.fun上只有0.41%的钱包实现了超过1万美元的利润。用简单的数学讲清发行、滑点和手续费如何对Meme币买家不利。
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0.41%
stat_label: pump.fun的1355万个钱包中实现超过1万美元利润的比例（Dune数据，2025年1月）
---
**为什么大多数买Meme币的人会亏钱？** 因为价格还没动，数学就已经对他们不利了：大多数新代币一天之内就没了，每次买卖都要付手续费和滑点，而最早的买家（往往是机器人和内部人）会把币卖给后来的人。想赚钱，一个代币既要活下来，*还要*涨到足以覆盖这些成本。

> **要点**
> - 2025年1月公布的Dune数据显示，在pump.fun的1355万个钱包中，只有约**0.41%**实现了超过**1万美元**的利润。
> - CoinGecko发现，pump.fun上**68.67%**的代币，最后一笔交易就发生在上线当天（2024年1月至2026年6月的数据）。
> - 新代币买卖一个来回，光平台手续费就可能超过**2.5%**，还要加上网络费和滑点。

## 第一部分——生存的数学

大多数Meme币不是"便宜"，而是"短命"。

- **上线当天就死掉。** CoinGecko统计了1867万个pump.fun代币，其中68.67%的最后一笔交易就在上线当天（2026年6月25日报道）。
- **很少能进入真正的市场。** "毕业"（graduation）是指代币离开pump.fun的初始价格曲线，进入普通的交易池。Dune数据显示，从2025年2月17日起连续四周，每周毕业率都低于**1%**；最好的一周（2024年11月）也只有**1.67%**。2026年3月达到**2.01%**，是2025年7月以来的最高值。

所以如果你随便挑新上线的币，手里大多是已经停止交易的币。几个大赢家要弥补许多归零的币，除非你挑得非常准——而在第一天，没有人知道哪些会活下来。

## 第二部分——手续费：进场要付，出场还要付

pump.fun的帮助页面（2025年9月）写明，毕业之前每笔交易收取**1.25%**的手续费（0.95%给平台，0.30%给创建者）。毕业后，代币越大费率越低，最小的1.25%，最大的0.30%。此外还有Solana网络费，以及可选的"优先"（priority）费和MEV保护费（该页面写的是每笔0.003–0.03 SOL）。

**算一笔账（仅作说明，不是真实价格）：** 你买了50美元的新代币，买和卖各付0.02 SOL的优先费。买卖两次1.25%的手续费约1.25美元，两次优先费可能还要再多几美元。只为回到50美元，这个代币大概就得涨**5–10%**。如果每次只交易10美元，情况更糟：固定费用占的比例大得多。

## 第三部分——滑点：你买的时候价格在动

**滑点**（slippage）是你看到的价格和你实际成交价格之间的差（见[Meme币词汇表]({lang}/memes/glossary/)）。新代币的池子很小，你自己的买单就会把价格推高——同一秒里其他人的买单也会。如果你把滑点设成10–20%（很多App对新币推荐这样设），就等于同意最多多付这么多。卖出时同样的问题反过来出现：池子很浅时，你的卖单会把价格压低。

## 第四部分——对面是谁

最早的买家往往是狙击手、捆绑者和开发者钱包（见[狙击手、捆绑者和开发者钱包]({lang}/blog/snipers-bundlers-dev-wallets/)）。他们以最低价买入，然后卖给第一波需求。如果你在第一根阳线之后才买，你往往就是"退出流动性"（exit liquidity）——他们卖币的接盘方。

## 一步一步：按下«Buy»之前先算一算

1. **第1步——算手续费。** 看兑换界面里的手续费那一行，再加上网络费/优先费。然后乘以二（买+卖）。
2. **第2步——检查滑点。** 在能成交的前提下尽量调低（比如池子大的币设1–3%）。如果一个币需要20%的滑点，这本身就是警告。
3. **第3步——看池子大小。** 在我们的[Meme页面]({lang}/memes/)打开代币，查看流动性。池子小＝买卖两边滑点都大。
4. **第4步——做安全检查。** 参考[买Meme币之前如何检查]({lang}/blog/how-to-check-a-memecoin-before-buying/)。
5. **第5步——提前定好能亏多少。** 只用亏光也无所谓的钱，并且在开始前就定好金额。

> **⚠️ 注意**
> - **"才0.0001美元，能涨1000倍。"** 价格低说明不了什么，很多代币发行量高达几十亿枚。重要的是这个代币能不能活下来，以及谁在把币卖给你。
> - **很多笔小额交易。** 光是固定的网络费和优先费，就可能在价格还没动时吃掉10美元交易的10%以上。
> - **晒收益的截图。** 你看到的是赚大钱的0.41%，看不到亏钱的几百万人；"大师"往往正在卖他们推荐的币。

## 如果你定期买入，这意味着什么

定期小额买入适用于多年后依然存在的资产——而不是今晚就可能停止交易的代币。如果你想持有加密货币，新手常走的路是一点点买入规模大、流动性好的币；作为对比，Solana自己的币SOL现在是{{price:sol}}（12个月{{chg1y:sol}}）——这是过去的结果，不是预测。你可以在我们的计算器里用任何资产试试"每天10美元"，并在你的[投资组合页面]({lang}/me/)上跟踪。

上一课：[狙击手、捆绑者和开发者钱包]({lang}/blog/snipers-bundlers-dev-wallets/)。所有课程都在[学习页面]({lang}/learn/)。

## 来源

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data（2025年1月11日）](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive（2025年3月14日）](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, Dune data: pump.fun graduation rate hits 2.01%（2026年3月17日）](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / CoinGecko data: nearly 70% of pump.fun tokens disappear on launch day（2026年6月25日）](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun Help Center: Transaction fees on pump.fun（2025年9月）](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*不构成投资建议。*
