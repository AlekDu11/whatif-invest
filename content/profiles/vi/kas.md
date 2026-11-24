---
title: Kaspa (KAS) giải thích dễ hiểu: blockDAG bằng chứng công việc từ 2021, 10 khối mỗi giây và tối đa 28,7 tỷ
description: Kaspa dễ hiểu: blockDAG và GHOSTDAG hoạt động thế nào, ra mắt công bằng không premine, nâng cấp Crescendo và Toccata, lịch sử và rủi ro chính.
date: 2026-11-24
kind: analysis
---
**Kaspa** là đồng tiền mã hóa bằng chứng công việc (proof of work), được đào như bitcoin nhưng thiết kế để nhanh hơn nhiều: thay vì một chuỗi khối duy nhất, nó dùng "blockDAG", nơi nhiều khối có thể được thêm vào cùng lúc. Kaspa ra mắt tháng 11/2021 không premine và không bán token, và vốn hóa đồng **KAS** hiện là {{mcap:kas}} ({{rank:kas}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Sẽ không bao giờ có quá khoảng 28,7 tỷ KAS, và đến cuối năm 2026 khoảng 97% số đó đã được đào.
> - Đỉnh kỷ lục là {{ath:kas}} ({{athd:kas}}); hôm nay giá cách đỉnh {{fromath:kas}}.
> - Từ bản nâng cấp Crescendo tháng 5/2025, mạng tạo 10 khối mỗi giây thay vì một.
> - Kaspa không có premine, không bán trước và không có coin dành riêng cho nhà sáng lập — mọi KAS đều đến từ việc đào.

## Cách hoạt động

Ở bitcoin, nếu hai thợ đào tìm ra khối cùng lúc, một khối sẽ bị bỏ đi, nên khối phải chậm (khoảng 10 phút một khối). Kaspa giữ lại tất cả các khối song song đó và nối chúng thành một đồ thị — **blockDAG** (đồ thị có hướng không chu trình). Giao thức **GHOSTDAG**, dựa trên nghiên cứu học thuật của Yonatan Sompolinsky và Aviv Zohar, sau đó sắp xếp mọi khối và giao dịch theo một thứ tự chung. Nhờ vậy Kaspa tạo khối rất thường xuyên và xác nhận thanh toán trong vài giây, vẫn giữ cách đào kiểu bitcoin với thuật toán riêng kHeavyHash. Lượng phát hành giảm dần đều: phần thưởng giảm một chút mỗi tháng và giảm một nửa khoảng mỗi năm một lần.

## Vì sao người ta cho rằng nó có giá trị

Người ủng hộ xem Kaspa như "bạc kỹ thuật số tốc độ cao": nó giữ những gì người ta thích ở bitcoin — bằng chứng công việc, nguồn cung cố định, không có công ty và không có coin chia trước — nhưng thanh toán hoàn tất trong vài giây thay vì vài phút. Việc ra mắt công bằng quan trọng với nhiều người nắm giữ, vì không đội ngũ hay quỹ nào nhận coin giá rẻ để bán về sau. Năm 2026 mạng còn bắt đầu có khả năng lập trình: bản nâng cấp Toccata mang đến covenant (quy tắc về cách tiêu coin), xác minh bằng chứng không tiết lộ (zero-knowledge) và token gốc, giúp nhà phát triển xây ứng dụng trên Kaspa.

## Các con số hiện tại

- Giá hôm nay: {{price:kas}}
- Đỉnh kỷ lục: {{ath:kas}} ({{athd:kas}}), cách đỉnh {{fromath:kas}}
- Vốn hóa thị trường: {{mcap:kas}} ({{rank:kas}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:kas}}
- 10 USD mỗi ngày trong 3 năm: {{dca:kas:3}} từ {{dcainv:3}} đã đầu tư ({{dcaroi:kas:3}})

## Câu chuyện của Arbitrum

Kaspa ra đời từ các nghiên cứu và công ty DAGlabs; mạng chính chạy từ ngày 7/11/2021. Năm đầu, coin chỉ được giao dịch trên các sàn nhỏ với giá vài phần trăm xu. Năm 2023 các sàn lớn hơn niêm yết, giá tăng gấp nhiều lần và đạt kỷ lục khoảng 0,21 USD vào giữa năm 2024. Các nhà phát triển viết lại phần mềm nút bằng Rust ("Rusty Kaspa"), giúp bước nhảy tốc độ trở thành hiện thực: ngày 5/5/2025, hard fork Crescendo nâng mạng từ một lên mười khối mỗi giây. Giá giảm mạnh trong năm 2025 và 2026, và năm 2026 hard fork Toccata biến Kaspa thành một layer 1 có thể lập trình.

## Các lựa chọn thay thế

Kaspa cạnh tranh trực tiếp nhất với các đồng thanh toán bằng chứng công việc khác như [Bitcoin]({lang}/btc/), [Litecoin]({lang}/ltc/) và [Bitcoin Cash]({lang}/bch/). Với chuyển tiền nhanh, rẻ và ứng dụng, người ta cũng dùng các mạng bằng chứng cổ phần như [Solana]({lang}/sol/), còn thanh toán hằng ngày thì nhiều người chỉ dùng stablecoin đô la.

## Rủi ro chính

- **Biến động mạnh:** KAS đã từng giảm hơn 80% so với kỷ lục năm 2024; điều đó có thể lặp lại.
- **Tập trung khai thác:** một vài pool lớn và nhà sản xuất ASIC kiểm soát phần lớn sức mạnh băm.
- **Đội ngũ nhỏ:** việc phát triển dựa vào một nhóm nhà phát triển cốt lõi được tài trợ chủ yếu bằng quyên góp của cộng đồng, không phải một công ty lớn.
- **Mức độ sử dụng:** tốc độ thôi chưa tạo ra nhu cầu; ứng dụng trên Toccata và thanh toán thực tế vẫn phải phát triển.
- **Tiếp cận thị trường:** phần lớn giao dịch diễn ra trên các sàn cỡ vừa, và quy định về tiền mã hóa có thể thay đổi tùy quốc gia.

## Ý nghĩa nếu bạn mua định kỳ

Kaspa là đồng coin non trẻ với những đợt tăng giảm rất gắt. Mua định kỳ một khoản cố định giúp chia giá vào qua cả tháng tốt lẫn tháng xấu, nhưng không bảo vệ bạn khỏi một đợt giảm kéo dài. Phần lớn KAS đã được đào, nên biến động giá sau này chủ yếu phụ thuộc vào nhu cầu. Nhiều người chỉ giữ những coin như vậy như một phần nhỏ trong danh mục tiền mã hóa. Kết quả trong quá khứ không đảm bảo kết quả tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Kaspa — official website (kaspa.org)](https://kaspa.org/)
- [PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus — Sompolinsky, Wyborski, Zohar (IACR ePrint 2018/104)](https://eprint.iacr.org/2018/104.pdf)
- [Kaspa Covenants++ «Toccata» hard-fork outlook — Michael Sutton, Kaspa core developer (Medium)](https://medium.com/@michaelsuttonil/kaspa-covenants-toccata-hard-fork-outlook-a4d81a40900c)
- [Kaspa price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/kaspa)
