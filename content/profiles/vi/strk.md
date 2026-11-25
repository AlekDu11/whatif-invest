---
title: Starknet (STRK) giải thích dễ hiểu: layer 2 của Ethereum do StarkWare xây dựng, chạy từ 2021, nay cho stake bitcoin
description: Starknet bằng ngôn ngữ đơn giản: layer 2 ZK-STARK này giúp Ethereum rẻ hơn ra sao, STRK dùng để làm gì, stake bitcoin, lịch sử, đối thủ và rủi ro chính.
date: 2026-11-25
kind: analysis
---
**Starknet** là một mạng "layer 2" chạy trên [Ethereum]({lang}/eth/): mạng này gom hàng nghìn giao dịch lại với nhau, dùng mật mã học để chứng minh tất cả đều đúng rồi gửi bằng chứng đó lên Ethereum, nhờ vậy dùng ứng dụng trên Starknet chỉ tốn một phần nhỏ chi phí so với trên chính Ethereum. Mạng do công ty Israel StarkWare xây dựng và đi vào hoạt động từ tháng 11/2021. Token STRK của mạng có tổng giá trị {{mcap:strk}} ({{rank:strk}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - 10 tỷ STRK được tạo ra khi token ra mắt vào tháng 2/2024; phần thưởng staking còn sinh thêm token mới ngoài số đó.
> - Từ tháng 9/2025, người nắm giữ wrapped bitcoin có thể stake trên Starknet, kèm chương trình khuyến khích trị giá 100 triệu STRK.
> - Đỉnh kỷ lục là {{ath:strk}} ({{athd:strk}}); giá hiện tại cách đỉnh {{fromath:strk}}.
> - Starknet dùng ngôn ngữ lập trình riêng là Cairo thay vì Solidity của Ethereum.

## Cách hoạt động

Starknet là một "ZK rollup". Giao dịch được thực hiện trên Starknet, sau đó một prover tạo ra STARK — một bằng chứng toán học ngắn gọn cho thấy mọi bước đều được tính đúng. Ethereum chỉ cần kiểm tra bằng chứng đó chứ không phải làm lại toàn bộ công việc, nên rất nhiều giao dịch dùng chung một lần kiểm tra rẻ mà vẫn dựa vào độ an toàn của Ethereum. Đồng sáng lập StarkWare Eli Ben-Sasson là một trong những nhà khoa học đã phát minh ra bằng chứng STARK; dự án cho biết loại bằng chứng này còn chống được máy tính lượng tử trong tương lai. Lập trình viên viết ứng dụng Starknet bằng Cairo, ngôn ngữ được thiết kế để chương trình dễ được chứng minh.

## STRK dùng để làm gì

STRK dùng để trả phí giao dịch trên Starknet, bỏ phiếu cho các bản nâng cấp mạng và để stake: người nắm giữ khóa token cùng validator để giúp bảo vệ mạng và nhận STRK mới làm phần thưởng. Staking bắt đầu từ tháng 11/2024. Tháng 8/2025, một cuộc bỏ phiếu on-chain (SNIP-31, khoảng 93,6% tán thành) cho phép stake wrapped bitcoin — WBTC, tBTC, LBTC và SolvBTC — cùng với STRK, và tính năng stake bitcoin chính thức chạy ngày 30/9/2025. Tháng 2/2026, Starknet công bố strkBTC, một token được bảo chứng bằng bitcoin với số dư riêng tư và chuyển tiền bảo mật.

## Các con số hiện tại

- Giá hôm nay: {{price:strk}}
- Đỉnh kỷ lục: {{ath:strk}} ({{athd:strk}}), cách đỉnh {{fromath:strk}}
- Vốn hóa thị trường: {{mcap:strk}} ({{rank:strk}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:strk}}
- 10 USD mỗi ngày trong 1 năm: {{dca:strk:1}} từ {{dcainv:1}} đã đầu tư ({{dcaroi:strk:1}})

## Câu chuyện của Starknet

StarkWare được thành lập năm 2018 và ban đầu bán công nghệ của mình dưới tên StarkEx, một bộ máy được các sàn như dYdX và Immutable sử dụng. Mạng đa năng Starknet mở cửa vào tháng 11/2021. Token STRK ra mắt ngày 20/2/2024 với đợt airdrop lớn cho người dùng và lập trình viên; giá cao nhất trong những ngày đầu rồi giảm gần như suốt hai năm sau đó, khi lượng lớn token của nhà đầu tư sớm và đội ngũ dần được mở khóa. Trong giai đoạn 2025–2026, dự án định vị lại Starknet thành nơi để sử dụng bitcoin, không chỉ Ethereum.

## Các lựa chọn thay thế

Starknet cạnh tranh với các mạng layer 2 khác của Ethereum: [Arbitrum]({lang}/arb/) và [Optimism]({lang}/op/) (optimistic rollup), Base của Coinbase, cùng các ZK rollup khác như [ZKsync]({lang}/zk/), Scroll và Linea. Điểm khác biệt của Starknet là bằng chứng STARK và ngôn ngữ Cairo; mặt trái là lập trình viên Ethereum phải học một ngôn ngữ mới.

## Rủi ro chính

- **Cạnh tranh:** rất nhiều mạng layer 2 tranh giành cùng một nhóm người dùng và ứng dụng, và những mạng được dùng nhiều nhất chiếm phần lớn hoạt động.
- **Nguồn cung token:** staking sinh thêm STRK mới, còn token của nhà đầu tư sớm và những người đóng góp được mở khóa trong nhiều năm.
- **Công nghệ:** mật mã phức tạp, cầu nối (bridge) và đơn vị phát hành wrapped bitcoin có thể gặp sự cố hoặc bị hack; một phần mạng vẫn do một nhóm nhỏ nhà vận hành điều khiển.
- **Thu giữ giá trị:** phí rẻ tốt cho người dùng nhưng để lại ít doanh thu hơn để hỗ trợ giá token.
- **Biến động mạnh:** như phần lớn các token còn non trẻ, STRK từng mất phần lớn giá trị so với đỉnh.

## Ý nghĩa nếu bạn mua định kỳ

STRK là token non trẻ, biến động mạnh và có lịch sử giá còn ngắn, nên đến nay một kế hoạch mua định kỳ với token này chủ yếu gặp giá giảm. Mua một số tiền cố định đều đặn giúp dàn trải rủi ro vào lệnh ở thời điểm xấu, nhưng không bảo vệ bạn trước một đợt giảm kéo dài. Nhiều người chỉ giữ những token như thế này ở một phần nhỏ trong danh mục tiền mã hóa. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Starknet ra mắt stake bitcoin và sản phẩm lợi suất trong đợt mở rộng BTCFi (The Block)](https://www.theblock.co/post/372720/starknet-bitcoin-staking-100m-strk-incentives-re7-btc-yield)
- [Starknet giới thiệu strkBTC, đưa "bitcoin riêng tư" lên mạng layer 2 của mình (The Block)](https://www.theblock.co/post/391420/starknet-introduces-strkBTC-to-bring-private-bitcoin-and-confidential-defi-transactions-to-its-layer-2-network)
- [Starknet triển khai stake bitcoin trên mạng L2 (ForkLog)](https://forklog.com/en/starknet-introduces-bitcoin-staking-on-l2-network/)
- [Starknet muốn biến bitcoin thành tài sản sinh lời (Blockworks)](https://www.blockworks.co/news/starknet-making-btc-productive)
- [Blog của Starknet (starknet.io)](https://www.starknet.io/blog/all/)
