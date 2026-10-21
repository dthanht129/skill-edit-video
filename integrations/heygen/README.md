# Kết nối HeyGen cho người dẫn kết hợp

## Trạng thái thực tế
Đã có công cụ kiểm tra kết nối chỉ đọc, dùng Python 3 chuẩn, không cần cài package. Chưa có công cụ tạo avatar/lip-sync đã được kiểm chứng và chưa có video AI thử thành công. Không coi việc thêm skill hoặc cấu hình nháp là đã cài xong dịch vụ.

Ở lần chuẩn bị này, môi trường chưa có HEYGEN_API_KEY hoặc HEYGEN_AVATAR_ID. Proxy từ chối truy cập api.heygen.com và docs.heygen.com. Đã lưu draft yêu cầu hai domain, secret và mã avatar; draft cần người dùng review/save/publish. Chưa kiểm chứng tài liệu API hiện hành. Checker dùng GET /v2/avatars, xác thực X-Api-Key và cấu trúc data.avatars làm hợp đồng dự kiến cần đối chiếu lại khi truy cập được docs. Nếu loại avatar dùng API khác, phải điều chỉnh theo tài liệu chính thức.

## Người dùng thực hiện bằng tài khoản của mình
1. Đăng nhập https://www.heygen.com/ và kiểm tra quyền API, loại avatar hỗ trợ và hạn mức trước khi mua gói. Không mặc định quyền website bao gồm API.
2. Tạo avatar cá nhân, làm theo yêu cầu video mẫu và bước xác nhận đồng ý của HeyGen. Không giả định footage 16,4 giây đã đủ điều kiện.
3. Trong cài đặt tài khoản HeyGen, tìm mục API/tích hợp theo giao diện hiện hành và tạo API key.
4. Trong cài đặt môi trường Codex, nhập khóa vào secret HEYGEN_API_KEY (đích api.heygen.com). Không dán khóa vào chat, Git, script hay .env được theo dõi.
5. Điền HEYGEN_AVATAR_ID bằng mã avatar có quyền sử dụng API. Đây là mã định danh, không phải API key.
6. Review/save cấu hình mạng và hướng dẫn khởi động đã lưu, rồi publish môi trường. Không cần mua thêm dịch vụ nếu tài khoản hiện tại đã đủ quyền.

## Agent tiếp tục
Đọc AGENTS.md và skill truc-doan-video. Dùng checkout hiện có, không tạo worktree nếu người dùng không yêu cầu.

```bash
python3 integrations/heygen/check_connection.py
python3 -m unittest discover -s integrations/heygen -p 'test_*.py' -v
```

Checker chỉ kiểm tra API danh sách và mã avatar; không tải media, không tạo video và không xác nhận quyền generation hoặc số dư. Mã thoát 2: thiếu cấu hình; 3: lỗi truy cập/schema/không tìm thấy avatar trong danh sách này. Không in response body, khóa hoặc URL ký số. Giữ TLS verification và proxy hiện có; không chuyển credential qua redirect.

Khi có kết nối:
1. Đọc https://docs.heygen.com/ để xác nhận endpoint hiện hành, upload audio, loại avatar, generation, polling và download.
2. Kiểm tra quyền API và thông tin chi phí/hạn mức nếu dịch vụ cung cấp. Không tự mua gói hoặc nạp tiền.
3. Chuẩn bị một cảnh thử ngắn với avatar người dùng và audio thật được phép dùng. Với câu nói mới cần bản thu mới hoặc lựa chọn giọng tổng hợp rõ ràng; không tự nhân bản giọng từ yêu cầu lip-sync.
4. Tích hợp tạo tác vụ, lưu job ID ngoài Git để tiếp tục polling, xử lý failed/completed/timeout. Không tự gửi lại POST khi timeout không rõ đã tạo job hay chưa.
5. Chỉ thêm domain upload/download cụ thể khi tài liệu hoặc kết quả API yêu cầu; không cấp API key cho CDN hoặc domain tải video.
6. Tải kết quả, kiểm tra file và nghe/xem khẩu hình, danh tính, tiếng Việt, sản phẩm. Chỉ lúc này báo công cụ avatar/lip-sync hoạt động.

## Kiểm tra đã thực hiện
Các unit test dùng response giả: thiếu khóa, schema thay đổi, avatar khớp/thiếu, che dữ liệu trong lỗi và từ chối redirect. Chúng không thay thế kiểm tra dịch vụ thật. Lệnh checker trong môi trường hiện tại báo missing_api_key đúng dự kiến; generation chưa chạy.
