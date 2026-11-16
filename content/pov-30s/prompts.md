# POV lịch sử Việt Nam, bản 30 giây

Mỗi tập gồm **3 clip Muse, mỗi clip 10 giây, tổng 30 giây**, khung dọc 9:16, góc nhìn thứ nhất. Cấu trúc chung: clip 1 dựng tình huống, clip 2 đẩy lên, clip 3 chốt bằng cú bất ngờ hoặc khoảnh khắc lịch sử. Mốc thời gian, tiêu đề và dòng chữ kết do mình thêm ở hậu kỳ.

## Chuẩn TikTok

**Phần mình lo ở hậu kỳ** (`content/tools/tiktok.py`):
- Xuất 1080×1920, 30fps, H.264 kèm AAC 48kHz, âm lượng −14 LUFS theo mức TikTok.
- Chữ móc câu cỡ lớn trong 2,5 giây đầu, ví dụ "POV: Bạn là dân Hoa Lư ngày dời đô năm 1010".
- Phụ đề lời thoại chèn cứng vào hình, vì nhiều người lướt TikTok tắt tiếng.
- Mốc thời gian ở đầu mỗi cảnh và dòng chữ lịch sử ở 3 giây cuối.
- Mọi chữ nằm trong vùng an toàn: không lấn lên thanh tab ở trên, không đè caption và tên nhạc ở dưới, không bị cột nút tim, bình luận, chia sẻ bên phải che.
- Ảnh bìa xuất kèm (file `.jpg`) là khung hình có chữ móc câu.

**Phần cần lưu ý khi tạo trên Muse:**
- **Giây đầu tiên phải có chuyển động.** Clip 1 của mỗi tập đã viết để hành động bắt đầu ngay ở 0s, không mở bằng cảnh tĩnh, vì người xem lướt qua chỉ trong khoảng 1 giây.
- **Giữ chủ thể ở khoảng giữa khung hình.** Phần dưới cùng sẽ bị caption TikTok che, mép phải bị cột nút che.
- **Đừng để Muse tự chèn chữ hay phụ đề**, vì mình đã chèn ở hậu kỳ.
- Câu cuối mỗi tập là một câu chốt bất ngờ, để người xem muốn xem lại hoặc bình luận.

**Khi đăng:** dùng caption và hashtag gợi ý ở cuối mỗi tập. Nên dùng nhạc nền có sẵn trong thư viện TikTok, để âm lượng nhạc khoảng 10–15% cho không lấn lời thoại. Nhạc trong thư viện đã có bản quyền và còn giúp video được đề xuất nhiều hơn.

---

Khi dán vào Muse, thay `[POV]` bằng khối POV chung, `[Bối cảnh]` bằng khối bối cảnh của từng tập, và `[Âm thanh]` bằng khối âm thanh.

**Khối POV chung**
```
First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, the viewer's own hands sometimes visible at the bottom of the frame, live-action realistic, cinematic natural lighting, vertical 9:16. No modern objects.
```

**Khối âm thanh**
```
Audio: natural ambient sound, Vietnamese dialogue spoken naturally with lip sync, no background music.
```

---

## Tập 1: POV: Bạn là dân Hoa Lư ngày dời đô, năm 1010

**Lịch sử:** mùa thu năm 1010, vua Lý Thái Tổ dời đô từ Hoa Lư ra thành Đại La. *Chiếu dời đô* khen đất ấy "rộng mà bằng phẳng, cao mà thoáng". Tương truyền khi thuyền vua cập bến thì thấy rồng vàng bay lên, nên vua đổi tên thành **Thăng Long**.

**Bối cảnh**
```
Vietnam, Lý dynasty, autumn 1010. Commoners barefoot, men with very short cropped hair, black-lacquered teeth, brown and indigo homespun clothes; wooden river boats with bamboo sails; limestone mountains of Hoa Lư; the wide Red River.
```
Nhân vật: **Ông Ba hàng xóm**, đàn ông khoảng 50 tuổi, đầu cạo ngắn, râu lún phún, răng đen, hay cằn nhằn.

### Clip 1: Hoa Lư, sáng sớm
Ảnh khung đầu:
```
First-person view on a riverbank at Hoa Lư with towering limestone mountains, 1010, the viewer's hands carrying a woven basket of pots and a rolled sleeping mat toward wooden boats, villagers loading belongings, a grumpy man around 50 with cropped hair and black teeth carrying a chicken cage, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: Early morning at the Hoa Lư riverbank, limestone peaks behind; the viewer carries a basket of pots toward a crowded wooden boat; Ông Ba, a grumpy man around 50 with cropped hair, holding a chicken cage, complains: "Đang yên đang lành, vua lại bắt cả kinh thành dọn nhà!" 5-10s: The viewer steps onto the swaying boat, the chicken squawks and flaps out of the cage, Ông Ba scrambles after it. [Âm thanh]
```

### Clip 2: Trên sông, gần Đại La
Ảnh khung đầu:
```
First-person view from the bow of a wooden boat on the wide Red River, 1010, a fleet of boats ahead including a large royal boat with yellow banners, villagers on board pointing up at the sky, golden morning light through clouds, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: On the boat in a fleet following the royal boat with yellow banners; suddenly Ông Ba drops his chicken and points at the sky, shouting: "Rồng! Rồng vàng kìa!" 5-10s: The camera tilts up: a huge golden dragon rises out of the clouds above the river and soars into the sky; everyone on the boats kneels and gasps. [Âm thanh]
```

### Clip 3: Thành Đại La
Ảnh khung đầu:
```
First-person view standing in a crowd at the earthen walls of Đại La citadel on flat open land by the river, 1010, a royal herald in a dark robe reading from an unrolled yellow scroll, yellow banners, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: At the walls of Đại La, a royal herald unrolls a yellow scroll and announces: "Vua thấy rồng vàng bay lên, từ nay nơi này gọi là Thăng Long!" The crowd cheers. 5-10s: Ông Ba looks around at the wide flat land, nods approvingly and says to the viewer: "Đất rộng, bằng phẳng, lại cao ráo... thôi, ở luôn!" [Âm thanh]
```

**Đăng TikTok:**
```
Ông Ba cằn nhằn cả đường, tới nơi thì đòi ở luôn 😂 Năm 1010, vua Lý Thái Tổ dời đô từ Hoa Lư về Đại La và đặt tên là Thăng Long. Bạn có biết Chiếu dời đô khen đất này thế nào không? 👇
#thanglongnghinnam #povlichsu #POV #lichsuvietnam #thanglong #hanoi1010 #lythaito #xuhuong #fyp
```

---

## Tập 2: POV: Bạn là nghĩa quân của Hai Bà Trưng, năm 40

**Lịch sử:** năm 40, Trưng Trắc và Trưng Nhị dấy binh ở Mê Linh chống thái thú nhà Hán là Tô Định. Câu thề "một xin rửa sạch nước thù, hai xin dựng lại nghiệp xưa họ Hùng" được chép trong *Thiên Nam ngữ lục*. Tô Định thua chạy về nước. Sử Việt chép rằng ông ta cắt tóc, cạo râu để trốn. Hai Bà lấy lại 65 thành.

**Bối cảnh**
```
Vietnam, year 40 AD, Mê Linh. Ancient Lạc Việt villagers barefoot with hair tied in topknots, brown woven clothes, bronze spears, crossbows, bronze drums; two warrior queens in dark lacquered armor with yellow sashes riding war elephants; Han dynasty soldiers in red-black armor; earthen citadel walls.
```
Nhân vật: **Hai Bà Trưng** (cưỡi voi, giáp sẫm, khăn vàng). **Tô Định** là quan Hán béo, râu dài, áo quan đỏ.

### Clip 1: Mê Linh, lễ thề
Ảnh khung đầu:
```
First-person view in a huge crowd of ancient Lạc Việt villagers holding bronze spears, year 40 AD, looking up at two warrior queens in dark armor with yellow sashes on war elephants, bronze drums, misty morning, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: Bronze drums boom; on a war elephant, the elder warrior queen Trưng Trắc raises her sword over the crowd and cries: "Một xin rửa sạch nước thù, hai xin dựng lại nghiệp xưa họ Hùng!" 5-10s: The viewer raises a bronze spear with thousands of villagers, roaring; a neighbor hands the viewer a crossbow. [Âm thanh]
```

### Clip 2: Đánh thành Luy Lâu
Ảnh khung đầu:
```
First-person view running toward an earthen citadel wall with a crossbow in hand, year 40 AD, war elephants charging alongside, arrows in the air, Han soldiers in red-black armor on the wall, dust and smoke, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: The viewer charges with the rebel army toward the citadel wall, war elephants smash into the wooden gate, Trưng Nhị on her elephant shouts: "Phá cổng! Tiến lên!" 5-10s: The gate collapses, Han soldiers drop their weapons and flee; the viewer runs through the gate into the citadel. [Âm thanh]
```

### Clip 3: Bụi rậm sau thành
Ảnh khung đầu:
```
First-person view pushing aside bushes behind a citadel, year 40 AD, revealing a fat Han official with half his long beard shaved off, holding a bronze knife, wearing a peasant's brown shirt over a red official robe, frozen in panic, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: The viewer pushes aside bushes behind the citadel and finds a fat Han official hastily shaving off his long beard with a knife, a peasant shirt half pulled over his red robe; he freezes and says nervously: "Ta... ta chỉ là dân thường thôi!" 5-10s: He drops the knife, hitches up his robe and sprints away into the forest; the viewer looks down at his fallen official seal on the ground. [Âm thanh]
```

**Đăng TikTok:**
```
Thái thú nhà Hán cạo râu giả làm dân thường để trốn 😳 Năm 40, Hai Bà Trưng khởi nghĩa ở Mê Linh, đánh đuổi Tô Định và lấy lại 65 thành. Bạn có thuộc lời thề của Hai Bà không? 👇
#povlichsu #POV #haibatrung #lichsuvietnam #phunuvietnam #xuhuong #fyp
```

---

## Tập 3: POV: Bạn là sĩ tử đi thi Hương, Nam Định 1897

**Lịch sử:** trường thi Nam Định là trường thi Hương lớn nhất Bắc Kỳ. Sĩ tử tự mang **lều chõng** vào trường, dựng lều giữa bãi để làm bài. Khoa thi năm Đinh Dậu 1897 được Tú Xương tả trong bài *Vịnh khoa thi Hương*, có các câu "Lôi thôi sĩ tử vai đeo lọ, ậm ọe quan trường miệng thét loa" và "lọng cắm rợp trời quan sứ đến, váy lê quét đất mụ đầm ra". Tú Xương thi tám lần, chỉ đỗ tú tài.

**Bối cảnh**
```
Vietnam, Nguyễn dynasty, Nam Định examination field, autumn 1897, French colonial era. Scholar candidates in long dark áo the and black turbans, carrying folded tent cloths, bamboo cots, bamboo tubes and ink pots on their shoulders; mandarins in blue and red robes shouting through tin megaphones; a French official under parasols with a European lady in a long trailing skirt.
```
Nhân vật: **Cụ đồ già**, sĩ tử khoảng 60 tuổi, râu bạc, áo the sờn, rất bình thản.

### Clip 1: Cổng trường thi, sáng sớm
Ảnh khung đầu:
```
First-person view in a crowd of scholar candidates in dark áo the and black turbans at the gate of Nam Định examination field, 1897, the viewer's shoulders loaded with a bamboo cot and tent cloth, a mandarin shouting through a tin megaphone, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: Dawn at the crowded gate; a mandarin in a blue robe shouts through a tin megaphone: "Sĩ tử xếp hàng khám xét! Ai giấu sách vào trường thì đuổi ra!" A guard pulls a tiny cheat sheet from a candidate's turban next to the viewer. 5-10s: Parasols part as a French official and a European lady in a long trailing skirt walk past, the skirt sweeping the dirt; the candidates stare. [Âm thanh]
```

### Clip 2: Trong trường thi
Ảnh khung đầu:
```
First-person view sitting on a bamboo cot inside a small cloth tent in a huge field of identical tents, 1897, the viewer's hand holding a brush over paper with an ink stone beside it, grey sky, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: Inside a small cloth tent among hundreds of tents; the viewer writes carefully with a brush; in the next tent the old scholar with a white beard leans over and whispers: "Viết chậm thôi cháu, mực nhòe là hỏng cả khoa." 5-10s: Rain starts drumming on the tent, water drips onto the paper, the viewer frantically covers the page with their sleeve. [Âm thanh]
```

### Clip 3: Ngày yết bảng
Ảnh khung đầu:
```
First-person view standing in a crowd in front of a large results board with names written in Chinese characters, 1897, the viewer's finger running down the list, the old white-bearded scholar beside him, realistic, vertical 9:16.
```
Video:
```
[POV] [Bối cảnh] 0-5s: In front of the results board, the viewer's finger runs down the list of names and stops at the bottom, nothing; the old white-bearded scholar beside him pats his shoulder and says calmly: "Năm nay là lần thứ chín của ông đấy, cháu ạ. Ba năm nữa ta lại đi." 5-10s: The old man shoulders his bamboo cot and walks off whistling; the viewer looks at their own ink-stained hands and laughs. [Âm thanh]
```

**Đăng TikTok:**
```
Thi trượt chưa buồn bằng gặp cụ đi thi lần thứ chín 😂 Năm 1897, trường thi Nam Định, đúng khoa thi Tú Xương tả trong bài "Vịnh khoa thi Hương". Bạn đã từng thi lại mấy lần? 👇
#povlichsu #POV #thihuong #tuxuong #lichsuvietnam #namdinh #xuhuong #fyp
```

---

## Dựng video (phần mình làm)

Bạn đặt tên file: `doido-1.mp4` … `doido-3.mp4`, `trung-1.mp4` … `trung-3.mp4`, `thi-1.mp4` … `thi-3.mp4`.

```
python3 ../tools/tiktok.py doi-do-1010.plan.txt doi-do-1010.mp4
python3 ../tools/tiktok.py hai-ba-trung.plan.txt hai-ba-trung.mp4
python3 ../tools/tiktok.py thi-huong-1897.plan.txt thi-huong-1897.mp4
```

Phụ đề trong file `.plan.txt` đang canh theo mốc giây ghi trong prompt. Nếu Muse cho nhân vật nói sớm hay muộn hơn, mình sẽ chỉnh lại mốc khi có clip thật.
