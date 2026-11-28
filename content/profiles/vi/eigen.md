---
title: EigenCloud (EIGEN) giải thích dễ hiểu: restaking trên Ethereum, đợt stakedrop 2024 và canh bạc 70 triệu USD của a16z
description: EigenCloud, tên cũ EigenLayer, dễ hiểu: restaking hoạt động ra sao, EIGEN dùng làm gì, slashing, thương vụ a16z, đối thủ, rủi ro và mua định kỳ.
date: 2026-11-28
kind: analysis
---
**EigenCloud**, tên gọi đến tháng 6/2025 là **EigenLayer**, là một dự án trên Ethereum cho phép "restaking": dùng lại số ether vốn đang bảo vệ Ethereum để làm việc lần thứ hai, bảo vệ thêm các dịch vụ khác và nhận thêm phần thưởng. Dự án do Eigen Labs xây dựng — công ty ở Seattle do CEO Sreeram Kannan, cựu giáo sư Đại học Washington, điều hành. EIGEN là token của dự án, vốn hóa hiện tại là {{mcap:eigen}} ({{rank:eigen}} trong các tiền mã hóa).

> **Điểm chính**
> - Restaking ra mắt trên Ethereum năm 2023, và đến tháng 6/2024 tổng tiền gửi đạt đỉnh hơn 20 tỷ USD.
> - Mức giá kỷ lục của EIGEN là {{ath:eigen}} ({{athd:eigen}}); giá hiện nay cách đỉnh {{fromath:eigen}}.
> - EIGEN được phát cho người dùng sớm qua đợt "stakedrop" năm 2024 và chỉ chuyển được từ ngày 30/9/2024.
> - Tháng 6/2025, a16z crypto mua thêm 70 triệu USD EIGEN khi dự án tái ra mắt với tên EigenCloud.

## Cách hoạt động

Người staking gửi ETH hoặc token liquid staking như stETH của Lido vào hợp đồng thông minh của EigenLayer rồi ủy quyền cho các nhà vận hành — những công ty chạy phần mềm cho dịch vụ bên ngoài. Các "dịch vụ được xác thực chủ động" (AVS) này, như lưu trữ dữ liệu cho rollup (EigenDA), oracle giá và cầu nối, trả tiền cho nhà vận hành và người staking để đổi lấy sự an toàn. Nếu nhà vận hành vi phạm luật của dịch vụ, một phần tiền restaking có thể bị tịch thu ("slashing"); slashing được kích hoạt trên mạng chính vào tháng 4/2025, và mức phạt của từng dịch vụ được tách riêng. Tháng 6/2025, dự án đổi tên thành EigenCloud — nền tảng cho các ứng dụng "có thể kiểm chứng", kết hợp EigenDA với EigenCompute để chạy mã và EigenVerify để giải quyết tranh chấp.

## Token dùng để làm gì

Người restaking khóa ETH chứ không khóa EIGEN, nên EIGEN có vai trò khác. Nó được stake để bảo vệ dịch vụ trước những lỗi mà riêng mã nguồn không chứng minh được, chẳng hạn oracle báo giá sai: khi đó người giữ EIGEN có thể tách (fork) token để kẻ gian chịu thiệt — đây là nền tảng của EigenVerify. EIGEN cũng được trả làm phần thưởng cho người staking và nhà vận hành. Nguồn cung ban đầu khoảng 1,67 tỷ và tiếp tục tăng nhờ phát hành khuyến khích hằng năm, còn token của đội ngũ và nhà đầu tư được mở khóa dần trong nhiều năm.

## Các con số hiện tại

- Giá hôm nay: {{price:eigen}}
- Đỉnh kỷ lục: {{ath:eigen}} ({{athd:eigen}}), cách đỉnh {{fromath:eigen}}
- Vốn hóa thị trường: {{mcap:eigen}} ({{rank:eigen}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:eigen}}
- 10 USD mỗi ngày trong 2 năm: {{dca:eigen:2}} từ {{dcainv:2}} đã đầu tư ({{dcaroi:eigen:2}})

## Câu chuyện của Fluid

Eigen Labs huy động 50 triệu USD trong vòng gọi vốn series A do Blockchain Capital dẫn dắt vào tháng 3/2023, và cùng năm đó restaking mở trên mạng chính Ethereum. Săn điểm thưởng và chờ airdrop, người dùng ồ ạt đổ tiền vào, và tháng 2/2024 a16z crypto dẫn dắt vòng series B trị giá 100 triệu USD. Năm 2024, đội ngũ công bố đợt stakedrop EIGEN: ban đầu token không chuyển được, và người dùng ở một số nước, trong đó có Mỹ, bị loại ra, khiến dự án bị chỉ trích. EIGEN chuyển được từ ngày 30/9/2024 và lập kỷ lục vào tháng 12 năm đó. Tiền gửi giảm từ đỉnh giữa năm 2024 xuống khoảng 12 tỷ USD vào tháng 6/2025, khi a16z mua thêm 70 triệu USD EIGEN và dự án trở thành EigenCloud. Tháng 7/2025, Eigen Labs cắt giảm khoảng 25% nhân sự để tập trung vào EigenCloud.

## Các lựa chọn thay thế

Lựa chọn đơn giản nhất là staking thông thường ngay trên [Ethereum]({lang}/eth/) hoặc liquid staking qua [Lido DAO]({lang}/ldo/). [ether.fi]({lang}/ethfi/) cung cấp liquid restaking xây dựng trên EigenLayer. Các giao thức restaking cạnh tranh gồm Symbiotic và Karak, chấp nhận nhiều loại tài sản hơn.

## Rủi ro chính

- **Biến động mạnh:** EIGEN thấp hơn nhiều so với kỷ lục tháng 12/2024, và token non trẻ có thể còn giảm tiếp.
- **Rủi ro chồng lớp:** ETH được restaking chịu rủi ro staking của chính Ethereum, cộng thêm lỗi hợp đồng thông minh và slashing từ các dịch vụ bổ sung.
- **Nhu cầu thật:** phần thưởng phụ thuộc vào việc các dịch vụ trả tiền cho sự an toàn; nếu trả ít, restaking mất sức hút.
- **Nguồn cung:** phát hành khuyến khích hằng năm và các đợt mở khóa của đội ngũ, nhà đầu tư sớm đưa thêm token ra thị trường.
- **Cạnh tranh và quy định:** các giao thức đối thủ tranh giành cùng một nguồn tiền gửi, và luật về staking, token khác nhau giữa các nước.

## Ý nghĩa nếu bạn mua định kỳ

EIGEN chủ yếu giảm kể từ khi bắt đầu giao dịch vào mùa thu năm 2024, nên người mua định kỳ đến nay phần lớn mua khi giá đang đi xuống. Mua một số tiền cố định theo lịch giúp chia nhỏ rủi ro chọn sai thời điểm, nhưng không biến một token đang giảm thành có lãi; kết quả phụ thuộc vào việc các dịch vụ của EigenCloud có tìm được khách hàng trả tiền hay không. Nhiều người chỉ giữ loại token này ở một phần nhỏ khoản tiết kiệm mà họ chấp nhận thấy giảm mạnh. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [a16z crypto invests $70 million in direct EigenLayer token deal to back EigenCloud (The Block, 17 June 2025)](https://www.theblock.co/news/deals/2025-06-17-a16z-crypto-eigen-token-eigencloud-358511)
- [EigenLayer gets $70M from a16z to launch off-chain verifiability platform (Decrypt, 17 June 2025)](https://decrypt.co/325503/eigenlayer-70m-a16z-verifiability-platform)
- [Eigen Labs lays off 25% of workforce to focus on EigenCloud (The Block, 9 July 2025)](https://www.theblock.co/news/business/2025-07-09-eigen-layoffs-361731)
- [EigenCloud (EIGEN) — CoinGecko](https://www.coingecko.com/en/coins/eigenlayer)
