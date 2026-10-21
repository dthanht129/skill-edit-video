# skill-edit-video

Lưu trữ skill và tài nguyên dựng video theo phong cách cá nhân của Trúc Đoàn.

## Bộ skill hiện có

[truc-doan-video](.agents/skills/truc-doan-video/SKILL.md): hướng dẫn dựng review sản phẩm với người dẫn, chữ nhấn hai tầng và đồ họa giải thích, dựa trên mẫu review.mp4 do người dùng cung cấp.

- [Phong cách](.agents/skills/truc-doan-video/references/style-guide.md)
- [Phân tích video mẫu](.agents/skills/truc-doan-video/references/review-breakdown.md)
- [Quy trình sản xuất](.agents/skills/truc-doan-video/references/production-workflow.md)
- [Kiểm tra chất lượng](.agents/skills/truc-doan-video/references/quality-checks.md)

## Sử dụng trong Codex

1. Mở tác vụ với repository này được checkout và truy cập được.
2. AGENTS.md hướng dẫn agent đọc skill khi làm video; client hỗ trợ có thể tự khám phá `.agents/skills`.
3. Ví dụ yêu cầu: “Dùng skill truc-doan-video, dựng review từ footage tôi gửi; ưu tiên phong cách mẫu review.”
4. Kiểm tra ở phiên mới: “Cho biết phong cách video mặc định và những file bạn đã đọc.”

Để lưu sở thích lâu dài, yêu cầu rõ “Áp dụng cho các video sau và lưu vào bộ skill”. Thay đổi phải được commit/push để có trên GitHub. Đây là bộ nhớ bằng file trong repository, không phải bộ nhớ toàn cục của mọi cuộc chat.

## Trạng thái

Đã có hướng dẫn và tài liệu tham chiếu. Chưa có renderer, template chạy được, font/icon hoặc video mẫu trong Git. Không cần cài dependencies để sử dụng phần hướng dẫn. Khi thêm công cụ dựng, phải bổ sung manifest, lockfile và lệnh cài/render đã kiểm chứng. Publication của môi trường Codex là bước riêng trong giao diện, không xảy ra khi push Git.

## Kết nối avatar/lip-sync
Xem [hướng dẫn HeyGen và trạng thái tích hợp](integrations/heygen/README.md). Đã có checker chỉ đọc; chưa kiểm chứng generation trên dịch vụ thật.

## Quy trình AI từ brief đến video
- [Quy trình sản xuất](.agents/skills/truc-doan-video/references/ai-production-pipeline.md)
- [Prompt tổng thể để điền brief](.agents/skills/truc-doan-video/templates/master-prompt.md)
- [Prompt hình ảnh/chuyển động từng cảnh](.agents/skills/truc-doan-video/templates/scene-prompt.md)

Bao gồm ảnh tham chiếu nhất quán, I2V, tiếng Việt, lip-sync và dựng tự động. Đây là hướng dẫn; khả năng chạy từng bước phụ thuộc công cụ kết nối thực tế.
