---
title: Stacks (STX) giải thích dễ hiểu: hợp đồng thông minh cho Bitcoin, hoạt động từ 2021, thưởng trả bằng BTC
description: Stacks giải thích dễ hiểu: lớp Bitcoin hoạt động ra sao, Proof of Transfer, stacking nhận BTC, sBTC, lịch sử, rủi ro chính và điều người mua định kỳ cần biết.
date: 2026-11-24
kind: analysis
---
**Stacks** là một blockchain xây dựng trên nền Bitcoin, bổ sung những thứ mà bản thân Bitcoin không có: hợp đồng thông minh và các ứng dụng như cho vay, giao dịch và NFT. Giao dịch của Stacks được neo vào blockchain Bitcoin, và hiện tổng giá trị token STX là {{mcap:stx-token}} ({{rank:stx-token}} trong các đồng tiền mã hóa). Nhiều người theo dõi Stacks như một trong những cách lâu đời và lớn nhất để bitcoin "làm được nhiều hơn" thay vì chỉ nằm yên trong ví.

> **Điểm chính**
> - Thợ đào Stacks trả bằng bitcoin thật để giành STX mới, và người nắm giữ STX khóa coin của mình có thể nhận số bitcoin đó.
> - Năm 2019, Blockstack — công ty đứng sau dự án — tổ chức đợt bán token đầu tiên được Ủy ban Chứng khoán Mỹ (SEC) chấp thuận theo Regulation A+.
> - Đỉnh kỷ lục là {{ath:stx-token}} ({{athd:stx-token}}); giá hiện tại cách đỉnh {{fromath:stx-token}}.
> - Từ bản nâng cấp Nakamoto tháng 10/2024, khối được tạo chỉ trong vài giây và giao dịch đã xác nhận có độ chắc chắn ngang với chính Bitcoin.

## Cách hoạt động

Stacks dùng cơ chế Proof of Transfer (PoX). Thay vì đốt điện như thợ đào Bitcoin, thợ đào Stacks gửi bitcoin để đấu giá quyền ghi khối Stacks tiếp theo và nhận STX mới phát hành. Số bitcoin đó không biến mất: nó được chuyển cho những người "stacking" — khóa STX trong một số chu kỳ nhất định (mỗi chu kỳ khoảng hai tuần) để giúp bảo vệ mạng lưới. Mỗi khối Stacks đều được ghi lên Bitcoin, nên muốn viết lại lịch sử Stacks thì phải viết lại cả lịch sử Bitcoin. Ứng dụng được viết bằng Clarity, ngôn ngữ lập trình được thiết kế để dễ dự đoán, dễ kiểm tra và có thể đọc những gì diễn ra trên chuỗi Bitcoin.

## Vì sao người ta cho rằng nó có giá trị

STX cần để trả phí giao dịch trên Stacks, là phần thưởng của thợ đào, và khóa STX là cách để nhận thưởng BTC — vì vậy nhu cầu sử dụng mạng gắn trực tiếp với nhu cầu đối với token. Ý tưởng lớn hơn là DeFi trên Bitcoin: phần lớn bitcoin đang nằm im, và Stacks đưa ra cách dùng nó trong ứng dụng mà không rời khỏi thế giới Bitcoin. Công cụ chính cho việc này là sBTC, token được bảo chứng 1:1 bằng bitcoin, có thể chuyển vào các ứng dụng Stacks và đổi lại thành BTC.

## Các con số hiện tại

- Giá hôm nay: {{price:stx-token}}
- Đỉnh kỷ lục: {{ath:stx-token}} ({{athd:stx-token}}), cách đỉnh {{fromath:stx-token}}
- Vốn hóa thị trường: {{mcap:stx-token}} ({{rank:stx-token}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:stx-token}}
- 10 USD mỗi ngày trong 5 năm: {{dca:stx-token:5}} từ {{dcainv:5}} đã đầu tư ({{dcaroi:stx-token:5}})

## Câu chuyện của Stacks

Muneeb Ali và Ryan Shea thành lập Blockstack năm 2013 sau khi gặp nhau ở Princeton. Năm 2017 dự án bán token cho nhà đầu tư, và tháng 7/2019 trở thành công ty đầu tiên chào bán token ra công chúng qua đợt phát hành Regulation A+ được SEC chấp thuận. Tháng 1/2021, mainnet Stacks 2.0 đi vào hoạt động cùng Proof of Transfer và Clarity, và trong năm đó giá tăng từ khoảng 0,40 USD lên trên 2 USD. Cuối năm 2022 giá giảm còn khoảng 0,20 USD, rồi bật tăng theo cơn sốt "Ordinals" trên Bitcoin và lập kỷ lục ngày 1/4/2024. Tiếp theo là bản nâng cấp Nakamoto vào tháng 10/2024, mở nạp sBTC vào tháng 12/2024 và rút về bitcoin vào tháng 4/2025. Dù vậy, giá vẫn trượt dốc suốt năm 2025 và nằm dưới 0,40 USD gần như cả năm 2026.

## Các lựa chọn thay thế

Trong các dự án đưa ứng dụng lên bitcoin, Rootstock vận hành một sidechain tương thích Ethereum được thợ đào Bitcoin bảo vệ, [Core]({lang}/core/) là một chuỗi riêng có staking bitcoin, còn [Babylon]({lang}/baby/) cho phép staking bitcoin để bảo vệ các mạng khác. Nhiều người giữ bitcoin chỉ đơn giản dùng wrapped bitcoin trên [Ethereum]({lang}/eth/). Còn với ai chỉ muốn sở hữu chính bitcoin, [Bitcoin]({lang}/btc/) là lựa chọn hiển nhiên.

## Rủi ro chính

- **Biến động mạnh:** đến cuối năm 2022, STX đã mất hơn 90% so với đỉnh năm 2021, và những cú giảm tương tự lại xảy ra sau kỷ lục năm 2024.
- **Nguồn cung mới:** mỗi ngày STX mới được tạo ra làm phần thưởng đào, có thể liên tục gây áp lực bán.
- **Cạnh tranh:** nhiều lớp Bitcoin mới hơn tranh giành cùng người dùng và cùng lượng bitcoin.
- **Công nghệ:** sBTC dựa vào một nhóm người ký (signer) nắm giữ bitcoin; lỗi hoặc sự cố ở khâu này có thể làm tổn hại niềm tin vào cả mạng lưới.
- **Lưu giữ và pháp lý:** nếu sàn phá sản hoặc bạn mất khóa riêng, coin có thể mất hẳn; quy định về tiền mã hóa khác nhau ở mỗi nước và có thể thay đổi nhanh.

## Ý nghĩa nếu bạn mua định kỳ

Giá Stacks đi theo những con sóng dài: hai đỉnh lớn vào năm 2021 và 2024, sau mỗi đỉnh là một đợt giảm sâu. Mua một số tiền cố định đều đặn giúp bạn mua nhiều hơn khi giá thấp và ít hơn khi giá cao mà không phải đoán đáy — nhưng cách này không bảo vệ bạn khỏi một đợt giảm kéo dài, như kết quả 5 năm ở trên cho thấy. Nhiều người chỉ để các đồng nhỏ như STX chiếm một phần nhỏ khoản tiết kiệm mà họ chịu được nếu giảm mạnh. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Finally, Finality: the Nakamoto upgrade (Stacks Foundation)](https://stacks.org/nakamoto)
- [The sBTC mainnet release is live with Bitcoin deposits (Stacks blog)](https://www.stacks.co/blog/bitcoin-deposits-live)
- [sBTC withdrawal functionality is now live (Stacks blog)](https://www.stacks.co/blog/sbtc-withdrawals-live)
- [Stacks price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/stacks)
