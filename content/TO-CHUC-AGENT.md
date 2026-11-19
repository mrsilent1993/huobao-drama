# Tổ chức "công ty agent" cho kênh POV - Một Ngày Ở Đại Việt

Thiết kế dựa trên toàn bộ công việc đã làm trong session này: nghiên cứu đề tài, kiểm chứng sử, viết kịch bản, viết prompt Muse, kiểm duyệt, dựng FFmpeg, đăng bài, đọc bình luận và số liệu, kiếm tiền.

**Đề xuất: 9 agent, chia 3 khối.** Trong đó **Sử gia** và **Kiểm duyệt nội quy TikTok, YouTube** là 2 agent bắt buộc, có quyền chặn video. Muốn gọn thì chạy bản rút gọn 6 agent (cuối file), hai agent này vẫn giữ riêng.

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
  3. Sử gia 🔒                6. Kiểm duyệt nội quy 🔒      9. Kiếm tiền và đối tác
  4. Biên kịch                7. Dựng phim và kiểm tra
```

**Luồng một video:**
2 chọn đề tài → 3 tra nguồn → 4 viết kịch bản → 5 viết prompt → **🔒 Cổng 1: Sử gia (3) + Kiểm duyệt (6) duyệt kịch bản và prompt** → **anh tạo clip trên Muse** → 7 kiểm tra clip, dựng 2 bản → **🔒 Cổng 2: Sử gia (3) soát hình + Kiểm duyệt (6) soát nội quy** → **anh duyệt** → 8 soạn thông tin đăng → **anh đăng** → 8 theo dõi bình luận → 2 phân tích → 1 cập nhật tiêu chuẩn.

---

## Hai agent bắt buộc, có quyền chặn 🔒

**Sử gia (3)** và **Kiểm duyệt nội quy TikTok, YouTube (6)** là hai "cổng" bắt buộc:
- **Luôn là 2 agent riêng.** Không gộp với nhau, không gộp với agent nào khác, kể cả ở bản rút gọn.
- **Có quyền chặn:** một trong hai nói "không" thì video dừng lại, trả về sửa. Điều phối không được bỏ qua.
- **Duyệt ở 2 cổng:**
  - **Cổng 1 · Kịch bản:** trước khi anh tạo clip Muse, cả hai cùng duyệt kịch bản và prompt.
  - **Cổng 2 · Bản dựng:** trước khi đăng. Sử gia soát hình (trang phục, cờ, cọc, vật dụng sai thời); Kiểm duyệt soát theo bảng kiểm TikTok, YouTube và luật.
- **Lý do:** các lỗi nặng nhất của kênh đều thuộc hai vai này. Tập A3 bị TikTok gắn cờ an toàn trẻ em; video Bạch Đằng 938 bị khoảng 30 bình luận chê cọc nhỏ và 18 bình luận chê cờ hiện đại.

## Bảng tổng quan

| # | Agent | Việc chính | Đầu ra | Có trong session này |
|---|---|---|---|---|
| 1 | **Điều phối sản xuất** | Nhận yêu cầu của anh, chia việc, giữ lịch đăng và `TIEU-CHUAN-KICH-BAN.md` | Kế hoạch tuần, lịch đăng, tiêu chuẩn cập nhật | Lập lịch 7 ngày, thứ tự loạt, cập nhật tiêu chuẩn |
| 2 | **Phân tích dữ liệu và xu hướng** | Đọc số liệu TikTok, YouTube và bình luận, đề xuất đề tài | Báo cáo hiệu quả, danh sách đề tài xếp hạng | Phân tích 11 video, 395 bình luận |
| 3 | **Sử gia, kiểm chứng** 🔒 | Tra nguồn, chấm mức A/B/C, tách sử chép và hư cấu, chuẩn hình ảnh từng thời | Phần lịch sử, chuẩn trang phục, cảnh báo sai sử | Cọc Bạch Đằng, vua giả 1790, quân Xiêm 1785… |
| 4 | **Biên kịch** | Viết kịch bản theo công thức Anh Tư | `_nguon.py` của tập: cảnh, câu chốt, hook, bản ngắn | Hơn 50 tập ở 10 loạt |
| 5 | **Prompt Muse** (hình và giọng) | Viết prompt ảnh và video, chuẩn hình ảnh, giọng, nối cảnh | File .md dán thẳng vào Muse | 7 quy tắc hình ảnh, bảng giọng, nối cảnh |
| 6 | **Kiểm duyệt nội quy TikTok và YouTube** 🔒 | Soát kịch bản và bản dựng theo nội quy TikTok, YouTube và luật Việt Nam (`nghien-cuu/noi-quy-tiktok-youtube.md`) | Phiếu duyệt có hoặc không, kèm yêu cầu sửa | Làm lại tập A3, tập "Ngày thứ 42" |
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

### 3. Sử gia, kiểm chứng (Historian) 🔒

- **Vai trò:** bảo đảm đúng sử, không xuyên tạc lịch sử, không để người xem bắt lỗi như vụ cọc nhỏ và cờ hiện đại.
- **Có quyền chặn** ở cả Cổng 1 (kịch bản, prompt) và Cổng 2 (bản dựng).
- **Đầu vào:** đề tài; kịch bản của agent 4; prompt của agent 5; bản dựng của agent 7.
- **Đầu ra:**
  - Phần "Lịch sử" của tập: sử chép kèm nguồn, phần dựng lại, phần hư cấu, mức A/B/C.
  - Chuẩn hình ảnh từng phe (`nghien-cuu/chuan-hinh-anh-quan-doi.md`).
  - Số liệu đã tra.
  - Phiếu duyệt CHO QUA / CHẶN.
- **Bảng kiểm:**
  1. Sự kiện, năm, địa danh, nhân vật đúng; không ghép nhầm thời đại (ví dụ Yết Kiêu thuộc thời Trần).
  2. Có mức nguồn; tách rõ sử chép, dựng lại, hư cấu; câu của nhân vật thật ghi "phỏng theo".
  3. Truyền thuyết có nhãn "theo truyền thuyết"; chuyện tranh cãi để ngỏ; cách gọi gây tranh cãi ghi "theo sử hiện đại".
  4. Số liệu khớp nguồn, ghi khoảng giá trị nếu các nguồn lệch nhau.
  5. **Không xuyên tạc lịch sử, không hạ thấp anh hùng và danh nhân** (Luật An ninh mạng 2018, phối hợp với agent 6).
  6. **Hình đúng thời:** trang phục, thuyền, vũ khí, kiến trúc, cờ, cọc, rồng; không vật dụng hiện đại. Từ hiện đại cố ý gây cười (KPI…) được phép tối đa 1 lần mỗi tập.
  7. Mục nào chưa tra được thì đánh dấu ⚠️ và báo anh.
- **Kỹ năng nên gắn:** nghiên cứu web sâu (deep research), phân tích sử (historian-analyst).
- **Đo hiệu quả:** 0 lỗi sử bị người xem bắt sau khi đăng.

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

### 6. Kiểm duyệt nội quy TikTok và YouTube (Compliance) 🔒

- **Vai trò:** chặn mọi rủi ro bị gắn cờ, bị gỡ video, bị giới hạn độ tuổi, mất quyền kiếm tiền, hoặc vi phạm luật Việt Nam.
- **Có quyền chặn** ở cả Cổng 1 và Cổng 2.
- **Đầu vào:** kịch bản, prompt, bản dựng, thông tin đăng (tiêu đề, mô tả, ảnh bìa, sản phẩm gắn kèm).
- **Đầu ra:** phiếu duyệt theo **`nghien-cuu/noi-quy-tiktok-youtube.md`** (mục A1–D4), kết luận CHO QUA / CHẶN kèm danh sách sửa.
- **Bảng kiểm gồm 4 nhóm:**
  - **A. Chung:** an toàn trẻ vị thành niên, bạo lực và hình ảnh ghê sợ, thù ghét, thông tin sai lệch, nhãn AI, tiêu đề đúng nội dung, bản quyền, quốc kỳ.
  - **B. TikTok:**
    - Nhãn "Nội dung do AI tạo".
    - Đủ điều kiện lên "Dành cho bạn": không kêu gọi rời TikTok bằng lời, không đăng lại video cũ.
    - Gắn sản phẩm đúng chỗ.
    - Video trả lời bình luận.
    - Không dùng bot trả lời bình luận.
  - **C. YouTube:**
    - "Nội dung bị thay đổi" chọn **Có**; "Dành cho trẻ em" chọn **Không**.
    - Bối cảnh giáo dục cho cảnh chiến tranh.
    - **Chính sách nội dung hàng loạt, thiếu tính nguyên bản** (điều kiện kiếm tiền YPP).
    - Siêu dữ liệu đúng nội dung; định dạng Shorts.
  - **D. Luật Việt Nam:**
    - Luật An ninh mạng 2018: không xuyên tạc lịch sử, không xúc phạm anh hùng.
    - Luật Trí tuệ nhân tạo số 134/2025: gắn nhãn AI.
    - Quốc kỳ; tài khoản đã xác thực.
- **Cập nhật:** đọc lại trang chính sách chính thức của TikTok và YouTube **mỗi tháng**, sửa bảng kiểm khi có thay đổi.
- **Đo hiệu quả:** 0 video bị gắn cờ, gỡ, giới hạn độ tuổi; kênh đủ điều kiện kiếm tiền.

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

## Bản rút gọn: 6 agent

Dùng khi muốn ít agent hơn. **Sử gia và Kiểm duyệt vẫn giữ riêng, có quyền chặn.**

| Agent | Gồm |
|---|---|
| A. Điều phối và phân tích | 1 + 2 |
| B. **Sử gia** 🔒 | 3 |
| C. **Kiểm duyệt nội quy TikTok, YouTube** 🔒 | 6 |
| D. Biên kịch và prompt | 4 + 5 |
| E. Dựng phim và kiểm tra | 7 |
| F. Đăng bài và kiếm tiền | 8 + 9 |

**Không bao giờ gộp Sử gia hay Kiểm duyệt với Biên kịch:** người viết khó tự bắt lỗi của chính mình. Vụ tập A3 bị gắn cờ là ví dụ.

## Tài sản dùng chung cho mọi agent

- `content/TIEU-CHUAN-KICH-BAN.md`: luật chung, ai cũng phải đọc trước.
- `content/MAU-KICH-BAN.md`: mẫu cho từng video.
- `content/nghien-cuu/chuan-hinh-anh-quan-doi.md`, `content/nghien-cuu/giong-nhan-vat.md`.
- `content/nghien-cuu/noi-quy-tiktok-youtube.md`: bảng kiểm của agent Kiểm duyệt.
- `content/tools/`:
  - `series.py`: sinh prompt.
  - `tiktok.py`: dựng video.
  - `khung-cuoi.py`: cắt khung cuối.
  - `xuat_phieu.py`: xuất phiếu.
- `content/xuat/phieu-san-xuat/`: phiếu từng video và mục lục trạng thái.
