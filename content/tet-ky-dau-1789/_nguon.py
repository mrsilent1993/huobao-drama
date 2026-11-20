#!/usr/bin/env python3
"""Tết Kỷ Dậu 1789: loạt 3 phần (ăn Tết sớm · ngủ trên võng · rơm ướt). Chuẩn 7 clip, YouTube 60–70s, TikTok 30–35s.
Nối với loạt Tây Sơn từng mốc (rút về Tam Điệp, đêm Hà Hồi, cầu phao mùng 5). Chạy: python3 _nguon.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tay-son-tung-moc"))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build, MUC_MOI  # noqa: E402
from _nguon import FACE, QING_EN, QING_VIS  # noqa: E402
FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a chipped front tooth; he acts naturally and understated, like a real person, not a performer")

GIONG = "Central Vietnamese (Huế) accent"
ARMY = ("Tây Sơn soldiers with black-lacquered teeth in dark-red uniforms with red head wraps, spears and swords")
KING = "the emperor Quang Trung, seen ONLY from behind or far away, a broad-shouldered figure in a dark battle robe"
NOTE = ("**Tết Kỷ Dậu 1789 (3 phần):** ba chuyện truyền tụng về Tết năm ấy, kể theo công thức Anh Tư, nối với loạt Tây Sơn "
        "từng mốc. Vua Quang Trung chỉ xuất hiện từ phía sau hoặc từ xa; quân Thanh chỉ là bối cảnh, không cảnh chết. "
        "**Hai video từ cùng 7 clip:** YouTube khoảng 67 giây, TikTok khoảng 35 giây, vẫn đủ 7 cảnh.")
LEN = ("hai video từ cùng 7 clip: **YouTube** khoảng 67 giây và **TikTok** khoảng 35 giây, vẫn đủ 7 cảnh (mỗi clip lấy "
       "khoảng 5 giây chứa câu chính, cảnh cuối 7 giây)")
COMMON = dict(length=LEN, muc=MUC_MOI, giong=GIONG, end_secs=1.6, visual=QING_VIS)
YT_BASE = ("quang trung, tết kỷ dậu 1789, tây sơn, ngọc hồi đống đa, đại phá quân thanh, tây sơn từng mốc, lịch sử việt "
           "nam, pov lịch sử, anh tư, đại việt, shorts")

EPISODES = [
    # ================================================================== Phần 1/3: Ăn Tết sớm
    dict(COMMON,
        slug="an-tet-som-tam-diep-1789", prefix="tkd1",
        voices={"officer": "a stern, clipped male voice", "Quang Trung": "a strong, commanding male voice, fiery and confident",
                "comrade": "a cheeky young adult male voice"},
        title="Phần 1/3 · Chưa đến giao thừa đã bị bắt ăn Tết, ăn xong thì… xuất quân (Tam Điệp, Tết Kỷ Dậu 1789)",
        history=("**Lịch sử:** cuối năm Mậu Thân, vua Quang Trung kéo quân ra Bắc, dừng ở Tam Điệp (Ninh Bình). Theo *Hoàng "
                 "Lê nhất thống chí*, vua cho khao quân, **ăn Tết trước**, rồi hẹn đến **mùng 7 Tết vào thành Thăng Long mở "
                 "tiệc ăn mừng**; đêm 30 Tết quân chia đường tiến ra Bắc (mức B/C: *Hoàng Lê nhất thống chí* là tiểu thuyết "
                 "lịch sử viết gần thời ấy). **Hư cấu:** Anh Tư, chuyện mang bánh chưng và mọi lời thoại (lời vua phỏng theo "
                 "ý sách chép)."),
        setting=("Vietnam, the last day of the lunar year (late January 1789), a huge army camp in the limestone passes of "
                 "Tam Điệp (Ninh Bình), cold mist, campfires, piles of square bánh chưng wrapped in green dong leaves, pots "
                 f"of rice, jars of rice wine. {ARMY}. {KING}. Anh Tư is {FACE}, a Tây Sơn soldier. Adults only, no "
                 "children. No flags, no legible writing, no modern objects."),
        hook="POV: Chưa giao thừa / đã bị bắt / ăn Tết",
        end="Follow để xem / phần 2/3: ngủ trên võng →",
        clips=[
            dict(name="Ăn Tết!", tiktok="0-5", label="Tam Điệp · cuối năm Mậu Thân",
                 img=f"First-person view in a misty mountain army camp, a stern officer pointing at a huge pile of bánh chưng and jars of rice wine, {FACE} beside the viewer, confused, realistic, vertical 9:16.",
                 vid=("0-5s: The officer points at piles of bánh chưng: \"Tối nay ăn Tết.\" Anh Tư: \"Giao thừa còn chưa tới "
                      "mà ạ?\" The officer: \"Đợi giao thừa thì muộn.\" 5-10s: Anh Tư stares at the food and whispers: \"Tết chưa đến... "
                      "đã bị bắt ăn.\""),
                 subs=[(0.3, 2.0, "Tối nay ăn Tết."),
                       (2.0, 3.4, "Giao thừa còn chưa tới / mà ạ?"),
                       (3.4, 4.9, "Đợi giao thừa / thì muộn."),
                       (5.2, 9.5, "Tết chưa đến... / đã bị bắt ăn.")]),
            dict(name="Ăn nhanh", tiktok="5-10", label="",
                 img=f"First-person view by a campfire, soldiers gulping down slices of bánh chưng, the officer walking past clapping his hands to hurry them, {FACE} with his cheeks stuffed, realistic, vertical 9:16.",
                 vid=("0-5s: The officer walks past clapping: \"Ăn nhanh! Ăn cho no!\" Soldiers gulp down bánh chưng. 5-10s: "
                      "Anh Tư, cheeks stuffed, to the viewer: \"Lần đầu em ăn Tết... mà vội như ăn vụng.\""),
                 subs=[(0.5, 4.8, "Ăn nhanh! / Ăn cho no!"),
                       (5.0, 9.5, "Lần đầu em ăn Tết... / mà vội như ăn vụng.")]),
            dict(name="Lời hẹn", tiktok="5-10", label="",
                 img=f"First-person view from among the soldiers, {KING} standing on a rock above the campfires addressing the army, soldiers raising their cups, {FACE} with a cup halfway to his mouth, realistic, vertical 9:16.",
                 vid=("0-5s: From a rock above the camp, the emperor, seen only from behind, calls out: \"Ăn Tết trước! Mùng "
                      "bảy vào Thăng Long ăn Tết tiếp!\" The army roars. 5-10s: Anh Tư, cup in hand, whispers: \"Tết năm nay... "
                      "ăn hai lần ạ?\""),
                 subs=[(0.5, 4.8, "Ăn Tết trước! / Mùng bảy vào Thăng Long / ăn Tết tiếp!"),
                       (5.0, 9.5, "Tết năm nay... / ăn hai lần ạ?")]),
            dict(name="Đòi lại Tết", tiktok="5-10", label="",
                 img=f"First-person view by the fire, a cheeky young comrade whispering to {FACE} and pointing north toward the dark mountains, Anh Tư suddenly serious, realistic, vertical 9:16.",
                 vid=("0-5s: The comrade whispers: \"Thăng Long giờ quân Thanh đang ăn Tết đấy.\" 5-10s: Anh Tư puts down his "
                      "bánh chưng and says to the viewer: \"Ăn Tết trước... để còn kịp ra Thăng Long đòi lại Tết.\""),
                 subs=[(0.5, 4.8, "Thăng Long giờ / quân Thanh đang ăn Tết đấy."),
                       (5.0, 9.5, "Ăn Tết trước... / để còn kịp ra Thăng Long / đòi lại Tết.")]),
            dict(name="Không mang bánh", tiktok="5-10", label="",
                 img=f"First-person view as {FACE} secretly stuffs two bánh chưng into his pack, the stern officer catching his wrist and shaking his head, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư sneaks two bánh chưng into his pack. The officer catches his wrist: \"Không mang. Mùng bảy "
                      "ăn ở Thăng Long.\" 5-10s: Anh Tư puts them back and tells the viewer: \"Bỏ bánh chưng lại... thì phải "
                      "thắng thật rồi.\""),
                 subs=[(0.5, 4.8, "Không mang. / Mùng bảy ăn ở Thăng Long."),
                       (5.0, 9.5, "Bỏ bánh chưng lại... / thì phải thắng thật rồi.")]),
            dict(name="Giao thừa trên đường", tiktok="5-10", label="",
                 img=f"First-person view at midnight, long columns of soldiers with torches marching out of the camp into the dark mountain pass, {FACE} looking back at the dying campfires, realistic, vertical 9:16.",
                 vid=("0-5s: Midnight; long columns of torches march out into the dark pass, drums beating softly. 5-10s: Anh "
                      "Tư looks back at the dying campfires: \"Giao thừa năm nay... em đón ở trên đường.\""),
                 subs=[(5.0, 9.5, "Giao thừa năm nay... / em đón ở trên đường.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view at dawn on a road north, {FACE} marching with his spear, chewing the last piece of bánh chưng, looking at the camera, realistic, vertical 9:16.",
                 vid=("0-4.5s: Dawn on the road north. A calm narrator's voice says: \"Cuối năm Mậu Thân, vua Quang Trung cho quân "
                      "ăn Tết sớm ở Tam Điệp, hẹn mùng bảy vào Thăng Long.\" 4.5-10s: Anh Tư says to the camera, chewing: "
                      "\"Tết này em ăn trước... trả sau.\""),
                 subs=[(3.0, 6.0, "Vua Quang Trung cho quân / ăn Tết sớm, hẹn mùng bảy / vào Thăng Long."),
                       (6.1, 8.4, "Tết này em ăn trước... / trả sau.")]),
        ],
        caption=("Chưa đến giao thừa đã bị bắt ăn Tết, ăn xong thì xuất quân 😳 Cuối năm Mậu Thân, vua Quang Trung cho quân ăn "
                 "Tết sớm ở Tam Điệp và hẹn mùng 7 vào Thăng Long ăn Tết tiếp. Bạn nghĩ vua có giữ được lời hẹn không? 👇"),
        tags="#tetkydau #quangtrung #taysontungmoc #antetsom #1789",
        tt_title="Chưa giao thừa đã bị bắt ăn Tết, ăn xong thì xuất quân",
        hooks_alt=["POV: Ăn Tết trước / để còn đòi lại Tết", "POV: Tết năm nay / ăn hai lần"],
        pin=("Vua Quang Trung hẹn mùng 7 vào Thăng Long ăn Tết 🔥 Đoán xem quân Tây Sơn tới sớm hay muộn? Phần 2: ngủ trên võng, "
             "follow để xem!"),
        yt_title="Tết Kỷ Dậu 1789 (1/3): ăn Tết sớm ở Tam Điệp | Tây Sơn từng mốc",
        yt_tags="ăn tết sớm, tam điệp, " + YT_BASE,
    ),
    # ================================================================== Phần 2/3: Ngủ trên võng
    dict(COMMON,
        slug="ngu-tren-vong-1789", prefix="tkd2", legend=True,
        voices={"officer": "a stern, clipped male voice", "comrade": "a cheeky young adult male voice",
                "old woman": "a warm, croaky old woman's voice"},
        title="Phần 2/3 · Đang hành quân đánh giặc thì bị lệnh… nằm ngủ (ba người một võng, Tết Kỷ Dậu 1789)",
        history=("**Lịch sử:** từ Tam Điệp, quân Tây Sơn tiến ra Bắc rất nhanh: đêm mùng 3 Tết đã vây đồn Hà Hồi, sáng mùng 5 "
                 "đánh đồn Ngọc Hồi (mức B). **Truyền tụng (mức C):** để đi nhanh mà không kiệt sức, quân chia ba người một "
                 "tốp, hai người khiêng võng, một người nằm nghỉ, cứ thế thay nhau đi cả ngày lẫn đêm. Chưa có chính sử chép "
                 "rõ chi tiết này, nên video gắn nhãn \"theo truyền tụng\". **Hư cấu:** Anh Tư, người đồng đội ngáy to, bà "
                 "cụ bên đường và mọi lời thoại."),
        setting=("Vietnam, the first days of the lunar new year 1789, a winding dirt road through northern rice fields and "
                 "villages, cold drizzle and mist, day and night. Long columns of Tây Sơn soldiers moving fast, in groups of "
                 "three: two men carrying a hammock slung on a bamboo pole on their shoulders, the third asleep in the "
                 f"hammock, swapping turns. {ARMY}. Anh Tư is {FACE}. Adults only, no children. No flags, no legible "
                 "writing, no modern objects."),
        hook="POV: Đi đánh giặc / mà bị lệnh / nằm ngủ",
        end="Follow để xem / phần 3/3: rơm ướt →",
        clips=[
            dict(name="Lệnh ngủ", tiktok="0-5", label="Hành quân ra Bắc · Tết 1789",
                 img=f"First-person view on a misty road, a stern officer handing a hammock on a long bamboo pole to {FACE} and a comrade, columns of soldiers passing, realistic, vertical 9:16.",
                 vid=("0-5s: The officer hands over a hammock on a bamboo pole: \"Ba người một võng. Hai khiêng, một ngủ.\" "
                      "Anh Tư: \"Ngủ... lúc đi đánh giặc ạ?\" The officer: \"Ngủ để còn đi. Nằm xuống!\" 5-10s: Anh Tư whispers to the "
                      "viewer: \"Lần đầu em thấy có lệnh... bắt ngủ.\""),
                 subs=[(0.3, 2.4, "Ba người một võng. / Hai khiêng, một ngủ."),
                       (2.4, 3.4, "Ngủ... / lúc đi đánh giặc ạ?"),
                       (3.4, 4.9, "Ngủ để còn đi. / Nằm xuống!"),
                       (5.2, 9.5, "Lần đầu em thấy có lệnh... / bắt ngủ.")]),
            dict(name="Võng đưa", tiktok="5-10", label="",
                 img=f"First-person view from inside a swaying hammock carried on a bamboo pole by two soldiers, grey sky and bare trees passing above, {FACE} lying back eyes half closed, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư lies in the hammock swaying gently as two comrades jog along the road. 5-10s: Eyes half "
                      "closed, he murmurs: \"Võng đưa... êm hơn giường nhà em.\""),
                 subs=[(5.0, 9.5, "Võng đưa... / êm hơn giường nhà em.")]),
            dict(name="Đổi!", tiktok="5-10", label="",
                 img=f"First-person view as {FACE} now carries the front of the bamboo pole on his shoulder, behind him a comrade asleep in the hammock with his mouth wide open, realistic, vertical 9:16.",
                 vid=("0-5s: \"Đổi!\" Anh Tư is tipped out of the hammock and takes the front of the pole; his comrade flops in "
                      "and immediately snores loudly. 5-10s: Anh Tư, carrying, to the viewer: \"Đến lượt em khiêng... nó ngáy "
                      "to hơn cả trống trận.\""),
                 subs=[(0.5, 4.8, "Đổi!"),
                       (5.0, 9.5, "Đến lượt em khiêng... / nó ngáy to hơn / cả trống trận.")]),
            dict(name="Một phần ba", tiktok="5-10", label="",
                 img=f"First-person wide view at night of an endless column of torches on the road, every third man asleep in a swinging hammock, {FACE} carrying a pole and counting on his fingers, realistic, vertical 9:16.",
                 vid=("0-5s: At night an endless column of torches moves fast along the road; in every group one man sleeps in "
                      "a swinging hammock. 5-10s: Anh Tư counts on his fingers and tells the viewer: \"Cả đạo quân đi ngày đi "
                      "đêm... mà lúc nào cũng có một phần ba đang ngủ.\""),
                 subs=[(5.0, 9.5, "Cả đạo quân đi ngày đi đêm... / mà lúc nào cũng có / một phần ba đang ngủ.")]),
            dict(name="Bà cụ bên đường", tiktok="5-10", label="",
                 img=f"First-person view at dawn by a village gate, an old woman offering a bowl of water to the passing soldiers, {FACE} taking it while still carrying the hammock pole, realistic, vertical 9:16.",
                 vid=("0-5s: At dawn an old woman at a village gate offers water: \"Quân đi đâu mà nhanh thế các con?\" 5-10s: "
                      "Anh Tư gulps the water and answers: \"Đi ăn Tết bà ạ. Mùng bảy... ở Thăng Long.\""),
                 subs=[(0.5, 4.8, "Quân đi đâu / mà nhanh thế các con?"),
                       (5.0, 9.5, "Đi ăn Tết bà ạ. / Mùng bảy... ở Thăng Long.")]),
            dict(name="Ngủ đủ giấc", tiktok="5-10", label="",
                 img=f"First-person view at night from a dark field, a distant enemy fort glowing with lanterns and firecrackers, {QING_EN}, {FACE} in the foreground springing out of a hammock, wide awake, realistic, vertical 9:16.",
                 vid=("0-5s: Night; in the distance an enemy fort glows with lanterns and firecrackers. Anh Tư springs out of "
                      "the hammock, wide awake. 5-10s: He whispers to the viewer: \"Giặc ăn Tết thức trắng... quân mình thì ngủ "
                      "đủ giấc.\""),
                 subs=[(5.0, 9.5, "Giặc ăn Tết thức trắng... / quân mình thì ngủ đủ giấc.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view at dawn, {FACE} rolling up the hammock and tying it to his pack, fresh and alert, soldiers forming up behind him, realistic, vertical 9:16.",
                 vid=("0-4.5s: Dawn. A calm narrator's voice says: \"Theo truyền tụng, quân Tây Sơn đi ba người một võng, thay "
                      "nhau khiêng, ngày đêm không nghỉ.\" 4.5-10s: Anh Tư rolls up the hammock and says to the camera: \"Đi "
                      "đánh giặc... mà em ngủ nhiều hơn ở nhà.\""),
                 subs=[(3.0, 6.0, "Theo truyền tụng: / ba người một võng, / ngày đêm không nghỉ."),
                       (6.1, 8.4, "Đi đánh giặc... / mà em ngủ nhiều hơn ở nhà.")]),
        ],
        caption=("Đang hành quân đánh giặc thì bị lệnh nằm ngủ 😂 Theo truyền tụng, Tết Kỷ Dậu 1789 quân Tây Sơn đi ba người một "
                 "võng, hai người khiêng một người ngủ, thay nhau đi ngày đêm. Bạn muốn khiêng hay muốn nằm? 👇"),
        tags="#tetkydau #quangtrung #taysontungmoc #bananguoimotvong #1789",
        tt_title="Đang hành quân đánh giặc thì bị lệnh nằm ngủ",
        hooks_alt=["POV: Ba người một võng / hai khiêng một ngủ", "POV: Giặc thức trắng / quân mình ngủ đủ giấc"],
        pin=("Ba người một võng là chuyện truyền tụng, sử chưa chép rõ, nhưng tốc độ hành quân thần tốc thì có thật 🔥 Phần 3: "
             "rơm ướt, follow để xem!"),
        yt_title="Tết Kỷ Dậu 1789 (2/3): ba người một võng, hành quân thần tốc | Tây Sơn từng mốc",
        yt_tags="ba người một võng, hành quân thần tốc, " + YT_BASE,
    ),
    # ================================================================== Phần 3/3: Rơm ướt
    dict(COMMON,
        slug="rom-uot-ngoc-hoi-1789", prefix="tkd3",
        voices={"officer": "a stern, clipped male voice", "comrade": "a cheeky young adult male voice"},
        title="Phần 3/3 · Tết rét căm căm bị sai nhúng rơm vào nước, sáng ra mới biết để làm gì (Ngọc Hồi, mùng 5 Tết 1789)",
        history=("**Lịch sử:** sáng mùng 5 Tết Kỷ Dậu (30/1/1789), quân Tây Sơn đánh đồn Ngọc Hồi (Thanh Trì, Hà Nội). Theo "
                 "*Hoàng Lê nhất thống chí*, vua Quang Trung cho **lấy sáu chục tấm ván, ghép ba tấm làm một bức, ngoài phủ rơm dấp nước, tất cả hai mươi bức**, "
                 "nhiều người khiêng một tấm đi trước để chắn tên lửa và súng của quân Thanh, quân cầm dao theo sau (mức "
                 "B/C). Đồn Ngọc Hồi vỡ, quân Thanh tan chạy; **chiều mùng 5 Tết, vua Quang Trung vào Thăng Long**, sớm hơn "
                 "lời hẹn mùng 7 (mức B). **Hư cấu:** Anh Tư, người đồng đội và mọi lời thoại. Chi tiết áo vua đen khói súng (cảnh 6) là truyền tụng, *Hoàng Lê* không chép. Không dựng cảnh chết, chỉ dựng "
                 "tên lửa cắm vào tấm rơm ướt và quân Thanh bỏ chạy."),
        setting=("Vietnam, dawn of the fifth day of the lunar new year (30 January 1789), cold fog over flat winter rice "
                 "fields, a Qing earthen fort with a wooden palisade at Ngọc Hồi. Tây Sơn soldiers advancing in lines behind "
                 "large wooden board shields covered in thick soaked straw, each carried by many men; fire arrows hissing "
                 f"into the wet straw and fizzling out with steam. {ARMY}. {QING_EN} {KING}, riding a war elephant far "
                 f"behind the lines. Anh Tư is {FACE}. Adults only, no children. No blood, no dead bodies, no flags, no "
                 "legible writing."),
        hook="POV: Tết rét căm căm / bị sai / nhúng rơm vào nước",
        end="Follow để xem / Tây Sơn từng mốc / tập tiếp theo →",
        clips=[
            dict(name="Nhúng rơm", tiktok="0-5", label="Ngọc Hồi · mùng 5 Tết 1789",
                 img=f"First-person view before dawn by a pond in freezing fog, a stern officer pointing at piles of straw and large wooden boards, {FACE} beside the viewer shivering, realistic, vertical 9:16.",
                 vid=("0-5s: In freezing fog the officer points at straw and wooden boards: \"Nhúng rơm. Bọc kín tấm ván.\" Anh "
                      "Tư, shivering: \"Rét thế này... nhúng nước ạ?\" The officer: \"Sáng mai mày sẽ cảm ơn nó.\" 5-10s: Anh Tư dunks an armful "
                      "of straw into the icy pond and gasps: \"Tết rét căm căm... em đi dầm rơm.\""),
                 subs=[(0.3, 2.4, "Nhúng rơm. / Bọc kín tấm ván."),
                       (2.4, 3.4, "Rét thế này... / nhúng nước ạ?"),
                       (3.4, 4.9, "Sáng mai / mày sẽ cảm ơn nó."),
                       (5.2, 9.5, "Tết rét căm căm... / em đi dầm rơm.")]),
            dict(name="Rơm ướt nặng", tiktok="5-10", label="",
                 img=f"First-person view as many soldiers lift a huge wooden board shield covered in dripping wet straw onto their shoulders, {FACE} at one corner straining, water running down his back, realistic, vertical 9:16.",
                 vid=("0-5s: Many soldiers heave a huge board covered in dripping straw onto their shoulders; cold water runs "
                      "down their backs. 5-10s: Anh Tư, straining, to the viewer: \"Rơm ướt nặng gấp mấy rơm khô... mà lưng "
                      "em thì chỉ có một.\""),
                 subs=[(5.0, 9.5, "Rơm ướt nặng / gấp mấy rơm khô... / mà lưng em chỉ có một.")]),
            dict(name="Tiến vào sương", tiktok="5-10", label="",
                 img=f"First-person view from behind a wet straw board shield advancing through thick fog toward a dim enemy palisade, {FACE} peeking around the edge, realistic, vertical 9:16.",
                 vid=("0-5s: Behind the dripping board the line advances slowly through thick fog toward the dim palisade; "
                      "drums thud. 5-10s: Anh Tư peeks around the edge and whispers: \"Sương mù thế này... giặc chỉ thấy một bức "
                      "tường rơm đi tới.\""),
                 subs=[(5.0, 9.5, "Sương mù thế này... / giặc chỉ thấy / một bức tường rơm đi tới.")]),
            dict(name="Xèo!", tiktok="5-10", label="",
                 img=f"Close first-person view from behind the board shield as flaming arrows thud into the thick wet straw and fizzle out in puffs of white steam, {FACE} flinching then exhaling, realistic, vertical 9:16.",
                 vid=("0-5s: Fire arrows thud into the wet straw one after another; each fizzles out with a hiss and a puff of "
                      "steam. 5-10s: Anh Tư says quietly to the viewer: \"Cả đời em nhóm bếp ghét rơm ướt... hôm nay rơm ướt cứu cả "
                      "đạo quân.\""),
                 subs=[(0.5, 4.8, "Xèo! Xèo!"),
                       (5.0, 9.5, "Cả đời em nhóm bếp / ghét rơm ướt... / hôm nay rơm ướt / cứu cả đạo quân.")]),
            dict(name="Đồn vỡ", tiktok="5-10", label="",
                 img=f"First-person wide view as the Tây Sơn lines drop their straw shields at the palisade and surge through the broken gate, {QING_EN} running away into the fog in the distance, {FACE} cheering, no blood, realistic, vertical 9:16.",
                 vid=("0-5s: The lines drop the boards at the palisade and surge through the broken gate; in the distance Qing "
                      "soldiers run away into the fog. No blood, no bodies. 5-10s: Anh Tư wrings water out of his shirt: \"Đồn "
                      "vỡ rồi... mà áo em còn chưa kịp khô.\""),
                 subs=[(5.0, 9.5, "Đồn vỡ rồi... / mà áo em còn chưa kịp khô.")]),
            dict(name="Áo vua đen khói", tiktok="5-10", label="",
                 img=f"First-person view through drifting smoke, {KING} on a war elephant, his dark robe blackened with gunpowder smoke, moving forward at the head of the army, {FACE} watching in awe, realistic, vertical 9:16.",
                 vid=("0-5s: Through drifting smoke the emperor, seen only from behind on a war elephant, moves forward at the "
                      "head of the army, his robe blackened by gunpowder smoke. 5-10s: Anh Tư whispers: \"Áo vua đen sì khói "
                      "súng... mà vẫn đi đầu.\""),
                 subs=[(5.0, 9.5, "Áo vua đen sì khói súng... / mà vẫn đi đầu.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view in the afternoon at a city gate of Thăng Long, Tây Sơn soldiers marching in, townspeople coming out of doorways, {FACE} counting on his fingers, realistic, vertical 9:16.",
                 vid=("0-4.5s: Afternoon at a Thăng Long city gate; soldiers march in and townspeople come out. A calm narrator's "
                      "voice says: \"Mùng 5 Tết Kỷ Dậu, quân Tây Sơn phá đồn Ngọc Hồi. Chiều hôm ấy, vua Quang Trung vào Thăng "
                      "Long.\" 4.5-10s: Anh Tư counts on his fingers, shaking his head: \"Hẹn mùng bảy ăn Tết ở Thăng Long... mùng năm "
                      "đã tới.\""),
                 subs=[(3.0, 6.0, "Mùng 5 Tết, phá đồn Ngọc Hồi. / Chiều hôm ấy, vua Quang Trung / vào Thăng Long."),
                       (6.1, 8.4, "Hẹn mùng bảy... / mùng năm đã tới.")]),
        ],
        caption=("Tết rét căm căm bị sai nhúng rơm vào nước, sáng ra mới biết để làm gì 😳 Mùng 5 Tết Kỷ Dậu 1789, quân Tây Sơn "
                 "khiêng tấm ván bọc rơm ướt đi trước, tên lửa bắn vào chỉ xèo một tiếng. Chiều hôm ấy vua Quang Trung đã vào "
                 "Thăng Long, sớm hơn lời hẹn hai ngày. Bạn thích phần nào nhất trong 3 phần? 👇"),
        tags="#tetkydau #quangtrung #ngochoidongda #taysontungmoc #1789",
        tt_title="Tết rét căm căm bị sai nhúng rơm vào nước, sáng ra mới biết để làm gì",
        hooks_alt=["POV: Hẹn mùng bảy / mùng năm đã tới", "POV: Rơm ướt / cứu cả đạo quân"],
        pin=("Hẹn mùng 7, mùng 5 đã vào Thăng Long 🔥 Xem lại phần 1 (ăn Tết sớm) và phần 2 (ngủ trên võng) trên trang của "
             "kênh nhé!"),
        yt_title="Tết Kỷ Dậu 1789 (3/3): tấm ván bọc rơm ướt ở Ngọc Hồi | Tây Sơn từng mốc",
        yt_tags="rơm ướt, tấm mộc rơm, đồn ngọc hồi, " + YT_BASE,
    ),
]

ACTING = ("Acting: natural and understated, like real people filmed in a documentary; small reactions (a sigh, a glance, a pause, a shake of the head) instead of big expressions. Anh Tư smiles at most once in the whole clip and never laughs at the camera; no exaggerated mugging or cartoonish faces.")
for _ep in EPISODES:
    _ep["setting"] = _ep["setting"] + " " + ACTING
    for _c in _ep["clips"]:
        if _c.get("setting"):
            _c["setting"] = _c["setting"] + " " + ACTING


if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#taysontungmoc #anhtu", note=NOTE, unit="Phần", file_unit="phan")
