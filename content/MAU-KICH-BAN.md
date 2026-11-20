# Mẫu kịch bản một video

Điền đủ các mục dưới đây trước khi viết vào `_nguon.py`. Quy tắc chi tiết ở `TIEU-CHUAN-KICH-BAN.md`.

## A. Thông tin chung

| Mục | Điền |
|---|---|
| Loạt / số tập | |
| Sự kiện, năm, địa danh | |
| Mức nguồn (A / B / C) | |
| Truyền thuyết? (nhãn "theo truyền thuyết") | có / không |
| Số clip (5 chuẩn / 6 đầy đủ) | |
| Tiền tố tên file Muse | ví dụ `ts1775` → `ts1775-1.mp4`… |
| Giọng vùng miền (mặc định Bắc) | |
| Nhân vật có lời ngoài Anh Tư, người dẫn chuyện, viên chỉ huy (mô tả giọng) | |
| Phe xuất hiện và chuẩn hình ảnh (trang phục, thuyền, cờ, danh sách cấm) | |

## B. Ý tưởng

- **Việc vô lý Anh Tư bị giao:**
- **Câu gạt của cấp trên (mỗi tập một câu riêng, hợp nhân vật; KHÔNG dùng "Không hỏi."):**
- **Câu đáng gửi bạn bè (câu chính của tập):**
- **Cú lật ở cuối (sự kiện thật, lời người dẫn chuyện):**
- **Câu chốt cuối RIÊNG của tập, nối lại chi tiết nào trong tập:** (không dùng "Ghi tên em vào sử")
- **Từ hiện đại duy nhất (nếu có):**
- **Hook "POV: …"** (mỗi dòng tối đa khoảng 20 ký tự) + 2 hook dự phòng:

## C. Bảng cảnh

| Cảnh | Tên | Mốc thời gian trên video | 0–5 giây (câu) | 5–10 giây (câu) | Bản ngắn dùng (nguyên / 0-5 / 5-10) | Nối cảnh với clip trước? | Chuyển cảnh vào clip |
|---|---|---|---|---|---|---|---|
| 1 | | | | | nguyên | — | — |
| 2 | | | | | | | |
| 3 | | | | | nguyên | | |
| 4 | | | | | | | |
| 5 | | | | | nguyên | | |
| (6) | | | | | | | |

Độ dài (sau chuyển cảnh): **YouTube 60–70 giây**, đủ 7 cảnh; **TikTok 30–35 giây**, 4 cảnh chính giữ trọn (`tiktok_canh=[1, x, y, 7]`). Đặt `muc=MUC_MOI` để `_nguon.py` tự kiểm.

## D. Lịch sử (in vào file .md)

- **Sử chép (kèm nguồn, mức nguồn):**
- **Phần dựng lại:**
- **Hư cấu:** Anh Tư, lời thoại, …
- **Những gì chỉ nói bằng lời, không dựng cảnh:**

## E. Đăng

- **Màn hình kết:** "Follow để xem [tập tiếp] →".
- **Tiêu đề TikTok:**
- **Mô tả + câu hỏi kéo bình luận:**
- **Hashtag của tập:**
- **Bình luận ghim:** câu hỏi hoặc gợi ý, không lộ đáp án; nhắc tập trước.
- **Tiêu đề YouTube** (tối đa 100 ký tự):
- **Thẻ YouTube** (có dấu, ngăn cách bằng dấu phẩy):

## F. Tự kiểm trước khi giao

- [ ] Việc vô lý rõ ngay giây đầu; mỗi clip có đúng một câu chốt.
- [ ] Câu chốt cuối riêng, không lặp tập khác; không có "Ghi tên em vào sử".
- [ ] Hook và tiêu đề không lộ cú lật; bình luận ghim không trả lời câu hỏi ở caption.
- [ ] Phụ đề mỗi dòng tối đa khoảng 26 ký tự; đã kiểm bằng `layout()`; phụ đề cuối kết thúc trước màn hình kết.
- [ ] YouTube đủ mọi cảnh (60–70 giây); TikTok 4 cảnh chính chọn bằng `tiktok_canh`, giữ trọn câu thoại (30–35 giây); không có cảnh báo ⚠ khi chạy `_nguon.py`.
- [ ] Prompt: chuẩn hình ảnh và danh sách cấm; cấm cờ hiện đại; không chữ; tách người trao và người nhận; cảnh một phe ghi "ONLY".
- [ ] Cọc đúng cỡ, rồng kiểu thời Lý (nếu có).
- [ ] Giọng vùng miền đúng; giọng nhân vật đã khai báo.
- [ ] An toàn: không trẻ em cận cảnh, không máu, không cảnh chết, không đùa về anh hùng, dân tộc, nước khác; vua chỉ thấy từ phía sau.
- [ ] Lịch sử: có mức nguồn, tách sử chép, dựng lại, hư cấu; số liệu đã tra; chuyện tranh cãi để ngỏ.
- [ ] Đã dựng thử bằng clip giả và xóa clip thử.
