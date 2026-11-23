---
title: Binance Wallet 만드는 법과 밈코인 사는 법: 단계별 안내
description: Binance 앱에서 Binance Wallet을 만들고 백업하고, Binance 계정에서 코인을 옮기고, 컨트랙트로 토큰을 찾아 스왑하는 법과 안전 점검.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: Binance Wallet을 지키는 키 조각 수. 들어가려면 2개가 필요
---
**Binance Wallet은 어떻게 만들까요?** Binance 앱을 열고 화면 위쪽에서 **Wallet**(지갑) 탭으로 바꾼 뒤 **Create Keyless Wallet**(키리스 지갑 만들기)을 누르고, 복구 비밀번호로 백업합니다. 몇 분이면 끝나고 시드 문구도 필요 없습니다. 그러면 밈코인 같은 온체인 토큰을 살 수 있는 자기 보관 지갑(거래소가 아니라 내가 코인을 관리하는 지갑)이 생깁니다.

> **핵심 정리**
> - Binance Wallet은 Binance 앱 안에 있습니다. 인증된 Binance 계정이 필요하지만, 지갑 속 코인은 자기 보관입니다. 백업은 내 책임입니다.
> - "키리스"(MPC) 지갑입니다. 키가 3조각으로 나뉘어 휴대폰, 내 클라우드 백업, Binance에 있습니다. 그중 아무 2개로 지갑을 열 수 있습니다.
> - 백업은 절대 건너뛰지 마세요. 휴대폰을 잃어버리고 **동시에** 복구 비밀번호도 잊으면 Binance도 지갑을 되살릴 수 없습니다.

시작하기 전에: 새 밈코인 대부분은 가치를 거의 다 잃습니다. 전부 잃어도 괜찮은 돈만 쓰세요. [밈코인이란]({lang}/blog/what-are-memecoins/)도 읽어 보세요.

## 준비물

- 공식 Binance 앱이 깔린 휴대폰(App Store, Google Play, binance.com에서만 받으세요. 가짜 앱이 흔합니다).
- 신원 인증(KYC: 신분증 제출)을 마친 Binance 계정. 아직 없다면 저희 링크로 가입할 수 있습니다: [Binance Wallet](/go/binance-web3?from=learn&l=ko).
- 매수와 네트워크 수수료에 쓸 약간의 BNB나 SOL(Binance 계정 안에).

## 1단계: 지갑 열기

1. Binance 앱에 로그인합니다.
2. 화면 위쪽에서 **Exchange**(거래소)를 **Wallet**으로 바꿉니다.
3. **Create Keyless Wallet**을 누릅니다. (이미 다른 지갑이 있다면 다른 선택지는 **Import Wallet**(지갑 가져오기)인데, 초보자에게는 필요 없습니다.)

만드는 데 몇 초면 됩니다. 앱은 12개나 24개의 시드 단어를 보여 주지 않습니다. 대신 MPC(다자간 계산: 키를 조각으로 나눠 한곳에 모이지 않게 하는 방식)를 씁니다.

## 2단계: 백업하기(건너뛰지 마세요)

앱은 백업 조각을 저장하는 방법 세 가지를 제공합니다. 하나를 고르세요:

- **iCloud** 또는 **Google Drive**. 나만 아는 **복구 비밀번호**를 정합니다. 조각은 그 비밀번호로 암호화되어 내 클라우드에 저장됩니다.
- **QR 코드.** 복구 비밀번호를 정하고 QR 코드를 저장합니다. 조각은 탈중앙화 클라우드에 보관됩니다.
- **Quick Backup**(빠른 백업). Face ID나 지문으로 확인합니다. 비밀번호는 없지만, 조각은 외부 업체가 보관합니다.

복구 비밀번호는 종이에 적어 안전한 곳에 두세요. 그다음 확인합니다: **Settings**(설정, 홈이나 자산 화면 왼쪽 위) → **Wallet Management**(지갑 관리). **Backed Up**(백업 완료) 표시가 보이면 됩니다.

## 3단계: Binance에서 지갑으로 코인 옮기기

1. 지갑에서 **Receive**(받기) → **Withdraw from Binance Exchange**(Binance 거래소에서 출금)를 누릅니다.
2. 코인(예: BNB)**과 네트워크**를 고릅니다(BNB는 BNB Smart Chain, SOL은 Solana). 네트워크가 꼭 맞아야 합니다.
3. 금액을 입력합니다. 확정하기 전에 앱이 수수료와 최종 금액을 보여 줍니다.
4. 돈을 현물(Spot) 계정에서 뺄지 펀딩(Funding) 계정에서 뺄지 고르고, **Withdraw**(출금)를 누른 뒤 주소와 네트워크를 확인하고 **Confirm**(확인)을 누릅니다.

처음에는 소액으로 테스트하세요. 확정된 전송은 취소할 수 없습니다. 지갑에는 항상 BNB나 SOL을 조금 남겨 두세요. 블록체인에서 하는 모든 일에는 실패하더라도 네트워크 수수료(가스비)가 듭니다.

## 4단계: 컨트랙트 주소로 맞는 토큰 찾기

많은 밈코인에는 이름과 로고가 똑같은 복제품이 있습니다. 확실한 신분증은 **컨트랙트 주소**(토큰마다 다른, 글자와 숫자로 된 긴 문자열)뿐입니다.

1. 믿을 만한 곳에서 주소를 얻으세요: 프로젝트의 인증 계정, 큰 데이터 사이트, 또는 저희 [밈코인 페이지]({lang}/memes/)의 토큰 페이지.
2. 지갑의 **Markets**(마켓)이나 **Trade**(거래) 화면에서 이름을 치는 대신 주소를 검색창에 붙여 넣으세요.
3. 앞뒤 4~6글자를 출처와 비교하세요.

## 5단계: 사기 전에 토큰 점검하기

저희 [밈코인 페이지]({lang}/memes/)의 각 토큰 페이지에는 Binance 보안 점검과 주요 숫자가 나옵니다. 이것들을 보세요:

- **유동성**: 거래 풀에 있는 돈의 양. 유동성이 적다 = 팔지 못할 수도 있습니다.
- **보유자 수와 상위 10곳 비중**: 지갑 몇 개가 물량 대부분을 가졌다면 가격을 무너뜨릴 수 있습니다.
- **생성 시점**: 한 시간 전에 만들어진 토큰은 복권과 같습니다.
- **경고**: 위험이나 보안 경고가 하나라도 보이면 멈추세요.

Binance 스스로도 Meme Rush(갓 나온 밈코인 목록)에 올라온 토큰은 점검하지 않는다고 말합니다. 점검은 내 몫입니다. 경고 신호는 [사기와 러그풀 강의]({lang}/blog/memecoin-scams-rug-pull/)에 정리해 두었습니다.

## 6단계: 스왑하기

1. **Trade** → **Swap**(스왑)을 엽니다. 같은 네트워크에서 낼 것(BNB)과 원하는 토큰을 고릅니다.
2. 적은 금액을 입력합니다. 환율, **슬리피지**(거래가 실패하기 전까지 받아들이는 최대 가격 변화), 네트워크 수수료를 읽어 보세요.
3. 어떤 토큰은 먼저 **Approve**(승인) 단계가 필요합니다. 약간의 수수료가 듭니다.
4. **Swap**을 누르고 패스키나 2단계 인증으로 확인합니다.

팔 때는 반대로 하면 됩니다. 가장 새로운 토큰을 보고 싶다면 Markets 탭에 **Meme Rush**가 있습니다. 갓 나온 토큰은 그곳에서 "본딩 커브"로 거래되며, 일반 DEX(탈중앙화 거래소)로 "이전"하기 전까지는 지갑 밖으로 옮길 수 없습니다. 시장에서 가장 위험한 구석입니다.

> **⚠️ 주의**
> - **백업이 없거나 비밀번호를 스크린샷으로 저장.** 휴대폰과 비밀번호를 모두 잃으면 코인은 영영 사라집니다.
> - **잘못된 네트워크나 주소.** Binance FAQ에 따르면 잘못된 주소로 보낸 토큰은 환불되지 않습니다. 항상 테스트 금액을 먼저 보내세요.
> - **가짜 토큰과 "고객 지원" 메시지.** 검색은 컨트랙트 주소로만 하세요. Binance 직원은 절대 복구 비밀번호를 묻거나 웹사이트에서 지갑을 "인증"하라고 하지 않습니다.

다음 강의: Binance Wallet을 DEX 사이트에 연결하는 법과 코인을 다시 Binance로 옮기는 법. 모든 강의는 [배우기]({lang}/learn/)에서.

## 출처

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*투자 조언이 아닙니다. 밈코인은 매우 위험합니다. 이 안내는 앱 사용법을 설명할 뿐이며 어떤 토큰의 매수도 권하지 않습니다. Binance Wallet은 일부 국가에서 이용하지 못할 수 있습니다.*
