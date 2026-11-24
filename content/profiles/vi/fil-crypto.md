---
title: Filecoin (FIL) giải thích dễ hiểu: mạng lưu trữ xây trên IPFS, giới hạn 2 tỷ token, hoạt động từ 2020
description: Filecoin giải thích dễ hiểu: thị trường lưu trữ vận hành ra sao, FIL dùng để làm gì, Onchain Cloud, câu chuyện, đối thủ, rủi ro chính và lời khuyên cho người mua định kỳ.
date: 2026-11-24
kind: analysis
---
**Filecoin** là một blockchain nơi ai cũng có thể cho thuê dung lượng ổ cứng còn trống và ai cũng có thể trả tiền để lưu tệp lên đó — giống như một dịch vụ lưu trữ đám mây mở và phi tập trung. Mạng được tạo bởi Protocol Labs, đội ngũ đứng sau giao thức chia sẻ tệp IPFS, và đi vào hoạt động từ tháng 10/2020. Token FIL có tổng giá trị {{mcap:fil-crypto}} ({{rank:fil-crypto}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Nhà cung cấp lưu trữ nhận FIL khi giữ dữ liệu và phải liên tục chứng minh rằng họ vẫn đang giữ nó.
> - Sẽ không bao giờ có quá 2 tỷ FIL; phần lớn được phát hành dần làm phần thưởng cho nhà cung cấp.
> - Năm 2026 mạng chuyển trọng tâm từ tăng dung lượng sang thu hút khách hàng trả tiền; Filecoin Onchain Cloud chạy từ tháng 3/2026.
> - Đỉnh kỷ lục là {{ath:fil-crypto}} ({{athd:fil-crypto}}); hiện giá cách đỉnh {{fromath:fil-crypto}}.

## Cách hoạt động

Nhà cung cấp lưu trữ — từ nhà vận hành nhỏ đến trung tâm dữ liệu lớn — chào bán dung lượng ổ đĩa. Khách hàng muốn lưu dữ liệu sẽ ký một "thỏa thuận" với một hoặc vài nhà cung cấp. Sau đó nhà cung cấp công bố bằng chứng mật mã: Proof-of-Replication cho thấy họ đã tạo một bản sao riêng, còn Proof-of-Spacetime cho thấy họ tiếp tục giữ bản sao đó theo thời gian. Nếu không đưa ra được bằng chứng, nhà cung cấp bị cắt một phần FIL đã khóa làm tài sản thế chấp ("slashing"). Từ tháng 3/2023, Filecoin Virtual Machine cho phép viết hợp đồng thông minh để tự động hóa thỏa thuận lưu trữ và thanh toán.

## Token dùng để làm gì

FIL dùng để trả phí lưu trữ và giao dịch trên mạng. Nhà cung cấp phải khóa FIL làm tài sản thế chấp trước khi chào bán dung lượng, và họ nhận FIL mới phát hành làm phần thưởng khối cùng phí từ khách hàng. Một phần phí bị đốt. Trên thực tế, nhu cầu với token phụ thuộc vào số khách hàng thật trả tiền lưu trữ — vì vậy chiến lược 2026 đặt các thỏa thuận có trả phí lên hàng đầu.

## Các con số hiện tại

- Giá hôm nay: {{price:fil-crypto}}
- Đỉnh kỷ lục: {{ath:fil-crypto}} ({{athd:fil-crypto}}), cách đỉnh {{fromath:fil-crypto}}
- Vốn hóa thị trường: {{mcap:fil-crypto}} ({{rank:fil-crypto}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:fil-crypto}}
- 10 USD mỗi ngày trong 5 năm: {{dca:fil-crypto:5}} từ {{dcainv:5}} đã đầu tư ({{dcaroi:fil-crypto:5}})

## Câu chuyện của Filecoin

Protocol Labs, do Juan Benet sáng lập, công bố whitepaper Filecoin năm 2014 và huy động khoảng 200 triệu USD qua đợt bán token năm 2017 — một trong những đợt lớn nhất thời đó. Mạng chính ra mắt vào tháng 10/2020. Tháng 4/2021, ngay sau khi niêm yết trên các sàn lớn, FIL có lúc được giao dịch trên 200 USD; trong những năm sau đó nó mất hơn 95% giá trị ấy. Hợp đồng thông minh được bổ sung vào tháng 3/2023. Tháng 2/2026, Filecoin Foundation công bố chiến lược tập trung vào nhu cầu trả phí, và tháng 3/2026 Filecoin Onchain Cloud ra mắt trên mạng chính — dịch vụ lưu trữ có sẵn thanh toán, giá từ 2,50 USD mỗi TiB mỗi tháng cho mỗi bản sao.

## Các lựa chọn thay thế

Trong lưu trữ phi tập trung, đối thủ chính là [Arweave]({lang}/ar/) — trả một lần để lưu vĩnh viễn — cùng [Storj]({lang}/storj/) và [Siacoin]({lang}/sc/), vốn cho thuê dung lượng giống Filecoin. Nhưng đối thủ lớn nhất vẫn là các dịch vụ đám mây quen thuộc như Amazon S3 và Google Cloud: rẻ, nhanh và quen thuộc với doanh nghiệp.

## Rủi ro chính

- **Biến động mạnh:** FIL đã giảm hơn 95% từ đỉnh năm 2021; những cú giảm như vậy có thể lặp lại.
- **Phát hành liên tục:** mỗi ngày token mới được trả cho nhà cung cấp, và việc mở khóa cho nhà đầu tư sớm kéo dài nhiều năm, tạo áp lực bán.
- **Nhu cầu thật:** phần lớn dữ liệu được lưu từng được trợ giá; nếu khách hàng trả tiền không tăng, công dụng của token vẫn hạn chế.
- **Cạnh tranh:** lưu trữ đám mây của các ông lớn công nghệ dễ dùng hơn và ngày càng rẻ.
- **Quy định:** luật về token và đợt bán năm 2017 khác nhau giữa các nước và có thể thay đổi.

## Ý nghĩa nếu bạn mua định kỳ

Filecoin là cược rằng lưu trữ phi tập trung sẽ có được khách hàng thật, và giá của nó biến động rất mạnh. Mua một số tiền cố định đều đặn giúp dàn đều các lần mua qua lúc lên và lúc xuống mà không phải đoán đáy — nhưng không loại bỏ rủi ro thua lỗ. Nhiều người chỉ giữ các token nhỏ như FIL ở một phần nhỏ trong danh mục tiền mã hóa. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Filecoin — trang chính thức và tài liệu (filecoin.io)](https://filecoin.io/)
- [Filecoin Onchain Cloud is live on mainnet (blog Filecoin, tháng 3/2026)](https://filecoin.io/blog/filecoin-onchain-cloud-is-live-on-mainnet)
- [The 2026 Filecoin Network Strategy (blog Filecoin, tháng 2/2026)](https://filecoin.io/blog/the-2026-filecoin-network-strategy)
- [Giá, vốn hóa và đỉnh kỷ lục của Filecoin (CoinGecko)](https://www.coingecko.com/en/coins/filecoin)
