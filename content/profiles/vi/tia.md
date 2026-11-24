---
title: Celestia (TIA) giải thích dễ hiểu: mạng dữ liệu cho rollup, hoạt động từ 2023, 1 tỷ token khi ra mắt
description: Celestia giải thích dễ hiểu: lớp dữ liệu hoạt động ra sao, TIA dùng để làm gì, các lần cắt phát hành, lịch sử, đối thủ, rủi ro chính.
date: 2026-11-24
kind: analysis
---
**Celestia** là một blockchain chỉ làm một việc hẹp: lưu trữ và công bố dữ liệu giao dịch của các blockchain khác, chủ yếu là "rollup", để ai cũng có thể kiểm tra. Mạng ra mắt vào tháng 10/2023, là mạng "mô-đun" đầu tiên thuộc loại này, và token TIA của nó có tổng giá trị {{mcap:tia}} ({{rank:tia}} trong các đồng tiền mã hóa). Nhiều người theo dõi Celestia như một ván cược rằng nhiều blockchain trong tương lai sẽ thuê dịch vụ này thay vì tự xây.

> **Điểm chính**
> - Celestia không chạy ứng dụng hay hợp đồng thông minh — nó chỉ bảo đảm rằng dữ liệu đã được công bố, và bán không gian đó bằng TIA.
> - Khi ra mắt có 1 tỷ TIA; không có giới hạn cứng, nhưng mức phát hành hằng năm đã giảm từ khoảng 7,2% xuống khoảng 5% vào tháng 7/2025 và xuống khoảng 2,5% vào tháng 11/2025.
> - Đỉnh kỷ lục là {{ath:tia}} ({{athd:tia}}); giá hiện cách đỉnh {{fromath:tia}}.
> - Các đợt mở khóa token lớn cho nhà đầu tư sớm và đội ngũ, bắt đầu từ tháng 10/2024, đã đè nặng lên giá.

## Cách hoạt động

Rollup là những mạng tự xử lý giao dịch rồi gửi một bản ghi đã nén lên một chuỗi khác. Celestia là nơi để đăng bản ghi đó. Rollup trả phí để đưa các "blob" dữ liệu vào khối của Celestia, và mạng bảo đảm dữ liệu thực sự có ở đó. Điểm then chốt là kỹ thuật lấy mẫu dữ liệu (data availability sampling): một nút nhẹ trên điện thoại hay laptop bình thường tải vài mảnh nhỏ ngẫu nhiên của một khối, và nếu tất cả đều có, nó có thể gần như chắc chắn rằng cả khối đã được công bố. Celestia được xây bằng Cosmos SDK và bảo mật bằng proof of stake. Bản nâng cấp Matcha cuối năm 2025 đã nâng kích thước khối tối đa từ 8 MB lên 128 MB.

## Token dùng để làm gì

TIA có ba công dụng. Rollup và ứng dụng trả phí bằng TIA cho không gian blob mà họ dùng. Người nắm giữ đem TIA đi staking với các validator — những bên tạo khối — và nhận token mới phát hành làm phần thưởng. Ngoài ra, người giữ TIA bỏ phiếu về thay đổi của mạng — ví dụ hai lần cắt giảm phát hành. Vì vậy, nhu cầu đối với token phụ thuộc vào số rollup thực sự chọn Celestia và lượng dữ liệu họ đăng lên.

## Các con số hiện tại

- Giá hôm nay: {{price:tia}}
- Đỉnh kỷ lục: {{ath:tia}} ({{athd:tia}}), cách đỉnh {{fromath:tia}}
- Vốn hóa thị trường: {{mcap:tia}} ({{rank:tia}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:tia}}
- 10 USD mỗi ngày trong 3 năm: {{dca:tia:3}} từ {{dcainv:3}} đã đầu tư ({{dcaroi:tia:3}})

## Câu chuyện của Celestia

Ý tưởng bắt đầu năm 2019 với LazyLedger, một bài nghiên cứu của Mustafa Al-Bassam; dự án đổi tên thành Celestia vào năm 2021. Mainnet Beta ra mắt ngày 31/10/2023 cùng một đợt airdrop TIA lớn cho nhà phát triển và người dùng. Trong đợt tăng giá của thị trường crypto năm 2024, giá leo lên khoảng 20 USD vào tháng 2/2024. Từ tháng 10/2024, các đợt mở khóa lớn cho nhà đầu tư sớm bắt đầu, và đến tháng 6/2025 TIA đã rơi xuống khoảng 1,32 USD, giảm khoảng 93%, rồi tiếp tục trượt dốc trong năm 2026. Khi đó, đồng sáng lập Mustafa Al-Bassam cho biết dự án có quỹ dự trữ 100 triệu USD, đủ hoạt động sáu năm. Các bản nâng cấp Lotus (tháng 7/2025) và Matcha (tháng 11/2025) đã giảm dần mức phát hành, hướng tới mức dài hạn 1,5% mỗi năm.

## Các lựa chọn thay thế

Đối thủ lớn nhất của Celestia chính là [Ethereum]({lang}/eth/): từ tháng 3/2024, Ethereum có không gian "blob" riêng, rẻ hơn, dành cho rollup. Các mạng dữ liệu khác gồm [Avail]({lang}/avail/), EigenDA của [EigenCloud]({lang}/eigen/) và lớp dữ liệu của [NEAR]({lang}/near/). Nhiều rollup như [Arbitrum]({lang}/arb/) và [Optimism]({lang}/op/) vẫn đăng dữ liệu lên Ethereum.

## Rủi ro chính

- **Cạnh tranh:** blob của Ethereum, Avail và EigenDA tranh giành cùng nhóm khách hàng, khiến phí luôn thấp.
- **Thu nhập từ phí thấp:** đến nay, phí rollup trả còn nhỏ so với giá trị của mạng.
- **Nguồn cung tăng:** không có giới hạn cứng, và TIA mới liên tục được phát hành cho người staking.
- **Mở khóa và tập trung:** nhà đầu tư sớm, đội ngũ và quỹ nắm tỷ lệ lớn, việc họ bán ra có thể làm giá biến động.
- **Biến động mạnh:** TIA mất hơn 90% so với đỉnh năm 2024 chỉ trong khoảng 16 tháng.

## Ý nghĩa nếu bạn mua định kỳ

Lịch sử ngắn của TIA chủ yếu là một đợt giảm dài sau đỉnh sớm, xen kẽ những lần bật tăng mạnh. Mua một khoản cố định đều đặn giúp dàn trải giá mua theo thời gian, nhưng không bảo vệ bạn nếu mạng không được dùng rộng rãi — và với một token còn non trẻ, ba năm lịch sử nói rất ít về ba năm tới. Nhiều người chỉ để những đồng như vậy chiếm một phần nhỏ trong khoản tiết kiệm. Kết quả trong quá khứ không bảo đảm lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Staking, quản trị và nguồn cung (tài liệu Celestia)](https://docs.celestia.org/learn/TIA/staking-governance-supply/)
- [Giới thiệu bản nâng cấp Matcha: hướng tới khối 128 MB (blog Celestia)](https://blog.celestia.org/matcha/)
- [Đồng sáng lập Celestia nói về quỹ dự trữ 100 triệu USD (The Block, tháng 6/2025)](https://www.theblock.co/post/359387/celestia-co-founder-cites-100-million-war-chest-and-six-year-runway-to-play-the-long-game-as-native-token-drops-over-90-from-peak)
