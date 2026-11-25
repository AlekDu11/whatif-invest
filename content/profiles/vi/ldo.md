---
title: Lido DAO (LDO) giải thích dễ hiểu: staking thanh khoản stETH từ 2020, giới hạn 1 tỷ token và quản trị kép
description: Lido giải thích dễ hiểu: stETH và wstETH hoạt động ra sao, LDO dùng để làm gì, quản trị kép, mua lại token, lịch sử từ 2020, đối thủ và rủi ro chính.
date: 2026-11-25
kind: analysis
---
**Lido** là dịch vụ staking ether lớn nhất: bạn giao ETH cho Lido, Lido vận hành validator thông qua các nhà vận hành node chuyên nghiệp, còn bạn nhận **stETH**, một token tăng dần theo phần thưởng staking và vẫn có thể giao dịch hoặc dùng trong các ứng dụng khác. Lido do một DAO điều hành, và token quản trị **LDO** hiện có vốn hóa {{mcap:ldo}} ({{rank:ldo}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Lido ra mắt tháng 12/2020; ngày 30/6/2026 Lido nắm khoảng 9,13 triệu ETH đang staking, xấp xỉ 21% tổng số ether được staking.
> - LDO có nguồn cung cố định 1 tỷ token. Token này cho quyền biểu quyết về giao thức, không chia trực tiếp phí.
> - Từ cuối tháng 6/2025, người giữ stETH có thể trì hoãn hoặc chặn quyết định của DAO nhờ cơ chế "quản trị kép" (dual governance).
> - Đỉnh kỷ lục là {{ath:ldo}} ({{athd:ldo}}); hiện giá cách đỉnh {{fromath:ldo}}.

## Cách hoạt động

Muốn tự chạy validator Ethereum, bạn cần 32 ETH, một máy chủ luôn trực tuyến và hiểu cách tránh bị phạt. Lido gom tiền gửi với mọi mức và chia cho nhiều nhà vận hành node. Đổi lại, bạn nhận **stETH** theo tỷ lệ một đổi một, và số dư trong ví tăng lên mỗi ngày theo phần thưởng. **wstETH** là phiên bản "đóng gói" với số dư cố định nhưng giá trị tăng dần; đây là dạng mà phần lớn ứng dụng DeFi và các blockchain khác sử dụng. Lido giữ 10% phần thưởng staking và chia cho nhà vận hành node cùng kho bạc DAO; người staking nhận 90% còn lại. Từ Lido V2 vào tháng 5/2023, stETH còn có thể rút trực tiếp về ETH. Tháng 1/2026, Lido V3 bổ sung **stVaults**: các cấu hình staking riêng cho tổ chức, quỹ và các mạng như Linea, vẫn cho phép tiếp cận stETH.

## Vì sao người ta cho rằng nó có giá trị

Người giữ LDO biểu quyết về cách giao thức vận hành: mức phí, nhà vận hành node nào tham gia, nâng cấp và cách chi tiêu kho bạc. Vì vậy đặt cược vào LDO là đặt cược rằng Lido sẽ tiếp tục ở trung tâm của staking Ethereum. Trong nhiều năm, phí chảy vào kho bạc và người giữ token không nhận được gì trực tiếp. Điều này bắt đầu thay đổi vào năm 2026: DAO đổi khoảng 1.591 stETH lấy khoảng 10 triệu LDO trong một đợt mua lại một lần, và thông qua cơ chế mua lại tự động (NEST), chỉ mua LDO khi doanh thu staking hằng năm vượt 40 triệu USD. Tính đến giữa năm 2026, ngưỡng này chưa đạt. Với quản trị kép, phiếu LDO cũng không còn là tiếng nói cuối cùng: người staking có thể phủ quyết những thay đổi họ không muốn.

## Các con số hiện tại

- Giá hôm nay: {{price:ldo}}
- Đỉnh kỷ lục: {{ath:ldo}} ({{athd:ldo}}), cách đỉnh {{fromath:ldo}}
- Vốn hóa thị trường: {{mcap:ldo}} ({{rank:ldo}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:ldo}}
- 10 USD mỗi ngày trong 4 năm: {{dca:ldo:4}} từ {{dcainv:4}} đã đầu tư ({{dcaroi:ldo:4}})
- Nguồn cung tối đa: 1 tỷ LDO

## Câu chuyện của Lido

Lido do Konstantin Lomashuk và Vasiliy Shapovalov sáng lập và đi vào hoạt động ngày 19/12/2020, khi ETH staking trên Beacon Chain mới chưa thể rút ra — stETH giúp tiền không bị "đóng băng". Lido tăng trưởng nhanh trong cơn sốt DeFi năm 2021, và LDO lập đỉnh vào tháng 8/2021. Tháng 6/2022, khi Celsius và Three Arrows Capital sụp đổ, stETH giao dịch thấp hơn ETH suốt nhiều tuần. Sau khi việc rút tiền trở nên khả thi vào năm 2023, thị phần của Lido trong tổng ETH staking lên gần một phần ba, rồi giảm dần khi các sàn giao dịch, đơn vị lưu ký và đối thủ lớn mạnh. Lido đóng các phiên bản trên blockchain khác để tập trung vào Ethereum. Doanh thu năm 2025 giảm 23%, còn 40,5 triệu USD, năm 2026 LDO rơi xuống mức giá thấp nhất trong lịch sử, và DAO đáp lại bằng việc mua lại token và ra mắt stVaults.

## Các lựa chọn thay thế

Trong staking thanh khoản, Lido cạnh tranh với [Rocket Pool]({lang}/rpl/), [Ether.fi]({lang}/ethfi/) và dịch vụ staking của các sàn như Coinbase, Binance, cùng các ETF có staking và đơn vị lưu ký cho nhà đầu tư lớn. Ở mảng restaking và công cụ cho validator có [EigenCloud (EigenLayer)]({lang}/eigen/) và [SSV Network]({lang}/ssv/). Nhiều người chỉ đơn giản nắm giữ [Ethereum]({lang}/eth/), và số phận của LDO phụ thuộc nhiều vào giá ETH.

## Rủi ro chính

- **Biến động mạnh:** đến năm 2026 LDO đã giảm hơn 95% so với đỉnh năm 2021 và có thể còn giảm nữa.
- **Hợp đồng thông minh và nhà vận hành:** một lỗi, vụ hack hay khoản phạt lớn với validator của Lido có thể khiến người staking mất tiền và kéo token đi xuống.
- **Mất thị phần:** phần của Lido trong tổng ETH staking thu hẹp từ năm 2023; ít ETH hơn nghĩa là ít doanh thu hơn.
- **Gắn kết yếu với doanh thu:** LDO chủ yếu cho quyền biểu quyết; việc mua lại chỉ bắt đầu khi doanh thu đủ cao.
- **Tập trung và pháp lý:** việc một giao thức nắm phần lớn ETH staking khiến một bộ phận cộng đồng Ethereum lo ngại, và quy định về staking khác nhau theo từng quốc gia.

## Ý nghĩa nếu bạn mua định kỳ

Từ năm 2022, câu chuyện của LDO chủ yếu là một đợt giảm dài xen kẽ những lần hồi ngắn. Mua một khoản cố định định kỳ giúp chia đều các lần mua qua lúc lên và lúc xuống mà không cần đoán đáy, nhưng không loại bỏ rủi ro thua lỗ, và một token quản trị có thể vẫn rẻ ngay cả khi giao thức rất lớn. Nếu bạn chủ yếu muốn phần thưởng staking, stETH và LDO là hai thứ rất khác nhau: một cái đi theo ETH, cái kia là khoản cược vào chính Lido. Nhiều người chỉ dành một phần nhỏ tiền tiết kiệm cho token của một dự án đơn lẻ như thế này. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [GOOSE-2026 & EGGs-2026 H1 Report (Lido, 2026)](https://lido.fi/ldo-hub/reports/h1-2026)
- [Lido DAO votes to enable dual governance, giving stakers veto power (The Block, June 2025)](https://www.theblock.co/post/360212/lido-dao-votes-to-enable-dual-governance-giving-stakers-veto-power)
- [Lido rolls out stVaults on mainnet (The Block, January 2026)](https://www.theblock.co/post/387769/lido-stvaults-mainnet)
- [Lido revenue dropped 23% last year (The Block, March 2026)](https://www.theblock.co/post/394947/lido-revenue-dropped-23-last-year-users-withdrew-funds-yields-declined)
- [Lido DAO (LDO) price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/lido-dao)
