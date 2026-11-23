---
title: Render(RENDER) 쉽게 정리: OTOY의 GPU 렌더링 네트워크, 약 6억 4,400만 개 한도, 2023년 솔라나 이전
description: Render(렌더)를 쉽게 설명합니다: 창작자가 렌더링·AI 작업 대가를 GPU 소유자에게 내는 방식, 소각·발행 모델, 솔라나 이전, 경쟁자, 주요 위험.
date: 2026-11-23
kind: analysis
---
**Render(렌더)**는 컴퓨팅 파워를 사고파는 시장입니다. 아티스트, 스튜디오, AI 개발자가 다른 사람의 그래픽카드(GPU)를 빌려 쓰는 대가를 내고, GPU 소유자는 RENDER 토큰으로 보상을 받습니다. 줄스 어바크(Jules Urbach)가 이끄는 로스앤젤레스의 그래픽 소프트웨어 회사 OTOY에서 출발했으며, 'AI·컴퓨팅' 토큰 가운데 가장 잘 알려진 것 중 하나입니다. 현재 시가총액은 {{mcap:render}}(암호화폐 중 {{rank:render}})입니다.

> **핵심 요약**
> - 공급 한도는 약 6억 4,400만 RENDER이며, 2026년 11월 기준 그중 약 86%가 유통되고 있었습니다.
> - 2023년 12월부터 네트워크는 '소각·발행(burn-and-mint)' 모델로 움직입니다. 작업 대금으로 쓰인 토큰은 소각되고, GPU 제공자를 위해 새 토큰이 발행됩니다.
> - 2023년 11월 토큰은 이더리움(티커 RNDR)에서 솔라나(티커 RENDER)로 옮겨 갔습니다.
> - 사상 최고가는 {{ath:render}}({{athd:render}})이며, 현재 가격은 그보다 {{fromath:render}} 수준입니다.

## 작동 원리

렌더링은 3D 장면을 완성된 이미지나 영상 프레임으로 바꾸는 작업으로, 많은 GPU 성능이 필요합니다. 창작자는 비싼 장비를 사는 대신 작업을 Render 네트워크에 보냅니다. 놀고 있는 GPU를 가진 독립 '노드 운영자'들이 주로 OTOY의 OctaneRender 소프트웨어로 작업을 처리하고, 결과가 확인되면 보상을 받습니다. 2025년부터는 Dispersed라는 플랫폼 등을 통해 AI와 일반 GPU 연산으로도 영역을 넓히고 있습니다. 규칙은 토큰 보유자가 투표하는 공개 제안 'Render Network Proposals(RNP)'로 바뀌며, 2023년 OTOY에서 분리된 Render Network Foundation이 거버넌스를 감독합니다.

## 토큰의 쓰임새

작업 가격은 일반 화폐 기준으로 정해집니다. 'Burn-and-Mint Equilibrium'(RNP-001)에 따라 창작자는 RENDER로 지불하고, 작업이 끝나면 그 토큰은 소각되어 유통에서 사라집니다. 네트워크는 에포크(약 1주)마다 정해진 감소 일정에 따라 새 RENDER를 발행해 노드 운영자와 다른 기여자들에게 나눠 줍니다. 실제 수요로 소각되는 양이 발행량보다 많으면 공급이 줄고, 수요가 약하면 늘어납니다. RENDER는 제안 투표에도 쓰입니다.

## 지금의 숫자

- 현재 가격: {{price:render}}
- 사상 최고가: {{ath:render}}({{athd:render}}), 최고가 대비 {{fromath:render}}
- 시가총액: {{mcap:render}}(암호화폐 중 {{rank:render}})
- 12개월 가격 변화: {{chg1y:render}}
- 1년간 매일 10달러: 투자금 {{dcainv:1}}이 {{dca:render:1}}로 ({{dcaroi:render:1}})

## 지금까지의 이야기

어바크는 2009년에 이 구상을 처음 밝혔습니다. 토큰 공개 판매는 2017년 10월, 비공개 판매는 2018년 1~5월에 진행됐고, 2020년 4월 27일 네트워크가 모두에게 열렸습니다. 2023년 인공지능이 시장의 최대 관심사가 되자 토큰 가격은 몇 배로 뛰었습니다. 보유자 투표로 솔라나 이전(RNP-002)이 결정돼 2023년 11월 2일 완료됐고, 소각·발행 모델에 따른 신규 발행은 2023년 12월에 시작됐습니다. 가격은 AI 붐이 한창이던 2024년 3월 정점을 찍었고, 2024년 동안 거래소들이 RNDR에서 RENDER로 전환했습니다. 2026년 11월에는 AI 관련 토큰이 함께 내리면서 Render가 일주일 새 약 12% 하락했습니다.

## 대안

다른 탈중앙 GPU·컴퓨팅 네트워크로는 [Akash]({lang}/akt/), [io.net]({lang}/io/), [Aethir]({lang}/ath/), [Golem]({lang}/glm/)이 있고, [Bittensor]({lang}/tao/)는 가장 큰 크립토·AI 프로젝트 중 하나입니다. 하지만 진짜 경쟁 상대는 Amazon Web Services, Google Cloud 같은 대형 클라우드입니다.

## 주요 위험

- **큰 변동성:** 소형 AI 토큰은 비트코인보다 훨씬 깊이 떨어질 수 있으며, 2024년 3월 정점 이후 Render는 가치의 대부분을 잃었습니다.
- **신규 발행:** 에포크마다 새 RENDER가 발행됩니다. 실제 작업으로 소각되는 토큰이 부족하면 공급은 계속 늘어납니다.
- **경쟁:** 대형 클라우드 기업은 엄청난 규모와 지원 체계로 GPU를 제공해, 탈중앙 네트워크가 따라가기 쉽지 않습니다.
- **의존성:** 네트워크는 OTOY의 소프트웨어와 솔라나 블록체인에 크게 기대고 있어, 어느 한쪽에 문제가 생기면 타격을 받습니다.
- **규제:** 암호화폐 규칙은 나라마다 다르고 빠르게 바뀔 수 있으며, RENDER 같은 토큰을 어떻게 분류하느냐도 여기에 포함됩니다.

## 적립식으로 산다면

RENDER 가격은 급등과 깊은 하락을 겪었고, AI를 둘러싼 시장 분위기를 따라 움직여 왔습니다. 일정 금액을 꾸준히 사면 가격이 낮을 때 더 많이, 높을 때 더 적게 사게 되어 바닥을 맞히려 애쓸 필요가 없습니다. 하지만 손실 위험이 사라지지는 않습니다. 많은 사람이 RENDER 같은 토큰을 크게 떨어져도 감당할 수 있는 저축의 작은 일부로만 둡니다. 과거 성과가 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [Render Network — official site (rendernetwork.com)](https://rendernetwork.com/)
- [Render Network Knowledge Base: history and Burn Mint Equilibrium (know.rendernetwork.com)](https://know.rendernetwork.com/basics/burn-mint-equilibrium)
- [RNP-001: Burn-and-Mint Equilibrium (Render Network proposals, GitHub)](https://github.com/rendernetwork/RNPs/blob/main/RNP-001.md)
- [Render price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/render-token)
