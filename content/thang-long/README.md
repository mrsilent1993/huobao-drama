# Thăng Long nghìn năm: loạt ông Ba

Loạt POV hài lịch sử về Thăng Long, nối tiếp tập **"POV: Bạn là dân Hoa Lư ngày dời đô năm 1010"** (phần 1, đã đăng, hơn 10 nghìn lượt xem trong 12 giờ). Nhân vật xuyên suốt là **ông Ba**: khó tính, hay cằn nhằn, nốt ruồi má trái. Từ phần 4, con cháu ông xuất hiện, đời nào cũng giống ông như đúc.

Mỗi phần dài 30 giây, gồm 3 clip Muse 10 giây, khung dọc 9:16.

## Các phần

| Phần | File | Nội dung | Câu chốt |
|---|---|---|---|
| 1 | (đã đăng) | Dời đô từ Hoa Lư, rồng vàng bay lên | "Đất rộng, bằng phẳng, lại cao ráo… thôi, ở luôn!" |
| 2 | `phan-2.md` | Xây thành sụt ba lần, ngựa trắng hiện ra | "Thế công đắp ba lần trước ai trả?" |
| 3 | `phan-3.md` | Chùa Một Cột, năm 1049 | "Mai vua mơ thấy cái nồi thì xây nhà hình cái nồi à?" |
| 4 | `phan-4.md` | Khoa thi đầu tiên, năm 1075 | "Đắp thành ba lần còn được, thi ba lần sợ gì!" |
| 5 | `phan-5.md` | Chuông Quy Điền đánh không kêu, năm 1101 | "Thôi… ít ra cũng có khách thuê." |
| 6 | `phan-6.md` | Thăng Long đổi tên, 1397 đến 1831 | "Đổi nữa là tôi về lại Hoa Lư đấy!" |

Mỗi file `phan-N.md` có đủ:
- Prompt ảnh khung đầu và prompt video cho từng clip, đã ghép sẵn, copy dán thẳng.
- Tên file cần đặt cho từng clip.
- Caption và hashtag để đăng.
- Phần chữ mình sẽ chèn lên video.

## Bước 0: tạo ảnh chân dung ông Ba (làm một lần, dùng cả loạt)

Tạo ảnh này bằng phần mềm ảnh, rồi dùng làm **ảnh tham chiếu nhân vật** trong Muse cho mọi clip có ông Ba hoặc con cháu ông. Đây là cách tốt nhất để ông Ba không bị đổi mặt giữa các phần.

```
Portrait photo of a grumpy Vietnamese man about 50 years old with a round face, thick eyebrows, short cropped hair, a sparse moustache, black-lacquered teeth showing slightly, a big mole on his left cheek, frowning with arms crossed, wearing a simple brown homespun shirt, ancient Vietnamese village background softly blurred, realistic, natural light, head and shoulders, vertical 9:16.
```

Muốn ông Ba già ở phần 3 thì tạo thêm một bản, thêm vào prompt: `aged 85, white hair, deep wrinkles, leaning on a wooden cane`.

## Lịch đăng

- Mỗi ngày 1 phần, theo thứ tự 2 → 3 → 4 → 5 → 6, cùng khung giờ đã đăng phần 1.
- Dòng chữ kết mỗi phần là câu hỏi bỏ lửng, kèm lời mời follow để xem phần sau. Vì vậy cần đăng đúng thứ tự, liên tục.
- Phần 6 kết bằng **"Comment 'phần 7' nếu muốn xem tiếp"**. Nếu nhiều người bình luận, mình sẽ viết tiếp loạt này.
- Hashtag riêng của loạt là `#thanglongnghinnam`, dùng ở mọi phần, kể cả phần 1 nếu sửa được caption.
- Nếu tài khoản có tính năng **Danh sách phát (Playlist)**, hãy gom cả 6 phần vào danh sách "Thăng Long nghìn năm".
- Ghim một bình luận ở phần 1: "Phần 2 đã lên, xem ở trang cá nhân nhé 👆".

## Trả lời bình luận bằng video trong vai ông Ba

Có 3 kịch bản viết sẵn trong `../tang-follow.md`:
- **B:** "Chiếu dời đô khen đất thế nào?"
- **C:** "Ông Ba khó tính quá"
- **D:** "Rồng vàng có thật không?"

Có bình luận nào hay ở phần 1, bạn chụp màn hình gửi mình, mình viết thêm kịch bản trả lời đúng giọng ông Ba.

## Gửi clip cho mình dựng

1. Đặt tên file đúng như trong từng `phan-N.md` (`tl2-1.mp4` … `tl6-3.mp4`).
2. Gửi link Google Drive. Có thể gửi từng phần một, không cần chờ đủ cả loạt.
3. Mình dựng bằng lệnh `python3 ../tools/tiktok.py phan-N.plan.txt phan-N.mp4`, gửi lại video và ảnh bìa, rồi xóa clip gốc trong phiên.
