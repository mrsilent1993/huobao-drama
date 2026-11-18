# Chuẩn hình ảnh quân đội và cách viết prompt cho đúng thời

Rút ra từ bản cuối tập 11 (Rạch Gầm 1785, `../pov-nguoi-binh-thuong/tap-11-dan-duong-rach-gam-1785.md`): anh phải sửa ba lỗi sau khi quay thử bằng prompt gốc:
- Muse dựng quân Xiêm mặc quân phục kiểu châu Âu và đi tàu buồm cao nhiều cột.
- Ở clip 2, Muse lẫn người trao bạc với Anh Tư.
- Ở clip 5, Muse tự chèn cờ đỏ sao vàng hiện đại.

## 7 quy tắc viết prompt (áp dụng cho mọi tập)

1. **Mỗi phe có một đoạn "chuẩn hình ảnh" dùng chung cả tập**, gồm trang phục, thuyền hoặc vũ khí, và cờ, viết cụ thể và đúng năm. Đoạn này in vào file .md (khóa `visual` trong `_nguon.py`) và chép vào bối cảnh của mọi clip có phe đó.
2. **Mỗi phe nước ngoài phải kèm danh sách cấm bằng chữ in hoa**, vì Muse hay tự chèn hình mặc định: `Absolutely NO European uniforms, NO epaulettes, NO tall European sailing warships…`.
3. **Cảnh chỉ có một phe** (họp bí mật, mai phục) phải ghi `IMPORTANT STORY LOGIC: … The frame contains ONLY: … Absolutely NO …`. Clip có bối cảnh riêng thì dùng khóa `setting` của clip.
4. **Hai người trao đổi vật gì đó** (trao bạc, trao thư) phải tách rõ: ai là `The GIVER`, ai là `The RECEIVER`, mỗi người mặc gì, đứng trái hay phải, ai làm hành động nào. Thêm câu "a completely different man" để Muse không gộp hai người làm một.
5. **Cờ:**
   - Mọi prompt đã có sẵn câu cấm cờ hiện đại (hằng `POV` trong `tools/series.py`).
   - Cảnh cần cờ thì tả đúng cờ của thời đó.
   - Cảnh cao trào nhiều thuyền, nhiều quân (Muse dễ chèn cờ nhất) thì ghi `ABSOLUTELY NO FLAGS OF ANY KIND`, phân biệt hai phe bằng áo và thuyền.
6. **Không có chữ trên áo, trên cờ, trên biển hiệu** (`no visible writing`): Muse viết chữ Hán, chữ Nôm sai hoặc vô nghĩa.
7. **Quay xong mà phải sửa prompt** thì lưu lại bản cuối đúng như đã dùng, rồi đặt `md_frozen=True` cho tập đó để bộ sinh không ghi đè.

## Chuẩn từng quân đội

Mức kiểm chứng:
- ✅ **đã kiểm chứng:** anh đã tra và dùng khi quay.
- ⚠️ **hiểu biết chung:** chưa kiểm chứng, nên tra lại trước khi quay. Đợt tìm nguồn ngày 18/11/2026 không tìm được tư liệu trực tuyến mô tả quân phục Tây Sơn hay lính Lục doanh nhà Thanh thập niên 1780.

### Quân Xiêm năm 1785 (đầu triều Rattanakosin, vua Rama I) ✅

- **Lính:** áo vải bông đỏ, phần dưới quấn chong kraben.
- **Cấm vệ:** áo senakut đỏ, giữa ngực có mặt sư tử (kirtimukha), đai lụa, khăn quấn đầu.
- **Thuyền chiến:** thuyền sông dài, thấp, hẹp, nhiều tay chèo. Mỗi thuyền lớn gắn một khẩu pháo ở mũi (6–12 pound), mũi chạm khắc, đuôi thấp, nhiều nhất một cột buồm nhỏ cuốn buồm.
- **Cờ triều Chakri:** nền đỏ, giữa có bánh xe chakra trắng.
- **Cấm:** quân phục kiểu Âu (chỉ có sau cải tổ năm 1852), áo xanh viền vàng, cầu vai, huân chương, mũ cắm lông hay nạm ngọc, tàu buồm cao nhiều cột, hàng pháo hai bên mạn.

### Quân Tây Sơn (1771–1802) ⚠️

- **Đang dùng:** áo vải sẫm màu đỏ thẫm hoặc nâu, khăn quấn đầu đỏ, đi chân đất hoặc dép cỏ, răng nhuộm đen. Vũ khí là giáo, đao, khiên mây, súng hỏa mai. Thuyền nhỏ, nhanh.
- Đây là hình ảnh phổ biến trong tranh vẽ và phim đời sau, chưa có tư liệu cùng thời để đối chiếu. **Không đưa cờ hiệu Tây Sơn vào cảnh**, vì chưa có nguồn chắc về cờ.

### Quân Thanh năm 1788–1790 ⚠️

- **Lính:** cạo nửa đầu trước, tết đuôi sam dài. Áo vải dài quá gối màu sẫm (xanh lam hoặc nâu) mặc ngoài quần, ủng vải, nón tre hoặc nón dạ.
- **Quan:** triều phục nhà Thanh, ngực có miếng bổ tử thêu (không có chữ), mũ có quả đỉnh và lông công.
- **Cấm:** chữ "兵" hay "勇" trên ngực áo (Muse viết sai, và kiểu áo này có thể thuộc thời muộn hơn), quân phục kiểu Âu, súng kiểu hiện đại, cờ có chữ.

### Quân Nam Hán năm 938 ⚠️

- **Thuyền:** lâu thuyền gỗ nhiều tầng, cờ đỏ trơn.
- **Lính:** giáp vảy (lamellar) kiểu cuối thời Đường, mũ có miếng che gáy.
- **Cấm:** giáp tấm kiểu châu Âu, cờ có chữ, thuyền buồm kiểu Tây.

### Quân Lê, Trịnh và chúa Nguyễn (thế kỷ 18) ⚠️

- **Lính:** áo vải trơn sẫm màu, khăn quấn đầu, giáo, đao.
- **Quan:** áo thụng có bổ tử, mũ cánh chuồn.
- Không gán màu áo riêng cho từng phe khi chưa có nguồn. Phân biệt các phe bằng bối cảnh và vị trí (trong thành hay ngoài thành), không bằng màu áo.

### Thời Bắc thuộc: quan nhà Hán, Lương, Đường và dân Giao Chỉ ⚠️

- **Quan nhà Hán (thế kỷ 1–2):** áo rộng tay sẫm màu, thắt đai, đội mũ vải đen.
- **Quan nhà Lương (thế kỷ 6):** áo rộng tay, đội mũ sa đen.
- **Quan nhà Đường (thế kỷ 7–9):** áo cổ tròn có màu theo phẩm hàm (đỏ, lục, lam), đội mũ phốc đầu đen, đeo đai da. Lính mặc giáp vảy kiểu Đường.
- **Dân Giao Chỉ:** tóc cắt ngắn hoặc búi, răng nhuộm đen, chân đất, áo vải trơn quấn quanh người.
- **Cấm:** chữ trên sổ sách, biển và cuộn văn, cờ các loại, quần áo và giáp kiểu châu Âu.

## Cần làm

- Tra quân phục Tây Sơn và quân Thanh ở tư liệu bảo tàng (Bảo tàng Quang Trung, sách *Huangchao Liqi Tushi* năm 1766 của nhà Thanh) rồi đổi ⚠️ thành ✅.
