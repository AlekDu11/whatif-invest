---
title: Curve DAO (CRV) giải thích dễ hiểu: sàn stablecoin, khóa veCRV và giới hạn 3 tỷ token
description: Curve bằng ngôn ngữ đơn giản: cách sàn stablecoin và crvUSD hoạt động, vì sao khóa CRV thành veCRV, Curve Wars, các vụ hack, đối thủ, rủi ro và mua định kỳ.
date: 2026-11-24
kind: analysis
---
**Curve Finance** là sàn giao dịch phi tập trung được xây dựng để hoán đổi những đồng coin lẽ ra có giá trị gần như nhau — chủ yếu là stablecoin đô la như USDT, USDC và DAI, nhưng cũng có các phiên bản khác nhau của ETH hoặc bitcoin. Curve ra mắt năm 2020, do Michael Egorov tạo ra và chạy trên Ethereum cùng nhiều blockchain khác. **CRV** là token quản trị của Curve, tổng giá trị {{mcap:crv}} ({{rank:crv}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Tổng nguồn cung CRV giới hạn ở khoảng 3,03 tỷ; token mới được trả cho nhà cung cấp thanh khoản, và lượng phát hành hằng năm giảm dần từng bước.
> - Đỉnh kỷ lục là {{ath:crv}} ({{athd:crv}}), lập trong những ngày giao dịch đầu tiên vào tháng 8/2020; giá hiện tại cách đỉnh {{fromath:crv}}.
> - Người dùng khóa CRV tối đa bốn năm dưới dạng veCRV để bỏ phiếu và nhận một phần phí của giao thức.
> - Curve còn phát hành stablecoin đô la riêng là crvUSD, ra mắt năm 2023.

## Cách hoạt động

Thay vì sổ lệnh, Curve dùng các pool: người dùng gửi vào các cặp hoặc nhóm coin, và trader hoán đổi với pool đó. Công thức của Curve giữ giá rất sát khi các coin trong pool có giá trị gần như bằng nhau, nên một giao dịch lớn, chẳng hạn từ USDC sang USDT, tốn rất ít chi phí. Người gửi coin nhận phí giao dịch và phần thưởng CRV. crvUSD là stablecoin được đúc dựa trên tài sản thế chấp tiền mã hóa; thay vì thanh lý đột ngột, cơ chế "thanh lý mềm" (soft liquidation) chuyển đổi dần tài sản thế chấp khi giá giảm. Các pool và thị trường cho vay của Curve được nhiều ứng dụng DeFi khác sử dụng ở phía sau.

## Token CRV dùng để làm gì

CRV có công dụng chính khi được khóa dưới dạng **veCRV** ("vote-escrowed CRV"). Khóa càng lâu — tối đa bốn năm — quyền biểu quyết càng lớn. Người nắm giữ veCRV bỏ phiếu về các nâng cấp và về việc pool nào nhận nhiều phần thưởng CRV nhất, nhận một phần phí giao dịch và lãi crvUSD, đồng thời có thể tăng phần thưởng của chính mình. Vì quyền điều hướng phần thưởng rất có giá trị, các dự án khác cạnh tranh để mua hoặc "hối lộ" phiếu veCRV — cuộc đua được gọi là "Curve Wars".

## Các con số hiện tại

- Giá hôm nay: {{price:crv}}
- Đỉnh kỷ lục: {{ath:crv}} ({{athd:crv}}), cách đỉnh {{fromath:crv}}
- Vốn hóa thị trường: {{mcap:crv}} ({{rank:crv}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:crv}}
- 10 USD mỗi ngày trong 5 năm: {{dca:crv:5}} từ {{dcainv:5}} đã đầu tư ({{dcaroi:crv:5}})

## Câu chuyện của Curve

Curve khởi đầu vào tháng 1/2020, và token CRV đi vào hoạt động tháng 8/2020; trong cơn sốt những ngày đầu, giá có lúc vọt lên trên 15 USD trước khi giảm nhanh. Trong năm 2021, Curve Wars biến Curve thành một trong những giao thức DeFi quan trọng nhất, với các giao thức như Convex gom được lượng veCRV khổng lồ. Tháng 5/2023, crvUSD ra mắt. Tháng 7/2023, một lỗi trong ngôn ngữ lập trình Vyper cho phép kẻ tấn công rút cạn nhiều pool với tổng giá trị khoảng 70 triệu USD, một phần sau đó đã được trả lại. Tháng 6/2024, các khoản vay lớn mà nhà sáng lập vay bằng cách thế chấp CRV của mình bị thanh lý, khiến giá giảm mạnh. Năm 2025, DAO phê duyệt hạn mức tín dụng crvUSD trị giá 60 triệu USD cho Yield Basis, giao thức mới của Egorov xây dựng trên các pool của Curve.

## Các lựa chọn thay thế

[Uniswap]({lang}/uni/) là sàn phi tập trung đa năng lớn nhất và cũng xử lý lượng lớn giao dịch stablecoin. [Balancer]({lang}/bal/) cung cấp các pool nhiều coin tương tự, còn trong mảng cho vay và stablecoin, Curve cạnh tranh với [Aave]({lang}/aave/) và [Sky]({lang}/sky/) (trước đây là Maker), đơn vị phát hành USDS và DAI. Sàn giao dịch tập trung vẫn là nơi chính mà hầu hết mọi người dùng để hoán đổi stablecoin.

## Rủi ro chính

- **Biến động mạnh:** CRV đã mất hơn 90% so với đỉnh năm 2020; token DeFi có thể lao dốc nhanh trong khủng hoảng.
- **Rủi ro hợp đồng thông minh:** vụ khai thác lỗ hổng năm 2023 cho thấy một lỗi, kể cả trong ngôn ngữ lập trình, cũng có thể rút cạn tiền.
- **Tập trung:** một vài giao thức và những người nắm giữ lớn kiểm soát phần lớn phiếu veCRV, và chính vị thế của nhà sáng lập đã từng làm giá biến động một lần.
- **Nguồn cung:** CRV mới liên tục được đưa ra thị trường dưới dạng phần thưởng, và nhiều người nhận đã bán chúng.
- **Quy định:** quy tắc cho sàn DeFi và stablecoin đang thay đổi ở Mỹ, EU và nhiều nơi khác, có thể hạn chế khả năng tiếp cận.

## Ý nghĩa nếu bạn mua định kỳ

Curve là giao thức hoạt động lâu năm và được sử dụng rộng rãi, nhưng biểu đồ giá token của nó chủ yếu đi xuống kể từ năm 2020. Mua một khoản cố định đều đặn giúp dàn trải thời điểm vào lệnh, nên bạn mua được nhiều hơn khi giá thấp mà không cần đoán đáy — nhưng không loại bỏ rủi ro thua lỗ. Nhiều người chỉ để token DeFi chiếm một phần nhỏ trong tiền tiết kiệm. Kết quả trong quá khứ không đảm bảo lợi nhuận tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Curve Finance — official site and docs (curve.finance)](https://curve.finance/)
- [Curve technical docs: CRV, veCRV and crvUSD (docs.curve.finance)](https://docs.curve.finance/)
- [Yield Basis clears Curve DAO vote hurdle (Blockworks)](https://blockworks.co/news/yield-basis-curve-dao-vote)
- [Curve DAO Token price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/curve-dao-token)
