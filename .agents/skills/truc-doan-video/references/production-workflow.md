# Quy trình sản xuất và tài nguyên

## Trạng thái hiện tại
Repository chứa hướng dẫn và phân tích tham chiếu. Chưa có renderer, package manifest, font, icon, template chạy được hoặc footage được quản lý trong Git. Không chạy npm install hay lệnh render giả định khi các file này chưa tồn tại.

## Chuẩn bị một video
1. Xác định đầu ra, nguồn footage, lời thoại và thông số có căn cứ.
2. Đọc hybrid-presenter.md. Lập bảng: start/end | cảnh thật/avatar/minh họa | lời thoại | nguồn audio | dòng dẫn | từ khóa | minh họa | nguồn thông số.
3. Chọn bộ công cụ phù hợp với dự án. Nếu xây bằng Remotion hoặc HyperFrames, dùng skill tương ứng đang khả dụng và tài liệu chính thức.
4. Với template mới, kiểm chứng hệ chữ, vùng an toàn và một sơ đồ trên đoạn đại diện trước khi nhân rộng.
5. Kiểm tra đầu ra theo quality-checks.md.

## Tài nguyên cần bổ sung khi phát triển template
- Font có giấy phép phù hợp và hỗ trợ dấu tiếng Việt.
- Icon/SVG có quyền sử dụng và ghi nhận nguồn khi cần.
- Component chữ hai tầng, bố cục người dẫn + sơ đồ, đồ họa toàn cảnh.
- Các module cơ chế theo từng sản phẩm, không mặc định sao chép từ mẫu.
- Manifest và lockfile, lệnh cài đặt/render đã thử, phiên bản runtime.

Không tự tải lại nội dung từ tài khoản mạng xã hội của người khác hoặc đưa footage cá nhân lên Git. Tài nguyên dung lượng lớn nên dùng kho lưu trữ được người dùng chọn; lưu đường dẫn và mô tả không chứa bí mật.

## Dùng lại ở phiên mới
Mở tác vụ có repository này. Agent đọc AGENTS.md rồi skill. Cơ chế tự khám phá `.agents/skills` phụ thuộc client; AGENTS.md là chỉ dẫn đọc trực tiếp. Một cuộc chat không có quyền truy cập repository sẽ không tự có bộ tài nguyên này.
