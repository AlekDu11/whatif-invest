---
title: Midnight (NIGHT) giải thích dễ hiểu: blockchain riêng tư của nhà sáng lập Cardano, 24 tỷ token và phí bằng DUST
description: Midnight dễ hiểu: quyền riêng tư zero-knowledge hoạt động ra sao, NIGHT và DUST dùng để làm gì, Glacier Drop, lịch mở khóa, đối thủ và rủi ro chính.
date: 2026-11-24
kind: analysis
---
**Midnight** là một blockchain được xây dựng cho quyền riêng tư: các ứng dụng trên đó có thể chứng minh một điều là đúng — rằng bạn đã trên 18 tuổi, rằng bạn có đủ tiền — mà không cần để lộ dữ liệu phía sau. Dự án do Input Output, công ty của nhà sáng lập Cardano Charles Hoskinson, tạo ra như "partner chain" (chuỗi đối tác) đầu tiên của Cardano, và token NIGHT của nó hiện có giá trị {{mcap:night}} ({{rank:night}} trong các đồng tiền mã hóa). Giới đầu tư theo dõi Midnight như một trong số ít canh bạc lớn về quyền riêng tư được thiết kế để hợp tác với cơ quan quản lý thay vì chống lại họ.

> **Điểm chính**
> - Tổng cung NIGHT sẽ không bao giờ vượt quá 24 tỷ; token ra mắt trên Cardano vào tháng 12/2025 và mainnet của mạng lưới bắt đầu chạy từ tháng 3/2026.
> - Phí không trả bằng NIGHT mà bằng DUST — một tài nguyên riêng tư, không thể chuyển nhượng, được tự động tạo ra cho người nắm giữ NIGHT.
> - Phần lớn token được tặng miễn phí cho người nắm giữ tám đồng tiền mã hóa khác và được mở khóa thành bốn đợt trong khoảng một năm.
> - Đỉnh kỷ lục là {{ath:night}} ({{athd:night}}); giá hiện tại cách đỉnh {{fromath:night}}.

## Cách hoạt động

Midnight sử dụng bằng chứng không kiến thức (zero-knowledge proof) — một loại mật mã học cho phép chứng minh một khẳng định mà không tiết lộ chi tiết. Mỗi ứng dụng lưu hai loại dữ liệu: dữ liệu công khai được ghi lên blockchain và dữ liệu riêng tư nằm lại trên thiết bị của người dùng. Nhà phát triển quyết định cái gì được hiển thị, cái gì được giấu đi, và có thể cho phép kiểm toán viên hoặc cơ quan quản lý xem những thông tin cụ thể. Dự án gọi cách tiếp cận này là "rational privacy" (quyền riêng tư hợp lý). Nhà phát triển viết ứng dụng bằng Compact, một ngôn ngữ dựa trên TypeScript, nên họ không cần là chuyên gia mật mã. Khi ra mắt, mạng lưới được vận hành bởi một nhóm nhà vận hành tin cậy, trong đó có một node do Google Cloud chạy; lộ trình sẽ chuyển việc tạo khối sang các nhà vận hành stake pool của Cardano và sau đó tiến tới phi tập trung hoàn toàn.

## Token dùng để làm gì

NIGHT là token công khai và có thể giao dịch trên các sàn. Nắm giữ NIGHT mang lại hai điều: quyền biểu quyết trong quản trị sau này và lượng DUST được tạo ra liên tục. DUST dùng để trả phí giao dịch và hợp đồng thông minh, không thể gửi cho người khác và sẽ hao hụt dần nếu không được dùng. Ý tưởng là doanh nghiệp có thể vận hành ứng dụng với chi phí dự đoán được mà không phải tiêu token cho mỗi giao dịch, trong khi tài nguyên phí riêng tư này không thể bị dùng để che giấu các khoản thanh toán. Validator nhận NIGHT làm phần thưởng khối. NIGHT tồn tại dưới dạng token gốc trên Cardano và theo kế hoạch sẽ hoạt động trên cả hai chuỗi như một tài sản duy nhất.

## Các con số hiện tại

- Giá hôm nay: {{price:night}}
- Đỉnh kỷ lục: {{ath:night}} ({{athd:night}}), cách đỉnh {{fromath:night}}
- Vốn hóa thị trường: {{mcap:night}} ({{rank:night}} trong các đồng tiền mã hóa)
- 10 USD mỗi ngày từ tháng 3/2026: {{dca:night:1}} ({{dcaroi:night:1}})

## Câu chuyện của Midnight

Input Output công bố Midnight vào tháng 11/2022 như một chuỗi bảo vệ dữ liệu gắn với Cardano. Năm 2025, dự án tổ chức Glacier Drop: người tự lưu ký ADA, BTC, ETH, SOL, XRP, BNB, AVAX và BAT có thể nhận NIGHT miễn phí, và hơn 3,5 tỷ token đã được nhận qua khoảng 170.000 địa chỉ. Giai đoạn thứ hai, Scavenger Mine, cho phép bất kỳ ai kiếm token bằng cách giải câu đố ngay trên trình duyệt; hơn 1 tỷ NIGHT đã đến tay hàng triệu địa chỉ. NIGHT ra mắt trên Cardano ngày 4/12/2025, việc quy đổi (redemption) mở từ ngày 10/12/2025 và mainnet chính thức hoạt động vào tháng 3/2026.

## Các lựa chọn thay thế

Những đồng coin riêng tư lâu đời như [Zcash]({lang}/zec/) và [Monero]({lang}/xmr/) tập trung vào thanh toán riêng tư, còn Midnight tập trung vào ứng dụng và dữ liệu riêng tư với khả năng công bố tùy chọn. [Oasis]({lang}/rose/) và [Dusk]({lang}/dusk/) cũng cung cấp hợp đồng thông minh bảo mật, và các dự án trên Ethereum bổ sung quyền riêng tư bằng zero-knowledge rollup. Họ hàng gần nhất của Midnight là [Cardano]({lang}/ada/), cùng chung nhà sáng lập và có các stake pool được kỳ vọng sẽ góp phần bảo vệ Midnight.

## Rủi ro chính

- **Mở khóa token:** token airdrop được mở khóa thành bốn đợt trong 360 ngày, còn quỹ dự trữ và ngân khố mở khóa muộn hơn, điều này có thể tạo thêm áp lực bán.
- **Mạng lưới còn non trẻ:** chuỗi bắt đầu chạy năm 2026 với các nhà vận hành tin cậy; phi tập trung hoàn toàn vẫn là kế hoạch, chưa phải thực tế.
- **Quản lý pháp lý:** công nghệ riêng tư là mục tiêu của các cơ quan quản lý, và một số sàn đã hủy niêm yết coin riêng tư ở một số quốc gia.
- **Mức độ ứng dụng:** giá trị của DUST và NIGHT phụ thuộc vào việc có ứng dụng thực sự dùng mạng lưới, và điều đó vẫn chưa được chứng minh.
- **Biến động mạnh:** token mới thường giảm sâu sau khi ra mắt, và giá có thể bị chi phối bởi tin tức về Cardano cũng như các cá voi nắm giữ lớn.

## Ý nghĩa nếu bạn mua định kỳ

Midnight mới được giao dịch từ cuối năm 2025, nên lịch sử giá còn ngắn và nói lên rất ít về dài hạn. Mua một số tiền cố định đều đặn giúp trải điểm vào lệnh theo thời gian, có thể làm dịu tác động của lịch mở khóa và những cú biến động mạnh — nhưng không loại bỏ được rủi ro một dự án non trẻ thất bại. Nhiều người chỉ giữ những token như vậy ở một phần nhỏ trong khoản tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Midnight Network — trang chính thức và blog](https://midnight.network/)
- [Midnight mở quy đổi token NIGHT (Midnight Foundation, 4/12/2025)](https://hackernoon.com/midnight-opens-redemptions-for-45b-night-tokens-after-record-breaking-distribution-event)
- [Báo cáo dự án Midnight (Binance Research)](https://www.binance.com/en/research/projects/midnight)
- [Midnight là gì? Partner chain tập trung vào quyền riêng tư của Cardano (Coin Bureau)](https://coinbureau.com/education/what-is-midnight-network-cardano)
