---
title: Filecoin(FIL) 쉽게 정리: 발행 한도 20억 FIL, 2020년부터 가동된 탈중앙 저장 네트워크
description: Filecoin을 쉽게 설명합니다: 저장 비용을 FIL로 내는 방식, 발행 한도 20억 개, 급등과 긴 하락, 주요 위험, 적립식으로 사는 사람이 알아야 할 점.
date: 2026-11-24
kind: analysis
---
**Filecoin**은 누구나 남는 디스크 공간을 빌려줄 수 있고, 누구나 돈을 내고 파일을 저장할 수 있는 네트워크입니다. 결제와 보상에는 FIL 토큰이 쓰입니다. Juan Benet이 세우고 IPFS도 만든 Protocol Labs가 개발했으며, 메인넷은 2020년 10월 15일에 가동됐습니다. 현재 FIL의 시가총액은 {{mcap:fil-crypto}}(암호화폐 중 {{rank:fil-crypto}})입니다.

> **핵심 요약**
> - FIL은 20억 개를 넘게 발행되지 않으며, 그중 70%는 저장 공간 제공자에게 줄 보상으로 배정돼 있습니다.
> - 2017년 토큰 판매로 약 2억 5,700만 달러를 모았으며, 당시 최대 규모 가운데 하나였습니다.
> - 사상 최고가는 {{ath:fil-crypto}}({{athd:fil-crypto}})이며, 현재 가격은 그보다 {{fromath:fil-crypto}} 수준입니다.
> - 2023년 3월부터 Filecoin Virtual Machine으로 네트워크에서 스마트 계약을 실행할 수 있습니다.

## 작동 원리

저장 공간 제공자(작은 운영자부터 데이터센터 기업까지)가 디스크 공간을 내놓습니다. 고객은 정해진 기간 동안 데이터를 저장하는 계약을 맺고 FIL로 비용을 냅니다. 제공자는 수익을 얻기 전에 담보로 FIL을 묶어 둬야 합니다. 네트워크는 두 가지 암호학적 증명으로 일을 확인합니다. Proof-of-Replication(PoRep)은 제공자가 데이터의 고유한 사본을 저장했음을 보여 주고, Proof-of-Spacetime(PoSt)은 데이터가 여전히 그 자리에 있음을 거듭 증명합니다. 검사를 통과하지 못하면 담보의 일부를 잃습니다. 새 블록은 약 30초마다 추가되며, 증명된 저장 공간이 많은 제공자일수록 블록과 함께 새로 생기는 FIL을 받을 확률이 높습니다.

## 사람들이 가치가 있다고 보는 이유

저장 비용을 내고 담보를 맡기려면 FIL이 필요하므로, 네트워크 사용이 늘면 토큰 수요도 늘어날 수 있습니다. 데이터는 한 클라우드 회사에 의존하지 않고 전 세계의 독립적인 제공자들에게 나뉘어 저장되며, 누구나 공개 블록체인에서 증명을 확인할 수 있습니다. 수수료와 벌금의 일부는 소각돼 그만큼의 FIL이 영원히 유통에서 사라집니다. 지지자들은 Filecoin을 공공 데이터셋, 아카이브, AI 모델에 필요한 방대한 데이터를 위한 기반으로 봅니다.

## 지금의 숫자

- 현재 가격: {{price:fil-crypto}}
- 사상 최고가: {{ath:fil-crypto}}({{athd:fil-crypto}}), 최고가 대비 {{fromath:fil-crypto}}
- 시가총액: {{mcap:fil-crypto}}(암호화폐 중 {{rank:fil-crypto}})
- 12개월 가격 변화: {{chg1y:fil-crypto}}
- 5년간 매일 10달러: 투자금 {{dcainv:5}}이 {{dca:fil-crypto:5}}로 ({{dcaroi:fil-crypto:5}})

## 지금까지의 이야기

Juan Benet은 2014년 7월 첫 Filecoin 백서를 발표했고, 같은 해 Protocol Labs를 세웠습니다. 2017년 프로젝트는 공인 투자자만 참여할 수 있는 토큰 판매를 열었고, 5,200만 달러 규모의 사전 판매를 합쳐 약 2억 5,700만 달러를 모았습니다. 네트워크를 만드는 데는 3년이 더 걸렸고, 메인넷은 2020년 10월 15일 블록 148,888에서 시작됐습니다. 2021년 봄 암호화폐 호황 때 FIL은 최고가를 찍은 뒤 급락해, 2022년 말에는 3달러 안팎에서 거래됐습니다. 2023년 3월 14일 Filecoin Virtual Machine이 가동되면서 이더리움 도구와 호환되는 스마트 계약이 도입됐습니다. 이후에도 가격은 계속 미끄러져 2026년에는 1달러 아래로 내려갔습니다.

## 대안

암호화폐 저장 프로젝트 중 [Arweave]({lang}/ar-crypto/)는 한 번만 돈을 내면 데이터를 영구 보관하는 방식이고, [Storj]({lang}/storj/)와 [Siacoin]({lang}/sc/)도 남는 디스크 공간을 빌려줄 수 있습니다. 가장 큰 경쟁자는 Amazon, Google, Microsoft의 일반 클라우드입니다. 쉽고 싸며 이미 자리를 잡았습니다. 투자자의 돈을 두고는 [이더리움]({lang}/eth/) 같은 범용 플랫폼과도 경쟁합니다.

## 주요 위험

- **큰 변동성:** 2022년 말까지 FIL은 2021년 최고가에서 95% 넘게 떨어졌고, 깊은 하락은 다시 올 수 있습니다.
- **신규 공급:** 제공자 보상으로 매일 새 FIL이 생겨나 가격에 꾸준한 매도 압력이 될 수 있습니다.
- **실제 수요:** 토큰 가치는 돈을 내는 고객에 달려 있습니다. 일반 클라우드가 계속 더 싸고 편하다면 FIL 수요는 약할 수 있습니다.
- **경쟁:** 다른 저장 네트워크와 대형 클라우드 기업이 같은 고객을 두고 다툽니다.
- **보관과 규제:** 거래소가 파산하거나 개인 키를 잃어버리면 코인을 잃을 수 있고, 암호화폐 규칙은 나라마다 다르며 빠르게 바뀔 수 있습니다.

## 적립식으로 산다면

출시 이후 Filecoin의 역사는 초기의 고점과 그 뒤의 긴 하락입니다. 일정 금액을 정기적으로 사면 가격이 낮을 때 더 많이, 높을 때 더 적게 사게 되지만, 가격이 계속 떨어지는 자산을 구해 주지는 못합니다. 위의 5년 결과가 이를 보여 줍니다. 많은 사람이 FIL 같은 작은 코인은 크게 떨어져도 견딜 수 있는 저축의 작은 일부로만 둡니다. 과거 성과가 미래 수익을 보장하지는 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Filecoin mainnet liftoff (Filecoin blog, October 2020)](https://filecoin.io/blog/mainnet-liftoff/)
- [Token allocation — Filecoin specification](https://spec.filecoin.io/systems/filecoin_token/token_allocation/)
- [$257 Million: Filecoin Breaks All-Time Record for ICO Funding (CoinDesk, September 2017)](https://coindesk.com/markets/2017/09/07/257-million-filecoin-breaks-all-time-record-for-ico-funding/)
- [The FVM is live on mainnet (Filecoin blog, March 2023)](https://filecoin.io/blog/fvm-is-live-on-mainnet)
- [Filecoin price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/filecoin)
