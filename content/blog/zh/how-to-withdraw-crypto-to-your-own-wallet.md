---
title: 如何把加密货币从交易所提到自己的钱包：一步步教你
description: 复制正确的地址、选同一个网络、需要时填写Memo，先小额测试。安全地把币从交易所转到你自己的钱包。
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 同一个网络
stat_label: 交易所和钱包必须用同一个网络，否则币可能丢失
---
**怎样把加密货币提到自己的钱包？** 先在钱包里复制这个币的**收款地址**。然后在交易所打开**Withdraw**（提币），粘贴地址，选择和钱包**相同的网络**，输入一笔小额测试金额，再用2FA确认。测试的币到账后，再把剩下的转过去。

> **要点**
> - 三样东西必须一致：**币种**、**地址**和**网络**（币在上面转移的区块链，比如Ethereum、BNB Smart Chain、TRON或Solana）。Binance提醒：用错网络发送的币可能永远找不回来。
> - 有些币（比如XRP、XLM或ATOM）还需要**Memo**或**Tag**（一串短数字，告诉收款方这笔币是谁的）。没有它，转账可能卡住，或者进了别人的账户。
> - **一定要先小额测试。** 币一旦离开交易所，提币就无法撤销。

本课接着[如何设置定投]({lang}/blog/how-to-set-up-a-recurring-buy/)。为什么要有自己的钱包，请看[热钱包和冷钱包]({lang}/blog/crypto-wallets-hot-vs-cold/)。

## 开始之前

你需要两样东西：一个有币、并且开了2FA保护的交易所账户（请看[如何注册加密货币交易所]({lang}/blog/how-to-register-on-a-crypto-exchange/)）；还有一个已经设置好的自己的钱包App。钱包的**助记词**（能恢复钱包的12个或24个秘密单词）要写在纸上，离线保存。助记词不要输入到任何别的地方——交易所、网站或“客服”都永远不需要它。

## 第1步——复制钱包的收款地址

1. 打开钱包App，点**Receive**（收款），有的叫**Deposit**（充值）。
2. 选择币种，比如比特币或USDT。
3. 如果钱包让你选网络，就选一个，并记下是哪个——比如“TRON上的USDT（TRC20）”或“Ethereum上的USDT（ERC20）”。
4. 点地址旁边的**Copy**（复制）。不要手动输入。

地址是一长串字母和数字。比特币地址常以**bc1**开头，Ethereum和BNB Smart Chain地址以**0x**开头，TRON地址以**T**开头。

## 第2步——在交易所打开提币页面

在Binance App里是**Assets → Spot → Send → Withdraw Crypto**；在网站上是**Wallet → Overview → Withdraw**。其他交易所在钱包或资产页面里，每个币旁边都有**Withdraw**按钮。选择和第1步相同的币。

## 第3步——粘贴地址，选择网络

1. 把地址粘贴到**Address**（地址）栏。
2. 把**前4位和后4位字符**和钱包里的对比一下。有些恶意软件会把你复制的地址换成小偷的地址。
3. 选择**网络**。它必须和第1步钱包显示的一样。Binance可能会自动推荐网络——还是要自己核对。不要只因为手续费最低就选某个网络。
4. 如果出现**Memo**或**Tag**栏，而钱包给了你一个，就填上。如果你自己的钱包没有显示Memo，通常就不需要——但最好在钱包的帮助页面再确认一下。

小提示：如果不确定，可以把地址保存到交易所的**Address Management**（地址簿）。Binance还有**白名单**：开启后，只能提币到已保存的地址，万一密码被盗也能多一层保护。

## 第4步——先小额测试

1. 输入一笔小金额——比页面显示的最低提币额稍多一点就行。
2. 看清**网络手续费**和**实际到账**（you will receive）两行。手续费按每笔提币固定收取，所以金额很小时，手续费占比可能很高。
3. 按**Withdraw**，用2FA验证码或通行密钥确认。有些交易所还会发确认邮件——打开邮件，点**Confirm**（确认）。

## 第5步——确认到账，再转剩下的

1. 等待。根据网络和拥堵情况，转账可能需要几秒到一小时左右。
2. 在交易所打开提币记录，可以看到状态和**TxID**（交易ID，可以在区块浏览器网站上查询）。
3. 币出现在钱包里后，用剩下的金额重复第2到第4步。地址已经在记录或地址簿里了，第二次会更快。

把币加入[你的投资组合]({lang}/me/)，无论它们放在哪里，都能在一个地方查看价值。

> **⚠️ 注意**
> - **网络选错。** USDT存在于很多网络上。把“TRC20”的USDT发到只接收“ERC20”的地址，币可能会丢失。网络要检查两遍。
> - **漏填Memo或Tag。** 需要Memo的交易所和钱包，没有它就不知道到账的币是谁的。即使能找回，也很慢，还要收费。
> - **假客服和“地址验证”网站。** 正规的机构不会问你要助记词，也不会让你转币来“验证”钱包。只在官方App或官方网站里提币。

## 如果你定期买入，这意味着什么

如果你每周或每月买一点，不需要每买一次就提一次币——每次提币都有手续费。很多人让币在交易所里慢慢攒着，隔一段时间（比如每季度一次）再一次性转一大笔到自己的钱包。我们计算器的例子：每天10美元买比特币，坚持3年（共{{dcainv:3}}），变成了{{dca:btc:3}}（{{dcaroi:btc:3}}）。这是过去的结果，不是预测。比特币现在的价格是{{price:btc}}；请看[比特币页面]({lang}/btc/)。

上一课：[如何设置定投]({lang}/blog/how-to-set-up-a-recurring-buy/)。下一课：如何卖出加密货币，把钱转到银行账户。在[交易所页面]({lang}/exchanges/)比较各家交易所；所有课程都在[学习页面]({lang}/learn/)。

## 来源

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance（2026年3月更新）](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account（2026年6月）](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*不构成投资建议。*
