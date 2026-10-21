# Mẫu chỉ dẫn từng cảnh

## Danh tính và mục đích
- scene_id: [S01]
- Thời lượng dự kiến: [giây; chốt theo audio]
- Loại: [footage thật / avatar / I2V sản phẩm / motion graphics]
- Mục đích: [một ý]
- Tham chiếu: [presenter_id, product_id, setting_id, các file truy cập được]

## Prompt hình tĩnh
[Người/vật chính] tại [bối cảnh], [trang phục, tư thế và vị trí sản phẩm]. Khung hình [cỡ cảnh, góc, bố cục dọc], ánh sáng [hướng và sắc độ]. Giữ nguyên [đặc điểm nhân vật, nhãn, hình dạng, màu sản phẩm] theo tham chiếu. Chừa [vùng chữ] nhưng không tạo chữ quảng cáo trong ảnh. Chỉ mô tả chi tiết có căn cứ hoặc thiết kế được phép.

## Prompt image-to-video
Từ ảnh tham chiếu [ID], [một hành động chính]. Camera [đứng yên hoặc một chuyển động cụ thể]. Bắt đầu [trạng thái], kết thúc [trạng thái nối cảnh]. Chuyển động [nhịp và mức độ]. Giữ [danh tính, trang phục, hình dạng và nhãn sản phẩm, ánh sáng]. Không biến hình sản phẩm hoặc thêm vật thể không yêu cầu. Chuyển các giới hạn sang tham số/negative prompt chỉ khi engine hỗ trợ.

## Audio và lip-sync
- Nội dung lời chính xác: [lời]
- Nguồn: [file thật / TTS và voice ID được phép]
- Cách đọc: [từ thương hiệu, đơn vị, tên riêng]
- Miệng có thấy trong cảnh không: [có/không]
- Clip/audio cho lip-sync: [đường dẫn sau khi tạo]

## Hậu kỳ
- Dòng dẫn / từ khóa: [nội dung]
- Caption: [tạo timestamp từ audio cuối]
- Đồ họa công dụng: [hành động cần giải thích, không chỉ icon trang trí]
- Điểm chuyển cảnh: [cuối ý hoặc hành động]

## Kiểm tra trước khi sử dụng
So sánh với tham chiếu; xem đầu/giữa/cuối clip và chuyển động liên tục; nghe lời, kiểm tra miệng/tay/sản phẩm/chữ. Lưu lỗi cần sửa, job ID và phiên bản đầu ra. Không ghi API key hoặc URL có chữ ký vào tài liệu công khai.
