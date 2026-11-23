---
title: Render（RENDER）をやさしく解説：OTOY発のGPUレンダリング網、上限約6.44億枚、2023年のSolana移行
description: Render（レンダー）をやさしく解説：クリエイターがGPU所有者にレンダリングやAI処理の対価を払う仕組み、バーン＆ミント、Solana移行、競合、主なリスク。
date: 2026-11-23
kind: analysis
---
**Render（レンダー）**は計算能力のマーケットプレイスです。アーティストやスタジオ、AI開発者が他人のグラフィックボード（GPU）を借りて使い、GPUの持ち主はRENDERトークンで報酬を受け取ります。ジュールズ・アーバック（Jules Urbach）率いるロサンゼルスのグラフィックソフト企業OTOYから生まれたプロジェクトで、「AI・コンピューティング」系トークンの代表格の一つです。現在の時価総額は{{mcap:render}}（暗号資産で{{rank:render}}）。

> **ポイント**
> - 供給上限は約6億4,400万RENDERで、2026年11月時点でその約86%が流通していました。
> - 2023年12月から「バーン＆ミント」方式で運営されています。仕事の支払いに使われたトークンは焼却され、GPU提供者向けに新しいトークンが発行されます。
> - 2023年11月、トークンはイーサリアム（ティッカーRNDR）からSolana（ティッカーRENDER）へ移行しました。
> - 最高値は{{ath:render}}（{{athd:render}}）で、現在の価格はそこから{{fromath:render}}の水準です。

## 仕組み

レンダリングとは、3Dのシーンを完成した画像や動画のコマに変換する処理で、大量のGPU能力を必要とします。高価な機材を買う代わりに、クリエイターは仕事をRenderネットワークに送ります。空いているGPUを持つ独立した「ノードオペレーター」がその仕事を引き受け、主にOTOYのソフトOctaneRenderで処理し、結果が確認されると報酬を受け取ります。2025年からは、Dispersedというプラットフォームなどを通じて、AIや一般的なGPU計算にも対象を広げています。ルール変更は公開提案「Render Network Proposals（RNP）」をトークン保有者が投票して決め、2023年にOTOYから独立したRender Network Foundationがガバナンスを監督しています。

## トークンの使い道

仕事の値段は普通のお金で決まります。「Burn-and-Mint Equilibrium」（RNP-001）では、クリエイターはRENDERで支払い、仕事が終わるとそのトークンは焼却（バーン）され、流通から消えます。エポック（約1週間）ごとに、ネットワークは決められた逓減スケジュールに沿って新しいRENDERを発行し、ノードオペレーターなどの貢献者に分配します。実際の需要による焼却が新規発行を上回れば供給は減り、需要が弱ければ増えます。RENDERは提案への投票にも使われます。

## 最新の数字

- 現在の価格：{{price:render}}
- 最高値：{{ath:render}}（{{athd:render}}）、そこから{{fromath:render}}
- 時価総額：{{mcap:render}}（暗号資産で{{rank:render}}）
- 12か月の価格変化：{{chg1y:render}}
- 毎日10ドルを1年間：投資額{{dcainv:1}}が{{dca:render:1}}に（{{dcaroi:render:1}}）

## これまでの歩み

アーバック氏がこの構想を初めて示したのは2009年です。トークンの一般販売は2017年10月、私募は2018年1〜5月に行われ、2020年4月27日にネットワークが一般公開されました。2023年、AIが市場の一番人気のテーマになると、トークン価格は何倍にも上がりました。保有者の投票でSolanaへの移行（RNP-002）が決まり、2023年11月2日に完了。バーン＆ミント方式による新規発行は2023年12月に始まりました。価格はAIブームのさなかの2024年3月にピークをつけ、2024年中に各取引所がRNDRからRENDERへ切り替えました。2026年11月には、AI関連トークンがそろって下げるなか、Renderは1週間で約12%下落しました。

## 代わりになるもの

ほかの分散型GPU・計算ネットワークには[Akash]({lang}/akt/)、[io.net]({lang}/io/)、[Aethir]({lang}/ath/)、[Golem]({lang}/glm/)があり、[Bittensor]({lang}/tao/)は暗号資産×AIの最大級のプロジェクトの一つです。ただし本当の競争相手は、Amazon Web ServicesやGoogle Cloudといった大手クラウドです。

## 主なリスク

- **値動きの大きさ：** 小型のAIトークンはビットコインよりはるかに大きく下がることがあり、2024年3月のピーク後、Renderは価値の大半を失いました。
- **新規発行：** エポックごとに新しいRENDERが発行されます。実際の仕事で焼却されるトークンが足りなければ、供給は増え続けます。
- **競争：** 大手クラウドは巨大な規模とサポート体制でGPUを提供しており、分散型ネットワークが太刀打ちするのは簡単ではありません。
- **依存：** ネットワークはOTOYのソフトとSolanaのブロックチェーンに大きく頼っており、どちらかに問題が起きれば影響を受けます。
- **規制：** 暗号資産のルールは国によって違い、急に変わることもあります。RENDERのようなトークンをどう分類するかも含めてです。

## 積立で買う人にとっての意味

RENDERの価格は急騰と深い下落を繰り返し、AIをめぐる市場の空気とともに動いてきました。決まった金額を定期的に買えば、安いときに多く、高いときに少なく買うことになり、底を当てようとする必要はありません。ただし損失のリスクがなくなるわけではありません。RENDERのようなトークンは、大きく値下がりしても困らない、貯蓄のごく一部にとどめる人が多いです。過去の成績は将来の利益を保証しません。

*投資助言ではありません。*

## 出典

- [Render Network — official site (rendernetwork.com)](https://rendernetwork.com/)
- [Render Network Knowledge Base: history and Burn Mint Equilibrium (know.rendernetwork.com)](https://know.rendernetwork.com/basics/burn-mint-equilibrium)
- [RNP-001: Burn-and-Mint Equilibrium (Render Network proposals, GitHub)](https://github.com/rendernetwork/RNPs/blob/main/RNP-001.md)
- [Render price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/render-token)
