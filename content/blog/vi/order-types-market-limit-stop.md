---
title: "Các loại lệnh: lệnh thị trường, lệnh giới hạn và lệnh dừng giải thích từng bước"
description: Nút Market, Limit và Stop trên ứng dụng sàn hoặc môi giới làm gì, kèm ví dụ tính toán và 3 lỗi khiến người mới mất tiền.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: loại lệnh cơ bản — thị trường (nhanh, giá không cố định), giới hạn (giá cố định, chưa chắc khớp), dừng (kích hoạt tại một mức giá)
---
**Có những loại lệnh nào?** **Lệnh thị trường** (Market) mua hoặc bán ngay lập tức ở giá tốt nhất đang có. **Lệnh giới hạn** (Limit) chỉ mua hoặc bán ở giá của bạn hoặc tốt hơn, nên có thể không bao giờ khớp. **Lệnh dừng** (Stop) chờ đến khi giá chạm mức bạn chọn, rồi gửi một lệnh thị trường — thường dùng để giới hạn thua lỗ.

> **Điểm chính**
> - Market = nhanh, nhưng bạn không kiểm soát được giá chính xác. Limit = kiểm soát giá, nhưng không chắc sẽ khớp.
> - Lệnh dừng trở thành lệnh thị trường khi được kích hoạt. Khi giá rơi nhanh, lệnh có thể khớp thấp hơn nhiều so với giá dừng của bạn.
> - Trước khi bấm "Mua", luôn kiểm tra ba thứ: loại lệnh, số lượng và giá.

## Ba nút bấm, nói đơn giản

Khi mở màn hình giao dịch trên ứng dụng sàn hoặc môi giới, bạn thường thấy các tab: **Market** (thị trường), **Limit** (giới hạn) và **Stop** (dừng; đôi khi là "Stop-limit").

- **Lệnh thị trường.** "Mua ngay, giá nào cũng được." Lệnh khớp gần như tức thì ở giá chào bán tốt nhất (giá **ask**, giá thấp nhất mà người bán đưa ra). Với coin lớn và cổ phiếu lớn, giá thường rất sát với giá bạn thấy. Với thị trường nhỏ, ít thanh khoản, giá có thể tệ hơn nhiều.
- **Lệnh giới hạn.** "Chỉ mua ở $X hoặc rẻ hơn" (hoặc "chỉ bán ở $X hoặc cao hơn"). Lệnh của bạn nằm chờ trong **sổ lệnh** (order book — danh sách mọi lệnh mua và bán đang chờ) cho đến khi có người chấp nhận giá của bạn. Nếu giá không bao giờ tới đó, sẽ không có gì xảy ra.
- **Lệnh dừng (stop-loss, cắt lỗ).** "Nếu giá giảm xuống $X thì bán." Trước đó lệnh vô hình và không làm gì cả. Khi giá chạm $X, nó thành lệnh thị trường và bán ở giá có sẵn tiếp theo.
- **Lệnh stop-limit.** Giống lệnh dừng, nhưng thay vào đó nó thành lệnh *giới hạn*. Bạn sẽ không bán thấp hơn mức giới hạn — nhưng khi giá rơi nhanh, có thể bạn không bán được chút nào.

## Ví dụ với con số đơn giản

Giả sử một cổ phiếu đang ở **$100,00**. Người mua tốt nhất trả $99,95 (giá **bid**) và người bán tốt nhất chào $100,05 (giá ask). Khoảng cách $0,10 là **chênh lệch giá** (spread).

1. Bạn bấm **Market mua, 10 cổ phiếu** → bạn trả khoảng $100,05 mỗi cổ phiếu = **$1.000,50** cộng phí nếu có.
2. Bạn đặt **Limit mua, 10 cổ phiếu ở $98** → không có gì xảy ra cho đến khi có người bán chấp nhận $98. Nếu giá lại tăng lên $105, lệnh của bạn chỉ nằm chờ và bạn không mua được gì.
3. Bạn đang có cổ phiếu và đặt **Stop ở $90** → nếu giá giảm còn $90, một lệnh bán thị trường được gửi đi. Khi thị trường bình thường, bạn có thể nhận $89,95. Nếu tin xấu ra trước giờ mở cửa và cổ phiếu mở cửa ở $80, lệnh dừng kích hoạt và bạn bán quanh **$80**, không phải $90.

Trường hợp thứ ba là có thật. Ngày 6/5/2010 ("flash crash"), giá ở Mỹ sụp đổ chỉ trong vài phút. Một số lệnh dừng khớp thấp hơn nhiều so với mức dừng, vài cổ phiếu thậm chí được giao dịch với giá một xu, theo báo cáo của SEC và CFTC.

## Từng bước: đặt lệnh giới hạn đầu tiên an toàn

Hãy tập với số tiền rất nhỏ trước.

1. **Bước 1 — Mở màn hình giao dịch** của coin hoặc cổ phiếu và chọn **Mua** (Buy).
2. **Bước 2 — Bấm tab "Limit"**, không phải "Market".
3. **Bước 3 — Nhập giá của bạn.** Xem giá hiện tại trước (ví dụ Bitcoin lúc này là {{price:btc}}). Mức giới hạn quá thấp so với giá hiện tại có thể không bao giờ khớp.
4. **Bước 4 — Nhập số lượng.** Kiểm tra ô đó là số coin/cổ phiếu hay số tiền (USD, EUR). Đây là lỗi gõ nhầm phổ biến nhất.
5. **Bước 5 — Kiểm tra phần tóm tắt**: loại lệnh, giá, số lượng, tổng, phí. Sau đó xác nhận.
6. **Bước 6 — Tìm lệnh của bạn** trong "Open orders" (lệnh đang mở). Bạn có thể hủy ở đó bất cứ lúc nào cho đến khi lệnh khớp. Khi khớp, lệnh chuyển sang "Order history" (lịch sử lệnh).

> **⚠️ Cẩn thận**
> - **Lệnh thị trường ở thị trường ít thanh khoản.** Với coin nhỏ hoặc ngoài giờ giao dịch thông thường, lệnh thị trường có thể khớp tệ hơn nhiều so với giá trên màn hình (gọi là **trượt giá**, slippage). Hãy dùng lệnh giới hạn ở đó.
> - **Nghĩ rằng stop-loss bảo đảm giá cho bạn.** Không: nó bảo đảm việc bán, không bảo đảm giá. Giá nhảy cóc và sập mạnh có thể đẩy giá khớp xuống thấp hơn nhiều. Stop-limit bảo vệ giá nhưng có thể không bán được.
> - **Nhầm các ô nhập.** Nhầm chiều (Bán thay vì Mua), thừa một số 0 ở số lượng, hoặc gõ giá vào nhầm ô. Đọc phần tóm tắt trước khi xác nhận.

## Điều này có ý nghĩa gì nếu bạn mua đều đặn

Nếu bạn chỉ mua một ít mỗi tuần hoặc mỗi tháng, bạn không cần lệnh phức tạp. Lệnh thị trường với tài sản lớn, thanh khoản cao thường là ổn, hoặc lệnh giới hạn cao hơn giá hiện tại một chút nếu bạn muốn đặt mức trần. Kết quả thật đến từ thời gian ở trên thị trường: $10 mỗi ngày vào Bitcoin trong 3 năm giờ sẽ có giá trị {{dca:btc:3}} (bạn đã bỏ vào {{dcainv:3}}) — kết quả quá khứ, không phải dự báo.

Tiếp theo trên WhatIfStack: xem sổ lệnh và các trader lớn di chuyển thị trường thế nào ở [trang trading]({lang}/trading/) và [công cụ theo dõi cá voi Hyperliquid]({lang}/trading/hyperliquid/), so sánh phí trên các [sàn giao dịch]({lang}/exchanges/), và tìm mọi bài học ở [trang Học]({lang}/learn/).

## Nguồn

- [Investor.gov (SEC): Các loại lệnh](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Bản tin nhà đầu tư — lệnh stop, stop-limit và trailing stop](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Các loại lệnh](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC và SEC: Báo cáo về các diễn biến thị trường ngày 6/5/2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Không phải lời khuyên đầu tư.*
