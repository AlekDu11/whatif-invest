---
title: Fluid (FLUID) giải thích dễ hiểu: giao thức cho vay và giao dịch của Instadapp, giới hạn 100 triệu token
description: Fluid bằng ngôn ngữ đơn giản: lớp thanh khoản chung cho vay và giao dịch hoạt động ra sao, smart collateral và debt, đổi tên từ INST, đối thủ, rủi ro.
date: 2026-11-27
kind: analysis
---
**Fluid** là giao thức tài chính phi tập trung (DeFi), nơi mọi người cho vay, vay và hoán đổi tiền mã hóa từ một bể tiền chung. Giao thức do đội ngũ đứng sau Instadapp xây dựng, một trong những ứng dụng DeFi lâu đời nhất trên Ethereum, và đầu năm 2025 token cũ INST được đổi tên thành FLUID. Vốn hóa hiện là {{mcap:fluid}} ({{rank:fluid}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Tổng cộng có 100 triệu token FLUID; việc đổi tên từ INST giữ nguyên nguồn cung và địa chỉ token.
> - Đỉnh kỷ lục, lập khi còn mang tên INST, là {{ath:fluid}} ({{athd:fluid}}); giá hiện tại cách đỉnh {{fromath:fluid}}.
> - Trên Fluid, cùng một khoản tiền gửi làm việc hai lần — vừa là tài sản thế chấp khoản vay vừa là thanh khoản giao dịch — nên người dùng có thể nhận cùng lúc phí cho vay và phí giao dịch.
> - Tháng 12/2024, ba tuần sau khi ra mắt, sàn của Fluid đã xử lý hơn 1 tỷ USD giao dịch.

## Cách hoạt động

Phần lớn ứng dụng DeFi tách cho vay và giao dịch thành các bể riêng. Fluid đưa mọi khoản tiền gửi vào một "lớp thanh khoản" duy nhất, và các ứng dụng khác nhau — thị trường tiền tệ, vault và sàn giao dịch phi tập trung (DEX) — cùng lấy vốn từ đó. Với "smart collateral", số coin bạn thế chấp cho khoản vay cũng được dùng làm thanh khoản giao dịch trên DEX và kiếm phí swap. Với "smart debt", số tiền bạn vay cũng được đưa vào làm thanh khoản, nên phí giao dịch có thể trả bớt một phần tiền lãi. Mọi thứ chạy bằng hợp đồng thông minh, tức chương trình trên blockchain, chủ yếu trên Ethereum và cả các mạng layer-2 như Arbitrum và Base. Năm 2025, sàn Jupiter trên Solana ra mắt ứng dụng cho vay Jupiter Lend, xây dựng bằng công nghệ của Fluid.

## Token dùng để làm gì

FLUID là token quản trị: người nắm giữ bỏ phiếu về mức phí, thị trường mới và cách chi tiêu ngân quỹ. Đề xuất đổi tên tháng 12/2024 cũng lên kế hoạch mua lại token khi doanh thu của giao thức đạt khoảng 10 triệu USD mỗi năm, để một phần phí mà Fluid thu được quay về token. FLUID không trả cổ tức, và giá trị của nó phụ thuộc vào việc giao thức kiếm được bao nhiêu và bao nhiêu trong số đó đến tay người nắm giữ.

## Các con số hiện tại

- Giá hôm nay: {{price:fluid}}
- Đỉnh kỷ lục: {{ath:fluid}} ({{athd:fluid}}), cách đỉnh {{fromath:fluid}}
- Vốn hóa thị trường: {{mcap:fluid}} ({{rank:fluid}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:fluid}}
- 10 USD mỗi ngày trong 1 năm: {{dca:fluid:1}} từ {{dcainv:1}} đã đầu tư ({{dcaroi:fluid:1}})

## Câu chuyện của Fluid

Instadapp được hai anh em Sowmay và Samyak Jain thành lập năm 2018, ban đầu là một bảng điều khiển đơn giản để dùng nhiều ứng dụng DeFi cùng lúc. Token quản trị INST ra mắt tháng 6/2021, giữa cơn sốt DeFi, và lên khoảng 24 USD ngay trong tháng đó trước khi mất hơn 95% đến cuối năm 2022. Sau khoảng hai năm phát triển, đội ngũ ra mắt giao thức cho vay Fluid năm 2024 và DEX vào tháng 11/2024, sàn này nhanh chóng trở thành một trong những sàn lớn nhất trên Ethereum tính theo khối lượng. Sau đó người nắm giữ chấp thuận chuyển đổi INST sang FLUID theo tỷ lệ một đổi một, và từ năm 2025 token giao dịch dưới tên FLUID, chủ yếu trong khoảng 1,50–6 USD.

## Các lựa chọn thay thế

[Aave]({lang}/aave/) là giao thức cho vay DeFi lớn nhất, còn [Morpho]({lang}/morpho/) là đối thủ đang tăng trưởng nhanh. Về giao dịch, DEX của Fluid cạnh tranh với [Uniswap]({lang}/uni/) và [Curve DAO]({lang}/crv/). Trên Solana, [Jupiter]({lang}/jup/) vừa là đối tác vừa là đối thủ.

## Rủi ro chính

- **Biến động mạnh:** token này từng mất hơn 95% giá trị; token DeFi có thể giảm rất nhanh trong thị trường gấu.
- **Rủi ro hợp đồng thông minh:** một lỗi hoặc vụ hack ở lớp thanh khoản chung có thể ảnh hưởng cùng lúc đến cả cho vay lẫn giao dịch.
- **Thanh lý:** khoản vay thế chấp bằng coin biến động mạnh sẽ bị bán tự động khi giá giảm, có thể gây phản ứng dây chuyền khi thị trường sập.
- **Giá trị cho người nắm giữ:** việc mua lại phụ thuộc vào mục tiêu doanh thu và các cuộc bỏ phiếu quản trị; phí có thể không đến được token như kỳ vọng.
- **Tập trung và pháp lý:** đội ngũ và nhà đầu tư sớm nắm tỷ trọng lớn, còn quy định về DeFi vẫn đang được soạn thảo ở nhiều nước.

## Ý nghĩa nếu bạn mua định kỳ

Dưới tên FLUID, token này có lịch sử ngắn, và các lần mua định kỳ từ năm 2025 chủ yếu diễn ra khi giá đang giảm. Mua một khoản cố định đều đặn giúp dàn trải rủi ro thời điểm, nhưng kết quả vẫn phụ thuộc vào việc giao thức có tiếp tục tăng doanh thu phí hay không. Nhiều người chỉ để token DeFi chiếm một phần nhỏ tiền tiết kiệm, phần mà họ chấp nhận được nếu giảm mạnh. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Trang chính thức và tài liệu của Fluid (fluid.io)](https://fluid.io/)
- [Instadapp proposes rebrand and new tokenomics following Fluid launch (The Defiant, 4/12/2024)](https://thedefiant.io/news/defi/instadapp-proposes-rebrand-and-new-tokenomics-following-fluid-launch)
- [DeFi superapp Fluid is coming for Aave and Uniswap's lunch (Blockworks)](https://blockworks.co/news/defi-superapp-competitor-to-aave-uniswap)
- [Giá, vốn hóa và đỉnh lịch sử của Fluid (CoinGecko)](https://www.coingecko.com/en/coins/instadapp)
