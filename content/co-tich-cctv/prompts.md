# Camera giám sát thời Văn Lang

Loạt clip ngắn theo trào lưu "camera giám sát thời cổ đại": nhân vật cổ tích Việt Nam bị camera chuông cửa ghi lại trong những tình huống rất đời thường hôm nay.

- Mỗi tập khoảng 30 giây, gồm 3 clip Muse dài 10 giây (A, B, C), khung dọc 9:16. A dựng tình huống, B đẩy lên, C là cao trào và câu chốt.
- Ba clip của một tập giữ **cùng góc máy, cùng bối cảnh**, để khi ghép trông như một đoạn camera quay liền.
- Lời thoại tiếng Việt, đặt trong ngoặc kép trong prompt.

## Quy trình

1. Tạo **ảnh khung đầu** của clip A bằng phần mềm ảnh (prompt bên dưới).
2. Đưa ảnh đó vào Muse (ảnh thành video) cùng **prompt video A**. Cách này giữ góc camera đứng yên tốt hơn chỉ dùng chữ.
3. Clip B: dùng **khung cuối của clip A** làm ảnh đầu vào nếu Muse cho phép. Nếu không, dùng lại ảnh khung đầu của A. Clip C làm tương tự, lấy khung cuối của B.
4. Đặt tên file kiểu `tap1-a.mp4`, `tap1-b.mp4`, `tap1-c.mp4`… rồi gửi cho mình. Mình sẽ ghép và phủ hiệu ứng camera (dòng ngày giờ, đồng hồ chạy, REC, méo ống kính, nhiễu hạt).

**Không cần** bảo Muse vẽ chữ, đồng hồ hay khung camera. Phần đó mình làm ở hậu kỳ, vì chữ do AI vẽ thường bị méo.

## Khối mô tả dùng chung

Mọi prompt đều bắt đầu bằng khối này. Muốn thêm tập mới thì giữ nguyên khối:

```
Real security doorbell camera footage, camera mounted high above the doorway looking steeply down, wide-angle fisheye lens, completely static camera with no movement, no cuts, live-action realistic, real actors in costume, natural flat daylight, slightly washed-out colors, vertical 9:16. Ancient Vietnamese Văn Lang era setting.
```

Âm thanh, thêm vào cuối mọi prompt video:

```
Audio: natural ambient sound only, no music, Vietnamese dialogue spoken naturally with lip sync, slightly tinny sound like a doorbell camera microphone.
```

---

## Tập 1: "Ai đến trước?" (Sơn Tinh – Thủy Tinh)

**Hậu kỳ:** dòng chữ `Hùng Vương thứ 18 · giờ Mão`, camera `CAM CỔNG CHÍNH`, đồng hồ bắt đầu `05:58:40`.

**Nhân vật:**
- **Sơn Tinh:** người đàn ông vạm vỡ khoảng 30 tuổi, da rám nắng, tóc búi cài lá rừng, mặc áo choàng xanh rêu thêu hình núi, vòng tay đồng.
- **Thủy Tinh:** người đàn ông gầy cao khoảng 30 tuổi, tóc dài ướt sũng, mặc áo choàng xanh biển thêu sóng nước, cổ đeo chuỗi vỏ ốc.

### Ảnh khung đầu A
```
[Khối mô tả dùng chung] Dawn, early morning mist. View from above the large wooden gate of King Hùng's palace: a wide packed-earth courtyard, thatched stilt-house palace roof edges, bronze drum decorations on the gate posts. Outside the gate, a muscular man in his 30s with tanned skin, hair in a topknot with forest leaves, moss-green cloak embroidered with mountain patterns and bronze bracelets (Sơn Tinh), standing proudly next to a real elephant with many tusks, a rooster and a horse with a red mane, all on ropes.
```

### Video A (10 giây)
```
[Khối mô tả dùng chung] Dawn mist outside the wooden gate of King Hùng's palace. 0-4s: Sơn Tinh, a muscular man with a leaf-crowned topknot and moss-green mountain-pattern cloak, leads an elephant with many tusks, a rooster and a red-maned horse to the gate, checks them off on a bamboo list. 4-10s: He leans close to the doorbell camera, grinning, and says: "Dạ con chào Vua Hùng! Voi chín ngà, gà chín cựa, ngựa chín hồng mao, đủ hết rồi nha. Con giao sớm cho chắc!" The gate creaks open and he leads the animals inside. [Âm thanh]
```

### Video B (10 giây)
```
[Khối mô tả dùng chung] Same gate, same camera angle, a few minutes later, the courtyard is empty, the gate closed. 0-4s: Water starts rushing into the frame and flooding the courtyard; a tall skinny man with long soaking-wet hair and a sea-blue wave-patterned cloak with a seashell necklace (Thủy Tinh) arrives riding a modern jet ski through the floodwater, holding a basket of fish and crabs. 4-7s: He looks up at the camera, out of breath, and says: "Ủa, mới sáu giờ mà?!" 7-10s: Inside the gate Sơn Tinh pokes his head out, waves at him smugly and says: "Đến sớm thì được vợ nha!" Thủy Tinh slaps the water angrily. [Âm thanh]
```

### Video C (10 giây)
```
[Khối mô tả dùng chung] Same gate, same camera angle, continuing. 0-4s: Thủy Tinh raises both arms and the floodwater surges higher, waves crashing against the gate; at the same time Sơn Tinh and a row of workers frantically shovel dirt and stack rocks along the gate, the ground rising like a small hill. 4-7s: The gate swings open and an elderly king with a long white beard and a feathered bronze crown, wearing a sleeping robe (Vua Hùng), steps out between them and shouts: "Hai đứa có thôi đi không, mới sáng sớm!" 7-10s: Both men freeze guiltily; a big wave splashes straight up onto the camera lens, the picture goes blurry with water droplets. [Âm thanh]
```

---

## Tập 2: "Đơn thứ ba trong ngày" (Thánh Gióng)

**Hậu kỳ:** dòng chữ `Làng Phù Đổng · giờ Ngọ`, camera `CAM CỬA TRƯỚC`, đồng hồ bắt đầu `11:47:05`.

**Nhân vật:**
- **Mẹ Gióng:** bà nông dân khoảng 60 tuổi, áo tứ thân nâu bạc màu, khăn mỏ quạ, người gầy, vẻ mệt mỏi.
- **Anh shipper:** thanh niên khoảng 25 tuổi, áo khoác giao hàng màu xanh lá không logo, mũ bảo hiểm, chạy xe máy cũ.

### Ảnh khung đầu A
```
[Khối mô tả dùng chung] Midday. View from above the bamboo door of a small thatched-roof peasant house in an ancient Vietnamese village, dirt yard, bamboo hedge, a clay water jar by the door. A young delivery man in a plain green delivery jacket with no logos and a helmet stands next to an old motorbike piled high with seven huge clay pots of steamed rice and woven baskets full of pickled eggplants.
```

### Video A (10 giây)
```
[Khối mô tả dùng chung] Midday, in front of the bamboo door of a thatched peasant house. 0-3s: A young delivery man in a plain green jacket with no logos and a helmet unloads seven huge clay pots of rice and baskets of pickled eggplant from an old motorbike onto the doorstep. 3-6s: An old peasant woman in a faded brown four-panel dress and black headscarf (Mẹ Gióng) opens the door. The delivery man says: "Bác ơi, đơn thứ ba hôm nay rồi. Nhà mình đông người hả bác?" 6-10s: She sighs tiredly and says: "Có một đứa thôi con." The delivery man stares at the mountain of food, confused. [Âm thanh]
```

### Video B (10 giây)
```
[Khối mô tả dùng chung] Same door, same camera angle, continuing. 0-4s: A gigantic child-sized hand, as big as a door, reaches out from inside the house and scoops up all the rice pots at once; the whole house shakes and dust falls from the thatched roof. 4-7s: A booming child's voice from inside says: "Mẹ ơi, con vẫn còn đói!" 7-10s: The delivery man freezes with his mouth open, slowly takes one step back toward his motorbike. [Âm thanh]
```

### Video C (10 giây)
```
[Khối mô tả dùng chung] Same door, same camera angle, continuing. 0-4s: The whole thatched house lifts and cracks as a giant boy stands up inside; two enormous bare legs, as tall as trees, step out into the yard right past the tiny delivery man, the ground shakes. 4-7s: The booming voice from above, out of frame, says: "Anh shipper ơi, còn đơn ngựa sắt với roi sắt nữa, giao giùm em luôn nha!" The delivery man drops his phone and runs away on foot, leaving his motorbike behind. 7-10s: The old woman walks into the middle of the yard, looks straight up at the camera and says tiredly: "Ba năm không nói câu nào, giờ nói toàn đặt đồ." [Âm thanh]
```

---

## Tập 3: "Một trăm quả trứng" (Lạc Long Quân – Âu Cơ)

**Hậu kỳ:** dòng chữ `Lạc Long Quân năm thứ nhất · giờ Thìn`, camera `CAM CỔNG`, đồng hồ bắt đầu `08:21:33`.

**Nhân vật:**
- **Âu Cơ:** người phụ nữ xinh đẹp khoảng 25 tuổi, tóc đen dài, váy trắng viền vàng, cài lông chim trên tóc.
- **Lạc Long Quân:** người đàn ông cao lớn khoảng 30 tuổi, tóc dài, áo giáp vảy rồng ánh xanh lục.
- **Chị shipper:** phụ nữ khoảng 30 tuổi, áo khoác giao hàng màu cam không logo, đạp xe ba gác.

### Ảnh khung đầu A
```
[Khối mô tả dùng chung] Morning, misty mountains in the background. View from above the wooden gate of a stilt house on a hillside, stone steps, flowering trees. A delivery woman in a plain orange delivery jacket with no logos stands next to a cargo tricycle stacked with a tall tower of egg cartons, holding a clipboard.
```

### Video A (10 giây)
```
[Khối mô tả dùng chung] Morning at the wooden gate of a hillside stilt house. 0-4s: A delivery woman in a plain orange jacket with no logos parks a cargo tricycle stacked with a tall wobbling tower of egg cartons and calls out: "Chị Âu Cơ ơi, đơn một trăm quả trứng, chị ký nhận giùm em!" 4-10s: A beautiful young woman with long black hair, a white dress with gold trim and a bird feather in her hair (Âu Cơ) opens the gate, stares at the tower of eggs and says: "Ủa, chị đâu có đặt?" [Âm thanh]
```

### Video B (10 giây)
```
[Khối mô tả dùng chung] Same gate, same camera angle, continuing. 0-6s: A tall man with long hair in shimmering green dragon-scale armor (Lạc Long Quân) appears behind Âu Cơ, scratching his head sheepishly, and says: "Anh đặt đó em. Lỡ sau này mình chia nhau, năm chục lên núi, năm chục xuống biển cho dễ." 6-10s: Âu Cơ slowly turns and gives him a long silent glare; the delivery woman awkwardly holds out the clipboard and pen. [Âm thanh]
```

### Video C (10 giây)
```
[Khối mô tả dùng chung] Same gate, same camera angle, continuing. 0-4s: The tower of egg cartons starts wobbling and glowing softly; the eggs crack open one after another and dozens of tiny babies tumble out, crawling all over the stone steps, babies giggling and crying. 4-7s: The delivery woman, surrounded by crawling babies, says nervously: "Dạ... vậy em tính thêm phí giao một trăm suất nha chị?" 7-10s: Lạc Long Quân quietly tiptoes backward toward the road; Âu Cơ grabs the back of his dragon-scale armor without looking and says: "Anh đứng lại đó!" [Âm thanh]
```

---

## Ghi chú

- Khi dán prompt vào Muse, **thay** `[Khối mô tả dùng chung]` và `[Âm thanh]` bằng nội dung hai khối ở trên.
- Nên thử một clip trước để xem Muse đọc tiếng Việt có tự nhiên không. Nếu giọng bị lơ lớ, có thể tắt thoại trong Muse rồi lồng tiếng sau, mình ghép âm thanh vào được.
- Muse có thể không vẽ đúng "voi chín ngà". Nếu voi chỉ có 2 ngà thì cũng vẫn buồn cười, vì lời thoại đã nói rõ.
- Muốn thêm tập? Gợi ý: Chử Đồng Tử trốn dưới cát khi công chúa Tiên Dung ghé bãi tắm; Mai An Tiêm nhận dưa hấu ship từ đảo; Tấm bị camera ghi lại cảnh cá bống "biến mất".

## Hậu kỳ (phần mình làm)

```
./cctv.sh "Hùng Vương thứ 18 · giờ Mão" "CAM CỔNG CHÍNH" 05:58:40 tap1.mp4 tap1-a.mp4 tap1-b.mp4 tap1-c.mp4
./cctv.sh "Làng Phù Đổng · giờ Ngọ" "CAM CỬA TRƯỚC" 11:47:05 tap2.mp4 tap2-a.mp4 tap2-b.mp4 tap2-c.mp4
./cctv.sh "Lạc Long Quân năm thứ nhất · giờ Thìn" "CAM CỔNG" 08:21:33 tap3.mp4 tap3-a.mp4 tap3-b.mp4 tap3-c.mp4
```
