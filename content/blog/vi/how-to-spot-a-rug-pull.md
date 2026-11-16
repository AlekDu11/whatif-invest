---
title: Cách nhận biết rug pull: 10 điểm cần kiểm tra trước khi mua token mới
description: Cách nhận biết rug pull trước khi mua: 10 điểm kiểm tra về khóa thanh khoản, quyền mint và freeze, holder lớn, honeypot, mạng xã hội giả và khối lượng ảo.
date: 2026-11-16
category: guides
assets: sol, pepe, bonk
---
**Làm sao nhận biết rug pull?** Rug pull (kéo thảm) là khi những người đứng sau một token ôm tiền bỏ đi, để lại người mua với thứ không ai muốn. Nó có thể diễn ra đột ngột (người tạo rút thanh khoản khỏi pool) hoặc từ từ (người trong cuộc bán dần số token khổng lồ của họ). Dù theo cách nào, giá cũng về gần bằng không.

Rug pull không hiếm. Trong báo cáo năm 2025, công ty phân tích blockchain Solidus Labs xếp **98,6%** trong hơn 7 triệu token ra mắt trên nền tảng Pump.fun vào nhóm rug pull hoặc pump-and-dump, và chỉ khoảng 97.000 token giữ được thanh khoản tối thiểu 1.000 USD. Hãy dùng danh sách dưới đây trước khi mua bất kỳ token mới nào.

## Hai ví dụ gần đây

- **HAWK (tháng 12/2024).** Một memecoin do một người nổi tiếng trên mạng quảng bá đã đạt vốn hóa khoảng 490 triệu USD ngay sau khi ra mắt, rồi giảm khoảng 91% trong chưa đầy ba giờ. Các nhà phân tích on-chain cho biết một cụm ví người trong cuộc và ví "sniper" nắm 80–90% nguồn cung lúc ra mắt; một ví mua 17,5% nguồn cung chỉ vài giây sau khi ra mắt và bán ra trong 1,5 giờ tiếp theo. Người quảng bá phủ nhận việc cô hoặc đội ngũ của mình đã bán.
- **LIBRA (tháng 2/2025).** Một token được Tổng thống Argentina Javier Milei quảng bá trên mạng xã hội đã tăng vọt rồi sụp đổ chỉ trong vài giờ. Theo dữ liệu on-chain do The Block đưa tin, người trong cuộc đã rút về khoảng 107 triệu USD, và Milei rút lại lời ủng hộ.

Cả hai đều có tên tuổi nổi tiếng, khối lượng giao dịch khổng lồ và mạng xã hội sôi sục. Không điều nào trong số đó bảo vệ được người mua.

## Danh sách kiểm tra 10 điểm

### 1. Thanh khoản đã được khóa hay đốt chưa?

Một token được giao dịch với một pool thanh khoản (ví dụ token + SOL). Nếu người tạo nắm LP token của pool, họ có thể rút pool bất cứ lúc nào. Hãy tìm thanh khoản đã được **đốt** (burn) hoặc **khóa** (lock) dài hạn qua một dịch vụ khóa có tiếng, và kiểm tra ngày hết hạn khóa. Câu "Tin tôi đi, đã khóa rồi" trong nhóm chat không phải bằng chứng.

### 2. Quyền mint đã bị thu hồi chưa?

Trên Solana, mint authority (quyền đúc) cho phép ai đó tạo thêm token. Nếu quyền này vẫn còn, người tạo có thể in hàng tỷ token mới và bán vào pool. Trang token trên các công cụ như GMGN, Solscan hay RugCheck cho biết quyền này đã bị thu hồi hay chưa.

### 3. Quyền freeze đã bị thu hồi chưa?

Freeze authority (quyền đóng băng) cho phép ai đó đóng băng tài khoản token. Người tạo giữ quyền này có thể chặn bạn bán trong khi chính họ bán. Với một memecoin, không có lý do chính đáng nào để giữ quyền này.

### 4. Các holder lớn nhất tập trung đến mức nào?

Mở danh sách holder. Bỏ qua pool và các ví sàn đã biết, rồi cộng tỷ lệ của top 10. Nếu một nhóm nhỏ ví nắm phần lớn nguồn cung, họ là người quyết định giá. Hãy cảnh giác với nhiều ví trông "khác nhau" nhưng được nạp tiền từ cùng một nguồn; các công cụ bubble map (bản đồ bong bóng) sẽ hiển thị những cụm ví như vậy.

### 5. Bạn có thật sự bán được không? (kiểm tra honeypot)

Honeypot cho bạn mua nhưng không cho bán, hoặc thu một khoản thuế bán ẩn rất lớn. Dấu hiệu cảnh báo: lịch sử giao dịch gần như không có lệnh bán, lệnh bán thất bại, hoặc hợp đồng có quy tắc chuyển token bất thường (phổ biến hơn trên Ethereum và BNB Chain). Các công cụ mô phỏng có thể thử lệnh bán trước khi bạn mua.

### 6. Các kênh mạng xã hội có thật không?

Kiểm tra website và tài khoản X/Telegram. Dấu hiệu đáng ngờ: tài khoản mới lập tuần trước, hàng nghìn người theo dõi nhưng không có thảo luận thật, nội dung website sao chép, "đội ngũ" dùng ảnh mạng, tắt bình luận, hoặc đường link khác với link trên trang token.

### 7. Khối lượng giao dịch có thật không?

Một làn sóng khối lượng đột ngột từ các ví mới, các lệnh có kích thước gần như y hệt nhau, hoặc cùng những ví mua bán qua lại với nhau (wash trading, giao dịch ảo) có thể được dùng để đẩy token lên danh sách "trending". Sự quan tâm thật thường đi kèm nhiều ví khác nhau và tăng trưởng từ từ.

### 8. Lúc ra mắt diễn ra thế nào?

Có vài ví mua một tỷ lệ lớn trong những giây đầu tiên không? Ví của nhà phát triển có bán ngay sau khi ra mắt không? Nhiều công cụ hiển thị lịch sử của ví "dev", kể cả các token nó từng phát hành trước đó; một người tạo để lại hàng loạt token đã chết là lời cảnh báo rõ ràng.

### 9. Ai đang quảng bá, và vì sao?

KOL được trả tiền, các vụ ra mắt của người nổi tiếng và thông điệp "chắc chắn x100" thường báo hiệu đỉnh. Hãy tự hỏi: nếu người này đang quảng bá, họ đã mua khi nào, ở giá bao nhiêu?

### 10. Biểu đồ giá có hợp lý không?

Một cây nến dựng đứng trên token mới vài giờ tuổi nghĩa là những người mua sớm đang lãi lớn, và nhiều người sẽ bán cho lớp người mua kế tiếp. Nỗi sợ bỏ lỡ (FOMO) chính là cảm giác mà một vụ rug pull được thiết kế để tạo ra.

## Quy trình nhanh trước mỗi lần mua

1. Sao chép địa chỉ hợp đồng từ nguồn đáng tin.
2. Kiểm tra trạng thái mint, freeze và thanh khoản.
3. Xem các holder lớn nhất và các cụm ví.
4. Rà lịch sử giao dịch xem có lệnh bán không.
5. Xác định số tiền tối đa bạn sẵn sàng mất, rồi chia đôi.

Nếu bất kỳ điểm nào không đạt, hãy bỏ qua. Lúc nào cũng sẽ có token khác.

## Ngay cả token "sạch" cũng có thể giảm 90%

Vượt qua danh sách này chỉ làm giảm rủi ro bị lừa đảo trắng trợn. Nó không biến một token thành khoản đầu tư tốt. Ngay cả những memecoin nổi tiếng nhất cũng đã giảm mạnh so với đỉnh; bạn có thể xem mức giảm hiện tại trên [trang memecoin]({lang}/memes/) và [công cụ theo dõi đỉnh lịch sử]({lang}/ath/) của chúng tôi. CoinGecko thống kê hơn một nửa số token được theo dõi từ năm 2021 đã "chết" vào cuối năm 2025.

## Câu hỏi thường gặp

### Rug pull có phạm pháp không?

Tùy quốc gia và chi tiết vụ việc. Nhiều vụ rug pull bị coi là lừa đảo, nhưng tiền on-chain hiếm khi được thu hồi, nên phòng tránh tốt hơn nhiều so với chờ công lý.

### Pool thanh khoản đã khóa có nghĩa là token an toàn không?

Không. Nó loại bỏ một cách kéo thảm, nhưng người trong cuộc vẫn có thể xả một phần lớn nguồn cung, và việc khóa có thể hết hạn.

### Có lấy lại được tiền sau khi bị rug pull không?

Thường là không. Hãy báo công an và nền tảng, đồng thời cảnh giác với các "dịch vụ lấy lại tiền" đòi trả phí; đó thường là vụ lừa đảo thứ hai.

### Công cụ nào giúp kiểm tra token?

Trang token trên GMGN và các DEX screener, trình khám phá khối như Solscan, và công cụ kiểm tra như RugCheck hiển thị thanh khoản, các quyền và holder. Hãy dùng nhiều hơn một công cụ.

## Nguồn

- [98% of tokens on Pump.fun have been rug pulls or an act of fraud, new report says (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Hawk Tuah memecoin dumps 90% (Cointelegraph)](https://cointelegraph.com/news/hawk-tuah-memecoin-dumps-90-percent-outrage-token-launch-insider)
- [Milei retracts LIBRA endorsement after insiders cash out $107 million (The Block)](https://www.theblock.co/post/341206/argentinian-president-javier-milei-retracts-libra-endorsement-after-insiders-cash-out-107-million)
- [Dead coins: over 50% of cryptocurrencies have failed, CoinGecko report (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*Không phải lời khuyên đầu tư. Danh sách kiểm tra này giúp giảm rủi ro nhưng không thể loại bỏ hoàn toàn; hầu hết token mới đều mất gần như toàn bộ giá trị.*
