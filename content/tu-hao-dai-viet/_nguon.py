#!/usr/bin/env python3
"""Loạt "Tự hào Đại Việt": những lần tổ tiên khiến người xem tự hào vì CÁCH CƯ XỬ (nhân nghĩa, khôn ngoan, đoàn kết).
Công thức Anh Tư, bản đầy đủ 6 cảnh, bản ngắn đủ cảnh. Sửa ở đây rồi chạy: python3 _nguon.py

Danh sách đề tài: ../nghien-cuu/de-tai-tu-hao-dan-toc.md. Mỗi tập qua 2 cổng duyệt: Sử gia + Kiểm duyệt nội quy.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build, MUC_MOI  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a chipped front tooth; "
        "he acts naturally and understated, like a real person, not a performer")
NO_TEXT = "No flags, no visible or legible writing anywhere, no modern objects, no blood, no dead bodies."

NOTE = ("**Tự hào Đại Việt:** những lần tổ tiên khiến ta tự hào vì cách cư xử (nhân nghĩa, khôn ngoan, đoàn kết), kể theo "
        "công thức Anh Tư. Giọng kể tự hào về ta, không hạ thấp nước khác. **Hai video từ cùng 6 clip:** bản dài (YouTube) "
        "đủ clip; bản ngắn (TikTok) vẫn đủ cả 6 cảnh.")
LEN6 = ("hai video từ cùng 6 clip: **bản dài** (YouTube, khoảng 58 giây sau chuyển cảnh) và **bản ngắn** (TikTok, khoảng "
        "38 giây) vẫn đủ cả 6 cảnh: cảnh mở đầu và cảnh kết giữ nguyên, 4 cảnh giữa cắt lấy 5 giây chứa câu chính")
LEN7 = ("hai video từ cùng 7 clip: **YouTube** đủ 7 cảnh (khoảng 67 giây); **TikTok** chọn **4 cảnh chính**, giữ gần trọn từng cảnh (khoảng 35 giây) để không mất câu thoại nào; các cảnh còn lại chỉ có ở bản YouTube")
# Tập mới từ 19/11/2026: length=LEN7, muc=MUC_MOI.
END = "Follow để xem / Tự hào Đại Việt / tập tiếp theo →"

SONG = ("Song dynasty soldiers in Song-style lamellar armor and helmets, tired and many of them sick, sitting by "
        "smoky campfires; the Song commander Quách Quỳ is a weary, grey-bearded Chinese general in his 50s in "
        "officer's armor, dignified")
TRAN = ("Trần dynasty Vietnamese soldiers and boatmen with hair in topknots and black-lacquered teeth, in brown or dark "
        "cotton tunics, barefoot, with spears and bows")
LY = ("Lý dynasty Vietnamese soldiers with hair in topknots and black-lacquered teeth, in brown or dark-red tunics, "
      "with spears and crossbows; Lý Thường Kiệt is a dignified, calm Vietnamese commander in his late 50s with a grey "
      "beard in dark Lý-era armor and a red cloak, seen only from behind or in profile")

EPISODES = [
    # ------------------------------------------------------------------ 1077 Như Nguyệt chủ động giảng hòa
    dict(
        slug="dua-thu-giang-hoa-nhu-nguyet-1077", prefix="th1077",
        voices={"Lý Thường Kiệt": "a deep, calm, commanding older male voice, slow and certain",
                "Quách Quỳ": "a tired, hoarse older male voice speaking Vietnamese with a light Chinese accent",
                "temple": "a solemn, echoing male voice reciting poetry slowly, as if from far away"},
        title="Thắng thế rồi lại bị sai đi đưa thư xin hòa cho giặc (Như Nguyệt, 1077)",
        length=LEN6,
        history=("**Lịch sử:** năm 1076–1077, quân Tống do Quách Quỳ chỉ huy kéo sang đánh Đại Việt, bị chặn ở phòng tuyến "
                 "sông Như Nguyệt (sông Cầu) suốt nhiều tuần. Quân Tống mỏi mệt, đau ốm nhiều. Sau các trận phản công thắng "
                 "lợi, Thái úy **Lý Thường Kiệt chủ động sai người sang trại Tống đề nghị giảng hòa**, mở cho quân Tống đường "
                 "rút về trong danh dự để sớm chấm dứt chiến tranh. Quách Quỳ đồng ý và rút quân. Quân Tống vẫn giữ một số "
                 "vùng biên giới; về sau, qua đàm phán (năm 1084), Đại Việt đòi lại thêm đất (mức B; sử nhà Tống cũng chép "
                 "việc rút quân). Theo truyền tụng, trong những ngày giằng co có tiếng đọc bài thơ \"Nam quốc sơn hà\" vọng ra "
                 "từ đền thờ bên sông (mức C; tác giả và hoàn cảnh bài thơ còn tranh luận). Bản dịch thơ dùng trong video là "
                 "bản dịch phổ biến trong sách giáo khoa. **Hư cấu:** Anh Tư đưa thư, mọi lời thoại (lời Lý Thường Kiệt và "
                 "Quách Quỳ phỏng theo ý sử chép). Không dựng cảnh chết chóc. Nguồn tham khảo: "
                 "[Wikipedia](https://en.wikipedia.org/wiki/Battle_of_Nh%C6%B0_Nguy%E1%BB%87t_River_(1077)), "
                 "[VietJack, Lịch sử 7](https://vietjack.com/lich-su-7-cd/ly-thuyet-bai-15-cuoc-khang-chien-chong-quan-tong-xam-luoc-cua-nha-ly-1075-1077.jsp)."),
        setting=("Vietnam, early 1077, the Như Nguyệt River (Cầu River): a wide river with an earthen rampart and bamboo "
                 "stakes on the south bank, a small old temple among trees on the bank, the Song army camp with tents on "
                 f"the north bank. {LY}. {SONG}. Anh Tư is {FACE}, a Lý soldier in a brown tunic. {NO_TEXT}"),
        visual=("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** quân Lý búi tóc, răng đen, áo nâu hoặc đỏ thẫm; quân Tống mặc giáp "
                "vảy và đội mũ kiểu Tống. Lý Thường Kiệt chỉ thấy từ phía sau hoặc nghiêng. Quân Tống mỏi mệt nhưng được "
                "dựng đàng hoàng, không bêu riếu. Không cờ, không chữ, không máu."),
        hook="POV: Thắng rồi / lại bị sai / đi xin hòa",
        end=END,
        end_secs=1.6,
        clips=[
            dict(name="Bài thơ trong đêm", label="Sông Như Nguyệt · năm 1077",
                 img=f"First-person view at night on an earthen rampart by a wide river, soldiers sitting silently, a small old temple among dark trees on the bank glowing faintly with lamplight, {FACE} beside the viewer, listening, realistic, vertical 9:16.",
                 vid=("0-10s: Night on the rampart; the soldiers fall silent as a solemn, echoing voice drifts from the small "
                      "temple by the river, reciting slowly in Vietnamese: \"Sông núi nước Nam vua Nam ở. Rành rành định phận "
                      "tại sách trời. Cớ sao lũ giặc sang xâm phạm? Chúng mày nhất định phải tan vỡ.\" Anh Tư slowly "
                      "straightens up, his face lit by the lamps, his fear gone."),
                 subs=[(0.3, 2.4, "Theo truyền tụng, đêm ấy / từ đền bên sông vọng ra:"),
                       (2.4, 4.2, "Sông núi nước Nam / vua Nam ở,"),
                       (4.2, 6.0, "Rành rành định phận / tại sách trời."),
                       (6.0, 7.9, "Cớ sao lũ giặc / sang xâm phạm?"),
                       (7.9, 9.8, "Chúng mày nhất định / phải tan vỡ.")]),
            dict(name="Thắng thế", tiktok="5-10", label="Mấy tuần sau",
                 img=f"First-person view from the rampart at dawn across the river, the Song camp quiet and smoky with tired, sick soldiers sitting by fires, {FACE} gripping his spear, an officer beside him shaking his head, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn; across the river the Song camp is quiet and smoky, soldiers sitting tired and sick by the "
                      "fires. Anh Tư grips his spear: \"Giặc mệt lắm rồi! Mai đánh nốt là xong!\" 5-10s: The officer "
                      "beside him shakes his head: \"Không đánh nữa. Thái úy gọi mày.\" Anh Tư blinks: \"Ơ...?\""),
                 subs=[(0.5, 4.8, "Giặc mệt lắm rồi! / Mai đánh nốt là xong!"),
                       (5.0, 7.6, "Không đánh nữa. / Thái úy gọi mày."),
                       (7.6, 9.6, "Ơ...?")]),
            dict(name="Lá thư", tiktok="5-10", label="Trướng của Thái úy",
                 img=f"First-person view inside a command tent lit by oil lamps, the dignified grey-bearded commander seen in profile handing a sealed letter to {FACE}, who holds out both hands, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is the dignified grey-bearded commander in dark armor and a red "
                      "cloak, seen in profile; the RECEIVER is Anh Tư in a brown tunic. 0-5s: The commander hands him a sealed "
                      "letter and says calmly: \"Mang sang trại Tống. Xin giảng hòa.\" 5-10s: Anh Tư holds the letter, "
                      "baffled, and whispers to the viewer: \"Mình đang thắng... mà mình xin hòa ạ?\""),
                 subs=[(0.5, 4.8, "Mang sang trại Tống. / Xin giảng hòa."),
                       (5.0, 9.5, "Mình đang thắng... / mà mình xin hòa ạ?")]),
            dict(name="Trại Tống", tiktok="5-10", label="Bờ bắc sông Như Nguyệt",
                 img=f"First-person view inside the Song camp, a weary grey-bearded Song general reading a letter by a campfire, tired Song soldiers watching, {FACE} standing respectfully in front of him, realistic, vertical 9:16.",
                 vid=("0-5s: In the Song camp, the weary grey-bearded general reads the letter by the fire; his shoulders "
                      "relax; he looks at his tired soldiers and says quietly in accented Vietnamese: \"Rút quân.\" 5-10s: Anh "
                      "Tư bows and whispers to the viewer: \"Ông ấy thở ra một hơi... như được tha về nhà.\""),
                 subs=[(0.5, 4.8, "Rút quân."),
                       (5.0, 9.5, "Ông ấy thở ra một hơi... / như được tha về nhà.")]),
            dict(name="Mở đường", tiktok="0-5", label="Sáng hôm sau",
                 img=f"First-person view from the south bank as the Song army marches away north along a road in an orderly column, Lý soldiers standing aside on the bank with their spears lowered, not attacking, {FACE} beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: The Song army marches away north in an orderly column; the Lý soldiers stand aside with spears "
                      "lowered. Anh Tư whispers to the viewer: \"Thắng rồi... mà còn mở đường cho nó về.\" 5-10s: The officer "
                      "beside him says quietly: \"Đánh nữa thì hai bên cùng mất người. Để nó về, nó nhớ lâu.\""),
                 subs=[(0.5, 4.8, "Thắng rồi... / mà còn mở đường cho nó về."),
                       (5.0, 9.5, "Đánh nữa thì hai bên / cùng mất người. / Để nó về, nó nhớ lâu.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunset over the calm river and the empty north bank where the camp used to be, {FACE} sitting on the rampart, thoughtful, then looking at the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset over the calm river; the north bank is empty. A calm narrator's voice says: \"Năm 1077, "
                      "Lý Thường Kiệt chủ động giảng hòa khi đang thắng thế, mở đường cho quân Tống rút về.\" 5-10s: Anh Tư "
                      "looks at the empty bank, then looks at the camera: \"Đánh giỏi đã khó... biết dừng còn khó hơn.\""),
                 subs=[(0.3, 4.8, "Năm 1077, đang thắng thế, / Lý Thường Kiệt chủ động / giảng hòa, mở đường / cho quân Tống rút về."),
                       (5.0, 8.4, "Đánh giỏi đã khó... / biết dừng còn khó hơn.")]),
        ],
        caption=("Thắng thế rồi lại bị sai đi đưa thư xin hòa cho giặc 😳 Năm 1077, sau khi chặn đứng quân Tống ở sông Như "
                 "Nguyệt, Lý Thường Kiệt chủ động giảng hòa, mở cho quân Tống đường rút về trong danh dự để sớm kết thúc chiến "
                 "tranh. Bạn thấy đây là khôn ngoan hay quá hiền? 👇"),
        tags="#tuhaodaiviet #nhunguyet #lythuongkiet #namquocsonha #1077",
        tt_title="Thắng thế rồi lại bị sai đi đưa thư xin hòa cho giặc",
        hooks_alt=["POV: Thắng rồi / mà còn mở đường cho nó về", "POV: Đánh giỏi đã khó / biết dừng còn khó hơn"],
        pin=("Bài thơ \"Nam quốc sơn hà\" vang lên bên sông Như Nguyệt là theo truyền tụng, tác giả đến nay vẫn còn bàn 📜 "
             "Bạn thuộc bài thơ này từ lớp mấy? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1077: đang thắng mà Lý Thường Kiệt chủ động giảng hòa | Tự hào Đại Việt",
        yt_tags=("như nguyệt, lý thường kiệt, giảng hòa, nam quốc sơn hà, quách quỳ, nhà tống, 1077, tự hào đại việt, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1285 Hội nghị Diên Hồng
    dict(
        slug="rot-nuoc-dien-hong-1285", prefix="th1285",
        voices={"Thượng hoàng": "a warm, grave, older male voice, slow and clear",
                "elderly man": "a trembling but firm, creaky old male voice"},
        title="Bị sai đi rót nước cho các cụ già khắp nước về kinh, không ai nói họp gì (Hội nghị Diên Hồng, 1285)",
        length=LEN6,
        history=("**Lịch sử:** cuối năm Giáp Thân (đầu năm 1285), quân Nguyên chuẩn bị đánh Đại Việt lần thứ hai. Thượng hoàng "
                 "Trần Thánh Tông mời các bô lão trong nước về điện Diên Hồng ở kinh đô, ban yến và hỏi kế: nên hòa hay nên "
                 "đánh. Các bô lão đồng thanh xin đánh, \"muôn người như một, như bật ra từ một miệng\" (*Đại Việt sử ký toàn "
                 "thư*, mức B). Khác với Hội nghị Bình Than (1282) là cuộc họp của vương hầu, tướng lĩnh. **Hư cấu:** Anh Tư "
                 "rót nước, các cụ nói giọng nhiều vùng, cụ già nắm tay Anh Tư, việc tiếng hô vang ra phố và mọi lời thoại "
                 "(lời Thượng hoàng phỏng theo ý sử chép). Không dựng cảnh chiến tranh."),
        setting=("Thăng Long, early 1285: the Diên Hồng palace hall of the Trần dynasty with red-lacquered wooden pillars, "
                 "low tables with tea and simple food, a river landing outside the capital where boats arrive. Many elderly "
                 "Vietnamese men from all over the country with white beards and hair in topknots or cloth turbans, in plain "
                 "brown and indigo robes, some with walking sticks; Trần officials in dark robes. The retired emperor "
                 "(Thượng hoàng) in a yellow robe is seen ONLY from behind or at a distance. Adults only, no children. "
                 f"Anh Tư is {FACE}, a young palace servant in a brown tunic carrying teapots. {NO_TEXT}"),
        visual=("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** điện thời Trần cột sơn son; các cụ râu tóc bạc, búi tóc hoặc quấn "
                "khăn, áo nâu, áo chàm, chống gậy; Thượng hoàng chỉ thấy từ phía sau. Chỉ người lớn. Không cờ, không chữ."),
        hook="POV: Rót nước / cho các cụ / về kinh họp",
        end=END,
        end_secs=1.6,
        clips=[
            dict(name="Đón các cụ", tiktok="5-10", label="Thăng Long · đầu năm 1285",
                 img=f"First-person view at a river landing outside the capital, boats arriving with elderly men with white beards stepping ashore helped by servants, an official giving orders, {FACE} beside the viewer holding a teapot and a stack of cups, realistic, vertical 9:16.",
                 vid=("0-5s: Boats arrive at the landing; elderly men with white beards step ashore, helped by servants. The "
                      "official says to Anh Tư: \"Đón các cụ cho khéo. Rót nước cho đủ.\" 5-10s: Anh Tư whispers: \"Các cụ khắp "
                      "nước về kinh... họp gì ạ?\" The official, without looking: \"Mày lo ấm nước thôi.\""),
                 subs=[(0.5, 4.8, "Đón các cụ cho khéo. / Rót nước cho đủ."),
                       (5.0, 7.6, "Các cụ khắp nước về kinh... / họp gì ạ?"),
                       (7.6, 9.6, "Mày lo ấm nước thôi.")]),
            dict(name="Giọng khắp nơi", tiktok="5-10", label="",
                 img=f"First-person view in a palace hall with red pillars, groups of elderly men from different regions chatting at low tables, {FACE} pouring tea into their cups, listening, realistic, vertical 9:16.",
                 vid=("0-5s: In the hall, Anh Tư pours tea for groups of elderly men chatting in different regional accents; "
                      "one asks another: \"Giặc đến đâu rồi?\" 5-10s: Anh Tư whispers to the viewer: \"Cụ thì giọng Nghệ, cụ thì "
                      "giọng Thanh... mà cụ nào cũng hỏi giặc đến đâu rồi.\""),
                 subs=[(0.5, 4.8, "Giặc đến đâu rồi?"),
                       (5.0, 9.5, "Cụ giọng Nghệ, / cụ giọng Thanh... / mà cụ nào cũng hỏi / giặc đến đâu rồi.")]),
            dict(name="Vua hỏi", tiktok="5-10", label="Điện Diên Hồng",
                 img=f"First-person view from the side of the palace hall, the retired emperor in a yellow robe seen only from behind standing before rows of seated elderly men, {FACE} holding a tray of cups, frozen, realistic, vertical 9:16.",
                 vid=("0-5s: The hall falls silent as the retired emperor, seen only from behind, rises before the rows of "
                      "elders. Anh Tư, holding his tray, whispers: \"Vua đứng... trước các cụ?\" 5-10s: The emperor's grave voice: "
                      "\"Giặc Nguyên sang đông. Nên hòa... hay nên đánh?\""),
                 subs=[(0.5, 4.8, "Vua đứng... / trước các cụ?"),
                       (5.0, 9.5, "Giặc Nguyên sang đông. / Nên hòa... hay nên đánh?")]),
            dict(name="Đánh!", label="",
                 img=f"First-person view in the palace hall as all the elderly men rise at once, raising their fists and walking sticks and shouting together, {FACE} in the foreground nearly dropping his teapot, realistic, vertical 9:16.",
                 vid=("0-5s: A moment of silence; then all the elders rise at once, raising fists and walking sticks, and shout "
                      "together with one voice: \"Đánh!\" The pillars seem to shake. 5-10s: Anh Tư, nearly dropping his teapot, "
                      "whispers to the viewer: \"Vua hỏi hòa hay đánh... mà các cụ hô to hơn cả lính.\""),
                 subs=[(0.5, 4.8, "ĐÁNH!"),
                       (5.0, 9.5, "Vua hỏi hòa hay đánh... / mà các cụ hô to / hơn cả lính.")]),
            dict(name="Bàn tay cụ già", tiktok="5-10", label="",
                 img=f"First-person view near a pillar, a very old man with a long white beard and trembling hands gripping {FACE}'s arm firmly and looking him in the eye, realistic, vertical 9:16.",
                 vid=("0-5s: A very old man with trembling hands grips Anh Tư's arm firmly and says: \"Cụ già rồi, không cầm "
                      "giáo được... nhưng con cháu cụ thì được.\" 5-10s: Anh Tư, moved, nods slowly: \"Dạ... cháu nghe rồi.\""),
                 subs=[(0.5, 4.8, "Cụ già rồi, / không cầm giáo được... / nhưng con cháu cụ thì được."),
                       (5.0, 9.5, "Dạ... cháu nghe rồi.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at dusk outside the palace gate, elderly men leaving with their walking sticks while young men line up nearby, {FACE} putting down his teapot and picking up a spear, determined, realistic, vertical 9:16.",
                 vid=("0-5s: Dusk at the palace gate; the elders leave with their sticks while young men line up nearby. A calm "
                      "narrator's voice says: \"Đầu năm 1285, Thượng hoàng Trần Thánh Tông mời các bô lão về điện Diên Hồng hỏi "
                      "kế. Muôn người như một: Đánh!\" 5-10s: Anh Tư sets down his teapot, picks up a spear and says to the camera: "
                      "\"Em rót nước cả buổi... về nhà, em đi tòng quân.\""),
                 subs=[(0.3, 4.8, "Năm 1285, Thượng hoàng / mời các bô lão về điện / Diên Hồng hỏi kế. / Muôn người như một: Đánh!"),
                       (5.0, 8.4, "Em rót nước cả buổi... / về nhà, em đi tòng quân.")]),
        ],
        caption=("Bị sai đi rót nước cho các cụ già khắp nước về kinh, không ai nói họp gì 😳 Đầu năm 1285, trước khi quân Nguyên "
                 "sang lần thứ hai, Thượng hoàng Trần Thánh Tông mời các bô lão về điện Diên Hồng hỏi nên hòa hay nên đánh. Cả "
                 "điện đồng thanh: \"Đánh!\" Nếu ông bà bạn ngồi đó, ông bà sẽ hô gì? 👇"),
        tags="#tuhaodaiviet #dienhong #hoinghidienhong #nhatran #1285",
        tt_title="Bị sai đi rót nước cho các cụ già khắp nước về kinh, không ai nói họp gì",
        hooks_alt=["POV: Vua hỏi hòa hay đánh / các cụ hô to hơn lính", "POV: Các cụ khắp nước / về kinh họp"],
        pin=("Hội nghị Diên Hồng là lần hiếm hoi vua hỏi ý dân trước khi quyết đánh giặc 🔥 Bạn có biết trước đó một năm còn có "
             "hội nghị nào khác không? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1285: rót nước ở Hội nghị Diên Hồng, các cụ hô \"Đánh!\" | Tự hào Đại Việt",
        yt_tags=("hội nghị diên hồng, điện diên hồng, trần thánh tông, bô lão, kháng chiến chống nguyên, 1285, nhà trần, "
                 "tự hào đại việt, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1285 Sát Thát
    dict(
        slug="pha-muc-sat-that-1285", prefix="th1285s",
        voices={"tattooer": "a gruff, calm middle-aged male voice, few words",
                "officer": "a short, stern male voice",
                "young soldier": "a cheeky, cheerful young adult male voice"},
        title="Bị sai pha mực cả đêm cho cả đạo quân xăm chữ lên tay (Sát Thát, 1285)",
        length=LEN6,
        history=("**Lịch sử:** khi quân Nguyên chuẩn bị sang đánh Đại Việt lần thứ hai (cuối 1284, đầu 1285), quân sĩ nhà Trần "
                 "đều thích (xăm) vào cánh tay hai chữ **\"Sát Thát\" (殺韃)**, nghĩa là \"đánh giặc Thát\" (tức quân Mông Cổ, "
                 "Nguyên sang xâm lược), để tỏ quyết tâm (*Đại Việt sử ký toàn thư*, mức B; chưa đối chiếu trực tiếp nguyên văn). "
                 "Thời Trần, chữ viết là chữ Hán, nên trên tay xăm chữ Hán 殺韃, phụ đề phiên âm \"Sát Thát\". **Hư cấu:** Anh "
                 "Tư pha mực, người thợ xăm, anh lính đòi xăm tên người yêu và mọi lời thoại. Không dựng cảnh đánh nhau, không máu."),
        setting=("Đại Việt, late 1284: a Trần army camp at night by a river, torches and campfires, rows of bamboo huts. "
                 + TRAN + ". A middle-aged tattooer with a bundle of fine bamboo needles and a bowl of black ink; soldiers "
                 "sit calmly with one sleeve rolled up, no blood, only clean black ink. The ONLY legible writing anywhere is "
                 "the two Chinese characters 殺韃 tattooed in black ink on soldiers' forearms, written clearly and correctly. "
                 f"Adults only, no children. Anh Tư is {FACE}, a camp helper grinding ink in a big stone mortar. "
                 "No flags, no other writing, no modern objects, no dead bodies."),
        visual=("**Chuẩn hình ảnh:** quân Trần búi tóc, răng đen, áo nâu, chân đất. **Riêng tập này** (anh duyệt): chữ **殺韃** "
                "xăm rõ trên cánh tay, mực đen, không máu; ngoài hai chữ này không có chữ nào khác. Nếu Muse vẽ sai nét chữ Hán, "
                "chọn khung hình chữ đúng nhất hoặc để tay hơi nghiêng; phụ đề đã ghi rõ \"Sát Thát\"."),
        hook="POV: Pha mực / cho cả đạo quân / xăm tay",
        end=END,
        end_secs=1.6,
        clips=[
            dict(name="Cối mực", tiktok="5-10", label="Trại quân nhà Trần · cuối 1284",
                 img=f"First-person view at night in a Trần army camp, an officer pointing at a huge stone mortar and sacks of soot beside a campfire, {FACE} holding a pestle, confused, realistic, vertical 9:16.",
                 vid=("0-5s: The officer points at a huge stone mortar and sacks of soot and says to Anh Tư: \"Pha mực. Pha cho "
                      "đủ cả đạo quân.\" 5-10s: Anh Tư whispers: \"Mực... để viết gì ạ? Ai biết chữ đâu?\" The officer, without "
                      "looking: \"Sáng mai khắc biết.\""),
                 subs=[(0.5, 4.8, "Pha mực. / Pha cho đủ cả đạo quân."),
                       (5.0, 7.8, "Mực... để viết gì ạ? / Ai biết chữ đâu?"),
                       (7.8, 9.6, "Sáng mai khắc biết.")]),
            dict(name="Xếp hàng", tiktok="5-10", label="",
                 img=f"First-person view of a long line of Trần soldiers in the torchlight, each rolling up one sleeve, {FACE} carrying a heavy bowl of black ink along the line, realistic, vertical 9:16.",
                 vid=("0-5s: A long line of soldiers in torchlight, each rolling up one sleeve; Anh Tư walks along carrying a "
                      "heavy bowl of ink. 5-10s: Anh Tư whispers to the viewer: \"Em tưởng xếp hàng lĩnh lương... hóa ra xếp hàng "
                      "đưa tay.\""),
                 subs=[(5.0, 9.5, "Em tưởng xếp hàng / lĩnh lương... / hóa ra xếp hàng đưa tay.")]),
            dict(name="Hai chữ", tiktok="5-10", label="",
                 img=f"Close view of a soldier's forearm with the two Chinese characters 殺韃 freshly tattooed in clean black ink, the tattooer's hand holding a bamboo needle bundle, {FACE} leaning in curiously, no blood, realistic, vertical 9:16.",
                 vid=("0-5s: The tattooer finishes the two characters 殺韃 in clean black ink on a soldier's forearm; the soldier "
                      "does not flinch. Anh Tư leans in: \"Hai chữ gì đấy ạ?\" 5-10s: The tattooer, without looking up: \"Sát "
                      "Thát. Đánh giặc Thát. Giặc sang... thì nhìn tay mà nhớ.\""),
                 subs=[(0.5, 4.8, "Hai chữ gì đấy ạ?"),
                       (5.0, 9.5, "Sát Thát. Đánh giặc Thát. / Giặc sang... / thì nhìn tay mà nhớ.")]),
            dict(name="Tên người yêu", label="",
                 img=f"First-person view as a cheeky young soldier holds out his arm to the tattooer, hopeful, the tattooer shaking his head, a few soldiers smirking, {FACE} in the foreground, trying not to smile, realistic, vertical 9:16.",
                 vid=("0-5s: A cheeky young soldier holds out his arm and asks: \"Thêm tên người yêu em vào được không?\" The "
                      "tattooer: \"Hai chữ thôi.\" A few soldiers snort. 5-10s: Anh Tư turns to the viewer: \"Cả đạo quân xăm "
                      "cùng một chữ... không ai xăm tên người yêu.\""),
                 subs=[(0.5, 3.2, "Thêm tên người yêu em / vào được không?"),
                       (3.2, 4.8, "Hai chữ thôi."),
                       (5.0, 9.5, "Cả đạo quân / xăm cùng một chữ... / không ai xăm tên người yêu.")]),
            dict(name="Còn mày?", tiktok="5-10", label="",
                 img=f"First-person view near dawn, the whole line of soldiers done, the tattooer looking at {FACE} with an empty spot on the mat, Anh Tư staring at his ink-stained hands, realistic, vertical 9:16.",
                 vid=("0-5s: Near dawn the line is finished. The tattooer pats the empty mat and looks at Anh Tư: \"Còn mày?\" "
                      "5-10s: Anh Tư looks at his ink-black hands, then slowly rolls up his own sleeve: \"Em pha mực cả đêm... thì "
                      "em cũng phải có phần.\""),
                 subs=[(0.5, 4.8, "Còn mày?"),
                       (5.0, 9.5, "Em pha mực cả đêm... / thì em cũng phải có phần.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunrise by the river, rows of soldiers with dark tattoos on their forearms marching off, {FACE} raising his own forearm with 殺韃 tattooed on it toward the camera, proud, realistic, vertical 9:16.",
                 vid=("0-5s: Sunrise; soldiers with dark tattoos on their forearms march off along the river. A calm narrator's "
                      "voice says: \"Năm 1285, trước khi quân Nguyên sang lần thứ hai, quân sĩ nhà Trần đều thích vào cánh tay "
                      "hai chữ: Sát Thát.\" 5-10s: Anh Tư raises his own tattooed forearm to the camera: \"Mực em pha "
                      "đấy... cả đời không phai.\""),
                 subs=[(0.3, 4.8, "Năm 1285, quân sĩ nhà Trần / thích vào cánh tay / hai chữ: Sát Thát."),
                       (5.0, 8.4, "Mực em pha đấy... / cả đời không phai.")]),
        ],
        caption=("Bị sai pha mực cả đêm, không ai nói để làm gì 😳 Sáng ra cả đạo quân đều có hai chữ trên tay: Sát Thát. Năm "
                 "1285, trước khi quân Nguyên sang lần thứ hai, quân sĩ nhà Trần xăm chữ lên tay để tỏ quyết tâm đánh giặc. Nếu "
                 "là bạn, bạn có dám đưa tay ra không? 👇"),
        tags="#tuhaodaiviet #satthat #nhatran #khangchienchongnguyen #1285",
        tt_title="Bị sai pha mực cả đêm cho cả đạo quân xăm chữ lên tay",
        hooks_alt=["POV: Cả đạo quân xăm một chữ / không ai xăm tên người yêu", "POV: Pha mực / mà không biết / để viết gì"],
        pin=("Hai chữ \"Sát Thát\" là lời thề đánh giặc Nguyên của quân nhà Trần 🔥 Bạn có biết trước đó, Trần Hưng Đạo còn "
             "viết một bài hịch nổi tiếng không? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1285: pha mực cho cả đạo quân xăm chữ \"Sát Thát\" | Tự hào Đại Việt",
        yt_tags=("sát thát, quân nhà trần, kháng chiến chống nguyên, 1285, trần hưng đạo, xăm chữ sát thát, tự hào đại việt, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1473 Lê Thánh Tông giữ đất
    dict(
        slug="do-dat-bien-gioi-1473", prefix="th1473",
        voices={"official": "a dry, strict middle-aged male voice",
                "old official": "a slow, firm, dignified older male voice"},
        title="Bị sai đi đo đất biên giới từng tấc, thiếu một tấc cũng phải đo lại (Lê Thánh Tông, khoảng 1473)",
        length=LEN6,
        history=("**Lịch sử:** đời Hồng Đức, khi có tranh chấp đất ở biên giới phía Bắc, vua Lê Thánh Tông dặn các quan đi "
                 "giữ việc biên cương: \"Một thước núi, một tấc sông của ta, lẽ nào lại tự nhiên vứt bỏ?\" và cấm ai đem đất "
                 "của Thái Tổ (Lê Lợi) để cho người khác (*Đại Việt sử ký toàn thư*, mức B). Năm chép còn khác nhau: thường ghi "
                 "1473, có tài liệu ghi 1471. Trước đó (1469) triều Lê đã lập bản đồ cả nước, thường gọi là bản đồ Hồng Đức. "
                 "**Hư cấu:** Anh Tư đo đất bằng thừng, cảnh quan bàn chuyện nhường đất và mọi lời thoại (câu của vua phỏng "
                 "theo sử chép). Không dựng cảnh đánh nhau, không nhắc đến hình phạt."),
        setting=("Đại Việt, Hồng Đức era (about 1473): the misty northern border mountains, steep green ridges, a small clear "
                 "river winding between them, a mountain trail. Lê dynasty officials in dark blue or black robes and black "
                 "gauze hats with small side wings; local guides in indigo clothes. Vietnamese only, no foreign soldiers, the "
                 "king never appears. Adults only, no children. "
                 f"Anh Tư is {FACE}, a helper in a brown tunic carrying a long coil of rope and a bamboo measuring stick. {NO_TEXT}"),
        visual=("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** quan thời Lê sơ áo xanh đen, mũ ô sa cánh nhỏ; núi biên giới phía "
                "Bắc nhiều sương, sông nhỏ. Vua không xuất hiện, chỉ có lời vua được đọc lại. Không cờ, không chữ, bản đồ chỉ vẽ "
                "núi sông."),
        hook="POV: Đo đất / biên giới / từng tấc một",
        end=END,
        end_secs=1.6,
        clips=[
            dict(name="Cuộn thừng", tiktok="5-10", label="Biên giới phía Bắc · khoảng 1473",
                 img=f"First-person view on a misty mountain trail, a strict Lê official handing over a huge coil of rope and a bamboo measuring stick, {FACE} looking at the endless ridges, dismayed, realistic, vertical 9:16.",
                 vid=("0-5s: On a misty mountain trail the official hands Anh Tư a huge coil of rope and a bamboo stick: \"Đo đất. "
                      "Từng tấc một.\" 5-10s: Anh Tư looks at the endless ridges and whispers: \"Đo... cả dãy núi này ạ?\" The "
                      "official: \"Cả dãy. Cả con sông.\""),
                 subs=[(0.5, 4.8, "Đo đất. / Từng tấc một."),
                       (5.0, 7.8, "Đo... / cả dãy núi này ạ?"),
                       (7.8, 9.6, "Cả dãy. Cả con sông.")]),
            dict(name="Leo núi", tiktok="5-10", label="",
                 img=f"First-person view on a steep ridge, {FACE} stretching the rope over rocks while the official counts, clouds below them, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư stretches the rope over rocks up a steep ridge while the official counts each length out loud. "
                      "5-10s: Out of breath, Anh Tư whispers to the viewer: \"Người ta đo ruộng để thu thuế... em đo cả núi.\""),
                 subs=[(5.0, 9.5, "Người ta đo ruộng / để thu thuế... / em đo cả núi.")]),
            dict(name="Thiếu một tấc", tiktok="5-10", label="",
                 img=f"First-person view at a small clear border river, the official frowning at the bamboo stick held against the rope, {FACE} wanting to give up, realistic, vertical 9:16.",
                 vid=("0-5s: At the river's edge the rope ends a little short. Anh Tư shrugs: \"Thiếu có một tấc... bỏ qua đi ạ?\" "
                      "5-10s: The official looks at him sternly: \"Thiếu một tấc... thì đo lại.\""),
                 subs=[(0.5, 4.8, "Thiếu có một tấc... / bỏ qua đi ạ?"),
                       (5.0, 9.5, "Thiếu một tấc... / thì đo lại.")]),
            dict(name="Lời vua", label="",
                 img=f"First-person view inside a lamplit tent at night, a few Lê officials around a low table, an old official holding an imperial letter (seal and paper only, no legible writing) and speaking firmly, {FACE} listening at the tent flap, realistic, vertical 9:16.",
                 vid=("0-5s: In a lamplit tent an official sighs: \"Có mấy quả đồi... hay là nhường cho yên chuyện?\" An old "
                      "official raises the king's letter and says firmly: \"Lời vua dặn: Một thước núi, một tấc sông của ta... "
                      "lẽ nào lại tự nhiên vứt bỏ?\" 5-10s: At the tent flap, Anh Tư looks at the rope in his hands and whispers: "
                      "\"Một tấc sông... không được để mất.\""),
                 subs=[(0.3, 1.8, "Hay là nhường / cho yên chuyện?"),
                       (1.8, 4.8, "Một thước núi, một tấc sông / của ta... / lẽ nào lại tự nhiên vứt bỏ?"),
                       (5.0, 9.5, "Một tấc sông... / không được để mất.")]),
            dict(name="Bản đồ", tiktok="5-10", label="",
                 img=f"First-person view of a hand-painted map of mountains and rivers on paper (no writing at all), an official marking a line along a ridge with a brush, {FACE} placing his knotted rope beside it, realistic, vertical 9:16.",
                 vid=("0-5s: An official carefully paints a line along a ridge on a hand-drawn map of mountains and rivers, "
                      "following the knots on Anh Tư's rope. 5-10s: Anh Tư says quietly to the viewer: \"Cái thừng của em... thành biên "
                      "giới.\""),
                 subs=[(5.0, 9.5, "Cái thừng của em... / thành biên giới.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunset on a high ridge above the misty border mountains and the little river, {FACE} coiling his rope and looking out over the land, proud, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset over the border mountains. A calm narrator's voice says: \"Đời Hồng Đức, vua Lê Thánh Tông dặn "
                      "các quan giữ biên giới: Một thước núi, một tấc sông của ta, lẽ nào lại tự nhiên vứt bỏ.\" 5-10s: Anh Tư "
                      "coils his rope and says to the camera: \"Em leo cả tháng... mới biết một tấc đất nặng thế nào.\""),
                 subs=[(0.3, 4.8, "Vua Lê Thánh Tông dặn: / Một thước núi, một tấc sông / của ta... lẽ nào vứt bỏ?"),
                       (5.0, 8.4, "Em leo cả tháng... / mới biết một tấc đất / nặng thế nào.")]),
        ],
        caption=("Bị sai đi đo đất biên giới từng tấc, thiếu một tấc cũng phải đo lại 😳 Đời Hồng Đức, vua Lê Thánh Tông dặn các "
                 "quan: \"Một thước núi, một tấc sông của ta, lẽ nào lại tự nhiên vứt bỏ?\" Câu nào của tổ tiên làm bạn nổi da "
                 "gà nhất? 👇"),
        tags="#tuhaodaiviet #lethanhtong #hongduc #biengioi #motthuocnuimottacsong",
        tt_title="Bị sai đi đo đất biên giới từng tấc, thiếu một tấc cũng phải đo lại",
        hooks_alt=["POV: Thiếu một tấc đất / phải đo lại", "POV: Cái thừng của em / thành biên giới"],
        pin=("\"Một thước núi, một tấc sông của ta, lẽ nào lại tự nhiên vứt bỏ?\" 🔥 Bạn có biết triều Lê còn vẽ bản đồ cả "
             "nước từ năm 1469 không? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Đo đất biên giới từng tấc: \"Một thước núi, một tấc sông\" | Tự hào Đại Việt",
        yt_tags=("lê thánh tông, một thước núi một tấc sông, hồng đức, bản đồ hồng đức, biên giới, nhà lê, tự hào đại việt, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1282 Trần Quốc Toản bóp nát quả cam
    dict(
        slug="qua-cam-tran-quoc-toan-1282", prefix="th1282",
        length=LEN7, muc=MUC_MOI, tiktok_canh=[1, 4, 6, 7],
        voices={"gatekeeper": "a dry, polite but firm middle-aged male voice",
                "palace servant": "a soft, careful male voice",
                "embroiderer": "a calm, steady middle-aged woman's voice"},
        title="Đứng ngoài cửa hội nghị giữ ngựa cho cậu chủ, lúc cậu bước ra tay chảy đầy nước cam (Trần Quốc Toản, Bình Than 1282)",
        history=("**Lịch sử:** năm 1282, vua Trần họp các vương hầu ở Bình Than bàn việc chống quân Nguyên. Hoài Văn hầu **Trần "
                 "Quốc Toản** khi ấy khoảng 15 tuổi, **còn nhỏ nên không được dự bàn**; vua thương, ban cho một quả cam. Quốc Toản "
                 "uất ức, **bóp nát quả cam lúc nào không biết**. Về sau ông về tập hợp **hơn nghìn gia nô và thân thích**, sắm vũ "
                 "khí, đóng thuyền, may lá cờ đề sáu chữ **\"Phá cường địch, báo hoàng ân\"** (*Đại Việt sử ký toàn thư*, mức B). "
                 "**Hư cấu:** Anh Tư, người giữ cửa, người thêu cờ và mọi lời thoại. **An toàn trẻ em:** Quốc Toản là thiếu niên, "
                 "nên chỉ thấy từ phía sau hoặc từ xa, không cận mặt, không dựng cảnh trận đánh; những người theo ông trong "
                 "phim đều là người lớn. Lá cờ là cờ vải thời Trần, chữ thêu để mờ, câu chữ chỉ hiện ở phụ đề."),
        setting=("Bình Than, Đại Việt, 1282: a large wooden riverside hall of the Trần court with red pillars, guards at the "
                 "door, horses tied outside; later the courtyard of a noble house. Trần Quốc Toản is a slim teenage boy of about "
                 "15 in a fine dark-blue noble's robe, seen ONLY from behind or from far away, never a close-up of his face. "
                 "All other people are ADULTS: Trần nobles and officials in dark robes, household servants and relatives in "
                 "brown clothes with topknots and black-lacquered teeth. A long red cloth banner on a bamboo pole with six "
                 "embroidered golden characters that are blurred and unreadable. "
                 f"Anh Tư is {FACE}, an adult household servant holding the young lord's horse. No modern flags, no other "
                 "writing, no modern objects, no blood, no battle scenes."),
        visual=("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** điện gỗ thời Trần cột sơn son; vương hầu áo tối màu; gia nhân áo nâu, "
                "búi tóc, răng đen. **Trần Quốc Toản chỉ thấy từ phía sau hoặc từ xa.** Lá cờ vải đỏ, chữ thêu mờ."),
        hook="POV: Cậu chủ / không được vào họp",
        end=END,
        end_secs=1.6,
        clips=[
            dict(name="Chưa đủ tuổi", tiktok="0-5", label="Bình Than · 1282",
                 img=f"First-person view at the door of a large wooden riverside hall, a firm gatekeeper raising his hand to stop a slim teenage boy in a fine robe seen only from behind, {FACE} beside the viewer holding a horse, realistic, vertical 9:16.",
                 vid=("0-5s: The gatekeeper stops the slim boy, seen only from behind, and Anh Tư: \"Các ngươi đứng ngoài.\" Anh Tư: "
                      "\"Cậu chủ em cũng là vương hầu mà?\" The gatekeeper: \"Tước thì có. Tuổi thì chưa.\" 5-10s: Anh Tư sighs to "
                      "the viewer: \"Cậu chủ em đủ tước... chỉ thiếu mấy cái Tết.\""),
                 subs=[(0.3, 2.2, "Các ngươi / đứng ngoài."), (2.2, 3.4, "Cậu chủ em / cũng là vương hầu mà?"),
                       (3.4, 4.9, "Tước thì có. / Tuổi thì chưa."), (5.2, 9.5, "Cậu chủ em đủ tước... / chỉ thiếu mấy cái Tết.")]),
            dict(name="Mòn cả gạch", tiktok="bo", label="",
                 img=f"First-person view outside the hall, the slim boy seen only from behind pacing back and forth along the brick path with his hands clasped behind his back, {FACE} holding the horse and watching, realistic, vertical 9:16.",
                 vid=("0-5s: Voices murmur inside the hall; outside, the boy, seen only from behind, paces back and forth on the "
                      "brick path. 5-10s: Anh Tư says quietly to the viewer: \"Trong kia bàn việc nước... ngoài này cậu đi mòn cả "
                      "gạch.\""),
                 subs=[(5.0, 9.5, "Trong kia bàn việc nước... / ngoài này cậu đi / mòn cả gạch.")]),
            dict(name="Quả cam", tiktok="bo", label="",
                 img=f"First-person view as a careful palace servant comes out of the hall holding a single orange on a small tray and offers it to the boy seen only from behind, {FACE} watching, realistic, vertical 9:16.",
                 vid=("0-5s: A palace servant comes out with a single orange on a tray: \"Vua thương hầu còn nhỏ, ban cho quả cam.\" "
                      "The boy, seen only from behind, takes it without a word. 5-10s: Anh Tư whispers: \"Không cho vào họp... thì "
                      "cho quả cam.\""),
                 subs=[(0.5, 4.8, "Vua thương hầu còn nhỏ, / ban cho quả cam."), (5.0, 9.5, "Không cho vào họp... / thì cho quả cam.")]),
            dict(name="Nước cam", label="",
                 img=f"First-person medium view from behind as the slim boy walks away from the hall, his clenched fist at his side dripping orange juice onto the bricks, adult nobles coming out of the hall, {FACE} staring, realistic, vertical 9:16.",
                 vid=("0-5s: The meeting ends; adult nobles come out talking. The boy, seen only from behind, walks away fast; juice "
                      "drips from his clenched fist onto the bricks. 5-10s: Anh Tư, very quietly, to the viewer: \"Cậu không được "
                      "vào họp... lúc bước ra, tay cậu chảy đầy nước cam.\""),
                 subs=[(5.0, 9.5, "Cậu không được vào họp... / lúc bước ra, / tay cậu chảy đầy nước cam.")]),
            dict(name="Gọi người", tiktok="bo", label="",
                 img=f"First-person view in the courtyard of a noble house, rows of adult servants and relatives in brown clothes lining up, the boy seen only from behind standing on the steps, {FACE} in the front row, realistic, vertical 9:16.",
                 vid=("0-5s: In the courtyard, rows of adult servants and relatives line up; the boy, seen only from behind on the "
                      "steps, raises one arm. 5-10s: Anh Tư, in the front row, says quietly: \"Không cho cậu bàn việc nước... cậu tự "
                      "đi làm việc nước.\""),
                 subs=[(5.0, 9.5, "Không cho cậu bàn việc nước... / cậu tự đi làm việc nước.")]),
            dict(name="Thêu cờ", label="",
                 img=f"First-person view inside the house, adult women embroidering six golden characters (blurred, unreadable) on a long red cloth banner by lamplight, {FACE} holding the end of the cloth, realistic, vertical 9:16.",
                 vid=("0-5s: By lamplight adult women embroider golden characters on a long red banner. Anh Tư, holding the cloth: "
                      "\"Thêu chữ gì đấy ạ?\" The embroiderer, without looking up: \"Phá cường địch, báo hoàng ân.\" 5-10s: Anh Tư "
                      "says quietly to the viewer: \"Em không biết chữ... nhưng em hiểu nghĩa.\""),
                 subs=[(0.5, 2.4, "Thêu chữ gì đấy ạ?"), (2.4, 4.8, "Phá cường địch, / báo hoàng ân."),
                       (5.0, 9.5, "Em không biết chữ... / nhưng em hiểu nghĩa.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at dawn in the courtyard, the red banner raised on a tall bamboo pole, the boy seen only from behind and far away beneath it, rows of adults around him, {FACE} holding the pole steady, realistic, vertical 9:16.",
                 vid=("0-4.5s: Dawn; the red banner is raised on a tall pole; the boy stands beneath it, seen only from behind and far "
                      "away. A calm narrator's voice says: \"Năm 1282, Trần Quốc Toản còn nhỏ, không được dự bàn ở Bình Than, bóp nát "
                      "quả cam. Về sau cậu tự tập hợp người, giương cờ: Phá cường địch, báo hoàng ân.\" 4.5-10s: Anh Tư, holding the "
                      "pole, says quietly to the camera: \"Không được ngồi vào bàn... cậu tự dựng cả một lá cờ.\""),
                 subs=[(3.0, 6.0, "Năm 1282, không được dự bàn, / Trần Quốc Toản / bóp nát quả cam, / về dựng cờ đánh giặc."),
                       (6.1, 8.4, "Không được ngồi vào bàn... / cậu tự dựng / cả một lá cờ.")]),
        ],
        caption=("Đứng ngoài cửa giữ ngựa cho cậu chủ, lúc cậu bước ra tay chảy đầy nước cam 🍊 Năm 1282, Trần Quốc Toản còn nhỏ, "
                 "không được dự bàn việc nước ở Bình Than, bóp nát quả cam lúc nào không biết, rồi về tự dựng cờ \"Phá cường địch, "
                 "báo hoàng ân\". Bạn học chuyện này năm lớp mấy? 👇"),
        tags="#tuhaodaiviet #tranquoctoan #bopnatquacam #nhatran #1282",
        tt_title="Cậu chủ không được vào họp, lúc bước ra tay chảy đầy nước cam",
        hooks_alt=["POV: Tước thì có / tuổi thì chưa", "POV: Không cho vào họp / thì cho quả cam"],
        pin=("\"Phá cường địch, báo hoàng ân\": phá giặc mạnh, đền ơn vua 🔥 Bạn còn nhớ bài \"Lá cờ thêu sáu chữ vàng\" không? "
             "Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Trần Quốc Toản bóp nát quả cam (1282): \"Phá cường địch, báo hoàng ân\" | Tự hào Đại Việt",
        yt_tags=("trần quốc toản, bóp nát quả cam, hội nghị bình than, phá cường địch báo hoàng ân, lá cờ thêu sáu chữ vàng, "
                 "nhà trần, 1282, tự hào đại việt, lịch sử việt nam, pov lịch sử, anh tư, shorts"),
    ),
]

ACTING = ("Acting: natural and understated, like real people filmed in a documentary; small reactions (a sigh, a glance, a pause, a shake of the head) instead of big expressions. Anh Tư smiles at most once in the whole clip and never laughs at the camera; no exaggerated mugging or cartoonish faces.")
for _ep in EPISODES:
    _ep["setting"] = _ep["setting"] + " " + ACTING
    for _c in _ep["clips"]:
        if _c.get("setting"):
            _c["setting"] = _c["setting"] + " " + ACTING


if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#tuhaodaiviet #anhtu", note=NOTE, unit="Tập", file_unit="tap")
