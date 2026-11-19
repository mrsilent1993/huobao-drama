#!/usr/bin/env python3
"""Loạt "Thăng Long kỳ truyện": chuyện lạ quanh các địa danh Hà Nội, công thức Anh Tư. Sửa ở đây rồi chạy: python3 _nguon.py

Tập truyền thuyết có legend=True (nhãn "AI tái hiện · theo truyền thuyết"). Không đùa về thần Phật, vua chúa:
câu đùa nhắm vào nỗi khổ của người thợ, người chèo thuyền.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
NO_TEXT = "No flags, no visible or legible writing anywhere, no modern objects."

NOTE = ("**Thăng Long kỳ truyện:** chuyện lạ quanh các địa danh Hà Nội, theo công thức Anh Tư (sẹo ngang lông mày trái, "
        "răng cửa mẻ, cười toe). Tập truyền thuyết có nhãn \"theo truyền thuyết\" ngay đầu video. Câu đùa chỉ nhắm vào "
        "nỗi khổ của người thợ, người chèo thuyền; thần Phật, vua chúa được dựng trang trọng. **Hai video từ cùng 5 clip:** "
        "bản dài (YouTube) đủ clip; bản ngắn (TikTok) vẫn đủ cả 5 cảnh.")
LEN = ("hai video từ cùng 5 clip: **bản dài** (YouTube, khoảng 48 giây sau chuyển cảnh) và **bản ngắn** (TikTok, khoảng "
       "38 giây) vẫn đủ cả 5 cảnh: clip 1, 3, 5 giữ nguyên, clip 2 và 4 cắt lấy 5 giây chứa câu chính")
END = "Follow để xem / Thăng Long kỳ truyện / tập tiếp theo →"

EPISODES = [
    # ------------------------------------------------------------------ 1049 chùa Một Cột
    dict(
        slug="chua-mot-cot-1049", prefix="tl1049",
        voices={"monk": "an old, soft, serene male voice, slow and gentle"},
        title="Bị sai dựng cả một ngôi điện trên đúng một cái cột giữa hồ, chỉ vì vua nằm mơ (chùa Một Cột, 1049)",
        length=LEN,
        history=("**Lịch sử:** theo *Đại Việt sử ký toàn thư* (mức B), năm 1049 vua Lý Thái Tông mộng thấy Phật Quan Âm ngồi "
                 "trên tòa sen, dắt vua lên đài. Tỉnh dậy vua kể lại, nhà sư Thiền Tuệ khuyên dựng chùa: dựng một cột đá "
                 "giữa hồ, trên đặt điện thờ hình hoa sen như trong giấc mộng, gọi là chùa Diên Hựu, ngày nay là chùa Một "
                 "Cột (Hà Nội). Chùa được trùng tu nhiều lần; công trình hiện nay dựng lại năm 1955. **Hư cấu:** Anh Tư, "
                 "các thợ và mọi lời thoại."),
        setting=("Thăng Long in 1049, a square lotus pond west of the citadel: Lý-era builders in brown clothes with "
                 "topknots and black-lacquered teeth, bamboo scaffolding, ropes and pulleys, a single tall stone pillar "
                 "rising from the middle of the pond, a small wooden pavilion shaped like a lotus being built on top. "
                 "An elderly Buddhist monk in brown robes; Lý officials in dark robes. "
                 f"Anh Tư is {FACE}, a carpenter. {NO_TEXT}"),
        hook="POV: Dựng cả ngôi điện / trên đúng / một cái cột",
        end=END,
        clips=[
            dict(name="Một cái cột", label="Thăng Long · năm 1049",
                 img=f"First-person view at the edge of a square lotus pond, an official pointing at a single stone pillar standing in the middle of the water, builders holding tools, {FACE} beside the viewer with a mallet, baffled, realistic, vertical 9:16.",
                 vid=("0-5s: The official points at the single stone pillar in the middle of the pond: \"Dựng điện thờ trên "
                      "cột này. Đúng một cột.\" 5-10s: Anh Tư whispers to the viewer: \"Một cột... thôi ạ? Nhà em bốn cột mà "
                      "còn nghiêng.\""),
                 subs=[(0.5, 4.8, "Dựng điện thờ trên cột này. / Đúng một cột."),
                       (5.0, 9.5, "Một cột... thôi ạ? / Nhà em bốn cột mà còn nghiêng.")]),
            dict(name="Giấc mộng", tiktok="0-5", label="",
                 img=f"First-person view under a tree by the pond, an elderly serene monk in brown robes explaining calmly to the builders, {FACE} listening with his chin in his hand, realistic, vertical 9:16.",
                 vid=("0-5s: The elderly monk explains calmly: \"Bệ hạ mộng thấy Phật Bà ngồi tòa sen giữa hồ. Dựng đúng như "
                      "thế.\" 5-10s: Anh Tư whispers to the viewer: \"Vua mơ một đêm... thợ làm cả năm.\""),
                 subs=[(0.5, 4.8, "Bệ hạ mộng thấy Phật Bà / ngồi tòa sen giữa hồ. / Dựng đúng như thế."),
                       (5.0, 9.5, "Vua mơ một đêm... / thợ làm cả năm.")]),
            dict(name="Đặt điện lên cột", label="",
                 img=f"First-person view from bamboo scaffolding above the pond, a team of builders hauling the wooden lotus-shaped pavilion up with ropes onto the top of the single stone pillar, {FACE} balancing on a beam and pulling a rope, realistic, vertical 9:16.",
                 vid=("0-5s: A team of builders hauls the wooden lotus-shaped pavilion up with ropes and lowers it onto the "
                      "top of the single stone pillar; everyone holds their breath. 5-10s: It settles perfectly. Anh Tư, "
                      "balancing on a beam, says to the viewer: \"Kỹ sư bây giờ mà nhìn... chắc ngất.\""),
                 subs=[(0.5, 4.8, "Cả ngôi điện đặt lên / đúng một cái cột."),
                       (5.0, 9.5, "Kỹ sư bây giờ mà nhìn... / chắc ngất.")]),
            dict(name="Như hoa sen", tiktok="5-10", label="Mấy tháng sau",
                 img=f"First-person view from a small boat on the lotus pond at dawn, the finished small pavilion on its single pillar looking like a lotus flower rising from the water, mist, {FACE} rowing, amazed, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn mist; from a small boat, the finished pavilion on its single pillar looks like a lotus "
                      "flower rising from the water. 5-10s: Anh Tư stops rowing and whispers to the viewer: \"Đứng gần thì "
                      "sợ đổ... đứng xa thì đẹp như mơ.\""),
                 subs=[(0.5, 4.8, "Ngôi điện như đóa sen / mọc lên giữa hồ."),
                       (5.0, 9.5, "Đứng gần thì sợ đổ... / đứng xa thì đẹp như mơ.")]),
            dict(name="Câu chốt", label="Gần một nghìn năm sau",
                 img=f"First-person view of the small one-pillar pagoda by the lotus pond in soft morning light, {FACE} standing on the bank, grinning proudly, realistic, vertical 9:16.",
                 vid=("0-5s: Soft morning light on the small one-pillar pagoda. A calm narrator's voice says: \"Năm 1049, vua "
                      "Lý Thái Tông cho dựng chùa Diên Hựu như trong giấc mộng. Ngày nay ta gọi là chùa Một Cột.\" 5-10s: Anh "
                      "Tư grins at the camera: \"Dựng lại bao nhiêu lần... vẫn đúng một cái cột!\""),
                 subs=[(0.3, 4.8, "Năm 1049, vua Lý Thái Tông / dựng chùa như trong mộng. / Nay là chùa Một Cột."),
                       (5.0, 9.8, "Dựng lại bao nhiêu lần... / vẫn đúng một cái cột!")]),
        ],
        caption=("Bị sai dựng cả một ngôi điện trên đúng một cái cột giữa hồ, chỉ vì vua nằm mơ 😳 Năm 1049, vua Lý Thái Tông "
                 "mộng thấy Phật Bà Quan Âm ngồi tòa sen, nhà sư Thiền Tuệ khuyên dựng chùa như trong mộng: đó là chùa Một "
                 "Cột. Bạn đã đến chùa Một Cột chưa? 👇"),
        tags="#thanglongkytruyen #chuamotcot #lythaitong #hanoi #1049",
        tt_title="Bị sai dựng cả ngôi điện trên đúng một cái cột giữa hồ, chỉ vì vua nằm mơ",
        hooks_alt=["POV: Vua mơ một đêm / thợ làm cả năm", "POV: Nhà bốn cột còn nghiêng / chùa một cột thì sao?"],
        pin=("Chùa Một Cột hiện nay được dựng lại năm 1955, nhưng vẫn giữ đúng kiểu một cột giữa hồ như năm 1049 🪷 Bạn "
             "biết chùa Một Cột còn tên gọi nào khác không? Follow để xem Thăng Long kỳ truyện tiếp theo!"),
        yt_title="Năm 1049: dựng cả ngôi điện trên một cái cột, chỉ vì vua nằm mơ (chùa Một Cột)",
        yt_tags=("chùa một cột, chùa diên hựu, lý thái tông, thăng long, hà nội, 1049, thăng long kỳ truyện, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ trâu vàng Hồ Tây (truyền thuyết)
    dict(
        slug="trau-vang-ho-tay", prefix="tltrau", legend=True,
        voices={"Khổng Lồ": "a huge, deep, rumbling, good-natured male voice"},
        title="Phụ đúc cái chuông to nhất nước, đánh một tiếng thì mất luôn cả cánh đồng (truyền thuyết trâu vàng Hồ Tây)",
        length=LEN,
        history=("**Truyền thuyết (mức C):** tương truyền thời Lý có nhà sư Khổng Lồ (có bản gắn với thiền sư Nguyễn Minh Không) "
                 "đúc một quả chuông đồng rất lớn. Tiếng chuông vang sang tận phương Bắc; con trâu vàng (trâu mẹ) tưởng tiếng "
                 "trâu con gọi, chạy theo tiếng chuông về, giẫm lún cả một vùng đất thành hồ Tây. Vì thế hồ Tây còn có tên là "
                 "hồ Kim Ngưu (trâu vàng). Truyện có nhiều dị bản. **Hư cấu:** Anh Tư và mọi lời thoại. Không dựng cảnh "
                 "trâu hay người bị thương."),
        setting=("A legendary time in the Lý era, the flat rice fields west of Thăng Long: a large outdoor bronze foundry with "
                 "clay furnaces and molten bronze, a gigantic bronze bell hung on a huge wooden frame. Khổng Lồ is a very "
                 "tall, broad, kindly monk-craftsman in brown robes. A glowing golden water buffalo appears later. Builders "
                 f"and villagers in brown clothes. Anh Tư is {FACE}, a foundry helper with a soot-covered face. {NO_TEXT}"),
        hook="POV: Phụ đúc cái chuông / to nhất nước",
        end=END,
        clips=[
            dict(name="Đúc chuông", label="Theo truyền thuyết · thời Lý",
                 img=f"First-person view at an outdoor bronze foundry, glowing molten bronze pouring into a huge clay mold, a very tall broad monk-craftsman supervising, {FACE} pumping bellows with a soot-covered face, realistic, vertical 9:16.",
                 vid=("0-5s: Molten bronze pours glowing into a huge clay mold; the very tall monk-craftsman says in a deep "
                      "voice: \"Đúc cái chuông to nhất nước.\" 5-10s: Anh Tư, pumping the bellows, asks: \"To nhất nước... thì "
                      "đánh kêu tới đâu ạ?\" The giant smiles: \"Tới tận phương Bắc.\""),
                 subs=[(0.5, 4.8, "Đúc cái chuông to nhất nước."),
                       (5.0, 7.6, "To nhất nước... / thì đánh kêu tới đâu ạ?"),
                       (7.6, 9.6, "Tới tận phương Bắc.")]),
            dict(name="Chuông treo", tiktok="5-10", label="",
                 img=f"First-person view looking up at a gigantic bronze bell hanging on a huge wooden frame in a field, workers tiny beside it, {FACE} standing under it with his mouth open, realistic, vertical 9:16.",
                 vid=("0-5s: Workers haul the gigantic bronze bell up onto its wooden frame; it sways gently. 5-10s: Anh Tư "
                      "looks up at it and whispers to the viewer: \"To thế này... đánh một cái chắc điếc cả làng.\""),
                 subs=[(0.5, 4.8, "Quả chuông treo lên / cao hơn cả mái đình."),
                       (5.0, 9.5, "To thế này... đánh một cái / chắc điếc cả làng.")]),
            dict(name="Tiếng chuông", label="",
                 img=f"First-person view in a field as the giant monk strikes the gigantic bell with a huge log, sound waves rippling over the rice fields, far on the horizon a golden glow, {FACE} covering his ears, realistic, vertical 9:16.",
                 vid=("0-5s: The giant monk swings a huge log against the bell: a deep boom rolls across the fields toward "
                      "the north; birds fly up. 5-10s: On the far horizon a golden glow appears and grows closer. Anh Tư, "
                      "still covering his ears, squints: \"Ơ... con gì vàng vàng đang chạy về đây thế kia?\""),
                 subs=[(0.5, 4.8, "Tiếng chuông vang / tới tận phương Bắc."),
                       (5.0, 9.5, "Ơ... con gì vàng vàng / đang chạy về đây thế kia?")]),
            dict(name="Trâu vàng", tiktok="0-5", label="",
                 img=f"First-person view in a rice field as a huge glowing golden water buffalo gallops past, the ground sinking behind it and water welling up, villagers running to higher ground, {FACE} running beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: A huge glowing golden water buffalo gallops across the fields toward the sound of the bell; "
                      "behind it the ground sinks and water wells up; villagers run safely to higher ground. Anh Tư, running, "
                      "shouts: \"Trâu chạy đến đâu... đất lún đến đấy!\" 5-10s: The golden buffalo circles the spot where "
                      "the bell rang and slowly sinks with the land into shining water."),
                 subs=[(0.5, 4.8, "Trâu chạy đến đâu... / đất lún đến đấy!"),
                       (5.0, 9.5, "Đất lún xuống, / nước dâng lên thành hồ.")]),
            dict(name="Câu chốt", label="Hồ Tây ngày nay",
                 img=f"First-person view at sunset over a wide calm lake with golden light on the water, {FACE} standing on the bank, scratching his head and grinning, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset over the wide calm lake, golden light on the water. A calm narrator's voice says: \"Tương "
                      "truyền, trâu vàng nghe tiếng chuông, tưởng con gọi, chạy theo, giẫm lún đất thành hồ Tây. Hồ còn tên là "
                      "hồ Kim Ngưu.\" 5-10s: Anh Tư scratches his head and grins at the camera: \"Đúc một cái chuông... ra luôn "
                      "cái hồ!\""),
                 subs=[(0.3, 4.8, "Tương truyền, đất lún / thành hồ Tây, nên hồ / còn tên là hồ Kim Ngưu."),
                       (5.0, 9.8, "Đúc một cái chuông... / ra luôn cái hồ!")]),
        ],
        caption=("Phụ đúc cái chuông to nhất nước, đánh một tiếng thì mất luôn cả cánh đồng 😳 Tương truyền, trâu vàng nghe "
                 "tiếng chuông của nhà sư Khổng Lồ, tưởng con gọi, chạy theo, giẫm lún đất thành hồ Tây, nên hồ còn tên là "
                 "hồ Kim Ngưu (trâu vàng). Bạn đã nghe truyền thuyết này chưa? 👇"),
        tags="#thanglongkytruyen #hotay #trauvang #hokimnguu #truyenthuyet",
        tt_title="Phụ đúc cái chuông to nhất nước, đánh một tiếng mất luôn cả cánh đồng",
        hooks_alt=["POV: Đúc một cái chuông / ra luôn cái hồ", "POV: Trâu chạy đến đâu / đất lún đến đấy"],
        pin=("Hồ Tây còn có tên là hồ Kim Ngưu, nghĩa là trâu vàng 🐃✨ Bạn còn biết tên gọi nào khác của hồ Tây không? "
             "Follow để xem Thăng Long kỳ truyện tiếp theo!"),
        yt_title="Đúc cái chuông to nhất nước, đánh một tiếng ra luôn hồ Tây (truyền thuyết trâu vàng)",
        yt_tags=("hồ tây, trâu vàng, hồ kim ngưu, khổng lồ đúc chuông, truyền thuyết hà nội, thăng long kỳ truyện, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1428 rùa thần Hồ Gươm (truyền thuyết)
    dict(
        slug="lau-guom-rua-than-1428", prefix="tl1428", legend=True,
        title="Được giao lau thanh gươm thật sáng cho vua đi thuyền, lau xong thì... rùa lấy mất (truyền thuyết Hồ Gươm, 1428)",
        length=LEN,
        history=("**Truyền thuyết (mức C):** tương truyền sau khi đánh đuổi quân Minh, năm 1428 vua Lê Lợi đi thuyền rồng "
                 "dạo hồ Lục Thủy ở kinh thành Thăng Long. Một con rùa vàng lớn nổi lên, xin vua trả thanh gươm thần mà Long "
                 "Quân đã cho mượn để đánh giặc. Vua trả gươm, rùa ngậm gươm lặn xuống. Từ đó hồ có tên là hồ Hoàn Kiếm (hồ "
                 "trả gươm). Truyện có nhiều dị bản; sử chính không chép. **Hư cấu:** Anh Tư lau gươm, chèo thuyền và mọi "
                 "lời thoại. Vua Lê Lợi chỉ xuất hiện từ phía sau."),
        setting=("Thăng Long in 1428, a calm green lake (Lục Thủy) in the capital with willow trees on the banks: a long "
                 "royal wooden boat with a carved Lê-style dragon prow (no writing), oarsmen in brown uniforms. King Lê Lợi "
                 "is seen ONLY from behind, in a yellow robe. A huge golden turtle with a glowing shell appears from the water. "
                 f"Anh Tư is {FACE}, an oarsman and attendant. {NO_TEXT}"),
        hook="POV: Lau gươm / cho vua đi thuyền",
        end=END,
        clips=[
            dict(name="Lau gươm", label="Thăng Long · năm 1428",
                 img=f"First-person view in a palace courtyard, an officer handing a long sword wrapped in yellow silk to {FACE}, who holds out both hands carefully, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is a stern officer in a dark uniform; the RECEIVER is Anh Tư. "
                      "0-5s: The officer hands Anh Tư a long sword wrapped in yellow silk: \"Lau cho sáng. Chiều nay vua đi "
                      "thuyền.\" 5-10s: Anh Tư polishes the blade carefully and looks at his reflection in it: \"Lau cả buổi... "
                      "soi gương được luôn.\""),
                 subs=[(0.5, 4.8, "Lau cho sáng. / Chiều nay vua đi thuyền."),
                       (5.0, 9.5, "Lau cả buổi... / soi gương được luôn.")]),
            dict(name="Chèo thuyền", tiktok="0-5", label="Hồ Lục Thủy",
                 img=f"First-person view from the oars of a long royal boat with a carved dragon prow gliding on a calm green lake, the king seen only from behind under a canopy, willow trees on the banks, {FACE} rowing beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: The royal boat glides over the calm green lake; Anh Tư rows and whispers to the viewer: \"Hồ "
                      "hôm nay... xanh lạ.\" 5-10s: The water near the boat starts to bubble gently; the oarsmen glance at "
                      "each other."),
                 subs=[(0.5, 4.8, "Hồ hôm nay... xanh lạ."),
                       (5.0, 9.5, "Mặt nước bỗng sủi bọt.")]),
            dict(name="Rùa nổi lên", label="",
                 img=f"First-person view from the royal boat as a huge golden turtle with a glowing shell surfaces right beside it, water streaming off its shell, the sword on its stand beginning to move by itself, {FACE} frozen at his oar, realistic, vertical 9:16.",
                 vid=("0-5s: A huge golden turtle with a glowing shell rises from the water right beside the boat; the "
                      "sword on its stand starts to move by itself. 5-10s: Anh Tư, frozen at his oar, whispers: \"Rùa... "
                      "rùa to bằng cái chiếu!\""),
                 subs=[(0.5, 4.8, "Một con rùa vàng / nổi lên cạnh thuyền."),
                       (5.0, 9.5, "Rùa... / rùa to bằng cái chiếu!")]),
            dict(name="Trả gươm", tiktok="5-10", label="",
                 img=f"First-person view from the boat as the king, seen only from behind, holds the shining sword out over the water and the golden turtle takes it gently in its mouth, {FACE} watching with a sad face, realistic, vertical 9:16.",
                 vid=("0-5s: The king, seen only from behind, holds the shining sword out over the water; the golden turtle "
                      "takes it gently in its mouth and slowly sinks. 5-10s: Anh Tư stares at the ripples and whispers sadly: "
                      "\"Em lau cả buổi sáng... rùa lấy mất.\""),
                 subs=[(0.5, 4.8, "Vua trả gươm. / Rùa ngậm gươm lặn xuống."),
                       (5.0, 9.5, "Em lau cả buổi sáng... / rùa lấy mất.")]),
            dict(name="Câu chốt", label="Hồ Gươm ngày nay",
                 img=f"First-person view at dawn over a calm green lake with willow trees and a small old tower on a tiny island, mist, {FACE} on the bank, grinning, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn mist over the calm green lake, a small old tower on a tiny island. A calm narrator's voice "
                      "says: \"Tương truyền, năm 1428 vua Lê Lợi trả gươm thần cho rùa vàng. Hồ từ đó gọi là hồ Hoàn Kiếm.\" "
                      "5-10s: Anh Tư grins at the camera: \"Gươm trả rồi... nhưng sáng nhất là nhờ em lau!\""),
                 subs=[(0.3, 4.8, "Tương truyền, vua Lê Lợi / trả gươm thần cho rùa vàng. / Hồ từ đó gọi là hồ Hoàn Kiếm."),
                       (5.0, 9.8, "Gươm trả rồi... / nhưng sáng nhất là nhờ em lau!")]),
        ],
        caption=("Được giao lau thanh gươm thật sáng cho vua đi thuyền, lau xong thì... rùa lấy mất 🐢⚔️ Tương truyền năm 1428, "
                 "vua Lê Lợi trả gươm thần cho rùa vàng trên hồ Lục Thủy, từ đó hồ có tên Hoàn Kiếm. Theo yêu cầu của các "
                 "bác ở phần bình luận! Bạn muốn xem truyền thuyết nào tiếp theo? 👇"),
        tags="#thanglongkytruyen #hoguom #hoankiem #ruathan #leloi",
        tt_title="Được giao lau gươm thật sáng cho vua đi thuyền, lau xong thì rùa lấy mất",
        hooks_alt=["POV: Lau gươm cả buổi sáng / rùa lấy mất", "POV: Chèo thuyền vua / trên hồ Lục Thủy"],
        pin=("Làm theo yêu cầu của bạn đã bình luận \"làm rùa thần Hồ Gươm đi\" 🐢 Bạn biết hồ Hoàn Kiếm trước đó tên là gì "
             "không? Follow để xem Thăng Long kỳ truyện tiếp theo!"),
        yt_title="Lau gươm cả buổi cho vua đi thuyền, rồi rùa thần lấy mất (truyền thuyết Hồ Gươm 1428)",
        yt_tags=("hồ gươm, hồ hoàn kiếm, rùa thần, trả gươm, lê lợi, 1428, truyền thuyết hà nội, thăng long kỳ truyện, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1484 bia tiến sĩ Văn Miếu
    dict(
        slug="khac-bia-tien-si-1484", prefix="tl1484",
        title="Bị sai khắc tên người khác lên đá cho muôn đời, còn tên mình thì... (bia tiến sĩ Văn Miếu, 1484)",
        length=LEN,
        history=("**Lịch sử:** năm 1484, vua Lê Thánh Tông cho dựng bia tiến sĩ ở Văn Miếu (Thăng Long), khắc tên những người "
                 "đỗ tiến sĩ, bắt đầu từ khoa thi năm 1442 (mức B). Việc dựng bia còn tiếp tục ở các triều sau. Ngày nay ở "
                 "Văn Miếu – Quốc Tử Giám còn 82 tấm bia đặt trên lưng rùa đá, được UNESCO công nhận là Di sản tư liệu thế "
                 "giới năm 2011. **Hư cấu:** Anh Tư khắc bia và mọi lời thoại. Chữ trên bia không dựng rõ để đọc được."),
        setting=("Văn Miếu in Thăng Long, 1484: a stone carvers' yard beside a temple courtyard with old trees, large flat "
                 "stone steles lying on wooden trestles, stone turtle bases, chisels and mallets, ink. Carved characters on "
                 "the steles are tiny and blurred, NOT legible. Lê-era officials in dark robes with black caps; stone carvers "
                 f"in brown clothes. Anh Tư is {FACE}, a stone carver with dusty hands. {NO_TEXT}"),
        hook="POV: Khắc tên người khác / lên đá / cho muôn đời",
        end=END,
        clips=[
            dict(name="Khắc tên", label="Văn Miếu · năm 1484",
                 img=f"First-person view in a stone carvers' yard, an official in a dark robe handing a long paper list (writing not legible) to {FACE}, who holds a chisel, a large blank stone stele behind, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is an official in a dark robe; the RECEIVER is Anh Tư with a "
                      "chisel. 0-5s: The official hands Anh Tư a long list: \"Khắc tên các tiến sĩ từ khoa năm 1442. Không "
                      "sai một nét.\" 5-10s: Anh Tư counts on his fingers and whispers: \"Người ta đỗ bốn mươi năm rồi... giờ "
                      "mới khắc ạ?\""),
                 subs=[(0.5, 4.8, "Khắc tên các tiến sĩ / từ khoa năm 1442. / Không sai một nét."),
                       (5.0, 9.5, "Người ta đỗ / bốn mươi năm rồi... / giờ mới khắc ạ?")]),
            dict(name="Rùa đội bia", tiktok="0-5", label="",
                 img=f"First-person view as a team of workers with ropes and poles lowers a heavy stone stele into the slot on the back of a large stone turtle, {FACE} pushing from the side, realistic, vertical 9:16.",
                 vid=("0-5s: A team of workers lowers a heavy stone stele onto the back of a large stone turtle; it slots in "
                      "with a deep thud. Anh Tư pats the turtle's head: \"Rùa này... chở chữ cho cả nghìn năm.\" 5-10s: The "
                      "workers wipe their brows; one sits on the turtle and is shooed off by an official."),
                 subs=[(0.5, 4.8, "Rùa này... / chở chữ cho cả nghìn năm."),
                       (5.0, 9.5, "Bia đặt trên lưng rùa đá.")]),
            dict(name="Một nét", label="",
                 img=f"First-person close-up of {FACE} carving tiny characters into a stone stele with a chisel and mallet, sweating, an official leaning over his shoulder pointing at one stroke, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư carves slowly, sweat on his forehead; the official leans over and taps one stroke: "
                      "\"Nét này lệch.\" 5-10s: Anh Tư freezes and whispers to the viewer: \"Lệch một nét... mà người ta nhìn "
                      "cả nghìn năm. Em run lắm.\""),
                 subs=[(0.5, 4.8, "Nét này lệch."),
                       (5.0, 9.5, "Lệch một nét... mà người ta / nhìn cả nghìn năm. Em run lắm.")]),
            dict(name="Tay phồng", tiktok="5-10", label="Mấy tháng sau",
                 img=f"First-person view at dusk in the carvers' yard, finished steles standing in a row on stone turtles, {FACE} sitting down and showing his blistered, dusty palms to the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Dusk; finished steles stand in a row on their stone turtles. 5-10s: Anh Tư sits down and shows "
                      "his blistered palms to the camera: \"Tên người ta lên đá... tay em lên phồng.\""),
                 subs=[(0.5, 4.8, "Từng tấm bia / đứng lên trên lưng rùa."),
                       (5.0, 9.5, "Tên người ta lên đá... / tay em lên phồng.")]),
            dict(name="Câu chốt", label="Văn Miếu ngày nay",
                 img=f"First-person view in a quiet temple courtyard with old trees and long rows of stone steles on stone turtles in soft light, {FACE} standing among them, smiling quietly, realistic, vertical 9:16.",
                 vid=("0-5s: Soft light over long rows of steles on stone turtles in a quiet courtyard. A calm narrator's "
                      "voice says: \"Năm 1484, vua Lê Thánh Tông cho dựng bia tiến sĩ ở Văn Miếu. 82 tấm bia nay là Di sản tư "
                      "liệu thế giới.\" 5-10s: Anh Tư touches a stele and smiles at the camera: \"Tên em không có trên bia... "
                      "nhưng chữ trên bia là em khắc.\""),
                 subs=[(0.3, 4.8, "Năm 1484, vua Lê Thánh Tông / dựng bia tiến sĩ ở Văn Miếu. / 82 bia nay là di sản thế giới."),
                       (5.0, 9.8, "Tên em không có trên bia... / nhưng chữ trên bia là em khắc.")]),
        ],
        caption=("Bị sai khắc tên người khác lên đá cho muôn đời, còn tên mình thì... 🪨 Năm 1484, vua Lê Thánh Tông cho dựng bia "
                 "tiến sĩ ở Văn Miếu, khắc tên người đỗ từ khoa năm 1442. Nay 82 tấm bia trên lưng rùa đá là Di sản tư liệu "
                 "thế giới. Mùa thi đến rồi, gửi video này cho đứa bạn sắp đi thi 👇"),
        tags="#thanglongkytruyen #vanmieu #biatiensi #lethanhtong #1484",
        tt_title="Bị sai khắc tên người khác lên đá cho muôn đời, còn tên mình thì...",
        hooks_alt=["POV: Tên người ta lên đá / tay mình lên phồng", "POV: Lệch một nét / người ta nhìn nghìn năm"],
        pin=("Lưu ý: bia tiến sĩ là di sản, ngày nay không được xoa đầu rùa nữa nhé 🐢 Bạn đã đến Văn Miếu chưa? Follow để "
             "xem Thăng Long kỳ truyện tiếp theo!"),
        yt_title="Năm 1484: khắc tên người khác lên đá cho muôn đời (bia tiến sĩ Văn Miếu)",
        yt_tags=("văn miếu, bia tiến sĩ, quốc tử giám, lê thánh tông, 1484, di sản tư liệu thế giới, thăng long kỳ truyện, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

# bản ngắn đủ cảnh: clip 1, 3, 5 giữ nguyên; clip 2 và 4 đã đánh dấu tiktok= ở trên
if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#anhtu", note=NOTE, unit="Tập", file_unit="tap")
