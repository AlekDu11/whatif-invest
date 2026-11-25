---
title: Starknet（STRK）をやさしく解説：StarkWareが手がけるEthereumのレイヤー2、2021年から稼働、今はビットコインのステーキングも
description: Starknetをやさしく解説：ZK-STARKのレイヤー2がEthereumを安くする仕組み、STRKの使い道、ビットコインのステーキング、歩み、ライバル、主なリスク。
date: 2026-11-25
kind: analysis
---
**Starknet**は[Ethereum]({lang}/eth/)の上で動く「レイヤー2」ネットワークです。数千件の取引をまとめ、それがすべて正しいことを暗号技術で証明し、その証明をEthereumに書き込みます。そのため、アプリを使うコストはEthereum上で直接使う場合のごく一部で済みます。開発したのはイスラエルの企業StarkWareで、2021年11月に稼働を始めました。トークンSTRKの時価総額は{{mcap:strk}}（暗号資産で{{rank:strk}}）です。

> **ポイント**
> - 2024年2月のトークン開始時に100億STRKが発行され、ステーキング報酬としてさらに新しいトークンが加わります。
> - 2025年9月から、ラップドビットコインの保有者はStarknet上でそれをステーキングできるようになり、1億STRKのインセンティブプログラムが用意されました。
> - 最高値は{{ath:strk}}（{{athd:strk}}）で、現在の価格はそこから{{fromath:strk}}の水準です。
> - Starknetは、EthereumのSolidityではなく独自のプログラミング言語Cairoを使っています。

## 仕組み

Starknetは「ZKロールアップ」です。取引はStarknet上で処理され、その後「プルーバー」がSTARKをつくります。STARKとは、すべての計算が正しく行われたことを示す短い数学的な証明です。Ethereumは作業をやり直す必要がなく、その証明を確認するだけで済むため、多くの取引が1回の安い確認を分け合いながら、Ethereumのセキュリティに頼ることができます。StarkWareの共同創業者Eli Ben-Sassonは、STARK証明を考案した科学者の一人です。プロジェクトによると、この証明は将来の量子コンピューターにも耐えられるとされています。開発者はCairoでStarknetのアプリを書きます。Cairoは、プログラムを証明しやすくするために設計された言語です。

## STRKは何に使われるのか

STRKはStarknetの取引手数料の支払いに使われ、ネットワークのアップグレードをめぐる投票にも使われます。さらにステーキングもできます。保有者がバリデーターにSTRKを預けてネットワークの安全を支え、報酬として新しいSTRKを受け取る仕組みです。ステーキングは2024年11月に始まりました。2025年8月のオンチェーン投票（SNIP-31、賛成約93.6%）で、ラップドビットコイン（WBTC、tBTC、LBTC、SolvBTC）をSTRKと並んでステーキングできるようになり、ビットコインのステーキングは2025年9月30日に始まりました。2026年2月には、残高を非公開にでき、送金内容も秘匿できるビットコイン裏付けのトークンstrkBTCを発表しました。

## 最新の数字

- 現在の価格：{{price:strk}}
- 最高値：{{ath:strk}}（{{athd:strk}}）、そこから{{fromath:strk}}
- 時価総額：{{mcap:strk}}（暗号資産で{{rank:strk}}）
- 12か月の価格変化：{{chg1y:strk}}
- 毎日10ドルを1年間：投資額{{dcainv:1}}が{{dca:strk:1}}に（{{dcaroi:strk:1}}）

## これまでの歩み

StarkWareは2018年に設立され、最初はStarkExとして技術を販売していました。StarkExはdYdXやImmutableなどの取引所が使うエンジンです。汎用ネットワークのStarknetは2021年11月に公開されました。STRKトークンは2024年2月20日に、ユーザーや開発者への大規模なエアドロップとともに始まりました。価格が最も高かったのは最初の数日で、その後の2年間の大半は下落が続きました。初期投資家やチームが持つ大量のトークンが少しずつロック解除されたためです。2025〜2026年には、StarknetをEthereumだけでなくビットコインを使う場所として位置づけ直しました。

## 代わりになるもの

Starknetは、ほかのEthereumのレイヤー2ネットワークと競合しています。[Arbitrum]({lang}/arb/)や[Optimism]({lang}/op/)（オプティミスティック・ロールアップ）、CoinbaseのBase、そして[ZKsync]({lang}/zk/)、Scroll、LineaといったほかのZKロールアップです。Starknetの特徴はSTARK証明とCairo言語ですが、その裏返しとして、Ethereumの開発者は新しい言語を覚えなければなりません。

## 主なリスク

- **競争：** 多くのレイヤー2ネットワークが同じユーザーとアプリを奪い合っており、よく使われるネットワークに活動の大半が集まります。
- **トークンの供給：** ステーキングで新しいSTRKが増えるうえ、初期投資家や貢献者のトークンは数年かけてロック解除されてきました。
- **技術：** 複雑な暗号技術、ブリッジ、ラップドビットコインの発行者は、故障したりハッキングされたりする可能性があります。ネットワークの一部は今も少数の運営者が動かしています。
- **価値の取り込み：** 安い手数料は利用者には良いことですが、トークン価格を支えうる収益は少なくなります。
- **大きな値動き：** 多くの新しいトークンと同じく、STRKはピークから価値の大半を失ったことがあります。

## 積立で買う人にとっての意味

STRKは価格の歴史が短く、値動きの激しい新しいトークンです。そのため、ここで積立を続けた人がこれまで経験してきたのは、主に下がり続ける価格でした。一定額を定期的に買えば、悪いタイミングで買うリスクは分散できますが、長い下落から守ってくれるわけではありません。多くの人は、こうしたトークンを暗号資産の保有分のごく一部にとどめています。過去の実績は将来のリターンを保証するものではありません。

*投資助言ではありません。*

## 出典

- [StarknetがBTCFi拡大でビットコインのステーキングと利回り商品を導入（The Block）](https://www.theblock.co/post/372720/starknet-bitcoin-staking-100m-strk-incentives-re7-btc-yield)
- [Starknet、レイヤー2に「プライベートなビットコイン」をもたらすstrkBTCを発表（The Block）](https://www.theblock.co/post/391420/starknet-introduces-strkBTC-to-bring-private-bitcoin-and-confidential-defi-transactions-to-its-layer-2-network)
- [StarknetがL2ネットワークでビットコインのステーキングを導入（ForkLog）](https://forklog.com/en/starknet-introduces-bitcoin-staking-on-l2-network/)
- [Starknet、ビットコインを「稼ぐ資産」にする取り組み（Blockworks）](https://www.blockworks.co/news/starknet-making-btc-productive)
- [Starknetブログ（starknet.io）](https://www.starknet.io/blog/all/)
