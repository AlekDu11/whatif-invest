---
title: Render (RENDER) giải thích dễ hiểu: mạng render GPU của OTOY, giới hạn 644 triệu token và chuyển sang Solana năm 2023
description: Render dễ hiểu: người sáng tạo trả tiền cho chủ GPU để render và chạy AI ra sao, mô hình đốt và đúc, chuyển sang Solana, đối thủ và rủi ro chính.
date: 2026-11-23
kind: analysis
---
**Render** là một chợ mua bán sức mạnh tính toán: nghệ sĩ, studio và nhà phát triển AI trả tiền để dùng card đồ họa (GPU) của người khác, còn chủ các GPU đó được trả bằng token RENDER. Dự án ra đời từ OTOY, công ty phần mềm đồ họa ở Los Angeles do Jules Urbach đứng đầu, và là một trong những token "AI và tính toán" nổi tiếng nhất, vốn hóa hôm nay {{mcap:render}} ({{rank:render}} trong các đồng tiền mã hóa).

> **Điểm chính**
> - Nguồn cung giới hạn khoảng 644 triệu RENDER; tháng 11/2026 khoảng 86% số đó đã lưu hành.
> - Từ tháng 12/2023 mạng vận hành theo mô hình đốt và đúc: token dùng để trả cho công việc bị đốt, còn token mới được đúc cho chủ GPU.
> - Tháng 11/2023 token chuyển từ Ethereum (mã RNDR) sang Solana (mã RENDER).
> - Đỉnh kỷ lục là {{ath:render}} ({{athd:render}}); hôm nay giá cách đỉnh {{fromath:render}}.

## Cách hoạt động

Render biến một cảnh 3D thành hình ảnh hoặc khung hình video hoàn chỉnh, và việc này cần rất nhiều sức mạnh GPU. Thay vì mua phần cứng đắt tiền, người sáng tạo gửi công việc lên mạng Render. Các "nhà vận hành node" độc lập có GPU nhàn rỗi nhận việc, phần lớn dùng phần mềm OctaneRender của OTOY, và được trả tiền sau khi kết quả được kiểm tra. Từ năm 2025 mạng cũng mở rộng sang AI và tính toán GPU nói chung, chẳng hạn qua nền tảng có tên Dispersed. Quy tắc được thay đổi qua các đề xuất công khai Render Network Proposals (RNP) do người nắm giữ token bỏ phiếu; Render Network Foundation, tách ra từ OTOY năm 2023, giám sát việc quản trị.

## Token dùng để làm gì

Giá công việc được tính bằng tiền thông thường. Theo Burn-and-Mint Equilibrium (RNP-001), người sáng tạo trả bằng RENDER và số token đó bị đốt — rút khỏi lưu hành — khi công việc xong. Mỗi epoch (khoảng một tuần) mạng đúc RENDER mới theo lịch cố định và giảm dần, rồi chia cho các nhà vận hành node và những người đóng góp khác. Nếu nhu cầu thật đốt nhiều hơn lượng được đúc, nguồn cung giảm; nếu nhu cầu yếu, nguồn cung tăng. RENDER cũng được dùng để bỏ phiếu cho các đề xuất.

## Các con số hiện tại

- Giá hôm nay: {{price:render}}
- Đỉnh kỷ lục: {{ath:render}} ({{athd:render}}), cách đỉnh {{fromath:render}}
- Vốn hóa thị trường: {{mcap:render}} ({{rank:render}} trong các đồng tiền mã hóa)
- Biến động giá trong 12 tháng: {{chg1y:render}}
- 10 USD mỗi ngày trong 1 năm: {{dca:render:1}} từ {{dcainv:1}} đã đầu tư ({{dcaroi:render:1}})

## Câu chuyện của Render

Jules Urbach lần đầu mô tả ý tưởng này vào năm 2009. Đợt bán token công khai diễn ra vào tháng 10/2017, đợt bán riêng từ tháng 1 đến tháng 5/2018, và mạng mở cho mọi người vào ngày 27/4/2020. Năm 2023 giá token tăng gấp nhiều lần khi trí tuệ nhân tạo trở thành chủ đề được thị trường yêu thích nhất. Người nắm giữ bỏ phiếu chuyển sang Solana (RNP-002), việc chuyển hoàn tất ngày 2/11/2023, và việc phát hành token theo mô hình đốt và đúc bắt đầu từ tháng 12/2023. Giá lên đỉnh vào tháng 3/2024 giữa cơn sốt AI, và trong năm 2024 các sàn chuyển từ RNDR sang RENDER. Tháng 11/2026 Render giảm khoảng 12% trong một tuần khi các token liên quan đến AI cùng đi xuống.

## Các lựa chọn thay thế

Các mạng GPU và tính toán phi tập trung khác gồm [Akash]({lang}/akt/), [io.net]({lang}/io/), [Aethir]({lang}/ath/) và [Golem]({lang}/glm/); [Bittensor]({lang}/tao/) là một trong những dự án crypto-AI lớn nhất. Nhưng đối thủ thật sự là các đám mây lớn như Amazon Web Services và Google Cloud.

## Rủi ro chính

- **Biến động mạnh:** các token AI nhỏ có thể giảm sâu hơn bitcoin nhiều; sau đỉnh tháng 3/2024, Render đã mất phần lớn giá trị.
- **Phát hành mới:** RENDER mới được đúc mỗi epoch; nếu công việc thật không đốt đủ token, nguồn cung tiếp tục tăng.
- **Cạnh tranh:** các công ty đám mây lớn cung cấp GPU ở quy mô khổng lồ với dịch vụ hỗ trợ mà mạng phi tập trung khó sánh kịp.
- **Phụ thuộc:** mạng dựa nhiều vào phần mềm của OTOY và blockchain Solana, nên sự cố ở bên nào cũng sẽ ảnh hưởng đến nó.
- **Pháp lý:** quy định về crypto khác nhau giữa các nước và có thể thay đổi nhanh, kể cả cách phân loại những token như RENDER.

## Ý nghĩa nếu bạn mua định kỳ

Giá RENDER từng tăng vọt và lao dốc sâu, và biến động theo tâm lý xoay quanh AI. Mua một khoản cố định đều đặn nghĩa là bạn mua được nhiều hơn khi giá thấp và ít hơn khi giá cao, không cần đoán đáy — nhưng rủi ro thua lỗ vẫn còn. Nhiều người chỉ giữ những token như RENDER ở một phần nhỏ tiền tiết kiệm mà họ chịu được nếu giảm mạnh. Kết quả trong quá khứ không đảm bảo lợi nhuận trong tương lai.

*Không phải lời khuyên đầu tư.*

## Nguồn

- [Render Network — official site (rendernetwork.com)](https://rendernetwork.com/)
- [Render Network Knowledge Base: history and Burn Mint Equilibrium (know.rendernetwork.com)](https://know.rendernetwork.com/basics/burn-mint-equilibrium)
- [RNP-001: Burn-and-Mint Equilibrium (Render Network proposals, GitHub)](https://github.com/rendernetwork/RNPs/blob/main/RNP-001.md)
- [Render price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/render-token)
