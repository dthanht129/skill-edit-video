# Phân tích mẫu review.mp4

## Bằng chứng và giới hạn
File được người dùng cung cấp trong hội thoại: 47,1 giây, 720 × 1560, 30 fps, H.264; có audio AAC stereo. Đây là bản quay màn hình có giao diện mạng xã hội, không phải project dựng gốc. Đã xem mẫu khung hình mỗi giây và mẫu dày hơn ở đoạn đầu; chưa nghe trực tiếp âm thanh. Mốc dưới đây xấp xỉ, không phải edit decision list chính xác theo frame. Không xác định được phần mềm, font hay preset gốc.

Không đưa file video vào Git trong lần tạo skill này. Bản phân tích còn dùng được khi file đính kèm không còn truy cập được; muốn đối chiếu chi tiết phải có lại media gốc. Không coi 720 × 1560 là yêu cầu xuất cho video mới.

| Mốc | Nội dung nhìn thấy | Kỹ thuật tham chiếu |
| --- | --- | --- |
| 0–3s | 25.000 Pa, bụi mịn, lông thú cưng | Người dẫn + từ khóa lớn + sơ đồ hút bụi |
| 3–7s | Bột ngũ cốc, đinh nhỏ | Thay cụm chữ, thay cỡ khuôn hình |
| 7–9s | Giẻ lau FlexiArm | Đồ họa góc nhìn xiên, mép tường |
| 9–12s | Vươn ra | Người dẫn + sơ đồ nhỏ giải thích chuyển động |
| 12–20s | Cảm biến vật cản, dây điện, đồ chơi | Đường đi và vật cản minh họa |
| 20–27s | SmartPlan 3.0, từng phòng, AI | Sơ đồ căn hộ và đường đi |
| 27–35s | Chống rối, lông và tóc | Hình con lăn cùng sợi tóc |
| 35–41s | Trải nghiệm, nước sạch/nước bẩn | Người dẫn xen sơ đồ dock |
| 41–47,1s | Giặt giẻ, khí ấm, 45 °C | Nước, luồng khí, chữ nhấn thông số |

Ở đoạn mở đầu, chữ 25.000 Pa có trạng thái chỉ lộ một phần rồi hiện đầy đủ, phù hợp với reveal bằng mask. Không đủ bằng chứng xác định implementation gốc. Không thấy CTA hoàn chỉnh; đoạn kết thúc khi nội dung vẫn đang tiếp diễn.

## Module có thể xây dựng về sau
- suction-particles: bụi và hướng hút.
- edge-mop-extension: giẻ lau vươn ra.
- obstacle-path: robot và đường tránh vật cản.
- room-cleaning-plan: phòng và lộ trình.
- anti-tangle-roller: con lăn và tóc.
- dock-water-airflow: nước và luồng khí.

Đây là danh sách thiết kế, chưa có template chạy được. Có thể tái tạo bằng vector/SVG có phối cảnh và animation 2D; không khẳng định mẫu dùng 3D thật.
