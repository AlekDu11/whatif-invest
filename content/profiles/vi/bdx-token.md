---
title: Beldex (BDX) giải thích dễ hiểu: bản fork Monero từ 2018, masternode 10.000 BDX và ứng dụng riêng tư
description: Beldex dễ hiểu: đồng coin riêng tư tách từ Monero, proof of stake từ 2021, BChat và BelNet, nguồn cung 9,9 tỷ, các rủi ro và điều người mua định kỳ cần biết.
date: 2026-11-24
kind: analysis
---
**Beldex (BDX)** là một tiền mã hóa tập trung vào quyền riêng tư: các khoản thanh toán trên blockchain của nó che giấu người gửi, người nhận và số tiền. Dự án ra mắt vào tháng 3/2018 trên mã nguồn tách ra (một bản "fork") từ Monero, và từ đó phát triển thành một bộ ứng dụng riêng tư — ứng dụng nhắn tin, VPN phi tập trung và trình duyệt — cùng chạy trên một mạng lưới. Giá trị vốn hóa hiện nay là {{mcap:bdx-token}} ({{rank:bdx-token}} trong các tiền mã hóa).

> **Điểm chính**
> - Beldex chuyển từ đào coin sang bằng chứng cổ phần (proof of stake) vào tháng 12/2021; muốn chạy một masternode phải khóa 10.000 BDX.
> - Có khoảng 9,9 tỷ BDX, nhưng các trang dữ liệu chỉ tính khoảng 7,9 tỷ là đang lưu hành — chênh lệch khoảng một phần năm.
> - Đỉnh giá cao nhất là {{ath:bdx-token}} ({{athd:bdx-token}}); giá hiện tại cách mức đó {{fromath:bdx-token}}.
> - Giống các đồng coin riêng tư khác, BDX vắng mặt trên nhiều sàn lớn nhất và có rủi ro bị hủy niêm yết.

## Cách hoạt động

Beldex khởi đầu là bản fork từ mã nguồn Monero, nên thừa hưởng cơ chế riêng tư kiểu Monero: chữ ký vòng trộn khoản thanh toán của bạn với các khoản khác, địa chỉ "ẩn" dùng một lần che giấu người nhận, và số tiền cũng được giấu đi. Ban đầu mạng chạy bằng đào coin proof of work. Với bản hard fork "Bucephalus" vào tháng 12/2021, mạng chuyển sang proof of stake: giờ đây mạng được bảo vệ bởi các masternode — máy chủ mà chủ sở hữu khóa 10.000 BDX làm tài sản đảm bảo. Đổi lại, họ nhận phần thưởng khối, và các nhóm masternode lần lượt tạo và kiểm tra khối. Cùng bản nâng cấp đó đã rút thời gian tạo khối từ 120 giây xuống 30 giây. Một phần mỗi khoản phí giao dịch bị đốt, giúp rút coin khỏi nguồn cung.

## BDX dùng để làm gì

BDX dùng để trả phí chuyển tiền riêng tư và là khoản đảm bảo mà masternode phải khóa. Các masternode cũng vận hành ứng dụng của dự án: **BChat**, ứng dụng nhắn tin mã hóa đầu cuối có tin nhắn được masternode chuyển tiếp; **BelNet**, VPN phi tập trung định tuyến lưu lượng qua masternode; **Beldex Browser** có VPN tích hợp và chặn trình theo dõi; và **Beldex Name Service (BNS)**, biến các địa chỉ dài thành tên dễ đọc. Một cầu nối (bridge) cho phép đưa BDX sang mạng khác dưới dạng token "bọc" (wrapped), chẳng hạn trên BNB Chain.

## Các con số hiện tại

- Giá hôm nay: {{price:bdx-token}}
- Đỉnh giá: {{ath:bdx-token}} ({{athd:bdx-token}}), cách đỉnh {{fromath:bdx-token}}
- Vốn hóa thị trường: {{mcap:bdx-token}} ({{rank:bdx-token}} trong các tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:bdx-token}}
- 10 USD mỗi ngày trong 3 năm: {{dca:bdx-token:3}} từ {{dcainv:3}} đã đầu tư ({{dcaroi:bdx-token:3}})

## Câu chuyện của Beldex

Beldex ra mắt vào tháng 3/2018, sau một đợt bán token (ICO) được công bố vào mùa xuân năm đó. Công ty đứng sau dự án, Beldex International, ghi Seychelles là trụ sở và Afanddy Bin Hushni là người sáng lập kiêm chủ tịch. Những năm đầu, BDX là một bản fork Monero nhỏ được đào; vào tháng 11/2019, giá của nó chỉ bằng một phần nhỏ của một xu. Việc chuyển sang proof of stake vào tháng 12/2021 biến nó thành mạng masternode, và trong những năm sau đó dự án dịch chuyển trọng tâm từ "tiền riêng tư" sang cả một hệ sinh thái riêng tư xoay quanh BChat, BelNet và trình duyệt. BDX cũng hoàn tất việc hoán đổi 1:1 token bọc của mình trên BNB Chain sang hợp đồng mới. Vào tháng 9/2026, một phân tích của Phemex đếm được khoảng 9,94 tỷ BDX trên chuỗi, trong đó khoảng 11,8 triệu đã bị đốt.

## Các lựa chọn thay thế

Đồng coin riêng tư nổi tiếng nhất là [Monero]({lang}/xmr/), nơi Beldex tách ra; Monero lớn hơn nhiều và vẫn được đào. [Zcash]({lang}/zec/) mang lại quyền riêng tư tùy chọn bằng bằng chứng không kiến thức (zero-knowledge proof), còn [Dash]({lang}/dash-token/) cũng dùng masternode nhưng với cơ chế trộn yếu hơn và chỉ là tùy chọn. Ngoài thế giới crypto, các ứng dụng của Beldex cạnh tranh với dịch vụ VPN thông thường và các ứng dụng nhắn tin mã hóa mà nhiều người đã dùng miễn phí.

## Rủi ro chính

- **Hủy niêm yết:** cơ quan quản lý gây sức ép buộc các sàn gỡ coin riêng tư; một số sàn lớn đã gỡ các đồng như Monero, và BDX chủ yếu giao dịch trên các sàn tầm trung như Gate, MEXC và KuCoin.
- **Minh bạch nguồn cung:** tổng cung khoảng 9,9 tỷ BDX, nhưng khoảng 2 tỷ không được tính là đang lưu hành, và dự án chưa giải thích rõ ai đang nắm giữ chúng.
- **Tập trung:** cơ cấu phân bổ token dành phần lớn cho phát triển hệ sinh thái (40%), nhà đầu tư hạt giống và đội ngũ; quyết định của một nhóm nhỏ có thể làm giá biến động.
- **Mạng lưới nhỏ:** bài đánh giá của Coin Bureau tháng 2/2025 cho thấy chỉ một phần nhỏ BDX được khóa trong masternode, khiến mạng dễ bị tấn công hơn các blockchain lớn.
- **Thanh khoản mỏng và mã trùng tên:** khối lượng giao dịch hằng ngày nhỏ so với vốn hóa, và các mã gần giống (như BDXN) hoặc token bọc không chính thức có thể khiến người mua nhầm lẫn.

## Ý nghĩa nếu bạn mua định kỳ

BDX là đồng coin nhỏ với thanh khoản mỏng: giá có thể dao động mạnh và khả năng mua bán phụ thuộc vào vài sàn. Mua một số tiền cố định đều đặn giúp trải đều các lần mua theo thời gian thay vì cố đoán đáy — nhưng không loại bỏ rủi ro thua lỗ, cũng như rủi ro sàn hủy niêm yết đồng coin. Nhiều người chỉ dành cho những đồng coin riêng tư nhỏ như thế này một phần rất nhỏ trong khoản tiết kiệm mà họ chấp nhận mất. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Beldex price, supply and project information (CoinMarketCap)](https://coinmarketcap.com/currencies/beldex/)
- [Beldex review: proof of stake, masternodes, BChat and BelNet (Coin Bureau, February 2025)](https://coinbureau.com/review/beldex-review)
- [Beldex POS chain launches with Bucephalus hard fork (press release via Nasdaq, 30 November 2021)](https://www.nasdaq.com/press-release/beldex-pos-chain-launches-with-bucephalus-hard-fork-2021-11-30)
- [What is Beldex and why 2 billion BDX are unlisted (Phemex, 2026)](https://phemex.com/blogs/what-is-beldex-and-why-2-billion-bdx-are-unlisted)
- [Beldex price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/beldex)
