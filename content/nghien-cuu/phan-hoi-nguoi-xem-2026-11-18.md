# Phân tích phản hồi người xem (18/11/2026)

**Nguồn:** báo cáo `TikTok_Phan_Tich_Binh_Luan_20261118.html`, gồm 395 bản ghi (392 bình luận người xem, 3 bình luận của kênh) trên 11 video.

**Giới hạn của mẫu:**
- 270/395 bình luận (68%) nằm ở video Bạch Đằng 938 "cắm cọc cả buổi sáng". Phân tích dưới đây phản ánh video đó là chính.
- Báo cáo chưa đọc hết bình luận và chưa mở hết các chuỗi trả lời, nên không dùng để suy ra tỷ lệ ý kiến của cả kênh.

## Lỗi người xem bắt được (xếp theo số bình luận)

| # | Lỗi | Số bình luận | Video | Đã sửa trong bộ tạo prompt |
|---|---|---|---|---|
| 1 | **Cọc quá nhỏ**, đóng bằng búa tay ("như que tăm", "to như cột đình mới đúng") | khoảng 30 | V01, V09 | Có: `STAKE_SPEC` tự kèm mọi cảnh có cọc |
| 2 | **Cờ đỏ sao vàng hiện đại**, có cả trên thuyền giặc; cờ giống cờ Mãn Thanh trong video dời đô | 18 | V01, V08 | Có (từ đợt tập 11): mọi prompt cấm cờ hiện đại, cảnh đông quân cấm hẳn cờ |
| 3 | **Giọng miền Nam** trong trận ở miền Bắc | 7 | V01, V09, V03 | Có: mặc định giọng Bắc, tập miền Trung ghi đè |
| 4 | **Rồng không đúng kiểu thời Lý** | 3 | V08 | Có: `DRAGON_SPEC` |
| 5 | **Chữ Hán sai thời** trên biển hay cờ | 2 | V01 | Có (từ đợt tập 11): cấm chữ |
| 6 | **Từ hiện đại** (KPI, "qua loa") | 4 | V01, V03 | Giữ có chừng mực, thêm nhãn "lời thoại hư cấu" |
| 7 | **Nhầm thật hay giả, nhầm truyền thuyết** | vài | V03 | Có: nhãn AI 3 giây đầu, tập truyền thuyết có nhãn riêng |

**Lỗi cờ là nặng nhất về độ tin cậy, và còn rủi ro.** Quốc kỳ hiện đại xuất hiện trên thuyền quân Nam Hán dễ bị coi là dùng sai quốc kỳ. Video V01 đã đăng thì không sửa được, nên chọn một trong ba cách:
1. Ghim bình luận nhận lỗi và giải thích.
2. Dựng lại bản sửa (mình làm mờ hoặc che cờ nếu anh gửi clip gốc) rồi đăng lại.
3. Làm video trả lời bình luận "Các bác nói đúng" (xem phần ý tưởng bên dưới).

## Người xem thích gì (nên giữ)

- **Câu chốt nhắc lại được:** "Đường e dẫn đấy, ghi tên em vào sử nhé" (19 lượt thích), "Cái cọc kia là của em". Câu cửa miệng của Anh Tư đang thành thương hiệu.
- **Lồng tiếng và lời thoại:** "Lồng tiếng hay vãi", "Tính ra hay hơn phim người thật", "giọng văn, ngôn từ như người Việt Nam".
- **Đùa chuyện "camera bất tử, vlog trận Bạch Đằng"** (26 bình luận): gần như toàn là đùa cùng kênh, tăng tương tác. Không phải lỗi.
- **Câu hỏi tương tác ở caption** đang có tác dụng: "Comment 1 hay 2" ở V02 kéo được người chơi game bình luận chiến thuật.

## Người xem muốn xem gì

| Yêu cầu | Bình luận | Tình trạng |
|---|---|---|
| Vua Quang Trung | C248 | **Đã làm** cả loạt Tây Sơn từng mốc và tập 9–12 |
| Video dài hơn, "full bộ" | C189, C074 | **Đã làm** Bạch Đằng 938 bản 3 phút |
| Rùa thần Hồ Gươm | C032 | **Chưa làm**: truyền thuyết, cần nhãn truyền thuyết |
| Yết Kiêu | C005, C270 | **Chưa làm**: Yết Kiêu thuộc thời Trần (thế kỷ 13), không phải năm 1427 |
| Thêm sử Việt, thêm video | nhiều | Duy trì lịch đăng đều |

## Ý tưởng video trả lời bình luận (biến lời chê thành nội dung)

1. **"Các bác nói đúng: cọc Bạch Đằng thật to cỡ nào?"** Trả lời C125, C280. Dựng lại cảnh đóng cọc đúng cỡ, nhiều người cùng đóng, kèm ảnh bãi cọc khảo cổ có ghi nguồn.
2. **"Thời Ngô Quyền có cờ đỏ sao vàng không?"** Trả lời C292, C337. Nhận lỗi AI tự chèn cờ, giải thích cờ thời xưa là chưa rõ, và nói kênh đã sửa quy trình. Nhận lỗi công khai giúp giữ uy tín.
3. **"Ai quay vlog trận Bạch Đằng?"** Trả lời C373 ("tui là người cầm máy quay nè"). Dựng Anh Tư làm "người quay phim bất tử", rồi chuyển sang phần giải thích sự kiện.

## Việc đã làm sau phân tích

- `tools/series.py`:
  - Mặc định giọng Bắc; khóa `giong` để đổi giọng cho tập ở miền Trung, miền Nam.
  - Tự kèm `STAKE_SPEC` cho mọi cảnh có cọc và `DRAGON_SPEC` cho mọi cảnh có rồng.
  - Tập truyền thuyết có `legend=True`.
- `tools/tiktok.py`: nhãn "AI tái hiện · lời thoại hư cấu" (hoặc "· theo truyền thuyết") hiện 3 giây đầu.
- Giọng miền Trung đã đặt cho các tập Tây Sơn ở Bình Định, Nghệ An, Huế.
- Nhãn truyền thuyết đã đặt cho Chử Đồng Tử, Thánh Gióng, Mai An Tiêm, Lương Thế Vinh cân voi, nỏ thần Cổ Loa, Dạ Trạch.
- Chuẩn mới đã ghi vào `chuan-hinh-anh-quan-doi.md`.
