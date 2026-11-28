# Bạch Đằng 1288, tập 8: Sông thành rừng (bản Seedance 2.0)

Viết theo skill `seedance-prompts-skill`. Dùng trên app **小云雀 (Xiaoyunque)** hoặc **即梦 (Jimeng)**: Tạo → Chế độ → **沉浸式短片 (Seedance 2.0)**, khung **9:16**.

- **Cảnh hoành tráng làm lại (theo skill `seedance-epic-fantasy-scifi`, mẫu tham khảo E2 trên goodcase.ai):** mỗi vật thể lớn có khối mô tả riêng (hạm đội, cọc lim, sông, thuyền nhẹ); độ lớn tả bằng **vật so sánh và số đo** (thuyền 30 m, mạn cao gấp 3 người, buồm 20 m, núi đá 200 m, sông rộng 600 m) và **góc máy thấp**, không dựa vào chữ "hoành tráng"; mỗi đoạn **chỉ một cảnh choáng ngợp**, viết rõ nguyên nhân và kết quả; cuối mỗi prompt có khối kỹ thuật và câu chốt khung hình cuối.
- **8 đoạn, tổng khoảng 1 phút 49 giây.** Seedance cho mỗi đoạn 4–15 giây, nên mỗi đoạn 10–15 giây, tối đa 2 câu thoại (theo công thức của skill: mỗi câu khoảng 1,3 giây + mỗi nhịp hình 0,8–1,5 giây).
- **Prompt viết bằng tiếng Trung** (Seedance hiểu tiếng Trung tốt nhất), **lời thoại giữ tiếng Việt** trong ngoặc kép, năm viết thành chữ.
- Mỗi câu thoại đặt đúng mốc giây của nó; khối 【声音】 chỉ mô tả giọng, nhạc, tiếng động, không chép lại lời.
- Câu đầu mỗi prompt là `画面无任何字幕。` (không chữ trên hình); phụ đề mình chèn khi dựng.
- Mô tả theo kiểu khẳng định ("画面中无…") thay vì "cấm…", để qua kiểm duyệt của Seedance.
- **Lưu ý:** Seedance mạnh nhất với tiếng Trung và tiếng Anh. Tiếng Việt có thể chưa tròn chữ. Anh thử đoạn 2 (chỉ Anh Tư nói) trước; nếu giọng chưa ổn thì để Seedance làm hình và tiếng động, em ghép giọng đọc tiếng Việt riêng khi dựng.

## 一、Ý chính

- **核心梗 (cú hook):** Cọc nhà em.
- **Một câu bán hàng:** Giặc hỏi "dưới sông mọc cái gì thế này?!" — Dạ, cọc nhà em ạ.
- **Mạch:** hạm đội Nguyên tự tin đuổi vào sông lúc triều lên → nước rút, cọc lim nhô lên trước mũi thuyền, giặc trở tay không kịp → quân Trần ba mặt đánh vào → thuyền lớn mắc cọc, càng lùi càng kẹt → cùng một ông quan sáng còn khoe "còn sợ cái gì", trưa đã hốt hoảng → hoàng hôn, cả khúc sông thành rừng cọc.
- **Lịch sử (mức A):** sáng 9/4/1288 (8/3 âm lịch Mậu Tý), hạm đội Ô Mã Nhi bị nhử vào sông lúc triều lên; triều rút, thuyền mắc cọc; Trần Hưng Đạo đánh từ thượng lưu, hai vua Trần đánh từ hai bên; *Nguyên sử* chép trận kéo dài từ giờ Mão đến giờ Dậu. Cọc 1288 không bịt sắt. Anh Tư, cai đội, quan Nguyên và mọi lời thoại là hư cấu.

## 二、Nhân vật

| Mã | Nhân vật | Hình | Giọng |
|---|---|---|---|
| C01 | **Anh Tư** | Ảnh mẫu `content/nhan-vat/anh_tu_ref.png` | Nam khoảng 30, ấm, hơi khàn, giọng Bắc (Hà Nội), nói thong thả, hài tỉnh bơ |
| C02 | **Quan Nguyên** (một người, xuất hiện 2 lần) | Cao, ngoài 40, ria mỏng, giáp lá đồng, mũ tròn tua đỏ | Nam ngoài 40, khàn, nói tiếng Việt hơi lơ lớ giọng nước ngoài; đoạn 1 tự tin, đoạn 6 hốt hoảng |
| C03 | **Cai đội** | Ngoài 40, mặt vuông, áo ngắn sẫm màu, đeo đao | Nam ngoài 40, gắt, câu ngắn, giọng Bắc |
| — | **Người dẫn chuyện** | Không xuất hiện | Nam trầm, chậm, kiểu phim tài liệu, giọng Bắc |

## 三、Tài sản cần tạo trước (ảnh tham chiếu)

Tạo bằng công cụ tạo ảnh (Nano Banana Pro, GPT-image…), mỗi ảnh một lần, dùng lại ở mọi đoạn. Tiền tố phong cách chung:
`电影级写实历史战争片剧照，真实摄影质感，胶片颗粒，自然光影，越南陈朝1288年，9:16竖屏，画面无任何文字`

### C01 — Anh Tư
Dùng thẳng ảnh `anh_tu_ref.png` (đã có). Mô tả để đối chiếu: 约30岁越南男子，皮肤黝黑，头顶小发髻，额头缠一条宽的褪色棕色布头巾，细胡须和短胡茬，牙齿染黑，眉边一道细疤，深棕色粗布长袖短衫系棕色布腰带，黑色宽裤，赤脚。

### C02 — Quan Nguyên
```
电影级写实历史战争片剧照，真实摄影质感，胶片颗粒，自然光影，9:16竖屏，画面无任何文字。元朝水军军官，四十多岁，身材高大，细长八字胡，面容精明，身穿铜片札甲，头戴红缨圆盔，腰挎长剑，站在木制战船船头，正面半身，背景江面晨雾，全身清晰。
```

### C03 — Cai đội
```
电影级写实历史战争片剧照，真实摄影质感，胶片颗粒，自然光影，9:16竖屏，画面无任何文字。越南陈朝什长，四十多岁，方脸，皮肤黝黑，头顶发髻，牙齿染黑，深色粗布短衫，腰佩长刀，神情严厉，站在小木船船头，正面半身。
```

### P01 — Cọc lim (dùng ở mọi đoạn có cọc)
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字。整根铁木树干削成的巨型木桩，粗如成年男子大腿（直径20至30厘米），长2.5至3米，去皮，顶端削成粗糙尖头，无铁尖，成排斜插在退潮后的江底泥滩上，比站在旁边的人还高，背景喀斯特石灰岩群峰。
```

### S01 — Sông Bạch Đằng lúc triều lên, hạm đội tiến vào
```
电影级写实历史战争片剧照，真实摄影质感，胶片颗粒，9:16竖屏，画面无任何文字，画面中无旗帜。清晨满潮的白藤江，江面宽阔，两岸高耸的喀斯特石灰岩群峰，金色晨雾，百余艘元军大型木制战船张满席帆，排成长长纵队逆流驶入，远处几只越南小轻舟在前方逃离，航拍远景。
```

### S02 — Bãi lau mai phục
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字。清晨江岸茂密高大的芦苇与红树林，薄雾，越南陈朝士兵手持弓箭长矛趴伏隐蔽在芦苇中，透过芦苇缝隙可见远处江面驶过的元军战船，前景芦苇虚化。
```

### S03 — Nước rút, cọc nhô lên trước mũi thuyền
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字，画面中无旗帜。上午的白藤江，潮水快速退去，岸边露出湿润泥滩，一排排巨大削尖铁木桩刚刚冲出水面，就在满帆元军战船的船头正前方，领头战船船底撞上木桩骤然停住，桅杆前倾，甲板上士兵踉跄抓住船舷。
```

### S04 — Quân Trần ba mặt đánh vào
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字，画面中无旗帜。宽阔江面大规模水战航拍：数百艘越南轻快小战船从上游和两岸同时高速冲出，船桨翻飞，两岸步兵从红树林中涌出，箭雨划过江面，远处山头一名深色长袍将领立于巨大战鼓旁（只见背影），江心元军巨舰卡在木桩间无法移动，硝烟飘过群峰。
```

### S05 — Giữa bãi cọc, thuyền giặc mắc kẹt
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字。退潮的木桩林中，一艘元军巨型战船被巨大铁木桩顶穿船底，船板开裂，桅杆倾斜，席帆撕裂，周围是浅水与泥滩，越南小船在四周环绕，近处一只小木船紧挨一根穿透船身的巨桩。
```

### S06 — Hoàng hôn trên sông
```
电影级写实历史战争片剧照，真实摄影质感，9:16竖屏，画面无任何文字。夕阳下的白藤江，天空燃烧般橙红，喀斯特群峰剪影，目力所及数百艘元军巨舰倾斜卡在木桩间，细细青烟升起，越南小船在其间平静穿行，一只小木船拴在一根木桩旁。
```

## 四、Kịch bản (định dạng △)

**8-1 Ngày · Ngoài · Sông Bạch Đằng lúc triều lên**
△ 【Cảnh mở】Quay từ trên cao, bay thấp theo hạm đội hơn trăm chiếc căng buồm tiến vào giữa núi đá, sương vàng.
Dẫn chuyện (vo): Ngày chín tháng tư năm 1288. Hạm đội Nguyên đuổi vào sông Bạch Đằng lúc triều lên.
△ Trung cảnh đẩy vào mũi thuyền đầu: quan Nguyên đứng trước gió, chĩa kiếm về thượng lưu, cười lớn.
Quan Nguyên (đắc ý): Thuyền nhỏ chạy hết rồi! Đuổi theo! Thuyền ta to thế này, còn sợ cái gì!

**8-2 Ngày · Ngoài · Bãi lau**
△ Qua khe lau (tiền cảnh mờ), hạm đội lướt qua phía xa.
△ Cận cảnh Anh Tư nằm sấp, con muỗi đậu lên mũi, anh lác mắt nhìn mà không nhúc nhích.
Anh Tư (thì thầm, tỉnh bơ): Muỗi đốt bốn mươi phát em không dám đập. Còn ông hỏi sợ cái gì à? Chờ nước rút, ông tự biết.

**8-3 Ngày · Ngoài · Sông Bạch Đằng, nước rút**
△ Bám theo hạm đội căng buồm trên mặt nước phẳng.
Dẫn chuyện (vo): Đoàn thuyền vẫn tiến vào, thì nước bắt đầu rút. Cọc lim nhô lên ngay trước mũi thuyền.
△ Máy sát mặt nước: mực nước tụt, đầu cọc lim phá mặt nước ngay trước mũi thuyền → thuyền đầu va cọc đánh rầm → cột buồm chúi tới → lính chao đảo bám mạn → thuyền sau đâm vào thuyền trước.

**8-4 Ngày · Ngoài · Bờ sông → toàn cảnh trận đánh**
△ Anh Tư bật dậy trên bờ, trố mắt nhìn ra sông.
Anh Tư (sửng sốt rồi khoái chí): Rút thật rồi! Mấy cái que em ôm không hết, giờ nhô lên chào giặc!
△ Lia nhanh lên đồi: trống trận nổ, lóe trắng → quay từ trên cao: hàng trăm thuyền nhẹ lao ra từ thượng lưu và hai bờ.
Dẫn chuyện (vo): Từ thượng lưu, Hưng Đạo vương đánh xuống. Hai vua Trần đem quân từ hai bên ập vào.

**8-5 Ngày · Ngoài · Thuyền xung phong**
△ Cận cảnh cai đội đứng mũi thuyền, quay lại hét.
Cai đội (gắt): Áp sát! Áp sát! Bắn vào buồm! Đừng bắn vào cọc, cọc nhà mình đấy!
△ Mưa tên bay về phía những cánh buồm.
△ Bám theo Anh Tư chèo ngang một chiếc thuyền khổng lồ mắc kẹt, vừa chèo vừa gật đầu vái.
Anh Tư (tỉnh bơ): Thuyền họ to như đình, giờ đứng im như đình thật. Em chèo ngang qua còn kịp vái một cái.

**8-6 Ngày · Ngoài · Giữa bãi cọc**
△ Góc thấp quay chậm: thuyền khổng lồ đè lên cọc, ván nứt, cột buồm nghiêng, buồm rách → toàn cảnh nhiều thuyền kẹt y như vậy.
Dẫn chuyện (vo): Hàng trăm thuyền lớn mắc cọc, vỡ ván, gãy buồm. Càng cố lùi ra, càng mắc chặt.
△ Trung cảnh: **cùng ông quan lúc sáng**, giờ bám chặt mạn thuyền nghiêng, hét xuống.
Quan Nguyên (hốt hoảng): Lùi lại! Lùi lại! Nước đâu hết rồi? Dưới sông này mọc cái gì thế này?!

**8-7 Ngày · Ngoài · Chân cọc**
△ Anh Tư trên thuyền nhỏ, hai tay ôm che cây cọc xuyên qua đáy thuyền giặc, ngước lên nhìn ông quan, lễ phép mà lo lắng.
Anh Tư (lễ phép, lo cho cọc): Dạ, cọc nhà em ạ. Cắm cả tuần đấy. Ông đứng yên cho, đừng giãy, giãy là gãy cọc em.

**8-8 Hoàng hôn · Ngoài · Sông Bạch Đằng**
△ 【Cảnh vắng】Quay từ trên cao, chậm: cả khúc sông đầy thuyền mắc kẹt dưới trời cam rực.
△ Anh Tư ngồi mũi thuyền nhỏ quay ra máy, ngón cái chỉ ngược ra sông, cười nhẹ.
Anh Tư (thong thả): Đánh từ sáng đến tối, sáng còn là sông, tối đã thành rừng cọc. Vợ hỏi cả tuần làm gì, em chỉ ra sông.

## 五、Prompt Seedance từng đoạn

Mỗi đoạn tạo riêng (cảnh đổi chỗ, không cần nối dài). Cột "Tải lên" là ảnh anh đính kèm theo đúng thứ tự @图片.

### Đoạn 1 · 15 giây · Hạm đội vào bẫy (cảnh hoành tráng: quy mô hạm đội)
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | S01 | Bối cảnh sông và hạm đội |
| 图片2 | C02 | Mặt và giáp quan Nguyên |

```
画面无任何字幕。

15秒，9:16竖屏，写实真人电影级历史战争大片，越南陈朝1288年白藤江，画面中无旗帜，画面中所有人物均安然无伤，无人落水。

【实体·元军舰队】百余艘元军大型木制战船，每艘船身长约三十米，船舷高出水面约五米，是站在甲板上的士兵身高的三倍；四面巨大的竹编席帆，每面帆高约二十米；船头包铁，船身深色木板。只提供船只外观与数量。
【实体·白藤江】江面宽约六百米，两岸是高约两百米的喀斯特石灰岩峭壁与红树林；木桩阵横贯整个江面，纵深约一百五十米。只提供环境与地理。
【实体·元朝军官】@图片2 中的元朝军官，四十多岁，细胡子，铜片札甲，红缨圆盔。只提供面容与服装。

【场景与气氛】清晨满潮，江面平静如镜，金色晨雾低悬，阳光从峭壁缝隙射出光束；用画面中的人、小渔舟和峭壁来交代尺度。

CUT 1（0-5秒）：机位贴近水面的超低角度，一只越南小渔舟停在画面左下角前景（虚化），一艘元军巨舰的船头从镜头上方缓缓压过，船舷遮住半个天空，浪花溅上镜头，鼓声低沉。

CUT 2（5-10秒）：无人机从水面急速拉升到峭壁顶端高度，揭示百余艘巨舰排成四列纵队铺满整个江面一直延伸到雾中，峭壁上的树木只有船帆的一半高，旁白（画外音，低沉缓慢）："Ngày chín tháng tư năm một nghìn hai trăm tám mươi tám. Hạm đội Nguyên đuổi vào sông Bạch Đằng lúc triều lên."

CUT 3（10-15秒）：领头战船船头，镜头由下往上仰拍，@图片2 的军官迎风而立，剑指上游，身后席帆被风吹满，元朝军官（得意洋洋，声音洪亮）："Thuyền nhỏ chạy hết rồi! Đuổi theo! Thuyền ta to thế này, còn sợ cái gì!"

【奇观】本段唯一的奇观是舰队的规模：先用一只小渔舟和一艘压过镜头的巨舰对比，再拉升揭示整个舰队，不加入战斗。

【声音】低沉管弦乐与远处战鼓渐强，配乐音量始终低于人声；巨帆鼓风声、木船吱嘎声、船头破浪声；旁白为低沉缓慢的越南语北部口音男声；军官为四十多岁沙哑男声，说越南语带轻微外国口音。

【技术】体积雾，晨光丁达尔光束，真实摄影级视觉特效，35毫米胶片颗粒，变形镜头轻微光晕，调色为深灰青与金色，写实电影质感。

【规则】@图片1 只用于江景构图，@图片2 只用于军官外观；军官面容全片一致；最后一帧稳定停在军官剑指上游、身后满帆舰队的仰拍画面，清晰不抖。
```
**Khung cuối:** góc thấp, quan Nguyên chĩa kiếm, sau lưng là cánh buồm căng và cả hạm đội.

### Đoạn 2 · 12 giây · Muỗi trong bãi lau
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | C01 | Mặt Anh Tư (`anh_tu_ref.png`) |
| 图片2 | S02 | Bãi lau |

```
画面无任何字幕。

电影级写实历史片，12秒，9:16竖屏，清晨薄雾，前景芦苇虚化，胶片颗粒，轻松幽默。

0-3秒：【空镜】透过芦苇缝隙，远处江面元军战船缓缓驶过，芦苇沙沙作响，蚊子嗡嗡声。

3-11秒：近景，@图片1 的男子（安四）趴伏在芦苇中一动不动，一只蚊子落在他鼻尖，他对眼盯着蚊子，身体纹丝不动，然后压低声音对镜头说，安四（耳语，平静冷幽默）："Muỗi đốt bốn mươi phát em không dám đập. Còn ông hỏi sợ cái gì à? Chờ nước rút, ông tự biết."

11-12秒：蚊子飞走，他轻轻眨眼，嘴角微动。

【声音】极轻的低音弦乐，蚊子嗡嗡声，芦苇声，远处战鼓；安四为约三十岁男声，温暖略沙哑，越南语北部河内口音，语速从容，冷幽默。

【参考】@图片1 锁定安四的脸、发髻、额头宽棕布头巾、染黑牙齿与深棕粗布衣，五官与图片完全一致；@图片2 仅用于芦苇场景氛围。
```
**Khung cuối:** cận mặt Anh Tư trong lau, muỗi vừa bay đi.

### Đoạn 3 · 15 giây · Nước rút, giặc trở tay không kịp (cảnh hoành tráng chính)
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | S03 | Cảnh nước rút, cọc trước mũi thuyền |
| 图片2 | P01 | Kích thước cọc lim |

```
画面无任何字幕。

15秒，9:16竖屏，写实真人电影级历史战争大片，越南陈朝1288年白藤江，画面中无旗帜，画面中所有人物均安然无伤，无人落水。

【实体·元军舰队】百余艘元军大型木制战船，每艘船身长约三十米，船舷高出水面约五米，是站在甲板上的士兵身高的三倍；四面巨大的竹编席帆，每面帆高约二十米；船头包铁，船身深色木板。只提供船只外观与数量。
【实体·铁木桩】每根木桩是一整根去皮铁木树干，粗如成年男子大腿（直径二十至三十厘米），长二点五至三米，顶端削成粗糙尖头，无铁尖；成排斜插江底，尖头朝向下游；退潮后露出水面的部分仍比站在旁边的人高。只提供木桩外观。
【实体·白藤江】江面宽约六百米，两岸是高约两百米的喀斯特石灰岩峭壁与红树林；木桩阵横贯整个江面，纵深约一百五十米。只提供环境与地理。

【地理】舰队四列纵队逆流前进；木桩阵就在领头战船正前方二十米处，满潮时完全隐藏在水下一米；两岸是泥滩与红树林。

【场景与气氛】上午，阳光斜照，潮水急速退去；用岸边泥滩上的小人和船舷上的士兵交代木桩与战船的尺度。

CUT 1（0-4秒）：低空跟拍满帆舰队在平静江面上前进，水面倒映席帆，旁白（画外音，低沉缓慢）："Đoàn thuyền vẫn tiến vào, thì nước bắt đầu rút."

CUT 2（4-9秒）：机位降到贴近水面，延时般的退潮：几秒内水位下降一米多，岸边泥滩快速露出，一排又一排如@图片2 的铁木桩尖头依次冲破水面，从近到远横贯整个江面，最近的一根就在镜头前方，比划过的一只小船还高，旁白："Cọc lim nhô lên ngay trước mũi thuyền."

CUT 3（9-15秒）：低角度慢镜头：领头战船船底撞上木桩，船身猛地一顿 → 桅杆向前猛甩，二十米高的席帆啪地鼓起又塌下 → 甲板上士兵整排踉跄，抓住绳索与船舷，探身往下惊望 → 后方第二艘巨舰来不及停下，船头撞上前船船尾，木屑飞溅 → 镜头拉高，整条纵队一艘接一艘被迫停住。

【奇观】本段唯一的奇观是"退潮露桩、巨舰撞停、后船追尾"这一条因果链，按顺序完整呈现。

【声音】管弦乐由平稳转为急促上扬，配乐音量始终低于人声；退潮水流声、木头撞击的沉闷巨响与碎裂声、甲板上的惊呼；旁白为低沉缓慢的越南语北部口音男声。

【技术】体积雾，晨光丁达尔光束，真实摄影级视觉特效，35毫米胶片颗粒，变形镜头轻微光晕，调色为深灰青与金色，写实电影质感。

【规则】@图片1 只用于构图与潮水状态，@图片2 只用于木桩粗细、长度与无铁尖的外形；每根木桩都是整根粗树干；最后一帧稳定停在一整列巨舰卡在木桩阵前的航拍画面，清晰不抖。
```
**Khung cuối:** cả một hàng thuyền lớn khựng lại trước rừng cọc, quay từ trên cao.

### Đoạn 4 · 15 giây · "Chào giặc!" và ba mặt đánh vào (cảnh hoành tráng: hợp vây)
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | C01 | Mặt Anh Tư |
| 图片2 | S04 | Toàn cảnh trận đánh |

```
画面无任何字幕。

15秒，9:16竖屏，写实真人电影级历史战争大片，越南陈朝1288年白藤江，画面中无旗帜，画面中所有人物均安然无伤，无人落水。

【实体·安四】@图片1 中的男子：头顶小发髻，额头宽棕布头巾，染黑牙齿，深棕粗布衣。只提供面容与服装。
【实体·陈朝轻舟】数百艘小型平底木船，每艘长约六米，坐六名划桨士兵，船身低矮，只到元军战船船舷的一半高度以下。只提供船只外观。
【实体·元军舰队】百余艘元军大型木制战船，每艘船身长约三十米，船舷高出水面约五米，是站在甲板上的士兵身高的三倍；四面巨大的竹编席帆，每面帆高约二十米；船头包铁，船身深色木板。只提供船只外观与数量。
【实体·将领与战鼓】远处一座高约八十米的山头，一名深色长袍将领只露背影，站在一面直径约两米的巨型战鼓旁。只提供剪影。

【地理】上游江湾在两公里外；两岸红树林各长约一公里；元军巨舰卡在江心木桩阵中。

CUT 1（0-5秒）：中景，@图片1 的安四在江岸芦苇边猛地站起，瞪大眼睛望向江面，随即露出得意的神情，安四（惊喜转为得意）："Rút thật rồi! Mấy cái que em ôm không hết, giờ nhô lên chào giặc!"

CUT 2（5-6秒）：甩镜到远处山头仰拍，将领背影与巨鼓剪影映在天空，鼓槌重重落下，画面白光一闪。

CUT 3（6-15秒）：无人机从山头高处向江心俯冲：数百艘陈朝轻舟同时从上游江湾和两岸红树林中冲出，船桨整齐翻飞，在江面上划出数百道白色航迹，像三支箭头从三个方向汇向江心；每艘轻舟只有巨舰的五分之一长；两岸步兵从红树林涌出到泥滩；一阵箭雨越过江面；旁白（画外音，低沉有力）："Từ thượng lưu, Hưng Đạo vương đánh xuống. Hai vua Trần đem quân từ hai bên ập vào."

【奇观】本段唯一的奇观是"三面合围"：数百条白色航迹从三个方向汇向被困巨舰，用航迹线条清楚呈现包围的形状。

【声音】一记震天战鼓后管弦乐与男声合唱全力爆发，配乐音量始终低于人声；数百支船桨击水、两岸呼喊声、箭矢破空声；安四为约三十岁温暖略沙哑男声，越南语北部河内口音；旁白为低沉的越南语北部口音男声。

【技术】体积雾，晨光丁达尔光束，真实摄影级视觉特效，35毫米胶片颗粒，变形镜头轻微光晕，调色为深灰青与金色，写实电影质感。

【规则】@图片1 只用于安四外观，面容与图片一致；将领只出现背影；最后一帧稳定停在三面航迹汇聚、包围江心巨舰的俯视航拍画面，清晰不抖。
```
**Khung cuối:** nhìn từ trên xuống, ba luồng vệt nước trắng xiết lại quanh đám thuyền lớn giữa sông.

### Đoạn 5 · 15 giây · "Đừng bắn vào cọc" và vái thuyền
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | C03 | Mặt cai đội |
| 图片2 | C01 | Mặt Anh Tư |
| 图片3 | S04 | Bối cảnh trận |

```
画面无任何字幕。

电影级写实历史战争片，15秒，9:16竖屏，硝烟，阳光穿透烟雾，胶片颗粒，画面中无旗帜，画面中人物均安然无伤。

0-6秒：近景，@图片1 的什长站在冲锋小船船头，回头挥刀指向敌船席帆，什长（严厉，大声下令）："Áp sát! Áp sát! Bắn vào buồm! Đừng bắn vào cọc, cọc nhà mình đấy!"

6-8秒：一阵箭雨划过天空射向巨大的席帆，帆布被穿透，箭矢破空声。

8-15秒：跟镜头，@图片2 的安四奋力划着小船经过一艘卡在木桩上的巨大战船，一边划一边恭敬地点头一拜，安四（一本正经的冷幽默）："Thuyền họ to như đình, giờ đứng im như đình thật. Em chèo ngang qua còn kịp vái một cái."

【声音】战鼓与管弦乐持续，配乐音量始终低于人声；船桨、箭雨、远处喊杀声；什长为四十多岁粗哑男声，越南语北部口音，短促有力；安四为约三十岁温暖略沙哑男声，越南语北部河内口音，语速从容。

【参考】@图片1 只用于什长的面容与衣着，不参考安四；@图片2 只用于安四的面容、头巾与衣着，不参考什长；@图片3 用于战场环境。
```
**Khung cuối:** Anh Tư chèo qua chiếc thuyền khổng lồ, vừa vái xong.

### Đoạn 6 · 15 giây · Càng lùi càng mắc (cảnh hoành tráng: thuyền khổng lồ trên cọc)
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | S05 | Thuyền mắc cọc |
| 图片2 | C02 | Mặt quan Nguyên |

```
画面无任何字幕。

15秒，9:16竖屏，写实真人电影级历史战争大片，越南陈朝1288年白藤江，画面中无旗帜，画面中所有人物均安然无伤，无人落水。

【实体·元军舰队】百余艘元军大型木制战船，每艘船身长约三十米，船舷高出水面约五米，是站在甲板上的士兵身高的三倍；四面巨大的竹编席帆，每面帆高约二十米；船头包铁，船身深色木板。只提供船只外观与数量。
【实体·铁木桩】每根木桩是一整根去皮铁木树干，粗如成年男子大腿（直径二十至三十厘米），长二点五至三米，顶端削成粗糙尖头，无铁尖；成排斜插江底，尖头朝向下游；退潮后露出水面的部分仍比站在旁边的人高。只提供木桩外观。
【实体·元朝军官】@图片2 中的同一位元朝军官，与第一段为同一人。只提供面容与服装。

【场景与气氛】退潮后的木桩阵中，浅水与泥滩，硝烟从江面飘过，阳光从烟中射出光束；用船舷上的士兵和船旁的小船交代巨舰的高度。

CUT 1（0-7秒）：机位在泥滩上贴地仰拍，一艘巨舰的船底压在三根铁木桩上，木桩穿透船板，裂缝沿船身向上延伸，船身随每次倒桨向后挣动一下，反而压得更深 → 桅杆缓缓倾斜，席帆撕开一道口子 → 镜头沿船身拉升到半空，揭示江面上几十艘巨舰以同样角度歪斜卡在木桩之间，像一片倒伏的森林，旁白（画外音，低沉缓慢）："Hàng trăm thuyền lớn mắc cọc, vỡ ván, gãy buồm. Càng cố lùi ra, càng mắc chặt."

CUT 2（7-15秒）：中景，@图片2 的军官紧抓倾斜十五度的船舷，脸色惊慌，朝下方大喊，元朝军官（惊慌失措）："Lùi lại! Lùi lại! Nước đâu hết rồi? Dưới sông này mọc cái gì thế này?!"

【奇观】本段唯一的奇观是"越挣越深"：每一次倒桨都让船压得更深，接着揭示整片被困的舰队。

【声音】低沉压迫的弦乐，木材呻吟与断裂声，水流从木桩间涌出声，配乐音量始终低于人声；旁白为低沉缓慢的越南语北部口音男声；军官为四十多岁沙哑男声，说越南语带轻微外国口音，惊慌但字字清楚。

【技术】体积雾，晨光丁达尔光束，真实摄影级视觉特效，35毫米胶片颗粒，变形镜头轻微光晕，调色为深灰青与金色，写实电影质感。

【规则】@图片1 只用于船只卡在木桩上的状态，@图片2 只用于军官外观，面容与第一段一致；最后一帧稳定停在军官紧抓船舷向下望的画面，清晰不抖。
```
**Khung cuối:** quan Nguyên bám mạn thuyền nghiêng, nhìn xuống.

### Đoạn 7 · 10 giây · "Dạ, cọc nhà em ạ"
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | C01 | Mặt Anh Tư |
| 图片2 | S05 | Thuyền mắc cọc, cây cọc xuyên đáy |

```
画面无任何字幕。

电影级写实历史片，10秒，9:16竖屏，硝烟中的柔和侧光，胶片颗粒，轻松幽默。

0-2秒：仰拍，一根巨大的铁木桩穿透战船船底，木屑与水滴落下。

2-10秒：中景，@图片1 的安四站在小木船上，双手护住那根巨桩，抬头望向上方船舷，表情礼貌又担心，安四（礼貌，担心自家木桩）："Dạ, cọc nhà em ạ. Cắm cả tuần đấy. Ông đứng yên cho, đừng giãy, giãy là gãy cọc em."

【声音】轻快俏皮的竹笛短句，木头吱嘎声，远处战斗声渐弱；安四为约三十岁温暖略沙哑男声，越南语北部河内口音，礼貌而从容。

【参考】@图片1 锁定安四的脸、头巾与衣着；@图片2 用于木桩穿透船身的画面。
```
**Khung cuối:** Anh Tư ôm cây cọc, ngước nhìn lên.

### Đoạn 8 · 12 giây · Hoàng hôn, câu chốt (cảnh hoành tráng: cả khúc sông thành rừng cọc)
| Tải lên | Mã | Dùng để |
|---|---|---|
| 图片1 | C01 | Mặt Anh Tư |
| 图片2 | S06 | Sông lúc hoàng hôn |

```
画面无任何字幕。

12秒，9:16竖屏，写实真人电影级历史战争大片，越南陈朝1288年白藤江，画面中无旗帜，画面中所有人物均安然无伤，无人落水。

【实体·元军舰队】百余艘元军大型木制战船，每艘船身长约三十米，船舷高出水面约五米，是站在甲板上的士兵身高的三倍；四面巨大的竹编席帆，每面帆高约二十米；船头包铁，船身深色木板。只提供船只外观与数量。
【实体·白藤江】江面宽约六百米，两岸是高约两百米的喀斯特石灰岩峭壁与红树林；木桩阵横贯整个江面，纵深约一百五十米。只提供环境与地理。
【实体·安四】@图片1 中的男子：头顶小发髻，额头宽棕布头巾，染黑牙齿，深棕粗布衣。只提供面容与服装。

【场景与气氛】夕阳贴着峭壁，天空橙红，江面金色；细细青烟从各处升起；用前景安四的四米长小木船交代远处巨舰的尺度。

CUT 1（0-4秒）：无人机从安四的小木船后方缓缓升高、越过他的头顶，一直升到峭壁之上，揭示三公里长的江面上数百艘巨舰歪斜卡在木桩之间，一直延伸到夕阳下的海口，青烟袅袅，陈朝轻舟在其间平静穿行。

CUT 2（4-12秒）：中景，@图片1 的安四坐在拴在木桩旁的小木船船头，转身面向镜头，竖起大拇指往身后满江搁浅的战船一指，嘴角微微一笑，安四（从容，带点得意）："Đánh từ sáng đến tối, sáng còn là sông, tối đã thành rừng cọc. Vợ hỏi cả tuần làm gì, em chỉ ra sông."

【奇观】本段唯一的奇观是从一只小船升起，揭示整条江的被困舰队。

【声音】竹笛主题旋律轻轻收尾，江水轻拍，海鸥声，配乐音量始终低于人声；安四为约三十岁温暖略沙哑男声，越南语北部河内口音。

【技术】黄金时刻逆光，体积雾，真实摄影级视觉特效，35毫米胶片颗粒，调色为橙金与深青，写实电影质感。

【规则】@图片1 只用于安四外观，面容与图片一致；最后一帧稳定停在安四竖拇指指向身后满江巨舰的中景，清晰不抖。
```
**Khung cuối:** Anh Tư ngồi mũi thuyền, ngón cái chỉ ra sông đầy thuyền kẹt.

## 六、Phụ đề khi dựng

| Đoạn | Thời gian | Phụ đề |
|---|---|---|
| 1 | 5–10s | Ngày chín tháng tư năm 1288. / Hạm đội Nguyên / đuổi vào sông Bạch Đằng / lúc triều lên. |
| 1 | 10–15s | Quan Nguyên: / Thuyền nhỏ chạy hết rồi! / Đuổi theo! / Thuyền ta to thế này, / còn sợ cái gì! |
| 2 | 3–11s | Muỗi đốt bốn mươi phát / em không dám đập. / Còn ông hỏi sợ cái gì à? / Chờ nước rút… / ông tự biết. |
| 3 | 0–9s | Đoàn thuyền vẫn tiến vào… / thì nước bắt đầu rút. / Cọc lim nhô lên / ngay trước mũi thuyền. |
| 4 | 0–5s | Rút thật rồi! / Mấy cái que / em ôm không hết… / giờ nhô lên chào giặc! |
| 4 | 6–15s | Từ thượng lưu, / Hưng Đạo vương đánh xuống. / Hai vua Trần / đem quân từ hai bên ập vào. |
| 5 | 0–6s | Cai đội: / Áp sát! Bắn vào buồm! / Đừng bắn vào cọc… / cọc nhà mình đấy! |
| 5 | 8–15s | Thuyền họ to như đình… / giờ đứng im như đình thật. / Em chèo ngang qua / còn kịp vái một cái. |
| 6 | 0–7s | Hàng trăm thuyền lớn / mắc cọc, vỡ ván, gãy buồm. / Càng cố lùi ra… / càng mắc chặt. |
| 6 | 7–15s | Quan Nguyên: / Lùi lại! Lùi lại! / Nước đâu hết rồi? / Dưới sông này / mọc cái gì thế này?! |
| 7 | 2–10s | Dạ… cọc nhà em ạ. / Cắm cả tuần đấy. / Ông đứng yên cho, / đừng giãy… / giãy là gãy cọc em. |
| 8 | 4–12s | Đánh từ sáng đến tối… / sáng còn là sông, / tối đã thành rừng cọc. / Vợ hỏi cả tuần làm gì… / em chỉ ra sông. |

**Hook:** `POV: Giặc hỏi dưới sông / mọc cái gì… / dạ, cọc nhà em` · **Kết:** `Follow để xem / Người từng đòi lên trời →`

Phần đăng TikTok, YouTube, Facebook dùng chung với bản Muse: `bd1288-tap8-song-thanh-rung.md`.
