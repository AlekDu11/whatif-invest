---
title: "Sniper, bundler và ví dev: người trong cuộc kiếm lời thế nào khi memecoin ra mắt"
description: Bot và người trong cuộc mua nhiều memecoin mới ngay giây đầu rồi bán trong vài phút. Sniper, bundler, ví dev hoạt động ra sao và cách nhận ra chúng.
date: 2026-11-27T09:30:00Z
category: learn
track: memes
step: 16
assets: sol, bnb
stat: 87%
stat_label: lệnh snipe liên quan đến ví người tạo token trên pump.fun có lãi (Pine Analytics, 4/2025)
---
**Ai mua memecoin mới trước cả khi bạn kịp nhìn thấy nó?** Thường là bot và người trong cuộc: **sniper** mua ngay ở block đầu tiên, **bundler** mua bằng nhiều ví cùng lúc, còn **ví dev** (dev wallet — ví của chính người tạo token) có thể nắm một phần lớn ngay từ đầu. Họ mua rẻ nhất và thường bán trong vài phút — cho những người đến sau.

> **Điểm chính**
> - Pine Analytics phát hiện hơn **50%** token trên pump.fun bị snipe ngay trong block mà token được tạo ra (báo cáo ngày 21/4/2025).
> - Trong một tháng (từ 15/3/2025), họ đếm được **hơn 15.000** lệnh snipe từ các ví được chính người tạo token cấp tiền; **87%** có lãi và khoảng **85%** bán sạch trong vòng **5 phút**.
> - CoinGecko thấy **68,67%** trong số 18,67 triệu token pump.fun có giao dịch cuối cùng ngay trong ngày ra mắt (1/2024 – 6/2026, công bố ngày 25/6/2026).

## Ba kiểu người trong cuộc, nói đơn giản

Cả ba thuật ngữ đều có trong [từ điển memecoin]({lang}/memes/glossary/) của chúng tôi.

- **Sniper** — một ví, gần như luôn là bot, mua trong 0–3 block đầu tiên (block là một "trang" của blockchain, trên Solana chưa tới một giây). Nó dùng công cụ đặc biệt để vào trước người mua bình thường, gom một lượng lớn với giá rẻ rồi bán vào làn sóng mua đầu tiên.
- **Bundler** — một người mua bằng nhiều ví trong cùng một block hoặc cùng một giao dịch. Trên biểu đồ trông như 20 người mua khác nhau; thực ra chỉ là một. Mục đích: che giấu một người nắm bao nhiêu và tạo nhu cầu giả.
- **Ví dev** — ví đã tạo ra token. Nếu ví này giữ một phần lớn, hoặc lặng lẽ chuyển token sang các ví mới, nó có thể xả lên đầu mọi người bất cứ lúc nào.

Báo cáo "Exit Liquidity Machines" của Pine Analytics (exit liquidity — thanh khoản thoát — là những người mua đến muộn, tiền của họ là nơi người trong cuộc bán ra) cho thấy cách việc này diễn ra trên pump.fun: người tạo token gửi SOL sang các ví "dùng một lần" (burner) mới tạo, các ví đó mua ngay trong block tạo token, và phần lớn bán ra chỉ trong một hai lệnh. Hơn 55% số lệnh snipe này được đóng hoàn toàn trong chưa đầy một phút.

## Bước 1 — Xem những người mua đầu tiên

Mở token trên một công cụ theo dõi (trên [trang memes]({lang}/memes/) của chúng tôi, trang token hiển thị người nắm giữ và bước kiểm tra an toàn; các công cụ như GMGN hay Solscan hiển thị những giao dịch đầu tiên). Nếu nhiều ví mua **cùng giây với lúc ra mắt**, với **số tiền gần giống nhau**, đó là sniping hoặc bundling.

## Bước 2 — Kiểm tra các ví lớn nhất nắm bao nhiêu

Xem **top 10 người nắm giữ**, không tính pool thanh khoản. Nhà cung cấp dữ liệu Mobula coi top 10 dưới **30%** và phần của dev dưới **5%** (hoặc đã khóa/đốt) là lành mạnh, còn top 10 trên **50%** là dấu hiệu đỏ. Vài ví sniper cộng lại nắm hơn 20% cũng là một dấu hiệu đỏ.

## Bước 3 — Kiểm tra ví dev

Tìm người tạo ("dev", "deployer" hoặc "creator" trên trang token). Ví đó đã bán chưa? Có chuyển token sang ví mới ngay trước hay sau khi ra mắt không? Cùng ví đó đã tung ra nhiều token rồi token nào cũng chết chưa? Một dev tung ra hàng chục coin mỗi tuần là đang chạy một cỗ máy, không phải làm dự án.

## Bước 4 — Tìm các ví mới được cấp tiền từ một nguồn

Bundle thường đến từ các ví được tạo vài phút trước khi ra mắt và được nạp tiền từ cùng một nguồn. Các công cụ bubble map (bản đồ bong bóng) vẽ chúng thành một cụm liên kết. Nếu "cộng đồng" chỉ là một cụm, giá nằm trong tay một người.

## Bước 5 — Đừng bao giờ đu theo cây nến đầu tiên

Cú tăng trong những phút đầu chính là lúc sniper bán ra. Nếu bạn vẫn muốn mua, hãy chờ, làm đủ các bước kiểm tra trong bài [cách kiểm tra memecoin trước khi mua]({lang}/blog/how-to-check-a-memecoin-before-buying/), dùng số tiền nhỏ và đặt giới hạn từ trước.

> **⚠️ Cẩn thận**
> - **"Nhiều người nắm giữ = an toàn."** Bundler tạo ra hàng trăm người nắm giữ chỉ từ một ví. Hãy xem ai cấp tiền cho họ, đừng xem có bao nhiêu.
> - **"Dev đã đốt/khóa token."** Tự kiểm tra trên blockchain; pool bị khóa không ngăn được ví sniper bán ra.
> - **Bot copy-trade "smart money".** Những ví trông như thiên tài thường chính là sniper, hoặc là dev; đến lúc bạn sao chép theo thì họ đang bán.

## Người mới học được gì từ đây

Khi token ra mắt, bạn thường không phải người đến sớm — bot mới là người đến sớm. Gần 7 trên 10 token pump.fun ngừng giao dịch ngay ngày đầu, nên lựa chọn an toàn nhất thường là không chơi. Nếu có chơi, hãy coi đó là tiền bạn có thể mất sạch. Mua đều đặn phù hợp với tài sản tồn tại qua nhiều năm; để so sánh, coin của chính Solana là SOL hiện đang ở mức {{price:sol}} ({{chg1y:sol}} trong 12 tháng) — kết quả trong quá khứ, không phải dự báo.

Bài trước: [Binance Alpha hoạt động thế nào]({lang}/blog/how-binance-alpha-works/). Bài tiếp theo: vì sao phần lớn người mua memecoin thua lỗ. Tất cả bài học ở [trang Học]({lang}/learn/).

## Nguồn

- [Pine Analytics: Exit Liquidity Machines — dissecting pump.fun farming (21/4/2025)](https://pineanalytics.substack.com/p/exit-liquidity-machines)
- [BeInCrypto: Pump.fun meme coin snipers are a systematic problem (22/4/2025)](https://beincrypto.com/pump-fun-meme-coin-snipers-systematic-problem)
- [Mobula docs: Detecting snipers and bundlers](https://docs.mobula.io/almanac/detecting-snipers-bundlers)
- [KuCoin News / dữ liệu CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25/6/2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)

*Không phải lời khuyên đầu tư.*
