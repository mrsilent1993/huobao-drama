#!/usr/bin/env python3
"""Nguồn của loạt "Ba lần Bạch Đằng". Sửa ở đây rồi chạy: python3 _nguon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

ANH_TU = ("a shirtless Vietnamese fisherman around 30 with deeply tanned skin, hair in a topknot, a scar across "
          "his left eyebrow and a wide grin with a chipped front tooth")

NOTE = ("**Anh Tư:** nhân vật xuyên suốt, dân chài sông Bạch Đằng. Mỗi phần là một đời con cháu, đời nào cũng "
        "tên Tư, cùng gương mặt: **sẹo ngang lông mày trái, răng cửa mẻ, cười toe**. Nên tạo một ảnh chân dung "
        "Anh Tư (prompt trong `README.md`) để làm ảnh tham chiếu nhân vật trong Muse cho cả loạt.")

EPISODES = [
    # ------------------------------------------------------------------ 938
    dict(
        slug="ngo-quyen-938", prefix="bd1", title="Ngô Quyền, năm 938",
        length="30 giây · 3 clip (một kế, một cú chốt)",
        history=("**Lịch sử:** năm 938, Ngô Quyền cho đóng cọc gỗ đầu bịt sắt xuống lòng sông Bạch Đằng. Khi triều "
                 "lên, cọc chìm dưới nước. Ông cho thuyền nhẹ ra khiêu chiến rồi giả thua, nhử thuyền quân Nam Hán do "
                 "Hoằng Tháo chỉ huy vào bãi cọc. Triều rút, thuyền giặc mắc cọc và vỡ, Hoằng Tháo tử trận. Chiến "
                 "thắng mở ra thời kỳ độc lập lâu dài."),
        setting=("Vietnam, year 938, Bạch Đằng River estuary. Fishermen and soldiers barefoot with hair in topknots, "
                 "brown homespun clothes, small wooden fishing boats and light war canoes; large enemy Southern Han "
                 "warships with red sails; tidal river with muddy banks and mangroves; sharpened wooden stakes tipped "
                 f"with iron. Anh Tư is {ANH_TU}."),
        hook="Ba lần Bạch Đằng · Phần 1: / Bạn cắm cọc cho Ngô Quyền",
        end="Cọc nhà Anh Tư còn dùng lại không? / Follow xem phần 2: / Lê Hoàn, năm 981 →",
        clips=[
            dict(name="Bãi sông, lúc triều rút", label="Sông Bạch Đằng · năm 938",
                 img=f"First-person view standing knee-deep in mud on a riverbank at low tide, year 938, the viewer's hands holding a heavy wooden mallet over a tall sharpened wooden stake tipped with iron, rows of stakes stretching across the riverbed, {ANH_TU} hammering next to the viewer, realistic, vertical 9:16.",
                 vid="0-5s: Low tide, the viewer swings a heavy wooden mallet and drives an iron-tipped wooden stake into the muddy riverbed; next to him Anh Tư wipes his sweat and asks: \"Cắm cả rừng cọc giữa sông, định nuôi hàu à anh?\" 5-10s: An officer in a brown armor vest walking past grins and says: \"Cứ cắm đi, chờ nước triều lên rồi biết!\" Hundreds of stakes stretch across the river.",
                 subs=[(0.5, 4.8, "Cắm cả rừng cọc giữa sông, / định nuôi hàu à anh?"),
                       (5.0, 9.5, "Cứ cắm đi, chờ nước triều lên rồi biết!")]),
            dict(name="Triều lên, nhử địch", label="Triều lên · nhử địch",
                 img="First-person view from a small light war canoe on a wide high-tide river, year 938, the water surface calm with no stakes visible, huge enemy warships with red sails approaching in the distance, the viewer's hands gripping a paddle, realistic, vertical 9:16.",
                 vid="0-5s: High tide, the stakes are hidden under the water; the viewer paddles a light canoe toward the huge red-sailed enemy warships, and the commander in the next canoe shouts: \"Đánh qua loa thôi! Lúc chạy nhớ diễn cho sâu, mặt phải sợ thật vào!\" 5-10s: The canoes turn and flee upstream, the enemy warships chase them with drums beating, arrows splashing around; Anh Tư paddles frantically and shouts: \"Khỏi diễn anh ơi, em sợ thật!\"",
                 subs=[(0.5, 4.8, "Đánh qua loa thôi! Lúc chạy nhớ diễn cho sâu, / mặt phải sợ thật vào!"),
                       (6.5, 9.8, "Khỏi diễn anh ơi, em sợ thật!")]),
            dict(name="Triều rút", label="Triều rút",
                 img="First-person view from a riverbank at falling tide, year 938, large enemy warships with red sails stuck and tilting on sharpened stakes poking out of the water, hulls cracking, Vietnamese soldiers charging from the mangroves, realistic, vertical 9:16.",
                 vid="0-5s: The tide drops fast; the iron-tipped stakes rise out of the water and pierce the hulls of the enemy warships, which tilt and crack with loud splintering sounds, enemy soldiers jumping into the river. 5-10s: Anh Tư grabs the viewer's shoulder, pointing at a wrecked ship, and laughs: \"Cái cọc kia em cắm đấy! Ghi tên em vào sử nhé!\"",
                 subs=[(5.0, 9.5, "Cái cọc kia em cắm đấy! / Ghi tên em vào sử nhé!")]),
        ],
        caption="Cắm cọc cả buổi sáng mà không ai giải thích, đến chiều mới hiểu 😎 Năm 938, Ngô Quyền dùng cọc gỗ bịt sắt và con nước triều đánh tan quân Nam Hán. Bạn có biết sông Bạch Đằng còn chứng kiến mấy lần cắm cọc nữa không? 👇",
        tags="#ngoquyen #938",
    ),
    # ------------------------------------------------------------------ 981
    dict(
        slug="le-hoan-981", prefix="bd2", title="Lê Hoàn, năm 981",
        length="40 giây · 4 clip (cắm cọc thêm kế giả hàng, cần thêm một nhịp)",
        history=("**Lịch sử:** năm 980, Lê Hoàn lên ngôi (vua Lê Đại Hành). Năm 981 quân Tống kéo sang, thủy quân theo "
                 "sông Bạch Đằng. Theo *Đại Việt sử ký toàn thư*, vua sai quân **đóng cọc ngăn sông** như Ngô Quyền "
                 "năm xưa. Vua còn dùng kế **giả hàng**, nhử tướng Tống là Hầu Nhân Bảo đến Chi Lăng rồi giết. Quân "
                 "Tống thua, phải rút về."),
        setting=("Vietnam, early Lê dynasty, year 981, Bạch Đằng River. Soldiers and fishermen with short cropped hair, "
                 "black-lacquered teeth, brown clothes, rattan shields; Song dynasty warships with dark sails; King Lê "
                 "Hoàn is a strong, sharp-eyed man around 40 in dark lacquered armor with a red cloak. Anh Tư (the "
                 f"grandson of the fisherman from 938, looking exactly like him) is {ANH_TU}."),
        hook="Ba lần Bạch Đằng · Phần 2: / Bạn cắm cọc cho Lê Hoàn",
        end="Kế giả hàng có lừa được tướng Tống? / Follow xem phần 3: / Trần Hưng Đạo, năm 1288 →",
        clips=[
            dict(name="Lại cắm cọc", label="Sông Bạch Đằng · năm 981",
                 img=f"First-person view on a muddy riverbank at low tide in 981, soldiers carrying long sharpened wooden logs, an officer pointing at the riverbed, {ANH_TU} stepping forward proudly with a mallet on his shoulder, realistic, vertical 9:16.",
                 vid="0-5s: An officer shouts to the soldiers carrying long sharpened logs: \"Vua truyền đóng cọc ngăn sông!\" Anh Tư steps forward proudly with a mallet on his shoulder: \"Cắm cọc à? Nhà em có nghề! Ông nội em cắm từ thời Ngô Quyền!\" 5-10s: The officer looks him up and down and says: \"Thế thì cắm nhanh lên, quân Tống sắp đến rồi!\" Anh Tư spits on his hands and starts hammering at lightning speed.",
                 subs=[(0.5, 2.0, "Vua truyền đóng cọc ngăn sông!"),
                       (2.0, 4.9, "Cắm cọc à? Nhà em có nghề! / Ông nội em cắm từ thời Ngô Quyền!"),
                       (5.0, 9.0, "Thế thì cắm nhanh lên, / quân Tống sắp đến rồi!")]),
            dict(name="Vua đi kiểm tra", label="Đêm hôm ấy",
                 img="First-person view at night on a riverbank with torches, year 981, a strong king around 40 in dark armor and a red cloak tapping a wooden stake with his hand, soldiers kneeling, the river dark behind, realistic, vertical 9:16.",
                 vid="0-5s: Torches at night; King Lê Hoàn walks along the riverbank and taps a stake firmly; he nods: \"Cọc chắc đấy. Nhưng lần này ta còn một kế nữa.\" 5-10s: The viewer, kneeling, whispers: \"Dạ... kế gì ạ?\" The king smiles slightly and says: \"Giả hàng.\" Anh Tư, kneeling beside the viewer, looks up confused.",
                 subs=[(0.5, 4.8, "Cọc chắc đấy. / Nhưng lần này ta còn một kế nữa."),
                       (5.0, 6.8, "Dạ... kế gì ạ?"),
                       (6.8, 9.5, "Giả hàng.")]),
            dict(name="Đi xin hàng", label="Sáng hôm sau",
                 img="First-person view from a small boat with a white flag rowing toward a large Song dynasty warship in 981, Vietnamese envoys sitting politely, but every soldier on the boat secretly sharpening a knife under his seat, realistic, vertical 9:16.",
                 vid="0-5s: A small boat with a white flag rows toward the big Song warships; Vietnamese envoys sit politely with bowed heads, but the viewer notices every soldier on board secretly sharpening a knife under the seat. 5-10s: Anh Tư, rowing, whispers: \"Đi đầu hàng mà sao anh em ai cũng mài dao thế?\" The soldier next to him whispers back: \"Hàng thì phải hàng cho chu đáo.\"",
                 subs=[(5.0, 7.5, "Đi đầu hàng mà sao / anh em ai cũng mài dao thế?"),
                       (7.5, 9.8, "Hàng thì phải hàng cho chu đáo.")]),
            dict(name="Cọc lại trúng", label="Vài hôm sau",
                 img="First-person view from a riverbank at falling tide in 981, Song warships with dark sails stuck on wooden stakes and breaking apart, Vietnamese soldiers cheering, a messenger running along the bank, realistic, vertical 9:16.",
                 vid="0-5s: The tide falls; Song warships with dark sails slam into the hidden stakes and crack apart; a messenger runs along the bank shouting: \"Tướng Tống Hầu Nhân Bảo mắc mưu giả hàng, tử trận rồi!\" 5-10s: Anh Tư jumps up and down pointing at a broken ship: \"Cọc nhà em lại trúng nữa rồi! Về khoe ông nội!\"",
                 subs=[(0.5, 4.8, "Tướng Tống Hầu Nhân Bảo / mắc mưu giả hàng, tử trận rồi!"),
                       (5.0, 9.5, "Cọc nhà em lại trúng nữa rồi! / Về khoe ông nội!")]),
        ],
        caption="Ông nội cắm cọc cho Ngô Quyền, cháu cắm cọc cho Lê Hoàn, lần này còn thêm kế \"đầu hàng\" 😂 Năm 981, vua Lê Đại Hành đóng cọc ngăn sông Bạch Đằng và dùng kế giả hàng, quân Tống thua phải rút. Bạn đoán lần cắm cọc thứ ba là của ai? 👇",
        tags="#lehoan #ledaihanh #981",
    ),
    # ------------------------------------------------------------------ 1288
    dict(
        slug="tran-hung-dao-1288", prefix="bd3", title="Trần Hưng Đạo, năm 1288",
        length="50 giây · 5 clip (lời thề, cắm cọc, nhử địch, triều rút, bắt sống tướng giặc)",
        history=("**Lịch sử:** năm 1288, trong cuộc kháng chiến chống Nguyên Mông lần thứ ba, Hưng Đạo Vương Trần "
                 "Quốc Tuấn cho đóng cọc trên sông Bạch Đằng. Theo *Đại Việt sử ký toàn thư*, khi qua sông Hóa ông chỉ "
                 "xuống dòng sông mà thề: **\"Trận này không phá xong giặc Nguyên, thề không về đến sông này nữa!\"** "
                 "Quân ta nhử thủy quân Nguyên vào bãi cọc lúc triều lên. Khi triều rút, thuyền giặc mắc cọc, tướng "
                 "**Ô Mã Nhi bị bắt sống**. Ngày nay, các bãi cọc Bạch Đằng ở Quảng Yên (Quảng Ninh) vẫn còn và là di "
                 "tích quốc gia đặc biệt."),
        setting=("Vietnam, Trần dynasty, spring 1288, the Hóa River and the Bạch Đằng River estuary. Trần soldiers "
                 "with short cropped hair, black-lacquered teeth, brown and dark-red uniforms, the two characters 'Sát "
                 "Thát' tattooed in black ink on their forearms, rattan shields, spears, small fast boats; huge Yuan "
                 "warships with many sails; Hưng Đạo Vương Trần Quốc Tuấn is a dignified commander around 60 with a "
                 "grey beard, in dark armor and a red cloak, holding a sword. Anh Tư (a descendant of the fishermen from "
                 f"938 and 981, looking exactly like them) is {ANH_TU}, with 'Sát Thát' tattooed on his forearm."),
        hook="Ba lần Bạch Đằng · Phần 3: / Bạn cắm cọc cho Trần Hưng Đạo",
        end="Ba lần cắm cọc, cọc giờ ở đâu? / Follow để xem mai bạn nghe / tiếng thơ thần trên sông Như Nguyệt →",
        clips=[
            dict(name="Lời thề trên sông Hóa", label="Sông Hóa · năm 1288",
                 img="First-person view standing among Trần soldiers with 'Sát Thát' tattoos on their forearms on a riverbank, 1288, a dignified commander with a grey beard in dark armor and red cloak pointing his sword at the river, boats waiting, realistic, vertical 9:16.",
                 vid="0-5s: On the bank of the Hóa River, Hưng Đạo Vương points his sword at the water and vows solemnly: \"Trận này không phá xong giặc Nguyên, thề không về đến sông này nữa!\" The soldiers raise their tattooed fists. 5-10s: As they board the boats, Anh Tư whispers to the viewer: \"Thề nặng thế, không thắng thì về kiểu gì?\" A veteran soldier behind them answers flatly: \"Thì thắng.\"",
                 subs=[(0.5, 4.8, "Trận này không phá xong giặc Nguyên, / thề không về đến sông này nữa!"),
                       (5.0, 8.0, "Thề nặng thế, không thắng thì về kiểu gì?"),
                       (8.0, 9.8, "Thì thắng.")]),
            dict(name="Cọc gia truyền", label="Sông Bạch Đằng · triều rút",
                 img=f"First-person view knee-deep in mud at low tide on the Bạch Đằng River, 1288, soldiers driving huge ironwood stakes into the riverbed, {ANH_TU} with a 'Sát Thát' tattoo on his forearm pointing proudly at one spot, an officer frowning, realistic, vertical 9:16.",
                 vid="0-5s: Low tide; soldiers drive huge ironwood stakes into the riverbed; Anh Tư points proudly at one spot and says: \"Chỗ này cụ tổ em cắm năm 938, ông cố em cắm năm 981, giờ đến lượt em!\" 5-10s: The officer frowns: \"Nhà mày cắm cọc ba trăm năm rồi à?\" Anh Tư grins with his chipped tooth: \"Nghề gia truyền anh ạ!\"",
                 subs=[(0.5, 4.8, "Chỗ này cụ tổ em cắm năm 938, / ông cố em cắm năm 981, giờ đến lượt em!"),
                       (5.0, 7.5, "Nhà mày cắm cọc ba trăm năm rồi à?"),
                       (7.5, 9.8, "Nghề gia truyền anh ạ!")]),
            dict(name="Nhử thuyền Nguyên", tiktok="5-10", label="Triều lên",
                 img="First-person view from a small fast boat on a high-tide river in 1288, a huge fleet of Yuan warships with many sails chasing, arrows in the air, the viewer's hands on a paddle, a fisherman with a scar on his eyebrow paddling hard in front, realistic, vertical 9:16.",
                 vid="0-5s: High tide hides the stakes; small Trần boats dash toward the huge Yuan fleet, strike, then turn and flee as planned; the officer shouts: \"Rút! Rút! Nhớ diễn cho giống!\" 5-10s: Anh Tư, paddling like crazy as arrows splash around, shouts back: \"Khỏi dặn! Nhà em sợ thật từ đời cụ rồi!\"",
                 subs=[(0.5, 4.8, "Rút! Rút! Nhớ diễn cho giống!"),
                       (5.0, 9.8, "Khỏi dặn! / Nhà em sợ thật từ đời cụ rồi!")]),
            dict(name="Triều rút", tiktok="bo", label="Giữa trưa · triều rút",
                 img="First-person view from a riverbank at falling tide in 1288, dozens of huge Yuan warships stuck and tilting on massive ironwood stakes poking out of the water, hulls splitting, Trần soldiers charging in small boats, realistic, vertical 9:16.",
                 vid="0-5s: The tide drops fast; the huge Yuan warships grind onto the ironwood stakes, tilt and split open with thunderous cracks; drums roar from both banks. 5-10s: Small Trần boats swarm out from the mangroves; the viewer and Anh Tư paddle forward with the attack, Anh Tư yelling: \"Lên! Lên! Cọc làm phần việc của nó rồi!\"",
                 subs=[(5.0, 9.5, "Lên! Lên! / Cọc làm phần việc của nó rồi!")]),
            dict(name="Bắt sống Ô Mã Nhi", label="Chiều hôm ấy",
                 img="First-person view at the river's edge in 1288, Trần soldiers pulling a soaked Yuan admiral in ornate armor out of the water, wrecked warships behind, a fisherman with a scar on his eyebrow and a 'Sát Thát' tattoo grinning at the camera, realistic, vertical 9:16.",
                 vid="0-5s: Soldiers drag a soaked Yuan admiral in ornate armor out of the river; someone shouts: \"Bắt sống Ô Mã Nhi rồi!\" Everyone cheers. 5-10s: Anh Tư walks up to the dripping admiral, points at the broken ship behind him and says cheerfully: \"Cái cọc đâm thuyền ông là của nhà tôi đấy. Ba đời rồi!\"",
                 subs=[(0.5, 4.5, "Bắt sống Ô Mã Nhi rồi!"),
                       (5.0, 9.8, "Cái cọc đâm thuyền ông là của nhà tôi đấy. / Ba đời rồi!")]),
        ],
        caption="Ba trăm năm, ba đời nhà Anh Tư, ba lần cắm cọc trên cùng một con sông 🔥 Năm 1288, Trần Hưng Đạo đánh tan thủy quân Nguyên trên sông Bạch Đằng, bắt sống Ô Mã Nhi. Các bãi cọc ở Quảng Yên (Quảng Ninh) đến nay vẫn còn. Bạn đã đến xem bãi cọc Bạch Đằng chưa? 👇",
        tags="#tranhungdao #1288 #satthat",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#balanbachdang #bachdang", note=NOTE)
