# Tiêu chuẩn giọng nói: kênh "POV - Một Ngày Ở Đại Việt"

Cập nhật 21/11/2026. Muse tạo tiếng riêng cho từng clip, nên cùng một nhân vật dễ bị đổi giọng giữa các clip. File này quy định **giọng cố định** cho từng nhân vật, **giọng vùng miền** theo từng tập, và **cách cho nhân vật lịch sử nói** (vua, tướng, danh nhân). `tools/series.py` tự chèn mô tả giọng vào prompt video của mọi clip có nhân vật đó (dòng `VOICES (...)`) và in lại trong mục "Giọng nhân vật" của mỗi file .md.

---

## 1. Năm quy tắc chung

1. **Mỗi nhân vật một giọng, giữ nguyên ở mọi clip, mọi tập.** Mô tả giọng chỉ nói âm sắc, tuổi, nhịp nói; vùng miền do khóa `giong` của tập quyết định.
2. **Các giọng trong cùng một cảnh phải khác hẳn nhau** (Anh Tư, viên chỉ huy, người dẫn chuyện, nhân vật lịch sử).
3. **Không nhạc nền.** Chỉ âm thanh tự nhiên (gió, nước, trống trận, pháo Tết…).
4. **Nói tự nhiên, không gào, không cường điệu.** Cái hài nằm ở câu thoại, không nằm ở giọng. Anh Tư nói nhỏ, tỉnh bơ; chỉ nhân vật lịch sử ở cảnh hiệu triệu mới nói to, vang.
5. **Mỗi clip chỉ một người nói tại một thời điểm.** Cảnh có lời nhân vật lịch sử thì Anh Tư im lặng; người dẫn chuyện để ở clip cuối.

---

## 2. Giọng vùng miền (khóa `giong` của từng tập)

| Bối cảnh | Giọng |
|---|---|
| **Mặc định**: Bắc Bộ, Thăng Long, các trận ở miền Bắc | Bắc (Hà Nội): `a natural Northern Vietnamese (Hà Nội) accent` |
| Quân Tây Sơn, Phú Xuân, loạt Quang Trung | Huế: `Central Vietnamese (Huế) accent` |
| Ấp Tây Sơn, An Thái, Quy Nhơn (anh em Tây Sơn thời trẻ) | Bình Định: `Central Vietnamese (Bình Định) accent` |
| Nghệ An (tuyển quân 1788, Nguyễn Thiếp, Viện Sùng Chính) | Nghệ An: `Central Vietnamese (Nghệ An) accent` |
| Gia Định, miền Nam | Nam: chỉ dùng khi bối cảnh ở miền Nam |

- **Người xem từng chê giọng Nam trong các trận ở miền Bắc**, nên không để giọng Nam lẫn vào tập miền Bắc.
- **Nhân vật khác vùng trong cùng tập** thì ghi vùng ngay trong mô tả giọng, ví dụ người dân Thăng Long trong tập quân Tây Sơn: `…, Northern accent`.
- **Người nước ngoài nói tiếng Việt** (tù binh, do thám nhà Thanh, quan nhà Tống): `speaking a few words of Vietnamese with a light Chinese accent`, nói ít, không chế giễu giọng.

---

## 3. Bảng giọng dùng chung (tự chèn ở mọi loạt)

| Nhân vật | Từ khóa trong prompt | Mô tả giọng |
|---|---|---|
| **Anh Tư** | `Anh Tư` | `ANH_TU_VOICE` trong `tools/series.py`: giọng nam khoảng 30, ấm, hơi khàn, trung trầm, **giọng Bắc (Hà Nội) ở mọi tập**, nói thong thả, hài nhẹ, không gào |
| **Người dẫn chuyện** | `narrator` | a calm, deep, slow male baritone, documentary style, warm and serious, the SAME narrator voice in every video of the channel |
| Viên chỉ huy | `officer` | a gruff, clipped male voice in his 40s, short commands, clearly different from Anh Tư's voice |
| Sứ giả, người đưa tin | `messenger`, `envoy` | a formal, crisp male voice, slightly breathless |
| Bà cụ | `old woman` | a warm, raspy elderly woman's voice |
| Ông cụ | `old farmer` | a creaky, grumpy elderly man's voice |
| Người phiên dịch | `interpreter` | a nervous, precise, thin male voice in his 30s |
| Mẹ Anh Tư | `Anh Tư's mother` | a sharp, quick-tongued woman's voice in her 50s, slightly raspy |
| Nguyễn Nhạc | `Nguyễn Nhạc` | a jovial, round, booming male voice in his late 30s, unhurried |
| Ngô Quyền | `Ngô Quyền` | a low, steady, authoritative male voice around 40, few words, never shouting |
| Trần Thủ Độ | `Thái sư` | an old, dry, very calm male voice in his 60s, slow and unshakeable |

**Đổi từ 26/11/2026 (anh chốt, thay quy định giọng Huế 25/11):** Anh Tư **luôn nói giọng Bắc (Hà Nội)** ở mọi tập, mọi bối cảnh, kể cả loạt miền Trung. Câu mô tả giọng chỉ nằm ở `ANH_TU_VOICE` (`tools/series.py`), dán y nguyên vào mọi clip; mặt Anh Tư nằm ở `ANH_TU_FACE` cùng file, khớp ảnh `content/nhan-vat/anh_tu_ref.png`.

**Đổi từ 21/11/2026:** giọng Anh Tư bỏ "quick and cheerful, a little cheeky", thay bằng "natural and conversational, dry humor, never exaggerated", cho hợp quy tắc diễn xuất tự nhiên.

---

## 4. Nhân vật lịch sử nói lời nổi tiếng (vua, tướng, danh nhân)

Áp dụng khi nhân vật thật nói câu có trong sử hoặc truyền tụng, ví dụ vua Quang Trung đọc lời dụ, Nguyễn Thiếp đoán "không quá mười ngày".

### 4.1. Giọng riêng, khai báo một lần, dùng lại mọi nơi

- **Vua Quang Trung (`QT_VOICE` trong `tools/series.py`, dùng chung mọi loạt):**
  > Quang Trung's own voice, used ONLY for him and identical in every clip: a deep, booming, thunderous male voice of a commander in his mid-thirties with a Central Vietnamese (Bình Định) accent; slow, heavy and powerful, each phrase struck like a war drum and echoing across the field; clearly different from Anh Tư and from the calm narrator.
- **Các nhân vật thật khác** (khai báo trong khóa `voices` của tập):

| Nhân vật | Mô tả giọng |
|---|---|
| Nguyễn Thiếp (La Sơn Phu Tử) | a calm, thin, unhurried old male voice with a Nghệ An accent, wise and certain |
| Lý Thường Kiệt | a deep, calm, commanding older male voice, slow and certain |
| Thượng hoàng Trần Thánh Tông | a warm, grave, older male voice, slow and clear |
| Vua Lê Hiển Tông (già yếu) | a frail, trembling, very old male voice |
| Thầy Trương Văn Hiến | a slow, dry, wise old male voice with a Nghệ An accent, few words |
| Trần Khánh Dư | giọng nam trầm, khô, thong thả |
| Trần Nhật Duật | giọng quý tộc trẻ, nhanh, vui |
| Tinh Thiều | giọng nho nhã, chậm rãi |
| Dương Thanh | giọng nam trầm, ít lời, cứng |

### 4.2. Cho người xem biết chắc ai đang nói

1. **Prompt clip** ghi rõ: `ONLY [tên] speaks… Anh Tư and the soldiers keep their mouths closed`.
2. **Phụ đề** đặt tên người nói ở dòng đầu: `Vua Quang Trung: / Đánh cho để dài tóc!`, `Nguyễn Thiếp: / Không quá mười ngày…`. Lý do: nhãn góc trên chỉ hiện 3 giây đầu clip, còn lời vua thường ở giây 5–10.
3. **Nhãn góc trên** của clip ghi tên người nói, ví dụ "Vua Quang Trung".
4. **Người dẫn chuyện** ở clip cuối được dặn "a calm, quiet narrator's voice (clearly different from the king's)".

### 4.3. Vua, danh nhân chỉ thấy từ phía sau: tránh Muse gán sai giọng

- Vì vua không lộ mặt, Muse có thể gán giọng vua cho gương mặt đang thấy (thường là Anh Tư). Khi tạo clip:
  - chọn bản **không ai mấp máy môi** trong lúc vua nói;
  - hoặc tạo lại với góc nhìn chỉ thấy lưng vua, hàng giáo, đám đông.
- Giọng vua có vang, có tiếng dội như giữa bãi rộng; không chèn nhạc.

---

## 5. Giọng nhân vật phụ theo vai (gợi ý, khai báo trong `voices` của tập)

| Vai | Mô tả gợi ý |
|---|---|
| Người giữ cửa, quan nhỏ | a dry, polite but firm middle-aged male voice |
| Quản gia hách dịch | a smug, oily middle-aged male voice |
| Lý trưởng | a fussy, nasal male voice |
| Ông thợ cả khó tính | a slow, gravelly, very strict old male voice with dry humor |
| Người lính trẻ lém | a cheeky young adult male voice |
| Người lính già | a raspy, low whisper of an old male soldier |
| Vợ Anh Tư (chị Tư) | a sharp, practical, quick-witted woman's voice around 30, Northern accent |
| Người thêu cờ, người làm nghề | a calm, steady middle-aged woman's voice |

---

## 6. Cách làm trên Muse để giọng đồng nhất thật

Mô tả bằng chữ giúp Muse ra giọng gần nhau hơn, nhưng **không bảo đảm giống hệt**.

1. **Nếu Muse có chọn giọng hoặc giọng tham chiếu** (voice reference, voice clone, giọng có sẵn):
   - Chọn **một giọng cố định** cho Anh Tư, người dẫn chuyện và vua Quang Trung; dùng đúng giọng đó cho mọi clip, mọi tập.
   - Ghi tên giọng đã chọn vào bảng ở mục 3 và 4 để lần sau dùng lại.
2. **Nếu Muse không có tính năng đó:**
   - Tạo clip xong thì nghe lại; clip nào lệch giọng rõ thì tạo lại riêng clip đó.
   - Ưu tiên giữ đúng giọng ở clip có câu chốt và clip vua nói.
3. **Người dẫn chuyện** là giọng ngoài khung hình, không cần khớp môi. Muốn giống hệt ở mọi video:
   - anh tự thu, hoặc dùng một ứng dụng đọc chữ thành giọng nói với một giọng cố định;
   - gửi file âm thanh, mình chèn vào lúc dựng thay cho giọng Muse (công cụ dựng cần thêm chức năng chèn giọng đọc, khi cần thì báo mình làm).

---

## 7. Bảng kiểm giọng trước khi đăng

- [ ] Anh Tư cùng một giọng ở mọi clip, nói tự nhiên, không gào.
- [ ] Giọng đúng vùng miền của tập (Bắc mặc định; Tây Sơn: Huế, Bình Định, Nghệ An).
- [ ] Nhân vật lịch sử có giọng riêng, khác hẳn Anh Tư và người dẫn chuyện; phụ đề có tên người nói.
- [ ] Khi vua nói, không ai khác mấp máy môi.
- [ ] Người dẫn chuyện cùng một giọng ở mọi video, chỉ ở clip cuối.
- [ ] Không nhạc nền.

## Thêm nhân vật mới

- **Xuất hiện nhiều tập:** thêm vào `VOICES` (hoặc một hằng số như `QT_VOICE`) trong `tools/series.py`.
- **Chỉ có trong một tập:** thêm khóa `voices={"Tên": "mô tả giọng"}` vào tập đó trong `_nguon.py`.
