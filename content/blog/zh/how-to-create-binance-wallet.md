---
title: 如何创建Binance Wallet并买入Meme币：一步步教程
description: 在Binance App里创建Binance Wallet并备份，从Binance账户转入币，按合约地址找到代币并兑换，附安全检查清单。
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: 份密钥分片保护Binance Wallet，进入钱包需要其中2份
---
**怎么创建Binance Wallet？** 打开Binance App，在顶部切换到 **Wallet**（钱包）标签，点 **Create Keyless Wallet**（创建无私钥钱包），再用恢复密码备份。只需几分钟，不需要助记词，你就有了一个自托管钱包（币由你自己掌控，而不是交易所），可以用来买Meme币等链上代币。

> **要点**
> - Binance Wallet就在Binance App里。你需要一个已认证的Binance账户，但钱包里的币是自托管的——备份由你负责。
> - 这是"无私钥"（MPC）钱包：密钥被分成3份，分别在你的手机上、你的云端备份里和Binance那里。任意2份就能打开钱包。
> - 千万别跳过备份。如果你丢了手机，**又**忘了恢复密码，Binance也无法帮你恢复钱包。

开始之前：大多数新Meme币几乎会跌光。只用你完全亏掉也承受得起的钱——先看看[什么是Meme币]({lang}/blog/what-are-memecoins/)。

## 你需要准备

- 一部装有官方Binance App的手机（只从App Store、Google Play或binance.com下载——假App很常见）。
- 一个已完成身份认证（KYC，即提交证件）的Binance账户。如果还没有，可以通过我们的链接注册：[Binance Wallet](/go/binance-web3?from=learn&l=zh)。
- Binance账户里有少量BNB或SOL，用来买币和支付网络手续费。

## 第1步：打开钱包

1. 登录Binance App。
2. 在屏幕顶部，从 **Exchange**（交易所）切换到 **Wallet**。
3. 点 **Create Keyless Wallet**。（如果你已经有别的钱包，另一个选项是 **Import Wallet**（导入钱包）——新手用不到。）

创建只要几秒。App不会给你12个或24个助记词，而是使用MPC（多方计算——密钥被拆成几份，从不放在同一个地方）。

## 第2步：备份（千万别跳过）

App提供三种方式保存你的备份分片，选一种：

- **iCloud** 或 **Google Drive**。你设置一个只有自己知道的**恢复密码**。分片用它加密后保存到你的云盘。
- **二维码。** 你设置恢复密码并保存一个二维码；分片存放在去中心化云端。
- **Quick Backup**（快速备份）。用Face ID或指纹确认；不需要密码，但分片由第三方服务商保管。

把恢复密码写在纸上，放在安全的地方。然后检查一下：点 **Settings**（设置，在首页或资产页左上角）→ **Wallet Management**（钱包管理）。你应该能看到 **Backed Up**（已备份）标签。

## 第3步：把币从Binance转进钱包

1. 在钱包里点 **Receive**（收款）→ **Withdraw from Binance Exchange**（从Binance交易所提现）。
2. 选择币种（比如BNB）**和网络**（BNB选BNB Smart Chain，SOL选Solana）。网络必须一致。
3. 输入金额。确认前，App会显示手续费和最终到账金额。
4. 选择钱从现货（Spot）账户还是资金（Funding）账户出，点 **Withdraw**（提现），核对地址和网络，再点 **Confirm**（确认）。

先用小额测试。已确认的转账无法撤销。钱包里一定要留一点BNB或SOL：链上的每个操作都要付网络手续费（Gas），失败了也要付。

## 第4步：用合约地址找到正确的代币

很多Meme币都有同名同图标的山寨版。唯一可靠的身份证是**合约地址**（每个代币独有的一长串字母和数字）。

1. 从可信来源获取地址：项目的认证账号、大型数据网站，或我们[Meme币页面]({lang}/memes/)上的代币页。
2. 在钱包的 **Markets**（市场）或 **Trade**（交易）界面，把地址粘贴到搜索框，不要输入名字。
3. 把开头和结尾的4–6个字符和来源对照一下。

## 第5步：买之前先检查代币

在我们的[Meme币页面]({lang}/memes/)上，每个代币页都会显示Binance的安全检查和关键数据。重点看：

- **流动性**——交易池里有多少钱。流动性少 = 你可能卖不掉。
- **持有人数和前10名占比**——如果少数几个钱包持有大部分代币，他们可以把价格砸穿。
- **上线时间**——一小时前刚创建的代币等于一张彩票。
- **警告**——只要出现任何风险或安全警告，就停手。

Binance自己也说，它不审核Meme Rush（它的全新Meme币列表）上的代币，所以检查要靠你自己。我们的[骗局与跑路课程]({lang}/blog/memecoin-scams-rug-pull/)列出了危险信号。

## 第6步：兑换

1. 打开 **Trade** → **Swap**（兑换）。在同一网络上，选择你用什么付款（BNB）和想要的代币。
2. 输入一个小金额。看清汇率、**滑点**（交易失败前你能接受的最大价格变化）和网络手续费。
3. 有些代币需要先做一步 **Approve**（授权），会收一点手续费。
4. 点 **Swap**，用通行密钥或双重验证确认。

卖出时反过来操作。如果你想看最新的代币，Markets标签里有 **Meme Rush**：全新代币在那里按"联合曲线"交易，在"迁移"到普通DEX（去中心化交易所）之前，不能转出钱包。这是市场里风险最高的角落。

> **⚠️ 注意**
> - **没备份，或者把密码存在截图里。** 手机和密码都丢了，币就永远没了。
> - **网络或地址填错。** Binance的常见问题说明，转到错误地址的代币无法退回。每次都先发一笔测试金额。
> - **假代币和"客服"消息。** 只用合约地址搜索。Binance员工绝不会问你的恢复密码，也不会让你去某个网站"验证"钱包。

下一课：如何把Binance Wallet连接到DEX网站，以及如何把币转回Binance。全部课程见[学习]({lang}/learn/)栏目。

## 来源

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*不构成投资建议。Meme币风险极高；本教程只讲解App怎么用，不推荐买入任何代币。Binance Wallet可能并非在所有国家都能使用。*
