---
title: The Graph (GRT) giải thích dễ hiểu: giao thức lập chỉ mục dữ liệu blockchain, hoạt động từ 2020, trên Ethereum và Arbitrum
description: The Graph bằng ngôn ngữ đơn giản: indexer biến dữ liệu blockchain thành truy vấn nhanh ra sao, GRT để làm gì, staking và ủy quyền, lịch sử, đối thủ và rủi ro.
date: 2026-11-25
kind: analysis
---
**The Graph** thường được gọi là "Google của blockchain": giao thức này sắp xếp dữ liệu thô trên blockchain để ứng dụng tìm được thứ mình cần chỉ trong vài mili giây. Ví, sàn giao dịch và ứng dụng DeFi dùng nó để hiển thị số dư, giao dịch và giá mà không phải tự vận hành máy chủ dữ liệu. Token **GRT** dùng để trả cho công việc đó và bảo mật mạng lưới, và hôm nay có giá trị {{mcap:grt}} ({{rank:grt}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Mạng lưới đi vào hoạt động tháng 12/2020 với 10 tỷ GRT; token mới được phát hành mỗi năm làm phần thưởng, nên không có giới hạn nguồn cung cố định.
> - Đỉnh kỷ lục của GRT là {{ath:grt}} ({{athd:grt}}); giá hôm nay cách đỉnh {{fromath:grt}}.
> - GRT là token công việc: indexer phải stake GRT để cung cấp dữ liệu, và ứng dụng trả phí truy vấn bằng GRT.
> - Đây là khoản đặt cược vào nhu cầu dữ liệu blockchain, không phải một loại tiền — mức sử dụng và giá thường đi theo hai hướng khác nhau.

## Cách hoạt động

Đọc dữ liệu trực tiếp từ blockchain vừa chậm vừa cồng kềnh. Lập trình viên trên The Graph mô tả dữ liệu họ cần trong một "subgraph" mở, chẳng hạn mọi giao dịch trên một sàn phi tập trung. **Indexer** — các nhà vận hành độc lập chạy máy chủ — xử lý các subgraph đó và trả lời truy vấn từ ứng dụng, nhận phí cùng GRT mới phát hành. **Curator** đánh dấu subgraph nào đáng được lập chỉ mục, còn **delegator** ủy quyền GRT của mình cho indexer họ tin tưởng để nhận một phần phần thưởng. Indexer cung cấp dữ liệu sai có thể bị mất một phần số token đã stake ("slashing"). Hiện The Graph hỗ trợ hàng chục blockchain, và từ năm 2024 phần thưởng cùng các khoản thanh toán chạy trên Arbitrum, một layer 2 của Ethereum, để giữ chi phí thấp. Năm 2025, dự án bắt đầu triển khai **Horizon**, bản nâng cấp cho phép cùng một hệ thống staking bảo mật các loại dịch vụ dữ liệu mới.

## Token dùng để làm gì

GRT có ba vai trò. Indexer phải stake GRT trước khi làm việc, khiến một phần lớn nguồn cung bị khóa lại. Ứng dụng trả phí truy vấn bằng GRT (thường được tự động chuyển đổi từ stablecoin hoặc thanh toán bằng thẻ). Người nắm giữ cũng có thể ủy quyền GRT để nhận một phần phần thưởng mà không cần chạy máy chủ. Một phần nhỏ phí truy vấn và thuế staking bị đốt, trong khi lượng phát hành mới khoảng 3% mỗi năm được chia cho indexer và delegator. GRT có tăng giá trị hay không phụ thuộc vào việc nhu cầu trả tiền cho dữ liệu có tăng nhanh hơn nguồn cung mới hay không.

## Các con số hiện tại

- Giá hôm nay: {{price:grt}}
- Đỉnh kỷ lục: {{ath:grt}} ({{athd:grt}}), cách đỉnh {{fromath:grt}}
- Vốn hóa thị trường: {{mcap:grt}} ({{rank:grt}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:grt}}
- 10 USD mỗi ngày trong 5 năm: {{dca:grt:5}} từ {{dcainv:5}} đã đầu tư ({{dcaroi:grt:5}})

## Câu chuyện của The Graph

The Graph được Yaniv Tal, Brandon Ramirez và Jannis Pohlmann khởi xướng năm 2018; công ty của họ sau này trở thành Edge & Node. Trong nhiều năm, dự án vận hành một "hosted service" miễn phí mà rất nhiều ứng dụng Ethereum dựa vào. Mạng lưới phi tập trung và token GRT ra mắt ngày 17/12/2020, và trong cơn sốt tiền mã hóa, GRT tăng lên khoảng 2,84 USD vào tháng 2/2021. Sau đó giá giảm hơn 90% trong suốt 2021 và 2022. Trong năm 2023 và 2024, dự án chuyển phần thưởng sang Arbitrum và đóng hosted service vào tháng 6/2024, buộc toàn bộ người dùng chuyển sang mạng lưới trả phí. Đợt tăng của các token AI đầu năm 2024 từng đẩy GRT lên một thời gian, nhưng sau đó giá lại rơi xuống mức thấp mới.

## Các lựa chọn thay thế

The Graph cạnh tranh với các công ty và giao thức lập chỉ mục như Goldsky, SubQuery và Covalent, cùng các API dữ liệu blockchain của Alchemy và QuickNode, vốn được nhiều lập trình viên đánh giá là đơn giản hơn. Một số ứng dụng lớn tự vận hành indexer riêng. Trong nhóm token gắn với dữ liệu blockchain, [Chainlink]({lang}/link/) và [Pyth Network]({lang}/pyth/) thường được so sánh với GRT, dù hai dự án này cung cấp dữ liệu giá cho hợp đồng thông minh chứ không phải tìm kiếm trên dữ liệu quá khứ.

## Rủi ro chính

- **Nguồn cung mới:** lượng phát hành hằng năm bổ sung GRT mới, và indexer thường bán phần thưởng để trang trải chi phí máy chủ.
- **Liên hệ yếu với mức sử dụng:** từ lâu phí truy vấn vẫn nhỏ so với phần thưởng, nên việc được dùng nhiều tự nó không đẩy giá lên.
- **Cạnh tranh:** các nhà cung cấp dữ liệu tập trung nhanh và rẻ, và ứng dụng có thể dễ dàng chuyển sang dùng họ.
- **Phụ thuộc vào một công ty:** Edge & Node và The Graph Foundation vẫn định hướng phần lớn việc phát triển.
- **Quy định:** luật lệ về token staking và phần thưởng của chúng khác nhau giữa các quốc gia và có thể thay đổi.

## Ý nghĩa nếu bạn mua định kỳ

Phần lớn thời gian tồn tại, GRT nằm xa dưới đỉnh năm 2021, nên người mua định kỳ liên tục nhận thêm token ở giá thấp hơn — điều này chỉ có lợi nếu giá phục hồi. Mua một khoản cố định đều đặn giúp dàn trải rủi ro chọn sai thời điểm, nhưng không loại bỏ rủi ro thua lỗ. Nhiều người chỉ giữ loại token này như một phần nhỏ trong khoản tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Giới thiệu về The Graph (tài liệu The Graph)](https://thegraph.com/docs/en/about/)
- [Hướng dẫn triển khai Horizon: những gì thay đổi với người tham gia mạng lưới (blog The Graph)](https://thegraph.com/blog/horizon-implementation-guide/)
- [Giá, vốn hóa và đỉnh kỷ lục của The Graph (CoinGecko)](https://www.coingecko.com/en/coins/the-graph)
