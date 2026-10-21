# Quy trình sản xuất video AI theo cảnh

## Mục tiêu đã được người dùng yêu cầu
Viết prompt tổng thể để tạo kịch bản và chỉ dẫn hình ảnh; tạo ảnh tham chiếu người dẫn, sản phẩm, bối cảnh nhất quán; tạo video từ ảnh; tạo thuyết minh tiếng Việt và lip-sync; dựng tự động thành video dọc cho Reels/TikTok. Kết hợp footage thật với avatar theo hybrid-presenter.md. Đây là quy trình sản xuất mong muốn, không phải bằng chứng về công nghệ của mẫu review.

## 1. Brief và prompt tổng thể
Dùng templates/master-prompt.md. Thu thập sản phẩm, đối tượng xem, vấn đề, lợi ích có căn cứ, CTA, footage, ảnh gốc, thời lượng và nền tảng. Ghi rõ phần chưa xác minh. Mô tả phong cách bằng hành vi cụ thể thay vì chỉ nói “chuyên nghiệp”: chữ đổi theo ý, minh họa diễn giải lời, người dẫn và B-roll xen kẽ có lý do.

Tạo danh sách cảnh trước: mỗi cảnh một mục đích, một hành động chính, lời vừa thời lượng. Cấu trúc mở đầu → vấn đề → lợi ích/minh họa → kết không phải khuôn bắt buộc; chọn theo brief. Không dùng lời chứng thực cá nhân nếu không có nguồn trải nghiệm thật.

## 2. Khóa tham chiếu
Tạo một bảng tham chiếu dùng xuyên suốt, gồm:
- Nhân vật: ID, ảnh được phép dùng, các đặc điểm cần giữ, tóc, trang phục, phụ kiện, giọng và cách xưng hô.
- Sản phẩm: ID, ảnh gốc nhiều góc nếu có, tên, logo, màu, tỷ lệ, chi tiết bao bì và thông tin được xác minh.
- Bối cảnh: ID, bố cục, vị trí đồ vật, hướng sáng, nhiệt độ màu và bảng màu.

Với người dùng xuất hiện trong footage, lấy người thật làm nguồn nhất quán; không tự thay bằng nhân vật khác. Ưu tiên ảnh gốc sản phẩm, cắt ghép hoặc đặt ảnh vào bố cục trước khi tái tạo bao bì bằng AI. Nếu chỉ thấy ảnh trong chat mà không truy cập được file, báo thiếu tài nguyên; không tự thay bằng ảnh AI rồi coi là ảnh gốc.

Khi công cụ hỗ trợ, truyền lại cùng ảnh tham chiếu và ID qua từng cảnh. Seed chỉ giúp tái lập một phần, không bảo đảm danh tính. Kiểm tra ảnh đầu ra cạnh nguồn: khuôn mặt, tóc, quần áo, logo, số lượng và hình dáng sản phẩm. Chọn ảnh đạt làm đầu vào video, không dùng ảnh lỗi để đi tiếp.

## 3. Viết và tạo từng cảnh
Dùng templates/scene-prompt.md. Tách prompt hình tĩnh (ai, vật gì, ở đâu, bố cục) khỏi prompt chuyển động (hành động, camera, nhịp, trạng thái đầu/cuối). Mỗi clip ưu tiên một hành động dễ kiểm soát. Thời lượng theo khả năng thật của engine; không mặc định mọi công cụ nhận cùng tham số.

Ưu tiên image-to-video với ảnh tham chiếu cho cảnh cần giữ danh tính/bao bì. Chỉ dùng first/last frame, nhiều ảnh, seed hoặc negative prompt nếu engine có hỗ trợ. Không nhét chữ quảng cáo vào ảnh/video sinh nếu có thể chèn chữ chính xác ở hậu kỳ.

Ghi model/version, prompt, tham chiếu, tham số, job ID và đường dẫn đầu ra ngoài Git khi chứa dữ liệu riêng. Poll job hiện có; không gửi lại tác vụ tính phí chỉ vì timeout. Kiểm tra từng clip trước khi ghép: không đổi mặt, biến dạng tay, sản phẩm biến hình hoặc nhãn sai. Sửa cảnh lỗi, không che lỗi bằng chữ.

## 4. Giọng Việt và khẩu hình
- Footage thật: giữ audio gốc ở các câu được chọn, không để audio gốc và TTS phát chồng.
- Lời mới: người dùng đã yêu cầu quy trình thuyết minh tiếng Việt bằng AI; chọn giọng được cấp phép phù hợp brief. Điều này không tự cho phép nhân bản giọng của người dùng.
- Nếu brief hiện tại yêu cầu “giữ giọng thật”, không tự thay lời thiếu bằng TTS: cần bản thu bổ sung hoặc lựa chọn rõ ràng từ người dùng.
- Chuẩn hóa cách đọc số, đơn vị, thương hiệu và tên riêng trong bản dành cho TTS; giữ chính tả chuẩn trong caption.
- Tạo audio trước, đo thời lượng thật và nghe kiểm tra, rồi điều chỉnh nhịp cảnh. Không ép lời dài vào clip ngắn bằng tăng tốc quá mức.
- Gửi audio đã chốt vào engine avatar/lip-sync phù hợp. Với cảnh không thấy miệng, không cần lip-sync.
- Kiểm tra tiếng Việt, nhịp nghỉ, cảm xúc, sự liên tục giọng, miệng/răng và đồng bộ đầu-cuối câu. Không coi waveform hoặc transcript là thay thế nghe trực tiếp.

## 5. Dựng tự động
Dựng theo một manifest cảnh duy nhất: thứ tự, clip, khoảng cắt, audio, từ khóa, caption và transition. Ghép bằng công cụ thực sự khả dụng, chẳng hạn HyperFrames/Remotion cho motion graphics và FFmpeg cho encode/kiểm tra. Các công cụ này không mặc định cung cấp avatar, TTS hoặc image-to-video.

Chốt audio rồi lấy timestamp từ audio cuối để căn caption; không suy thời gian chỉ theo số từ. Chữ nhấn hai tầng phải bám đúng ý, không chỉ lặp tên sản phẩm. Xen người dẫn, cảnh công dụng và sơ đồ theo nội dung. Chuyển cảnh phù hợp nhịp, không mặc định thêm cùng một hiệu ứng cho mọi chỗ cắt.

Nhạc/SFX có nguồn được phép dùng; hạ nhạc dưới lời, kiểm tra clipping và độ rõ giọng. Không lấy việc đủ giây làm tiêu chí chính. Nếu thiếu footage/audio/công cụ cho cảnh bắt buộc, báo phần thiếu và tiếp tục phần độc lập; không thay bằng slideshow kéo dài rồi gọi là đạt mẫu.

## 6. Xuất và nghiệm thu
Mặc định đề xuất 9:16, 1080 × 1920, 30 fps, H.264/AAC MP4; điều chỉnh theo nguồn, brief và yêu cầu nền tảng hiện hành. Không nói upscale làm tăng chi tiết gốc. Vùng an toàn phải kiểm tra với bố cục đăng thực tế.

Kiểm tra đủ cảnh, đúng thời lượng, không mất tiếng, caption đúng, hình/giọng nhất quán, không có UI bản quay màn hình. Xem/nghe đầu ra và so với mục tiêu phong cách; giải mã thành công chỉ chứng minh file hợp lệ. Bàn giao MP4, project/manifest và ghi rõ cảnh AI, giọng tổng hợp, hạn chế còn lại.

## Trạng thái công cụ
Quy trình này là hướng dẫn tái sử dụng, không phải engine đã cài. Tạo ảnh, I2V, TTS, avatar/lip-sync, transcription và dựng là các khả năng độc lập: kiểm tra từng khả năng trong phiên hiện tại. HeyGen hiện chỉ có checker và cấu hình nháp, chưa xác minh generation. Không tự mua gói, nạp tiền hoặc tuyên bố hệ thống hoạt động trọn chuỗi khi chưa kiểm thử thực tế.
