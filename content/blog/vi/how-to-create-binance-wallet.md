---
title: Cách tạo Binance Wallet và mua memecoin: hướng dẫn từng bước
description: Tạo Binance Wallet trong ứng dụng Binance, sao lưu, chuyển coin từ tài khoản Binance, tìm token theo hợp đồng và swap, kèm các bước kiểm tra an toàn.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: phần khóa bảo vệ một Binance Wallet; cần 2 phần để vào ví
---
**Tạo Binance Wallet như thế nào?** Mở ứng dụng Binance, chuyển sang tab **Wallet** (ví) ở phía trên, chạm **Create Keyless Wallet** (tạo ví không cần khóa) và sao lưu bằng một mật khẩu khôi phục. Chỉ mất vài phút, không cần seed phrase, và bạn có một ví tự lưu ký (ví mà chính bạn, không phải sàn, kiểm soát coin) để mua các token on-chain như memecoin.

> **Điểm chính**
> - Binance Wallet nằm bên trong ứng dụng Binance. Bạn cần một tài khoản Binance đã xác minh, nhưng coin trong ví là tự lưu ký: bạn chịu trách nhiệm sao lưu.
> - Đây là ví "keyless" (MPC): khóa được chia thành 3 phần, trên điện thoại của bạn, trong bản sao lưu đám mây của bạn và ở Binance. Bất kỳ 2 phần nào cũng mở được ví.
> - Đừng bao giờ bỏ qua bước sao lưu. Nếu bạn mất điện thoại **và** quên mật khẩu khôi phục, Binance không thể khôi phục ví.

Trước khi bắt đầu: hầu hết memecoin mới đều mất gần như toàn bộ giá trị. Chỉ dùng số tiền bạn chấp nhận mất hoàn toàn. Xem [memecoin là gì]({lang}/blog/what-are-memecoins/).

## Bạn cần chuẩn bị gì

- Một điện thoại có ứng dụng Binance chính thức (chỉ tải từ App Store, Google Play hoặc binance.com; ứng dụng giả rất phổ biến).
- Một tài khoản Binance đã hoàn tất xác minh danh tính (KYC, tức là xuất trình giấy tờ tùy thân). Nếu chưa có, bạn có thể đăng ký qua liên kết của chúng tôi: [Binance Wallet](/go/binance-web3?from=learn&l=vi).
- Một ít BNB hoặc SOL trong tài khoản Binance để mua và trả phí mạng.

## Bước 1 — Mở ví

1. Đăng nhập vào ứng dụng Binance.
2. Ở phía trên màn hình, chuyển từ **Exchange** (sàn) sang **Wallet**.
3. Chạm **Create Keyless Wallet**. (Nếu bạn đã có ví khác, lựa chọn còn lại là **Import Wallet** (nhập ví); người mới không cần đến nó.)

Việc tạo ví chỉ mất vài giây. Ứng dụng không cho bạn xem 12 hay 24 từ seed phrase; thay vào đó nó dùng MPC (multi-party computation, tính toán đa bên: khóa được chia thành nhiều mảnh không bao giờ nằm chung một chỗ).

## Bước 2 — Sao lưu (đừng bỏ qua)

Ứng dụng có ba cách lưu phần sao lưu của bạn. Chọn một:

- **iCloud hoặc Google Drive.** Bạn đặt một **mật khẩu khôi phục** mà chỉ bạn biết. Phần khóa được mã hóa bằng mật khẩu này và lưu vào đám mây của bạn.
- **Mã QR.** Bạn đặt mật khẩu khôi phục và lưu một mã QR; phần khóa được lưu trên một đám mây phi tập trung.
- **Quick Backup** (sao lưu nhanh). Bạn xác nhận bằng Face ID hoặc vân tay; không cần mật khẩu, nhưng phần khóa do một nhà cung cấp bên thứ ba giữ.

Hãy viết mật khẩu khôi phục ra giấy và cất ở nơi an toàn. Sau đó kiểm tra: chạm **Settings** (cài đặt, góc trên bên trái ở Home hoặc Assets) → **Wallet Management** (quản lý ví). Bạn phải thấy nhãn **Backed Up** (đã sao lưu).

## Bước 3 — Chuyển coin từ Binance vào ví

1. Trong ví, chạm **Receive** (nhận) → **Withdraw from Binance Exchange** (rút từ sàn Binance).
2. Chọn coin (ví dụ BNB) **và mạng** (BNB Smart Chain cho BNB, Solana cho SOL). Mạng phải khớp.
3. Nhập số lượng. Ứng dụng hiển thị phí và số tiền cuối cùng trước khi bạn xác nhận.
4. Chọn tiền lấy từ tài khoản Spot hay Funding, chạm **Withdraw** (rút), kiểm tra địa chỉ và mạng, rồi **Confirm** (xác nhận).

Hãy bắt đầu bằng một khoản thử nhỏ. Giao dịch chuyển đã xác nhận thì không hủy được. Luôn để lại một ít BNB hoặc SOL trong ví: mọi thao tác trên blockchain đều tốn phí mạng (gas), kể cả thao tác thất bại.

## Bước 4 — Tìm đúng token bằng địa chỉ hợp đồng

Nhiều memecoin có bản sao cùng tên, cùng logo. Dấu hiệu nhận dạng đáng tin duy nhất là **địa chỉ hợp đồng** (một chuỗi dài gồm chữ và số, riêng cho từng token).

1. Lấy địa chỉ từ nguồn đáng tin: tài khoản đã xác minh của dự án, một trang dữ liệu lớn hoặc trang token trên [trang memecoin]({lang}/memes/) của chúng tôi.
2. Trong màn hình **Markets** (thị trường) hoặc **Trade** (giao dịch) của ví, dán địa chỉ vào ô tìm kiếm thay vì gõ tên.
3. So sánh 4–6 ký tự đầu và cuối với nguồn của bạn.

## Bước 5 — Kiểm tra token trước khi mua

Trên [trang memecoin]({lang}/memes/) của chúng tôi, mỗi trang token hiển thị kết quả kiểm tra bảo mật của Binance và các con số chính. Hãy xem:

- **Thanh khoản**: có bao nhiêu tiền trong pool giao dịch. Thanh khoản ít = có thể bạn không bán được.
- **Holder và tỷ lệ của top 10**: nếu vài ví nắm phần lớn nguồn cung, họ có thể đánh sập giá.
- **Tuổi**: một token mới tạo cách đây một giờ là một tấm vé số.
- **Cảnh báo**: nếu xuất hiện bất kỳ cảnh báo rủi ro hay bảo mật nào, hãy dừng lại.

Chính Binance nói rằng họ không kiểm tra các token xuất hiện trên Meme Rush (mục memecoin mới toanh của họ), nên việc kiểm tra là của bạn. [Bài học về lừa đảo và rug pull]({lang}/blog/memecoin-scams-rug-pull/) của chúng tôi liệt kê các dấu hiệu cảnh báo.

## Bước 6 — Swap

1. Mở **Trade** → **Swap** (hoán đổi). Chọn thứ bạn dùng để trả (BNB) và token bạn muốn, trên cùng một mạng.
2. Nhập một số lượng nhỏ. Đọc tỷ giá, **slippage** (mức thay đổi giá lớn nhất bạn chấp nhận trước khi giao dịch thất bại) và phí mạng.
3. Một số token cần bước **Approve** (phê duyệt) trước; bước này tốn một khoản phí nhỏ.
4. Chạm **Swap** và xác nhận bằng passkey hoặc 2FA.

Để bán, làm tương tự theo chiều ngược lại. Nếu muốn xem các token mới nhất, tab Markets có **Meme Rush**: token mới toanh được giao dịch ở đó trên một "bonding curve" và không thể chuyển ra khỏi ví cho đến khi chúng "di chuyển" sang một DEX thông thường (sàn phi tập trung). Đây là góc rủi ro nhất của thị trường.

> **⚠️ Cẩn thận**
> - **Không sao lưu, hoặc lưu mật khẩu trong ảnh chụp màn hình.** Mất điện thoại và mật khẩu là mất coin vĩnh viễn.
> - **Sai mạng hoặc sai địa chỉ.** Phần câu hỏi thường gặp của Binance nói rằng token gửi nhầm địa chỉ không thể hoàn lại. Luôn gửi một khoản thử trước.
> - **Token giả và tin nhắn từ "bộ phận hỗ trợ".** Chỉ tìm bằng địa chỉ hợp đồng. Nhân viên Binance sẽ không bao giờ hỏi mật khẩu khôi phục của bạn hay bảo bạn "xác minh" ví trên một trang web.

Bài tiếp theo: cách kết nối Binance Wallet với một trang DEX và chuyển coin về lại Binance. Xem tất cả bài học trên [trang Học]({lang}/learn/).

## Nguồn

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Không phải lời khuyên đầu tư. Memecoin cực kỳ rủi ro; bài hướng dẫn này giải thích cách ứng dụng hoạt động và không khuyến nghị mua bất kỳ token nào. Binance Wallet có thể không khả dụng ở mọi quốc gia.*
