---
title: Cách kiểm tra memecoin trước khi mua: 6 bước kiểm tra trong 5 phút
description: Trước khi mua memecoin, hãy kiểm tra hợp đồng, thanh khoản, người nắm giữ, tỷ lệ top 10, tuổi token và kiểm tra bảo mật của Binance. Checklist đơn giản.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: bước kiểm tra trước khi mua bất kỳ memecoin nào
---
**Kiểm tra memecoin trước khi mua như thế nào?** Tìm token bằng địa chỉ hợp đồng, rồi kiểm tra sáu điều: kiểm tra bảo mật, thanh khoản, số người nắm giữ, 10 ví lớn nhất nắm bao nhiêu, token bao nhiêu tuổi và người tạo còn thay đổi được token hay không. Chỉ cần một mục đỏ là bỏ qua — còn hàng nghìn coin khác.

> **Điểm chính**
> - Các bước này không làm memecoin trở nên an toàn. Chúng chỉ giúp bạn tránh những cái bẫy rõ ràng nhất: token không bán được, bản sao giả và coin mà vài ví có thể đánh sập.
> - Tab **Audit** trong Binance Wallet kiểm tra rủi ro hợp đồng, rủi ro giao dịch và rủi ro lừa đảo (ví dụ "honeypot" — token mua được nhưng không bao giờ bán được). Chính Binance nói rằng bản kiểm tra này không phải lúc nào cũng chính xác.
> - Trên [trang memecoin]({lang}/memes/) của chúng tôi, bộ lọc chất lượng bật sẵn (**Chỉ chất lượng: thanh khoản từ 100K USD, từ 1 ngày**): chỉ hiện token có thanh khoản từ $100K và ít nhất 1 ngày tuổi.

Bài này tiếp nối bài [Cách kết nối Binance Wallet với DEX]({lang}/blog/connect-binance-wallet-to-dex/). Memecoin cực kỳ rủi ro — chỉ dùng số tiền bạn chấp nhận mất.

## Bước 1 — Lấy đúng địa chỉ hợp đồng

Mỗi token có một **địa chỉ hợp đồng** (contract address — mã định danh duy nhất trên blockchain, một chuỗi dài chữ và số). Ai cũng có thể tạo token cùng tên và cùng logo, nên cái tên chẳng nói lên điều gì.

1. Sao chép địa chỉ từ tài khoản chính thức của dự án hoặc từ một trang dữ liệu đáng tin.
2. Dán vào ô tìm kiếm trong ví. So sánh 4 ký tự đầu và 4 ký tự cuối.
3. Nếu thấy nhiều token cùng tên, các token còn lại là bản sao.

## Bước 2 — Mở kiểm tra bảo mật

Trong ứng dụng Binance, mở token ở mục **Wallet** rồi chạm vào tab **Audit** (trên website: bấm vào token, rồi **Audit**). Trên trang token memecoin của chúng tôi, bạn thấy cùng kết quả đó dưới dạng **Kiểm tra an toàn của Binance: Rủi ro thấp / Rủi ro trung bình / Rủi ro cao**.

Xem ba nhóm:

- **Rủi ro hợp đồng** — người tạo có thể chặn việc bán, đưa ví vào danh sách đen, đổi thuế hoặc đổi số dư không?
- **Rủi ro giao dịch** — rủi ro honeypot, thuế mua hoặc bán bất thường (phí bị trừ ở mỗi giao dịch), thanh khoản thấp, rủi ro rug pull.
- **Rủi ro lừa đảo** — token giả, lừa đảo đã biết, spam.

Có một mục đỏ = đừng mua. "Rủi ro thấp" vẫn không có nghĩa là an toàn: người tạo vẫn có thể làm gì đó sau khi bạn mua.

## Bước 3 — Kiểm tra thanh khoản

Thanh khoản là số tiền trong pool giao dịch giúp bạn bán được. Nếu nó rất nhỏ, chỉ một lệnh bán nhỏ cũng đẩy giá xuống mạnh, và người tạo có thể rút tiền ra (rug pull). Trên WhatIfStack, bộ lọc mặc định ẩn các token có thanh khoản dưới $100K. Hãy kiểm tra thêm thanh khoản của pool đã bị khóa (locked) hay bị đốt (burned — xóa vĩnh viễn) chưa, nếu trang dữ liệu có hiển thị.

## Bước 4 — Đếm người nắm giữ và tỷ lệ top 10

Trên trang token, xem **Người nắm giữ** (bao nhiêu ví đang giữ) và **Top 10 nắm** (10 ví lớn nhất giữ bao nhiêu phần trăm tổng số coin). Chỉ vài trăm người nắm giữ và top 10 nắm phần lớn nghĩa là một nhóm nhỏ có thể bán và đánh sập giá. Lưu ý: địa chỉ pool và địa chỉ đốt cũng nằm trong top 10 — phần đó là bình thường.

## Bước 5 — Kiểm tra tuổi token

Phần lớn token lừa đảo chỉ sống vài giờ hoặc vài ngày. Token chưa đầy một ngày tuổi thì hoàn toàn chưa có lịch sử. Bộ lọc của chúng tôi trên /memes/ chỉ hiện token ít nhất 1 ngày tuổi. Lâu hơn không có nghĩa là an toàn — chỉ là bớt mù mờ hơn.

## Bước 6 — Trên Solana: người tạo còn thay đổi được token không?

Trên Solana có hai cài đặt quan trọng:

- **Mint authority** (quyền tạo thêm token mới). Nếu vẫn bật, người tạo có thể in thêm và phần của bạn bị nhỏ lại.
- **Freeze authority** (quyền đóng băng ví). Nếu vẫn bật, người tạo có thể chặn bạn chuyển hoặc bán.

Trạng thái an toàn hơn là "revoked" hoặc "disabled" (không ai giữ quyền đó). Bạn xem được cả hai trên trang token của một block explorer như Solscan.

> **⚠️ Cẩn thận**
> - **Bản sao giả cùng tên.** Luôn mua theo địa chỉ hợp đồng, đừng bao giờ mua theo tên hay logo.
> - **Honeypot.** Bạn mua được, biểu đồ tăng, nhưng không ai bán được. Lịch sử chỉ có lệnh mua mà không có lệnh bán là dấu hiệu nguy hiểm.
> - **Tin vào một tín hiệu xanh duy nhất.** Bản kiểm tra, nhiều người nắm giữ hay một cái tên nổi tiếng không bảo vệ bạn nếu giá đơn giản là giảm — phần lớn memecoin kết thúc gần bằng không.

## Ý nghĩa nếu bạn mua đều đặn

Mua đều đặn từng khoản nhỏ hiệu quả nhất với những tài sản nhiều khả năng vẫn còn tồn tại sau năm năm. Phần lớn memecoin thì không. Nếu vẫn muốn thử, hãy giữ ở một khoản rất nhỏ và cố định, rồi theo dõi cùng phần tiền còn lại trong [danh mục của bạn]({lang}/me/).

Bài tiếp theo: câu chuyện về Dogecoin. Tất cả bài học có trên [trang Học]({lang}/learn/).

## Nguồn

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Không phải lời khuyên đầu tư. Bài hướng dẫn này giải thích cách kiểm tra một token và không khuyến nghị mua bất kỳ coin nào.*
