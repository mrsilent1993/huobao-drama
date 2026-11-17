#!/usr/bin/env python3
"""Nguồn của loạt "Bạch Đằng ngoại truyện" (50–60 giây). Sửa ở đây rồi chạy: python3 _nguon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

ANH_TU = ("a shirtless Vietnamese fisherman around 30 with deeply tanned skin, hair in a topknot, a scar across "
          "his left eyebrow and a wide grin with a chipped front tooth")

NOTE = ("**Anh Tư** (nhân vật của loạt \"Ba lần Bạch Đằng\") xuất hiện ở cả ba tập: sẹo ngang lông mày trái, răng "
        "cửa mẻ, cười toe. Dùng lại ảnh chân dung Anh Tư làm ảnh tham chiếu trong Muse.")

EPISODES = [
    # ------------------------------------------------------------------ 1
    dict(
        slug="linh-nam-han-938", prefix="ngt1", title="Bạn là lính Nam Hán theo Hoằng Tháo, năm 938",
        length="50 giây · 5 clip (từ lúc tự tin đến lúc ôm tấm ván giữa sông)",
        history=("**Lịch sử:** năm 937, Kiều Công Tiễn giết Dương Đình Nghệ rồi cầu cứu nhà Nam Hán. Vua Nam Hán sai "
                 "con là **Hoằng Tháo** đem thủy quân sang. Nhưng trước khi quân Nam Hán tới, **Ngô Quyền đã giết Kiều "
                 "Công Tiễn**. Ngô Quyền cho cắm cọc ở cửa sông Bạch Đằng, nhử thuyền giặc vào lúc triều lên. Triều rút, "
                 "thuyền giặc mắc cọc và vỡ, quá nửa quân chết đuối, **Hoằng Tháo tử trận**."),
        setting=("Southern Han dynasty war fleet, year 938, sailing into the Bạch Đằng River estuary in northern "
                 "Vietnam: large wooden warships with red sails and rows of oars; Southern Han soldiers and oarsmen in "
                 "dark red tunics and leather armor (the viewer is a young oarsman); Prince Hoằng Tháo is an arrogant "
                 "young commander around 20 in shiny gilded armor and a plumed helmet; a wide tidal river with muddy "
                 f"banks and mangroves. On the Vietnamese bank, Anh Tư is {ANH_TU}."),
        hook="POV: Bạn là lính giặc / ở sông Bạch Đằng năm 938",
        end="Hoằng Tháo có thoát được không? / Follow để xem mai bạn đốn gỗ / làm cọc cho Trần Hưng Đạo →",
        clips=[
            dict(name="Được mời sang", label="Trên biển · năm 938",
                 img="First-person view of an oarsman on a large wooden warship with red sails at sea, 938, rows of oars, an arrogant young prince in shiny gilded armor and a plumed helmet standing at the bow with arms raised, realistic, vertical 9:16.",
                 vid="0-5s: On the deck of a big red-sailed warship, Prince Hoằng Tháo raises his arms and shouts to the rowers: \"Kiều Công Tiễn mời ta sang! Giao Châu coi như nằm trong túi!\" The soldiers cheer. 5-10s: The viewer, rowing, whispers to the oarsman next to him: \"Được người ta mời sang đánh nhà người ta... nghe cứ sai sai.\"",
                 subs=[(0.5, 4.8, "Kiều Công Tiễn mời ta sang! / Giao Châu coi như nằm trong túi!"),
                       (5.0, 9.8, "Được người ta mời sang đánh nhà người ta... / nghe cứ sai sai.")]),
            dict(name="Người mời đã mất", label="Gần cửa sông Bạch Đằng",
                 img="First-person view on a warship deck near a river mouth, 938, a scout climbing aboard from a small boat and kneeling before an arrogant young prince in gilded armor, whose smile freezes, realistic, vertical 9:16.",
                 vid="0-5s: A scout climbs aboard from a small boat and kneels: \"Bẩm... Kiều Công Tiễn bị Ngô Quyền giết rồi ạ!\" The prince's smile freezes. 5-10s: Hoằng Tháo waves it off: \"Thì ta tự vào!\" The viewer mutters to himself: \"Người mời mình mất rồi mà vẫn đến ăn cỗ à?\"",
                 subs=[(0.5, 4.8, "Bẩm... Kiều Công Tiễn / bị Ngô Quyền giết rồi ạ!"),
                       (5.0, 7.0, "Thì ta tự vào!"),
                       (7.0, 9.8, "Người mời mình mất rồi / mà vẫn đến ăn cỗ à?")]),
            dict(name="Có cái gì nhọn nhọn", label="Cửa sông · triều lên",
                 img="First-person view from a warship on a wide calm high-tide river, 938, small Vietnamese canoes fleeing upstream, the viewer leaning over the side looking down at a dark pointed shape just under the water's surface, realistic, vertical 9:16.",
                 vid="0-5s: High tide; small Vietnamese canoes dart out, attack, then flee upstream; Hoằng Tháo laughs: \"Quân Nam yếu thế này à! Đuổi theo!\" 5-10s: As the fleet surges forward, the viewer leans over the side and sees a dark pointed tip just under the water; he calls out: \"Ơ... dưới nước có cái gì nhọn nhọn...\" Nobody listens; drums drown him out.",
                 subs=[(0.5, 4.8, "Quân Nam yếu thế này à! Đuổi theo!"),
                       (5.0, 9.8, "Ơ... dưới nước / có cái gì nhọn nhọn...")]),
            dict(name="Triều rút", tiktok="5-10", label="Giữa trưa · triều rút",
                 img="First-person view on a tilting warship deck at falling tide, 938, sharpened wooden stakes tipped with iron piercing up through the hull, water gushing in, soldiers falling, other warships cracking nearby, realistic, vertical 9:16.",
                 vid="0-5s: The tide drops fast; with a horrible crunch the ship jolts to a stop as iron-tipped stakes punch up through the hull; water gushes in and the deck tilts. 5-10s: The viewer, clinging to an oar as soldiers slide past, shouts: \"Đã bảo có cái gì nhọn nhọn mà!\"",
                 subs=[(5.0, 9.5, "Đã bảo có cái gì nhọn nhọn mà!")]),
            dict(name="Ôm ván giữa sông", tiktok="0-5", label="Chiều hôm ấy",
                 img=f"First-person view from the water, clinging to a broken plank among floating wreckage on a river, 938, on the muddy riverbank {ANH_TU} waving cheerfully at the viewer, realistic, vertical 9:16.",
                 vid=f"0-5s: The viewer floats among the wreckage, clinging to a broken plank, coughing up water; on the muddy bank, Anh Tư waves cheerfully and shouts: \"Cọc em cắm đấy! Lần sau sang nhà người ta nhớ xem lịch nước!\" 5-10s: The viewer looks at the stakes sticking out of the water all across the river and sighs, paddling weakly with one hand.",
                 subs=[(0.5, 4.8, "Cọc em cắm đấy! / Lần sau sang nhà người ta nhớ xem lịch nước!")]),
        ],
        caption="Được mời sang đánh, đến nơi thì người mời đã mất, rồi còn thấy \"cái gì nhọn nhọn\" dưới nước 😂 Năm 938, Hoằng Tháo dẫn thủy quân Nam Hán vào sông Bạch Đằng và mắc bẫy cọc của Ngô Quyền. Nếu là lính Nam Hán, bạn có dám lên tiếng không? 👇",
        tags="#bachdang #ngoquyen #938 #hoangthao",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="don-go-lam-coc-1288", prefix="ngt2", title="Bạn đốn gỗ làm cọc cho Trần Hưng Đạo, năm 1288",
        length="50 giây · 5 clip (đốn lim, kéo gỗ, đọc con nước, cắm cọc đêm, sáng ra mặt sông phẳng lặng)",
        history=("**Lịch sử:** năm 1288, Hưng Đạo Vương cho đóng cọc gỗ trên sông Bạch Đằng để chặn đường rút của "
                 "thủy quân Nguyên. Khảo cổ ở các bãi cọc Yên Giang, Đồng Vạn Muối, Đồng Má Ngựa (Quảng Yên, Quảng "
                 "Ninh) tìm thấy hàng trăm cọc bằng gỗ lim, táu, vạt nhọn đầu, cắm theo từng hàng. Trận đánh được chọn "
                 "đúng lúc thủy triều rút. **Ông lão đọc con nước trong tập này là nhân vật hư cấu**, đại diện cho kinh "
                 "nghiệm sông nước của dân ven biển."),
        setting=("Vietnam, Trần dynasty, early spring 1288, the Bạch Đằng region: a dense forest of huge ironwood (lim) "
                 "trees; muddy paths with water buffalo; the wide tidal river at night lit only by moonlight. Villagers "
                 "and soldiers with short cropped hair, black-lacquered teeth, brown clothes, some with 'Sát Thát' "
                 "tattooed on their forearms; an officer in a dark-red uniform; a wise old fisherman around 75 with a "
                 f"white beard and a conical hat. Anh Tư is {ANH_TU}, with 'Sát Thát' tattooed on his forearm; the "
                 "viewer is a young villager working with him."),
        hook="POV: Bạn đốn gỗ làm cọc / cho Trần Hưng Đạo năm 1288",
        end="Giặc có vào đúng giờ nước rút không? / Follow để xem mai bạn là lính Nguyên / trên sông Bạch Đằng →",
        clips=[
            dict(name="Đốn lim", label="Rừng lim · đầu xuân 1288",
                 img=f"First-person view in a dense forest of huge ironwood trees, 1288, the viewer's hands gripping a long two-man saw cutting into a massive trunk, {ANH_TU} on the other end of the saw, sweating, an officer watching, realistic, vertical 9:16.",
                 vid="0-5s: The viewer and Anh Tư saw back and forth at a massive ironwood trunk; an officer shouts: \"Mỗi làng nộp một trăm cây lim!\" 5-10s: Anh Tư stops, wipes his sweat and holds up the dull saw: \"Gỗ lim cứng như đá! Cùn ba lưỡi cưa mới đổ được một cây đấy anh ơi!\" The officer hands him a fourth saw without a word.",
                 subs=[(0.5, 4.8, "Mỗi làng nộp một trăm cây lim!"),
                       (5.0, 9.8, "Gỗ lim cứng như đá! / Cùn ba lưỡi cưa mới đổ được một cây!")]),
            dict(name="Kéo gỗ ra sông", label="Đường ra sông",
                 img="First-person view pulling a thick rope over the shoulder on a muddy forest path, 1288, a huge ironwood log dragged by a water buffalo and a line of villagers, the river visible ahead, realistic, vertical 9:16.",
                 vid="0-5s: The viewer, rope over his shoulder, drags a huge ironwood log through the mud alongside a water buffalo; he groans: \"Cây này nặng hơn cả con trâu!\" 5-10s: Anh Tư, pulling just ahead, grins back: \"Con trâu cũng đang nghĩ thế về mày đấy.\" The buffalo turns its head and snorts at the viewer.",
                 subs=[(0.5, 4.8, "Cây này nặng hơn cả con trâu!"),
                       (5.0, 9.5, "Con trâu cũng đang nghĩ thế về mày đấy.")]),
            dict(name="Đọc con nước", tiktok="bo", label="Bờ sông Bạch Đằng · chiều tối",
                 img="First-person view on a riverbank at dusk, 1288, a wise old fisherman with a white beard and conical hat crouching at the water's edge, touching the water and looking at the moon, an officer in a dark-red uniform listening closely, realistic, vertical 9:16.",
                 vid="0-5s: An old fisherman with a white beard dips his hand in the river, looks up at the rising moon and says to the officer: \"Mai nước rút nhanh nhất vào giữa trưa. Giặc vào lúc sáng thì trưa là mắc.\" 5-10s: The officer bows deeply to him; the viewer whispers: \"Ông biết cả giờ nước rút ạ?\" The old man smiles: \"Bảy mươi năm ăn ở trên con sông này, cháu ạ.\"",
                 subs=[(0.5, 4.8, "Mai nước rút nhanh nhất vào giữa trưa. / Giặc vào lúc sáng thì trưa là mắc."),
                       (5.0, 7.0, "Ông biết cả giờ nước rút ạ?"),
                       (7.0, 9.8, "Bảy mươi năm ăn ở / trên con sông này, cháu ạ.")]),
            dict(name="Cắm cọc trong đêm", tiktok="5-10", label="Nửa đêm · nước ròng",
                 img="First-person view at night in moonlight, standing chest-deep in a muddy river at low tide, 1288, the viewer's hands steadying a huge sharpened log while others hammer it, no torches, dark silhouettes working silently, realistic, vertical 9:16.",
                 vid="0-5s: Moonlight only, no torches; the viewer steadies a huge sharpened log while others hammer it into the riverbed in silence; an officer whispers: \"Không đốt đuốc, không nói to. Giặc có tai mắt.\" 5-10s: The viewer takes a step and sinks to his chest in the mud; he whispers in panic: \"Anh Tư ơi... em cắm luôn cả em xuống rồi!\" Anh Tư hauls him out by the arm, shaking with silent laughter.",
                 subs=[(0.5, 4.8, "Không đốt đuốc, không nói to. / Giặc có tai mắt."),
                       (5.0, 9.8, "Anh Tư ơi... / em cắm luôn cả em xuống rồi!")]),
            dict(name="Sáng ra", label="Rạng sáng · triều lên",
                 img="First-person view at dawn on a riverbank, 1288, a wide calm river with a smooth, empty surface and no stakes visible, mist, villagers sitting exhausted and muddy on the bank, a fisherman with a scar on his eyebrow grinning, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; the tide has risen and the river is smooth and empty, not a single stake visible; Anh Tư, covered in mud, admires it: \"Đẹp chưa? Nhìn như chưa có chuyện gì xảy ra.\" 5-10s: The viewer collapses on the bank: \"Ba ngày đốn gỗ, một đêm cắm cọc... giờ thì ngồi chờ.\" Far out at sea, a line of large sails appears on the horizon.",
                 subs=[(0.5, 4.8, "Đẹp chưa? / Nhìn như chưa có chuyện gì xảy ra."),
                       (5.0, 9.8, "Ba ngày đốn gỗ, một đêm cắm cọc... / giờ thì ngồi chờ.")]),
        ],
        caption="Ba ngày đốn lim, một đêm ngâm bùn cắm cọc, sáng ra mặt sông phẳng như chưa có gì xảy ra 😮‍💨 Năm 1288, những hàng cọc lim trên sông Bạch Đằng chờ đúng giờ nước rút. Ngày nay các bãi cọc ở Quảng Yên vẫn còn. Bạn nghĩ cắm một cây cọc lim mất bao lâu? 👇",
        tags="#bachdang #tranhungdao #1288 #baicoc",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug="linh-nguyen-1288", prefix="ngt3", title="Bạn là lính thủy quân Nguyên trên sông Bạch Đằng, năm 1288",
        length="60 giây · 6 clip (chuyện cổ tích ba trăm năm trước thành sự thật)",
        history=("**Lịch sử:** đầu năm 1288, thủy quân Nguyên do **Ô Mã Nhi** chỉ huy rút về theo sông Bạch Đằng. "
                 "Quân Trần nhử thuyền giặc vào bãi cọc lúc triều lên. Khi triều rút, thuyền to mắc cọc, không xoay "
                 "trở được, bị đánh tan. Ô Mã Nhi bị bắt sống. Theo *Đại Việt sử ký toàn thư*, năm sau khi trao trả tù "
                 "binh, thuyền chở Ô Mã Nhi bị đục chìm giữa biển. Chuyện lính Nguyên bàn về \"cọc ba trăm năm trước\" "
                 "là chi tiết hư cấu để gây cười."),
        setting=("Yuan dynasty war fleet, spring 1288, on the Bạch Đằng River in northern Vietnam: huge multi-deck "
                 "wooden warships with many sails; Yuan sailors and soldiers in Mongol-Chinese leather armor and fur-"
                 "trimmed hats (the viewer is a young sailor; an old grizzled sailor around 55 is his friend); Admiral Ô "
                 "Mã Nhi is a burly, bearded, arrogant commander in ornate armor; small fast Trần boats; mangroves and "
                 f"riverbanks with calm Vietnamese villagers watching. On the bank, Anh Tư is {ANH_TU}, with 'Sát Thát' "
                 "tattooed on his forearm."),
        hook="POV: Bạn là lính Nguyên / trên sông Bạch Đằng năm 1288",
        end="Ô Mã Nhi về nước bằng cách nào? / Follow để xem tập sau →",
        clips=[
            dict(name="Chuyện cổ tích", label="Thủy quân Nguyên · năm 1288",
                 img="First-person view on the deck of a huge multi-deck Yuan warship on a river, 1288, a burly bearded admiral in ornate armor boasting with arms spread, a grizzled old sailor beside the viewer coiling a rope, many sails behind, realistic, vertical 9:16.",
                 vid="0-5s: Admiral Ô Mã Nhi spreads his arms on the deck and boasts: \"Thuyền ta to gấp mười thuyền Nam, sợ gì!\" 5-10s: The viewer whispers to the old sailor coiling rope beside him: \"Nghe nói ba trăm năm trước, ở đúng sông này có người mắc cọc...\" The old sailor snorts: \"Chuyện cổ tích của bọn Nam thôi.\"",
                 subs=[(0.5, 4.8, "Thuyền ta to gấp mười thuyền Nam, sợ gì!"),
                       (5.0, 7.5, "Nghe nói ba trăm năm trước, / ở đúng sông này có người mắc cọc..."),
                       (7.5, 9.8, "Chuyện cổ tích của bọn Nam thôi.")]),
            dict(name="Bị chọc", tiktok="bo", label="Sông Bạch Đằng · buổi sáng",
                 img="First-person view from a huge Yuan warship, 1288, small fast Vietnamese boats darting close, soldiers in them shouting and waving, the burly admiral pointing angrily, realistic, vertical 9:16.",
                 vid="0-5s: Small fast Trần boats dart up, shoot a few arrows, then turn and flee; Ô Mã Nhi roars: \"Dám chọc ta à? Đuổi theo!\" 5-10s: The viewer raises a hand nervously: \"Tướng quân ơi... con sông này có tiền sử không tốt lắm ạ.\" The admiral glares at him; the viewer quickly goes back to pulling ropes.",
                 subs=[(0.5, 4.8, "Dám chọc ta à? Đuổi theo!"),
                       (5.0, 9.8, "Tướng quân ơi... / con sông này có tiền sử không tốt lắm ạ.")]),
            dict(name="Dân hai bờ ngồi xem", tiktok="5-10", label="Gần trưa",
                 img=f"First-person view from a Yuan warship moving up a river, 1288, on the muddy bank Vietnamese villagers sitting calmly eating rice balls and watching like an audience, {ANH_TU} among them waving, realistic, vertical 9:16.",
                 vid="0-5s: The fleet chases deeper into the river; along the bank, Vietnamese villagers sit calmly eating rice balls and watching, as if waiting for a show to start. 5-10s: Anh Tư, among them, grins and waves at the viewer. The viewer turns to the old sailor: \"Sao dân hai bên bờ ngồi xem như xem hát thế kia?\" The old sailor stops coiling the rope.",
                 subs=[(5.0, 9.8, "Sao dân hai bên bờ / ngồi xem như xem hát thế kia?")]),
            dict(name="Cổ tích là thật", label="Giữa trưa · triều rút",
                 img="First-person view from a huge Yuan warship at falling tide, 1288, hundreds of sharpened ironwood stakes rising out of the water all across the river around the fleet, sailors staring in horror, realistic, vertical 9:16.",
                 vid="0-5s: The tide drops fast; all across the river, hundreds of sharpened ironwood stakes rise out of the water around the fleet like a forest; the sailors freeze. 5-10s: The old sailor drops his rope and whispers, pale: \"...Hóa ra cổ tích là thật.\" Ships begin grinding onto the stakes with loud cracks.",
                 subs=[(5.0, 9.5, "...Hóa ra cổ tích là thật.")]),
            dict(name="Thuyền to quá", tiktok="5-10", label="Ít phút sau",
                 img="First-person view on a tilting Yuan warship deck, 1288, the hull cracking on stakes, the burly admiral shouting orders while the huge ship cannot turn, small Vietnamese boats swarming in, realistic, vertical 9:16.",
                 vid="0-5s: The ship tilts and cracks; Ô Mã Nhi shouts: \"Bình tĩnh! Quay thuyền lại!\" The giant ship doesn't budge. 5-10s: A helmsman yells back: \"Thuyền to quá, không quay được ạ!\" Small Trần boats swarm in from the mangroves with drums roaring; the viewer jumps overboard.",
                 subs=[(0.5, 4.8, "Bình tĩnh! Quay thuyền lại!"),
                       (5.0, 9.5, "Thuyền to quá, không quay được ạ!")]),
            dict(name="Ba đời rồi", label="Chiều hôm ấy",
                 img=f"First-person view from the water, a hand reaching down from a small Vietnamese boat, 1288, {ANH_TU} with a 'Sát Thát' tattoo grinning and pulling the viewer up, in the background soldiers leading a soaked burly admiral away, realistic, vertical 9:16.",
                 vid="0-5s: In the water among wreckage, a strong tattooed arm reaches down and hauls the viewer into a small boat; it's Anh Tư, grinning: \"Lên đây! Cọc nhà tôi đấy, ba đời rồi!\" 5-10s: The viewer, dripping, looks back: soldiers are leading the soaked Ô Mã Nhi away in ropes. The viewer mutters: \"Lần sau tôi tin chuyện cổ tích...\"",
                 subs=[(0.5, 4.8, "Lên đây! Cọc nhà tôi đấy, ba đời rồi!"),
                       (5.0, 9.5, "Lần sau tôi tin chuyện cổ tích...")]),
        ],
        caption="Ba trăm năm trước ở đúng con sông này có người mắc cọc, và lính Nguyên tưởng đó là chuyện cổ tích 😂 Năm 1288, thủy quân Nguyên của Ô Mã Nhi mắc bẫy cọc trên sông Bạch Đằng, thuyền to quá không quay được. Bạn có biết Ô Mã Nhi về nước bằng cách nào không? 👇",
        tags="#bachdang #tranhungdao #1288 #omanhi",
    ),
    # ------------------------------------------------------------------ 4 (A3 làm lại, chỉ người lớn)
    dict(
        slug="vo-anh-tu-o-nha-938", prefix="ngt4", title="Vợ Anh Tư ở nhà: sáng tiễn chồng ra trận, chiều chưa biết có về (938)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Bối cảnh lịch sử:** năm 938, dân chài và trai tráng ven sông Bạch Đằng theo Ngô Quyền cắm cọc, "
                 "đánh thủy quân Nam Hán. Người ở nhà không có cách nào biết tin, chỉ nghe tiếng trống từ xa và chờ người "
                 "về. **Hư cấu:** vợ Anh Tư, các chị em hàng xóm và mọi lời thoại. **Làm lại bản A3 bị gắn cờ:** bản này "
                 "**chỉ có người lớn trên hình**, không có trẻ em, không có cảnh khóc lóc kéo dài; cảm xúc đến từ sự chờ "
                 "đợi và cú gặp lại có tiếng cười."),
        setting=("Vietnam, year 938, a fishing village on the bank of the Bạch Đằng River: thatched stilt houses, nets "
                 "drying, wooden boats, mangroves, the wide tidal river. Adults only on screen. Women with hair wrapped "
                 "in brown cloth, black-lacquered teeth, brown homespun dresses; Vợ Anh Tư (Anh Tư's wife) is a strong, "
                 "quick-witted woman around 28 with a sharp tongue and warm eyes. Anh Tư is "
                 f"{ANH_TU}."),
        hook="Sáng tiễn chồng ra trận / chiều chưa biết có về",
        end="Sử không ghi tên người chờ ở nhà. / Follow để xem tập sau →",
        clips=[
            dict(name="Tiễn chồng", label="Làng chài ven sông Bạch Đằng · sáng năm 938",
                 img=f"First-person close-up at dawn of a woman's hands pressing rice balls into a banana leaf and tying it with string, {ANH_TU} standing at the door of a thatched stilt house with a wooden mallet on his shoulder, mist on the river, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's hands press rice balls into a banana leaf and tie it tight; Vợ Anh Tư shoves the bundle into Anh Tư's chest: \"Đi cắm cọc gì mà mang cả búa lẫn cơm ba ngày?\" 5-10s: Anh Tư grins with his chipped tooth: \"Người ta không nói. Anh cũng không hỏi.\" He walks off toward the river with the other men; she watches him go, arms crossed.",
                 subs=[(0.5, 4.8, "Đi cắm cọc gì mà mang cả búa / lẫn cơm ba ngày?"),
                       (5.0, 9.5, "Người ta không nói. Anh cũng không hỏi.")]),
            dict(name="Làng toàn đàn bà", tiktok="bo", label="Giữa buổi",
                 img="First-person view in a fishing village at midmorning, women mending nets and hauling a heavy boat up the bank by themselves, laughing, no men in sight, realistic, vertical 9:16.",
                 vid="0-5s: The village has no men left; the women haul a heavy boat up the bank by themselves, mend nets, chop wood. 5-10s: A neighbor wipes her forehead and laughs: \"Đàn ông đi hết, việc của họ mình làm hết. Thế mà cũng xong!\" Vợ Anh Tư laughs too, then glances at the river.",
                 subs=[(5.0, 9.8, "Đàn ông đi hết, việc của họ mình làm hết. / Thế mà cũng xong!")]),
            dict(name="Tiếng trống", label="Chiều",
                 img="First-person view on a riverbank in the afternoon, a group of village women standing still and staring downstream, a faint plume of smoke on the horizon, a woman gripping a fishing net tightly, realistic, vertical 9:16.",
                 vid="0-5s: Afternoon; distant war drums roll across the water from downstream, and a thin plume of smoke rises on the horizon; every woman on the bank stops working. 5-10s: Vợ Anh Tư grips the net in her hands and says quietly, half to herself: \"Ông ấy mà không về... tôi biết lấy ai cãi nhau.\"",
                 subs=[(5.0, 9.8, "Ông ấy mà không về... / tôi biết lấy ai cãi nhau.")]),
            dict(name="Thuyền về", tiktok="bo", label="Chạng vạng",
                 img="First-person view on a riverbank at dusk, small boats returning with tired muddy men, village women rushing to the water's edge searching faces, a woman standing on tiptoe looking past them, no injuries shown, realistic, vertical 9:16.",
                 vid="0-5s: At dusk, small boats come back up the river with tired, muddy men; the women rush to the water's edge, searching every face. 5-10s: Vợ Anh Tư stands on tiptoe, scanning boat after boat; the last boat passes, and he is not on it. Her face falls.",
                 subs=[]),
            dict(name="Anh Tư về", label="Tối",
                 img=f"First-person view on a riverbank at night with torches, {ANH_TU} covered head to toe in mud, grinning and waving from a small late boat, a strong woman on the bank with hands on her hips, realistic, vertical 9:16.",
                 vid="0-5s: Torchlight; one more small boat appears late; Anh Tư, covered head to toe in mud, waves and grins: \"Thắng rồi! Cái cọc to nhất là anh cắm đấy!\" 5-10s: Vợ Anh Tư smacks his shoulder hard, then pulls him into a tight hug: \"Lần sau đi đâu thì nói một câu! Bùn thế này, ai giặt?\"",
                 subs=[(0.5, 4.8, "Thắng rồi! / Cái cọc to nhất là anh cắm đấy!"),
                       (5.0, 9.8, "Lần sau đi đâu thì nói một câu! / Bùn thế này, ai giặt?")]),
        ],
        caption=("Sáng tiễn chồng đi cắm cọc mà không ai nói để làm gì, chiều nghe tiếng trống mới biết là đánh trận 🥲 "
                 "Năm 938, khi trai làng ven sông Bạch Đằng theo Ngô Quyền ra trận, người ở nhà chỉ biết chờ. Sử không "
                 "ghi tên những người chờ ở nhà. Tag người hay lo cho bạn nhất 👇"),
        tags="#ngoquyen #938 #anhtu",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#bachdangngoaitruyen",
          note=NOTE, unit="Tập", file_unit="tap")
