---
title: LayerZero(ZRO) 쉽게 정리: 발행량 10억 개, 2024년 6월 에어드롭, 블록체인 간 메시징
description: LayerZero를 쉽게 설명합니다: 블록체인을 잇는 방식, 2024년 ZRO 에어드롭, 고정된 10억 개 공급량, 언락, 위험, 사는 사람이 알아야 할 점.
date: 2026-11-24
kind: analysis
---
**LayerZero**는 블록체인끼리 '대화'하게 해 주는 메시징 프로토콜입니다. 한 체인의 앱이 다른 체인의 앱으로 데이터, 명령, 토큰을 보낼 수 있습니다. 토큰 ZRO는 2024년 6월 20일 초기 사용자 대상 에어드롭과 함께 출시됐고, 현재 시가총액은 {{mcap:zro}}(암호화폐 중 {{rank:zro}})입니다. 사람들은 주로 LayerZero가 앞으로도 블록체인 사이의 핵심 '배관'으로 남고, 자체 신규 네트워크 Zero가 실제로 쓰일 것이라는 데 베팅하며 ZRO를 삽니다.

> **핵심 요약**
> - ZRO는 10억 개를 넘게 발행되지 않으며, 8.5%(8,500만 개)가 2024년 6월 20일 첫 에어드롭으로 사용자에게 배분됐습니다.
> - 사상 최고가는 {{ath:zro}}({{athd:zro}})이고, 현재 가격은 최고가 대비 {{fromath:zro}}입니다.
> - 투자자와 팀 몫(공급량의 57.7%)은 1년 잠금 후 2년 동안 매달 풀리기 때문에, 2027년 중반쯤까지 새 ZRO가 계속 시장에 나옵니다.
> - 2026년 4월 LayerZero 기반 브리지인 Kelp DAO의 rsETH가 공격을 받아 약 2억 9,200만 달러를 잃었습니다.

## 작동 원리

Ethereum, Solana, BNB Chain 같은 블록체인은 서로의 데이터를 직접 읽을 수 없습니다. LayerZero는 체인마다 endpoint라는 작고 변경할 수 없는 컨트랙트를 둡니다. 앱이 메시지를 보내면 DVN(탈중앙 검증자 네트워크)이라는 독립 검증자들이 받는 쪽에서 메시지가 실제로 보내졌는지 확인하고, executor가 이를 전달합니다. 어떤 DVN을 믿고 몇 곳이 동의해야 하는지는 앱마다 직접 정하므로, 보안 수준은 그 선택에 달려 있습니다. 그 위에는 OFT(Omnichain Fungible Token) 표준이 있습니다. 토큰을 한 체인에서 소각하거나 잠그고 다른 체인에서 발행하거나 풀어 주기 때문에 총공급량은 그대로입니다. LayerZero에 따르면 OFT로 160개 이상의 블록체인에서 2,900억 달러가 넘는 전송이 이뤄졌습니다. 스테이블코인과 ETH를 옮기는 브리지 Stargate가 그 위에 만들어진 첫 대형 앱입니다.

## 사람들이 가치가 있다고 보는 이유

ZRO는 거버넌스 토큰으로, 보유자는 프로토콜 운영 방식에 투표합니다. 가장 주목받는 쟁점은 'fee switch'입니다. LayerZero 메시지마다 작은 수수료를 붙여 이를 ZRO로 바꾼 뒤 소각해 공급량을 줄이는 방안입니다. 보유자들은 2024년 12월부터 1년에 두 번 이 안건에 투표해 왔고, 가장 최근인 2026년 6월을 포함해 지금까지 모든 투표에서 수수료는 꺼진 상태로 유지됐습니다. 2026년에는 ZRO의 역할도 커졌습니다. LayerZero가 자체 블록체인 Zero를 발표했는데, 여기서 ZRO는 가스비, 네트워크를 지키는 스테이킹 토큰, 그리고 거래 엔진 ATLAS 거래 수수료의 75%(거래소 리베이트 차감 후)로 되사서 소각하는 자산이 될 예정입니다.

## 지금의 숫자

- 현재 가격: {{price:zro}}
- 사상 최고가: {{ath:zro}}({{athd:zro}}), 최고가 대비 {{fromath:zro}}
- 시가총액: {{mcap:zro}}(암호화폐 중 {{rank:zro}})
- 12개월 가격 변화: {{chg1y:zro}}
- 1년간 매일 10달러: 투자금 {{dcainv:1}}이 {{dca:zro:1}}로 ({{dcaroi:zro:1}})

## 지금까지의 이야기

LayerZero Labs는 Bryan Pellegrino(CEO), Ryan Zarick(CTO), Caleb Banister가 세웠습니다. 2022년 3월 Stargate가 가동됐고, 같은 달 회사는 Sequoia, a16z, FTX Ventures 등 투자자로부터 기업가치 10억 달러로 1억 3,500만 달러를 유치했습니다. 2023년 4월에는 1억 2,000만 달러 규모의 추가 투자로 기업가치가 30억 달러가 됐습니다. 토큰 출시 전 팀은 여러 지갑으로 에어드롭을 쓸어 담는 '파머'를 걸러 내는 공개 'sybil hunt'를 벌였고, 약 128만 개 지갑이 자격을 얻었습니다. 수령(클레임)은 2024년 6월 20일 'proof of donation'이라는 독특한 조건과 함께 시작됐습니다. 받으려면 이더리움 개발자 기금인 Protocol Guild에 ZRO 1개당 0.10달러를 기부해야 했습니다. 많은 사용자가 반발했고, 가격은 출시 당시 약 4.40달러에서 첫 며칠 동안 떨어졌습니다. ZRO는 2024년 12월 최고가를 기록했습니다. 2025년 8월 Stargate DAO는 Wormhole의 경쟁 제안에도 불구하고 약 95% 찬성으로, ZRO 약 1억 2,000만 달러어치(STG 1개당 0.08634 ZRO)에 LayerZero에 인수되는 안을 통과시켰습니다. 2026년 2월 LayerZero는 Citadel Securities, DTCC, ICE, ARK Invest가 지원하는 금융시장용 블록체인 Zero를 발표했고, 2026년 10월 Zero 메인넷과 ATLAS의 출시 예정일을 2026년 11월 30일로 정했습니다.

## 대안

크로스체인 메시징에서 LayerZero는 [Wormhole]({lang}/w/), CCIP 서비스를 가진 [Chainlink]({lang}/link/), [Axelar]({lang}/axl/)와 경쟁합니다. 단순히 체인 간에 토큰을 옮기려는 사용자는 [Across]({lang}/acx/) 같은 브리지도 고릅니다. [Stargate]({lang}/stg/)는 LayerZero 자체 브리지 앱으로, 지금은 프로토콜이 소유하고 있습니다.

## 주요 위험

- **큰 변동성:** ZRO는 최고가보다 한참 낮은 수준에서 오래 머문 적이 많고, 소형 코인은 비트코인보다 훨씬 빠르게 떨어질 수 있습니다.
- **언락:** 투자자와 팀은 2027년 중반쯤까지 매달 새 토큰을 받습니다. 이들이 팔면 가격에 부담이 될 수 있습니다.
- **해킹:** 크로스체인 브리지는 암호화폐에서 가장 많이 공격받는 분야 중 하나입니다. 2026년 4월 DVN을 하나만 설정했던 Kelp DAO의 rsETH 브리지가 약 2억 9,200만 달러를 잃었습니다. LayerZero는 북한 Lazarus 그룹과 검증자 하나뿐인 설정을 원인으로 지목했고, 이후 일부 프로젝트는 Chainlink로 옮겨 갔습니다.
- **경쟁:** Chainlink, Wormhole, Axelar가 같은 앱을 두고 다투며, 앱은 갈아탈 수 있습니다.
- **가치 포착:** fee switch는 아직 꺼져 있고 Zero와 ATLAS는 새롭습니다. 이들이 쓰이지 않으면 ZRO 수요는 제한적으로 남습니다.

## 적립식으로 산다면

ZRO의 짧은 역사는 과열된 에어드롭, 초반 급락, 2024년 말 최고가, 그리고 급반등이 섞인 긴 하락의 연속이었습니다. 일정 금액을 꾸준히 사면 한 시점에 베팅하는 대신 매수 가격을 시간에 걸쳐 나눌 수 있습니다. 하지만 아직 젊은 코인이고 매달 언락도 있어, 그래도 돈의 큰 부분을 잃을 수 있습니다. 많은 사람이 이런 코인은 암호화폐 자산의 아주 작은 부분으로만 두고, 암호화폐 자체도 저축의 작은 부분으로 제한합니다. 과거 성과가 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [LayerZero V2 overview — LayerZero docs](https://docs.layerzero.network/v2/home/v2-overview)
- [LayerZero Foundation to begin ZRO token airdrop claims today (The Block, 2024년 6월 20일)](https://www.theblock.co/post/300951/layerzero-foundation-to-begin-zro-token-airdrop-claims-today)
- [LayerZero's proof-of-donation claiming mechanism (The Block, 2024년 6월)](https://www.theblock.co/post/301043/layerzero-proof-of-donation-zro-claiming-mechanism)
- [Fee switch referendums — LayerZero Foundation](https://layerzero.foundation/fee-switch)
- [Stargate DAO approves LayerZero acquisition (The Block, 2025년 8월 24일)](https://www.theblock.co/post/368040/stargate-dao-approves-layerzero-acquisition-despite-last-minute-interest-from-wormhole-axelar-and-across)
- [LayerZero says Lazarus likely behind Kelp DAO exploit (The Block, 2026년 4월 20일)](https://www.theblock.co/post/398028/layerzero-kelp-dao-lazarus)
- [ZRO surges as LayerZero unveils ATLAS on Zero (The Block, 2026년 8월 25일)](https://theblock.co/news/ecosystems/2026-08-25-zro-token-layerzero-atlas-exchange-infrastructure-zero-blockchain-412736)
- [LayerZero sets November 30 launch for Zero mainnet and ATLAS (crypto.news, 2026년 10월)](https://crypto.news/layerzero-zero-mainnet-atlas-november-30-launch/)
- [LayerZero Labs raises $135 million (Business Wire, 2022년 3월 30일)](https://www.businesswire.com/news/home/20220330005301/en/LayerZero-Labs-Raises-135-Million-to-Create-Omnichain-Crypto-Networks)
