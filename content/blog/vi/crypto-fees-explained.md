---
title: "Giải thích phí crypto: phí giao dịch, spread và phí mạng"
description: Mỗi lần mua hay rút crypto đều có ba khoản phí ẩn — phí giao dịch, spread và phí mạng. Cách từng loại hoạt động và cách xem trước khi xác nhận.
date: 2026-11-26T13:40:00Z
category: learn
track: crypto
step: 8
assets: btc, eth, bnb
stat: 3 loại phí
stat_label: phí giao dịch, spread và phí mạng — kiểm tra cả ba trước khi bấm Xác nhận
---
**Thực ra bạn trả bao nhiêu khi mua, bán hay gửi crypto?** Thường là ba khoản: **phí giao dịch** (hoa hồng của sàn), **spread** (chênh lệch giữa giá mua và giá bán) và, khi coin rời khỏi sàn, **phí mạng** (trả cho blockchain). Cách dễ nhất để thấy hết cùng lúc là dòng "bạn sẽ nhận được" trên màn hình xác nhận.

> **Điểm chính**
> - Ví dụ phí giao dịch cho người dùng thường của Binance là **0,1%** giá trị lệnh — 1 USD cho lệnh mua 1.000 USD — và trả phí bằng BNB được **giảm tới 25%** (trang hỗ trợ của Binance, cập nhật tháng 1–2/2026).
> - Nút "Mua" đơn giản và thanh toán bằng thẻ thường đắt hơn sổ lệnh (order book), vì giá đã gồm spread và đôi khi cả phí thẻ.
> - Phí mạng Bitcoin phụ thuộc vào **kích thước** dữ liệu của giao dịch và mức độ đông đúc của mạng — **không phụ thuộc vào số tiền bạn gửi**.

## Phí 1 — phí giao dịch

Đây là khoản sàn thu để thực hiện giao dịch. Nó tính theo phần trăm số tiền.

- Ví dụ của chính Binance dùng mức 0,1% cho người dùng thường: mua 10 ETH mất phí 0,01 ETH. Phí được trừ bằng đồng bạn **nhận về** — mua ETH thì trả phí bằng ETH, bán lấy USDC thì trả phí bằng USDC.
- Nhiều sàn có hai mức phí: **maker** (lệnh của bạn nằm chờ trong danh sách đến khi có người khớp, ví dụ lệnh giới hạn thấp hơn giá hiện tại) và **taker** (lệnh khớp ngay theo giá hiện tại). Phí maker thường bằng hoặc rẻ hơn.
- Người giao dịch lớn được mức phí thấp hơn (cấp VIP). Người mới trả mức phí tiêu chuẩn.

**Bước 1 — Tìm trang phí.** Sàn lớn nào cũng có trang tên **Fees** hoặc **Fee schedule** (trên Binance: hồ sơ của bạn → **Fees & Transactions Overview**). Xem mức phí spot cho cấp của bạn.

**Bước 2 — Bật các ưu đãi bạn đã đủ điều kiện.** Trên Binance, giữ một ít BNB trong tài khoản Spot và bật **Using BNB Deduction** (menu Fee Level, hoặc trong ứng dụng: Account Center → Settings → BNB Discount). Binance cho biết cách này giảm tới 25% phí spot. Bạn không cần mua BNB chỉ để làm việc này; nó chỉ có ích nếu bạn đã có sẵn BNB.

## Phí 2 — spread

**Spread** là chênh lệch giữa giá bạn có thể mua và giá bạn có thể bán ở cùng một thời điểm. Nếu mua rồi bán ngay, bạn mất phần spread dù hoa hồng bằng 0.

- Trên màn hình giao dịch chính (sổ lệnh) của coin lớn như Bitcoin, spread thường rất nhỏ.
- Trên **màn hình đơn giản Mua / Bán / Convert (Chuyển đổi)**, sàn hiển thị một mức giá đã gồm phần lời của họ. Ví dụ, Coinbase ghi trong phần công bố giá rằng mua bán đơn giản có cộng spread ngoài phí.
- Với coin nhỏ và memecoin, spread có thể lên vài phần trăm vì ít người giao dịch.

**Bước 3 — So sánh hai mức giá.** Trước khi mua kiểu đơn giản, mở biểu đồ của coin đó trên cùng sàn (hoặc trên [trang Bitcoin]({lang}/btc/) của chúng tôi) và so giá thị trường với giá trên màn hình xác nhận. Phần chênh lệch xấp xỉ là spread bạn phải chịu.

**Bước 4 — Để ý phí thẻ.** Mua bằng thẻ ngân hàng là cách vào nhanh nhất, và thường đắt nhất: sàn và đối tác thanh toán thường cộng phí thẻ vài phần trăm. Chuyển khoản ngân hàng hoặc P2P trên sàn thường rẻ hơn nhưng chậm hơn — xem [cách mua Bitcoin bằng thẻ ngân hàng]({lang}/blog/how-to-buy-bitcoin-with-a-bank-card/).

## Phí 3 — phí mạng

Khi bạn **rút** coin về ví riêng hoặc sang sàn khác, giao dịch chuyển được ghi lên blockchain. Những người vận hành mạng (thợ đào hoặc validator) thu phí cho việc này.

- Trên Bitcoin, phí tính bằng satoshi trên mỗi byte ảo (sat/vB; một satoshi là một phần trăm triệu bitcoin). Một giao dịch thanh toán đơn giản khoảng 140 vB, nên gửi 0,01 BTC hay 9 BTC trong cùng kiểu giao dịch đều tốn như nhau.
- Khi nhiều người gửi cùng lúc, phí tăng; khi mạng vắng, phí giảm.
- Sàn hiển thị **phí rút** để trả khoản này, đôi khi cao hơn phí mạng thật. Phí rút thường là một lượng coin cố định, không phải phần trăm — nên rút ít thì thiệt nhiều nhất.
- Cùng một coin nhưng khác mạng thì phí có thể chênh rất xa (USDT trên mạng này chỉ vài xu, trên mạng khác vài đô). Hãy chọn mạng mà địa chỉ nhận hỗ trợ — xem [cách rút crypto về ví của riêng bạn]({lang}/blog/how-to-withdraw-crypto-to-your-own-wallet/).

**Bước 5 — Đọc màn hình rút trước khi xác nhận.** Ở đó có mạng, phí và "số tiền nhận được". Nếu phí lớn so với số tiền, hãy chờ và gửi một lần với số tiền lớn hơn thay vì gửi nhiều lần nhỏ.

## Bước 6 — Ghi lại

Thêm mỗi lần mua cùng chi phí thực vào [danh mục của bạn]({lang}/me/). Khi đó kết quả cho thấy số tiền bạn thực sự đã trả, chứ không chỉ là mức thay đổi giá của coin.

> **⚠️ Cẩn thận**
> - **Băng rôn "miễn phí".** Một giao dịch có thể không mất hoa hồng nhưng vẫn có spread rộng. Luôn nhìn con số "bạn sẽ nhận được".
> - **Rút nhiều lần nhỏ.** Phí rút cố định vài đô cho một lần chuyển 20 USD là phần không nhỏ trong số tiền của bạn.
> - **Chọn sai mạng để tiết kiệm vài xu.** Nếu bên nhận không hỗ trợ mạng đó, coin có thể mất. Hãy thử trước với một khoản nhỏ.

## Ý nghĩa nếu bạn mua đều đặn

Nếu mỗi tuần bạn mua một ít, phí sẽ cộng dồn: 0,1% mỗi lần mua là nhỏ, nhưng phí thẻ vài phần trăm mỗi lần thì không. Người mua đều đặn thường nạp tiền bằng chuyển khoản ngân hàng, dùng tính năng mua định kỳ (recurring buy) trên thị trường chính, và chỉ thỉnh thoảng mới rút về ví riêng trong một lần chuyển lớn hơn. Ví dụ từ máy tính của chúng tôi: 10 USD mỗi ngày vào Bitcoin trong 3 năm (tổng cộng {{dcainv:3}}) đã thành {{dca:btc:3}} ({{dcaroi:btc:3}}), chưa tính phí. Đây là kết quả quá khứ, không phải dự báo. Bitcoin hiện ở mức {{price:btc}}.

Bài trước: [Cách bán crypto và rút tiền về tài khoản ngân hàng]({lang}/blog/how-to-sell-crypto-and-withdraw-to-bank/). So sánh các sàn trên [trang sàn giao dịch]({lang}/exchanges/) của chúng tôi; tất cả bài học ở [trang Học]({lang}/learn/).

## Nguồn

- [Binance Support: How to calculate Binance spot trading fees (cập nhật tháng 1/2026)](https://www.binance.com/en/support/faq/detail/e85d6e703b874674840122196b89780a)
- [Binance Support: How to use BNB to pay for fees and get a 25% discount (cập nhật tháng 2/2026)](https://www.binance.com/en/support/faq/115000583311)
- [Coinbase Help: Pricing and fees disclosures](https://help.coinbase.com/en/coinbase/getting-started/getting-started-with-coinbase/pricing-and-fees)
- [Bitcoin.org: Bitcoin fees](https://bitcoin.org/fees/)
- [Ledger Academy: Bitcoin fees explained (tháng 4/2026)](https://www.ledger.com/academy/bitcoin-fees)

*Không phải lời khuyên đầu tư.*
