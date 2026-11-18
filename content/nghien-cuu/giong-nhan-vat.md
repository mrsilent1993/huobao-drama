# Giọng nhân vật: bảng giọng cố định

Muse tạo tiếng riêng cho từng clip, nên cùng một nhân vật dễ bị đổi giọng giữa các clip (Anh Tư clip này trầm, clip sau cao). Bảng dưới đây là **mô tả giọng cố định** cho từng nhân vật. `tools/series.py` tự chèn mô tả vào prompt video của mọi clip có nhân vật đó (dòng `VOICES (...)`), và in lại trong mục "Giọng nhân vật" của mỗi file .md.

## Bảng giọng dùng chung (mọi loạt)

| Nhân vật | Từ khóa nhận diện trong prompt | Mô tả giọng |
|---|---|---|
| Anh Tư | `Anh Tư` | a bright, slightly husky male voice around 30, quick and cheerful, a little cheeky when joking, the SAME voice in every clip |
| người dẫn chuyện | `narrator` | a calm, deep, slow male baritone, documentary style, warm and serious, the SAME narrator voice in every video of the channel |
| mẹ Anh Tư | `Anh Tư's mother` | a sharp, quick-tongued woman's voice in her 50s, slightly raspy |
| Nguyễn Nhạc | `Nguyễn Nhạc` | a jovial, round, booming male voice in his late 30s, unhurried |
| Ngô Quyền | `Ngô Quyền` | a low, steady, authoritative male voice around 40, few words, never shouting |
| Trần Thủ Độ | `Thái sư` | an old, dry, very calm male voice in his 60s, slow and unshakeable |
| viên chỉ huy | `officer` | a gruff, clipped male voice in his 40s, short commands, clearly different from Anh Tư's voice |
| sứ giả, người đưa tin | `messenger` | a formal, crisp male voice, slightly breathless |
| bà cụ | `old woman` | a warm, raspy elderly woman's voice |
| ông cụ | `old farmer` | a creaky, grumpy elderly man's voice |
| người phiên dịch | `interpreter` | a nervous, precise, thin male voice in his 30s |

**Giọng riêng của từng tập** (khóa `voices` trong `_nguon.py`):

| Nhân vật | Tập | Mô tả giọng |
|---|---|---|
| Trần Khánh Dư | Vân Đồn 1288 | giọng nam trầm, khô, thong thả |
| Trần Nhật Duật | Hàm Tử 1285 | giọng quý tộc trẻ, nhanh, vui |
| Lính Tống lưu vong | Hàm Tử 1285 | giọng ông lớn tuổi, nói tiếng Việt lơ lớ |
| Nguyễn Thiếp | La Sơn Phu Tử 1788 | giọng già, mảnh, chậm, hơi mỉa |
| Tinh Thiều | Bắc thuộc 541 | giọng nho nhã, chậm rãi |
| Dương Thanh | Bắc thuộc 819 | giọng nam trầm, ít lời, cứng |

Mô tả giọng chỉ nói âm sắc, tuổi và nhịp nói. **Vùng miền** do khóa `giong` của tập quyết định: mặc định giọng Bắc, các tập Tây Sơn dùng giọng miền Trung.

## Cách làm trên Muse để giọng đồng nhất thật

Mô tả bằng chữ giúp Muse ra giọng gần nhau hơn, nhưng **không bảo đảm giống hệt**. Cách chắc nhất:

1. **Nếu Muse có chọn giọng hoặc giọng tham chiếu** (voice reference, voice clone, chọn giọng có sẵn):
   - Chọn **một giọng cố định cho Anh Tư** và một giọng cố định cho **người dẫn chuyện**, rồi dùng đúng giọng đó cho mọi clip, mọi tập.
   - Lưu tên giọng đã chọn vào bảng trên để lần sau dùng lại.
2. **Nếu Muse không có tính năng đó:**
   - Tạo clip xong thì nghe lại. Clip nào giọng Anh Tư lệch rõ so với các clip khác thì tạo lại riêng clip đó.
   - Ưu tiên giữ đúng giọng ở clip có câu chốt.
3. **Người dẫn chuyện** là giọng đọc ngoài khung hình, không cần khớp môi. Muốn giọng đọc giống hệt ở mọi video thì có hai cách:
   - Anh tự thu giọng đọc.
   - Dùng một ứng dụng đọc chữ thành giọng nói với cố định một giọng.

   Gửi file âm thanh cho mình, mình chèn vào lúc dựng thay cho giọng Muse. Công cụ dựng cần thêm chức năng chèn giọng đọc, khi nào anh cần thì báo mình làm.

## Thêm nhân vật mới

- **Nhân vật xuất hiện nhiều tập:** thêm vào `VOICES` trong `tools/series.py`.
- **Nhân vật chỉ có trong một tập:** thêm khóa `voices={"Tên": "mô tả giọng"}` vào tập đó trong `_nguon.py`.
