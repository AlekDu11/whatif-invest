---
title: Stacks(STX) 쉽게 정리: 비트코인에 스마트 계약을 더한 네트워크, 2021년부터 가동, 보상은 BTC로 지급
description: Stacks를 쉽게 설명합니다: 비트코인 레이어의 작동 방식, Proof of Transfer, BTC를 받는 스태킹, sBTC, 지금까지의 이야기, 주요 위험, 적립식으로 사는 사람이 알아야 할 점.
date: 2026-11-24
kind: analysis
---
**Stacks**는 비트코인 위에 세워진 블록체인으로, 비트코인 자체에는 없는 스마트 계약과 대출, 거래, NFT 같은 앱을 더해 줍니다. 거래 기록은 비트코인 블록체인에 고정(앵커링)되며, STX 토큰의 시가총액은 현재 {{mcap:stx-token}}(암호화폐 중 {{rank:stx-token}})입니다. 지갑에 그냥 묵혀 두는 비트코인을 "더 쓸모 있게" 만드는 가장 오래되고 큰 방법 가운데 하나로 주목받고 있습니다.

> **핵심 요약**
> - Stacks 채굴자는 실제 비트코인을 내고 새 STX를 얻으며, STX를 묶어 둔 보유자는 그 비트코인을 받을 수 있습니다.
> - 2019년 개발사 Blockstack은 미국 SEC(증권거래위원회)가 Regulation A+에 따라 승인한 첫 토큰 판매를 진행했습니다.
> - 사상 최고가는 {{ath:stx-token}}({{athd:stx-token}})이며, 현재 가격은 그보다 {{fromath:stx-token}} 수준입니다.
> - 2024년 10월 Nakamoto 업그레이드 이후 블록은 몇 초 만에 만들어지고, 확정된 거래는 비트코인 자체만큼 되돌리기 어렵습니다.

## 작동 원리

Stacks는 Proof of Transfer(PoX)라는 방식을 씁니다. 비트코인 채굴자처럼 전기를 태우는 대신, Stacks 채굴자는 비트코인을 보내 다음 Stacks 블록을 쓸 권리에 입찰하고 새로 발행되는 STX를 받습니다. 그 비트코인은 사라지지 않습니다. STX를 정해진 주기(한 주기는 약 2주) 동안 묶어 두고 네트워크 보안을 돕는 '스태킹' 참여자에게 돌아갑니다. 모든 Stacks 블록은 비트코인에 기록되므로, Stacks의 기록을 고쳐 쓰려면 비트코인의 기록을 고쳐 써야 합니다. 앱은 Clarity로 작성됩니다. Clarity는 동작을 예측하기 쉽고 검증하기 쉽도록 설계된 프로그래밍 언어이며, 비트코인 체인에서 일어나는 일을 읽을 수도 있습니다.

## 사람들이 가치가 있다고 보는 이유

STX는 Stacks에서 거래 수수료를 내는 데 필요하고, 채굴자가 받는 보상이며, 묶어 두면 BTC 보상을 받는 수단이 됩니다. 그래서 네트워크 수요가 곧바로 토큰 수요로 이어집니다. 더 큰 그림은 '비트코인 디파이(DeFi)'입니다. 대부분의 비트코인은 쓰이지 않고 잠들어 있는데, Stacks는 비트코인 세계를 떠나지 않고도 이를 앱에서 활용할 길을 제공합니다. 이를 위한 핵심 도구가 sBTC입니다. 비트코인으로 1:1 뒷받침되는 토큰으로, Stacks 앱으로 옮겨 쓰다가 다시 BTC로 돌려받을 수 있습니다.

## 지금의 숫자

- 현재 가격: {{price:stx-token}}
- 사상 최고가: {{ath:stx-token}}({{athd:stx-token}}), 최고가 대비 {{fromath:stx-token}}
- 시가총액: {{mcap:stx-token}}(암호화폐 중 {{rank:stx-token}})
- 12개월 가격 변화: {{chg1y:stx-token}}
- 5년간 매일 10달러: 투자금 {{dcainv:5}}이 {{dca:stx-token:5}}로 ({{dcaroi:stx-token:5}})

## 지금까지의 이야기

Muneeb Ali와 Ryan Shea는 Princeton에서 만난 뒤 2013년 Blockstack을 시작했습니다. 2017년 프로젝트는 투자자들에게 토큰을 판매했고, 2019년 7월에는 SEC가 승인한 Regulation A+ 방식으로 일반 대중에게 토큰을 판매한 첫 기업이 됐습니다. 2021년 1월 Proof of Transfer와 Clarity를 갖춘 Stacks 2.0 메인넷이 가동됐고, 그해 가격은 약 0.40달러에서 2달러 이상으로 올랐습니다. 2022년 말에는 약 0.20달러까지 떨어졌다가 비트코인 'Ordinals' 열풍을 타고 반등해 2024년 4월 1일 최고가를 기록했습니다. 이어 2024년 10월 Nakamoto 업그레이드, 2024년 12월 sBTC 입금, 2025년 4월 비트코인으로의 출금이 시작됐습니다. 그럼에도 가격은 2025년 내내 미끄러졌고, 2026년 대부분 기간 동안 0.40달러를 밑돌았습니다.

## 대안

비트코인에 앱을 가져오는 프로젝트 가운데 Rootstock은 비트코인 채굴자가 보안을 맡는 이더리움 호환 사이드체인을 운영하고, [Core]({lang}/core/)는 비트코인 스테이킹을 갖춘 별도의 체인이며, [Babylon]({lang}/baby/)은 비트코인을 스테이킹해 다른 네트워크의 보안을 돕게 합니다. 많은 비트코인 보유자는 그냥 [이더리움]({lang}/eth/) 위의 랩드 비트코인을 대신 씁니다. 그리고 비트코인 자체만 원한다면 [비트코인]({lang}/btc/)이 가장 확실한 대안입니다.

## 주요 위험

- **큰 변동성:** STX는 2022년 말까지 2021년 고점에서 90% 넘게 떨어졌고, 2024년 최고가 이후에도 비슷한 하락이 다시 나타났습니다.
- **신규 공급:** 채굴 보상으로 매일 새 STX가 생겨나 꾸준한 매도 압력이 될 수 있습니다.
- **경쟁:** 새로 등장한 여러 비트코인 레이어가 같은 사용자와 같은 비트코인을 두고 다툽니다.
- **기술:** sBTC는 비트코인을 보관하는 서명자 그룹에 의존합니다. 그곳에서 버그나 장애가 생기면 네트워크 전체에 대한 신뢰가 흔들릴 수 있습니다.
- **보관과 규제:** 거래소가 파산하거나 개인 키를 잃어버리면 코인을 잃을 수 있고, 암호화폐 규칙은 나라마다 다르며 빠르게 바뀔 수 있습니다.

## 적립식으로 산다면

Stacks 가격은 긴 파도를 그려 왔습니다. 2021년과 2024년 두 번의 큰 고점이 있었고, 그때마다 깊은 하락이 뒤따랐습니다. 일정 금액을 정기적으로 사면 바닥을 맞히려 애쓰지 않아도 가격이 낮을 때 더 많이, 높을 때 더 적게 사게 됩니다. 하지만 위의 5년 결과가 보여 주듯 긴 하락에서 지켜 주지는 못합니다. 많은 사람이 STX 같은 작은 코인은 크게 떨어져도 견딜 수 있는 저축의 작은 일부로만 둡니다. 과거 성과가 미래 수익을 보장하지는 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Finally, Finality: the Nakamoto upgrade (Stacks Foundation)](https://stacks.org/nakamoto)
- [The sBTC mainnet release is live with Bitcoin deposits (Stacks blog)](https://www.stacks.co/blog/bitcoin-deposits-live)
- [sBTC withdrawal functionality is now live (Stacks blog)](https://www.stacks.co/blog/sbtc-withdrawals-live)
- [Stacks price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/stacks)
