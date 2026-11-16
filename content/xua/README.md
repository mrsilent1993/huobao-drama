# Việt Nam thời xưa: loạt POV đa chủ đề

6 tập, mỗi tập một mảng khác nhau của Việt Nam thời xưa. Định dạng POV góc nhìn thứ nhất, hài, dài 30–50 giây tùy truyện. Mỗi file `tap-N-*.md` có đủ: prompt ảnh khung đầu, prompt video đã ghép sẵn (copy dán thẳng), tên file cần đặt, caption kèm hashtag, và phần chữ mình sẽ chèn lên video.

| Tập | Chủ đề | Mảng | Độ dài | Tên file Muse |
|---|---|---|---|---|
| 1 | Bạn chơi của Trạng nguyên 13 tuổi (Nguyễn Hiền, 1247) | Thần đồng | 30 giây | `nh-1..3.mp4` |
| 2 | Đi sứ cùng Mạc Đĩnh Chi (1308) | Ngoại giao, câu đối | 40 giây | `mdc-1..4.mp4` |
| 3 | Gia nhân phủ chúa và món "mầm đá" (Trạng Quỳnh) | Truyện tiếu lâm | 50 giây | `tq-1..5.mp4` |
| 4 | Học trò của Hải Thượng Lãn Ông (1781) | Nghề y, y đức | 40 giây | `lo-1..4.mp4` |
| 5 | Hầu bếp cho vua Tự Đức (Huế) | Cung đình, ẩm thực | 30 giây | `nt-1..3.mp4` |
| 6 | Đi hỏi vợ bị thách cưới (làng Bắc Bộ thế kỷ 19) | Phong tục cưới hỏi | 40 giây | `tc-1..4.mp4` |

Tổng cộng 23 clip Muse.

## Thứ tự đăng

Đăng mỗi ngày 1 tập theo thứ tự 1 → 6. Dòng chữ kết của mỗi tập mời follow để xem đúng tập kế tiếp:
- Trạng 13 tuổi → "mai bạn đi sứ cùng trạng xấu nhất mà giỏi nhất"
- Mạc Đĩnh Chi → "mai bạn làm gia nhân bị Trạng Quỳnh lừa ăn mầm đá"
- Trạng Quỳnh → "mai bạn theo học thầy thuốc giỏi nhất nước Nam"
- Hải Thượng Lãn Ông → "mai bạn hầu bếp cho ông vua kén ăn nhất"
- Tự Đức → "mai bạn đi hỏi vợ bị nhà gái thách cưới"

Ba tập đầu nối với nhau thành mạch "ba ông trạng": trạng nhỏ tuổi nhất, trạng hai nước, trạng tiếu lâm. Mạch này dễ khiến người xem xem liền cả ba.

## Độ chính xác

Mỗi tập ghi rõ phần nào là **sử chép**, phần nào là **giai thoại, truyền thuyết** hay **truyện dân gian**:
- Trạng Quỳnh là truyện tiếu lâm.
- Chuyện Tự Đức uống trà sương sen là giai thoại cung đình.
- Câu đối của Mạc Đĩnh Chi là tương truyền.
- Chuyện Hải Thượng Lãn Ông có thật, lấy từ *Thượng kinh ký sự*.

Khi bị hỏi trong bình luận, bạn trả lời theo đúng các ghi chú này.

## Sửa nội dung

Toàn bộ nội dung nằm trong `_nguon.py`. Muốn đổi câu thoại hay prompt, bạn nhắn mình, mình sửa ở đó rồi chạy `python3 _nguon.py` để sinh lại tất cả file `.md` và `.plan.txt` cho khớp nhau.
