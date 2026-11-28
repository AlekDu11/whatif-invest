---
title: 펄(PEARL) 쉽게 정리: GPU로 채굴하는 Proof of Useful Work, 최대 21억 개
description: 펄 쉽게 정리: GPU 채굴이 AI 연산과 어떻게 연결되는지, 최대 21억 개 공급, 2026년 4월 출시, 비판, 경쟁자, 주요 위험.
date: 2026-11-28
kind: analysis
---
**펄(Pearl)**은 엔비디아 그래픽카드로 채굴하는 새로운 레이어1 블록체인입니다. 비트코인 채굴자가 푸는 쓸모없는 해시 퍼즐 대신, 펄의 '유용한 작업 증명'(Proof of Useful Work)은 AI 모델을 돌리는 것과 같은 수학인 행렬 곱셈을 채굴자에게 시킵니다. 이론상 GPU 하나로 AI 고객 서비스와 네트워크 보안을 동시에 해낼 수 있다는 뜻입니다. 컴퓨터과학자 옴리 와인스타인이 공동 창업한 Pearl Research Labs가 만들었으며, 메인넷은 2026년 4월 27일에 시작됐습니다. 현재 시가총액은 {{mcap:pearl}}(암호화폐 중 {{rank:pearl}})입니다.

> **핵심 요약**
> - 코인은 최대 21억 개로, 비트코인 2,100만 개의 100배입니다. 채굴 보상은 반감기 없이 서서히 줄어듭니다.
> - 사상 최고가는 {{ath:pearl}}({{athd:pearl}})이며, 현재 가격은 그보다 {{fromath:pearl}} 수준입니다.
> - 프로젝트 측은 사전 채굴도, 투자자 배정도, 팀 금고도 없었다고 밝힙니다. 모든 코인은 채굴로만 나옵니다.
> - 2026년 6월 한 연구 논문은 당시 채굴이 쓸모 있는 AI 작업을 전혀 만들어 내지 못했다고 지적했습니다.

## 작동 원리

채굴자는 GPU에서 '노이즈를 섞은' 행렬 곱셈을 하고, 결과의 작은 조각을 해시한 뒤 작업을 영지식 증명으로 감쌉니다. 그래서 누구나 다시 계산하지 않고도 빠르게 검증할 수 있습니다. 이 방법은 와인스타인이 공동 저자로 참여한 2025년 암호학 논문에서 나왔습니다. 공식 채굴 프로그램은 AI 모델 구동에 널리 쓰이는 vLLM에 붙어 엔비디아 H100, H200 같은 데이터센터용 카드에서 돌아가고, 커뮤니티가 만든 채굴 프로그램은 게임용 RTX 카드에서도 작동합니다. 내부 구조는 비트코인과 비슷해서 비트코인 노드 프로그램인 btcd를 바탕으로 만들어졌고, 몇 분마다 새 블록이 생깁니다. 티커는 흔히 PRL로 표시되며, 일부 시세 사이트에서는 관계없는 다른 토큰이 같은 티커를 씁니다.

## 토큰의 쓰임새

코인은 채굴자 보상으로만 발행되며 거래 수수료를 내는 데 쓰입니다. 첫 상업 사례는 2026년 5월에 나왔습니다. AI 클라우드 기업 Together AI가 펄 채굴기에서 돌아가는 Gemma 모델을 평소보다 25% 넘게 싸게 내놓았고, 할인분은 PRL 보상으로 메웠습니다. AI 고객이 정말 이런 식으로 네트워크를 쓴다면 채굴은 단순한 전기 낭비가 아니게 됩니다. 그렇지 않다면 펄은 공급량이 많은 또 하나의 작업증명 코인일 뿐입니다.

## 지금의 숫자

- 현재 가격: {{price:pearl}}
- 사상 최고가: {{ath:pearl}}({{athd:pearl}}), 최고가 대비 {{fromath:pearl}}
- 시가총액: {{mcap:pearl}}(암호화폐 중 {{rank:pearl}})
- 12개월 가격 변화: {{chg1y:pearl}}

## 지금까지의 이야기

바탕이 된 논문은 2025년 4월에 공개됐고, 메인넷은 미리 나눠 준 코인 없이 2026년 4월 27일에 가동됐습니다. 5월 말 Together AI와의 제휴 이후 게이머와 GPU 보유자들이 몰려들었고, 경쟁이 치열해지면서 몇 주 만에 RTX 5090 한 대의 하루 수익은 절반가량으로 줄었습니다. 처음에는 MEXC처럼 유동성이 얇은 작은 거래소에서만 거래됐습니다. 2026년 6월 arXiv에 실린 논문 'The Usefulness Gap in Proof-of-Useful-Work'는 네트워크의 채굴자 수천 명이 유용한 AI 연산을 하지 않고 있으며, 가장 많이 쓰이는 채굴 프로그램에는 AI 코드조차 없다고 보고했습니다. 펄은 6월 하드포크로 mixture-of-experts 방식의 AI 모델을 지원하기 시작했고, 2026년 10월까지 최대 공급량의 약 16%가 채굴됐습니다.

## 대안

[비트코인]({lang}/btc/)은 GPU가 아닌 전용 칩으로 채굴하는 대표적인 작업증명 코인입니다. AI·컴퓨팅 프로젝트 가운데 [비트텐서(Bittensor)]({lang}/tao/)는 AI 모델을 돌리는 사람에게 보상하고, [렌더(Render)]({lang}/render/), [아카시 네트워크(Akash Network)]({lang}/akt/), [io.net]({lang}/io/)은 GPU 연산력을 직접 빌려줍니다. 펄의 발상은 다릅니다. 채굴 자체가 쓸모 있는 AI 작업이 되도록 하려는 것입니다.

## 주요 위험

- **아주 새로운 코인:** 가격 이력이 몇 달뿐이며, 신생 코인은 짧은 기간에 가치 대부분을 잃을 수 있습니다.
- **유용성 미입증:** 독립 연구자들은 지금까지 실제 AI 작업을 거의 찾지 못했습니다. 핵심 내세움이 성립하지 않을 수 있습니다.
- **채굴 수익성:** 난이도 상승과 보상 감소로 수익이 줄고, 채굴자는 전기요금을 내려고 코인을 파는 경우가 많습니다.
- **보유 집중:** 첫 몇 주는 싸게 채굴할 수 있었기 때문에 초기 참여자가 큰 몫을 갖고 있습니다.
- **유동성과 동명 토큰:** 대형 코인보다 거래가 얇고, 같은 PRL 티커를 쓰는 다른 토큰도 있습니다. 컨트랙트와 거래소를 꼼꼼히 확인하세요.

## 적립식으로 산다면

펄은 거래된 지 몇 달밖에 되지 않아 적립식으로 샀을 때의 의미 있는 기록이 아직 없습니다. 정해진 금액을 일정하게 사면 타이밍을 잘못 잡을 위험은 나눌 수 있지만, 갓 나온 코인이라면 돈 대부분을 잃을 위험까지 없애 주지는 못합니다. 많은 사람이 이런 실험적인 코인은 저축의 아주 작은 부분으로만 보유합니다. 과거 성과가 미래 수익을 보장하지 않습니다.

*투자 조언이 아닙니다.*

## 출처

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
