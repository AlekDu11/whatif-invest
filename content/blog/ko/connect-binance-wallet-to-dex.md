---
title: Binance Wallet을 DEX에 연결하고 코인을 되돌리는 법: 단계별 안내
description: Binance Wallet을 DEX 사이트에 안전하게 연결하고, 맞는 네트워크로 코인을 Binance 계정에 보내고, 오래된 승인을 지우는 법을 쉽게 알려 드립니다.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: 새 주소나 네트워크마다 먼저 보내는 소액 테스트 전송
---
**Binance Wallet은 DEX에 어떻게 연결할까요?** DEX의 공식 웹사이트를 열고 **Connect Wallet**(지갑 연결)을 누른 뒤 Binance Wallet을 고르거나(또는 WalletConnect를 고르고 Binance 앱으로 QR 코드를 스캔) 앱에서 확인합니다. 코인을 되돌릴 때는 같은 코인·같은 네트워크의 Binance **입금 주소**를 복사해 지갑에서 그 주소로 보냅니다. 먼저 소액으로 테스트하세요.

> **핵심 정리**
> - DEX(탈중앙화 거래소 — 내 지갑에서 바로 토큰을 바꾸는 웹사이트)는 복구 비밀번호나 시드 문구를 절대 요구하지 않습니다. 연결은 사이트가 서명을 *요청*할 수 있게 할 뿐이고, 내가 확인하기 전에는 아무것도 움직이지 않습니다.
> - 양쪽 네트워크가 같아야 합니다(BNB Smart Chain은 BNB Smart Chain으로, Solana는 Solana로). 네트워크나 주소가 틀리면 코인을 잃을 수 있습니다.
> - "Approve"(승인)를 할 때마다 사이트가 그 토큰을 대신 쓸 수 있게 됩니다. 승인은 작게 하고, 안 쓰는 승인은 지우세요.

이 수업은 [Binance Wallet 만드는 법]({lang}/blog/how-to-create-binance-wallet/)에 이어집니다. 밈코인은 매우 위험합니다. 잃어도 괜찮은 돈만 쓰세요.

## 1단계: 진짜 웹사이트 열기

로고까지 똑같은 가짜 DEX 사이트는 가장 흔한 함정 중 하나입니다.

1. 주소를 직접 입력하거나 즐겨찾기를 쓰세요. 검색 결과의 광고나 채팅방 링크는 누르지 마세요.
2. 주소창을 한 글자씩 확인하세요.
3. 그 DEX가 내 코인이 있는 네트워크를 지원하는지 확인하세요.

## 2단계: 지갑 연결하기

기기에 따라 세 가지 방법이 있습니다.

- **Binance Wallet 브라우저 확장 프로그램이 있는 컴퓨터**(Chrome 또는 Brave). Binance 앱으로 확장 프로그램의 QR 코드를 스캔해 로그인합니다. 그다음 DEX에서 **Connect** 또는 **Connect Wallet**을 누르고 Binance Wallet을 고른 뒤 팝업을 확인합니다.
- **확장 프로그램이 없는 컴퓨터.** DEX에서 **Connect Wallet → WalletConnect**를 누르면 QR 코드가 나옵니다. Binance 앱의 스캐너로 스캔하고 **Connect**를 누릅니다.
- **휴대폰.** 휴대폰 브라우저에서 DEX를 열고 **Connect Wallet**을 누른 뒤 목록에서 Binance Wallet을 고르고 앱에서 확인합니다.

확인 전에 팝업을 읽으세요. 사이트 이름, 주소, 네트워크. 하나라도 이상하면 Cancel(취소)을 누르세요.

## 3단계: 스왑하고 모든 서명 읽기

1. 낼 코인과 원하는 토큰을 고르세요(토큰은 이름이 아니라 **컨트랙트 주소**로 찾으세요).
2. 소액을 넣고 환율, 슬리피지(허용하는 최대 가격 변동), 네트워크 수수료를 확인하세요.
3. 어떤 토큰을 처음 팔 때 사이트가 **Approve**(그 토큰을 쓸 권한)를 요청합니다. 가능하면 "무제한" 대신 금액을 정하세요.
4. 앱에서 스왑을 확인하세요. 서명 요청이 읽을 수 없는 코드로 가득하거나 이해가 안 되면 — **서명하지 마세요**.

## 4단계: 코인을 Binance 계정으로 되돌리기

1. Binance 앱에서 **Exchange** → **Assets** → **Deposit**(입금)으로 갑니다. 코인을 고릅니다(예: BNB).
2. **네트워크**를 고릅니다(예: BNB Smart Chain). 입금 주소를 복사합니다. 일부 코인은 **memo/tag**(메모/태그)도 필요하니 함께 복사하세요.
3. **Wallet** → **Send**(보내기)로 바꿉니다. 같은 코인, 같은 네트워크를 고르고 주소(메모가 있으면 메모도)를 붙여 넣습니다.
4. 먼저 소액을 테스트로 보내세요. Binance 계정에 도착하면 나머지를 보내세요.

지갑에 BNB나 SOL을 조금 남겨 두세요. 온체인 작업은 실패하더라도 모두 네트워크 수수료가 듭니다. 어떤 밈코인은 거래소에 아예 입금할 수 없습니다(거래소가 상장하지 않은 경우). 현금화하려면 먼저 지갑에서 BNB, SOL, USDT로 바꾸세요.

## 5단계: 연결 해제하고 정리하기

1. 끝나면 사이트 연결을 해제하세요(지갑의 연결된 사이트나 WalletConnect 설정, 또는 DEX의 **Disconnect** 버튼).
2. 가끔 토큰 승인 목록을 확인하고 필요 없는 승인은 취소(revoke)하세요. 취소에는 약간의 수수료가 듭니다.
3. 공용 컴퓨터라면 확장 프로그램에서 로그아웃하세요.

산 토큰은 [내 포트폴리오]({lang}/me/)에서 확인하고, 실시간 밈코인 데이터는 [밈코인 페이지]({lang}/memes/)에서 보세요.

> **⚠️ 주의**
> - **사이트나 "고객 지원"이 복구 비밀번호, 시드 문구, "지갑 동기화"를 요구할 때.** 진짜 DEX나 Binance 직원은 절대 그러지 않습니다. 페이지를 닫으세요.
> - **무제한 승인과 내용 모를 서명.** 악성 승인이나 서명 하나로 사기꾼이 나중에 내 확인 없이 그 토큰을 몽땅 가져갈 수 있습니다.
> - **틀린 네트워크, 빠진 메모, 바뀐 붙여넣기 주소.** 악성 프로그램이 복사한 주소를 바꿔치기할 수 있습니다. 매번 앞뒤 글자를 비교하고 소액으로 테스트하세요.

다음 수업: 사기 전에 밈코인 점검하는 법. 모든 수업은 [배우기 페이지]({lang}/learn/)에 있습니다.

## 출처

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*투자 조언이 아닙니다. 이 안내는 도구 사용법을 설명할 뿐이며 어떤 토큰의 매수도 권하지 않습니다. Binance Wallet은 일부 국가에서 이용하지 못할 수 있습니다.*
