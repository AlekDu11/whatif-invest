---
title: "Xác thực hai yếu tố (2FA): cách bật từng bước"
description: 2FA thêm một ổ khóa thứ hai cho tài khoản sàn của bạn. Cách bật ứng dụng xác thực hoặc passkey từng bước, và vì sao mã SMS là lựa chọn yếu nhất.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 triệu USD
stat_label: bị mất vì lừa đảo SIM swap năm 2021 qua 1.611 đơn tố cáo gửi FBI (IC3, tháng 2/2022)
---
**2FA là gì và bật nó thế nào?** Xác thực hai yếu tố (2FA) nghĩa là muốn đăng nhập hoặc rút tiền thì cần hai thứ: mật khẩu *và* một bằng chứng thứ hai, chẳng hạn mã 6 chữ số từ ứng dụng trên điện thoại hoặc passkey (vân tay hay khuôn mặt của bạn). Hãy bật nó trong phần **Security** (Bảo mật) của sàn và dùng ứng dụng xác thực hoặc passkey thay vì SMS.

> **Điểm chính**
> - Có 2FA, kẻ gian chỉ trộm được mật khẩu thôi thì không đủ để rút sạch tài khoản của bạn.
> - **Mã SMS là lựa chọn yếu nhất:** trong chiêu "SIM swap", kẻ gian chuyển số điện thoại của bạn sang thẻ SIM của chúng và nhận luôn mã của bạn. FBI ghi nhận 1.611 đơn tố cáo kiểu này và thiệt hại hơn **68 triệu USD** năm 2021, tăng từ 320 đơn và khoảng 12 triệu USD trong giai đoạn 2018–2020.
> - FBI khuyên dùng các lựa chọn mạnh hơn: ứng dụng xác thực, sinh trắc học hoặc khóa bảo mật vật lý.

## Các lựa chọn, từ yếu nhất đến mạnh nhất

- **Mã SMS** — tin nhắn chứa mã. Có còn hơn không, nhưng số điện thoại của bạn có thể bị đánh cắp.
- **Mã qua e-mail** — chỉ an toàn bằng tài khoản e-mail của bạn (hãy bảo vệ nó bằng 2FA luôn).
- **Ứng dụng xác thực** (Google Authenticator, Microsoft Authenticator và tương tự) — ứng dụng trên điện thoại tạo mã 6 chữ số mới mỗi 30 giây, kể cả khi không có mạng. Không ai chặn được mã này qua nhà mạng của bạn.
- **Passkey** (sinh trắc học) — bạn xác nhận bằng vân tay, khuôn mặt hoặc mã PIN điện thoại. Passkey chỉ hoạt động trên trang thật, nên trang giả không lấy cắp được.
- **Khóa bảo mật vật lý** (thiết bị nhỏ USB/NFC) — mạnh nhất, phù hợp khi số tiền lớn.

## Từng bước: ứng dụng xác thực (ví dụ trên ứng dụng Binance)

Các sàn khác làm gần như y hệt; hãy tìm mục **Security** (Bảo mật) trong hồ sơ của bạn.

1. **Bước 1 — Cài ứng dụng.** Tải Google Authenticator (hoặc ứng dụng xác thực khác) từ App Store hoặc Google Play chính thức.
2. **Bước 2 — Mở cài đặt bảo mật.** Trong ứng dụng Binance, chạm biểu tượng **Account**, chạm vào hồ sơ ở trên cùng, rồi chọn **Security**.
3. **Bước 3 — Bắt đầu cài đặt.** Chạm **Authenticator App**, rồi **Enable**. Bạn sẽ thấy một mã QR và một **setup key** (khóa thiết lập, là một dãy mã dài).
4. **Bước 4 — Chép setup key ra giấy.** Đây là bản dự phòng nếu bạn mất điện thoại. Cất offline, giống như seed phrase. Đừng chạm **Next** vội.
5. **Bước 5 — Thêm tài khoản vào ứng dụng xác thực.** Trong Google Authenticator chạm **+**, chọn **Enter a setup key** (hoặc quét mã QR), dán khóa, gõ tên ví dụ "Binance", rồi chạm **Add**.
6. **Bước 6 — Xác nhận.** Quay lại Binance, chạm **Next** và nhập mã 6 chữ số từ ứng dụng. Bạn sẽ thấy thông báo thành công.
7. **Bước 7 — Thử lại.** Đăng xuất rồi đăng nhập lại. Nếu được hỏi mã, nghĩa là 2FA đã hoạt động.

## Từng bước: passkey (còn đơn giản hơn)

Theo trang trợ giúp của Binance, bạn cần ứng dụng phiên bản 2.60+, iOS 16+ hoặc Android 9+.

1. **Account → hồ sơ → Security → Passkeys (Biometrics) → Add Passkey.**
2. Xác nhận bằng 2FA hiện tại nếu được hỏi, rồi chạm **Continue**.
3. Chọn nơi lưu: iCloud Keychain (iPhone), Google Password Manager (Android) hoặc khóa bảo mật, rồi xác nhận bằng vân tay, khuôn mặt hoặc mã PIN.

## Sau khi đã bật 2FA

- Tắt SMS làm phương thức đăng nhập nếu sàn cho phép, hoặc ít nhất nhờ nhà mạng khóa SIM / đặt mã PIN chống chuyển số.
- Bảo vệ e-mail liên kết với sàn bằng 2FA nữa.
- Bật **withdrawal whitelist** (danh sách rút tiền cho phép: chỉ địa chỉ đã lưu mới nhận được tiền) nếu sàn của bạn có.

> **⚠️ Cẩn thận**
> - **Người thật không bao giờ hỏi mã 2FA của bạn.** "Hỗ trợ" trên Telegram, người gọi tự nhận từ "sàn" hay "ngân hàng" đòi mã 6 chữ số luôn là kẻ lừa đảo.
> - **Mất điện thoại mà không có khóa dự phòng.** Khi đó khôi phục tài khoản mất nhiều ngày xác minh danh tính. Hãy chép setup key ra giấy và cất kỹ.
> - **Ứng dụng xác thực giả và trang đăng nhập nhái.** Chỉ cài ứng dụng từ kho chính thức, tự gõ địa chỉ sàn hoặc dùng bookmark.

## Ý nghĩa nếu bạn mua đều đặn

Nếu mỗi tháng bạn mua một ít, tài khoản sàn của bạn dần thành một khoản tiền thật — ví dụ bitcoin hiện ở mức {{price:btc}} ({{chg1y:btc}} trong 12 tháng), kết quả quá khứ, không phải dự báo. Mười phút cài 2FA bảo vệ nhiều năm tích lũy. Theo dõi tài sản của bạn trên [trang danh mục]({lang}/me/).

Bài trước: [seed phrase: 5 quy tắc giữ an toàn]({lang}/blog/seed-phrase-safety-rules/). Xem thêm: [cách đăng ký sàn crypto]({lang}/blog/how-to-register-on-a-crypto-exchange/), [các sàn dùng được ở nước bạn]({lang}/exchanges/). Tất cả bài học có trên [trang Học]({lang}/learn/).

## Nguồn

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8/2/2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (cập nhật 10/12/2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (cập nhật 10/12/2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Không phải lời khuyên đầu tư.*
