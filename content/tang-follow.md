# Tăng follow: kết lửng và trả lời bình luận bằng video

## 1. Kết lửng và mời follow

Mỗi video **không kể hết**. Dòng chữ kết ở 3 giây cuối gồm hai phần:

1. **Một câu hỏi bỏ lửng** về chính câu chuyện vừa xem, ví dụ "Tô Định cạo râu chạy về đâu?" hay "Ba năm nữa, cụ đồ có đỗ không?". Người xem sẽ vào bình luận đoán hoặc hỏi, và đó chính là tương tác TikTok cần.
2. **Lời mời follow nêu đúng vai của tập sau**, theo công thức "Follow để xem mai bạn làm [vai cụ thể] →". Nêu vai cụ thể (lính, thầy đồ, dân chài) hiệu quả hơn hẳn câu "theo dõi để xem thêm" chung chung.

Phần giải thích lịch sử đầy đủ để ở **caption**, không đặt trên hình. Người tò mò sẽ mở caption hoặc bình luận hỏi, và đó lại là dịp để trả lời bằng video.

Vì dòng chữ kết luôn nhắc tập kế tiếp, cần **đăng đúng thứ tự** dưới đây. Mỗi tập nói "mai" thì tập sau phải lên đúng ngày hôm sau:

| Chuỗi | Thứ tự đăng (mỗi ngày 1 tập) |
|---|---|
| Nhà giáo (gắn với 20/11) | Chu Văn An → Tết thầy → Bình dân học vụ → Học sinh 9x → Thầy giáo cắm bản (đúng 20/11) |
| Thăng Long nghìn năm | Phần 2 → 3 → 4 → 5 → 6. Phần 6 kết bằng "Comment 'phần 7'" để đo xem người xem có muốn loạt dài thêm không. |
| POV lịch sử | Hai Bà Trưng → Thi Hương → Bạch Đằng → Như Nguyệt → Hoàn Kiếm → Điện Biên → Bao cấp |

Nếu đăng hai chuỗi song song (ví dụ Nhà giáo buổi trưa, Thăng Long buổi tối), mỗi chuỗi vẫn giữ đúng thứ tự của nó.

## 2. Trả lời bình luận bằng video (15–30 phút mỗi ngày)

**Cách làm trên TikTok:** bấm vào bình luận, chọn biểu tượng quay video (Trả lời bằng video). TikTok sẽ tự gắn khung bình luận gốc lên video.

**Định dạng:** 10–20 giây, 1–2 clip Muse. Nhân vật **trả lời ngay trong vai**, như ông Ba hay anh lính, nhìn thẳng vào camera. Mình dựng bằng `tools/tiktok.py` nhưng **bỏ dòng mốc thời gian** ở góc trên, vì chỗ đó dành cho khung bình luận TikTok gắn vào. Kéo khung bình luận lên khoảng 1/3 trên màn hình, tránh che mặt nhân vật.

**Chọn bình luận nào để trả lời:**
- Câu hỏi "đứng về phe nào", ví dụ "Bạn sẽ đánh hay chạy?". Kiểu này dễ lên follow nhất vì người xem tranh luận bên dưới.
- Câu hỏi kiến thức mà caption đã gợi ra, ví dụ "Chiếu dời đô khen đất thế nào?".
- Bình luận đùa với nhân vật, ví dụ "Ông Ba khó tính quá".
- Bình luận bắt lỗi lịch sử, nếu bình luận đó đúng. Trả lời thật lòng, cảm ơn người góp ý, và bạn sẽ được tin tưởng hơn.

### Kịch bản trả lời sẵn

**Dùng chung cho mọi prompt bên dưới:**
```
First-person POV is NOT used here: medium close-up of the character looking straight into the camera and talking to the viewer, as if answering a question, static camera, live-action realistic, vertical 9:16, character centered in the lower two-thirds of the frame. Audio: Vietnamese dialogue with lip sync, natural ambient sound, no music.
```

**A. "Bạn sẽ đánh hay chạy?"** (cho các tập chiến trận: Hai Bà Trưng, Bạch Đằng, Như Nguyệt, Điện Biên)
```
Vietnam, year 1077, a soldier around 25 with short cropped hair, black-lacquered teeth, brown uniform and rattan shield on an earthen rampart at dawn, river and mist behind. 0-5s: He looks at the camera, smiles and says: "Đánh hay chạy à? Hồi đầu tôi cũng định chạy đấy." 5-10s: He grips his spear and says seriously: "Nhưng nhà tôi ở ngay sau con sông này. Chạy thì chạy đi đâu?" He turns back toward the river.
```
Phụ đề: `Đánh hay chạy à? Hồi đầu tôi cũng định chạy đấy.`, rồi `Nhưng nhà tôi ở ngay sau con sông này. / Chạy thì chạy đi đâu?`

**B. "Chiếu dời đô khen đất Đại La thế nào?"** (cho tập dời đô đã đăng)
```
Vietnam, 1010, a grumpy man about 50 with a round face, thick eyebrows, short cropped hair, sparse moustache, black-lacquered teeth and a big mole on his left cheek (Ông Ba), standing in front of wide flat land by a river, arms crossed. 0-5s: He says: "Chiếu dời đô bảo đất này rộng mà bằng phẳng, cao mà thoáng, dân khỏi lo ngập lụt." 5-10s: He sighs and adds: "Viết thì hay thế thôi, chứ khiêng đồ ra đây là tôi khổ!"
```
Phụ đề: `Chiếu dời đô bảo đất này rộng mà bằng phẳng, / cao mà thoáng, dân khỏi lo ngập lụt.`, rồi `Viết thì hay thế thôi, / chứ khiêng đồ ra đây là tôi khổ!`

**C. "Ông Ba khó tính quá"** (cho loạt Thăng Long)
```
Same Ông Ba as above, sitting on a low stool under a big banyan tree in 1010 Thăng Long, peeling a sugarcane stick. 0-5s: He looks up at the camera and says: "Khó tính à? Ai đắp thành ba lần sụt ba lần thì cũng khó tính thôi!" 5-10s: He points the sugarcane at the camera: "Mai xem phần tiếp, đời cháu tôi còn khổ hơn!"
```
Phụ đề: `Khó tính à? Ai đắp thành ba lần sụt ba lần / thì cũng khó tính thôi!`, rồi `Mai xem phần tiếp, đời cháu tôi còn khổ hơn!`

**D. "Rồng vàng có thật không?"**
```
Same Ông Ba as above, on a wooden boat on the Red River in 1010. 0-5s: He leans toward the camera and whispers: "Thật hay không thì tôi không biết. Nhưng hôm đấy cả thuyền quỳ hết." 5-10s: He points up at the sky and says: "Còn con gà nhà tôi thì sợ quá bay mất luôn!"
```
Phụ đề: `Thật hay không thì tôi không biết. / Nhưng hôm đấy cả thuyền quỳ hết.`, rồi `Còn con gà nhà tôi thì sợ quá bay mất luôn!`

Mẫu file kế hoạch dựng cho video trả lời (không có `hook`, không có mốc thời gian):
```
end: Follow để xem mai ông Ba / làm gì tiếp →
clip: reply-b-1.mp4 |
sub: 1 | 0.5-4.8 | Chiếu dời đô bảo đất này rộng mà bằng phẳng, / cao mà thoáng, dân khỏi lo ngập lụt.
sub: 1 | 5.0-9.8 | Viết thì hay thế thôi, / chứ khiêng đồ ra đây là tôi khổ!
```

**Duet và Ghép nối:** khi có video lịch sử khác đang lên xu hướng, bạn ghép nối (stitch) 3–5 giây đầu của video đó rồi nối clip "ông Ba phản ứng". Ví dụ ông Ba cằn nhằn: "Hồi tôi sống ở đấy không phải như thế đâu!" Bạn gửi link video gốc, mình viết lời phản ứng cho hợp.
