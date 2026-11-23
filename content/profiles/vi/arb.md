---
title: Arbitrum (ARB) giải thích dễ hiểu: layer 2 của Ethereum, optimistic rollup và tối đa 10 tỷ ARB
description: Arbitrum bằng ngôn ngữ đơn giản: layer 2 của Ethereum này hoạt động ra sao, ARB dùng để làm gì trong DAO, mở khóa token, lịch sử và rủi ro.
date: 2026-11-23
kind: analysis
---
**Arbitrum** là một mạng xây dựng trên Ethereum, giúp giao dịch nhanh hơn và rẻ hơn nhiều nhưng vẫn dựa vào Ethereum để bảo mật — thường gọi là "layer 2" (lớp 2). Mạng do công ty Mỹ Offchain Labs tạo ra, còn token **ARB** cho phép người nắm giữ bỏ phiếu về cách vận hành mạng và ngân quỹ của nó. Hôm nay ARB có giá trị {{mcap:arb}} ({{rank:arb}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Sẽ không bao giờ có quá 10 tỷ ARB; khi ra mắt vào tháng 3/2023, khoảng 42% thuộc ngân quỹ DAO, khoảng 27% cho đội ngũ và 17,5% cho nhà đầu tư.
> - Đỉnh kỷ lục là {{ath:arb}} ({{athd:arb}}); hôm nay giá cách đỉnh {{fromath:arb}}.
> - ARB là token quản trị: phí trên Arbitrum được trả bằng ETH, không phải ARB.
> - Token của đội ngũ và nhà đầu tư được mở khóa hằng tháng từ tháng 3/2024, bổ sung nguồn cung mới ra thị trường.

## Cách hoạt động

Arbitrum là một **optimistic rollup**. Thay vì để mọi nút Ethereum xử lý mọi giao dịch, Arbitrum thực hiện chúng trên chuỗi riêng rồi gửi các gói dữ liệu đã nén về Ethereum. Một bên vận hành duy nhất là **sequencer** (bộ sắp xếp, do Offchain Labs điều hành) xếp thứ tự giao dịch và xác nhận chúng trong chưa đầy một giây. Kết quả được coi là đúng ("lạc quan") trừ khi có người phản đối: bất kỳ validator nào cũng có thể gửi **bằng chứng gian lận** (fraud proof), và tranh chấp được phân xử trên Ethereum. Từ tháng 2/2025, giao thức **BoLD** cho phép bất kỳ ai tham gia xác thực, và chỉ cần một validator trung thực là đủ bảo vệ chuỗi. Phần mềm **Nitro** tương thích với ứng dụng Ethereum, còn chương trình **Orbit** cho phép các dự án khác ra mắt chuỗi riêng bằng công nghệ của Arbitrum.

## Token dùng để làm gì

ARB chủ yếu là token để bỏ phiếu. Người nắm giữ, hoặc người đại diện họ chọn, bỏ phiếu trong **Arbitrum DAO** về các nâng cấp của mạng và cách chi tiêu ngân quỹ DAO, nơi giữ hàng tỷ ARB cùng nguồn thu từ phí sequencer. Không cần ARB để dùng Arbitrum: phí gas được trả bằng ETH. Vì vậy giá trị của token phụ thuộc vào quyền biểu quyết và vào việc DAO quyết định làm gì với tiền của mình, chứ không trực tiếp vào mức độ sử dụng mạng.

## Các con số hiện tại

- Giá hôm nay: {{price:arb}}
- Đỉnh kỷ lục: {{ath:arb}} ({{athd:arb}}), cách đỉnh {{fromath:arb}}
- Vốn hóa thị trường: {{mcap:arb}} ({{rank:arb}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:arb}}
- 10 USD mỗi ngày trong 3 năm: {{dca:arb:3}} từ {{dcainv:3}} đã đầu tư ({{dcaroi:arb:3}})

## Câu chuyện của Arbitrum

Offchain Labs ra đời từ nghiên cứu tại Đại học Princeton. Arbitrum One mở cửa cho công chúng vào cuối tháng 8/2021, và bản nâng cấp Nitro tháng 8/2022 đã giảm phí và tăng công suất. Ngày 23/3/2023, token ARB ra mắt cùng đợt airdrop lớn cho người dùng. Vài ngày sau, đề xuất đầu tiên AIP-1 gây phản ứng dữ dội vì Quỹ đã bắt đầu dùng khoản phân bổ 750 triệu ARB trước khi bỏ phiếu; sau đó Quỹ tách đề xuất và trao cho DAO nhiều quyền kiểm soát hơn. ARB đạt đỉnh khoảng 2,39 USD vào tháng 1/2024. Ngày 16/3/2024, khoảng 1,1 tỷ token của đội ngũ và nhà đầu tư được mở khóa, tiếp theo là các đợt mở khóa hằng tháng. Năm 2025 BoLD đi vào hoạt động, còn giá giảm mạnh trong suốt 2025 và 2026.

## Các lựa chọn thay thế

Arbitrum cạnh tranh với các mạng layer 2 khác của Ethereum: [Optimism]({lang}/op/) và các chuỗi xây trên OP Stack của nó, trong đó có Base của Coinbase vốn không có token riêng; các rollup zero-knowledge như [ZKsync]({lang}/zk/) và [Starknet]({lang}/strk/); cùng [Mantle]({lang}/mnt/) và [POL (ex-MATIC)]({lang}/pol/). Bản thân [Ethereum]({lang}/eth/) cũng là một lựa chọn, vì các nâng cấp của nó khiến chi phí sử dụng ngày càng rẻ.

## Rủi ro chính

- **Nguồn cung mới:** các đợt mở khóa cho đội ngũ và nhà đầu tư vẫn tiếp tục, và ngân quỹ DAO nắm một phần lớn tổng số ARB.
- **Sequencer tập trung:** chỉ một bên sắp xếp giao dịch; nếu nó ngừng hoạt động hoặc hành xử sai, người dùng phải dựa vào các đường dự phòng chậm hơn.
- **Cạnh tranh:** Base và các mạng layer 2 khác tranh giành cùng người dùng, ứng dụng và phí.
- **Liên kết yếu với mức sử dụng:** phí trả bằng ETH, nên Arbitrum được dùng nhiều cũng không tự động làm tăng nhu cầu ARB.
- **Quy định:** luật lệ về token, DAO và các công ty đứng sau có thể khác nhau và thay đổi theo từng quốc gia.

## Ý nghĩa nếu bạn mua định kỳ

Phần lớn lịch sử của ARB là đi xuống từ đỉnh ban đầu, nên người mua định kỳ đã gom ngày càng nhiều token ở giá thấp hơn — điều này chỉ có ích nếu giá phục hồi. Mua một khoản cố định đều đặn giúp dàn trải rủi ro chọn sai thời điểm, nhưng không loại bỏ rủi ro thua lỗ. Nhiều người chỉ giữ loại token này như một phần nhỏ trong khoản tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [A gentle introduction to Arbitrum (tài liệu Arbitrum)](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO (Arbitrum Foundation)](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet (The Block, 12/2/2025)](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/arbitrum)
