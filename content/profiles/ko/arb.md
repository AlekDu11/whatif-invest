---
title: Arbitrum(ARB) 쉽게 정리: 이더리움 레이어2, 옵티미스틱 롤업, 발행 한도 100억 개
description: Arbitrum을 쉽게 설명합니다: 이더리움 레이어2의 작동 원리, DAO에서 ARB의 역할, 토큰 언락, 지금까지의 이야기, 주요 위험.
date: 2026-11-23
kind: analysis
---
**Arbitrum(아비트럼)**은 이더리움 위에 만들어진 네트워크로, 거래를 더 빠르고 훨씬 저렴하게 만들면서도 보안은 이더리움에 의존합니다. 이런 구조를 '레이어2'라고 부릅니다. 미국 기업 Offchain Labs가 만들었고, 토큰 **ARB**를 가진 사람은 네트워크와 그 금고(트레저리)를 어떻게 운영할지 투표할 수 있습니다. 현재 ARB의 시가총액은 {{mcap:arb}}(암호화폐 중 {{rank:arb}})입니다.

> **핵심 요약**
> - ARB는 100억 개를 넘어 발행되지 않습니다. 2023년 3월 출시 당시 약 42%는 DAO 금고, 약 27%는 팀, 17.5%는 투자자에게 배정됐습니다.
> - 사상 최고가는 {{ath:arb}}({{athd:arb}})이며, 현재 가격은 최고가 대비 {{fromath:arb}}입니다.
> - ARB는 거버넌스 토큰입니다. Arbitrum의 수수료는 ARB가 아니라 ETH로 냅니다.
> - 2024년 3월부터 매달 팀과 투자자 물량의 언락(잠금 해제)이 이뤄져 시장에 새 공급이 더해지고 있습니다.

## 작동 원리

Arbitrum은 **옵티미스틱 롤업**입니다. 이더리움의 모든 노드가 모든 거래를 처리하는 대신, Arbitrum은 자체 체인에서 거래를 실행하고 압축한 데이터 묶음을 이더리움에 다시 기록합니다. 거래 순서를 정하고 순식간에 확인해 주는 것은 Offchain Labs가 운영하는 단 하나의 **시퀀서**입니다. 결과는 누군가 이의를 제기하지 않는 한 올바른 것으로 간주되며('낙관적' 방식), 어떤 검증자든 **사기 증명**(fraud proof)을 제출할 수 있고 분쟁은 이더리움에서 판가름 납니다. 2025년 2월부터 **BoLD** 프로토콜 덕분에 누구나 검증에 참여할 수 있고, 정직한 검증자 한 명만 있으면 체인을 지킬 수 있습니다. 소프트웨어 기반인 **Nitro**는 이더리움 앱과 호환되며, **Orbit** 프로그램으로 다른 프로젝트가 Arbitrum 기술로 자체 체인을 띄울 수 있습니다.

## 토큰의 쓰임새

ARB는 주로 투표용 토큰입니다. 보유자나 그들이 고른 대리인(델리게이트)이 **Arbitrum DAO**에서 네트워크 업그레이드와, 수십억 개의 ARB와 시퀀서 수수료 수입을 보유한 DAO 금고의 사용처에 대해 투표합니다. Arbitrum을 쓰는 데 ARB는 필요 없으며 가스비는 ETH로 냅니다. 따라서 토큰의 가치는 네트워크 사용량에 직접 연동되기보다 투표권과 DAO가 자금을 어떻게 쓰기로 하느냐에 달려 있습니다.

## 지금의 숫자

- 현재 가격: {{price:arb}}
- 사상 최고가: {{ath:arb}}({{athd:arb}}), 최고가 대비 {{fromath:arb}}
- 시가총액: {{mcap:arb}}(암호화폐 중 {{rank:arb}})
- 12개월 가격 변화: {{chg1y:arb}}
- 3년간 매일 10달러: 투자금 {{dcainv:3}}이 {{dca:arb:3}}로 ({{dcaroi:arb:3}})

## 지금까지의 이야기

Offchain Labs는 미국 프린스턴대학교의 연구에서 출발했습니다. Arbitrum One은 2021년 8월 말 일반에 공개됐고, 2022년 8월 Nitro 업그레이드로 수수료가 낮아지고 처리 용량이 늘었습니다. 2023년 3월 23일 이용자 대상 대규모 에어드롭과 함께 ARB 토큰이 출시됐습니다. 며칠 뒤 첫 제안인 AIP-1이 큰 반발을 샀습니다. 재단이 투표 전에 이미 7억 5,000만 ARB 배정분을 쓰기 시작했기 때문이며, 재단은 이후 제안을 나누고 DAO에 더 많은 통제권을 줬습니다. ARB는 2024년 1월 약 2.39달러로 고점을 찍었습니다. 2024년 3월 16일 팀과 투자자 물량 약 11억 개가 언락됐고, 이후 매달 언락이 이어졌습니다. 2025년 BoLD가 가동됐고, 가격은 2025~2026년에 걸쳐 크게 떨어졌습니다.

## 대안

Arbitrum은 이더리움의 다른 레이어2와 경쟁합니다. [Optimism]({lang}/op/)과 그 OP Stack으로 만든 체인들(자체 토큰이 없는 코인베이스의 Base 포함), [ZKsync]({lang}/zk/)·[Starknet]({lang}/strk/) 같은 영지식 롤업, 그리고 [Mantle]({lang}/mnt/)과 [POL (ex-MATIC)]({lang}/pol/)입니다. 업그레이드로 이용 비용이 계속 낮아지고 있는 [이더리움]({lang}/eth/) 자체도 대안입니다.

## 주요 위험

- **새 공급:** 팀과 투자자 물량의 언락이 계속되고 있고, DAO 금고도 전체 ARB의 큰 몫을 갖고 있습니다.
- **중앙화된 시퀀서:** 거래 순서는 한 운영자가 정합니다. 멈추거나 잘못 행동하면 이용자는 더 느린 우회 경로에 의존해야 합니다.
- **경쟁:** Base와 다른 레이어2가 같은 이용자, 앱, 수수료를 두고 다툽니다.
- **사용과의 약한 연결:** 수수료를 ETH로 내기 때문에 Arbitrum이 많이 쓰여도 ARB 수요가 자동으로 늘지는 않습니다.
- **규제:** 토큰, DAO, 그 뒤의 기업에 대한 규칙은 나라마다 다르고 바뀔 수 있습니다.

## 적립식으로 산다면

ARB는 역사 대부분을 초기 고점에서 내려오며 보냈기 때문에, 적립식으로 산 사람은 낮은 가격에 점점 더 많은 토큰을 모았습니다. 다만 이는 가격이 회복될 때만 도움이 됩니다. 일정 금액을 꾸준히 사면 매수 시점의 위험은 분산되지만 손실 위험이 사라지지는 않습니다. 많은 사람이 이런 토큰을 저축의 작은 일부로만 보유합니다. 과거 수익이 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [A gentle introduction to Arbitrum (Arbitrum 공식 문서)](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO (Arbitrum Foundation)](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet (The Block, 2025년 2월 12일)](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/arbitrum)
