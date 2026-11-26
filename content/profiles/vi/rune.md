---
title: THORChain (RUNE) giải thích dễ hiểu: hoán đổi bitcoin thật và các đồng khác giữa các blockchain, không cần wrapped token
description: THORChain bằng ngôn ngữ đơn giản: hoán đổi xuyên chuỗi và pool thanh khoản RUNE, bond của node, các vụ hack 2021, đóng băng cho vay 2025, rủi ro chính.
date: 2026-11-26
kind: analysis
---
**THORChain (RUNE)** là blockchain cho phép hoán đổi tiền mã hóa giữa các mạng khác nhau — ví dụ bitcoin thật lấy ether thật — mà không cần sàn tập trung và không cần các bản sao "bọc" (wrapped) của đồng coin. RUNE là token nằm ở trung tâm: mọi pool giao dịch đều ghép cặp với RUNE, và các máy tính vận hành mạng phải khóa RUNE làm tiền đặt cọc bảo đảm. Toàn bộ RUNE đang lưu hành hiện có vốn hóa {{mcap:rune}} ({{rank:rune}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - THORChain hoán đổi tài sản gốc giữa các chuỗi như Bitcoin, Ethereum, BNB Chain, Dogecoin và nhiều chuỗi khác chỉ trong một bước.
> - Mọi pool thanh khoản đều ghép cặp với RUNE, và nhà vận hành node phải bond RUNE, có thể bị tịch thu nếu họ gian lận.
> - Đỉnh kỷ lục là {{ath:rune}} ({{athd:rune}}); giá hiện tại cách đỉnh {{fromath:rune}}.
> - Mạng từng bị hack hai lần trong năm 2021 và đóng băng sản phẩm cho vay, tiết kiệm vào tháng 1/2025.

## Cách hoạt động

THORChain được xây dựng bằng Cosmos SDK. Một nhóm node độc lập cùng kiểm soát các "vault" — địa chỉ trên Bitcoin, Ethereum và các chuỗi được kết nối khác — bằng chữ ký ngưỡng (threshold signature), nên không node nào có thể tự ý chuyển tiền. Khi bạn đổi BTC lấy ETH, bạn gửi bitcoin vào một vault; mạng bán số bitcoin đó lấy RUNE trong pool BTC, rồi bán RUNE lấy ETH trong pool ETH, và một vault gửi cho bạn ether thật. Giá được xác định từ số dư của các pool, giống như trên [Uniswap]({lang}/uni/). Nhà cung cấp thanh khoản gửi coin vào pool và nhận một phần phí hoán đổi. Các node phải bond lượng RUNE có giá trị lớn hơn số tiền họ giúp canh giữ, nhằm khiến việc đánh cắp không có lợi.

## Vì sao người ta cho rằng nó có giá trị

Chuyển giá trị giữa các blockchain thường chậm, rủi ro hoặc phải dùng sàn tập trung có xác minh tài khoản. THORChain mở ra tuyến đường trực tiếp giữa các đồng coin gốc, vì vậy nhiều ví tiền mã hóa và ứng dụng hoán đổi định tuyến giao dịch qua nó. Nhu cầu với RUNE đến từ ba nguồn: RUNE là một nửa của mọi pool, là khoản bond mà node phải nộp, và một phần phí hoán đổi được chia cho người nắm giữ và staking RUNE. Vì thế khối lượng giao dịch càng cao thì người giữ RUNE nhận càng nhiều phí.

## Các con số hiện tại

- Giá hôm nay: {{price:rune}}
- Đỉnh kỷ lục: {{ath:rune}} ({{athd:rune}}), cách đỉnh {{fromath:rune}}
- Vốn hóa thị trường: {{mcap:rune}} ({{rank:rune}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:rune}}
- 10 USD mỗi ngày trong 5 năm: {{dca:rune:5}} từ {{dcainv:5}} đã đầu tư ({{dcaroi:rune:5}})

## Câu chuyện của RUNE

RUNE lần đầu được mở bán qua Binance Launchpad vào tháng 7/2019. Một "chaosnet" dùng tiền thật, được giới hạn có chủ đích, hoạt động từ năm 2020, và giao dịch đa chuỗi xuất hiện vào tháng 4/2021. Trong cơn sốt năm 2021, RUNE đạt khoảng 20 USD vào tháng 5/2021, nhưng đến tháng 7/2021 mạng bị hai vụ tấn công trị giá hàng triệu USD. Mainnet đầy đủ được công bố vào tháng 6/2022. Tháng 1/2025, THORChain tạm dừng sản phẩm cho vay và "savers" sau khi nghĩa vụ nợ tích tụ khoảng 200 triệu USD; khoản nợ này sau đó được chuyển thành một token riêng tên TCY. Tháng 2/2025, nhóm hacker đứng sau vụ trộm 1,4 tỷ USD từ sàn Bybit đã dùng THORChain để đổi số ether đánh cắp sang bitcoin, mang lại khối lượng kỷ lục cùng những chỉ trích gay gắt.

## Các lựa chọn thay thế

Sàn tập trung vẫn là cách dễ nhất để hoán đổi giữa các chuỗi. Đối thủ on-chain gồm các dịch vụ cầu nối và tổng hợp, cùng Maya Protocol — một bản fork của THORChain. Để hoán đổi trong cùng một mạng, người ta dùng các sàn phi tập trung như [Uniswap]({lang}/uni/) hoặc [PancakeSwap]({lang}/cake/). Để kết nối các blockchain nói chung, [Cosmos]({lang}/atom/) và [Chainlink]({lang}/link/) đưa ra những cách tiếp cận khác.

## Rủi ro chính

- **Biến động mạnh:** RUNE đã hơn một lần giảm hơn 80% so với đỉnh.
- **Hack:** các vault xuyên chuỗi giữ số tiền lớn và từng bị tấn công; một lỗi mới có thể khiến người dùng mất tiền.
- **Sản phẩm thất bại:** việc đóng băng cho vay năm 2025 cho thấy tính năng mới có thể gây thua lỗ cho người dùng và tạo áp lực lên RUNE.
- **Pháp lý:** việc hacker dùng mạng để rửa tiền thu hút sự chú ý của cơ quan quản lý và có thể dẫn tới hạn chế.
- **Phụ thuộc vào RUNE:** vì mọi pool đều ghép cặp với RUNE, một cú giảm mạnh của RUNE sẽ ảnh hưởng toàn hệ thống.

## Ý nghĩa nếu bạn mua định kỳ

RUNE là một canh bạc rằng mọi người sẽ tiếp tục dùng THORChain để hoán đổi xuyên chuỗi, và lịch sử của nó có cả những vụ hack, một sản phẩm bị đóng băng lẫn những đợt tăng giá nhanh. Mua một số tiền cố định đều đặn giúp cân bằng giá vào, nhưng không bảo vệ bạn trước những cú sốc riêng của dự án. Nhiều người chỉ để một token chuyên biệt như RUNE chiếm phần nhỏ trong khoản tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Tài liệu THORChain — giới thiệu (docs.thorchain.org)](https://docs.thorchain.org/)
- [RUNE tăng 15% khi THORChain khởi động lại phần lớn giao dịch hoán đổi sau sự cố (Cointelegraph)](https://cointelegraph.com/markets/rune-rallies-15-as-thorchain-restarts-most-swaps-after-outage)
- [Giá THORChain, vốn hóa thị trường và đỉnh mọi thời đại (CoinGecko)](https://www.coingecko.com/en/coins/thorchain)
