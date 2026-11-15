# POV: Một ngày làm dân thường thời Trần

Video góc nhìn thứ nhất: người xem "là" một chàng trai nông dân 18 tuổi ở làng ven sông Hồng, cuối năm 1284. Đây là ngay trước cuộc kháng chiến chống Nguyên Mông lần thứ hai. Cả ngày là những việc rất đời thường, đến tối mới ngoặt sang lịch sử.

- **6 clip Muse, mỗi clip 10 giây, tổng 60 giây**, khung dọc 9:16.
- **Bản 30 giây:** mình cắt mỗi clip còn 5 giây đầu (`CLIP_SECONDS=5`). Vì vậy mỗi clip nên dồn hành động chính và câu thoại quan trọng nhất vào 5 giây đầu. Các prompt dưới đây đã viết theo cách đó.
- Mốc giờ, tiêu đề và dòng chữ kết do mình thêm ở hậu kỳ. Không cần bảo Muse vẽ chữ.

## Chi tiết lịch sử dùng trong video

Những chi tiết này có ghi chép hoặc được giới nghiên cứu thừa nhận, nên dùng chúng sẽ khiến video "đúng chất":

- **Ngoại hình:** đàn ông thời Trần thường cắt tóc rất ngắn hoặc cạo trọc. Cả nam lẫn nữ đi chân đất, **nhuộm răng đen** và **ăn trầu**. Sứ Nguyên Trần Phu tả lại điều này khi sang Đại Việt năm 1293.
- **Trang phục dân thường:** đàn ông mặc khố hoặc quần ngắn, áo cánh nâu. Phụ nữ mặc yếm, váy, tóc quấn khăn. Mọi thứ đều màu nâu, chàm, đất. **Tránh áo dài**, vì kiểu áo này ra đời muộn hơn nhiều.
- **Nhà ở:** nhà tranh vách đất, nền đất nện, chõng tre, chiếu cói, đèn dầu.
- **Đời sống:** cày bằng trâu, chợ phiên dùng tiền đồng có lỗ vuông, chùa chiền rất thịnh vì đạo Phật phát triển mạnh thời Trần.
- **Lịch sử:** Hội nghị Diên Hồng (cuối năm 1284), nơi các bô lão đồng thanh hô **"Đánh!"**. Binh sĩ thích lên tay hai chữ **"Sát Thát"** (殺韃, nghĩa là giết giặc Thát Đát).

Câu "răng trắng như răng chó" ở cảnh 3 là cách người xưa chê răng không nhuộm đen. Câu này có thật và rất gây cười với người xem hiện đại.

## Khối mô tả dùng chung

Đặt ở đầu mọi prompt video:

```
First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, the viewer's own hands and bare feet sometimes visible at the bottom of the frame, natural slight head movement, live-action realistic, cinematic natural lighting, vertical 9:16. Vietnam, Trần dynasty, year 1284, a farming village by the Red River. Historically accurate: commoners barefoot, men with very short cropped or shaved hair, everyone has black-lacquered teeth, simple brown and indigo homespun clothing, thatched mud-wall houses. No modern objects.
```

Đặt ở cuối mọi prompt video:

```
Audio: natural ambient sound, Vietnamese dialogue spoken naturally to the camera with lip sync, no background music.
```

Nhân vật xuất hiện nhiều lần (giữ nguyên mô tả):
- **Mẹ:** phụ nữ nông dân khoảng 45 tuổi, răng đen, đang nhai trầu, yếm nâu, váy đen, tóc quấn khăn chàm.
- **Chú Tư hàng xóm:** đàn ông khoảng 40 tuổi, đầu cạo trọc, răng đen, cởi trần, đóng khố, cười rất to.

---

## Cảnh 1: Giờ Dần, 4 giờ sáng

**Ảnh khung đầu**
```
First-person view lying on a straw mat on a bamboo bed inside a dark thatched mud-wall hut in 13th-century Vietnam, dim light from a small oil lamp, a woman in her 40s with black-lacquered teeth, brown bodice and indigo head wrap leaning over the viewer, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: Darkness, the viewer's eyes open on a straw mat in a thatched hut lit by a tiny oil lamp; the mother, a woman in her 40s with black teeth chewing betel, brown bodice and indigo head wrap, shakes the viewer's shoulder and says: "Dậy đi con, gà gáy ba lần rồi, ra đồng kẻo nắng!" 5-10s: The viewer sits up and looks down at their own rough, calloused hands and bare dusty feet; a rooster crows outside. [Âm thanh]
```

## Cảnh 2: Giờ Mão, 6 giờ sáng

**Ảnh khung đầu**
```
First-person view from behind a wooden plough in a flooded rice field at sunrise in 13th-century Vietnam, the viewer's own hands gripping the plough handle, a water buffalo pulling ahead, misty Red River countryside, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: Sunrise over flooded rice fields; the viewer struggles behind a wooden plough pulled by a water buffalo, knee-deep in mud, the buffalo stops and turns its head to look back. Next field over, a bald man around 40 with black teeth, shirtless in a loincloth (Chú Tư), laughs loudly and shouts: "Trâu nó kéo cày hay mày kéo trâu đấy hả?" 5-10s: The viewer slips and falls forward into the mud, the camera dips into muddy water and comes back up, Chú Tư laughing even harder. [Âm thanh]
```

## Cảnh 3: Giờ Ngọ, 12 giờ trưa

**Ảnh khung đầu**
```
First-person view sitting on a grassy rice-field dike at noon in 13th-century Vietnam, the viewer's hands holding a rice ball wrapped in a banana leaf, an old woman with black-lacquered teeth holding out a folded betel leaf quid toward the viewer, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: Noon on a rice-field dike, the viewer unwraps a rice ball in a banana leaf with a piece of braised fish; an old woman with black teeth leans in, offers a folded betel quid and says: "Ăn miếng trầu đi cháu, răng trắng như răng chó thì đứa nào nó lấy!" 5-10s: The viewer hesitantly takes it and chews; the old woman grins widely, showing shiny black teeth, and gives a thumbs-up. [Âm thanh]
```

## Cảnh 4: Giờ Mùi, 2 giờ chiều

**Ảnh khung đầu**
```
First-person view walking into a busy 13th-century Vietnamese village market under banyan trees, thatched stalls, baskets of rice, fish, chickens and pottery, barefoot villagers in brown clothing, a Buddhist monk in a brown robe in the background, the viewer's hand holding a string of square-holed copper coins, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: A crowded village market under a banyan tree; the viewer points at a chicken in a bamboo cage, a sharp-eyed woman vendor with black teeth crosses her arms and says: "Ba đồng một con, không bớt một xu!" The viewer counts square-holed copper coins on a string in their palm. 5-10s: A shuttlecock kicked by village kids flies past the viewer's face; a Buddhist monk in a brown robe walks by calmly, nodding. [Âm thanh]
```

## Cảnh 5: Giờ Dậu, 6 giờ tối

**Ảnh khung đầu**
```
First-person view standing in a crowd of barefoot villagers in front of a village communal house at sunset in 13th-century Vietnam, a royal messenger on a horse holding up a scroll, an old village elder with a white beard beside him, red sunset sky, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: Sunset, a drum beats; a royal messenger on horseback rides into the crowd of villagers in front of the communal house, an old white-bearded village elder unrolls a scroll and announces: "Giặc Nguyên sắp kéo sang! Bô lão cả nước về điện Diên Hồng, vua hỏi: đánh hay hòa?" 5-10s: The whole crowd, including Chú Tư and the viewer's own raised fist at the bottom of the frame, shouts together: "Đánh! Đánh!" [Âm thanh]
```

## Cảnh 6: Giờ Tuất, 8 giờ tối

**Ảnh khung đầu**
```
First-person view looking down at the viewer's own bare forearm resting on a wooden table at night, lit by oil lamps, a man holding a fine needle and a bowl of black ink about to tattoo, a line of young village men waiting in the background, 13th-century Vietnam, realistic, vertical 9:16.
```
**Video**
```
[Khối mô tả dùng chung] 0-5s: Night, oil lamps flicker; the viewer looks down at their own forearm on a wooden table while a man pricks two black Chinese characters into the skin with a needle and ink; Chú Tư, already tattooed, slaps the viewer's back and says: "Đau thì cắn răng, giặc đến thì đánh!" 5-10s: The viewer lifts the freshly tattooed arm up toward the camera; around them, a line of young village men raise their own tattooed arms in the lamplight, faces determined. [Âm thanh]
```

---

## Ghi chú

- Khi dán prompt vào Muse, thay `[Khối mô tả dùng chung]` và `[Âm thanh]` bằng nội dung hai khối ở trên.
- AI thường vẽ sai chữ Hán ở cảnh 6. Không sao, vì dòng chữ kết ở hậu kỳ sẽ giải thích rõ.
- Nếu Muse cho thêm ảnh tham chiếu nhân vật, hãy tạo ảnh Mẹ và Chú Tư trước để hai người không bị đổi mặt giữa các cảnh.
- Đặt tên file `tran-1.mp4` … `tran-6.mp4` rồi gửi mình link Drive.

## Hậu kỳ (phần mình làm)

Kế hoạch dựng nằm ở `plan.txt`:

```
./pov.sh plan.txt pov-thoi-tran-60s.mp4
CLIP_SECONDS=5 ./pov.sh plan.txt pov-thoi-tran-30s.mp4
```
