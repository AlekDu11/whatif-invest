---
title: Morpho (MORPHO) giải thích dễ hiểu: thị trường cho vay mở, vault do người quản lý tuyển chọn và giới hạn 1 tỷ token
description: Morpho dễ hiểu: thị trường cho vay và vault hoạt động thế nào, vì sao khoản vay của Coinbase chạy trên nó, token MORPHO dùng làm gì, lịch sử, đối thủ và rủi ro.
date: 2026-11-23
kind: analysis
---
**Morpho** là một mạng lưới cho vay trên Ethereum và các blockchain khác: người dùng gửi tiền mã hóa hoặc stablecoin để nhận lãi, người khác vay bằng cách thế chấp tiền mã hóa của mình, và đứng giữa là hợp đồng thông minh chứ không phải ngân hàng. Morpho được thành lập tại Pháp năm 2021, và những tên tuổi lớn như Coinbase xây dựng dịch vụ cho vay trên nền tảng này. Toàn bộ MORPHO đang lưu hành hôm nay có giá trị {{mcap:morpho}} ({{rank:morpho}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Theo Morpho, tiền gửi tăng từ khoảng 5 tỷ USD lên 13 tỷ USD trong năm 2025, và số người dùng từ 67.000 lên hơn 1,4 triệu.
> - Các khoản vay USDC thế chấp bằng bitcoin của Coinbase chạy trên các thị trường Morpho trên mạng Base; đến tháng 11/2026 dịch vụ này đã có ở cả 50 bang của Mỹ.
> - Tổng số MORPHO sẽ không bao giờ vượt quá 1 tỷ; khoảng 706 triệu đang lưu hành vào tháng 11/2026.
> - Đỉnh kỷ lục là {{ath:morpho}} ({{athd:morpho}}); giá hôm nay cách đỉnh {{fromath:morpho}}.

## Cách hoạt động

Morpho có hai tầng. **Thị trường (markets)** là những bể cho vay nhỏ với quy tắc cố định: mỗi thị trường có một tài sản để cho vay, một tài sản thế chấp, một nguồn giá (price feed) và một ngưỡng thanh lý, và khi đã tạo thì không thể sửa quy tắc. Nếu tài sản thế chấp của người vay giảm giá quá sâu, nó sẽ bị bán để trả nợ. **Vault** nằm ở tầng trên: tiền gửi được giao cho một "người quản lý" (curator) chuyên nghiệp, người này phân bổ vào nhiều thị trường để kiếm lãi trong giới hạn rủi ro đã đặt ra. Các ứng dụng như Coinbase, Crypto.com, Gemini và Bitpanda hiển thị các vault và khoản vay này cho người dùng mà họ không cần trực tiếp thao tác trên blockchain. Năm 2026 Morpho ra mắt sản phẩm lãi suất cố định, kỳ hạn cố định mang tên Midnight, trong đó lãi suất do thị trường quyết định chứ không phải một công thức.

## Token dùng để làm gì

MORPHO là token quản trị: người nắm giữ bỏ phiếu trong Morpho DAO về những việc như hỗ trợ blockchain nào và chi tiêu khoản khuyến khích ra sao. Token này bắt đầu chuyển nhượng được từ tháng 11/2024. Trong năm 2026, bản thân giao thức không giữ lại phần nào từ tiền lãi, nên người nắm giữ không có quyền trực tiếp đối với phí; muốn bật loại phí như vậy cần một cuộc bỏ phiếu quản trị. Vì thế, nhu cầu với token chủ yếu phụ thuộc vào kỳ vọng về sự tăng trưởng của Morpho và các quyết định trong tương lai.

## Các con số hiện tại

- Giá hôm nay: {{price:morpho}}
- Đỉnh kỷ lục: {{ath:morpho}} ({{athd:morpho}}), cách đỉnh {{fromath:morpho}}
- Vốn hóa thị trường: {{mcap:morpho}} ({{rank:morpho}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:morpho}}
- 10 USD mỗi ngày trong 1 năm: {{dca:morpho:1}} từ {{dcainv:1}} đã đầu tư ({{dcaroi:morpho:1}})

## Câu chuyện của Morpho

Paul Frambot cùng ba nhà đồng sáng lập khởi động Morpho vào tháng 8/2021 và huy động 18 triệu USD từ a16z và Variant vào tháng 6/2022. Sản phẩm đầu tiên, Morpho Optimizer (tháng 6/2022), ghép trực tiếp người cho vay và người vay trên nền Aave và Compound để có lãi suất tốt hơn. Tháng 1/2024 Morpho ra mắt thị trường và vault riêng, và tháng 8/2024 huy động 50 triệu USD trong vòng gọi vốn do Ribbit Capital dẫn đầu. Coinbase bắt đầu cung cấp khoản vay thế chấp bằng tiền mã hóa qua Morpho vào tháng 1/2025, Ethereum Foundation gửi 2.400 ETH vào các vault Morpho vào tháng 10/2025, và mảng tiền mã hóa của Société Générale cùng Bitwise sử dụng Morpho vào đầu năm 2026. Tháng 4/2026 một bộ trưởng Pháp gọi Morpho là "kỳ lân", dựa trên giá trị thị trường của token khi đó vượt 1,5 tỷ USD.

## Các lựa chọn thay thế

Đối thủ lớn nhất là [Aave]({lang}/aave/), giao thức cho vay lớn nhất, dùng các bể chung quy mô lớn thay vì thị trường tách biệt. Những cái tên khác gồm Compound, Spark thuộc hệ sinh thái [Sky]({lang}/sky/) và Kamino trên Solana. Các nền tảng tập trung như Nexo cũng cho vay thế chấp bằng tiền mã hóa, nhưng ở đó tiền do một công ty nắm giữ.

## Rủi ro chính

- **Biến động mạnh:** MORPHO là token còn non trẻ; đến tháng 11/2026 giá đã giảm hơn một nửa so với đỉnh tháng 1/2025.
- **Rủi ro vault và người quản lý:** người quản lý có thể chọn tài sản thế chấp rủi ro hoặc nguồn giá lỗi, và người gửi tiền vào vault đó có thể bị lỗ.
- **Rủi ro hợp đồng thông minh:** lỗi phần mềm hoặc tấn công vào một thị trường hay một tích hợp có thể gây thiệt hại, dù đã được kiểm toán.
- **Nguồn cung token:** khoảng 30% trong 1 tỷ MORPHO chưa lưu hành vào tháng 11/2026, và các nhà đầu tư ban đầu nắm tỷ trọng lớn.
- **Không có quyền với phí:** nếu DAO không bao giờ bật phí, sự tăng trưởng về lượng sử dụng có thể không đến được với người nắm giữ token; quy định về cho vay cũng có thể bị siết chặt.

## Ý nghĩa nếu bạn mua định kỳ

MORPHO mới được giao dịch trong thời gian ngắn, nên lịch sử còn quá ít để đánh giá việc mua định kỳ. Mua một số tiền cố định mỗi tuần hoặc mỗi tháng giúp dàn đều giá vào, nhưng với một token quản trị còn non trẻ, rủi ro thua lỗ lớn vẫn cao. Nhiều người chỉ giữ những token như vậy ở mức nhỏ trong danh mục tiền mã hóa. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Morpho 2026 — Paul Frambot (blog Morpho, tháng 1/2026)](https://morpho.org/blog/morpho-2026)
- [The Morpho Effect: April 2026 (blog Morpho)](https://morpho.org/blog/the-morpho-effect-april-2026)
- [Morpho (DeFi lending protocol) (Wikipedia)](https://en.wikipedia.org/wiki/Morpho_(DeFi_lending_protocol))
