# Nội dung TikTok: quy trình và quy tắc chung

## Quy trình

1. Claude viết prompt, gồm ảnh khung đầu và video cho từng clip, kèm file kế hoạch dựng `.plan.txt` (chữ móc câu, mốc thời gian, phụ đề, dòng chữ kết).
2. Bạn tạo ảnh bằng phần mềm ảnh, tạo video bằng Muse, đặt tên file theo hướng dẫn rồi gửi link Google Drive.
3. Claude dựng bằng `tools/tiktok.py`: 1080×1920, 30fps, −14 LUFS, phụ đề chèn cứng, chữ nằm trong vùng an toàn, xuất kèm ảnh bìa.

## Độ dài video: linh hoạt từ 30 đến 50 giây

Mỗi clip Muse dài 10 giây. Số clip được chọn theo lượng nội dung cần kể, không kéo dài cho đủ thời lượng:

| Độ dài | Số clip | Dùng khi |
|---|---|---|
| **30 giây** | 3 | Một tình huống, một cú chốt: truyền thuyết ngắn, mẩu hài, ký ức. Đây là mặc định. |
| **40 giây** | 4 | Cần thêm một nhịp đẩy trước cao trào: sự kiện có diễn biến, hoặc có hai nhân vật đối đáp. |
| **50 giây** | 5 | Câu chuyện có nhiều mốc thời gian (một ngày, nhiều đời người, nhiều năm), hoặc trận đánh có diễn biến rõ. |

Nhịp chung:
- **Clip 1** dựng tình huống. Phải có chuyển động ngay giây 0, vì chữ móc câu chỉ hiện trong 2,5 giây đầu.
- **Các clip giữa** đẩy câu chuyện lên. Mỗi clip có một thông tin mới hoặc một câu thoại đáng nhớ.
- **Clip cuối** là cú chốt: câu thoại bất ngờ hoặc tên gọi nổi tiếng. Dòng chữ lịch sử hiện ở 3 giây cuối.

Với video dài hơn 30 giây, phải có lý do để người xem ở lại:
- Ở khoảng giây 15–20 cần một "móc giữa", như câu hỏi, chi tiết lạ hay tình huống trớ trêu, để người xem không lướt đi.
- Không có hai clip liền nhau chỉ toàn cảnh, không có thoại hay hành động mới.

Ghi chú cho TikTok: video từ 30 giây trở lên đều được tính là nội dung dài. Tỉ lệ xem hết vẫn là yếu tố quan trọng nhất, nên một video 30 giây chặt chẽ luôn tốt hơn một video 50 giây bị loãng.

## Quy ước cố định

- Khung dọc 9:16. Giữ chủ thể ở giữa khung. Không để Muse tự chèn chữ.
- Khối `[POV]` và `[Âm thanh]` dùng chung, nằm ở đầu `pov-30s/prompts.md`.
- Mỗi tập có caption đăng bài kết bằng câu hỏi, kèm 7–9 hashtag chia ba nhóm: hashtag lớn (`#xuhuong #fyp`), hashtag của kênh (`#povlichsu #POV #lichsuvietnam`) và hashtag theo chủ đề.
- Dòng chữ kết luôn **kết lửng**: một câu hỏi bỏ ngỏ, kèm "Follow để xem mai bạn làm [vai của tập sau] →". Giải thích lịch sử đặt ở caption. Chi tiết, thứ tự đăng, kịch bản trả lời bình luận và khung livestream xem ở `tang-follow.md`.
- Loạt nhiều phần dùng hashtag riêng (ví dụ `#thanglongnghinnam`) và có số phần trong chữ móc câu.
- Luôn bật nhãn "Nội dung do AI tạo" khi đăng.
- Khi chạy thử script, chỉ dùng clip nền đơn sắc nhỏ tự tạo và xóa ngay sau khi kiểm tra.
