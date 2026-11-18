# Nội dung TikTok: quy trình và quy tắc chung

## Quy trình

1. Claude viết prompt, gồm ảnh khung đầu và video cho từng clip, kèm file kế hoạch dựng `.plan.txt` (chữ móc câu, mốc thời gian, phụ đề, dòng chữ kết).
2. Bạn tạo ảnh bằng phần mềm ảnh, tạo video bằng Muse, đặt tên file theo hướng dẫn rồi gửi link Google Drive.
3. Claude dựng bằng `tools/tiktok.py`: 1080×1920, 30fps, −14 LUFS, phụ đề chèn cứng, chữ nằm trong vùng an toàn, xuất kèm ảnh bìa.

## Độ dài video: linh hoạt từ 30 đến 60 giây

Mỗi clip Muse dài 10 giây. Số clip được chọn theo lượng nội dung cần kể, không kéo dài cho đủ thời lượng:

| Độ dài | Số clip | Dùng khi |
|---|---|---|
| **30 giây** | 3 | Một tình huống, một cú chốt: truyền thuyết ngắn, mẩu hài, ký ức. Đây là mặc định. |
| **40 giây** | 4 | Cần thêm một nhịp đẩy trước cao trào: sự kiện có diễn biến, hoặc có hai nhân vật đối đáp. |
| **50 giây** | 5 | Câu chuyện có nhiều mốc thời gian (một ngày, nhiều đời người, nhiều năm), hoặc trận đánh có diễn biến rõ. |
| **60 giây** | 6 | Truyền thuyết có nhiều khúc (gặp gỡ, biến cố, kết cục), xem `truyen-dai/`. |

Nhịp chung:
- **Clip 1** dựng tình huống. Phải có chuyển động ngay giây 0, vì chữ móc câu chỉ hiện trong 2,5 giây đầu.
- **Các clip giữa** đẩy câu chuyện lên. Mỗi clip có một thông tin mới hoặc một câu thoại đáng nhớ.
- **Clip cuối** là cú chốt: câu thoại bất ngờ hoặc tên gọi nổi tiếng. Dòng chữ lịch sử hiện ở 3 giây cuối.

Với video dài hơn 30 giây, phải có lý do để người xem ở lại:
- Ở khoảng giây 15–20 cần một "móc giữa", như câu hỏi, chi tiết lạ hay tình huống trớ trêu, để người xem không lướt đi.
- Không có hai clip liền nhau chỉ toàn cảnh, không có thoại hay hành động mới.

Ghi chú cho TikTok: video từ 30 giây trở lên đều được tính là nội dung dài. Tỉ lệ xem hết vẫn là yếu tố quan trọng nhất, nên một video 30 giây chặt chẽ luôn tốt hơn một video 50 giây bị loãng.

## Một nội dung, hai bản: YouTube Shorts và TikTok

Với các tập dài 50–60 giây, **cùng một bộ clip Muse** sẽ được dựng ra hai video:

| Bản | Độ dài | Cách dựng | Lời kêu gọi cuối video |
|---|---|---|---|
| **YouTube Shorts** | 50–60 giây | Đủ tất cả clip | "Đăng ký để xem…" |
| **TikTok** | 30–40 giây | Bỏ bớt hoặc chỉ lấy nửa clip theo đánh dấu `tiktok=` | "Follow để xem…" |

- Bạn **không phải tạo thêm clip nào**. Mỗi file tập ghi rõ ở từng clip: bản TikTok giữ cả clip, chỉ lấy giây 0–5 hoặc 5–10, hay bỏ clip đó.
- Quy tắc cắt: luôn giữ clip mở đầu (câu móc), clip "móc giữa" và clip chốt cuối. Các clip còn lại chỉ giữ nửa có câu thoại hay nhất, hoặc bỏ.
- Phụ đề tự cắt và dời theo. Câu nào bị cắt gần hết (còn dưới 0,8 giây) sẽ tự ẩn.
- Lệnh `python3 ../tools/tiktok.py <plan> <tên>.mp4` sẽ ra `<tên>-youtube.mp4`, `<tên>-tiktok.mp4` và ảnh bìa cho từng bản.
- Mỗi file tập có thêm mục **"Đăng YouTube Shorts"** gồm tiêu đề kèm `#Shorts` và mô tả soạn sẵn. YouTube yêu cầu khai báo nội dung do AI tạo ở mục "Nội dung bị thay đổi" (Altered content).
- Các tập 30–40 giây (loạt Thăng Long, POV 30 giây, Bạch Đằng phần 1–2…) quá ngắn cho chuẩn YouTube 50–60 giây, nên vẫn chỉ dựng một bản.

## An toàn trẻ em (bắt buộc)

TikTok siết mục **An toàn cho trẻ vị thành niên** gắt nhất, đặc biệt với video AI có người trông như thật. Tập A3 cũ ("Vợ lính Ngô Quyền", có em bé khóc trong bối cảnh chiến tranh) đã bị gắn cờ vì lý do này. Từ giờ, mọi tập áp dụng:

- **Không để trẻ em lộ mặt hoặc cận cảnh.** Nếu truyện bắt buộc có trẻ em (Thánh Gióng, Nguyễn Hiền), chỉ quay từ phía sau, ở xa, hoặc chỉ thấy bàn tay.
- **Không có trẻ em khóc, sợ hãi, bị thương hay ở gần cảnh chiến tranh.** Không dùng đồ chơi trẻ em để ám chỉ thương vong.
- **Nhân vật có thật còn nhỏ tuổi** (Trần Quốc Toản 15 tuổi) được dựng với ngoại hình thanh niên, và không dùng câu thoại kiểu "cả đội toàn trẻ con" trong bối cảnh ra trận.
- **Cảm xúc gia đình thời chiến** dựng bằng người lớn: vợ, mẹ, ông bà, hàng xóm.
- Khối mô tả chung trong `tools/series.py` đã có sẵn câu chặn trẻ em cận mặt và đau buồn, nên mọi prompt sinh ra đều mang câu này.

**Nếu một video bị gắn cờ:** mở video, bấm vào dòng cảnh báo "Vi phạm Nguyên tắc Cộng đồng" để xem mục bị ghi. Nếu là mục an toàn trẻ em, thường nên **xóa video thay vì kháng nghị**, nhất là video có ít lượt xem, để tránh ảnh hưởng tới việc đề xuất của cả kênh.

## Chất hài

Mỗi tập cần ít nhất **2 điểm cười**, và câu cuối phải là một câu chốt bất ngờ. Các kỹ thuật dùng được:

- **Chen từ hiện đại vào bối cảnh xưa:** KPI, chung cư, "mốt mới", "khách thuê"…
- **Gọi lại chi tiết cũ:** con gà của ông Ba, chuyện đắp thành ba lần, nhà ông Ba đời nào cũng cằn nhằn.
- **Phản ứng tỉnh bơ trước chuyện lớn:** "Đông thế thì nấu cơm chắc mệt lắm."
- **Bào chữa vụng về khi bị bắt quả tang:** "Dạ, đây là bùa may mắn ạ!", "Đây là… mốt mới!"
- **Đối đáp chốt hạ:** "Lần thứ mười hai rồi ạ." / "Thì lần thứ mười ba."

Giới hạn:
- Không đùa cợt anh hùng dân tộc, lời thề hay thơ thiêng (Hai Bà Trưng, "Nam quốc sơn hà", Điện Biên). Tiếng cười đặt vào nhân vật phụ.
- Không lấy dân tộc thiểu số hay cảnh nghèo khó làm trò cười.

## Thông tin đăng (có sẵn trong file .md của mỗi tập)

Mỗi tập có hai mục "Đăng TikTok" và "Đăng YouTube Shorts" để copy dán thẳng lúc đăng:

- **TikTok:** hook (chữ trên ảnh bìa), hook dự phòng, tiêu đề, mô tả kèm hashtag, bình luận ghim.
- **YouTube:** tiêu đề (có #Shorts), mô tả (thêm dòng ghi video do AI tạo, nhân vật hư cấu), thẻ (ô Tags, không có dấu #, viết có dấu), bình luận ghim (đổi "Follow" thành "Đăng ký").
- **Tiêu đề và hook dự phòng không được lộ cú lật ở cuối.**
- **Bình luận ghim là một câu hỏi hoặc gợi ý, không trả lời luôn câu hỏi ở caption**, để người xem tự bình luận. Đáp án thì trả lời bằng video sau.
- Khai báo trong `_nguon.py` bằng các khóa `tt_title`, `hooks_alt`, `pin`, `yt_title`, `yt_tags`, `yt_pin`. Tập không khai báo thì `tools/series.py` tự điền mặc định.

## Quy ước cố định

- Khung dọc 9:16. Giữ chủ thể ở giữa khung. Không để Muse tự chèn chữ.
- Khối `[POV]` và `[Âm thanh]` dùng chung, nằm ở đầu `pov-30s/prompts.md`.
- Mỗi tập có caption đăng bài kết bằng câu hỏi, kèm 7–9 hashtag chia ba nhóm: hashtag lớn (`#xuhuong #fyp`), hashtag của kênh (`#povlichsu #POV #lichsuvietnam`) và hashtag theo chủ đề.
- Dòng chữ kết luôn **kết lửng**: một câu hỏi bỏ ngỏ, kèm "Follow để xem mai bạn làm [vai của tập sau] →". Giải thích lịch sử đặt ở caption. Chi tiết, thứ tự đăng và kịch bản trả lời bình luận xem ở `tang-follow.md`.
- Loạt nhiều phần dùng hashtag riêng (ví dụ `#thanglongnghinnam`) và có số phần trong chữ móc câu.
- Luôn bật nhãn "Nội dung do AI tạo" khi đăng.
- Khi chạy thử script, chỉ dùng clip nền đơn sắc nhỏ tự tạo và xóa ngay sau khi kiểm tra.
