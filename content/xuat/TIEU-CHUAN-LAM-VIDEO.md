# Tiêu chuẩn làm video: kênh "POV - Một Ngày Ở Đại Việt"

Tổng hợp mọi quy tắc anh đã đặt ra và chỉnh qua từng video, cùng bài học từ số liệu và bình luận người xem (cập nhật 20/11/2026). Mọi kịch bản mới phải theo file này. Khi viết, điền theo `MAU-KICH-BAN.md`.

---

## 1. Công thức nội dung (video thắng)

Gốc từ video Bạch Đằng 938 "Cắm cọc cả buổi sáng" (1,7 triệu lượt xem, 43,6% xem hết, 14 nghìn lượt chia sẻ). Các video theo công thức này đạt tỷ lệ thích **4,7–5,1%**, gấp đôi video kể kiến thức thẳng (1,9–2,5%).

1. **Người thường bị giao một việc vô lý, không ai giải thích.** Cấp trên gạt đi, không giải thích, nên người xem tò mò đến cuối mới biết lý do. **Câu gạt mỗi tập phải khác nhau và hợp nhân vật, hợp việc** (từ 19/11/2026 không dùng lại "Không hỏi."), tốt nhất là tự nó đã buồn cười hoặc gài sẵn cho cú lật, ví dụ: "Có vữa thì đã chẳng cần mày." (thợ xây), "Vợ mày cũng phải đổi." (đổi tiền, gài cho cảnh vợ giấu hũ đồng), "Sáng mai mày sẽ cảm ơn nó." (nhúng rơm ướt). Không bắt buộc cảnh 1 nào cũng có câu gạt: có thể cho cấp trên bỏ đi luôn, trả lời lạc đề, hoặc chỉ nhìn.
2. **Nhân vật quen mặt: Anh Tư.**
   - Ngoại hình: sẹo ngang lông mày trái, răng cửa mẻ, da rám nắng, khoảng 30 tuổi.
   - **Diễn xuất (từ 19/11/2026):** tự nhiên, tiết chế như người thật trong phim tài liệu. Cái hài nằm ở câu thoại và tình huống, không nằm ở nét mặt. Mỗi clip Anh Tư cười **tối đa một lần**, không cười vào ống kính, không nhăn nhó quá đà. Thay "grins / laughs" bằng phản ứng nhỏ: thở dài, liếc nhìn, ngập ngừng, lắc đầu, nói nhỏ. Prompt gắn câu `ACTING` (xem `tu-hao-dai-viet/_nguon.py`) vào bối cảnh của mọi clip. Luôn dùng ảnh tham chiếu (prompt trong `bach-dang/README.md`).
   - Mỗi tập là một đời con cháu, hoặc cùng một người ở cùng thời.
3. **Mỗi clip đúng một câu chốt ngắn**, đủ để người xem gửi cho bạn bè.
4. **Vỡ lẽ ở clip cuối:**
   - Cảnh lớn kèm lời người dẫn chuyện nêu sự kiện thật.
   - Sau đó là **một câu chốt RIÊNG của tập**, nối lại một chi tiết trong chính tập đó. Ví dụ: "Em còn nợ ông ấy hai đồng", "Cấy ngược mà vẫn thắng".
5. **KHÔNG dùng lại câu "Ghi tên em vào sử nhé!"** (bỏ từ 19/11/2026 vì tập nào cũng lặp). Màn hình kết cũng bỏ dòng "Sử không ghi tên Anh Tư".
6. **Kết lửng và nối tập:**
   - Màn hình kết: "Follow để xem [tập hoặc mốc tiếp theo] →". Bản YouTube tự đổi "Follow" thành "Đăng ký".
   - Bình luận ghim nhắc tập trước, để người xem đi tìm cả loạt.

### Chất hài

- **Hài kiểu tỉnh bơ, có nhắc lại** (câu ở clip 1 quay lại ở clip cuối), nhắc chéo giữa các tập (ví dụ "cấm đập muỗi" xuất hiện lại ở tập khác).
- **Từ hiện đại** (KPI, ship, CV, đổi tên công ty, thẻ căn cước): **tối đa một từ mỗi tập**, đặt ở câu chốt hài. Người xem chia hai phe, phần đông đùa theo.
- **Câu đùa chỉ nhắm vào:** Anh Tư, việc vô lý, quan tham.
- **KHÔNG đùa về:**
  - Anh hùng dân tộc, vua chúa, thần Phật.
  - Dân tộc thiểu số.
  - Nước khác hoặc người nước khác (quân Xiêm, Thanh, Nguyên chỉ là bối cảnh, không bêu riếu).
  - Cái chết, chiến tranh.
- **Vua và danh nhân dựng trang trọng:** Nguyễn Huệ / Quang Trung, Lê Lợi… **chỉ xuất hiện từ phía sau hoặc từ xa**.

### Chọn đề tài

- **Ưu tiên:** công thức Anh Tư gắn với sự kiện hoặc địa danh nổi tiếng (dời đô 130K, ngựa trắng 79K).
- **Ưu tiên:** đề tài người xem xin trực tiếp (Quang Trung, rùa thần Hồ Gươm, Yết Kiêu, video dài hơn, "full bộ").
- **KHÔNG làm thêm biến thể của cùng một đề tài đã chạy** (hai video ăn theo Bạch Đằng 938 chỉ đạt khoảng 2%). Thay vào đó làm **video trả lời bình luận** để khai thác khách của video gốc.
- **Hạn chế:** video kể thẳng không có nhân vật. Loạt "Phía bên kia" chỉ đăng thỉnh thoảng.
- **Không làm livestream.**

---

## 2. Định dạng và độ dài

> **Từ 19/11/2026 (anh duyệt): TikTok 30–35 giây, YouTube 60–70 giây**, linh động theo từng video. Các tập làm trước ngày này giữ nguyên.

| Loại | Số clip Muse (10 giây/clip) | Bản YouTube | Bản TikTok |
|---|---|---|---|
| **Tập chuẩn (mới)** | **7** | **đủ 7 cảnh, khoảng 67 giây** (60–70) | **4 cảnh chính, giữ gần trọn từng cảnh, khoảng 35 giây** (30–35) |
| Tập ít cảnh, cảnh dài hơi | 6, có cảnh dài hơn 10 giây nếu Muse cho | 60–70 giây | 4 cảnh chính, 30–35 giây |
| Trận đánh dài (YouTube) + trailer (TikTok) | 18 + 3 | 3 phút (tự cắt còn 2:59,5 nếu cần) | trailer 30 giây, dẫn sang YouTube |
| Video giới thiệu loạt | 4, quay kiểu trailer | một bản dùng chung, khoảng 39 giây | |

- **Từ 20/11/2026 (anh duyệt): YouTube kể đủ mọi cảnh, TikTok kể ít cảnh hơn nhưng trọn vẹn** (kiểu "YouTube nội dung 1–8, TikTok nội dung 1–4"). Lý do: cắt mọi cảnh còn 5 giây làm mất khoảng 1/4 câu thoại (84/353 câu) và chuyển cảnh quá nhanh.
  - **YouTube:** đủ 7 clip (70 giây trừ 6 lần chuyển cảnh 0,4 giây = 67,6 giây). Muốn 8 cảnh thì khoảng 77 giây, vượt mốc 70 giây, chỉ làm khi anh duyệt.
  - **TikTok:** chọn **4 cảnh chính** bằng khóa `tiktok_canh=[...]` (thường: cảnh mở đầu, cảnh dẫn, cảnh có câu đáng gửi bạn bè, cảnh chốt). Công cụ tự cắt mỗi cảnh giữ gần trọn (từ 0,2 giây đến hết phụ đề cuối + 0,2 giây; cảnh cuối từ phụ đề đầu − 0,3 giây đến hết), cảnh khác bỏ ở TikTok. Ví dụ 9,7 + 9,5 + 9,5 + 7,3 − 1,2 = 34,8 giây.
  - **4 cảnh TikTok phải tự kể được câu chuyện:** đọc riêng 4 cảnh đó vẫn hiểu việc vô lý, cú lật và câu chốt.
- **Đoạn cắt linh động:** `tiktok=a-b` nhận mọi khoảng (ví dụ `2-7`, `4-10`), không chỉ `0-5`/`5-10`. Chọn sao cho câu chính nằm trọn trong khoảng cắt.
- **Kiểm tự động:** tập mới đặt `muc=MUC_MOI` (trong `tools/series.py`); khi chạy `_nguon.py` sẽ in thời lượng ước tính của từng bản và cảnh báo `⚠ NGOÀI KHOẢNG` nếu lệch.
- **Không cảnh nào trong 4 cảnh TikTok bị mất câu thoại** (kiểm bằng cách so phụ đề với khoảng cắt).
- **Kỹ thuật:** 1080x1920, 30 khung/giây, H.264 + AAC, âm lượng -14 LUFS.
- **Dựng bằng** `tools/tiktok.py`. Chỉ thử bằng clip giả rồi xóa ngay; **không bao giờ dùng clip Thermostat cũ**.

### Bố cục một clip 10 giây

- **0–5 giây:** hành động cận cảnh và câu lệnh (hoặc câu dẫn).
- **5–10 giây:** phản ứng và câu chốt.
- **Cảnh nào cũng phải hiểu được khi xem riêng**, vì bản TikTok chỉ lấy 4 cảnh.

---

## 3. Chữ trên video

- **Hook giây 0–2,5:** chữ to, dạng "POV: …", mỗi dòng **tối đa khoảng 20 ký tự**, tối đa 3 dòng, ngắt bằng " / ". Có thêm 2 hook dự phòng.
- **Nhãn 3 giây đầu:** "AI tái hiện · lời thoại hư cấu". Tập truyền thuyết dùng "AI tái hiện · theo truyền thuyết" (khóa `legend=True`). Nhãn riêng thì đặt khóa `nhan`, ví dụ "AI tái hiện · lời dụ theo truyền tụng".
- **Mốc thời gian** (nhãn góc trên, 3 giây đầu clip): ngắn, một dòng. Loạt dài ghi tên loạt, ví dụ "Tây Sơn từng mốc · 1773".
- **Phụ đề:**
  - Thời gian chuẩn 0,5–4,8 giây và 5,0–9,5 giây.
  - Mỗi dòng **tối đa khoảng 26 ký tự**. Ngắt tay bằng " / ", không để vỡ thành 4–5 dòng.
  - Kiểm bằng hàm `layout()` của `tools/tiktok.py`.
  - **Lời của nhân vật lịch sử thật** (vua, tướng) thì đặt tên người nói ở dòng đầu phụ đề, ví dụ "Vua Quang Trung: / Đánh cho để dài tóc!", vì nhãn góc trên chỉ hiện 3 giây đầu clip.
- **Màn hình kết:** 1,5–1,8 giây cuối (`end_giay`). Phụ đề cuối phải kết thúc trước lúc màn hình kết hiện.
- **Không dùng emoji trong chữ trên video:** chữ hiện thành ô vuông. Dùng "→".
- **Vùng an toàn:** chữ tránh khoảng 230px trên, khoảng 480px dưới và khoảng 160px bên phải (công cụ dựng đã tự xử lý).

---

## 4. Viết prompt Muse

### Cấu trúc prompt video

`[khối POV] [bối cảnh của tập hoặc của clip] [VOICES…] [nối cảnh nếu có] [diễn biến 0–5s / 5–10s] [mô tả cọc hoặc rồng nếu có] [Audio…]`

- **Khối POV** (tự chèn sẵn): góc nhìn thứ nhất, cầm máy ngang tầm mắt, dọc 9:16, không đồ hiện đại, không chữ trên màn hình, quy tắc an toàn trẻ em, **cấm cờ hiện đại**.
- **Ảnh khung đầu:** một câu tả đủ người, bối cảnh, ánh sáng, "realistic, vertical 9:16".
- **Tên file:** `tiền-tố-số.mp4`, ví dụ `ts1773-1.mp4`. Tiền tố riêng cho từng tập.

### 7 quy tắc hình ảnh (từ bản cuối tập 11 Rạch Gầm)

1. **Mỗi phe một đoạn "chuẩn hình ảnh" đúng năm** (trang phục, thuyền, vũ khí, cờ), in vào file .md bằng khóa `visual` và chép vào bối cảnh mọi clip có phe đó.
2. **Phe nước ngoài phải kèm danh sách cấm bằng chữ in hoa**, ví dụ "Absolutely NO European uniforms, NO tall European sailing warships…".
3. **Cảnh chỉ có một phe:** ghi "The frame contains ONLY … Absolutely NO …" (khóa `setting` riêng của clip).
4. **Hai người trao nhau vật gì:** tách rõ "The GIVER is … / The RECEIVER is Anh Tư…": mặc gì, đứng bên nào, ai làm gì.
5. **Cờ:**
   - Mọi prompt cấm cờ hiện đại; Muse từng tự chèn cờ đỏ sao vàng, 18 bình luận chê.
   - Cảnh cao trào đông người: "ABSOLUTELY NO FLAGS OF ANY KIND", phân biệt hai phe bằng áo và thuyền.
6. **Không có chữ** trên áo, cờ, biển, giấy tờ. Chữ bắt buộc phải có (bia đá, chiếu chỉ) thì để mờ, không đọc được.
7. **Prompt nào sửa sau khi quay:** lưu bản cuối và đặt `md_frozen=True` để không bị ghi đè.

### Chuẩn cụ thể (xem `nghien-cuu/chuan-hinh-anh-quan-doi.md`)

- **Quân Xiêm 1785 ✅** (anh đã kiểm chứng): áo đỏ, chong kraben; cấm vệ mặc áo senakut có mặt sư tử; thuyền sông dài và thấp, pháo ở mũi; không quân phục kiểu Âu.
- **Cọc Bạch Đằng:**
  - Cả thân cây lim dày 20–30 cm, dài 2,5–3 m (có cọc 37–40 cm, dài 3–4 m ở Cao Quỳ), nhiều người cùng đóng.
  - **Không que nhỏ, không búa tay.** Cọc năm 1288 khai quật không bịt sắt.
  - Công cụ tự chèn mô tả `STAKE_SPEC`.
- **Rồng thời Lý:** thân mảnh uốn khúc như rắn, đầu nhỏ, không sừng (`DRAGON_SPEC`). Tốt nhất không quay cận cảnh rồng.
- **Quân Thanh, Tây Sơn, Nguyên, Minh, Nam Hán, quan Hán–Đường:** mức ⚠️ hiểu biết chung. Không gán màu áo khi chưa có nguồn.

### Nối cảnh

- **Hai clip liền nhau cùng một cảnh:** đánh dấu `noi=True`.
- Clip sau dùng **khung cuối của clip trước** làm ảnh khung đầu (cắt bằng `tools/khung-cuoi.py`).
- Prompt clip sau có câu "Continue seamlessly from the previous shot…".

---

## 5. Giọng nói

- **Giọng vùng miền:**
  - Mặc định giọng Bắc (Hà Nội): người xem chê giọng Nam trong các trận ở miền Bắc.
  - Tập ở miền Trung, miền Nam ghi đè bằng khóa `giong`, ví dụ "Central Vietnamese (Bình Định) accent" cho các tập Tây Sơn.
- **Mỗi nhân vật một giọng cố định**, tự chèn vào prompt từng clip (bảng `VOICES` trong `tools/series.py`, chi tiết ở `nghien-cuu/giong-nhan-vat.md`, bản xuất `xuat/TIEU-CHUAN-GIONG-NOI.md`):
  - **Anh Tư:** nam khoảng 30 tuổi, sáng, hơi khàn, nói tự nhiên, hài kiểu tỉnh bơ, không gào.
  - **Người dẫn chuyện:** nam trầm, chậm, kiểu phim tài liệu, giống nhau ở mọi video.
  - **Viên chỉ huy:** cộc, ngắn gọn, khác hẳn giọng Anh Tư.
  - **Nhân vật riêng của tập:** khai báo bằng khóa `voices={"Tên": "mô tả"}`.
- **Âm thanh:** chỉ âm thanh tự nhiên, **không nhạc nền**. Trailer được dùng trống trận.
- **Nếu Muse có chọn giọng hoặc giọng tham chiếu:** dùng đúng một giọng cho mỗi nhân vật ở mọi clip.
- **Nhân vật lịch sử đọc lời nổi tiếng** (ví dụ vua Quang Trung đọc lời dụ):
  - Một giọng riêng, mô tả rõ và khác hẳn giọng Anh Tư và người dẫn chuyện (ví dụ `QT_VOICE`: trầm, vang, hùng hồn, giọng Bình Định, mỗi vế như một hồi trống). Tạo giọng một lần, dùng lại ở mọi clip người đó nói.
  - Prompt clip ghi "ONLY [tên] speaks… Anh Tư and the soldiers keep their mouths closed". Vì vua chỉ thấy từ phía sau, nếu Muse gán giọng cho gương mặt khác thì chọn bản không ai mấp máy môi.
  - Clip có lời nhân vật thật thì không để Anh Tư nói cùng lúc; người dẫn chuyện để sang clip khác.

---

## 6. Độ chính xác lịch sử

- **Mức nguồn ghi trong mọi tập:**
  - **A:** sử Việt và sử nước ngoài, hoặc khảo cổ, cùng xác nhận.
  - **B:** chính sử Việt (*Toàn thư*, sử nhà Nguyễn…).
  - **C:** truyền thuyết, giai thoại, tiểu thuyết lịch sử (ví dụ *Hoàng Lê nhất thống chí*).
- **Phần lịch sử của mỗi tập tách rõ:** sử chép (kèm nguồn), phần dựng lại, phần **hư cấu** (Anh Tư, lời thoại, chi tiết thêm).
- **Câu của nhân vật thật** lấy theo ý sử chép, ghi "phỏng theo", không nhận là nguyên văn.
- **Câu nói nổi tiếng phải đối chiếu văn bản gốc trước khi ghi nguồn.** Ví dụ: "Đánh cho để dài tóc…" thường được gán cho *Hoàng Lê nhất thống chí*, nhưng đọc lại hồi 14 thì sách không chép; lời dụ ở Nghệ An trong sách là "Trong khoảng vũ trụ, đất nào sao ấy…". Câu chưa thấy văn bản gốc ghi mức C (truyền tụng) và không nêu địa danh khi các nguồn ghi khác nhau.
- **Chuyện đang tranh luận** (ví dụ "vua giả" năm 1790): video để ngỏ, mời người xem bình chọn.
- **Số liệu:** tra trước khi viết, ghi khoảng giá trị nếu các nguồn lệch nhau. Không suy diễn quá nguồn; "nhiều người cùng làm" thì không khẳng định một cách đóng cọc cụ thể.
- **Phân biệt thời đại**, không ghép nhầm nhân vật (ví dụ Yết Kiêu thuộc thời Trần, không phải năm 1427).
- **Chuyện có cách gọi tranh cãi** (Tây Sơn bị sử nhà Nguyễn gọi là "giặc"): caption ghi "theo sử hiện đại".
- **Video đã đăng có lỗi:** sửa bản dùng về sau, ghim bình luận nhận lỗi, hoặc làm video trả lời.

---

## 7. An toàn và kiểm duyệt (bắt buộc)

Bảng kiểm đầy đủ theo nội quy TikTok, YouTube và luật Việt Nam: **`nghien-cuu/noi-quy-tiktok-youtube.md`**. Mỗi video phải qua 2 lần duyệt (kịch bản và bản dựng) của **Sử gia** và **Kiểm duyệt nội quy**; một trong hai chặn thì dừng.

- **Trẻ em:**
  - Không trẻ em cận cảnh, không thấy mặt, không khóc, không trong cảnh chiến tranh. Chỉ thấy từ phía sau hoặc từ xa.
  - **Không dựng chuyện hôn nhân hay tình cảm có người dưới 18 tuổi** (ví dụ Ngọc Hân năm 1786 mới 16 tuổi, nên không làm).
  - Nhân vật thiếu niên như Trần Quốc Toản thì không nhắc ở trận đánh.
  - (Video A3 từng bị TikTok gắn cờ an toàn trẻ em.)
- **Bạo lực:**
  - Không máu, không xác, không cảnh chết, hành quyết hay tự tử.
  - Cái chết chỉ nói bằng lời dẫn chuyện, khi thật cần.
  - Cầu sập, thuyền lật: không dựng người rơi xuống nước.
- **Đề tài nhạy cảm KHÔNG làm:**
  - Đánh Chiêm Thành: người Chăm nay là dân tộc thiểu số.
  - Các mốc hành quyết (năm 1777, năm 1802).
- **Danh nhân và nhân vật lịch sử gây tranh cãi** (ví dụ Nguyễn Ánh): giọng trung tính, không chế giễu.
- **Quốc kỳ:** không để cờ hiện đại xuất hiện, nhất là trên thuyền giặc.
- **Nhãn AI:**
  - TikTok bật "Nội dung do AI tạo".
  - YouTube mục "Nội dung bị thay đổi" chọn **Có**.
  - Video có nhãn "AI tái hiện" ở đầu.
- **Kiểm duyệt của TikTok:** tự hại, máu me, trẻ em, thù ghét, nhãn AI, thông tin sai: kiểm từng tập trước khi đăng.

---

## 8. Thông tin đăng (có sẵn trong mỗi file .md)

**TikTok:**
- Hook và 2 hook dự phòng.
- Tiêu đề.
- Mô tả: câu vô lý + bối cảnh sử + **câu hỏi kéo bình luận**.
- Hashtag: `#povlichsu #POV #lichsuvietnam #xuhuong #fyp` + hashtag của loạt + hashtag của tập.
- Bình luận ghim. Đăng xong ghim ngay.

**YouTube Shorts:**
- Tiêu đề tối đa 100 ký tự + `#Shorts`.
- Mô tả: thêm dòng "video do AI tạo, nhân vật và lời thoại hư cấu". Bỏ `#fyp #xuhuong`.
- **Thẻ:** viết có dấu, ngăn cách bằng dấu phẩy, không có dấu #.
- Bình luận ghim: đổi "Follow" thành "Đăng ký".

**Quy tắc chung:**
- **Tiêu đề và hook KHÔNG lộ cú lật ở cuối.**
- **Bình luận ghim là câu hỏi hoặc gợi ý, KHÔNG trả lời luôn câu hỏi ở caption.** Đáp án thì trả lời bằng video.
- **Đăng mỗi ngày một tập** theo thứ tự của loạt.
- Video giới thiệu loạt: ghim lên trang cá nhân; trên YouTube tạo danh sách phát.
- **Trailer trên TikTok dẫn sang YouTube** bằng biểu tượng YouTube ở trang cá nhân. Chỉ nhắc nhẹ trong bình luận ghim, không kêu gọi rời TikTok bằng lời trong video.
- **Video trả lời bình luận:** đăng bằng "Trả lời bằng video", kéo nhãn bình luận xuống giữa màn hình.

---

## 9. Chuyển cảnh khi dựng

- **Mặc định:** hòa hình và hòa tiếng 0,4 giây.
- **Đổi riêng từng chỗ nối:**
  - `fadeblack:0.8`: khi nhảy thời gian (đêm sang sáng, năm này sang năm khác).
  - `fadewhite:0.3`: trailer.
  - `fade:0.25`: giữa các cảnh hành động.
  - `cat`: cắt thẳng cho cú bất ngờ (phất cờ, tiếng hô).
- **Mỗi chỗ chuyển cảnh làm video ngắn đi đúng bằng thời lượng chuyển.** Thời lượng trong phiếu sản xuất đã trừ phần này.

---

## 10. Quy trình một video

1. **Chọn đề tài** (mục 1), tra nguồn, ghi mức nguồn.
2. **Viết vào `_nguon.py`** của loạt theo `MAU-KICH-BAN.md`: tình huống vô lý, 7 cảnh (YouTube 60–70 giây, TikTok 30–35 giây), câu chốt từng cảnh, câu chốt cuối riêng, đoạn cắt cho bản ngắn.
3. **Chạy `python3 _nguon.py`.** Kiểm chia dòng bằng `layout()`, dựng thử bằng clip giả rồi xóa.
4. **Xuất phiếu** bằng `python3 tools/xuat_phieu.py`, gửi anh file .md hoặc phiếu. Khi anh muốn chọn kiểu kể, làm **3 mẫu**, mỗi mẫu một kiểu (ví dụ: công thức Anh Tư cổ điển · nhật ký đếm ngày · cặp đôi hài), kèm gợi ý nên chọn mẫu nào.
5. **Anh tạo clip trên Muse** (chú ý nối cảnh, nghe lại giọng, xem lại cờ, chữ, trang phục), rồi gửi Drive.
6. **Dựng ra 2 bản**, kiểm thời lượng, chữ, âm lượng, rồi gửi anh.
7. **Đăng** theo mục 8. Sau 1–2 ngày, đọc bình luận và số liệu, đưa bài học mới vào file này.
