---
title: Starknet(STRK) 쉽게 정리: StarkWare가 만든 Ethereum 레이어 2, 2021년부터 가동, 이제는 비트코인 스테이킹까지
description: Starknet을 쉽게 설명합니다: ZK-STARK 레이어 2가 Ethereum을 싸게 만드는 원리, STRK의 쓰임새, 비트코인 스테이킹, 지금까지의 이야기, 경쟁자, 주요 위험.
date: 2026-11-25
kind: analysis
---
**Starknet**은 [Ethereum]({lang}/eth/) 위에서 돌아가는 '레이어 2' 네트워크입니다. 수천 건의 거래를 한데 묶고, 그 거래가 모두 올바르다는 것을 암호학으로 증명한 뒤 그 증명을 Ethereum에 올립니다. 그래서 앱을 쓰는 비용이 Ethereum에서 직접 쓸 때의 일부에 불과합니다. 이스라엘 기업 StarkWare가 만들었고 2021년 11월에 가동을 시작했습니다. 토큰 STRK의 시가총액은 {{mcap:strk}}(암호화폐 중 {{rank:strk}})입니다.

> **핵심 요약**
> - 2024년 2월 토큰 출시 때 STRK 100억 개가 만들어졌고, 스테이킹 보상으로 새 토큰이 더해집니다.
> - 2025년 9월부터 랩드 비트코인 보유자는 이를 Starknet에서 스테이킹할 수 있으며, 1억 STRK 규모의 인센티브 프로그램이 뒷받침합니다.
> - 사상 최고가는 {{ath:strk}}({{athd:strk}})이며, 현재 가격은 그보다 {{fromath:strk}} 수준입니다.
> - Starknet은 Ethereum의 Solidity 대신 자체 프로그래밍 언어인 Cairo를 씁니다.

## 작동 원리

Starknet은 'ZK 롤업'입니다. 거래는 Starknet에서 처리되고, 이어서 '프루버'가 STARK를 만듭니다. STARK는 모든 계산 단계가 올바르게 이뤄졌음을 보여 주는 짧은 수학적 증명입니다. Ethereum은 작업을 다시 할 필요 없이 그 증명만 확인하면 되므로, 많은 거래가 값싼 확인 한 번을 나눠 쓰면서도 Ethereum의 보안에 기댈 수 있습니다. StarkWare의 공동 창업자 Eli Ben-Sasson은 STARK 증명을 고안한 과학자 중 한 명이며, 프로젝트 측은 이 증명이 미래의 양자 컴퓨터에도 견딜 수 있다고 말합니다. 개발자들은 증명하기 쉬운 프로그램을 만들도록 설계된 언어인 Cairo로 Starknet 앱을 작성합니다.

## STRK는 어디에 쓰이나

STRK는 Starknet의 거래 수수료를 내는 데 쓰이고, 네트워크 업그레이드에 관한 투표에도 쓰이며, 스테이킹할 수도 있습니다. 보유자가 STRK를 검증인에게 맡겨 네트워크 보안을 돕고 보상으로 새 STRK를 받는 방식입니다. 스테이킹은 2024년 11월에 시작됐습니다. 2025년 8월 온체인 투표(SNIP-31, 찬성 약 93.6%)로 랩드 비트코인(WBTC, tBTC, LBTC, SolvBTC)을 STRK와 함께 스테이킹할 수 있게 됐고, 비트코인 스테이킹은 2025년 9월 30일에 시작됐습니다. 2026년 2월 Starknet은 잔액을 비공개로 하고 송금 내용을 숨길 수 있는 비트코인 담보 토큰 strkBTC를 발표했습니다.

## 지금의 숫자

- 현재 가격: {{price:strk}}
- 사상 최고가: {{ath:strk}}({{athd:strk}}), 최고가 대비 {{fromath:strk}}
- 시가총액: {{mcap:strk}}(암호화폐 중 {{rank:strk}})
- 12개월 가격 변화: {{chg1y:strk}}
- 1년간 매일 10달러: 투자금 {{dcainv:1}}이 {{dca:strk:1}}로 ({{dcaroi:strk:1}})

## 지금까지의 이야기

StarkWare는 2018년에 설립됐고, 처음에는 dYdX와 Immutable 같은 거래소가 쓰는 엔진인 StarkEx로 기술을 판매했습니다. 범용 네트워크 Starknet은 2021년 11월에 열렸습니다. STRK 토큰은 2024년 2월 20일 사용자와 개발자를 대상으로 한 대규모 에어드롭과 함께 출시됐습니다. 가격은 처음 며칠이 가장 높았고, 이후 2년 대부분 동안 하락했습니다. 초기 투자자와 팀이 가진 대량의 토큰이 조금씩 락업 해제됐기 때문입니다. 2025~2026년에 프로젝트는 Starknet을 Ethereum뿐 아니라 비트코인을 활용하는 곳으로 새로 자리매김했습니다.

## 대안

Starknet은 다른 Ethereum 레이어 2 네트워크와 경쟁합니다. [Arbitrum]({lang}/arb/)과 [Optimism]({lang}/op/)(옵티미스틱 롤업), Coinbase의 Base, 그리고 [ZKsync]({lang}/zk/), Scroll, Linea 같은 다른 ZK 롤업입니다. Starknet만의 특징은 STARK 증명과 Cairo 언어이지만, 그 대신 Ethereum 개발자는 새 언어를 배워야 한다는 단점이 있습니다.

## 주요 위험

- **경쟁:** 많은 레이어 2 네트워크가 같은 사용자와 앱을 두고 다투며, 가장 많이 쓰이는 네트워크가 활동의 대부분을 가져갑니다.
- **토큰 공급:** 스테이킹으로 새 STRK가 늘어나고, 초기 투자자와 기여자의 토큰은 여러 해에 걸쳐 락업 해제됐습니다.
- **기술:** 복잡한 암호 기술, 브리지, 랩드 비트코인 발행사는 고장 나거나 해킹당할 수 있으며, 네트워크 일부는 여전히 소수의 운영자가 돌리고 있습니다.
- **가치 포착:** 싼 수수료는 사용자에게는 좋지만, 토큰 가격을 받쳐 줄 수 있는 수익은 줄어듭니다.
- **큰 변동성:** 대부분의 신생 토큰처럼 STRK도 고점 대비 가치의 대부분을 잃은 적이 있습니다.

## 적립식으로 산다면

STRK는 가격 이력이 짧고 변동성이 큰 신생 토큰이라, 여기서 적립식으로 산 사람은 지금까지 주로 떨어지는 가격을 겪었습니다. 일정 금액을 꾸준히 사면 나쁜 시점에 들어갈 위험은 분산되지만, 긴 하락에서 지켜 주지는 못합니다. 많은 사람이 이런 토큰을 암호화폐 보유분의 작은 일부로만 둡니다. 과거 수익률이 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Starknet, BTCFi 확장으로 비트코인 스테이킹과 수익 상품 도입 (The Block)](https://www.theblock.co/post/372720/starknet-bitcoin-staking-100m-strk-incentives-re7-btc-yield)
- [Starknet, 레이어 2에 '프라이빗 비트코인'을 가져올 strkBTC 공개 (The Block)](https://www.theblock.co/post/391420/starknet-introduces-strkBTC-to-bring-private-bitcoin-and-confidential-defi-transactions-to-its-layer-2-network)
- [Starknet, L2 네트워크에 비트코인 스테이킹 도입 (ForkLog)](https://forklog.com/en/starknet-introduces-bitcoin-staking-on-l2-network/)
- [비트코인을 일하게 만들려는 Starknet (Blockworks)](https://www.blockworks.co/news/starknet-making-btc-productive)
- [Starknet 블로그 (starknet.io)](https://www.starknet.io/blog/all/)
