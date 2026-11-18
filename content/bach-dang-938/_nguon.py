#!/usr/bin/env python3
"""Bạch Đằng 938: trailer 30 giây và video trận đánh 2 phút 30 là HAI video riêng. Sửa ở đây rồi chạy: python3 _nguon.py

Sinh ra:
- bach-dang-938-trailer.md / .plan.txt     trailer 30 giây (3 clip Muse), đăng nhử trước một ngày
- bach-dang-938-tran-danh.md / .plan.txt   trận đánh 150 giây (15 clip Muse)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import POV, AUDIO  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, hair in a topknot, a scar across his left eyebrow and a "
        "wide grin with a chipped front tooth, very expressive face")
NGO = ("Ngô Quyền, a stern, calm Vietnamese commander around 40 with a short black beard and topknot, in dark "
       "lacquered leather armor and a deep-red cloak, dignified")
SETTING = ("Vietnam, winter of 938, the Bạch Đằng River estuary near the sea: a wide brown tidal river, mangrove "
           "banks, limestone hills, broad mudflats at low tide. Vietnamese soldiers with hair in topknots and "
           "black-lacquered teeth, in brown tunics or bare-chested, with spears, crossbows and bows, small light "
           "wooden boats. The Southern Han forces: tall multi-deck wooden warships with red banners, soldiers in "
           "Tang-style lamellar armor. No blood, no gore, no dead bodies shown.")
TRAILER_STYLE = ("Cinematic epic trailer shot, live-action realistic, dramatic natural light, sweeping camera, "
                 "vertical 9:16. No modern objects, no on-screen text. No blood, no gore, no children.")
TRAILER_AUDIO = ("Audio: deep war drums and natural ambient sound (wind, water, wood creaking); only the noted "
                 "Vietnamese line is spoken, with lip sync; no modern music.")

TRAILER = [
    dict(name="Hạm đội vượt biển",
         img="Cinematic wide aerial shot at dawn over a misty sea estuary with limestone hills, a vast fleet of tall multi-deck wooden warships with red banners and huge sails entering the mouth of a wide brown river, realistic, vertical 9:16.",
         vid="0-4s: Slow aerial push over the misty estuary at dawn; a vast fleet of tall warships with red banners glides in, oars beating in rhythm. 4-10s: Low angle on the water as a huge prow passes overhead, drums booming; a deep Vietnamese narrator's voice says: \"Năm 938. Quân Nam Hán vượt biển sang.\"",
         subs=[(4.0, 9.6, "Năm 938. / Quân Nam Hán vượt biển sang.")]),
    dict(name="Cọc bịt sắt",
         img=f"Cinematic night shot by torchlight on a muddy riverbed at low tide, rows of men hammering huge sharpened ironwood stakes with iron-capped tips into the mud, close-up of a gleaming iron tip in the foreground, {NGO} standing among them in torchlight, realistic, vertical 9:16.",
         vid=f"0-4s: Quick cinematic cuts by torchlight: mallets striking, a blacksmith fitting an iron cap onto a stake tip with sparks, rows of stakes rising from black mud. 4-10s: Close on {NGO} in the torchlight, looking out to sea; he says quietly: \"Thuyền chúng vào được... nhưng không ra được.\"",
         subs=[(4.5, 9.6, "Thuyền chúng vào được... / nhưng không ra được.")]),
    dict(name="Nước rút",
         img="Cinematic wide shot at midday over the Bạch Đằng estuary as the tide falls, a forest of dark iron-tipped stakes emerging from the water, huge warships tilting and stuck among them, hundreds of small Vietnamese boats charging out from the mangroves, realistic, vertical 9:16.",
         vid="0-5s: The water drops; a forest of iron-tipped stakes rises from the river; a huge warship slams onto them with a deep crack of timber and tilts; war drums on both banks. 5-10s: Hundreds of small boats burst out of the mangroves in slow motion; the camera rises high above the estuary and holds on the river.",
         subs=[(0.5, 4.5, "Nước rút... là lúc cọc lên."),
               (6.0, 9.8, "TRẬN BẠCH ĐẰNG / 938")]),
]

BATTLE = [
    # ---- Hồi 1: quyết định
    dict(name="Bàn kế ở Đại La", label="Đại La · cuối năm 938",
         img=f"First-person view of a soldier standing guard in a torch-lit wooden hall, {NGO} standing before a circle of generals, {FACE} standing guard beside the viewer with a spear, realistic, vertical 9:16.",
         vid=f"0-5s: {NGO} addresses his generals: \"Hoằng Tháo đem quân từ xa đến, quân mỏi mệt, lại mất nội ứng.\" 5-10s: He pauses: \"Nhưng chúng mạnh về thuyền. Ta phải đánh vào thuyền.\" Beside the viewer, Anh Tư nods hard as if he understood everything.",
         subs=[(0.5, 4.8, "Hoằng Tháo từ xa đến, quân mỏi mệt, / lại mất nội ứng."),
               (5.0, 9.6, "Nhưng chúng mạnh về thuyền. / Ta phải đánh vào thuyền.")]),
    dict(name="Kế cắm cọc", label="",
         img=f"First-person view over a large sand map of a river mouth drawn on the ground, {NGO} pressing a row of small sticks into the sand with his hand, {FACE} leaning in beside the viewer, curious, realistic, vertical 9:16.",
         vid=f"0-6s: {NGO} presses small sticks into the sand map across the river mouth: \"Cắm cọc lớn, đầu bịt sắt, ngầm dưới cửa biển. Triều lên, chúng vào. Triều xuống... chúng ở lại.\" 6-10s: Anh Tư whispers to the viewer: \"Ở lại... luôn ạ?\"",
         subs=[(0.3, 3.2, "Cắm cọc lớn, đầu bịt sắt, / ngầm dưới cửa biển."),
               (3.2, 6.0, "Triều lên, chúng vào. / Triều xuống... chúng ở lại."),
               (6.3, 9.6, "Ở lại... luôn ạ?")]),
    dict(name="Đẽo cọc lim", label="",
         img=f"First-person view in a forest clearing, men felling tall ironwood trees and sharpening thick trunks into stakes with axes, a blacksmith fitting iron caps on the tips at a small forge, {FACE} beside the viewer holding a heavy iron cap, realistic, vertical 9:16.",
         vid="0-5s: Axes chop, wood chips fly; men sharpen huge trunks; at a forge a blacksmith hammers an iron cap onto a stake tip, sparks flying. 5-10s: Anh Tư weighs the iron cap in his hand and says to the viewer: \"Mài nhọn rồi còn bịt sắt... cọc còn sang hơn cả em.\"",
         subs=[(5.0, 9.6, "Mài nhọn rồi còn bịt sắt... / cọc còn sang hơn cả em.")]),
    # ---- Hồi 2: cắm cọc
    dict(name="Cắm cọc lúc triều rút", label="Cửa sông Bạch Đằng · đêm, triều rút",
         img=f"First-person view at night on a wide muddy riverbed at low tide, torches along the bank, hundreds of men in mud up to their knees driving huge slanted iron-tipped stakes into the riverbed in long rows, {FACE} beside the viewer swinging a big wooden mallet, realistic, vertical 9:16.",
         vid="0-5s: The viewer and Anh Tư drive a huge stake into the mud with mallets, row after row of stakes stretching away by torchlight. 5-10s: An officer walks along the line: \"Nhanh lên! Trước khi nước lên!\" Anh Tư, covered in mud: \"Bùn đến đùi rồi anh ơi!\"",
         subs=[(5.0, 7.4, "Nhanh lên! Trước khi nước lên!"),
               (7.4, 9.6, "Bùn đến đùi rồi anh ơi!")]),
    dict(name="Nước lên, cọc biến mất", label="",
         img=f"First-person view at dawn from a small boat on a wide calm river, the tide high, the surface smooth with no stakes visible, mist, {FACE} in the boat looking down at the water, realistic, vertical 9:16.",
         vid="0-5s: Dawn; the tide has come in and the river is smooth and calm, no stake visible anywhere. The officer in the boat: \"Nhớ chỗ này. Lát nữa đừng có chèo vào đây.\" 5-10s: Anh Tư looks around at the identical water in every direction: \"Em nhớ rồi! ...Mà chỗ nào cũng là nước anh ạ.\"",
         subs=[(0.5, 4.8, "Nhớ chỗ này. / Lát nữa đừng có chèo vào đây."),
               (5.0, 9.6, "Em nhớ rồi! ...Mà chỗ nào / cũng là nước anh ạ.")]),
    # ---- Hồi 3: mai phục và nhử
    dict(name="Mai phục", label="Sáng hôm sau · triều lên",
         img=f"First-person view hidden among dense mangrove roots on the riverbank, rows of Vietnamese archers and spearmen crouching silently, small boats hidden in a side creek, {FACE} crouching beside the viewer with a finger on his lips, realistic, vertical 9:16.",
         vid="0-6s: Silence in the mangroves; archers crouch, boats hidden in a side creek, only birds and water. A lookout in a tree suddenly hisses: \"Buồm! Ngoài cửa biển!\" 6-10s: Every head turns toward the sea; Anh Tư grips his spear and swallows hard.",
         subs=[(0.5, 4.0, "Bờ bên kia cũng mai phục. / Không ai được thở mạnh."),
               (4.0, 6.5, "Buồm! Ngoài cửa biển!")]),
    dict(name="Hạm đội Nam Hán", label="",
         img=f"First-person view from a small low boat at water level, a huge multi-deck Southern Han warship with red banners towering above, a young adult commander in ornate armor standing at its prow, more warships behind, {FACE} in the boat looking up with his mouth open, realistic, vertical 9:16.",
         vid="0-6s: From the low boat, the giant warships slide past, rows of oars, red banners, a young armored commander at the prow pointing forward. 6-10s: Anh Tư stares up and whispers: \"Thuyền nó to bằng cả cái làng em...\"",
         subs=[(0.5, 5.5, "Chủ tướng Nam Hán: Lưu Hoằng Tháo, / con trai vua Nam Hán."),
               (6.0, 9.6, "Thuyền nó to / bằng cả cái làng em...")]),
    dict(name="Ra khiêu chiến", label="",
         img=f"First-person view from a light boat rowing fast toward a line of huge warships, Vietnamese soldiers in the boat shouting and shooting a few arrows, {FACE} rowing hard beside the viewer, realistic, vertical 9:16.",
         vid="0-5s: The light boats dart toward the huge fleet; soldiers shout taunts and loose a few arrows that thud into the wooden hulls. The officer: \"Đánh vài miếng rồi chạy. Chạy cho thật!\" 5-10s: The warships turn toward them, drums booming. Anh Tư grins: \"Khoản chạy em giỏi nhất!\"",
         subs=[(0.5, 4.8, "Đánh vài miếng rồi chạy. / Chạy cho thật!"),
               (5.0, 9.6, "Khoản chạy em giỏi nhất!")]),
    dict(name="Giả thua", label="",
         img=f"First-person view from a fleeing light boat looking back over the stern, huge warships chasing upstream on the high tide over calm water, arrows falling short into the water, {FACE} looking back excitedly, realistic, vertical 9:16.",
         vid="0-5s: The light boats flee upstream; behind them the huge warships give chase over the calm high water, arrows splashing short. 5-10s: Anh Tư looks back and whispers excitedly: \"Nó qua bãi cọc rồi... qua hết rồi!\"",
         subs=[(0.5, 4.8, "Nước đang lên, cọc ngập sâu. / Thuyền giặc cứ thế đi qua."),
               (5.0, 9.6, "Nó qua bãi cọc rồi... / qua hết rồi!")]),
    # ---- Hồi 4: nước rút, phản công
    dict(name="Chờ nước rút", label="Quá trưa · triều bắt đầu rút",
         img=f"First-person view on a hilltop above the estuary, {NGO} watching a wooden marker pole in the river where the waterline is dropping, a signal flag in his hand, drummers ready behind him, realistic, vertical 9:16.",
         vid=f"0-6s: Close on the marker pole: the waterline slowly drops. {NGO} watches without moving. 6-10s: He raises the signal flag high: \"Nước rút rồi. Đánh!\" The great war drums thunder from both banks.",
         subs=[(0.5, 5.5, "Nước rút dần. / Cả đội chờ một lá cờ."),
               (6.0, 9.6, "Nước rút rồi. Đánh!")]),
    dict(name="Phản công", label="",
         img=f"First-person view from a light boat surging forward among hundreds of small boats bursting out of the mangrove creeks, archers on both banks shooting volleys of arrows toward huge warships that are turning back toward the sea, {FACE} rowing furiously and shouting, realistic, vertical 9:16.",
         vid="0-5s: Hundreds of small boats burst out of the side creeks; volleys of arrows arc from both banks and thud into the warships' wooden sides and sails. 5-10s: The warships try to turn back toward the sea with the falling tide; Anh Tư rows and yells: \"Giờ thì đến lượt mình đuổi!\"",
         subs=[(0.5, 4.8, "Hai bên bờ cùng đánh ra. / Giặc quay đầu về biển."),
               (5.0, 9.6, "Giờ thì đến lượt mình đuổi!")]),
    dict(name="Thuyền đâm cọc", label="",
         img=f"First-person view from a small boat as a huge warship fleeing toward the sea crashes onto iron-tipped stakes just under the falling water, timber splintering, the ship lurching and stuck, {FACE} pointing at it with a huge chipped-tooth grin, realistic, vertical 9:16.",
         vid="0-5s: A fleeing warship hits the hidden stakes with a deep crunch of timber; it lurches, stuck fast; another ship behind slams into it. 5-10s: Anh Tư stands up in the boat, pointing and laughing: \"Cọc nhà em! Cọc nhà em trúng rồi!\"",
         subs=[(0.5, 4.8, "Nước rút gấp. / Thuyền giặc mắc cọc, không lùi được."),
               (5.0, 9.6, "Cọc nhà em! / Cọc nhà em trúng rồi!")]),
    dict(name="Không cho chiếc nào ra", label="",
         img=f"First-person view among stuck and tilting warships in a forest of stakes, Vietnamese soldiers in small boats hooking the ships' sides with long hooked poles and climbing aboard, enemy soldiers abandoning ships and wading through shallow water, {FACE} throwing a hooked pole, realistic, vertical 9:16.",
         vid="0-5s: Warships tilt and jam against each other among the stakes; one slowly capsizes onto its side. Enemy soldiers drop their weapons and wade through the shallow water toward the banks. 5-10s: The officer shouts: \"Móc lấy thuyền! Không để chiếc nào ra!\" Anh Tư hooks a ship's rail with a long pole and pulls hard.",
         subs=[(0.5, 4.8, "Thuyền lật, thuyền mắc, / quân giặc bỏ thuyền lội vào bờ."),
               (5.0, 9.6, "Móc lấy thuyền! / Không để chiếc nào ra!")]),
    # ---- Hồi 5: kết
    dict(name="Tin báo", label="Chiều tối",
         img=f"First-person view at sunset over the estuary full of stuck, tilted warships among the stakes, disarmed enemy soldiers sitting on the riverbank under guard, a messenger running along the bank, {FACE} beside the viewer exhausted and covered in mud, realistic, vertical 9:16.",
         vid="0-5s: Sunset; the estuary is full of stuck, tilted warships; disarmed enemy soldiers sit quietly on the bank under guard. 5-10s: A messenger runs past shouting: \"Chủ tướng giặc Hoằng Tháo đã tử trận!\" The viewer and Anh Tư look at each other in silence.",
         subs=[(0.5, 4.8, "Quân giặc chết đuối quá nửa / (Đại Việt sử ký toàn thư)."),
               (5.0, 9.6, "Chủ tướng giặc Hoằng Tháo / đã tử trận!")]),
    dict(name="Ghi tên em vào sử", label="Cổ Loa · mùa xuân năm 939",
         img=f"First-person view from a joyful crowd at the earthen walls of Cổ Loa citadel in spring, {NGO} standing on a platform before banners, {FACE} in the crowd beside the viewer with a proud chipped-tooth grin, realistic, vertical 9:16.",
         vid=f"0-5s: Spring; a joyful crowd before the walls of Cổ Loa; {NGO} stands on a platform. A calm narrator's voice says: \"Năm 939, Ngô Quyền xưng vương, đóng đô ở Cổ Loa.\" 5-10s: Anh Tư turns to the camera, grinning: \"Cọc thứ ba hàng thứ bảy là em cắm đấy! Ghi tên em vào sử nhé!\"",
         subs=[(0.3, 4.6, "Năm 939, Ngô Quyền xưng vương, / đóng đô ở Cổ Loa."),
               (4.8, 8.4, "Cọc thứ ba hàng thứ bảy là em cắm! / Ghi tên em vào sử nhé!")]),
]

HISTORY = """**Lịch sử (theo *Đại Việt sử ký toàn thư*, sử Trung Quốc cũng chép trận thua này):**

- Mùa xuân năm 937, Kiều Công Tiễn giết Tiết độ sứ Dương Đình Nghệ. Ngô Quyền, con rể Dương Đình Nghệ, đem quân từ Ái Châu ra đánh.
- Kiều Công Tiễn cầu cứu nước Nam Hán. Vua Nam Hán sai con là Lưu Hoằng Tháo cầm quân thủy sang, tự mình đóng quân ở Hải Môn để tiếp ứng.
- Cuối năm 938, Ngô Quyền giết Kiều Công Tiễn trước, rồi bàn với các tướng: Hoằng Tháo từ xa đến, quân mệt, lại mất người làm nội ứng; nhưng giặc mạnh về chiến thuyền, nên sai cắm cọc lớn vạt nhọn, đầu bịt sắt, ngầm ở cửa biển.
- Khi triều lên, Ngô Quyền cho thuyền nhẹ ra khiêu chiến, giả thua để nhử. Thuyền Nam Hán đuổi vào trong bãi cọc. Triều rút, quân ta đánh ra, thuyền giặc mắc cọc mà lật, quân giặc chết đuối quá nửa, Hoằng Tháo tử trận. Vua Nam Hán khóc, thu quân về nước.
- Năm 939, Ngô Quyền xưng vương, đóng đô ở Cổ Loa. Sử học Việt Nam xem đây là mốc khép lại thời Bắc thuộc.

**Phần dựng lại (sử không chép chi tiết):** mai phục hai bên bờ, cọc gỗ lim, cột đo mực nước, móc câu kéo thuyền, thời điểm "quá trưa". Bãi cọc của trận 938 hiện chưa xác định được vị trí. Các bãi cọc đã khai quật ở Quảng Yên là của trận năm 1288.

**Hư cấu:** Anh Tư, người lính "bạn", viên chỉ huy thuyền nhẹ và mọi lời thoại. Lời Ngô Quyền ở clip 1, 2 của trận đánh và ở trailer phỏng theo lời ông chép trong *Toàn thư*, không phải nguyên văn."""

NGO_REF = ("Portrait photo of a stern, calm Vietnamese commander around 40 with a short black beard, hair in a "
           "topknot, dark lacquered leather armor and a deep-red cloak, standing on a riverbank with mangroves and "
           "limestone hills in mist behind, dignified expression, realistic, natural light, head and shoulders, "
           "vertical 9:16.")


NOTE_TRAILER = """**Video riêng, 30 giây, 3 clip Muse** quay kiểu phim (không phải góc nhìn thứ nhất). Đăng trước video trận đánh một ngày để nhử người xem. Prompt ảnh tham chiếu Ngô Quyền ở dưới, dùng chung với video trận đánh.

**Kiểm duyệt:** không có máu, không có xác, không có trẻ em."""

NOTE_BATTLE = """**Video riêng, 2 phút 30 giây, 15 clip Muse** (mỗi clip 10 giây), góc nhìn thứ nhất, có Anh Tư. Trailer 30 giây nằm ở file `bach-dang-938-trailer.md`.

| Hồi | Clip | Thời gian | Nội dung |
|---|---|---|---|
| 1 · Quyết định | 1–3 | 0:00–0:30 | Bàn kế ở Đại La, kế cắm cọc, đẽo cọc lim bịt sắt |
| 2 · Cắm cọc | 4–5 | 0:30–0:50 | Cắm cọc đêm triều rút, sáng ra nước lên che hết cọc |
| 3 · Nhử giặc | 6–9 | 0:50–1:30 | Mai phục, hạm đội Nam Hán vào, thuyền nhẹ khiêu chiến, giả thua kéo giặc qua bãi cọc |
| 4 · Phản công | 10–13 | 1:30–2:10 | Chờ nước rút, hai bờ đánh ra, thuyền đâm cọc, móc thuyền không cho chiếc nào ra |
| 5 · Kết | 14–15 | 2:10–2:30 | Tin Hoằng Tháo tử trận, Ngô Quyền xưng vương ở Cổ Loa |

**Anh Tư** dùng lại ảnh chân dung trong `../bach-dang/README.md`. **Ngô Quyền** dùng ảnh tham chiếu bên dưới (giống file trailer) để mặt giữ nguyên qua các clip.

**Kiểm duyệt:** cảnh đánh nhau không có máu, không có xác. Thuyền lật và quân giặc lội vào bờ; chuyện chết đuối và Hoằng Tháo tử trận chỉ nói bằng chữ và lời. Không có trẻ em. Hoằng Tháo dựng là người trưởng thành."""

TAGS = "#povlichsu #lichsuvietnam #bachdang #bachdang938 #ngoquyen #anhtu #xuhuong #fyp"

BATTLE_POST = dict(
    hook="Trận Bạch Đằng 938 / diễn biến từng bước",
    hooks_alt=["Thuyền giặc vào được / nhưng không ra được", "Vì sao Ngô Quyền / chờ nước rút mới đánh?"],
    end="Follow để xem / Bạch Đằng lần thứ hai (981) →", end_secs=1.5,
    tt_title="Trận Bạch Đằng 938 diễn biến từng bước: vì sao thuyền giặc vào được mà không ra được?",
    caption=("Trận Bạch Đằng năm 938, diễn biến từng bước ⚔️ Ngô Quyền cắm cọc bịt sắt ngầm ở cửa biển, nhử thuyền "
             "Nam Hán vào lúc triều lên, chờ nước rút mới đánh. Kết quả: chủ tướng Lưu Hoằng Tháo tử trận, năm sau "
             "Ngô Quyền xưng vương. Theo bạn, chi tiết nào trong trận này hay nhất? 👇"),
    pin=("Câu đố: trận Bạch Đằng 938 đánh lúc nước lên hay nước rút? Trả lời mà không xem lại video nhé 😏 "
         "Follow để xem Bạch Đằng lần thứ hai năm 981!"),
    yt_title="Trận Bạch Đằng 938 diễn biến từng bước: vì sao thuyền giặc vào mà không ra được?",
    yt_tags=("trận bạch đằng, bạch đằng 938, ngô quyền, lưu hoằng tháo, nam hán, cắm cọc bạch đằng, "
             "lịch sử việt nam, pov lịch sử, anh tư, đại việt, chiến thắng bạch đằng, shorts"),
    yt_note=("Video dọc 2 phút 30 giây vẫn được tính là Shorts (tối đa 3 phút). Ở mục \"Video liên quan\" chọn "
             "trailer, và ngược lại ở trailer chọn video này."),
    desc_extra=("Video do AI tạo, dựa trên Đại Việt sử ký toàn thư; nhân vật Anh Tư và lời thoại là hư cấu, một số "
                "chi tiết trận đánh là dựng lại. Đăng ký kênh để xem mỗi ngày một ngày sống ở Đại Việt."),
)

TRAILER_POST = dict(
    hook="Thuyền vào được / nhưng không ra được",
    hooks_alt=["Năm 938 / hạm đội Nam Hán vượt biển", "Nước rút... / là lúc cọc lên"],
    end="Trận đầy đủ / ở trang cá nhân →", end_secs=1.8,
    tt_title="Năm 938, hạm đội Nam Hán vượt biển sang. Thuyền vào được... nhưng không ra được",
    caption=("Năm 938. Hạm đội Nam Hán vượt biển sang. Thuyền chúng vào được... nhưng không ra được ⚔️ Trận đánh "
             "đầy đủ, diễn biến từng bước, đăng ngày mai. Follow để không lỡ!"),
    pin=("Bạn đoán Ngô Quyền dùng cách gì để thuyền giặc \"không ra được\"? 👇 "
         "(Đăng video trận đánh xong thì sửa thành: \"Trận đầy đủ đã lên, xem ở trang cá nhân 👆\")"),
    yt_title="Năm 938: thuyền giặc vào được… nhưng không ra được",
    yt_tags=("trận bạch đằng, bạch đằng 938, ngô quyền, trailer lịch sử, nam hán, lịch sử việt nam, đại việt, "
             "shorts"),
    yt_note="Ở mục \"Video liên quan\" chọn video trận đánh khi đã đăng.",
    desc_extra="Video do AI tạo, dựa trên Đại Việt sử ký toàn thư. Đăng ký kênh để xem trận đánh đầy đủ.",
)


def posting(p):
    hook_line = p["hook"].replace(" / ", " ")
    yt_hash = " ".join(t for t in TAGS.split() if t not in ("#fyp", "#xuhuong"))
    return ["## Đăng TikTok", "",
            "**Hook** (chữ to ở giây đầu, đã có trong video; dùng làm chữ trên ảnh bìa):", "```", hook_line, "```", "",
            "Hook dự phòng:", "```", "\n".join(h.replace(" / ", " ") for h in p["hooks_alt"]), "```", "",
            "**Tiêu đề:**", "```", p["tt_title"], "```", "",
            "**Mô tả và hashtag:**", "```", p["caption"], TAGS, "```", "",
            "**Bình luận ghim:**", "```", p["pin"], "```", "",
            "Khi đăng: bật nhãn \"Nội dung do AI tạo\".", "",
            "## Đăng YouTube Shorts", "",
            "**Tiêu đề:**", "```", f"{p['yt_title']} #Shorts", "```", "",
            "**Mô tả:**", "```", p["caption"], "", p["desc_extra"], "", f"#Shorts {yt_hash}", "```", "",
            "**Thẻ:**", "```", p["yt_tags"], "```", "",
            "**Bình luận ghim:**", "```", p["pin"].replace("Follow", "Đăng ký"), "```", "",
            p["yt_note"], "",
            "Khi đăng: ở mục \"Nội dung bị thay đổi\" chọn **Có**.", ""]


def plan_head(base, p):
    return [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4",
            f"hook: {p['hook']}", f"end: {p['end']}", f"end_giay: {p['end_secs']}", ""]


def main():
    # ---------------- trailer
    md = ["# Trận Bạch Đằng 938: trailer 30 giây", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          NOTE_TRAILER, "", "## Ảnh tham chiếu Ngô Quyền (làm một lần, dùng chung hai video)", "",
          "```", NGO_REF, "```", ""]
    plan, subs = plan_head("bach-dang-938-trailer", TRAILER_POST), []
    for i, c in enumerate(TRAILER, 1):
        f = f"bd938-t{i}.mp4"
        md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{f}`", "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", f"{TRAILER_STYLE} {SETTING} {c['vid']} {TRAILER_AUDIO}", "```", ""]
        plan.append(f"clip: {f} |")
        # clip cuối: câu chữ kết thúc trước dòng kết để không đè nhau
        subs += [f"sub: {i} | {a}-{min(b, 8.0) if i == len(TRAILER) else b} | {t}" for a, b, t in c["subs"]]
    plan += [""] + subs
    md += posting(TRAILER_POST) + ["## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(),
                                   "```", ""]
    out = {"bach-dang-938-trailer.md": md, "bach-dang-938-trailer.plan.txt": plan}

    # ---------------- trận đánh
    md = ["# Trận Bạch Đằng 938: diễn biến trận đánh (2 phút 30 giây)", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          NOTE_BATTLE, "", HISTORY, "", "## Ảnh tham chiếu Ngô Quyền (giống file trailer)", "",
          "```", NGO_REF, "```", ""]
    plan, subs = plan_head("bach-dang-938-tran-danh", BATTLE_POST), []
    for j, c in enumerate(BATTLE, 1):
        f = f"bd938-{j:02d}.mp4"
        md += [f"## Clip {j}: {c['name']}", f"File Muse đặt tên: `{f}`", "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", f"{POV} {SETTING} Anh Tư is {FACE}. {c['vid']} {AUDIO}", "```", ""]
        plan.append(f"clip: {f} | {c['label']}")
        subs += [f"sub: {j} | {a}-{b} | {t}" for a, b, t in c["subs"]]
    plan += [""] + subs
    md += posting(BATTLE_POST) + ["## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(),
                                  "```", ""]
    out.update({"bach-dang-938-tran-danh.md": md, "bach-dang-938-tran-danh.plan.txt": plan})

    for name, lines in out.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
