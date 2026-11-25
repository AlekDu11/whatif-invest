---
title: Lighter (LIT) giải thích dễ hiểu: hợp đồng vĩnh cửu không phí trên zk-rollup của Ethereum và điều gì làm token biến động
description: Lighter bằng ngôn ngữ đơn giản: sàn hợp đồng tương lai vĩnh cửu trên zk-rollup riêng của Ethereum, 0 phí cho nhà giao dịch nhỏ lẻ, token LIT và các rủi ro.
date: 2026-11-25
kind: analysis
---
**Lighter** là sàn giao dịch phi tập trung cho hợp đồng tương lai vĩnh cửu (perpetual futures) — loại hợp đồng cho phép bạn đặt cược vào giá bitcoin, ether và các tài sản khác bằng đòn bẩy. Sàn chạy trên zk-rollup riêng xây trên Ethereum, nhà giao dịch thông thường không trả phí giao dịch, và mỗi lần khớp lệnh đều được kiểm chứng bằng bằng chứng không tiết lộ (zero-knowledge). Token **LIT** của sàn ra mắt ngày 30/12/2025 và hôm nay có giá trị {{mcap:lit}} ({{rank:lit}} trong các loại tiền mã hóa).

> **Điểm chính**
> - Có tổng cộng 1 tỷ LIT; 50% dành cho hệ sinh thái, trong đó 25% được airdrop cho người dùng sớm vào tháng 12/2025.
> - Mức giá kỷ lục là {{ath:lit}} ({{athd:lit}}); hôm nay giá cách kỷ lục {{fromath:lit}}.
> - Token của đội ngũ (26%) và nhà đầu tư (24%) bị khóa một năm sau khi ra mắt, sau đó được mở dần trong ba năm.
> - Với nhà giao dịch nhỏ lẻ, giao dịch qua website và ứng dụng là miễn phí; phí do các nhà giao dịch chuyên nghiệp qua API và giao dịch tần suất cao trả.

## Cách hoạt động

Lighter là một mạng lớp 2 (layer 2) trên Ethereum. Giao dịch diễn ra trong sổ lệnh tốc độ cao của riêng Lighter, và các mạch zero-knowledge được thiết kế riêng chứng minh rằng lệnh được khớp công bằng theo giá và thời gian, còn thanh lý, thanh toán funding và kiểm tra rủi ro đều tuân theo quy tắc. Tiền của người dùng nằm trong hợp đồng thông minh của Ethereum, và trạng thái mạng chỉ được cập nhật sau khi bằng chứng được xác minh trên Ethereum. Nếu bên vận hành ngừng hoạt động hoặc kiểm duyệt người dùng, họ có thể gửi yêu cầu thẳng lên Ethereum hoặc rút ra qua lối thoát khẩn cấp gọi là "Desert Mode".

## Cách kiếm tiền và vai trò của LIT

Mô hình kinh doanh của Lighter khá khác thường: ai giao dịch qua giao diện thì không trả gì, còn luồng lệnh qua API và giao dịch tần suất cao — các nhà tạo lập thị trường và công ty trading — trả phí "premium". Đội ngũ cho biết doanh thu của sàn và của các sản phẩm tương lai hiển thị trên chuỗi và được dùng cho tăng trưởng và mua lại LIT tùy điều kiện thị trường; phí và các đợt mua lại có thể theo dõi qua tài khoản ngân quỹ trên trình duyệt khối của Lighter.

LIT do công ty Lighter tại Mỹ phát hành. Tháng 1/2026, staking trở thành công dụng lớn đầu tiên của token: muốn nạp tiền vào Lighter Liquidity Pool (LLP) — quỹ mang lại lợi suất và đóng vai trò quỹ bảo hiểm khi thanh lý — bạn phải stake 1 LIT cho mỗi 10 USDC. Ai stake ít nhất 100 LIT được miễn phí rút và chuyển tiền, đồng thời staking giúp giảm phí premium. Đội ngũ cũng dự định gắn hạ tầng giao dịch và xác minh tính công bằng của mình với việc stake LIT.

## Các con số hiện tại

- Giá hôm nay: {{price:lit}}
- Kỷ lục: {{ath:lit}} ({{athd:lit}}), cách kỷ lục {{fromath:lit}}
- Giá trị thị trường: {{mcap:lit}} ({{rank:lit}} trong các loại tiền mã hóa)
- Tổng cung: 1 tỷ LIT (50% hệ sinh thái, 26% đội ngũ, 24% nhà đầu tư)

## Câu chuyện của Lighter

Lighter được thành lập năm 2022 bởi Vladimir Novakovski, người vào Harvard năm 16 tuổi và bắt đầu làm việc tại Citadel năm 18 tuổi. Dự án ra đời từ Lunchclub, ứng dụng kết nối nghề nghiệp dùng AI mà ông đồng sáng lập năm 2017; phần lớn đội ngũ đó chuyển sang Lighter. Năm 2024 dự án gọi vốn 21 triệu USD trong vòng do Haun Ventures và Craft Ventures dẫn dắt. Sau khoảng tám tháng thử nghiệm kín với khoảng 188.000 tài khoản, mạng chính công khai mở cửa vào tháng 10/2025.

Tăng trưởng rất nhanh: giữa tháng 11/2025, khối lượng giao dịch theo tuần đạt đỉnh 74,9 tỷ USD, và trong tháng 11/2025 Lighter báo cáo 292,5 tỷ USD, vượt Aster và Hyperliquid. Cũng trong tháng đó, sàn gọi vốn 68 triệu USD trong vòng do Founders Fund và Ribbit Capital dẫn dắt, có Haun Ventures và Robinhood tham gia, theo báo chí với mức định giá khoảng 1,5 tỷ USD. Đầu tháng 12/2025 sàn bổ sung giao dịch giao ngay.

LIT bắt đầu giao dịch ngày 30/12/2025; đợt airdrop cho người giữ điểm của hai mùa đầu năm 2025 khi đó trị giá khoảng 675 triệu USD. Đầu tháng 1/2026 tài khoản ngân quỹ bắt đầu tích lũy LIT, được thị trường hiểu là mua lại, và ngày 14/1/2026 sàn công bố bắt buộc stake cho LLP. Sau airdrop, nhiều người "săn điểm" rời đi: đến giữa tháng 1/2026 khối lượng theo tuần giảm còn khoảng 25,3 tỷ USD, chừng một phần ba mức đỉnh, và Hyperliquid giành lại vị trí số một.

## Các lựa chọn thay thế

Đối thủ chính là [Hyperliquid]({lang}/hype/), chạy trên blockchain lớp 1 riêng thay vì Ethereum và có token HYPE. [Aster]({lang}/aster/) cạnh tranh với Lighter cho vị trí số một về khối lượng vào cuối năm 2025, còn [dYdX]({lang}/dydx/) là một trong những sàn hợp đồng vĩnh cửu phi tập trung lâu đời nhất. Các sàn tập trung lớn như Binance và OKX vẫn chiếm phần lớn giao dịch hợp đồng tương lai tiền mã hóa.

## Rủi ro chính

- **Khối lượng nhờ phần thưởng:** phần lớn hoạt động năm 2025 đến từ việc săn điểm trước airdrop; sau đó khối lượng giảm khoảng ba lần chỉ trong vài tuần.
- **Mở khóa token:** một nửa nguồn cung thuộc đội ngũ và nhà đầu tư; sau một năm khóa, số token này được mở trong ba năm, có thể tạo áp lực bán.
- **Cạnh tranh:** Hyperliquid, Aster và các sàn tập trung giành cùng một nhóm nhà giao dịch, và giao dịch miễn phí rất dễ bị sao chép.
- **Công nghệ:** một zk-rollup non trẻ với sổ lệnh và hệ thống bằng chứng riêng có thể gặp lỗi hoặc sự cố, dù có lối thoát qua Ethereum.
- **Quy định:** sản phẩm phái sinh có đòn bẩy bị quản lý chặt ở nhiều nước, và quy định với sàn phi tập trung có thể thay đổi.
- **Biến động mạnh:** LIT là token non trẻ; những cú giảm sâu sau khi ra mắt là một phần lịch sử của nó.

## Ý nghĩa nếu bạn mua định kỳ

LIT mới giao dịch chưa đầy một năm, nên chưa có lịch sử "10 USD mỗi ngày" dài để tham khảo — mọi kết quả chỉ phản ánh một giai đoạn ngắn và rất biến động. Mua một khoản cố định đều đặn giúp trải giá vào lệnh theo thời gian thay vì đặt cược vào một thời điểm, nhưng không loại bỏ rủi ro thua lỗ, nhất là với token non trẻ và các đợt mở khóa sắp tới. Nếu mua, nhiều người chỉ giữ loại token này ở một phần nhỏ khoản tiết kiệm mà họ chấp nhận được việc giảm mạnh. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Lighter launches native token LIT, allocates half to ecosystem growth (The Block, 30/12/2025)](https://www.theblock.co/post/383940/lighter-native-token-lit)
- [Lighter introduces mandatory LIT staking for liquidity pool access (The Block, 14/1/2026)](https://www.theblock.co/post/385696/lighter-lit-staking)
- [Lighter opens public mainnet with Ethereum-settled zk perps (Blockworks)](https://blockworks.co/news/lighter-opens-public-mainnet)
- [DeFi founder who graduated Harvard at 18 raises $68 million for crypto trading protocol Lighter (Fortune, 11/11/2025)](https://fortune.com/2025/11/11/lighter-fundraise-founders-fund-ribbit-capital-haun-ventures-robinhood-vladimir-novakovski/)
- [Trading volume on Lighter plummets threefold after airdrop (ForkLog, 19/1/2026)](https://forklog.com/en/news/trading-volume-on-lighter-exchange-plummets-threefold-after-airdrop)
- [Lighter: giá, vốn hóa và mức cao nhất mọi thời đại (CoinGecko)](https://www.coingecko.com/en/coins/lighter)
