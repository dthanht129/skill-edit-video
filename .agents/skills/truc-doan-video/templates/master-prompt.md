# Mẫu prompt tổng thể

Thay các trường trong ngoặc bằng dữ liệu thật. Trường chưa có phải để “chưa cung cấp”, không bịa.

---
Bạn là biên kịch và đạo diễn dựng video review của tôi. Áp dụng skill truc-doan-video và phong cách đã lưu.

## Brief
- Sản phẩm và ảnh/footage nguồn: [tên, asset ID hoặc đường dẫn truy cập được]
- Khách hàng và vấn đề: [đối tượng, tình huống]
- Công dụng/lợi ích đã xác minh: [nội dung + nguồn]
- Tuyên bố chưa có bằng chứng, không được dùng như sự thật: [danh sách]
- Nền tảng, tỷ lệ, thời lượng: [Reels/TikTok, 9:16, số giây]
- Thông điệp chính và CTA: [nội dung]
- Người dẫn: [tham chiếu người thật, avatar cùng người, phong cách biểu cảm]
- Giọng: [audio thật / bản thu bổ sung / TTS được phép]; phương ngữ, xưng hô, cách đọc thương hiệu: [quy định]
- Bối cảnh và bảng màu: [tham chiếu]
- Công cụ thực sự khả dụng và giới hạn: [liệt kê]

## Chỉ đạo
Kết hợp footage thật, avatar/lip-sync và minh họa theo từng ý. Giữ danh tính người dẫn, sản phẩm và bối cảnh nhất quán. Mỗi cảnh có một mục đích, lời vừa thời lượng và hình minh họa liên quan trực tiếp. Từ khóa lớn trên nền cam đất, dòng dẫn nhỏ, sơ đồ nền tối theo style-guide. Không sao chép thông số sản phẩm từ video mẫu.

## Đầu ra bắt buộc
1. Tóm tắt ý tưởng và thông điệp trong 2–3 câu.
2. Bảng nguồn thông tin: điều đã xác minh, điều cần xác minh, nội dung không sử dụng.
3. Bảng khóa tham chiếu: presenter_id, product_id, setting_id và đặc điểm phải giữ nguyên.
4. Storyboard: scene_id | start/end dự kiến | mục đích | loại cảnh | lời thoại | nguồn audio | hành động/hình | dòng dẫn | từ khóa | transition | asset cần có.
5. Prompt hình tham chiếu và prompt chuyển động riêng cho từng cảnh, dùng scene-prompt.md.
6. Kịch bản thu âm/TTS, chú giải cách đọc tiếng Việt và caption dự kiến. Thời gian caption chỉ chốt sau khi có audio cuối.
7. Danh sách tác vụ tạo tài nguyên/dựng, phụ thuộc và phần đang thiếu công cụ.
8. Tiêu chí nghiệm thu: đúng nội dung, nhất quán, hình/lời/chữ liên kết, khẩu hình và file xuất.

Không coi storyboard là video hoàn chỉnh. Nếu được yêu cầu dựng, tiếp tục tạo và kiểm tra tài nguyên rồi render trong phạm vi công cụ/quyền truy cập có thật.
---
