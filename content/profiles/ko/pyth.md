---
title: 피스 네트워크(PYTH) 쉽게 정리: 100개 넘는 블록체인용 가격 오라클, 최대 100억 개, 2021년부터 가동
description: 피스 네트워크 쉽게 정리: 가격이 블록체인에 전달되는 방식, PYTH의 용도, 잠금 해제 일정, 지금까지의 이야기, 주요 위험, 적립식 투자자가 알아야 할 것.
date: 2026-11-24
kind: analysis
---
**피스 네트워크(Pyth Network)**는 '오라클', 즉 암호화폐·주식·환율·원자재 같은 실제 시장 가격을 블록체인으로 가져오는 서비스입니다. 덕분에 대출 앱, 거래소 등 스마트 계약이 무엇이 얼마인지 알 수 있습니다. 가격은 웹사이트에서 긁어 온 것이 아니라 거래소와 트레이딩 회사에서 직접 들어옵니다. 2021년 솔라나에서 시작해 지금은 100개가 넘는 블록체인에서 쓰이며, PYTH 토큰의 시가총액은 {{mcap:pyth}}(암호화폐 중 {{rank:pyth}})입니다.

> **핵심 요약**
> - 피스는 거래소·마켓메이커·트레이딩 회사 같은 1차 출처의 가격을 100개가 넘는 블록체인에 보냅니다.
> - PYTH는 절대 100억 개를 넘지 않습니다. 85%는 출시 때 잠겼고 2027년 5월까지 매년 한 번씩 4단계로 풀립니다.
> - 2025년 8월 미국 상무부는 공식 GDP 데이터를 블록체인에 게시하기 위해 체인링크와 함께 피스를 선택했습니다.
> - 사상 최고가는 {{ath:pyth}}({{athd:pyth}})이며, 현재 가격은 최고가 대비 {{fromath:pyth}}입니다.

## 작동 원리

데이터 '퍼블리셔'는 자신들의 가격을 1초에도 여러 번 피스 전용 네트워크로 보냅니다. 피스는 이를 하나의 가격으로 합치고, 출처들 사이에 차이가 얼마나 나는지 보여 주는 신뢰 구간을 함께 붙입니다. 모든 가격을 모든 체인에 계속 기록하는 대신 피스는 '풀(pull)' 방식을 씁니다. 앱이 필요할 때만 서명된 최신 가격을 가져가고 소액의 수수료를 냅니다. 그래서 비용이 낮고, 같은 데이터가 여러 체인에 동시에 전달됩니다.

## 토큰은 어디에 쓰이나

PYTH는 주로 거버넌스와 보안을 위한 토큰입니다. 스테이킹한 보유자는 Pyth DAO에서 수수료, 보상, 새 가격 피드에 대해 투표합니다. Oracle Integrity Staking을 통해 특정 퍼블리셔를 뒷받침하도록 PYTH를 스테이킹할 수도 있는데, 좋은 데이터에는 보상이, 나쁜 데이터에는 불이익이 따를 수 있습니다. 2025년 하반기부터 Pyth Pro가 은행과 트레이딩 회사에 프리미엄 시장 데이터를 구독형으로 팔고 있으며, 2025년 12월 DAO는 네트워크 수익으로 채워지는 재원의 3분의 1을 매달 시장에서 PYTH를 사는 데 쓰는 PYTH Reserve를 시작했습니다.

## 지금의 숫자

- 현재 가격: {{price:pyth}}
- 사상 최고가: {{ath:pyth}}({{athd:pyth}}), 최고가 대비 {{fromath:pyth}}
- 시가총액: {{mcap:pyth}}(암호화폐 중 {{rank:pyth}})
- 12개월 가격 변화: {{chg1y:pyth}}
- 1년간 매일 10달러: 투자금 {{dcainv:1}}이 {{dca:pyth:1}}로 ({{dcaroi:pyth:1}})

## 지금까지의 이야기

피스는 2021년 트레이딩 회사와 거래소 그룹의 지원을 받아 솔라나에서 시작했으며, 초기 기여자 중에는 Jump Crypto도 있었습니다. PYTH 토큰은 2023년 11월 피스를 쓰는 앱 이용자들에게 에어드롭되며 출시됐습니다. 가격은 2024년 3월 약 1.20달러로 정점을 찍은 뒤 이후 2년 대부분 하락했고, 2024년 5월과 2025년 5월의 대규모 잠금 해제가 공급을 늘렸습니다. 2025년 8월 28일에는 미국 GDP 데이터 소식에 PYTH가 하루 만에 70% 넘게 올랐습니다. 2025년 9월 Pyth Pro가, 2025년 12월 토큰 매입 준비금이 뒤따랐습니다.

## 대안

압도적인 최대 경쟁자는 가장 오래되고 가장 널리 쓰이는 오라클인 [체인링크(Chainlink)]({lang}/link/)입니다. 그 밖에 [RedStone]({lang}/red/), [API3]({lang}/api3/), [Band]({lang}/band/)가 있습니다. 전통 금융에서는 Pyth Pro가 블룸버그(Bloomberg), LSEG 같은 기존 데이터 업체와도 경쟁합니다.

## 주요 위험

- **토큰 잠금 해제:** 마지막 대규모 해제는 2027년 5월로 예정돼 있고, 새 공급은 과거에도 가격을 눌렀습니다.
- **경쟁:** 오라클 시장은 체인링크가 장악하고 있으며, 여러 업체를 함께 쓰는 앱도 많습니다.
- **데이터 오류:** 틀리거나 늦은 가격은 부당한 청산을 일으키고 신뢰를 해칠 수 있습니다.
- **사용과 가격의 약한 연결:** 네트워크가 커져도 토큰은 떨어질 수 있으며, 매입 규모는 토큰 가치에 비해 작습니다.
- **집중과 규제:** 초기 투자자와 내부자가 많은 물량을 보유하고 있고, 암호화폐와 시장 데이터 규정은 바뀔 수 있습니다.

## 적립식으로 산다면

PYTH는 역사가 짧고 가격이 대부분 하락해 온 젊은 토큰입니다. 일정 금액을 꾸준히 사면 매수 가격이 분산되지만, 앞으로의 잠금 해제 압력이나 토큰이 계속 가치를 잃을 위험까지 없애 주지는 않습니다. 이런 토큰은 저축의 작은 일부로만 두는 사람이 많습니다. 과거 수익이 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Understanding the PYTH tokenomics (Pyth Network)](https://www.pyth.network/blog/understanding-the-pyth-tokenomics)
- [Pyth launches token buyback program, allocating 33% of DAO treasury to monthly PYTH purchases (The Block, 12 December 2025)](https://www.theblock.co/news/business/2025-12-12-pyth-token-buyback-program-33-dao-treasury-monthly-pyth-purchases-382357)
- [Pyth Network token surges after US Commerce Department puts data onchain (Cointelegraph, 28 August 2025)](https://cointelegraph.com/news/pyth-network-token-surges-us-commerce-onchain-data)
- [Pyth Network price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/pyth-network)
