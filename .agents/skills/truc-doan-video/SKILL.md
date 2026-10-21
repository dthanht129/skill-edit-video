---
name: truc-doan-video
description: Dựng và đánh giá video review sản phẩm theo phong cách tham chiếu của Trúc Đoàn; dùng khi người dùng muốn video tương tự mẫu review, chữ nhấn hai tầng và đồ họa giải thích cơ chế.
---

# Video review theo phong cách Trúc Đoàn

## Đọc trước khi làm
- [Phong cách mặc định](references/style-guide.md).
- [Kiểm tra chất lượng](references/quality-checks.md).
- Khi đối chiếu mẫu review: [Phân tích mẫu](references/review-breakdown.md).
- Khi chuẩn bị sản xuất: [Quy trình và tài nguyên](references/production-workflow.md).

## Đầu vào
Xác định sản phẩm, nguồn thông số, footage, lời thoại, thời lượng và nền tảng xuất. Tận dụng thông tin đã có; chỉ hỏi phần thiếu thực sự ngăn tiến độ. Không tự bịa thông số, lời chứng thực hoặc trải nghiệm sử dụng. Không đưa nội dung riêng tư vào repository khi chưa được phép.

## Quy trình
1. Kiểm tra file thực tế và khả năng của công cụ. Phân biệt footage gốc với bản quay màn hình. Không sao chép giao diện nền tảng vào video mới.
2. Chia nội dung thành từng ý: tính năng → ví dụ hoặc cơ chế → lợi ích. Không bắt buộc mỗi video phải có cùng trình tự với mẫu.
3. Lập timeline gồm timecode, lời thoại, cảnh người dẫn/B-roll, dòng dẫn, từ khóa và đồ họa. Nếu chưa có lời thoại hoàn chỉnh, đánh dấu thời gian là dự kiến.
4. Chọn chữ nhấn theo ý nghĩa; áp dụng bố cục hai tầng trong style-guide. Giữ đúng chính tả và dấu tiếng Việt.
5. Chọn hình minh họa phù hợp với sản phẩm. Tách kỹ thuật dùng chung khỏi sơ đồ riêng như robot, con lăn hoặc dock nước.
6. Dùng template đã tồn tại nếu phù hợp. Nếu cần viết renderer, chọn công cụ theo dự án và kỹ năng có sẵn, kiểm tra phiên bản và dependencies trước khi chạy. Remotion là phương án đề xuất, không phải yêu cầu đã được xác nhận.
7. Đồng bộ chữ và hình với lời nói khi có quyền truy cập âm thanh; không tuyên bố đã kiểm tra nghe nếu chỉ đọc transcript hoặc xem waveform.
8. Render đoạn đại diện khi cần đánh giá template mới, rồi kiểm tra và hoàn thiện đầu ra theo yêu cầu. Không dừng ở đoạn demo nếu người dùng đã yêu cầu video hoàn chỉnh và không có bước duyệt bắt buộc.
9. Kiểm tra chất lượng, báo file đầu ra, kiểm tra đã chạy và giới hạn còn lại. Không báo thành công chỉ từ exit code nếu chưa kiểm tra đầu ra.

## Người dẫn kết hợp thật và AI
Người dùng đã yêu cầu kết hợp footage thật với avatar/lip-sync trong cùng video. Đọc [Quy trình người dẫn kết hợp](references/hybrid-presenter.md). Đây là định hướng người dùng yêu cầu, không phải kết luận rằng video mẫu dùng avatar.

## Kết nối dịch vụ avatar
Xem [tích hợp HeyGen](../../../integrations/heygen/README.md) trước khi dùng avatar/lip-sync. Chỉ có checker kết nối; generation chưa được xác minh. Không báo dịch vụ sẵn sàng dựa vào unit test hoặc cấu hình nháp.

## Ghi nhớ có kiểm soát
Khi người dùng xác nhận một quy tắc áp dụng lâu dài, cập nhật style-guide và nêu rõ quy tắc nào đã thay đổi. Phân biệt quan sát từ mẫu, sở thích người dùng đã xác nhận và thông số triển khai đề xuất. Không ghi suy đoán thành sự thật.
