#!/usr/bin/env python3
"""Loạt "Tự hào Đại Việt": những lần tổ tiên khiến người xem tự hào vì CÁCH CƯ XỬ (nhân nghĩa, khôn ngoan, đoàn kết).
Công thức Anh Tư, bản đầy đủ 6 cảnh, bản ngắn đủ cảnh. Sửa ở đây rồi chạy: python3 _nguon.py

Danh sách đề tài: ../nghien-cuu/de-tai-tu-hao-dan-toc.md. Mỗi tập qua 2 cổng duyệt: Sử gia + Kiểm duyệt nội quy.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
NO_TEXT = "No flags, no visible or legible writing anywhere, no modern objects, no blood, no dead bodies."

NOTE = ("**Tự hào Đại Việt:** những lần tổ tiên khiến ta tự hào vì cách cư xử (nhân nghĩa, khôn ngoan, đoàn kết), kể theo "
        "công thức Anh Tư. Giọng kể tự hào về ta, không hạ thấp nước khác. **Hai video từ cùng 6 clip:** bản dài (YouTube) "
        "đủ clip; bản ngắn (TikTok) vẫn đủ cả 6 cảnh.")
LEN6 = ("hai video từ cùng 6 clip: **bản dài** (YouTube, khoảng 58 giây sau chuyển cảnh) và **bản ngắn** (TikTok, khoảng "
        "38 giây) vẫn đủ cả 6 cảnh: cảnh mở đầu và cảnh kết giữ nguyên, 4 cảnh giữa cắt lấy 5 giây chứa câu chính")
END = "Follow để xem / Tự hào Đại Việt / tập tiếp theo →"

SONG = ("Song dynasty soldiers in Song-style lamellar armor and helmets, tired and many of them sick, sitting by "
        "smoky campfires; the Song commander Quách Quỳ is a weary, grey-bearded Chinese general in his 50s in "
        "officer's armor, dignified")
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
                 img=f"First-person view from the rampart at dawn across the river, the Song camp quiet and smoky with tired, sick soldiers sitting by fires, {FACE} grinning and gripping his spear, an officer beside him shaking his head, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn; across the river the Song camp is quiet and smoky, soldiers sitting tired and sick by the "
                      "fires. Anh Tư grips his spear and grins: \"Giặc mệt lắm rồi! Mai đánh nốt là xong!\" 5-10s: The officer "
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
                 img=f"First-person view at sunset over the calm river and the empty north bank where the camp used to be, {FACE} sitting on the rampart, thoughtful, then smiling at the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset over the calm river; the north bank is empty. A calm narrator's voice says: \"Năm 1077, "
                      "Lý Thường Kiệt chủ động giảng hòa khi đang thắng thế, mở đường cho quân Tống rút về.\" 5-10s: Anh Tư "
                      "looks at the empty bank, then smiles at the camera: \"Đánh giỏi đã khó... biết dừng còn khó hơn.\""),
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
                      "nước về kinh... họp gì ạ?\" The official, without looking: \"Không hỏi.\""),
                 subs=[(0.5, 4.8, "Đón các cụ cho khéo. / Rót nước cho đủ."),
                       (5.0, 7.6, "Các cụ khắp nước về kinh... / họp gì ạ?"),
                       (7.6, 9.6, "Không hỏi.")]),
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
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#tuhaodaiviet #anhtu", note=NOTE, unit="Tập", file_unit="tap")
