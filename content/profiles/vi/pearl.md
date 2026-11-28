---
title: Pearl (PEARL) giải thích dễ hiểu: đào bằng GPU với Proof of Useful Work, tối đa 2,1 tỷ
description: Pearl dễ hiểu: việc đào bằng GPU gắn với tính toán AI ra sao, nguồn cung 2,1 tỷ, ra mắt tháng 4/2026, những chỉ trích, đối thủ và rủi ro chính.
date: 2026-11-28
kind: analysis
---
**Pearl** là một blockchain lớp 1 mới được đào bằng card đồ họa Nvidia. Thay vì những câu đố hash vô ích mà thợ đào Bitcoin giải, "bằng chứng công việc hữu ích" (Proof of Useful Work) của Pearl yêu cầu thợ đào nhân ma trận — chính phép toán chạy các mô hình AI — nên về lý thuyết một GPU có thể vừa phục vụ khách hàng AI vừa bảo vệ mạng. Dự án do Pearl Research Labs xây dựng, đồng sáng lập bởi nhà khoa học máy tính Omri Weinstein, và mạng chính ra mắt ngày 27/4/2026. Vốn hóa hiện tại là {{mcap:pearl}} ({{rank:pearl}} trong các tiền mã hóa).

> **Điểm chính**
> - Sẽ không bao giờ có quá 2,1 tỷ đồng, gấp 100 lần 21 triệu của Bitcoin; phần thưởng đào giảm dần đều thay vì giảm một nửa theo chu kỳ.
> - Mức giá kỷ lục là {{ath:pearl}} ({{athd:pearl}}); giá hiện nay cách đỉnh {{fromath:pearl}}.
> - Dự án cho biết không có đào trước, không có phần cho nhà đầu tư và không có quỹ của đội ngũ: mọi đồng đều đến từ việc đào.
> - Một nghiên cứu tháng 6/2026 cho thấy việc đào lúc đó hoàn toàn không tạo ra công việc AI hữu ích nào.

## Cách hoạt động

Thợ đào chạy các phép nhân ma trận "có nhiễu" trên GPU, băm những mảnh nhỏ của kết quả và gói công việc vào một bằng chứng không tiết lộ (zero-knowledge proof), để ai cũng có thể kiểm tra nhanh mà không phải làm lại. Phương pháp này lấy từ một bài báo mật mã học năm 2025 mà Weinstein là đồng tác giả. Phần mềm đào chính thức gắn vào vLLM — phần mềm phổ biến để chạy mô hình AI — trên các card trung tâm dữ liệu như Nvidia H100 và H200, còn phần mềm do cộng đồng viết chạy được cả trên card RTX chơi game. Bên trong, Pearl khá giống Bitcoin: nó dựa trên btcd, một chương trình nút Bitcoin, và vài phút lại có một khối mới. Đồng coin thường được niêm yết với mã PRL, và trên một số trang giá có một token khác không liên quan dùng cùng mã này.

## Token dùng để làm gì

Coin chỉ được tạo ra làm phần thưởng cho thợ đào và dùng để trả phí giao dịch. Ví dụ thương mại đầu tiên xuất hiện vào tháng 5/2026: công ty điện toán đám mây AI Together AI cung cấp một mô hình Gemma chạy trên các máy đào Pearl với giá thấp hơn mức thường hơn 25%, phần giảm giá được bù bằng phần thưởng PRL. Nếu khách hàng AI thật sự dùng mạng theo cách này, việc đào không còn chỉ là tiêu tốn điện; nếu không, Pearl chỉ là thêm một đồng proof-of-work với nguồn cung lớn.

## Các con số hiện tại

- Giá hôm nay: {{price:pearl}}
- Đỉnh kỷ lục: {{ath:pearl}} ({{athd:pearl}}), cách đỉnh {{fromath:pearl}}
- Vốn hóa thị trường: {{mcap:pearl}} ({{rank:pearl}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:pearl}}

## Câu chuyện của Fluid

Bài báo nền tảng được công bố tháng 4/2025, và mạng chính chạy từ ngày 27/4/2026 mà không chia trước đồng nào. Cuối tháng 5, sau thỏa thuận với Together AI, game thủ và chủ GPU đổ xô đi đào, và chỉ trong vài tuần thu nhập mỗi ngày của một card RTX 5090 giảm khoảng một nửa vì cạnh tranh tăng. Ban đầu đồng coin chỉ được giao dịch trên các sàn nhỏ, thanh khoản mỏng như MEXC. Tháng 6/2026, một bài báo trên arXiv mang tên "The Usefulness Gap in Proof-of-Useful-Work" cho biết hàng nghìn thợ đào trong mạng không tạo ra phép tính AI hữu ích nào và phần mềm đào phổ biến nhất thậm chí không chứa mã AI. Pearl bổ sung hỗ trợ mô hình AI dạng mixture-of-experts trong một đợt hard fork tháng 6, và đến tháng 10/2026 khoảng 16% nguồn cung tối đa đã được đào.

## Các lựa chọn thay thế

[Bitcoin]({lang}/btc/) là đồng proof-of-work cổ điển, được đào bằng chip chuyên dụng chứ không phải GPU. Trong các dự án AI và điện toán, [Bittensor]({lang}/tao/) thưởng cho người chạy mô hình AI, còn [Render]({lang}/render/), [Akash Network]({lang}/akt/) và [io.net]({lang}/io/) cho thuê sức mạnh GPU trực tiếp. Ý tưởng của Pearl thì khác: chính việc đào phải là công việc AI hữu ích.

## Rủi ro chính

- **Rất mới:** đồng coin mới có vài tháng lịch sử giá, và các đồng non trẻ có thể nhanh chóng mất phần lớn giá trị.
- **Lợi ích chưa được chứng minh:** các nhà nghiên cứu độc lập đến nay chỉ thấy rất ít công việc AI thật; luận điểm chính của dự án có thể không đứng vững.
- **Kinh tế của việc đào:** độ khó tăng và phần thưởng giảm làm thu nhập thợ đào giảm, mà thợ đào thường bán coin để trả tiền điện.
- **Tập trung:** những tuần đầu đào rất rẻ, nên người tham gia sớm nắm một phần lớn.
- **Thanh khoản và mã trùng:** giao dịch mỏng hơn các đồng lớn và có một token khác dùng cùng mã PRL — hãy kiểm tra kỹ hợp đồng và sàn.

## Ý nghĩa nếu bạn mua định kỳ

Pearl mới được giao dịch vài tháng, nên chưa có lịch sử đáng kể nào cho việc mua định kỳ. Mua một số tiền cố định theo lịch giúp chia nhỏ rủi ro chọn sai thời điểm, nhưng với một đồng hoàn toàn mới thì không loại bỏ được rủi ro mất phần lớn số tiền. Nhiều người chỉ giữ những đồng thử nghiệm như vậy ở một phần rất nhỏ khoản tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
