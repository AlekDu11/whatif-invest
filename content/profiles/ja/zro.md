---
title: LayerZero（ZRO）をやさしく解説：発行上限10億枚、2024年6月のエアドロップ、ブロックチェーン間メッセージング
description: LayerZeroをやさしく解説：ブロックチェーン同士をつなぐ仕組み、2024年のZROエアドロップ、固定の10億枚、アンロック、リスク、買う人が知っておきたいこと。
date: 2026-11-24
kind: analysis
---
**LayerZero**は、ブロックチェーン同士を「会話」させるメッセージングプロトコルです。あるチェーン上のアプリが、別のチェーン上のアプリにデータや命令、トークンを送れるようになります。トークンのZROは2024年6月20日、初期ユーザーへのエアドロップとともに誕生し、現在の時価総額は{{mcap:zro}}（暗号資産で{{rank:zro}}）。ZROを買う人の多くは、LayerZeroがこれからもブロックチェーン間の主要な「配管」であり続け、独自の新ネットワーク「Zero」が実際に使われることに賭けています。

> **ポイント**
> - ZROは10億枚を超えて発行されることはなく、そのうち8.5%（8,500万枚）が2024年6月20日の最初のエアドロップでユーザーに配られました。
> - 最高値は{{ath:zro}}（{{athd:zro}}）で、現在の価格はそこから{{fromath:zro}}です。
> - 投資家とチームの保有分（供給量の57.7%）は、1年間のロック後に2年かけて毎月アンロックされるため、2027年半ばごろまで新しいZROが市場に出てきます。
> - 2026年4月、LayerZero上に構築されたブリッジ、Kelp DAOのrsETHが攻撃を受け、約2億9,200万ドルを失いました。

## 仕組み

Ethereum、Solana、BNB Chainなどのブロックチェーンは、互いのデータを直接読むことができません。LayerZeroは各チェーンに「endpoint」と呼ばれる小さな変更不可能なコントラクトを置きます。アプリがメッセージを送ると、DVN（分散型検証者ネットワーク）と呼ばれる独立した検証者が受け取り側で本当に送られたことを確認し、executorがそれを届けます。どのDVNを信頼し、いくつの合意を必要とするかは各アプリが自分で選ぶため、安全性はその選択次第です。その上にあるのがOFT（Omnichain Fungible Token）規格で、トークンをあるチェーンでバーン（焼却）またはロックし、別のチェーンでミントまたは解放するので、総供給量は変わりません。LayerZeroによると、OFTはこれまでに160以上のブロックチェーンで2,900億ドルを超える送金を処理しました。ステーブルコインやETHを移すブリッジのStargateは、この上に作られた最初の大型アプリです。

## なぜ価値があると考えられているのか

ZROはガバナンストークンで、保有者はプロトコルの運営方法に投票します。最も注目されているのは「fee switch」です。LayerZeroのメッセージ1件ごとに小さな手数料をかけ、それをZROに換えてバーンし、供給量を減らす仕組みです。保有者は2024年12月から年2回この件に投票してきましたが、直近の2026年6月を含め、これまでの投票ではすべて手数料はオフのままとされました。2026年にはZROの役割も広がりました。LayerZeroが独自のブロックチェーン「Zero」を発表し、ZROはそのガス代、ネットワークを守るステーキング用トークン、さらに取引エンジンATLASの取引手数料の75%（取引所へのリベート後）で買い戻してバーンされる資産になる予定です。

## 最新の数字

- 現在の価格：{{price:zro}}
- 最高値：{{ath:zro}}（{{athd:zro}}）、そこから{{fromath:zro}}
- 時価総額：{{mcap:zro}}（暗号資産で{{rank:zro}}）
- 12か月の価格変化：{{chg1y:zro}}
- 毎日10ドルを1年間：投資額{{dcainv:1}}が{{dca:zro:1}}に（{{dcaroi:zro:1}}）

## これまでの歩み

LayerZero Labsは、Bryan Pellegrino（CEO）、Ryan Zarick（CTO）、Caleb Banisterが創業しました。2022年3月にStargateが稼働し、同じ月にSequoia、a16z、FTX Venturesなどの投資家から評価額10億ドルで1億3,500万ドルを調達。2023年4月には1億2,000万ドルの追加調達で評価額は30億ドルになりました。トークン発行前、チームは多数のウォレットでエアドロップを集める「ファーマー」を摘発する公開の「sybil hunt」を実施し、約128万のウォレットが対象となりました。受け取り（クレーム）は2024年6月20日に始まりましたが、「proof of donation」という変わった条件付きでした。受け取るには、Ethereum開発者向けの基金Protocol Guildに1 ZROあたり0.10ドルを寄付する必要があったのです。多くのユーザーが反発し、価格はローンチ時の約4.40ドルから最初の数日で下落しました。ZROは2024年12月に最高値をつけました。2025年8月、Stargate DAOはWormholeからの対抗提案があったにもかかわらず、約95%の賛成で、ZRO建て約1億2,000万ドル（1 STGあたり0.08634 ZRO）でのLayerZeroによる買収を承認しました。2026年2月、LayerZeroはCitadel Securities、DTCC、ICE、ARK Investが支援する金融市場向けブロックチェーン「Zero」を発表し、2026年10月にはZeroのメインネットとATLASの稼働予定日を2026年11月30日と定めました。

## 代わりになるもの

クロスチェーンのメッセージングでは、LayerZeroは[Wormhole]({lang}/w/)、CCIPサービスを持つ[Chainlink]({lang}/link/)、[Axelar]({lang}/axl/)と競合しています。単にチェーン間でトークンを移すだけなら、[Across]({lang}/acx/)のようなブリッジを選ぶ人もいます。[Stargate]({lang}/stg/)はLayerZero自身のブリッジアプリで、現在はプロトコルが所有しています。

## 主なリスク

- **大きな値動き：** ZROは最高値を大きく下回る期間が長く続いてきました。小型コインはビットコインよりはるかに速く下落することがあります。
- **アンロック：** 投資家とチームは2027年半ばごろまで毎月新しいトークンを受け取ります。彼らが売れば、価格の重しになりかねません。
- **ハッキング：** クロスチェーンブリッジは暗号資産の中でも特に攻撃されやすい分野です。2026年4月、DVNを1つだけ設定していたKelp DAOのrsETHブリッジが約2億9,200万ドルを失いました。LayerZeroは北朝鮮のLazarusグループと検証者1つだけの設定に原因があるとし、その後一部のプロジェクトはChainlinkへ移りました。
- **競争：** Chainlink、Wormhole、Axelarが同じアプリを奪い合っており、乗り換えも可能です。
- **価値の取り込み：** fee switchはまだオフで、ZeroとATLASも始まったばかりです。使われなければ、ZROへの需要は限られたままです。

## 積立で買う人にとっての意味

ZROの短い歴史は、話題を呼んだエアドロップ、序盤の急落、2024年末の最高値、そして急反発をはさんだ長い下落の連続です。一定額を定期的に買えば、一度のタイミングに賭けるのではなく、購入価格を時間で分散できます。ただし、若いコインで毎月アンロックもあるため、それでも資金の大部分を失う可能性はあります。こうしたコインは暗号資産のごく一部にとどめ、その暗号資産自体も貯蓄の一部に抑える人が多くいます。過去の結果は将来のリターンを保証しません。

*投資助言ではありません。*

## 出典

- [LayerZero V2 overview — LayerZero docs](https://docs.layerzero.network/v2/home/v2-overview)
- [LayerZero Foundation to begin ZRO token airdrop claims today (The Block, 2024年6月20日)](https://www.theblock.co/post/300951/layerzero-foundation-to-begin-zro-token-airdrop-claims-today)
- [LayerZero's proof-of-donation claiming mechanism (The Block, 2024年6月)](https://www.theblock.co/post/301043/layerzero-proof-of-donation-zro-claiming-mechanism)
- [Fee switch referendums — LayerZero Foundation](https://layerzero.foundation/fee-switch)
- [Stargate DAO approves LayerZero acquisition (The Block, 2025年8月24日)](https://www.theblock.co/post/368040/stargate-dao-approves-layerzero-acquisition-despite-last-minute-interest-from-wormhole-axelar-and-across)
- [LayerZero says Lazarus likely behind Kelp DAO exploit (The Block, 2026年4月20日)](https://www.theblock.co/post/398028/layerzero-kelp-dao-lazarus)
- [ZRO surges as LayerZero unveils ATLAS on Zero (The Block, 2026年8月25日)](https://theblock.co/news/ecosystems/2026-08-25-zro-token-layerzero-atlas-exchange-infrastructure-zero-blockchain-412736)
- [LayerZero sets November 30 launch for Zero mainnet and ATLAS (crypto.news, 2026年10月)](https://crypto.news/layerzero-zero-mainnet-atlas-november-30-launch/)
- [LayerZero Labs raises $135 million (Business Wire, 2022年3月30日)](https://www.businesswire.com/news/home/20220330005301/en/LayerZero-Labs-Raises-135-Million-to-Create-Omnichain-Crypto-Networks)
