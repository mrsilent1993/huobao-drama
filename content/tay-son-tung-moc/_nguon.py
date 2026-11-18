#!/usr/bin/env python3
"""Loạt "Tây Sơn từng mốc": mỗi mốc của phong trào Tây Sơn là một video, theo công thức Anh Tư.
Sửa ở đây rồi chạy: python3 _nguon.py

Chỉ chứa các mốc CHƯA có tập. Các mốc đã có (1771, 1785, 1788 La Sơn Phu Tử, 1789, 1790, 1797) nằm ở loạt
"POV người bình thường"; bảng thứ tự đầy đủ ở README.md của thư mục này.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
NHAC = "Nguyễn Nhạc, a stout, cheerful Vietnamese man in his thirties with a short beard"
REBELS = ("Tây Sơn fighters with black-lacquered teeth in plain dark-indigo or brown clothes with red head wraps, "
          "spears and swords")

LEN_FULL = ("hai video từ cùng 5 clip: **bản dài** (YouTube, khoảng 48 giây sau chuyển cảnh) và **bản ngắn** "
            "(TikTok, khoảng 38 giây) vẫn đủ cả 5 cảnh: 3 clip chính giữ nguyên, 2 clip phụ cắt lấy 5 giây chứa "
            "câu chính (xem ghi chú \"Bản TikTok\" ở từng clip)")

NOTE = ("**Tây Sơn từng mốc:** mỗi mốc là một video, theo công thức Anh Tư (sẹo ngang lông mày trái, răng cửa mẻ, "
        "cười toe; ảnh tham chiếu trong `../bach-dang/README.md`). Nguyễn Huệ chỉ xuất hiện từ phía sau hoặc từ xa, "
        "mọi câu đùa nhắm vào Anh Tư. **Hai video từ cùng bộ clip:** bản dài (YouTube) đủ mọi clip; bản ngắn (TikTok) vẫn đủ mọi cảnh, chỉ cắt mỗi cảnh phụ còn 5 giây chứa câu chính. "
        "Thứ tự đăng cả loạt (kể cả các tập đã có) xem `README.md`.")

END_NEXT = "Follow để xem mốc tiếp: / {} →"

EPISODES = [
    # ------------------------------------------------------------------ 1773 (bản đầy đủ 6 cảnh)
    dict(
        slug="khieng-cui-quy-nhon-1773", prefix="ts1773", giong="Central Vietnamese (Bình Định) accent",
        title="Bị sai khiêng một cái cũi có người vào thành, không ai nói người trong cũi là ai (lấy thành Quy Nhơn, 1773)",
        length=("hai video từ cùng 6 clip: **bản dài** (YouTube, khoảng 58 giây sau chuyển cảnh) và **bản ngắn** "
                "(TikTok, khoảng 38 giây) vẫn đủ cả 6 cảnh: cảnh mở đầu và cảnh kết giữ nguyên 10 giây, 4 cảnh giữa "
                "mỗi cảnh cắt lấy 5 giây chứa câu quan trọng nhất"),
        history=("**Lịch sử:** năm 1771, ba anh em Nguyễn Nhạc, Nguyễn Huệ, Nguyễn Lữ dấy binh ở Tây Sơn. Năm 1773, nghĩa "
                 "quân lấy được thành Quy Nhơn bằng mưu, đây là thành lớn đầu tiên Tây Sơn chiếm được. Theo sử nhà Nguyễn "
                 "(mức B, có màu giai thoại), Nguyễn Nhạc tự vào cũi, sai người khiêng nộp cho viên quan giữ thành Nguyễn "
                 "Khắc Tuyên như thể đã bắt được thủ lĩnh giặc; quan mừng, đem giam. Nửa đêm Nhạc ra khỏi cũi, mở cổng "
                 "thành cho quân vào. **Hư cấu:** Anh Tư khiêng cũi, chiếc chốt \"lắp ngược\", bữa tiệc mừng và mọi lời "
                 "thoại."),
        setting=("Vietnam, autumn 1773, Quy Nhơn citadel in Bình Định: high earth-and-brick walls, a heavy wooden gate, "
                 "the garrison of the Nguyễn lords in plain dark cotton uniforms with cloth head wraps, a provincial "
                 "official in an embroidered robe. No visible writing on clothes or signs, no flags. "
                 f"{REBELS}. {NHAC}. Anh Tư is {FACE}, in a brown shirt with a red head wrap."),
        hook="POV: Khiêng cũi / có người / vào thành giặc",
        end=END_NEXT.format("năm 1778"),
        clips=[
            dict(name="Thành cao", label="Tây Sơn từng mốc · 1773",
                 img=f"First-person view at dusk from a hill outside a high earth-and-brick citadel wall, a group of rebels with red head wraps looking at the wall, {NHAC} standing in front with his hand on an empty wooden cage on carrying poles, {FACE} beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: At dusk the rebels stare up at the high citadel wall. Nguyễn Nhạc says: \"Thành cao, quân ta "
                      "ít, đánh thì không vào được.\" 5-10s: He grins and pats an empty wooden cage on carrying poles: "
                      "\"Thì để quan... tự khiêng ta vào.\" Anh Tư, beside the viewer, stares at the cage: \"Khiêng... anh "
                      "cả vào ạ?\""),
                 subs=[(0.5, 4.8, "Thành cao, quân ta ít, / đánh thì không vào được."),
                       (5.0, 7.6, "Thì để quan... / tự khiêng ta vào."),
                       (7.6, 9.6, "Khiêng... anh cả vào ạ?")]),
            dict(name="Vào cũi", tiktok="0-5", noi=True, label="",
                 img=f"First-person view in the rebel camp at dusk, {NHAC} climbing into a sturdy wooden cage on carrying poles and sitting cross-legged, smiling, {FACE} holding one pole and staring at him, realistic, vertical 9:16.",
                 vid=("0-5s: Nguyễn Nhạc climbs into the wooden cage, settles comfortably and says: \"Cứ nói là bắt được "
                      "thủ lĩnh giặc. Diễn cho khéo.\" 5-10s: Anh Tư, holding a carrying pole, whispers to the viewer: "
                      "\"Anh cả... tự chui vào cũi thật ạ?\""),
                 subs=[(0.5, 4.8, "Cứ nói là bắt được / thủ lĩnh giặc. Diễn cho khéo."),
                       (5.0, 9.5, "Anh cả... / tự chui vào cũi thật ạ?")]),
            dict(name="Cổng thành", tiktok="5-10", label="Trước cổng thành Quy Nhơn",
                 img=f"First-person view carrying a wooden cage on a pole toward a citadel gate, guards in plain dark cotton uniforms with spears blocking the way, {FACE} at the front of the pole, putting on a serious face, realistic, vertical 9:16.",
                 vid=("0-5s: At the gate, a guard blocks them; Anh Tư puts on a grave face and announces loudly: \"Bắt "
                      "được thủ lĩnh giặc đây ạ!\" 5-10s: As the guard waves them through, Anh Tư mutters to the viewer: "
                      "\"Bắt khó lắm... anh ấy tự chui vào.\""),
                 subs=[(0.5, 4.8, "Bắt được thủ lĩnh giặc đây ạ!"),
                       (5.0, 9.5, "Bắt khó lắm... / anh ấy tự chui vào.")]),
            dict(name="Quan mừng", tiktok="5-10", label="",
                 img=f"First-person view in a citadel courtyard, a delighted official in an embroidered robe laughing and pointing at the cage, servants bringing wine, inside the cage {NHAC} lying on his side asleep, {FACE} beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: The official laughs with delight: \"Bắt được thủ lĩnh rồi! Mở tiệc!\" Soldiers cheer around "
                      "the cage. 5-10s: Anh Tư leans toward the viewer and whispers: \"Quan mừng quá... mà trong cũi, anh "
                      "cả đang ngủ ngáy.\" Soft snoring comes from the cage."),
                 subs=[(0.5, 4.8, "Bắt được thủ lĩnh rồi! / Mở tiệc!"),
                       (5.0, 9.5, "Quan mừng quá... mà trong cũi, / anh cả đang ngủ ngáy.")]),
            dict(name="Nửa đêm", tiktok="5-10", label="Nửa đêm",
                 img=f"First-person view at night in a dark storeroom lit by moonlight, the wooden cage door swinging open, {NHAC} stepping out quietly, {FACE} crouching beside it holding a wooden latch, realistic, vertical 9:16.",
                 vid=("0-5s: Moonlight; Anh Tư pulls out a wooden latch and the cage door swings open silently; Nguyễn Nhạc "
                      "steps out and stretches. 5-10s: Anh Tư holds up the latch to the viewer with a proud whisper: \"Chốt "
                      "cũi em làm... lắp ngược từ đầu.\""),
                 subs=[(0.5, 4.8, "Cửa cũi mở không một tiếng động."),
                       (5.0, 9.5, "Chốt cũi em làm... / lắp ngược từ đầu.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at night from inside a citadel as the big wooden gate swings open and hundreds of torches of rebels with red head wraps pour in, no fighting, {FACE} beside the gate with a huge chipped-tooth grin, realistic, vertical 9:16.",
                 vid=("0-5s: The heavy gate swings open; hundreds of torches pour into the citadel; no fighting shown. A calm "
                      "narrator's voice says: \"Năm 1773, Tây Sơn lấy thành Quy Nhơn bằng mưu, thành lớn đầu tiên của nghĩa "
                      "quân.\" 5-10s: Anh Tư turns to the camera with his chipped-tooth grin: \"Cái cũi ấy em khiêng! Lần sau anh cả tự đi bộ nhé!\""),
                 subs=[(0.3, 4.8, "Năm 1773, Tây Sơn lấy thành / Quy Nhơn bằng mưu: thành lớn / đầu tiên của nghĩa quân."),
                       (5.0, 8.4, "Cái cũi ấy em khiêng! / Lần sau anh cả tự đi bộ nhé!")]),
        ],
        end_secs=1.6,
        caption=("Bị sai khiêng một cái cũi có người vào thành giặc 😳 Năm 1773, Tây Sơn lấy thành Quy Nhơn bằng mưu: sử "
                 "nhà Nguyễn chép Nguyễn Nhạc tự vào cũi, giả làm thủ lĩnh bị bắt để được khiêng vào thành. Mở đầu loạt "
                 "Tây Sơn từng mốc, mỗi mốc một video, đến tận vua Quang Trung. Bạn có dám tự chui vào cũi như anh cả "
                 "không? 👇"),
        tags="#taysontungmoc #nguyennhac #quynhon #tayson #1773",
        tt_title="Bị sai khiêng một cái cũi có người vào thành giặc, không ai nói người trong cũi là ai",
        hooks_alt=["POV: Thủ lĩnh / tự chui vào cũi", "POV: Lấy thành / bằng một cái cũi"],
        pin=("Loạt Tây Sơn từng mốc bắt đầu từ đây: mỗi mốc một video, đến khi Nguyễn Huệ lên ngôi Quang Trung 🔥 "
             "Bạn đoán mốc tiếp theo năm 1778 là chuyện gì? Follow để xem!"),
        yt_title="Năm 1773: lấy thành Quy Nhơn bằng một cái cũi | Tây Sơn từng mốc",
        yt_tags=("tây sơn, nguyễn nhạc, thành quy nhơn, khởi nghĩa tây sơn, 1773, tây sơn từng mốc, quang trung, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1778
    dict(
        slug="thay-bien-thanh-hoang-de-1778", giong="Central Vietnamese (Bình Định) accent", prefix="ts1778",
        title="Bị sai thay biển tên cả tòa thành trong một đêm, sáng ra phải gọi anh cả bằng tên khác (Nguyễn Nhạc lên ngôi, 1778)",
        length=LEN_FULL,
        history=("**Lịch sử:** năm 1778, Nguyễn Nhạc lên ngôi Hoàng đế, đặt niên hiệu Thái Đức, đóng đô ở thành Đồ Bàn "
                 "(Bình Định) và đổi tên là thành Hoàng Đế (mức B). Nguyễn Lữ và Nguyễn Huệ được phong tước, cầm quân. "
                 "**Hư cấu:** Anh Tư thay biển, may áo, ghi lại năm tháng trên giấy tờ và mọi lời thoại."),
        setting=("Vietnam, 1778, the old Cham-built citadel of Đồ Bàn in Bình Định being renovated as a capital: brick "
                 "towers in the distance, a big wooden gate with a large horizontal signboard whose lettering is not legible (no readable text), officials in new court robes. "
                 f"{REBELS}. {NHAC}, now in a yellow imperial robe. Anh Tư is {FACE}, in a neat dark-red uniform."),
        hook="POV: Thay biển tên / cả tòa thành / trong một đêm",
        end=END_NEXT.format("năm 1785"),
        clips=[
            dict(name="Thay biển", label="Thành Đồ Bàn · năm 1778",
                 img=f"First-person view at night from a ladder against a big citadel gate, the viewer's hands holding a large new wooden signboard, an old signboard lying on the ground, {FACE} on the next ladder holding the other end, realistic, vertical 9:16.",
                 vid="0-5s: On ladders at night, Anh Tư and the viewer heave a big new signboard into place over the gate; an officer below calls up: \"Treo cho thẳng. Sáng mai tên thành đã khác.\" 5-10s: Anh Tư, straining, whispers: \"Đổi tên cả tòa thành... như đổi tên công ty ấy nhỉ?\"",
                 subs=[(0.5, 4.8, "Treo cho thẳng. / Sáng mai tên thành đã khác."),
                       (5.0, 9.5, "Đổi tên cả tòa thành... / như đổi tên công ty ấy nhỉ?")]),
            dict(name="Năm thứ nhất", tiktok="0-5", label="Sáng hôm sau",
                 img=f"First-person view at a scribe's desk piled with documents, a brush and ink, a scribe crossing out dates, {FACE} holding a stack of papers, confused, realistic, vertical 9:16.",
                 vid="0-5s: A scribe hands Anh Tư a stack of papers: \"Từ nay ghi năm Thái Đức thứ nhất.\" 5-10s: Anh Tư flips through the pages and asks the viewer: \"Thế năm ngoái... giờ là năm thứ mấy ạ?\"",
                 subs=[(0.5, 4.8, "Từ nay ghi: / năm Thái Đức thứ nhất."),
                       (5.0, 9.5, "Thế năm ngoái... / giờ là năm thứ mấy ạ?")]),
            dict(name="Gọi là gì", label="Lễ lên ngôi",
                 img=f"First-person view from among kneeling officials in a courtyard, {NHAC} in a yellow imperial robe seated on a throne under banners, {FACE} kneeling beside the viewer, whispering, realistic, vertical 9:16.",
                 vid="0-5s: The officials kneel and shout \"Vạn tuế!\"; Nguyễn Nhạc sits on the throne in a yellow robe. Anh Tư whispers to an officer: \"Hôm qua còn gọi là anh cả... hôm nay gọi là gì ạ?\" 5-10s: The officer hisses: \"Hoàng thượng!\" Anh Tư nods hard and whispers to the viewer: \"...Anh cả hoàng thượng.\"",
                 subs=[(0.5, 4.8, "Hôm qua còn gọi là anh cả... / hôm nay gọi là gì ạ?"),
                       (5.0, 7.0, "Hoàng thượng!"),
                       (7.0, 9.6, "...Anh cả hoàng thượng.")]),
            dict(name="Áo vàng", tiktok="0-5", label="",
                 img=f"First-person view in a tailor's workshop, tailors sewing yellow silk, {FACE} holding up a yellow cloth against himself and admiring it, a tailor snatching it back, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư picks up a piece of yellow silk and holds it against himself, admiring it. 5-10s: A tailor snatches it back: \"Màu này cả nước chỉ một người được mặc!\" Anh Tư to the viewer: \"Thế thôi, em mặc... màu nâu cho lành.\"",
                 subs=[(0.5, 4.8, "Màu này cả nước / chỉ một người được mặc!"),
                       (5.0, 9.5, "Thế thôi, em mặc / màu nâu cho lành.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunrise looking up at the big citadel gate with its new signboard, crowds and soldiers in front of it, {FACE} pointing proudly at the signboard, realistic, vertical 9:16.",
                 vid="0-5s: Sunrise over the gate with its new signboard; crowds gather. A calm narrator's voice says: \"Năm 1778, Nguyễn Nhạc lên ngôi Hoàng đế, niên hiệu Thái Đức, đổi thành Đồ Bàn thành thành Hoàng Đế.\" 5-10s: Anh Tư points up at the signboard and grins at the camera: \"Tấm biển ấy em treo! Lệch một tí... không ai dám nói.\"",
                 subs=[(0.3, 4.8, "Năm 1778, Nguyễn Nhạc / lên ngôi, niên hiệu Thái Đức, / đổi tên thành Đồ Bàn / thành thành Hoàng Đế."),
                       (5.0, 9.8, "Tấm biển ấy em treo! / Lệch một tí... / không ai dám nói.")]),
        ],
        caption=("Bị sai thay biển tên cả tòa thành trong một đêm, sáng ra phải gọi anh cả bằng tên khác 😅 Năm 1778, "
                 "Nguyễn Nhạc lên ngôi Hoàng đế, niên hiệu Thái Đức, đóng đô ở thành Đồ Bàn và đổi tên là thành Hoàng Đế. "
                 "Một mốc trong loạt Tây Sơn từng mốc. Bạn đã đến thăm thành Hoàng Đế ở Bình Định chưa? 👇"),
        tags="#taysontungmoc #nguyennhac #thanhhoangde #thaiduc #1778",
        tt_title="Thay biển tên cả tòa thành trong một đêm, sáng ra phải gọi anh cả bằng tên khác",
        hooks_alt=["POV: Hôm qua gọi anh cả / hôm nay gọi gì?", "POV: Đổi tên cả tòa thành / như đổi tên công ty"],
        pin=("Thành Hoàng Đế (thành Đồ Bàn) vẫn còn dấu tích ở thị xã An Nhơn, Bình Định. Ai ở gần ghé xem chưa? "
             "Follow để xem mốc tiếp: năm 1785!"),
        yt_title="Năm 1778: Nguyễn Nhạc lên ngôi, cả tòa thành đổi tên trong một đêm | Tây Sơn từng mốc",
        yt_tags=("tây sơn, nguyễn nhạc, thái đức, thành hoàng đế, thành đồ bàn, 1778, tây sơn từng mốc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1786
    dict(
        slug="canh-kho-phu-chua-1786", giong="Central Vietnamese (Bình Định) accent", prefix="ts1786",
        title="Ra Bắc được giao canh kho báu phủ chúa mà cấm sờ vào bất cứ thứ gì (phù Lê diệt Trịnh, 1786)",
        length=LEN_FULL,
        history=("**Lịch sử:** giữa năm 1786, Nguyễn Huệ đánh chiếm Phú Xuân rồi tiến ra Bắc với danh nghĩa \"phù Lê "
                 "diệt Trịnh\". Quân Tây Sơn vào Thăng Long, chính quyền chúa Trịnh (nắm quyền hơn hai trăm năm) sụp "
                 "đổ, Nguyễn Huệ vào chầu vua Lê Hiển Tông. Sử chép quân Tây Sơn giữ kỷ luật nghiêm khi vào kinh thành "
                 "(mức B). **Hư cấu:** Anh Tư canh kho, bắp cải, buổi học lễ nghi và mọi lời thoại. Tập phim không dựng "
                 "chuyện số phận chúa Trịnh."),
        setting=("Vietnam, summer 1786, Thăng Long: the grand palace of the Trịnh lords with red-lacquered halls, a "
                 "treasury room with chests, porcelain and silk, Thăng Long townspeople in brown and indigo clothes "
                 "watching cautiously. Tây Sơn soldiers in dark-red uniforms with red head wraps. "
                 f"Anh Tư is {FACE}, in a dark-red uniform."),
        hook="POV: Canh kho báu / mà cấm sờ / vào bất cứ thứ gì",
        end=END_NEXT.format("năm 1787"),
        clips=[
            dict(name="Không một cọng rau", label="Thăng Long · mùa hè năm 1786",
                 img=f"First-person view on a Thăng Long street, townspeople watching from doorways, a vegetable seller's basket nearby, {FACE} beside the viewer holding a cabbage he has just picked up, a stern Tây Sơn officer glaring at him, realistic, vertical 9:16.",
                 vid="0-5s: Marching into the city, Anh Tư picks up a cabbage that rolled from a seller's basket. The officer barks: \"Ta ra giúp vua Lê. Không lấy của dân một cọng rau!\" 5-10s: Anh Tư quickly puts the cabbage back in the basket and bows to the seller: \"Dạ... em trả. Em chỉ nhặt hộ thôi.\"",
                 subs=[(0.5, 4.8, "Ta ra giúp vua Lê. / Không lấy của dân / một cọng rau!"),
                       (5.0, 9.5, "Dạ... em trả. / Em chỉ nhặt hộ thôi.")]),
            dict(name="Học lễ", tiktok="0-5", label="Trước giờ vào chầu",
                 img=f"First-person view in a palace corridor, an elderly court official demonstrating a deep formal bow, {FACE} beside the viewer trying to copy it awkwardly, realistic, vertical 9:16.",
                 vid="0-5s: An elderly court official demonstrates: \"Lạy năm lạy, vái ba vái, không được ngẩng đầu.\" Anh Tư copies, loses count and bumps his head on a pillar. 5-10s: Rubbing his forehead, he whispers to the viewer: \"Đánh trận còn dễ hơn.\"",
                 subs=[(0.5, 4.8, "Lạy năm lạy, vái ba vái, / không được ngẩng đầu."),
                       (5.0, 9.5, "Đánh trận còn dễ hơn.")]),
            dict(name="Canh kho", label="Phủ chúa Trịnh",
                 img=f"First-person view inside a treasury room of a lord's palace, chests overflowing with silk, porcelain and gold ornaments, {FACE} standing guard beside the viewer with a spear, staring at the treasures with his hands clasped tightly behind his back, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư stands guard among overflowing chests of silk and porcelain; the officer at the door says: \"Canh cho kỹ. Ai sờ vào là về quê cày ruộng.\" 5-10s: Anh Tư, hands clasped tightly behind his back, whispers: \"Canh kho vàng... mà cấm sờ. Khổ hơn cả cấm đập muỗi.\"",
                 subs=[(0.5, 4.8, "Canh cho kỹ. Ai sờ vào / là về quê cày ruộng."),
                       (5.0, 9.5, "Canh kho vàng... mà cấm sờ. / Khổ hơn cả cấm đập muỗi.")]),
            dict(name="Dân xem", tiktok="0-5", label="",
                 img=f"First-person view at a palace gate, a crowd of Thăng Long townspeople peering in curiously, an old woman offering a bowl of green tea, {FACE} accepting it politely, realistic, vertical 9:16.",
                 vid="0-5s: Townspeople peer through the gate; an old woman offers Anh Tư a bowl of green tea: \"Nghe đồn quân Tây Sơn dữ lắm, hóa ra hiền thế.\" 5-10s: Anh Tư sips and smiles: \"Dữ với giặc thôi cụ ạ. Với cụ thì em... uống nước.\"",
                 subs=[(0.5, 4.8, "Nghe đồn quân Tây Sơn / dữ lắm, hóa ra hiền thế."),
                       (5.0, 9.5, "Dữ với giặc thôi cụ ạ. / Với cụ thì em... uống nước.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at dusk from the palace steps over the rooftops of Thăng Long, Tây Sơn banners raised on the walls, a commander seen only from behind walking toward the royal palace, {FACE} beside the viewer, proud, realistic, vertical 9:16.",
                 vid="0-5s: Dusk; Tây Sơn banners rise on the walls; the commander, seen only from behind, walks toward the royal palace. A calm narrator's voice says: \"Năm 1786, Nguyễn Huệ ra Bắc phù Lê diệt Trịnh. Hơn hai trăm năm chúa Trịnh nắm quyền khép lại.\" 5-10s: Anh Tư grins at the camera: \"Kho ấy em canh, không mất một xu! ...Cọng rau cũng không.\"",
                 subs=[(0.3, 4.8, "Năm 1786, Nguyễn Huệ ra Bắc / phù Lê diệt Trịnh. Hơn 200 năm / chúa Trịnh nắm quyền khép lại."),
                       (5.0, 9.8, "Kho ấy em canh, / không mất một xu! / ...Cọng rau cũng không.")]),
        ],
        caption=("Ra Bắc được giao canh kho báu phủ chúa mà cấm sờ vào bất cứ thứ gì 😭 Năm 1786, Nguyễn Huệ tiến ra Thăng "
                 "Long với danh nghĩa phù Lê diệt Trịnh, khép lại hơn hai trăm năm chúa Trịnh nắm quyền. Một mốc trong "
                 "loạt Tây Sơn từng mốc. Nếu là bạn, bạn có nhịn được không? 👇"),
        tags="#taysontungmoc #nguyenhue #phuledietrinh #thanglong #1786",
        tt_title="Ra Bắc được giao canh kho báu phủ chúa mà cấm sờ vào bất cứ thứ gì",
        hooks_alt=["POV: Canh kho vàng / mà cấm sờ", "POV: Vào kinh thành / không được lấy một cọng rau"],
        pin=("Mốc trước (năm 1785, Rạch Gầm – Xoài Mút) ở trang cá nhân 👆 Mốc tiếp theo năm 1787 có một chuyện mà ít "
             "người dám kể. Follow để xem!"),
        yt_title="Năm 1786: ra Bắc canh kho báu phủ chúa mà cấm sờ | Tây Sơn từng mốc",
        yt_tags=("tây sơn, nguyễn huệ, phù lê diệt trịnh, phủ chúa trịnh, thăng long 1786, tây sơn từng mốc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1787
    dict(
        slug="vay-thanh-phe-minh-1787", giong="Central Vietnamese (Bình Định) accent", prefix="ts1787",
        title="Bị lệnh vây một tòa thành, đến nơi mới biết đó là thành của chính phe mình (anh em Tây Sơn bất hòa, 1787)",
        length=LEN_FULL,
        history=("**Lịch sử:** năm 1787, Nguyễn Nhạc và Nguyễn Huệ bất hòa sau chuyến ra Bắc. Nguyễn Huệ đem quân vây "
                 "thành Hoàng Đế (Quy Nhơn) của anh. Theo sử nhà Nguyễn (mức B), Nguyễn Nhạc lên mặt thành khóc, kêu "
                 "\"nồi da nấu thịt, lòng em sao nỡ\". Hai anh em giảng hòa, chia nhau cai quản: Nguyễn Nhạc ở Quy "
                 "Nhơn, Nguyễn Lữ ở Gia Định, Nguyễn Huệ từ Quảng Nam trở ra. **Hư cấu:** Anh Tư, người lính quen trên "
                 "mặt thành, bữa cơm ở cổng thành và mọi lời thoại."),
        setting=("Vietnam, 1787, outside the walls of the Hoàng Đế citadel near Quy Nhơn: brick walls with banners, two "
                 "armies of Tây Sơn soldiers in identical dark-red uniforms with red head wraps, one outside and one on "
                 f"the walls. {NHAC} appears on the wall in a yellow robe. Anh Tư is {FACE}, a soldier outside the walls. "
                 "No fighting, no injuries."),
        hook="POV: Bị lệnh / vây thành / của chính phe mình",
        end=END_NEXT.format("lên ngôi năm 1788"),
        clips=[
            dict(name="Vây thành", label="Thành Hoàng Đế · năm 1787",
                 img=f"First-person view from a line of soldiers in dark-red uniforms outside a brick citadel wall, soldiers in the same uniforms looking down from the wall, {FACE} beside the viewer frowning in confusion, realistic, vertical 9:16.",
                 vid="0-5s: The officer orders: \"Vây kín thành Hoàng Đế. Không ai ra vào.\" 5-10s: Anh Tư looks up at the soldiers on the wall, in exactly the same uniforms, and whispers: \"Thành Hoàng Đế... là thành của anh cả mình mà?\" The officer: \"Vây. Không hỏi.\"",
                 subs=[(0.5, 4.8, "Vây kín thành Hoàng Đế. / Không ai ra vào."),
                       (5.0, 7.6, "Thành Hoàng Đế... / là thành của anh cả mình mà?"),
                       (7.6, 9.6, "Vây. Không hỏi.")]),
            dict(name="Người quen", tiktok="0-5", label="",
                 img=f"First-person view looking up at a citadel wall, a soldier on top in the same dark-red uniform waving cheerfully, {FACE} below waving back, realistic, vertical 9:16.",
                 vid="0-5s: A soldier on the wall leans out and waves: \"Ê Tư! Mẹ mày khỏe không?\" Anh Tư waves back happily: \"Khỏe! Bố mày khỏe không?\" 5-10s: The officer glares; Anh Tư freezes, lowers his hand and says to the viewer: \"...Đứa cùng làng.\"",
                 subs=[(0.5, 4.8, "Ê Tư! Mẹ mày khỏe không? / Khỏe! Bố mày khỏe không?"),
                       (5.0, 9.5, "...Đứa cùng làng.")]),
            dict(name="Tiếng khóc trên thành", label="",
                 img=f"First-person view looking up at the citadel wall where {NHAC} in a yellow robe stands with tears on his face, calling down, soldiers on both sides silent, {FACE} beside the viewer with his helmet in his hands, realistic, vertical 9:16.",
                 vid="0-5s: Nguyễn Nhạc appears on the wall, tears on his face, and calls down: \"Nồi da nấu thịt... lòng em sao nỡ!\" Both armies fall silent. 5-10s: Anh Tư lowers his head and whispers to the viewer: \"Hai anh em giận nhau... mà cả hai đạo quân đứng giữa.\"",
                 subs=[(0.5, 4.8, "Nồi da nấu thịt... / lòng em sao nỡ!"),
                       (5.0, 9.5, "Hai anh em giận nhau... / mà cả hai đạo quân đứng giữa.")]),
            dict(name="Bữa cơm ở cổng thành", tiktok="5-10", label="Mấy hôm sau",
                 img=f"First-person view at the open citadel gate, soldiers from both sides sitting together on mats sharing rice and fish, {FACE} handing a bowl to the soldier from the wall, both laughing, realistic, vertical 9:16.",
                 vid="0-5s: The gate is open; soldiers from both sides sit together on mats sharing rice and dried fish. 5-10s: Anh Tư passes a bowl to his friend from the wall and says to the viewer: \"Mới hôm trước còn vây nhau... giờ ăn chung một nồi.\"",
                 subs=[(5.0, 9.5, "Mới hôm trước còn vây nhau... / giờ ăn chung một nồi.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunset outside the citadel as the besieging army packs up and marches away peacefully, banners lowered, soldiers on the wall waving goodbye, {FACE} waving back with a relieved grin, realistic, vertical 9:16.",
                 vid="0-5s: Sunset; the army outside packs up and marches away in peace while the soldiers on the wall wave goodbye. A calm narrator's voice says: \"Năm 1787, Nguyễn Huệ vây thành của anh. Nguyễn Nhạc lên thành khóc. Hai anh em giảng hòa, chia nhau cai quản đất nước.\" 5-10s: Anh Tư waves back, then grins at the camera: \"May mà không ai bắt em chọn phe! Về nhà mẹ hỏi đánh ai... em biết nói sao?\"",
                 subs=[(0.3, 4.8, "Năm 1787, hai anh em / giảng hòa, chia nhau / cai quản đất nước."),
                       (5.0, 9.8, "May mà không ai / bắt em chọn phe! / Về nhà mẹ hỏi đánh ai... / em biết nói sao?")]),
        ],
        caption=("Bị lệnh vây một tòa thành, đến nơi mới biết đó là thành của chính phe mình 😳 Năm 1787, Nguyễn Huệ vây "
                 "thành Hoàng Đế của anh là Nguyễn Nhạc. Sử nhà Nguyễn chép Nguyễn Nhạc lên thành khóc: \"nồi da nấu "
                 "thịt, lòng em sao nỡ\". Một mốc trong loạt Tây Sơn từng mốc. Bạn có biết chuyện này trước đây không? 👇"),
        tags="#taysontungmoc #nguyennhac #nguyenhue #noidanauthit #1787",
        tt_title="Bị lệnh vây một tòa thành, đến nơi mới biết đó là thành của chính phe mình",
        hooks_alt=["POV: Người trên thành / là đứa cùng làng", "POV: Hai anh em giận nhau / cả quân đội đứng giữa"],
        pin=("Ít ai biết hai anh em Tây Sơn từng suýt đánh nhau năm 1787 😢 Bạn đứng về phía ai: anh cả hay em thứ? "
             "Follow để xem mốc tiếp: lên ngôi năm 1788!"),
        yt_title="Năm 1787: vây thành của chính phe mình, \"nồi da nấu thịt\" | Tây Sơn từng mốc",
        yt_tags=("tây sơn, nguyễn nhạc, nguyễn huệ, nồi da nấu thịt, thành hoàng đế, 1787, tây sơn từng mốc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1788
    dict(
        slug="dung-dan-nui-ban-1788", giong="Central Vietnamese (Huế) accent", prefix="ts1788",
        title="Bị sai dựng đàn tế trên núi gấp mấy ngày, buổi sáng vua lên ngôi, buổi chiều đã xuất quân (lên ngôi ở núi Bân, 1788)",
        length=LEN_FULL,
        history=("**Lịch sử:** cuối năm 1788, nghe tin quân Thanh chiếm Thăng Long, Nguyễn Huệ lập đàn ở núi Bân (Phú "
                 "Xuân, Huế ngày nay), ngày 25 tháng 11 năm Mậu Thân (22/12/1788) lên ngôi Hoàng đế, niên hiệu Quang "
                 "Trung, rồi lập tức kéo đại quân ra Bắc (mức B). Hơn một tháng sau, mùng 5 Tết Kỷ Dậu, vua vào Thăng "
                 "Long. **Hư cấu:** Anh Tư dựng đàn, việc \"dựng trong ba ngày\", việc dỡ đàn và mọi lời thoại."),
        setting=("Vietnam, December 1788, Bân mountain near Phú Xuân (Huế): a low pine-covered hill, a square "
                 "three-tiered earthen altar with banners and incense, officials in court robes, a huge Tây Sơn army "
                 "in dark-red uniforms assembling below. The new emperor is seen only from behind or at a distance, in "
                 f"a yellow robe. Anh Tư is {FACE}, a laborer-soldier in a dark-red uniform."),
        hook="POV: Dựng đàn tế / cho vua lên ngôi / gấp trong ba ngày",
        end=END_NEXT.format("Tết Kỷ Dậu 1789"),
        clips=[
            dict(name="Ba ngày", label="Núi Bân, Phú Xuân · cuối năm 1788",
                 img=f"First-person view on a pine-covered hill, workers carrying earth in baskets to build a square three-tiered altar, an official holding a plan, {FACE} beside the viewer with two baskets on a shoulder pole, realistic, vertical 9:16.",
                 vid="0-5s: An official points at the half-built altar: \"Ba ngày nữa xong đàn. Không được chậm một canh.\" 5-10s: Anh Tư, sweating under two baskets of earth, asks: \"Đàn để làm gì mà gấp thế ạ?\" The official: \"Không hỏi. Đắp.\"",
                 subs=[(0.5, 4.8, "Ba ngày nữa xong đàn. / Không được chậm một canh."),
                       (5.0, 7.6, "Đàn để làm gì / mà gấp thế ạ?"),
                       (7.6, 9.6, "Không hỏi. Đắp.")]),
            dict(name="Tập lễ", tiktok="5-10", label="Đêm thứ ba",
                 img=f"First-person view at night on the finished altar lit by torches, officials rehearsing a ceremony, {FACE} standing in for the emperor in the rehearsal, stiff and nervous, realistic, vertical 9:16.",
                 vid="0-5s: At night, officials rehearse the ceremony; for lack of anyone else, Anh Tư stands in the emperor's place while they bow to him. 5-10s: Anh Tư, stiff as a post, whispers to the viewer: \"Được người ta lạy có một lần... mà em run hơn cả lúc ra trận.\"",
                 subs=[(5.0, 9.5, "Được người ta lạy / có một lần... mà em run / hơn cả lúc ra trận.")]),
            dict(name="Lên ngôi", label="Ngày 22/12/1788",
                 img=f"First-person view from the foot of the altar at dawn, officials kneeling in rows, the new emperor in a yellow robe seen only from behind at the top of the altar facing north, a vast army below, {FACE} kneeling beside the viewer, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; incense smoke; officials kneel and shout \"Vạn tuế!\"; the emperor, seen only from behind, stands at the top of the altar looking north. 5-10s: Anh Tư whispers to the viewer: \"Vừa lên ngôi xong... sao ông ấy cứ nhìn về phía Bắc thế?\" Below, drums begin to beat.",
                 subs=[(0.5, 4.8, "Vạn tuế! Vạn tuế! / Vạn vạn tuế!"),
                       (5.0, 9.5, "Vừa lên ngôi xong... / sao ông ấy cứ nhìn / về phía Bắc thế?")]),
            dict(name="Dỡ đàn", tiktok="5-10", label="Buổi chiều",
                 img=f"First-person view on the hill in the afternoon, the long army column marching north into the distance, the empty altar with fallen banners, {FACE} alone with a shovel, looking at the altar, realistic, vertical 9:16.",
                 vid="0-5s: The army marches north in a long column; an official hands Anh Tư a shovel: \"Dỡ đàn đi.\" 5-10s: Anh Tư looks at the altar and sighs to the viewer: \"Đắp ba ngày, dùng một buổi sáng... giờ lại dỡ.\"",
                 subs=[(0.5, 4.8, "Dỡ đàn đi."),
                       (5.0, 9.5, "Đắp ba ngày, / dùng một buổi sáng... / giờ lại dỡ.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view from the hilltop at sunset, a vast army with red banners marching north along the road toward the horizon, {FACE} beside the viewer, shovel on his shoulder, grinning, realistic, vertical 9:16.",
                 vid="0-5s: Sunset; the army stretches north to the horizon. A calm narrator's voice says: \"Ngày 22/12/1788, Nguyễn Huệ lên ngôi ở núi Bân, niên hiệu Quang Trung, rồi lập tức ra Bắc. Hơn một tháng sau, quân Thanh tan.\" 5-10s: Anh Tư grins at the camera: \"Cái đàn ấy em đắp! Đắp ba ngày, đổi cả một triều đại.\"",
                 subs=[(0.3, 4.8, "Lên ngôi ở núi Bân, / niên hiệu Quang Trung, / rồi lập tức ra Bắc."),
                       (5.0, 9.8, "Cái đàn ấy em đắp! / Đắp ba ngày, / đổi cả một triều đại.")]),
        ],
        caption=("Bị sai dựng đàn tế gấp trong mấy ngày, buổi sáng vua lên ngôi, buổi chiều đã xuất quân 😳 Ngày 22/12/1788, "
                 "Nguyễn Huệ lên ngôi ở núi Bân (Huế), niên hiệu Quang Trung, rồi lập tức kéo quân ra Bắc đánh quân "
                 "Thanh. Một mốc trong loạt Tây Sơn từng mốc. Bạn đã đến núi Bân ở Huế chưa? 👇"),
        tags="#taysontungmoc #quangtrung #nuiban #lenngoi #1788",
        tt_title="Dựng đàn tế gấp mấy ngày, buổi sáng vua lên ngôi, buổi chiều đã xuất quân",
        hooks_alt=["POV: Vua lên ngôi buổi sáng / chiều đã xuất quân", "POV: Đắp ba ngày / dùng một buổi"],
        pin=("Núi Bân nay ở phường An Cựu, Huế, vẫn còn dấu tích đàn lên ngôi của vua Quang Trung. Ai ở Huế ghé xem "
             "chưa? Follow để xem mốc tiếp: Tết Kỷ Dậu 1789!"),
        yt_title="Năm 1788: vua Quang Trung lên ngôi buổi sáng, chiều đã xuất quân | Tây Sơn từng mốc",
        yt_tags=("quang trung lên ngôi, núi bân, nguyễn huệ, tây sơn, 1788, tây sơn từng mốc, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1791-1792
    dict(
        slug="the-can-cuoc-tin-bai-1792", giong="Central Vietnamese (Nghệ An) accent", prefix="ts1792",
        title="Bị sai đi làm thẻ căn cước cho cả làng từ hơn 200 năm trước, đến mùa thu năm ấy thì... (tín bài thời Quang Trung, 1791–1792)",
        length=LEN_FULL,
        history=("**Lịch sử:** sau khi đánh tan quân Thanh, vua Quang Trung lo dựng lại đất nước: ban chiếu khuyến nông "
                 "bắt dân phiêu tán về quê cày cấy, dùng chữ Nôm trong giấy tờ, mở Sùng chính viện. Khoảng năm 1791, "
                 "triều đình phát **tín bài** cho đàn ông trong tuổi phải đăng ký, trên có dấu \"Thiên hạ đại tín\"; ai "
                 "không có tín bài bị coi là dân lậu (mức B). Ngày 29 tháng 7 năm Nhâm Tý (16/9/1792), vua Quang Trung "
                 "mất ở Phú Xuân, khi mới 40 tuổi, nhiều việc còn dang dở. **Hư cấu:** Anh Tư, người khai gian tuổi và "
                 "mọi lời thoại. Không dựng cảnh nhà vua mất; clip cuối giữ giọng trang trọng."),
        setting=("Vietnam, 1791 to 1792, a village in Nghệ An: a banyan tree, a communal house yard with a long wooden "
                 "table, a district clerk in a dark robe with a register, a pile of small wooden tags and a large red "
                 "seal, adult villagers queuing (no children), rice fields around. "
                 f"Anh Tư is {FACE}, the clerk's helper in a brown shirt."),
        hook="POV: Bị sai đi làm / thẻ căn cước / từ thế kỷ 18",
        end="Follow để xem cả loạt / Tây Sơn từng mốc →",
        clips=[
            dict(name="Thẻ căn cước", label="Nghệ An · năm 1791",
                 img=f"First-person view at a long wooden table under a banyan tree, a clerk with a register, a pile of small wooden tags and a big red seal, a queue of adult villagers, {FACE} beside the viewer holding the seal, realistic, vertical 9:16.",
                 vid="0-5s: The clerk calls out to the queue: \"Ai không có tín bài thì coi như dân lậu!\" Anh Tư stamps a wooden tag with the red seal. 5-10s: He holds the tag up to the viewer, amazed: \"Làm thẻ căn cước... thời này đã có rồi à?\"",
                 subs=[(0.5, 4.8, "Ai không có tín bài / thì coi như dân lậu!"),
                       (5.0, 9.5, "Làm thẻ căn cước... / thời này đã có rồi à?")]),
            dict(name="Đóng dấu", tiktok="5-10", label="",
                 img=f"First-person view close on the table, {FACE} accidentally stamping the red seal on his own hand, villagers laughing, realistic, vertical 9:16.",
                 vid="0-5s: In a hurry, Anh Tư brings the big seal down on his own hand; the queue bursts out laughing. 5-10s: He shows the red mark \"Thiên hạ đại tín\" on his palm to the viewer: \"Em là người đầu tiên trong làng... được đóng dấu.\"",
                 subs=[(0.5, 4.8, "\"Thiên hạ đại tín\""),
                       (5.0, 9.5, "Em là người đầu tiên / trong làng được đóng dấu.")]),
            dict(name="Khai tuổi", label="",
                 img=f"First-person view at the registration table, a strong young-looking man around 30 with smooth skin and black hair leaning on a cane theatrically, {FACE} staring at him in disbelief, realistic, vertical 9:16.",
                 vid="0-5s: A strong man around 30 leans on a cane, coughs theatrically and says: \"Tôi năm nay... sáu mươi mốt.\" 5-10s: Anh Tư stares at his smooth face and black hair, then whispers to the viewer: \"Sáu mươi mốt... mà da căng hơn cả em.\"",
                 subs=[(0.5, 4.8, "Tôi năm nay... / sáu mươi mốt."),
                       (5.0, 9.5, "Sáu mươi mốt... / mà da căng hơn cả em.")]),
            dict(name="Về quê cày ruộng", tiktok="5-10", label="Năm 1792",
                 img=f"First-person view in a rice field, {FACE} plowing with a buffalo, a wooden tag hanging from his belt, villagers working in the fields around, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư plows a rice field behind a buffalo, the wooden tag swinging at his belt; around him every field is being worked again. 5-10s: He wipes his brow and says to the viewer: \"Vua bảo ai về quê nấy cày ruộng. Ruộng bỏ hoang... giờ xanh hết rồi.\"",
                 subs=[(5.0, 9.5, "Vua bảo ai về quê nấy / cày ruộng. Ruộng hoang / giờ xanh hết rồi.")]),
            dict(name="Câu chốt", label="Mùa thu năm 1792",
                 img=f"First-person view in a rice field at dusk in autumn, villagers stopping work and taking off their hats, a distant drum sounding from the village, {FACE} standing still holding his wooden tag, serious and quiet, realistic, vertical 9:16.",
                 vid="0-5s: Autumn dusk; a slow drum sounds from the village; one by one the villagers stop working and take off their hats in silence. A calm narrator's voice says: \"Mùa thu năm 1792, vua Quang Trung mất, khi mới 40 tuổi.\" 5-10s: Anh Tư looks at the wooden tag in his hand, then quietly at the camera: \"Tấm thẻ này em giữ đến giờ. Ít ra... nhà vua biết tên em.\"",
                 subs=[(0.3, 4.8, "Mùa thu năm 1792, / vua Quang Trung mất, / khi mới 40 tuổi."),
                       (5.0, 9.8, "Tấm thẻ này em giữ đến giờ. / Ít ra... nhà vua biết tên em.")]),
        ],
        caption=("Bị sai đi làm thẻ căn cước cho cả làng... từ năm 1791 🪪 Thời vua Quang Trung, đàn ông phải mang \"tín "
                 "bài\" có dấu \"Thiên hạ đại tín\", không có thì bị coi là dân lậu. Mùa thu năm 1792, nhà vua mất khi mới "
                 "40 tuổi. Mốc cuối của loạt Tây Sơn từng mốc. Theo bạn, nếu vua Quang Trung sống lâu hơn thì sao? 👇"),
        tags="#taysontungmoc #quangtrung #tinbai #theancuoc #1792",
        tt_title="Bị sai đi làm thẻ căn cước cho cả làng từ năm 1791",
        hooks_alt=["POV: Thẻ căn cước / có từ năm 1791", "POV: Khai gian tuổi / để khỏi đi lính"],
        pin=("Tín bài thời Quang Trung được nhiều người gọi là \"thẻ căn cước\" đầu tiên của Việt Nam 🪪 Bạn đã biết chưa? "
             "Xem lại cả loạt Tây Sơn từng mốc ở trang cá nhân 👆"),
        yt_title="Thẻ căn cước từ năm 1791? Tín bài thời vua Quang Trung | Tây Sơn từng mốc",
        yt_tags=("tín bài, quang trung, thẻ căn cước, chiếu khuyến nông, tây sơn, 1792, tây sơn từng mốc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#taysontungmoc #anhtu", note=NOTE, unit="Tập", file_unit="tap")
