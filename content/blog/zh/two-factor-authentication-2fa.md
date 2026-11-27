---
title: "双重验证（2FA）：一步一步教你开启"
description: 2FA给你的交易所账户加上第二把锁。一步一步教你开启身份验证器App或通行密钥，以及为什么短信验证码是最弱的方式。
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 6800万美元
stat_label: 2021年SIM卡互换诈骗造成的损失，FBI共收到1611起投诉（IC3，2022年2月）
---
**2FA是什么？怎么开启？** 双重验证（2FA，也叫两步验证）是指登录或提币时需要两样东西：你的密码，*再加上*第二个证明，比如手机App里的6位数验证码，或者通行密钥（passkey，用指纹或面容）。在交易所的**Security**（安全）设置里开启它，并且优先用身份验证器App或通行密钥，而不是短信。

> **要点**
> - 有了2FA，光偷到密码还不足以清空你的账户。
> - **短信验证码是最弱的方式：** 在"SIM卡互换"（SIM swap）中，犯罪分子把你的手机号转到他们的SIM卡上，收走你的验证码。FBI记录了2021年的1611起此类投诉，损失超过**6800万美元**；而2018–2020年是320起投诉、约1200万美元。
> - FBI推荐更强的方式：身份验证器App、生物识别或实体安全密钥。

## 各种方式，从弱到强

- **短信验证码**——一条带验证码的短信。聊胜于无，但你的手机号可能被盗。
- **邮箱验证码**——安全程度取决于你的邮箱账户（邮箱也要开2FA）。
- **身份验证器App**（Google Authenticator、Microsoft Authenticator等）——手机App每30秒生成一个新的6位数验证码，离线也能用。没人能通过运营商截获它。
- **通行密钥**（passkey，生物识别）——用指纹、面容或手机PIN确认。它只在真正的网站上有效，所以假网站偷不走。
- **实体安全密钥**（小小的USB/NFC设备）——最强的方式，适合大额资金。

## 一步一步：身份验证器App（以币安App为例）

其他交易所的步骤几乎一样；在个人资料里找**Security**（安全）。

1. **第1步——安装App。** 从官方App Store或Google Play下载Google Authenticator（或其他身份验证器App）。
2. **第2步——打开安全设置。** 在币安App里点**Account**（账户）图标，点顶部你的个人资料，再点**Security**。
3. **第3步——开始设置。** 点**Authenticator App**（身份验证器App），再点**Enable**（启用）。你会看到一个二维码和一个**设置密钥**（一长串代码）。
4. **第4步——把设置密钥抄在纸上。** 这是你手机丢了时的备份。像助记词一样离线保管。先别点**Next**（下一步）。
5. **第5步——在验证器里添加账户。** 在Google Authenticator里点**+**，选择**Enter a setup key**（输入设置密钥），或者扫描二维码，粘贴密钥，输入一个名字比如"Binance"，点**Add**（添加）。
6. **第6步——确认。** 回到币安点**Next**，输入App里的6位数验证码。你会看到成功提示。
7. **第7步——测试一下。** 退出登录再重新登录。如果要求输入验证码，就说明设置好了。

## 一步一步：通行密钥（更简单）

币安帮助页面说，需要App版本2.60以上、iOS 16以上或Android 9以上。

1. **Account → 个人资料 → Security → Passkeys (Biometrics) → Add Passkey。**
2. 如果要求，用你现在的2FA确认，点**Continue**（继续）。
3. 选择保存位置：iCloud钥匙串（iPhone）、Google密码管理工具（Android）或安全密钥，然后用指纹、面容或PIN确认。

## 开启2FA之后

- 如果交易所允许，关掉短信登录方式；至少也要向运营商申请SIM卡锁或携号转网密码。
- 绑定交易所的邮箱也要开启2FA。
- 如果交易所有这个功能，开启**提币白名单**（只有保存过的地址才能收款）。

> **⚠️ 注意**
> - **真正的工作人员绝不会问你要2FA验证码。** Telegram上的"客服"、自称"交易所"或"银行"打来电话要6位数验证码的，一定是骗子。
> - **手机丢了又没有备份密钥。** 那样恢复账户要花好几天做身份验证。把设置密钥写在纸上，妥善保管。
> - **假的验证器App和仿冒的登录页面。** 只从官方应用商店安装App，交易所网址自己输入或用书签打开。

## 如果你定期买入，这意味着什么

如果你每月买一点，你的交易所账户会慢慢变成一笔真正的钱——比如比特币现在是{{price:btc}}（12个月{{chg1y:btc}}），这是过去的结果，不是预测。花十分钟设置2FA，就能保护多年的积累。在你的[投资组合页面]({lang}/me/)跟踪你持有的资产。

上一课：[助记词：保管好它的5条规则]({lang}/blog/seed-phrase-safety-rules/)。更多：[如何注册加密货币交易所]({lang}/blog/how-to-register-on-a-crypto-exchange/)、[在你所在国家能用的交易所]({lang}/exchanges/)。所有课程都在[学习页面]({lang}/learn/)。

## 来源

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions（2022年2月8日）](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app（2025年12月10日更新）](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account（2025年12月10日更新）](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*不构成投资建议。*
