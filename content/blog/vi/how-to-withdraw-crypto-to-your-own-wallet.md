---
title: Cách rút crypto từ sàn về ví của riêng bạn: hướng dẫn từng bước
description: Chuyển coin từ sàn về ví riêng an toàn: sao chép đúng địa chỉ, chọn cùng một mạng, thêm memo nếu cần và gửi thử một khoản nhỏ trước.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 mạng
stat_label: sàn và ví phải dùng cùng một mạng, nếu không coin có thể bị mất
---
**Làm sao để rút crypto về ví của riêng bạn?** Trong ví, bạn sao chép **địa chỉ nhận** (receive address) của đồng coin. Sau đó trên sàn, mở **Withdraw** (Rút), dán địa chỉ đó, chọn **đúng mạng** mà ví của bạn dùng, nhập một khoản thử nhỏ và xác nhận bằng 2FA. Khi khoản thử đã đến, bạn gửi phần còn lại.

> **Điểm chính**
> - Ba thứ phải khớp nhau: **đồng coin**, **địa chỉ** và **mạng** (blockchain mà coin đi qua, ví dụ Ethereum, BNB Smart Chain, TRON hoặc Solana). Binance cảnh báo rằng coin gửi sai mạng có thể mất vĩnh viễn.
> - Một số coin (như XRP, XLM hoặc ATOM) còn cần **memo** hoặc **tag** (một dãy số ngắn cho bên nhận biết coin là của ai). Thiếu nó, giao dịch có thể bị kẹt hoặc vào nhầm người.
> - **Luôn gửi thử một khoản nhỏ trước.** Lệnh rút không thể hủy khi coin đã rời khỏi sàn.

Bài học này tiếp nối [Cách cài đặt mua định kỳ]({lang}/blog/how-to-set-up-a-recurring-buy/). Vì sao bạn có thể muốn có ví riêng được giải thích trong bài [ví nóng và ví lạnh]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Trước khi bắt đầu

Bạn cần hai thứ. Một là tài khoản sàn có coin (được bảo vệ bằng 2FA — xem [Cách đăng ký sàn crypto]({lang}/blog/how-to-register-on-a-crypto-exchange/)). Hai là ứng dụng ví riêng đã cài đặt xong, với **cụm từ khôi phục** (seed phrase — 12 hoặc 24 từ bí mật để khôi phục ví) đã ghi ra giấy và cất offline. Đừng bao giờ gõ seed phrase ở bất kỳ nơi nào khác — không sàn, trang web hay "nhân viên hỗ trợ" nào cần đến nó.

## Bước 1 — Sao chép địa chỉ nhận của ví

1. Mở ứng dụng ví và nhấn **Receive** (đôi khi là **Deposit**).
2. Chọn đồng coin, ví dụ Bitcoin hoặc USDT.
3. Nếu ví hỏi, hãy chọn mạng. Ghi lại đó là mạng nào — ví dụ "USDT trên TRON (TRC20)" hoặc "USDT trên Ethereum (ERC20)".
4. Nhấn **Copy** cạnh địa chỉ. Đừng tự gõ tay.

Địa chỉ là một dãy dài chữ và số. Địa chỉ Bitcoin thường bắt đầu bằng **bc1**, địa chỉ Ethereum và BNB Smart Chain bằng **0x**, địa chỉ TRON bằng **T**.

## Bước 2 — Mở Withdraw trên sàn

Trong ứng dụng Binance, đường dẫn là **Assets → Spot → Send → Withdraw Crypto**; trên trang web là **Wallet → Overview → Withdraw**. Các sàn khác có nút **Withdraw** cạnh mỗi đồng coin trong màn hình ví hoặc danh mục. Chọn đúng đồng coin bạn đã chọn ở Bước 1.

## Bước 3 — Dán địa chỉ và chọn mạng

1. Dán địa chỉ vào ô **Address**.
2. So sánh **4 ký tự đầu và 4 ký tự cuối** với ví của bạn. Có loại mã độc tráo địa chỉ đã sao chép thành địa chỉ của kẻ trộm.
3. Chọn **mạng** (network). Nó phải trùng với mạng mà ví hiển thị ở Bước 1. Binance có thể tự gợi ý mạng — vẫn hãy kiểm tra lại. Đừng chọn mạng chỉ vì phí rẻ nhất.
4. Nếu xuất hiện ô **Memo** hoặc **Tag** và ví đã cho bạn một mã, hãy điền vào. Nếu ví của bạn không hiển thị memo, thường là không cần — nhưng hãy kiểm tra lại trong trang trợ giúp của ví.

Mẹo: nếu không chắc chắn, hãy lưu địa chỉ trong **Address Management** (sổ địa chỉ) của sàn. Binance còn có **whitelist** (danh sách trắng): khi bật, lệnh rút chỉ có thể đến các địa chỉ đã lưu, giúp ích nếu ai đó đánh cắp mật khẩu của bạn.

## Bước 4 — Gửi thử một khoản nhỏ

1. Nhập một khoản nhỏ — chỉ cao hơn mức rút tối thiểu hiển thị trên màn hình một chút.
2. Xem dòng **phí mạng** (network fee) và **số bạn sẽ nhận** (you will receive). Phí cố định cho mỗi lần rút, nên với khoản rất nhỏ, phí có thể chiếm phần lớn.
3. Nhấn **Withdraw** và xác nhận bằng mã 2FA hoặc passkey. Một số sàn còn gửi email xác nhận — mở email và nhấn **Confirm**.

## Bước 5 — Kiểm tra đã đến chưa, rồi gửi phần còn lại

1. Chờ đợi. Một lần chuyển có thể mất từ vài giây đến khoảng một giờ, tùy mạng và lưu lượng.
2. Trên sàn, mở lịch sử rút để xem trạng thái và **TxID** (mã giao dịch, có thể tra trên trang block explorer).
3. Khi coin đã hiện trong ví, lặp lại Bước 2–4 với phần còn lại. Địa chỉ đã có trong lịch sử hoặc sổ địa chỉ, nên lần thứ hai nhanh hơn.

Thêm coin vào [danh mục của bạn]({lang}/me/) để theo dõi giá trị ở một nơi, dù chúng được cất ở đâu.

> **⚠️ Cẩn thận**
> - **Sai mạng.** USDT có trên nhiều mạng. Gửi USDT "TRC20" đến địa chỉ chỉ nhận "ERC20" có thể khiến coin bị mất. Kiểm tra mạng hai lần.
> - **Thiếu memo hoặc tag.** Sàn và ví cần memo sẽ không biết coin đến là của ai nếu thiếu nó. Việc lấy lại, nếu làm được, rất chậm và mất phí.
> - **Hỗ trợ giả và trang "xác minh địa chỉ".** Không bên hợp pháp nào hỏi seed phrase của bạn hay bảo bạn "xác minh" ví bằng cách gửi coin. Chỉ rút trong ứng dụng hoặc trang web chính thức.

## Ý nghĩa nếu bạn mua đều đặn

Nếu bạn mua một ít mỗi tuần hoặc mỗi tháng, bạn không cần rút sau mỗi lần mua — mỗi lần rút đều mất phí. Nhiều người để coin tích lại trên sàn và thỉnh thoảng mới chuyển về ví riêng, ví dụ mỗi quý một lần, bằng một lần chuyển lớn hơn. Ví dụ từ máy tính của chúng tôi: 10 USD mỗi ngày vào Bitcoin trong 3 năm (tổng cộng {{dcainv:3}}) đã thành {{dca:btc:3}} ({{dcaroi:btc:3}}). Đây là kết quả quá khứ, không phải dự báo. Bitcoin hiện ở mức {{price:btc}}; xem [trang Bitcoin]({lang}/btc/).

Bài trước: [Cách cài đặt mua định kỳ]({lang}/blog/how-to-set-up-a-recurring-buy/). Bài tiếp theo: cách bán crypto và rút tiền về tài khoản ngân hàng. So sánh các sàn trên [trang sàn giao dịch]({lang}/exchanges/) của chúng tôi; tất cả bài học ở [trang Học]({lang}/learn/).

## Nguồn

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance (cập nhật tháng 3/2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account (tháng 6/2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Không phải lời khuyên đầu tư.*
