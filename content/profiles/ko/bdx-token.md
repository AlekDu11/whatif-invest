---
title: Beldex(BDX) 쉽게 정리: 2018년 Monero 포크, 1만 BDX 마스터노드, 프라이버시 앱
description: Beldex 쉽게 정리: Monero에서 갈라진 프라이버시 코인, 2021년부터 지분증명, BChat과 BelNet, 약 99억 개 공급량, 주요 위험과 적립식 매수자가 알아야 할 점.
date: 2026-11-24
kind: analysis
---
**Beldex(BDX)**는 프라이버시에 초점을 맞춘 암호화폐로, 블록체인에서 이뤄지는 결제가 보내는 사람·받는 사람·금액을 모두 숨깁니다. 2018년 3월 Monero에서 갈라져 나온('포크') 코드로 출발했고, 이후 메신저, 탈중앙화 VPN, 브라우저 같은 프라이버시 앱을 같은 네트워크에서 운영하는 프로젝트로 커졌습니다. 현재 시가총액은 {{mcap:bdx-token}}(암호화폐 중 {{rank:bdx-token}})입니다.

> **핵심 요약**
> - Beldex는 2021년 12월 채굴에서 지분증명(proof of stake)으로 전환했으며, 마스터노드를 운영하려면 1만 BDX를 잠가야 합니다.
> - BDX는 약 99억 개가 존재하지만 데이터 사이트는 약 79억 개만 유통량으로 집계해, 약 5분의 1의 차이가 있습니다.
> - 최고가는 {{ath:bdx-token}}({{athd:bdx-token}})이며, 현재 가격은 그보다 {{fromath:bdx-token}} 수준입니다.
> - 다른 프라이버시 코인처럼 대형 거래소 상당수에 상장돼 있지 않고 상장폐지 위험이 있습니다.

## 작동 원리

Beldex는 Monero 코드의 포크로 시작해 Monero식 프라이버시를 물려받았습니다. 링 서명이 내 결제를 다른 결제와 섞고, 한 번만 쓰는 '스텔스' 주소가 받는 사람을 숨기며, 금액도 감춰집니다. 처음에는 작업증명(proof of work) 채굴로 운영됐습니다. 2021년 12월 'Bucephalus' 하드포크로 지분증명으로 바뀌었고, 지금은 마스터노드가 네트워크를 지킵니다. 마스터노드는 소유자가 담보로 1만 BDX를 잠근 서버입니다. 그 대가로 블록 보상을 받고, 마스터노드 그룹이 돌아가며 블록을 만들고 검증합니다. 같은 업그레이드로 블록 생성 시간이 120초에서 30초로 줄었습니다. 거래 수수료의 일부는 소각돼 공급량에서 빠집니다.

## BDX는 어디에 쓰이나

BDX는 비공개 송금의 수수료로 쓰이며, 마스터노드가 잠가야 하는 담보이기도 합니다. 마스터노드는 프로젝트의 앱도 떠받칩니다. 메시지를 마스터노드가 전달하는 종단간 암호화 메신저 **BChat**, 트래픽을 마스터노드로 우회시키는 탈중앙화 VPN **BelNet**, VPN이 내장되고 추적기를 차단하는 **Beldex Browser**, 긴 주소를 읽기 쉬운 이름으로 바꿔 주는 **Beldex Name Service(BNS)**가 있습니다. 브리지를 이용하면 BDX를 '래핑' 토큰 형태로 BNB Chain 같은 다른 네트워크로 옮길 수 있습니다.

## 지금의 숫자

- 현재 가격: {{price:bdx-token}}
- 최고가: {{ath:bdx-token}}({{athd:bdx-token}}), 그보다 {{fromath:bdx-token}}
- 시가총액: {{mcap:bdx-token}}(암호화폐 중 {{rank:bdx-token}})
- 12개월 가격 변화: {{chg1y:bdx-token}}
- 3년간 매일 10달러: 투자금 {{dcainv:3}}이 {{dca:bdx-token:3}}로 ({{dcaroi:bdx-token:3}})

## 지금까지의 이야기

Beldex는 그해 봄 발표된 토큰 판매(ICO)를 거쳐 2018년 3월 출범했습니다. 프로젝트를 운영하는 Beldex International은 세이셸을 거점으로, Afanddy Bin Hushni를 창업자 겸 회장으로 밝히고 있습니다. 초기의 BDX는 채굴로 발행되는 작은 Monero 포크였고, 2019년 11월에는 1센트에 한참 못 미치는 가격에 거래됐습니다. 2021년 12월 지분증명 전환으로 마스터노드 네트워크가 됐고, 그 뒤 프로젝트는 '비공개 화폐'에서 BChat, BelNet, 브라우저를 중심으로 한 프라이버시 생태계 전체로 무게중심을 옮겼습니다. BDX는 BNB Chain의 래핑 토큰을 새 컨트랙트로 1:1 교환하는 작업도 마쳤습니다. 2026년 9월 Phemex의 분석에 따르면 체인에는 약 99.4억 BDX가 있었고, 그중 약 1,180만 개가 소각된 상태였습니다.

## 대안

가장 잘 알려진 프라이버시 코인은 Beldex의 뿌리인 [Monero]({lang}/xmr/)로, 규모가 훨씬 크고 여전히 채굴로 발행됩니다. [Zcash]({lang}/zec/)는 영지식 증명을 이용한 선택적 프라이버시를 제공하고, [Dash]({lang}/dash-token/)도 마스터노드를 쓰지만 믹싱이 더 약하고 선택 사항입니다. 암호화폐 밖에서는 Beldex의 앱이 일반 VPN 서비스, 그리고 많은 사람이 이미 무료로 쓰는 암호화 메신저와 경쟁합니다.

## 주요 위험

- **상장폐지:** 규제 당국이 거래소에 프라이버시 코인을 내리라고 압박하고 있으며, 여러 대형 거래소가 이미 Monero 같은 코인을 상장폐지했습니다. BDX는 주로 Gate, MEXC, KuCoin 같은 중형 거래소에서 거래됩니다.
- **공급량 투명성:** 총공급량은 약 99억 BDX이지만 약 20억 개는 유통량으로 잡히지 않으며, 누가 보유하고 있는지 프로젝트가 명확히 설명하지 않았습니다.
- **집중:** 토큰 배분에서 생태계 개발(40%), 시드 투자자, 팀에 큰 몫이 돌아갔습니다. 소수 집단의 결정이 가격을 움직일 수 있습니다.
- **작은 네트워크:** 2025년 2월 Coin Bureau 리뷰에 따르면 마스터노드에 잠긴 BDX는 일부에 불과해, 큰 블록체인보다 공격에 취약합니다.
- **얇은 거래와 헷갈리는 종목:** 하루 거래량이 시가총액에 비해 작고, 비슷한 티커(BDXN 등)나 비공식 래핑 토큰이 매수자를 헷갈리게 할 수 있습니다.

## 적립식으로 산다면

BDX는 거래가 얇은 소형 코인이라 가격 변동이 크고, 살 수 있는지도 몇몇 거래소에 달려 있습니다. 일정 금액을 꾸준히 사면 바닥을 맞히려 애쓰지 않고 매수 시점을 나눌 수 있지만, 손실 위험도, 거래소가 상장폐지할 위험도 사라지지 않습니다. 많은 사람이 이런 소형 프라이버시 코인은 잃어도 감당할 수 있는 저축의 아주 작은 부분으로만 제한합니다. 과거 성과가 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Beldex price, supply and project information (CoinMarketCap)](https://coinmarketcap.com/currencies/beldex/)
- [Beldex review: proof of stake, masternodes, BChat and BelNet (Coin Bureau, February 2025)](https://coinbureau.com/review/beldex-review)
- [Beldex POS chain launches with Bucephalus hard fork (press release via Nasdaq, 30 November 2021)](https://www.nasdaq.com/press-release/beldex-pos-chain-launches-with-bucephalus-hard-fork-2021-11-30)
- [What is Beldex and why 2 billion BDX are unlisted (Phemex, 2026)](https://phemex.com/blogs/what-is-beldex-and-why-2-billion-bdx-are-unlisted)
- [Beldex price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/beldex)
