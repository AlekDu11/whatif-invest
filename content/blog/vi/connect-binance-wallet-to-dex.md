---
title: Cách kết nối Binance Wallet với DEX và chuyển coin về lại: từng bước
description: Kết nối Binance Wallet với trang DEX an toàn, gửi coin về tài khoản Binance đúng mạng và xóa các quyền approve cũ — các bước đơn giản.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: lần chuyển thử nhỏ trước mỗi địa chỉ hoặc mạng mới
---
**Kết nối Binance Wallet với DEX như thế nào?** Mở trang web chính thức của DEX, bấm **Connect Wallet**, chọn Binance Wallet (hoặc WalletConnect rồi quét mã QR bằng ứng dụng Binance) và xác nhận trong ứng dụng. Để chuyển coin về, hãy sao chép **địa chỉ nạp** (deposit address) trên Binance cho cùng coin và cùng mạng, rồi gửi từ ví tới đó — chuyển thử một khoản nhỏ trước.

> **Điểm chính**
> - DEX (sàn phi tập trung — trang web nơi bạn đổi token trực tiếp từ ví của mình) không bao giờ cần mật khẩu khôi phục hay seed phrase của bạn. Kết nối chỉ cho phép trang *yêu cầu* bạn ký; không có gì di chuyển cho tới khi bạn xác nhận.
> - Mạng phải trùng ở cả hai phía (BNB Smart Chain sang BNB Smart Chain, Solana sang Solana). Sai mạng hoặc sai địa chỉ có thể khiến coin bị mất.
> - Mỗi lần "Approve" cho phép trang tiêu token thay bạn. Hãy cấp quyền nhỏ và xóa những quyền không còn dùng.

Bài này tiếp nối [Cách tạo Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Memecoin cực kỳ rủi ro — chỉ dùng số tiền bạn chấp nhận mất.

## Bước 1 — Mở đúng trang web thật

Trang DEX giả với logo y hệt là một trong những cái bẫy phổ biến nhất.

1. Tự gõ địa chỉ hoặc dùng bookmark. Đừng bấm quảng cáo trên kết quả tìm kiếm hay link trong các nhóm chat.
2. Kiểm tra thanh địa chỉ từng ký tự.
3. Kiểm tra DEX có hoạt động trên mạng mà coin của bạn đang nằm không.

## Bước 2 — Kết nối ví

Có ba cách, tùy thiết bị:

- **Trên máy tính có tiện ích trình duyệt Binance Wallet** (Chrome hoặc Brave). Đăng nhập tiện ích bằng cách quét mã QR của nó bằng ứng dụng Binance. Sau đó trên DEX bấm **Connect** hoặc **Connect Wallet**, chọn Binance Wallet và xác nhận cửa sổ bật lên.
- **Trên máy tính không có tiện ích.** Trên DEX bấm **Connect Wallet → WalletConnect**. Một mã QR hiện ra. Quét bằng máy quét trong ứng dụng Binance và chạm **Connect**.
- **Trên điện thoại.** Mở DEX trong trình duyệt điện thoại, bấm **Connect Wallet**, chọn Binance Wallet trong danh sách và xác nhận trong ứng dụng.

Trước khi xác nhận, hãy đọc cửa sổ bật lên: tên trang, địa chỉ và mạng. Nếu có gì không đúng, bấm Cancel.

## Bước 3 — Swap và đọc kỹ mọi yêu cầu ký

1. Chọn coin dùng để trả và token bạn muốn (tìm token bằng **địa chỉ hợp đồng**, không phải bằng tên).
2. Nhập một số tiền nhỏ và kiểm tra tỷ giá, slippage (mức thay đổi giá lớn nhất bạn chấp nhận) và phí mạng.
3. Lần đầu bán một token, trang sẽ yêu cầu **Approve** (cho phép tiêu token đó). Nếu ứng dụng cho phép, hãy nhập số lượng thay vì "unlimited" (không giới hạn).
4. Xác nhận swap trong ứng dụng. Nếu yêu cầu ký là một trang mã khó hiểu hoặc vô lý — **đừng ký**.

## Bước 4 — Gửi coin về tài khoản Binance

1. Trong ứng dụng Binance, chuyển sang **Exchange** → **Assets** → **Deposit**. Chọn coin (ví dụ BNB).
2. Chọn **mạng** (ví dụ BNB Smart Chain). Sao chép địa chỉ nạp. Một số coin còn cần **memo/tag** — sao chép luôn.
3. Chuyển sang **Wallet** → **Send**. Chọn cùng coin và cùng mạng. Dán địa chỉ (và memo nếu có).
4. Gửi thử một khoản nhỏ trước. Khi tiền đã về tài khoản Binance, gửi phần còn lại.

Hãy để lại một ít BNB hoặc SOL trong ví: mọi thao tác on-chain, kể cả thất bại, đều tốn phí mạng. Một số memecoin hoàn toàn không nạp được lên sàn (sàn không niêm yết) — muốn rút tiền, hãy đổi chúng về BNB, SOL hoặc USDT trong ví trước.

## Bước 5 — Ngắt kết nối và dọn dẹp

1. Khi xong, ngắt kết nối trang (trong phần cài đặt các trang đã kết nối hoặc WalletConnect của ví, hoặc nút **Disconnect** trên DEX).
2. Thỉnh thoảng kiểm tra các quyền approve token và revoke (thu hồi) những quyền không cần. Revoke tốn một khoản phí nhỏ.
3. Trên máy tính dùng chung, hãy đăng xuất khỏi tiện ích.

Bạn có thể theo dõi các token đã mua trong [danh mục của bạn]({lang}/me/) và xem dữ liệu memecoin trực tiếp trên [trang memecoin]({lang}/memes/).

> **⚠️ Cẩn thận**
> - **Một trang hoặc "hỗ trợ viên" đòi mật khẩu khôi phục, seed phrase hay "đồng bộ ví".** DEX thật hay nhân viên Binance không bao giờ làm vậy. Hãy đóng trang.
> - **Approve không giới hạn và ký mù.** Một lần approve hoặc chữ ký độc hại có thể cho kẻ lừa đảo rút sạch token đó về sau, không cần bạn xác nhận thêm.
> - **Sai mạng, thiếu memo hoặc địa chỉ dán vào bị thay đổi.** Phần mềm độc hại có thể tráo địa chỉ đã sao chép. Mỗi lần hãy so ký tự đầu và cuối, và chuyển thử số nhỏ.

Bài tiếp theo: cách kiểm tra một memecoin trước khi mua. Tất cả bài học có trên [trang Học]({lang}/learn/).

## Nguồn

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Không phải lời khuyên đầu tư. Bài hướng dẫn này giải thích cách các công cụ hoạt động và không khuyến nghị mua bất kỳ token nào. Binance Wallet có thể không khả dụng ở mọi quốc gia.*
