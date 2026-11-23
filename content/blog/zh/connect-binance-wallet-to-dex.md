---
title: 如何把Binance Wallet连接到DEX并把币转回来：一步一步
description: 安全地把Binance Wallet连接到DEX网站，用正确的网络把币转回Binance账户，并清理旧的授权——步骤简单清楚。
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: 每个新地址或新网络前先做一笔小额测试转账
---
**怎么把Binance Wallet连接到DEX？** 打开DEX的官方网站，点 **Connect Wallet**（连接钱包），选择Binance Wallet（或者选WalletConnect，用Binance App扫二维码），再在App里确认。要把币转回来，就复制Binance上同一币种、同一网络的**充值地址**，然后从钱包转过去——先转一小笔测试。

> **要点**
> - DEX（去中心化交易所——直接用自己钱包兑换代币的网站）永远不需要你的恢复密码或助记词。连接只是让网站可以*请求*你签名；你不确认，什么都不会动。
> - 两边的网络必须一致（BNB Smart Chain对BNB Smart Chain，Solana对Solana）。网络或地址错了，币可能就没了。
> - 每次"Approve"（授权）都会让网站可以替你花这个代币。授权额度要小，不用的授权要删掉。

本课接着[如何创建Binance Wallet]({lang}/blog/how-to-create-binance-wallet/)。Meme币风险极高——只用亏得起的钱。

## 第1步：打开真正的网站

连Logo都一模一样的假DEX网站，是最常见的陷阱之一。

1. 自己输入网址或用书签。不要点搜索结果里的广告，也不要点聊天群里的链接。
2. 逐个字母检查地址栏。
3. 确认这个DEX支持你的币所在的网络。

## 第2步：连接钱包

根据设备不同，有三种方式：

- **装了Binance Wallet浏览器扩展的电脑**（Chrome或Brave）。用Binance App扫描扩展上的二维码登录。然后在DEX上点 **Connect** 或 **Connect Wallet**，选Binance Wallet，确认弹窗。
- **没装扩展的电脑。** 在DEX上点 **Connect Wallet → WalletConnect**，会出现一个二维码。用Binance App里的扫码功能扫描，点 **Connect**。
- **手机。** 在手机浏览器里打开DEX，点 **Connect Wallet**，从列表里选Binance Wallet，在App里确认。

确认之前先看弹窗：网站名称、网址、网络。只要有一项不对，就点Cancel（取消）。

## 第3步：兑换，并读懂每一次签名

1. 选择你要付的币和你想要的代币（用**合约地址**找代币，不要用名字）。
2. 输入一小笔金额，检查汇率、滑点（你能接受的最大价格变动）和网络手续费。
3. 第一次卖某个代币时，网站会要求 **Approve**（花费这个代币的权限）。如果可以，填具体金额，不要选"无限"。
4. 在App里确认兑换。如果签名请求是一大段看不懂的代码，或者根本说不通——**不要签**。

## 第4步：把币转回Binance账户

1. 在Binance App里切换到 **Exchange** → **Assets** → **Deposit**（充值），选择币种（比如BNB）。
2. 选择**网络**（比如BNB Smart Chain），复制充值地址。有些币还需要 **memo/tag**（备注/标签）——也一起复制。
3. 切换到 **Wallet** → **Send**（发送），选同一个币、同一个网络，粘贴地址（有备注的话也粘贴）。
4. 先转一小笔测试。到账之后再转剩下的。

钱包里留一点BNB或SOL：每次链上操作都要付网络手续费，失败了也一样。有些Meme币根本不能充到交易所（交易所没有上线它）——要变现，先在钱包里把它换回BNB、SOL或USDT。

## 第5步：断开连接并清理

1. 用完后断开网站连接（在钱包的已连接网站或WalletConnect设置里，或者DEX上的 **Disconnect** 按钮）。
2. 时不时检查代币授权，把不需要的撤销（revoke）。撤销要花一点手续费。
3. 在公用电脑上，要退出扩展的登录。

你买的代币可以在[我的投资组合]({lang}/me/)里跟踪，实时Meme币数据见[Meme币页面]({lang}/memes/)。

> **⚠️ 注意**
> - **网站或"客服"索要恢复密码、助记词或"同步钱包"。** 真正的DEX和Binance员工从来不会这样做。马上关掉页面。
> - **无限授权和盲签。** 一次恶意授权或签名，就能让骗子以后不经你确认清空这个代币。
> - **网络错了、漏了备注、粘贴的地址被换了。** 恶意软件能替换你复制的地址。每次都核对开头和结尾的字符，并用小额测试。

下一课：买之前如何检查一个Meme币。所有课程都在[学习页面]({lang}/learn/)。

## 来源

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*不构成投资建议。本教程只讲解工具怎么用，不推荐买入任何代币。Binance Wallet可能并非在所有国家都能使用。*
