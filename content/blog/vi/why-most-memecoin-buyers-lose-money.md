---
title: "Vì sao đa số người mua memecoin thua lỗ: bài toán token mới, slippage và phí"
description: Chỉ 0,41% ví pump.fun chốt lời hơn 10.000 USD. Bài toán đơn giản về token mới, slippage và phí khiến người mua memecoin luôn ở thế bất lợi.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41%
stat_label: trong 13,55 triệu ví pump.fun đã chốt lời hơn 10.000 USD (dữ liệu Dune, tháng 1/2025)
---
**Vì sao phần lớn người mua memecoin lại thua lỗ?** Vì bài toán đã bất lợi cho họ ngay cả trước khi giá nhúc nhích: đa số token mới chết trong vòng một ngày, mỗi lần mua và bán đều tốn phí và slippage, còn những người mua sớm nhất (thường là bot và người trong cuộc) bán lại cho người đến sau. Muốn có lời, token phải sống sót *và* tăng đủ mạnh để bù hết những khoản đó.

> **Điểm chính**
> - Dữ liệu Dune công bố tháng 1/2025 cho thấy chỉ khoảng **0,41%** trong 13,55 triệu ví pump.fun đã chốt lời hơn **10.000 USD**.
> - CoinGecko phát hiện **68,67%** token trên pump.fun có giao dịch cuối cùng ngay trong ngày ra mắt (dữ liệu tháng 1/2024 – tháng 6/2026).
> - Mỗi vòng mua + bán một token mới có thể tốn **2,5%+** chỉ riêng phí nền tảng, chưa kể phí mạng và slippage.

## Phần 1 — Bài toán sống sót

Phần lớn memecoin không phải là "rẻ" — chúng chỉ sống rất ngắn.

- **Chết ngay ngày ra mắt.** CoinGecko đếm được 18,67 triệu token pump.fun; 68,67% có giao dịch cuối cùng ngay trong ngày ra mắt (báo cáo ngày 25/6/2026).
- **Rất ít token ra được thị trường thật.** "Graduation" (tốt nghiệp) nghĩa là token rời khỏi đường cong khởi đầu của pump.fun và có một pool giao dịch bình thường. Dữ liệu Dune cho thấy tỷ lệ tốt nghiệp hằng tuần nằm dưới **1%** suốt bốn tuần kể từ 17/2/2025; tuần tốt nhất, vào tháng 11/2024, là **1,67%**. Đến tháng 3/2026 tỷ lệ này đạt **2,01%**, cao nhất kể từ tháng 7/2025.

Vậy nếu bạn chọn token mới một cách ngẫu nhiên, phần lớn coin bạn cầm sẽ ngừng giao dịch. Vài token thắng lớn không thể bù cho rất nhiều token về 0, trừ khi bạn chọn cực giỏi — mà ngày đầu tiên thì chẳng ai biết token nào sẽ sống sót.

## Phần 2 — Phí: bạn trả khi vào và trả cả khi ra

Trang trợ giúp của pump.fun (tháng 9/2025) ghi phí **1,25%** cho mỗi giao dịch trước khi tốt nghiệp (0,95% cho nền tảng, 0,30% cho người tạo token). Sau khi tốt nghiệp, phí giảm dần khi token lớn lên, từ 1,25% với token nhỏ nhất xuống 0,30% với token lớn nhất. Cộng thêm phí mạng Solana và các khoản phí tùy chọn "priority" (ưu tiên) và chống MEV (0,003–0,03 SOL mỗi giao dịch theo trang của họ).

**Ví dụ tính toán (minh họa, không phải giá thật):** bạn mua 50 USD một token mới và trả phí priority 0,02 SOL mỗi chiều. Phí 1,25% lúc vào và lúc ra khoảng 1,25 USD, còn hai lần phí priority có thể thêm vài đô nữa. Chỉ để về lại 50 USD, token có lẽ phải tăng **5–10%**. Với lệnh 10 USD còn tệ hơn nhiều: phí cố định chiếm phần lớn hơn hẳn.

## Phần 3 — Slippage: giá chạy trong lúc bạn mua

**Slippage** (trượt giá) là chênh lệch giữa giá bạn thấy và giá bạn thực sự nhận (xem [thuật ngữ memecoin]({lang}/memes/glossary/)). Token mới có pool rất nhỏ, nên chính lệnh mua của bạn đẩy giá lên — lệnh mua của người khác trong cùng giây đó cũng vậy. Nếu bạn đặt slippage 10–20% (nhiều ứng dụng gợi ý mức này cho coin mới), tức là bạn chấp nhận trả đắt hơn tới mức đó. Khi bán thì ngược lại: trong pool mỏng, lệnh bán của bạn đè giá xuống.

## Phần 4 — Ai đứng ở phía bên kia

Người mua sớm nhất thường là sniper, bundler và ví của dev (xem [sniper, bundler và ví dev]({lang}/blog/snipers-bundlers-dev-wallets/)). Họ mua ở giá thấp nhất rồi bán vào làn sóng nhu cầu đầu tiên. Nếu bạn mua sau cây nến xanh đầu tiên, rất có thể bạn là "exit liquidity" — số tiền mà họ bán lại để thoát hàng.

## Từng bước: kiểm tra bài toán trước khi bấm «Mua»

1. **Bước 1 — Cộng phí.** Xem dòng phí trên màn hình swap và cộng thêm phí mạng/priority. Nhân đôi (mua + bán).
2. **Bước 2 — Kiểm tra slippage.** Đặt thấp nhất mà lệnh vẫn khớp (ví dụ 1–3% với coin có pool lớn). Nếu coin cần slippage 20%, đó là dấu hiệu cảnh báo.
3. **Bước 3 — Kiểm tra quy mô pool.** Trên [trang memes]({lang}/memes/) của chúng tôi, mở token và xem thanh khoản. Pool nhỏ = slippage lớn cả hai chiều.
4. **Bước 4 — Kiểm tra an toàn.** Dùng bài [cách kiểm tra memecoin trước khi mua]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Bước 5 — Quyết định trước số tiền chấp nhận mất.** Chỉ dùng tiền bạn có thể mất hết, và chốt số tiền trước khi bắt đầu.

> **⚠️ Cẩn thận**
> - **"Giá chỉ 0,0001 USD, có thể tăng 1000×."** Giá thấp chẳng nói lên điều gì; nhiều token có lượng cung tới hàng tỷ. Điều quan trọng là token có sống sót không và ai đang bán cho bạn.
> - **Quá nhiều lệnh nhỏ.** Phí mạng và phí priority cố định có thể ngốn 10%+ của một lệnh 10 USD trước khi giá kịp nhúc nhích.
> - **Ảnh chụp màn hình người thắng.** Bạn thấy 0,41% thắng lớn, chứ không thấy hàng triệu người thua; các "guru" thường đang bán chính coin họ quảng cáo.

## Ý nghĩa nếu bạn mua đều đặn

Mua nhỏ đều đặn hiệu quả với tài sản vẫn còn tồn tại nhiều năm sau — không phải với token có thể ngừng giao dịch ngay tối nay. Nếu muốn đầu tư crypto, con đường quen thuộc cho người mới là một coin lớn, thanh khoản cao, mua dần từng chút; để so sánh, coin của chính Solana là SOL hiện ở mức {{price:sol}} ({{chg1y:sol}} trong 12 tháng) — kết quả quá khứ, không phải dự báo. Bạn có thể thử «10 USD mỗi ngày» với bất kỳ tài sản nào trong máy tính của chúng tôi và theo dõi trên [trang danh mục]({lang}/me/).

Bài trước: [sniper, bundler và ví dev]({lang}/blog/snipers-bundlers-dev-wallets/). Tất cả bài học có trên [trang Học]({lang}/learn/).

## Nguồn

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11/1/2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14/3/2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, dữ liệu Dune: pump.fun graduation rate hits 2.01% (17/3/2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / dữ liệu CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25/6/2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun Help Center: Transaction fees on pump.fun (tháng 9/2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Không phải lời khuyên đầu tư.*
