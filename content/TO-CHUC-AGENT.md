# Tổ chức "công ty agent" cho kênh POV - Một Ngày Ở Đại Việt

Thiết kế dựa trên toàn bộ công việc đã làm trong session này: nghiên cứu đề tài, kiểm chứng sử, viết kịch bản, viết prompt Muse, kiểm duyệt, dựng FFmpeg, đăng bài, đọc bình luận và số liệu, kiếm tiền.

**Đề xuất: 9 agent, chia 3 khối.** Muốn gọn thì chạy bản rút gọn 5 agent (cuối file).

Anh là **Giám đốc (người duyệt)**. Có 3 việc agent không thay được:
- Tạo clip trên Muse (Muse không có kết nối tự động).
- Bấm đăng TikTok, YouTube.
- Duyệt cuối.

---

## Sơ đồ

```
                         ANH (Giám đốc, duyệt cuối)
                                   │
                    ┌──────────────┴──────────────┐
                    │  1. ĐIỀU PHỐI SẢN XUẤT       │  giữ kế hoạch, lịch đăng, tiêu chuẩn
                    └──────────────┬──────────────┘
      ┌────────────────────────────┼────────────────────────────┐
  KHỐI NỘI DUNG               KHỐI SẢN XUẤT                KHỐI TĂNG TRƯỞNG
  2. Phân tích dữ liệu        5. Prompt Muse               8. Đăng bài và cộng đồng
  3. Sử gia, kiểm chứng       6. Kiểm duyệt an toàn        9. Kiếm tiền và đối tác
  4. Biên kịch                7. Dựng phim và kiểm tra
```

**Luồng một video:**
2 chọn đề tài → 3 tra nguồn → 4 viết kịch bản → 3 soát sử → 5 viết prompt → 6 kiểm duyệt kịch bản → **anh tạo clip trên Muse** → 7 kiểm tra clip, dựng 2 bản → 6 kiểm duyệt bản dựng → **anh duyệt** → 8 soạn thông tin đăng → **anh đăng** → 8 theo dõi bình luận → 2 phân tích → 1 cập nhật tiêu chuẩn.

---

## Bảng tổng quan

| # | Agent | Việc chính | Đầu ra | Có trong session này |
|---|---|---|---|---|
| 1 | **Điều phối sản xuất** | Nhận yêu cầu của anh, chia việc, giữ lịch đăng và `TIEU-CHUAN-KICH-BAN.md` | Kế hoạch tuần, lịch đăng, tiêu chuẩn cập nhật | Lập lịch 7 ngày, thứ tự loạt, cập nhật tiêu chuẩn |
| 2 | **Phân tích dữ liệu và xu hướng** | Đọc số liệu TikTok, YouTube và bình luận, đề xuất đề tài | Báo cáo hiệu quả, danh sách đề tài xếp hạng | Phân tích 11 video, 395 bình luận |
| 3 | **Sử gia, kiểm chứng** | Tra nguồn, chấm mức A/B/C, tách sử chép và hư cấu, chuẩn hình ảnh từng thời | Phần lịch sử, chuẩn trang phục, cảnh báo sai sử | Cọc Bạch Đằng, vua giả 1790, quân Xiêm 1785… |
| 4 | **Biên kịch** | Viết kịch bản theo công thức Anh Tư | `_nguon.py` của tập: cảnh, câu chốt, hook, bản ngắn | Hơn 50 tập ở 10 loạt |
| 5 | **Prompt Muse** (hình và giọng) | Viết prompt ảnh và video, chuẩn hình ảnh, giọng, nối cảnh | File .md dán thẳng vào Muse | 7 quy tắc hình ảnh, bảng giọng, nối cảnh |
| 6 | **Kiểm duyệt an toàn** | Soát kịch bản và bản dựng theo quy định TikTok, YouTube và luật | Phiếu duyệt có hoặc không, kèm yêu cầu sửa | Làm lại tập A3, tập "Ngày thứ 42" |
| 7 | **Dựng phim và kiểm tra kỹ thuật** | Kiểm clip Muse, dựng FFmpeg ra 2 bản, chuyển cảnh, phụ đề, âm lượng | `-youtube.mp4`, `-tiktok.mp4`, ảnh bìa | `tiktok.py`, `khung-cuoi.py`, chuyển cảnh |
| 8 | **Đăng bài và cộng đồng** | Soạn tiêu đề, mô tả, thẻ, bình luận ghim; trả lời bình luận; video trả lời | Thông tin đăng, kịch bản trả lời bình luận | Mục đăng ở mỗi tập, video "Cọc thật to cỡ nào" |
| 9 | **Kiếm tiền và đối tác** | TikTok Shop, YouTube Partner Program, sản phẩm gắn video, đối tác | Kế hoạch kiếm tiền, danh sách sản phẩm | Tư vấn gắn sách, mốc YPP |

---

## Mô tả từng agent

### 1. Điều phối sản xuất (Producer)

- **Vai trò:** "trưởng phòng". Nhận yêu cầu của anh, chia việc cho các agent, ghép kết quả, báo anh duyệt.
- **Đầu vào:** yêu cầu của anh; báo cáo của agent 2; trạng thái từng video.
- **Đầu ra:**
  - Kế hoạch tuần, lịch đăng (mỗi ngày một tập).
  - `content/xuat/phieu-san-xuat/MUC-LUC.md` (đánh dấu đã đăng).
  - `TIEU-CHUAN-KICH-BAN.md` cập nhật sau mỗi lần anh chỉnh hoặc người xem góp ý.
- **Quy tắc:**
  - Không cho video qua bước tiếp nếu thiếu duyệt của agent 3 và agent 6.
  - Mọi thay đổi quy tắc ghi vào tiêu chuẩn.
  - Chỉ đẩy lên nhánh làm việc.
- **Đo hiệu quả:** đăng đúng lịch, số vòng phải sửa mỗi video giảm dần.

### 2. Phân tích dữ liệu và xu hướng (Analyst)

- **Vai trò:** đọc số liệu (lượt xem, tỷ lệ thích, tỷ lệ xem hết, chia sẻ, nguồn truy cập, độ tuổi) và bình luận, rồi rút bài học.
- **Đầu vào:** ảnh chụp TikTok Studio, YouTube Studio; file bình luận xuất ra.
- **Đầu ra:**
  - Bảng so sánh video theo tỷ lệ thích (không so lượt xem thô vì video đăng ngày khác nhau).
  - Danh sách lỗi người xem bắt được.
  - Đề tài người xem xin.
  - Đề tài xếp hạng ưu tiên.
- **Quy tắc:**
  - Ghi rõ giới hạn của mẫu (ví dụ 68% bình luận dồn vào một video).
  - Không suy ra nhu cầu của cả kênh từ một bình luận.
- **Đo hiệu quả:** đề tài được đề xuất có tỷ lệ thích từ 4,5% trở lên.

### 3. Sử gia, kiểm chứng (Historian)

- **Vai trò:** bảo đảm đúng sử, tránh bị bắt lỗi như vụ cọc nhỏ và cờ hiện đại.
- **Đầu vào:** đề tài; bản nháp kịch bản của agent 4.
- **Đầu ra:**
  - Phần "Lịch sử" của tập, gồm sử chép kèm nguồn, phần dựng lại và phần hư cấu, mức A/B/C.
  - Chuẩn hình ảnh từng phe trong `nghien-cuu/chuan-hinh-anh-quan-doi.md`.
  - Số liệu đã tra (ví dụ cọc Yên Giang 2,6–2,8 m, đường kính 20–30 cm).
- **Quy tắc:**
  - Chuyện tranh cãi thì để ngỏ.
  - Không ghép nhầm thời đại.
  - Chuyện có cách gọi gây tranh cãi thì ghi "theo sử hiện đại".
  - Truyền thuyết phải gắn nhãn.
  - Mục nào chưa tra được thì đánh dấu ⚠️.
- **Kỹ năng nên gắn:** nghiên cứu web sâu (deep research), phân tích sử (historian-analyst).

### 4. Biên kịch (Scriptwriter)

- **Vai trò:** viết kịch bản theo `TIEU-CHUAN-KICH-BAN.md` mục 1–3 và điền `MAU-KICH-BAN.md`.
- **Đầu vào:** đề tài đã duyệt; phần lịch sử của agent 3.
- **Đầu ra:** mục của tập trong `_nguon.py`:
  - 5–6 cảnh, câu ở 0–5 và 5–10 giây.
  - Câu đáng gửi bạn bè, câu chốt cuối riêng.
  - Hook và 2 hook dự phòng.
  - Đoạn cắt cho bản ngắn đủ cảnh.
- **Quy tắc:**
  - Mỗi clip một câu chốt.
  - Tối đa một từ hiện đại mỗi tập.
  - Không dùng "Ghi tên em vào sử".
  - Không đùa về anh hùng, dân tộc, nước khác.
  - Hook tối đa khoảng 20 ký tự mỗi dòng, phụ đề tối đa khoảng 26 ký tự mỗi dòng.
- **Đo hiệu quả:** tỷ lệ xem hết, số chia sẻ, câu chốt được người xem nhắc lại trong bình luận.

### 5. Prompt Muse: hình ảnh và giọng (Prompt designer)

- **Vai trò:** biến kịch bản thành prompt dán thẳng vào Muse.
- **Đầu vào:** kịch bản của agent 4; chuẩn hình ảnh của agent 3.
- **Đầu ra:** prompt ảnh khung đầu và prompt video từng clip; bảng giọng nhân vật; đánh dấu nối cảnh; bản cuối đã quay được khóa lại (`md_frozen`).
- **Quy tắc:**
  - 7 quy tắc hình ảnh: danh sách cấm, cảnh một phe ghi "ONLY", tách người trao và người nhận, cấm cờ hiện đại, không chữ…
  - Cọc đúng cỡ, rồng kiểu thời Lý.
  - Giọng vùng miền đúng; giọng cố định cho Anh Tư và người dẫn chuyện.
- **Đo hiệu quả:** số clip phải tạo lại vì sai hình hoặc sai giọng.

### 6. Kiểm duyệt an toàn (Compliance)

- **Vai trò:** chặn rủi ro bị gắn cờ hoặc bị gỡ video, hai lần: khi duyệt kịch bản và khi duyệt bản dựng.
- **Đầu vào:** kịch bản, prompt, bản dựng.
- **Đầu ra:** phiếu duyệt có hoặc không, kèm danh sách sửa.
- **Danh sách kiểm:**
  - **Trẻ em:** không cận cảnh, không khóc, không chiến tranh, không hôn nhân dưới 18 tuổi.
  - **Bạo lực:** không máu, không xác, không cảnh chết hay hành quyết.
  - **Đề tài tránh:** Chiêm Thành, các mốc hành quyết.
  - **Quốc kỳ và nhãn AI:** không cờ hiện đại; bật nhãn AI trên TikTok, YouTube và trong video.
  - **Thù ghét, thông tin sai.**
  - **Luật AI Việt Nam số 134/2025** (hiệu lực từ 1/3/2026).
- **Đo hiệu quả:** 0 video bị gắn cờ hoặc bị gỡ.

### 7. Dựng phim và kiểm tra kỹ thuật (Editor/QA)

- **Vai trò:** kiểm clip Muse anh gửi, rồi dựng thành phẩm.
- **Đầu vào:** clip Muse từ Drive; `*.plan.txt`.
- **Đầu ra:**
  - Bản YouTube và bản TikTok: 1080x1920, 30 khung/giây, -14 LUFS.
  - Chuyển cảnh, phụ đề, nhãn AI, ảnh bìa.
  - Khung cuối để nối cảnh; bảng chấm độ liền mạch.
- **Quy tắc:**
  - Kiểm từng clip: cờ, chữ, trang phục, giọng, lời nói khớp phụ đề.
  - Chỉ thử bằng clip giả rồi xóa; không dùng clip cũ.
  - Kiểm thời lượng sau dựng.
- **Công cụ:** `tools/tiktok.py`, `tools/khung-cuoi.py`, FFmpeg.
- **Đo hiệu quả:** 0 lỗi kỹ thuật (chữ đè nhau, lệch tiếng, sai thời lượng).

### 8. Đăng bài và cộng đồng (Publisher)

- **Vai trò:** chuẩn bị mọi thứ để anh bấm đăng, rồi chăm sóc bình luận.
- **Đầu vào:** bản dựng đã duyệt; lịch của agent 1.
- **Đầu ra:**
  - Hook, tiêu đề, mô tả, hashtag, thẻ YouTube, bình luận ghim.
  - Gợi ý ghim video và danh sách phát.
  - Bản nháp trả lời bình luận.
  - Kịch bản video trả lời bình luận.
- **Quy tắc:**
  - Tiêu đề không lộ cú lật; bình luận ghim không trả lời câu hỏi ở caption.
  - Trailer dẫn sang YouTube nhưng chỉ nhắc nhẹ.
  - **Chỉ soạn nháp trả lời bình luận để anh duyệt, không dùng bot trả lời tự động.**
- **Đo hiệu quả:** tỷ lệ bình luận, follow và subscriber mới sau mỗi video.

### 9. Kiếm tiền và đối tác (Monetization)

- **Vai trò:** biến lượt xem thành thu nhập.
- **Đầu vào:** số liệu kênh; danh sách video đã đăng.
- **Đầu ra:**
  - Kế hoạch đạt YouTube Partner Program: 1.000 subscriber cộng 10 triệu lượt xem Shorts trong 90 ngày.
  - TikTok Shop affiliate: gắn sách lịch sử 50–200 nghìn đồng vào video đúng chủ đề.
  - Danh sách đối tác (nhà sách, bảo tàng, du lịch di tích).
- **Quy tắc:**
  - Không gắn sản phẩm vào tập mở đầu loạt hay tập nhạy cảm.
  - Sản phẩm phải khớp nội dung video.
  - TikTok Creator Rewards chưa mở ở Việt Nam.
- **Đo hiệu quả:** doanh thu tiếp thị liên kết, tiến độ đến mốc YPP.

---

## Bản rút gọn: 5 agent

Dùng khi muốn ít agent hơn:

| Agent gộp | Gồm |
|---|---|
| A. Điều phối và phân tích | 1 + 2 |
| B. Sử gia và kiểm duyệt | 3 + 6 |
| C. Biên kịch và prompt | 4 + 5 |
| D. Dựng phim và kiểm tra | 7 |
| E. Đăng bài và kiếm tiền | 8 + 9 |

**Không gộp kiểm duyệt (6) với biên kịch (4):** người viết khó tự bắt lỗi của chính mình. Vụ tập A3 bị gắn cờ là ví dụ.

## Tài sản dùng chung cho mọi agent

- `content/TIEU-CHUAN-KICH-BAN.md`: luật chung, ai cũng phải đọc trước.
- `content/MAU-KICH-BAN.md`: mẫu cho từng video.
- `content/nghien-cuu/chuan-hinh-anh-quan-doi.md`, `content/nghien-cuu/giong-nhan-vat.md`.
- `content/tools/`:
  - `series.py`: sinh prompt.
  - `tiktok.py`: dựng video.
  - `khung-cuoi.py`: cắt khung cuối.
  - `xuat_phieu.py`: xuất phiếu.
- `content/xuat/phieu-san-xuat/`: phiếu từng video và mục lục trạng thái.
