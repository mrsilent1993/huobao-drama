#!/usr/bin/env python3
"""Nguồn dữ liệu của loạt "Việt Nam thời xưa". Sửa nội dung ở đây rồi chạy:

    python3 _nguon.py

để sinh lại các file tap-*.md (prompt dán thẳng) và tap-*.plan.txt (chữ trên video).
"""
import os

POV = ("First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, "
       "the viewer's own hands sometimes visible at the bottom of the frame, live-action realistic, "
       "cinematic natural lighting, vertical 9:16. No modern objects, no on-screen text.")
AUDIO = "Audio: natural ambient sound, Vietnamese dialogue spoken naturally with lip sync, no background music."
TAGS = "#povlichsu #POV #lichsuvietnam #xuhuong #fyp"

EPISODES = [
    # ------------------------------------------------------------------ 1
    dict(
        slug="nguyen-hien", prefix="nh", title="Bạn chơi của Trạng nguyên 13 tuổi",
        length="30 giây · 3 clip (truyện ngắn, một cú chốt)",
        history=("**Lịch sử và truyền thuyết:** Nguyễn Hiền đỗ Trạng nguyên năm 1247 đời Trần, khi mới 13 tuổi, "
                 "là trạng nguyên trẻ nhất lịch sử khoa cử Việt Nam. Tương truyền khi sứ phương Bắc đố xâu chỉ qua "
                 "ruột ốc, Nguyễn Hiền đang chơi đã hát ngay lời giải: buộc chỉ vào lưng con kiến, bôi mỡ ở đầu bên kia "
                 "cho kiến bò qua. Tương truyền cậu còn đòi triều đình phải đón rước cho đúng lễ thì mới vào chầu."),
        setting=("Vietnam, Trần dynasty, year 1247, a village in Nam Định: rice fields, a dirt yard, bamboo hedges; "
                 "village kids barefoot in brown clothes with shaved heads and small tufts of hair; Nguyễn Hiền is a "
                 "skinny 13-year-old boy with a tuft of hair, bright clever eyes and a cheeky grin; a royal envoy in a "
                 "dark-red robe and black hat."),
        hook="POV: Bạn chơi thân / với Trạng nguyên 13 tuổi",
        end="Ăn xong, trạng có chịu vào triều? / Follow để xem mai bạn đi sứ / cùng trạng xấu nhất mà giỏi nhất →",
        clips=[
            dict(name="Đang thả diều thì quan đến", label="Làng quê Nam Định · 1247",
                 img="First-person view in a village yard in 13th-century Vietnam, a skinny 13-year-old boy with a tuft of hair flying a bamboo kite, a royal envoy in a dark-red robe walking up holding a spiral seashell and a long thread, other kids watching, realistic, vertical 9:16.",
                 vid="0-5s: The viewer holds the kite string next to Nguyễn Hiền, a skinny 13-year-old boy with a tuft of hair; a royal envoy in a dark-red robe hurries up holding a spiral seashell and a thread and says: \"Sứ Tàu đố xâu chỉ qua ruột ốc, cả triều chịu! Cậu bé có cách không?\" 5-10s: Without taking his eyes off the kite, the boy sings cheekily: \"Tang tình tang! Bắt con kiến càng, buộc chỉ ngang lưng, bôi mỡ đầu kia!\"",
                 subs=[(0.5, 4.8, "Sứ Tàu đố xâu chỉ qua ruột ốc, / cả triều chịu! Cậu bé có cách không?"),
                       (5.0, 9.8, "Tang tình tang! Bắt con kiến càng, / buộc chỉ ngang lưng, bôi mỡ đầu kia!")]),
            dict(name="Không đón đúng lễ thì không đi", label="Một tháng sau · thi đỗ Trạng nguyên",
                 img="First-person view in a village yard in 13th-century Vietnam, the same 13-year-old boy now in an oversized red scholar's robe with sleeves too long, arms crossed, refusing to step into a small palanquin, an envoy bowing, villagers watching, realistic, vertical 9:16.",
                 vid="0-5s: The boy, now in an oversized red Trạng nguyên robe with sleeves dragging on the ground, crosses his arms in front of a small palanquin and says: \"Vua mời con vào chầu thì phải sai quan đến đón cho đúng lễ chứ!\" 5-10s: The envoy wipes his sweat; the viewer whispers to the boy: \"Mày đỗ trạng rồi mà còn làm khó người ta à?\" The boy grins: \"Trạng thì phải ra dáng trạng.\"",
                 subs=[(0.5, 4.8, "Vua mời con vào chầu / thì phải sai quan đến đón cho đúng lễ chứ!"),
                       (5.0, 7.5, "Mày đỗ trạng rồi mà còn làm khó người ta à?"),
                       (7.5, 9.8, "Trạng thì phải ra dáng trạng.")]),
            dict(name="Mẹ gọi về ăn cơm", label="Chiều hôm ấy",
                 img="First-person view in a village yard at sunset in 13th-century Vietnam, the 13-year-old boy in a red scholar's robe climbing into a decorated palanquin with officials bowing, his mother in a brown dress standing at the gate with hands on her hips, realistic, vertical 9:16.",
                 vid="0-5s: Officials bow low as the boy in the oversized red robe climbs proudly into the decorated palanquin; drums play. 5-10s: His mother appears at the gate with hands on her hips and shouts: \"Hiền! Trạng gì thì trạng, ăn cơm xong rồi hẵng đi!\" The boy climbs straight back out, sleeves flapping, and runs home; the officials stare at each other.",
                 subs=[(5.0, 9.5, "Hiền! Trạng gì thì trạng, / ăn cơm xong rồi hẵng đi!")]),
        ],
        caption="Bạn thân đỗ Trạng nguyên năm 13 tuổi, giải câu đố của sứ Tàu trong lúc đang thả diều 😂 Nguyễn Hiền đỗ trạng năm 1247 đời Trần, là trạng nguyên trẻ nhất lịch sử Việt Nam. Năm 13 tuổi bạn đang làm gì? 👇",
        tags="#nguyenhien #trangnguyen #thandong #nhatran",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="mac-dinh-chi", prefix="mdc", title="Đi sứ cùng Mạc Đĩnh Chi",
        length="40 giây · 4 clip (hai lần đối đáp, cần thêm một nhịp)",
        history=("**Lịch sử và truyền thuyết:** Mạc Đĩnh Chi đỗ Trạng nguyên năm 1304 đời Trần. Ông thấp bé, "
                 "tướng mạo không đẹp, nhưng nổi tiếng tài ứng đối. Khi đi sứ nhà Nguyên, tương truyền ông đến cửa ải "
                 "muộn, quân canh đóng cửa và ra câu đối \"Quá quan trì, quan quan bế, nguyện quá khách quá quan\". Ông "
                 "đối lại \"Xuất đối dị, đối đối nan, thỉnh tiên sinh tiên đối\", và được mở cửa. Ở triều Nguyên, ông "
                 "nổi tiếng với câu đối \"Nguyệt cung tinh đạn, hoàng hôn xạ lạc kim ô\". Tương truyền ông được phong "
                 "\"Lưỡng quốc Trạng nguyên\" (trạng nguyên của hai nước)."),
        setting=("Vietnam and Yuan China, Trần dynasty, year 1308. Mạc Đĩnh Chi is a short, plain-looking Vietnamese "
                 "scholar-envoy around 28 with a calm, sharp gaze, wearing a dark blue envoy robe and black hat; "
                 "Vietnamese attendants in brown clothes carrying gift boxes; Yuan officials and guards in Mongol-Chinese "
                 "armor and robes; a massive stone border gate; a grand Yuan palace hall."),
        hook="POV: Bạn đi sứ cùng / trạng nguyên xấu nhất mà giỏi nhất",
        end="Vua Nguyên phong gì cho ông? / Follow để xem mai bạn làm gia nhân / bị Trạng Quỳnh lừa ăn \"mầm đá\" →",
        clips=[
            dict(name="Đến ải muộn", label="Cửa ải biên giới · chiều tối 1308",
                 img="First-person view at dusk in front of a massive closed stone border gate with Yuan guards on top holding torches, 1308, a short plain-looking Vietnamese envoy in a dark blue robe standing calmly in front, attendants with gift boxes behind, realistic, vertical 9:16.",
                 vid="0-5s: The viewer, an attendant carrying gift boxes, runs up to the massive gate as it slams shut; a Yuan guard on the wall shouts down a couplet: \"Quá quan trì, quan quan bế, nguyện quá khách quá quan!\" 5-10s: The viewer turns to the short envoy, Mạc Đĩnh Chi, and whispers in panic: \"Đối không được là tối nay mình ngủ ngoài ải đấy ông ơi!\" He just smiles calmly.",
                 subs=[(0.5, 4.8, "Quá quan trì, quan quan bế, / nguyện quá khách quá quan!"),
                       (5.0, 9.8, "Đối không được là tối nay / mình ngủ ngoài ải đấy ông ơi!")]),
            dict(name="Đối một câu, cửa mở", label="Vài giây sau",
                 img="First-person view at dusk below a massive stone gate, 1308, a short Vietnamese envoy in a dark blue robe looking up and speaking confidently, Yuan guards on the wall looking surprised, the gate starting to open, realistic, vertical 9:16.",
                 vid="0-5s: Mạc Đĩnh Chi looks up at the wall and answers clearly: \"Xuất đối dị, đối đối nan, thỉnh tiên sinh tiên đối!\" The guards look at each other, stunned. 5-10s: With a long creak the gate opens; the viewer picks up the gift boxes and hurries through, grinning: \"Em không hiểu gì, nhưng thấy bên kia im là mình thắng!\"",
                 subs=[(0.5, 4.8, "Xuất đối dị, đối đối nan, / thỉnh tiên sinh tiên đối!"),
                       (5.0, 9.8, "Em không hiểu gì, / nhưng thấy bên kia im là mình thắng!")]),
            dict(name="Triều Nguyên chê xấu", label="Kinh đô nhà Nguyên",
                 img="First-person view in a grand Yuan palace hall with red pillars and gold decorations, 1308, tall Yuan officials in rich robes smirking at a short plain Vietnamese envoy in a dark blue robe, Vietnamese attendants kneeling behind, realistic, vertical 9:16.",
                 vid="0-5s: In the grand hall, tall Yuan officials smirk at the short envoy; one says loudly, mocking: \"Sứ nước Nam bé thế này à?\" The viewer clenches the gift box angrily. 5-10s: A senior Yuan official raises a hand and challenges: \"Nhật hỏa vân yên, bạch đán thiêu tàn ngọc thố!\" The hall goes quiet; everyone looks at Mạc Đĩnh Chi.",
                 subs=[(0.5, 4.8, "Sứ nước Nam bé thế này à?"),
                       (5.0, 9.8, "Nhật hỏa vân yên, / bạch đán thiêu tàn ngọc thố!")]),
            dict(name="Câu đối chốt hạ", label="Một khắc sau",
                 img="First-person view in a Yuan palace hall, 1308, a short Vietnamese envoy in a dark blue robe standing tall and speaking, tall Yuan officials frozen with open mouths, the Yuan emperor on a golden throne leaning forward, realistic, vertical 9:16.",
                 vid="0-5s: Mạc Đĩnh Chi steps forward and answers without hesitation: \"Nguyệt cung tinh đạn, hoàng hôn xạ lạc kim ô!\" The Yuan officials freeze, mouths open; the emperor on the golden throne leans forward. 5-10s: The viewer, still kneeling, whispers proudly to the attendant beside him: \"Lúc nãy ai bảo sứ nước Nam bé nhỉ?\"",
                 subs=[(0.5, 4.8, "Nguyệt cung tinh đạn, / hoàng hôn xạ lạc kim ô!"),
                       (5.0, 9.8, "Lúc nãy ai bảo sứ nước Nam bé nhỉ?")]),
        ],
        caption="Bị đóng cửa ải, bị chê thấp bé, và hai câu đối làm cả triều Nguyên im lặng 😎 Tương truyền Mạc Đĩnh Chi được phong \"Lưỡng quốc Trạng nguyên\". Bạn có thuộc câu đối nào của ông không? 👇",
        tags="#macdinhchi #luongquoctrangnguyen #caudoi #nhatran",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug="trang-quynh-mam-da", prefix="tq", title="Gia nhân phủ chúa và món \"mầm đá\"",
        length="50 giây · 5 clip (truyện có nhiều bước, cú chốt là màn giải thích chữ)",
        history=("**Truyện dân gian:** chúa Trịnh ăn mãi sơn hào hải vị nên chán. Trạng Quỳnh hứa nấu món \"mầm đá\" "
                 "rất ngon, nhưng bắt chúa chờ suốt ngày trong lúc ninh đá. Đến khi chúa đói lả, Quỳnh dọn cơm với một "
                 "lọ tương đề hai chữ \"đại phong\". Chúa ăn ngon miệng, hỏi ra mới biết: \"đại phong\" là gió lớn, gió "
                 "lớn thì đổ chùa, đổ chùa thì tượng lọ (tượng lăn lóc), \"tượng lọ\" nói lái ra là \"tương lọ\". Ý là "
                 "đói thì ăn gì cũng ngon. Đây là truyện tiếu lâm dân gian, không phải sử chép."),
        setting=("Vietnam, Lê–Trịnh period, 18th century, the lord's palace (phủ chúa) in Thăng Long: a lavish dining "
                 "hall with lacquered red-and-gold furniture, a huge palace kitchen with clay stoves and big pots; Lord "
                 "Trịnh is a plump man around 45 in a rich yellow-brown silk robe and hat, bored and spoiled; Trạng Quỳnh "
                 "is a lean, witty scholar around 35 in a plain dark áo the with a mischievous smile; kitchen servants "
                 "in brown clothes."),
        hook="POV: Bạn làm gia nhân phủ chúa / ngày Trạng Quỳnh nấu \"mầm đá\"",
        end="Chúa có phạt Trạng Quỳnh không? / Follow để xem mai bạn theo học / thầy thuốc giỏi nhất nước Nam →",
        clips=[
            dict(name="Chúa chán ăn", label="Phủ chúa Trịnh · buổi sáng",
                 img="First-person view of a servant holding a tray in a lavish 18th-century Vietnamese palace dining hall, a plump bored lord in a silk robe pushing away a table full of dozens of fancy dishes, a lean witty scholar in a dark áo the standing nearby smiling, realistic, vertical 9:16.",
                 vid="0-5s: The plump lord pushes away a table covered with dozens of fancy dishes and sighs: \"Sơn hào hải vị ăn mãi chán rồi, có món gì lạ không?\" 5-10s: Trạng Quỳnh, a lean scholar in a dark áo the, bows with a sly smile: \"Bẩm chúa, thần biết nấu món mầm đá, ăn một lần nhớ cả đời.\"",
                 subs=[(0.5, 4.8, "Sơn hào hải vị ăn mãi chán rồi, / có món gì lạ không?"),
                       (5.0, 9.8, "Bẩm chúa, thần biết nấu món mầm đá, / ăn một lần nhớ cả đời.")]),
            dict(name="Ninh đá", label="Nhà bếp phủ chúa · giữa trưa",
                 img="First-person view in a huge 18th-century palace kitchen, the viewer's hands stirring a giant clay pot full of boiling water and round river stones, a lean scholar in a dark áo the fanning the fire calmly, smoke, realistic, vertical 9:16.",
                 vid="0-5s: The viewer stirs a giant pot of boiling water full of round river stones; Trạng Quỳnh calmly fans the fire. The viewer asks: \"Thầy ơi, đá này ninh đến bao giờ thì mềm ạ?\" 5-10s: Quỳnh answers without looking up: \"Đến khi chúa đói.\" The viewer blinks, looks at the stones, then at him.",
                 subs=[(0.5, 4.8, "Thầy ơi, đá này ninh đến bao giờ thì mềm ạ?"),
                       (6.0, 9.5, "Đến khi chúa đói.")]),
            dict(name="Chúa đói", label="Chiều tối",
                 img="First-person view at the door of a palace dining hall at dusk, a plump lord in a silk robe slumped on his chair holding his stomach, empty table, a servant peeking in, realistic, vertical 9:16.",
                 vid="0-5s: The plump lord slumps on his chair holding his stomach, which growls loudly; he groans: \"Mầm đá chín chưa? Ta đói lả rồi!\" 5-10s: Trạng Quỳnh whispers to the viewer: \"Dọn cơm lên, mang cái lọ này theo.\" He hands over a small clay jar with two Chinese characters painted on it.",
                 subs=[(0.5, 4.8, "Mầm đá chín chưa? Ta đói lả rồi!"),
                       (5.0, 9.5, "Dọn cơm lên, mang cái lọ này theo.")]),
            dict(name="Lọ \"đại phong\"", label="Bữa tối",
                 img="First-person view placing a small clay jar with two painted Chinese characters next to a bowl of plain white rice in front of a hungry plump lord in a silk robe, palace dining hall at night, oil lamps, realistic, vertical 9:16.",
                 vid="0-5s: The viewer sets a bowl of plain rice and the small clay jar of soybean sauce in front of the lord; he gobbles the rice dipped in the sauce, eyes closed in bliss: \"Ngon! Ngon quá! Lọ này là món gì?\" 5-10s: Trạng Quỳnh bows: \"Bẩm, là đại phong ạ.\" The lord frowns, confused, still chewing.",
                 subs=[(0.5, 4.8, "Ngon! Ngon quá! Lọ này là món gì?"),
                       (5.0, 9.8, "Bẩm, là \"đại phong\" ạ.")]),
            dict(name="Giải nghĩa", label="Một lúc sau",
                 img="First-person view in a palace dining hall at night, a lean scholar in a dark áo the explaining with his hands to a plump lord holding an empty rice bowl, the lord's face slowly realizing, servants hiding smiles, realistic, vertical 9:16.",
                 vid="0-5s: Trạng Quỳnh explains slowly, counting on his fingers: \"Đại phong là gió lớn. Gió lớn thì đổ chùa, đổ chùa thì tượng lọ. Tượng lọ... là tương lọ ạ.\" 5-10s: The lord stares at the empty jar, then at Quỳnh; the viewer, behind the pillar, covers his mouth to hold back laughter, shoulders shaking.",
                 subs=[(0.5, 6.0, "Đại phong là gió lớn. / Gió lớn thì đổ chùa, / đổ chùa thì tượng lọ. / Tượng lọ... là tương lọ ạ.")]),
        ],
        caption="Chúa chờ \"mầm đá\" cả ngày, đến tối ăn cơm với tương mà khen nức nở 😂 Đói thì ăn gì cũng ngon, Trạng Quỳnh dạy chúa đúng một bài. Bạn còn nhớ truyện Trạng Quỳnh nào nữa? 👇",
        tags="#trangquynh #mamda #truyendangian #tieulam",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        slug="hai-thuong-lan-ong", prefix="lo", title="Học trò của Hải Thượng Lãn Ông",
        length="40 giây · 4 clip (có một tình huống khó xử cần thêm nhịp)",
        history=("**Lịch sử:** Lê Hữu Trác, hiệu Hải Thượng Lãn Ông, là danh y thế kỷ 18, sống ở Hương Sơn (Hà Tĩnh). "
                 "Năm 1781 ông bị triệu về kinh chữa bệnh cho thế tử Trịnh Cán. Trong *Thượng kinh ký sự*, ông kể mình "
                 "từng nghĩ kê thuốc qua loa để được cho về sớm, nhưng lương tâm người thầy thuốc không cho phép, nên vẫn "
                 "kê đúng bài thuốc. Ông để lại câu nổi tiếng về y đức và bộ sách y học đồ sộ *Hải Thượng y tông tâm lĩnh*."),
        setting=("Vietnam, late Lê–Trịnh period, year 1781: first a quiet mountain home in Hương Sơn with medicinal herbs "
                 "drying on bamboo trays; then the lavish lord's palace in Thăng Long with lacquered pillars and silk "
                 "curtains. Hải Thượng Lãn Ông is a thin, dignified man around 60 with a long grey beard, plain brown "
                 "robe and a medicine bag; his student (the viewer) is a young man; palace officials in red and blue robes."),
        hook="POV: Bạn là học trò / của Hải Thượng Lãn Ông",
        end="Thế tử có khỏi bệnh không? / Follow để xem mai bạn hầu bếp / cho ông vua kén ăn nhất →",
        clips=[
            dict(name="Lệnh vào kinh", label="Hương Sơn · năm 1781",
                 img="First-person view in the yard of a quiet mountain house in 18th-century Vietnam, bamboo trays of medicinal herbs drying, a thin old physician with a long grey beard reading an official scroll, palace soldiers in uniforms waiting with horses, realistic, vertical 9:16.",
                 vid="0-5s: Soldiers wait with horses in the herb-drying yard; the old physician reads an official scroll and sighs; the viewer asks: \"Thầy ơi, phủ chúa gọi mình vào kinh thật ạ?\" 5-10s: The physician rolls up the scroll and says: \"Ta đã định ở núi làm ông già lười, giờ lại phải đi.\" The viewer looks at the long mountain road and groans.",
                 subs=[(0.5, 4.8, "Thầy ơi, phủ chúa gọi mình vào kinh thật ạ?"),
                       (5.0, 9.8, "Ta đã định ở núi làm ông già lười, / giờ lại phải đi.")]),
            dict(name="Vào phủ chúa", label="Phủ chúa Trịnh · Thăng Long",
                 img="First-person view walking through a lavish 18th-century palace corridor with lacquered red pillars and silk curtains, the old physician with a grey beard walking ahead carrying a medicine bag, officials in rich robes bowing, realistic, vertical 9:16.",
                 vid="0-5s: The viewer follows the old physician through endless gilded corridors and gates; the viewer whispers in awe: \"Qua chín lần cửa rồi thầy ạ, nhà gì mà to hơn cả làng mình!\" 5-10s: They reach a dim room where a pale, thin young prince lies on a silk bed surrounded by officials; the physician kneels to take his pulse, frowning.",
                 subs=[(0.5, 4.8, "Qua chín lần cửa rồi thầy ạ, / nhà gì mà to hơn cả làng mình!")]),
            dict(name="Kê thuốc nhạt?", label="Đêm hôm ấy",
                 img="First-person view at night in a small guest room in the palace, oil lamp, the old physician sitting at a low desk with a brush over a blank prescription paper, deep in thought, the student leaning in, realistic, vertical 9:16.",
                 vid="0-5s: By an oil lamp, the student leans in and whispers: \"Thầy kê thuốc nhạt nhạt thôi, chữa không khỏi người ta cho mình về núi!\" 5-10s: The old physician holds his brush still for a long moment, then shakes his head and says quietly: \"Ta học thuốc để cứu người, đâu phải để được về sớm.\"",
                 subs=[(0.5, 4.8, "Thầy kê thuốc nhạt nhạt thôi, / chữa không khỏi người ta cho mình về núi!"),
                       (5.0, 9.8, "Ta học thuốc để cứu người, / đâu phải để được về sớm.")]),
            dict(name="Bài thuốc thật", label="Sáng hôm sau",
                 img="First-person view in a palace room at morning, the old physician handing a written prescription to an official in a red robe, herbs laid out on a tray, the student watching proudly, realistic, vertical 9:16.",
                 vid="0-5s: The old physician hands a carefully written prescription to an official and says: \"Uống đúng thang này, ăn uống điều độ, bớt cao lương mỹ vị đi.\" The official looks shocked. 5-10s: The student whispers: \"Thầy bảo người trong phủ chúa ăn ít đi á?\" The physician smiles: \"Bệnh ở đây là do ăn nhiều quá.\"",
                 subs=[(0.5, 4.8, "Uống đúng thang này, ăn uống điều độ, / bớt cao lương mỹ vị đi."),
                       (5.0, 7.5, "Thầy bảo người trong phủ chúa ăn ít đi á?"),
                       (7.5, 9.8, "Bệnh ở đây là do ăn nhiều quá.")]),
        ],
        caption="Muốn về núi sớm, học trò xui thầy kê thuốc nhạt, và câu trả lời của Hải Thượng Lãn Ông 🙏 Năm 1781 ông vào phủ chúa chữa bệnh cho thế tử, chuyện được ông kể lại trong \"Thượng kinh ký sự\". Bạn có biết vì sao ông tự gọi mình là \"Lãn Ông\" (ông già lười) không? 👇",
        tags="#haithuonglanong #lehuutrac #yduc #thaythuoc",
    ),
    # ------------------------------------------------------------------ 5
    dict(
        slug="ngu-thien-tu-duc", prefix="nt", title="Hầu bếp cho vua Tự Đức",
        length="30 giây · 3 clip (một ngày trong cung, một cú chốt)",
        history=("**Lịch sử và giai thoại:** vua Tự Đức (trị vì 1847–1883) nổi tiếng kén ăn. Giai thoại kể mỗi bữa "
                 "vua dùng khoảng 50 món do 50 đầu bếp nấu, mỗi người một món. Vua thích uống trà ướp sen: chiều tối cung "
                 "nữ chèo thuyền ra hồ Tịnh Tâm thả trà vào bông sen, sáng sớm lấy trà ra và hứng sương đọng trên lá sen để "
                 "pha. Đây là giai thoại cung đình được kể lại nhiều, chi tiết có thể khác nhau tùy nguồn."),
        setting=("Vietnam, Nguyễn dynasty, Huế, around 1860: Tịnh Tâm lake at dawn covered with pink lotus flowers and "
                 "mist; the imperial kitchen with long rows of cooks at clay stoves; an imperial dining room with red-and-"
                 "gold lacquer. Palace maids in plain blue áo dài and turbans; cooks in white; Emperor Tự Đức is a thin, "
                 "pale, elegant man around 35 in a yellow imperial robe, seen from behind or from a distance."),
        hook="POV: Bạn làm cung nữ / hầu bếp cho vua Tự Đức",
        end="Món số 37 có được vua gắp không? / Follow để xem mai bạn đi hỏi vợ / bị nhà gái thách cưới →",
        clips=[
            dict(name="Hứng sương sen", label="Hồ Tịnh Tâm · 4 giờ sáng",
                 img="First-person view from a small wooden boat on a misty lotus lake at dawn in 19th-century Huế, the viewer's hands tilting a big lotus leaf to pour a few drops of dew into a tiny porcelain cup, another palace maid in a blue áo dài rowing, realistic, vertical 9:16.",
                 vid="0-5s: Misty dawn on the lotus lake; the viewer carefully tilts a lotus leaf, and a few drops of dew roll into a tiny porcelain cup. The maid rowing the boat whispers: \"Cẩn thận! Đổ một giọt là cả đêm nay mất trắng.\" 5-10s: The viewer holds up the cup, barely a third full, and sighs: \"Hứng cả đêm được nửa chén, vua nhấp một ngụm là hết!\"",
                 subs=[(0.5, 4.8, "Cẩn thận! Đổ một giọt / là cả đêm nay mất trắng."),
                       (5.0, 9.8, "Hứng cả đêm được nửa chén, / vua nhấp một ngụm là hết!")]),
            dict(name="Năm mươi món", label="Ngự thiện phòng · gần trưa",
                 img="First-person view in a huge 19th-century imperial kitchen in Huế, a long row of cooks in white each standing at their own clay stove preparing one dish, dozens of small porcelain bowls lined up, a nervous young cook holding bowl number 37, realistic, vertical 9:16.",
                 vid="0-5s: A long row of cooks, each at their own stove, finish dozens of small dishes; a nervous young cook next to the viewer holds up his bowl and says: \"Em là món số 37. Vua mà gắp trúng là em được thưởng!\" 5-10s: Servants carry the fifty bowls away in a long line; the young cook clasps his hands and prays at the stove.",
                 subs=[(0.5, 4.8, "Em là món số 37. / Vua mà gắp trúng là em được thưởng!")]),
            dict(name="Vua gắp ba món", label="Bữa trưa",
                 img="First-person view peeking from behind a red lacquered screen into an imperial dining room in Huế, a thin emperor in a yellow robe seen from behind at a table covered with fifty small dishes, servants kneeling, realistic, vertical 9:16.",
                 vid="0-5s: From behind a lacquered screen, the viewer watches the emperor, seen from behind, slowly pick a bite from just three dishes, then set down his chopsticks. 5-10s: The young cook peeks in beside the viewer, counts the dishes, and whispers, heartbroken: \"Ba món... món 37 vẫn còn nguyên.\" The viewer pats his shoulder.",
                 subs=[(5.0, 9.5, "Ba món... món 37 vẫn còn nguyên.")]),
        ],
        caption="Hứng sương cả đêm được nửa chén trà, nấu 50 món mà vua chỉ gắp 3 🥲 Giai thoại kể vua Tự Đức rất kén ăn, uống trà ướp sen pha bằng sương hứng trên lá sen hồ Tịnh Tâm. Nếu nấu cho vua, bạn sẽ nấu món gì? 👇",
        tags="#tuduc #nhanguyen #cungdinhhue #amthuchue",
    ),
    # ------------------------------------------------------------------ 6
    dict(
        slug="thach-cuoi", prefix="tc", title="Đi hỏi vợ bị thách cưới",
        length="40 giây · 4 clip (thách cưới cần một nhịp mặc cả)",
        history=("**Phong tục:** ngày xưa, khi nhà trai đến hỏi, nhà gái có tục **thách cưới**: đưa ra danh sách lễ vật "
                 "như trầu cau, lợn, gạo, rượu, tiền cheo nộp cho làng. Nhà trai nghèo không đủ lễ có khi phải **ở rể**, "
                 "tức là làm lụng cho nhà vợ một thời gian để \"trả\" thay lễ. Ca dao còn nhiều câu nói về chuyện thách "
                 "cưới và nộp cheo. Tập này dựng theo phong tục chung của làng quê Bắc Bộ xưa, nhân vật là hư cấu."),
        setting=("Vietnam, northern village, 19th century: a thatched house with a tiled-roof front porch, a betel palm "
                 "and a well in the yard, rice fields behind. The groom's side in their best black áo the and turbans; "
                 "the matchmaker (bà mối) is a talkative woman around 55 with black teeth chewing betel; the bride's father "
                 "is a stern, skinny man around 55 with a thin beard and black teeth; the bride peeks from behind a curtain."),
        hook="POV: Bạn đi hỏi vợ / và bị nhà gái thách cưới",
        end="Ba năm ở rể, bạn có cưới được không? / Follow để xem tập sau / bạn là ai ở thời xưa →",
        clips=[
            dict(name="Đến nhà gái", label="Làng quê Bắc Bộ · thế kỷ 19",
                 img="First-person view walking into the yard of a 19th-century northern Vietnamese village house holding a tray of betel leaves and areca nuts, a talkative matchmaker woman with black teeth leading the way, a stern skinny father with a thin beard waiting on the porch, realistic, vertical 9:16.",
                 vid="0-5s: The viewer walks nervously into the yard holding a tray of betel and areca; the matchmaker, chewing betel, nudges him and whispers: \"Cười lên! Mặt như đi nộp sưu thế kia ai gả con cho!\" 5-10s: The stern father on the porch looks the viewer up and down slowly and says: \"Ngồi đi. Nhà ta nói chuyện lễ trước.\"",
                 subs=[(0.5, 4.8, "Cười lên! Mặt như đi nộp sưu thế kia / ai gả con cho!"),
                       (5.0, 9.5, "Ngồi đi. Nhà ta nói chuyện lễ trước.")]),
            dict(name="Danh sách thách cưới", label="Trên chiếu",
                 img="First-person view sitting on a mat on a village house porch, 19th century, a stern father with a thin beard unrolling a very long paper list that rolls onto the floor, the matchmaker's eyes widening, betel tray on the mat, realistic, vertical 9:16.",
                 vid="0-5s: The father unrolls a very long paper list that rolls off the mat onto the floor and reads: \"Trăm buồng cau, trăm lá trầu, năm chum rượu, một con lợn béo, mười thúng gạo nếp...\" 5-10s: The paper keeps rolling across the yard; the viewer whispers to the matchmaker: \"Bà ơi, nhà con bán cả trâu cũng không đủ!\" The matchmaker keeps chewing betel, unbothered.",
                 subs=[(0.5, 4.8, "Trăm buồng cau, trăm lá trầu, năm chum rượu, / một con lợn béo, mười thúng gạo nếp..."),
                       (5.0, 9.8, "Bà ơi, nhà con bán cả trâu cũng không đủ!")]),
            dict(name="Mặc cả", label="Một tuần trà sau",
                 img="First-person view on a village house porch, 19th century, the talkative matchmaker with black teeth leaning toward the stern father, gesturing and bargaining, the bride peeking from behind a curtain smiling, realistic, vertical 9:16.",
                 vid="0-5s: The matchmaker leans toward the father, all smiles: \"Ông ơi, thằng bé chăm lắm, sức khỏe như trâu. Lễ bớt cho nó một nửa đi!\" 5-10s: The bride peeks from behind the curtain and smiles at the viewer; the father strokes his thin beard and says: \"Được. Bớt một nửa lễ, nhưng phải ở rể.\"",
                 subs=[(0.5, 4.8, "Ông ơi, thằng bé chăm lắm, sức khỏe như trâu. / Lễ bớt cho nó một nửa đi!"),
                       (5.0, 9.8, "Được. Bớt một nửa lễ, nhưng phải ở rể.")]),
            dict(name="Ở rể", label="Sáng hôm sau",
                 img="First-person view at dawn standing at the edge of a huge rice field in 19th-century northern Vietnam, the viewer's hands holding a wooden plough and a buffalo rope, the stern father pointing to the far horizon, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; the father hands the viewer a plough and a buffalo rope, points at an enormous rice field stretching to the horizon and says: \"Ba năm. Cày hết chỗ này, gánh nước đầy giếng, rồi tính chuyện cưới.\" 5-10s: The viewer looks at the endless field, then back at the house where the bride waves from the gate, takes a deep breath and says: \"Con làm!\"",
                 subs=[(0.5, 4.8, "Ba năm. Cày hết chỗ này, gánh nước đầy giếng, / rồi tính chuyện cưới."),
                       (6.5, 9.5, "Con làm!")]),
        ],
        caption="Đi hỏi vợ, nhà gái đọc danh sách thách cưới dài hết cả sân, mặc cả xong thì... ở rể ba năm 😭 Ngày xưa nhà trai không đủ lễ thì phải ở rể làm lụng cho nhà vợ. Quê bạn ngày xưa thách cưới những gì? 👇",
        tags="#thachcuoi #oro #phongtucviet #cuoihoixua",
    ),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    index = []
    for n, ep in enumerate(EPISODES, 1):
        base = f"tap-{n}-{ep['slug']}"
        md = [f"# Tập {n}: {ep['title']}", "",
              f"**Độ dài:** {ep['length']}", "",
              "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
              ep["history"], ""]
        plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4",
                f"hook: {ep['hook']}", f"end: {ep['end']}", ""]
        subs = []
        for i, c in enumerate(ep["clips"], 1):
            fname = f"{ep['prefix']}-{i}.mp4"
            video = f"{POV} {ep['setting']} {c['vid']} {AUDIO}"
            md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{fname}`", "",
                   "**Ảnh khung đầu**", "```", c["img"], "```", "",
                   "**Video (Muse)**", "```", video, "```", ""]
            plan.append(f"clip: {fname} | {c['label']}")
            subs += [f"sub: {i} | {a}-{b} | {t}" for a, b, t in c["subs"]]
        plan += [""] + subs
        md += ["## Đăng TikTok", "", "```", f"{ep['caption']}", f"{TAGS} {ep['tags']}", "```", "",
               "Khi đăng: bật nhãn \"Nội dung do AI tạo\".", "",
               "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
        with open(os.path.join(here, base + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md))
        with open(os.path.join(here, base + ".plan.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(plan) + "\n")
        index.append((n, ep, base))
    print("\n".join(f"{n}. {base}: {len(ep['clips'])} clip" for n, ep, base in index))


if __name__ == "__main__":
    main()
