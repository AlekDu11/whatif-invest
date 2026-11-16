---
title: DEX là gì và khác gì so với sàn giao dịch crypto thông thường?
description: DEX là gì? Giải thích dễ hiểu về sàn phi tập trung: AMM, pool thanh khoản, ví, phí gas, cùng ưu và nhược điểm khi so với sàn tập trung (CEX).
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**DEX là gì?** DEX (sàn giao dịch phi tập trung) là tập hợp các hợp đồng thông minh trên blockchain cho phép bạn đổi token này lấy token khác trực tiếp từ ví của mình. Không có công ty nào giữ tiền của bạn, không cần tài khoản và thường không cần xác minh danh tính. Uniswap trên Ethereum, cùng Raydium, Orca và Meteora trên Solana, là những ví dụ nổi tiếng.

Một sàn crypto thông thường như Binance, Coinbase hay Kraken là **CEX** (sàn tập trung): một công ty giữ tiền của bạn, khớp lệnh người mua và người bán trong hệ thống riêng và phải tuân thủ các quy định tài chính.

## DEX hoạt động như thế nào

### Nhà tạo lập thị trường tự động (AMM)

Hầu hết DEX không có sổ lệnh gồm người mua và người bán. Thay vào đó, chúng dùng **nhà tạo lập thị trường tự động** (automated market maker), tức một công thức để định giá.

Phiên bản kinh điển, được Uniswap v2 sử dụng, là quy tắc "tích số không đổi" (constant product): một pool chứa hai token, và số lượng token A nhân với số lượng token B phải giữ nguyên sau mỗi giao dịch. Khi bạn mua token A, bạn thêm token B vào pool và lấy token A ra, nên A trở nên khan hiếm hơn trong pool và giá của nó tăng.

Bạn không cần tự tính toán. Ý chính là: **pool càng lớn, giao dịch của bạn càng ít làm giá biến động.**

### Pool thanh khoản

Token trong pool đến từ **nhà cung cấp thanh khoản**: những người gửi vào các cặp token và nhận một phần phí giao dịch (thường 0,05–1% mỗi lần swap). Rủi ro của họ là giá hai token lệch xa nhau, khiến họ có thể thiệt hơn so với chỉ giữ nguyên token ("tổn thất tạm thời", impermanent loss).

Với các token mới ra mắt, người tạo thường là người lập pool đầu tiên. Đó là lý do việc khóa thanh khoản quan trọng: ai kiểm soát pool thì có thể rút nó.

### Ví chính là tài khoản của bạn

Để dùng DEX, bạn kết nối một ví tự lưu ký như MetaMask (Ethereum và các mạng tương tự) hoặc Phantom (Solana). Mỗi giao dịch là một giao dịch do chính bạn ký. **Seed phrase** là chìa khóa chủ: mất nó là mất tiền; chia sẻ nó là người khác lấy tiền.

### Gas và các loại phí

Mỗi giao dịch trên DEX đều trả phí mạng, trên Ethereum gọi là **gas**. Trên Ethereum, phí này tăng khi mạng đông; các mạng Layer-2 và Solana thường rẻ hơn nhiều, phí cơ bản của Solana là 0,000005 SOL cho mỗi chữ ký. Ngoài gas, bạn còn trả phí pool, và có thể gặp **slippage** và **tác động giá** với các token nhỏ hoặc biến động nhanh.

## DEX và CEX: những khác biệt chính

- **Ai giữ tiền của bạn:** trên DEX là bạn (ví của bạn); trên CEX là sàn.
- **Tài khoản và xác minh danh tính:** DEX thường không cần; CEX yêu cầu xác minh danh tính (KYC).
- **Lựa chọn token:** DEX có gần như mọi token, kể cả token mới toanh; CEX chỉ niêm yết các token được chọn lọc.
- **Mua bằng thẻ hoặc chuyển khoản ngân hàng:** thường không làm trực tiếp được trên DEX; là tiêu chuẩn trên CEX.
- **Phí:** DEX có gas, phí pool và slippage; CEX có phí giao dịch, chênh lệch giá (spread) và phí rút.
- **Hỗ trợ khi có sự cố:** DEX không có tổng đài hỗ trợ; CEX có chăm sóc khách hàng và đôi khi có cơ chế bảo vệ.
- **Rủi ro chính:** DEX là token lừa đảo, phê duyệt sai và lỗi của chính bạn; CEX là bị hack, bị khóa tài khoản và phá sản.

## Ưu điểm của DEX

- **Tự lưu ký.** Không ai có thể đóng băng tài khoản hay làm mất tiền của bạn trong một vụ phá sản.
- **Truy cập mở.** Bất kỳ ai có ví đều giao dịch được, từ gần như mọi nơi.
- **Có token mới trước tiên.** Token xuất hiện trên DEX từ rất lâu trước khi (hoặc thay vì) được niêm yết trên sàn.
- **Minh bạch.** Pool, giao dịch và holder đều hiển thị trên blockchain.

## Nhược điểm của DEX

- **Bạn là ngân hàng.** Chỉ một sai sót (sai địa chỉ, trang web giả, phê duyệt độc hại) là tiền mất vĩnh viễn.
- **Token lừa đảo.** Ai cũng có thể tạo token và pool chỉ trong vài phút. Hầu hết token mới mất gần như toàn bộ giá trị; xem [danh sách kiểm tra rug pull]({lang}/blog/how-to-spot-a-rug-pull/) của chúng tôi.
- **Chi phí ẩn.** Slippage và tác động giá có thể tốn hơn cả mức phí hiển thị.
- **Khó nạp tiền ban đầu.** Thường bạn phải mua crypto trên CEX trước rồi chuyển về ví.
- **Rủi ro hợp đồng thông minh.** Lỗi hoặc các vụ hack trong mã nguồn DEX đã gây ra những thiệt hại lớn.

## Người mới nên dùng loại nào?

Nhiều người dùng cả hai: một CEX được cấp phép để đổi tiền nội tệ sang crypto, và một DEX cho các token chỉ có on-chain. Để mua định kỳ, dài hạn các tài sản lớn như Bitcoin hay Ethereum, một CEX phí thấp thường đơn giản hơn; hãy so sánh các lựa chọn trên [trang sàn giao dịch]({lang}/exchanges/) của chúng tôi.

Nếu bạn muốn tìm hiểu memecoin và các token on-chain khác, hãy bắt đầu với số tiền thật nhỏ, một ví riêng, và những đồng có tiếng nhất trên [trang memecoin]({lang}/memes/) của chúng tôi. Hướng dẫn từng bước [cách mua memecoin trên Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) trình bày toàn bộ quy trình, kể cả các công cụ như [GMGN](/go/gmgn?from=blog&l=vi).

## Thuật ngữ DEX thường gặp

- **Swap**: đổi một token lấy token khác.
- **Pair (cặp)**: hai token trong một pool, ví dụ SOL/USDC.
- **Slippage tolerance (mức trượt giá chấp nhận)**: mức thay đổi giá tối đa bạn chấp nhận.
- **Approve (phê duyệt)**: quyền cho một hợp đồng chuyển token khỏi ví của bạn (chủ yếu trên các mạng kiểu Ethereum). Hãy thu hồi các phê duyệt cũ không còn cần đến.
- **Aggregator (bộ tổng hợp)**: dịch vụ chia giao dịch của bạn qua nhiều DEX để có giá tốt hơn, như Jupiter trên Solana hay 1inch trên Ethereum.

## Câu hỏi thường gặp

### DEX có an toàn hơn CEX không?

DEX loại bỏ rủi ro sàn làm mất hoặc đóng băng tiền của bạn, nhưng thêm rủi ro từ lỗi của chính bạn và token lừa đảo. Không bên nào là không có rủi ro.

### Dùng DEX có cần giấy tờ tùy thân không?

Thường là không, vì bạn giao dịch từ ví của chính mình. Tuy vậy, luật pháp và thuế tại nơi bạn sống vẫn áp dụng.

### Vì sao giao dịch trên DEX của tôi thất bại?

Các lý do thường gặp: không đủ coin gốc để trả gas, slippage đặt quá thấp so với giá biến động nhanh, hoặc token chặn việc bán.

### Giao dịch trên DEX có phải chịu thuế không?

Ở nhiều quốc gia là có: một lần swap từ token này sang token khác có thể được tính là một lần bán. Hãy lưu lại lịch sử giao dịch.

## Nguồn

- [Cách Uniswap hoạt động (tài liệu Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas và phí (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Tài liệu Solana: cấu trúc phí](https://solana.com/docs/core/fees/fee-structure)

*Không phải lời khuyên đầu tư. Bài hướng dẫn này giải thích cách DEX hoạt động và không khuyến nghị bất kỳ nền tảng hay token nào.*
