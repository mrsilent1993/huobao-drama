#!/usr/bin/env python3
"""Nguồn của loạt "POV người bình thường" (bản 2). Sửa ở đây rồi chạy: python3 _nguon.py

Công thức (từ video Bạch Đằng 938: 1,4 triệu lượt xem, 43,6% xem hết, 14 nghìn lượt chia sẻ):
- Nhân vật quen mặt: ANH TƯ (sẹo ngang lông mày trái, răng cửa mẻ, cười toe). Mỗi tập là một đời con cháu,
  đời nào cũng bị giao một việc vô lý mà không ai giải thích.
- Giây 0: lao động cận cảnh + câu lệnh vô lý. Mỗi clip đúng MỘT câu chốt ngắn.
- Clip cuối: vỡ lẽ bằng cảnh lớn + một câu chốt RIÊNG của tập, nối lại chi tiết trong tập (từ 19/11/2026 không dùng
  câu "Ghi tên em vào sử nhé!" nữa; câu này chỉ còn ở các tập đã đăng).
- TikTok 30 giây = clip 1, 3, 5. YouTube 50 giây = đủ 5 clip (clip 2, 4 là trò cười riêng, không phải clip đệm).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")

HUE = ("a lean young man of about 18 with curly hair, very bright piercing eyes and a ringing voice, in plain "
       "dark-indigo clothes with a red headband")

QING_VIS = '**Chuẩn hình ảnh quân Thanh 1789 (⚠️ hiểu biết chung, xem `../nghien-cuu/chuan-hinh-anh-quan-doi.md`):** lính cạo nửa đầu trước, tết đuôi sam, áo vải dài quá gối màu sẫm (xanh lam hoặc nâu), ủng vải, nón tre hoặc nón dạ; quan mặc triều phục có bổ tử thêu, mũ có quả đỉnh. Không có chữ trên áo hay trên cờ, không quân phục kiểu Âu, không cờ hiện đại.'
QING_EN = 'Qing soldiers of 1789 have shaved foreheads and long braided queues, wear plain dark-blue or brown knee-length cotton tunics over trousers, cloth boots and conical bamboo or felt hats; Qing officers wear court robes with an embroidered square rank badge and a hat with a finial. Absolutely NO European uniforms, NO epaulettes, NO modern rifles, NO characters or writing on any clothing, flag or sign.'

LEN_FULL = ("hai video từ cùng 5 clip: **bản dài** (YouTube, khoảng 48 giây sau chuyển cảnh) và **bản ngắn** "
            "(TikTok, khoảng 38 giây) vẫn đủ cả 5 cảnh: 3 clip chính giữ nguyên, 2 clip phụ cắt lấy 5 giây chứa "
            "câu chính (xem ghi chú \"Bản TikTok\" ở từng clip)")
LEN_FULL_45 = ("hai video từ cùng 5 clip: **bản dài** (YouTube, khoảng 48 giây) và **bản ngắn** (TikTok, khoảng 43 giây) "
               "vẫn đủ cả 5 cảnh: clip 4 cắt lấy 5 giây chứa câu chính, các clip khác giữ nguyên")

NOTE = ("**Anh Tư:** nhân vật của video 1,4 triệu. Mỗi tập là một đời con cháu, cùng một gương mặt: **sẹo ngang "
        "lông mày trái, răng cửa mẻ, cười toe**. Dùng lại ảnh chân dung Anh Tư (prompt trong `../bach-dang/README.md`) "
        "làm ảnh tham chiếu trong Muse, chỉ đổi trang phục theo thời. **Bản TikTok 30 giây** gồm clip 1, 3, 5; **bản "
        "YouTube 50 giây** gồm đủ 5 clip.")

EPISODES = [
    # ------------------------------------------------------------------ 1077
    dict(
        slug="cam-tre-nhu-nguyet-1077", prefix="nbt1",
        title="Bị bắt cắm tre cả đêm mà không ai nói để làm gì, sáng ra mới hiểu (Như Nguyệt, 1077)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1077, quân Lý dựng phòng tuyến dọc bờ nam sông Như Nguyệt (sông Cầu): lũy đất, "
                 "cọc tre cắm dày nhiều tầng, dưới bãi sông có hố chông ngầm. Quân Tống của Quách Quỳ kéo đến bờ bắc, "
                 "nhiều lần vượt sông không được, bị giữ chân nhiều tuần rồi giảng hòa rút quân. **Hư cấu:** Anh Tư, "
                 "các tình huống và mọi lời thoại."),
        setting=("Vietnam, Lý dynasty, early 1077, the south bank of the Như Nguyệt River (Cầu River) at night and at "
                 "dawn: an earthen rampart, rows of sharpened bamboo stakes, pits on the muddy river flat, mist; across "
                 "the river a huge Song army camp. Villagers and soldiers with short cropped hair, black-lacquered teeth, "
                 f"brown clothes, barefoot; an officer in a dark-red uniform. Anh Tư is {FACE}, in a brown shirt."),
        hook="POV: Cắm tre cả đêm / không ai nói để làm gì",
        end="Follow để xem Anh Tư / bị bắt khuân hết thóc đi →",
        clips=[
            dict(name="Lệnh vô lý", label="Bờ sông Như Nguyệt · đêm 1077",
                 img=f"First-person close-up at night by moonlight of muddy hands hammering a sharpened bamboo stake into an earthen rampart, {FACE} beside the viewer holding the stake and frowning, rows of stakes behind, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer hammers a bamboo stake by moonlight while Anh Tư holds it steady and frowns at the endless rows: \"Cắm tre dày thế này... giặc sang hay vịt sang hả anh?\" 5-10s: An officer walks past without stopping: \"Cắm đi. Không hỏi.\" Anh Tư sighs and grabs another stake.",
                 subs=[(0.5, 4.8, "Cắm tre dày thế này... / giặc sang hay vịt sang hả anh?"),
                       (5.0, 9.5, "Cắm đi. Không hỏi.")]),
            dict(name="Hố tự đào", tiktok="bo", label="Nửa đêm",
                 img=f"First-person view on a muddy river flat at night, {FACE} standing next to a freshly covered pit hidden under reeds, smug, holding a shovel, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư finishes covering a pit with reeds and mud and brushes his hands proudly: \"Đào hố xong lại lấp kín. Đúng là việc vô ích nhất đời em.\" 5-10s: He takes one step back and drops straight into his own pit up to the chest; from inside, he looks up at the viewer and says slowly: \"...À. Ra là để thế này.\"",
                 subs=[(0.5, 4.8, "Đào hố xong lại lấp kín. / Đúng là việc vô ích nhất đời em."),
                       (5.0, 9.5, "...À. Ra là để thế này.")]),
            dict(name="Sương tan", label="Rạng sáng",
                 img=f"First-person view at dawn from the top of an earthen rampart lined with bamboo stakes, mist lifting over the river to reveal a huge Song army with thousands of banners on the far bank, {FACE} beside the viewer frozen with his mouth open, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; the mist lifts and reveals a huge Song army filling the far bank, thousands of banners. 5-10s: Anh Tư stares, mouth open, then whispers: \"...Vịt nhà ai mà đông thế anh?\"",
                 subs=[(5.0, 9.5, "...Vịt nhà ai mà đông thế anh?")]),
            dict(name="Giặc thử sang", tiktok="bo", label="Mấy hôm sau",
                 img="First-person view from an earthen rampart, Song soldiers wading across a shallow part of the river, stumbling into hidden pits and getting stuck among bamboo stakes, then retreating in confusion, no blood, realistic, vertical 9:16.",
                 vid="0-5s: A group of Song soldiers tries to wade across a shallow stretch; one after another they plunge into hidden pits and tangle in the bamboo stakes, then scramble back to their own bank. 5-10s: Anh Tư jumps up on the rampart, pointing: \"Cái hố kia em đào! Em cũng ngã rồi, em biết nó đau!\"",
                 subs=[(5.0, 9.5, "Cái hố kia em đào! / Em cũng ngã rồi, em biết nó đau!")]),
            dict(name="Câu chốt", label="Mấy tuần sau",
                 img=f"First-person view from an earthen rampart lined with bamboo stakes, across the river Song soldiers sitting idle at their camp, one fishing, {FACE} on the rampart eating a rice ball and waving at them cheerfully, realistic, vertical 9:16.",
                 vid="0-5s: Weeks later; across the river, Song soldiers sit idle, one of them fishing, staring at the wall of bamboo. 5-10s: Anh Tư, eating a rice ball on the rampart, waves at them, then turns to the camera with his chipped-tooth grin: \"Cắm một đêm, nó đứng nhìn cả tháng. Tre làng em... bảo hành trọn đời!\"",
                 subs=[(5.0, 9.8, "Cắm một đêm, nó đứng / nhìn cả tháng. Tre làng em / bảo hành trọn đời!")]),
        ],
        caption=("Bị bắt cắm tre cả đêm mà không ai nói để làm gì, sáng ra mới hiểu 😳 Năm 1077, lũy đất, cọc tre "
                 "nhiều tầng và hố chông ngầm ở sông Như Nguyệt giữ chân quân Tống hàng tuần liền. Sử không ghi tên "
                 "người cắm tre, nhưng không có họ thì không có trận này. Tag đứa bạn hay hỏi \"làm cái này để làm gì\" 👇"),
        tags="#nhunguyet #lythuongkiet #1077",
    ),
    # ------------------------------------------------------------------ 1285
    dict(
        slug="khuan-thoc-1285", prefix="nbt2",
        title="Bị bắt khuân hết thóc đi, bỏ trống cả nhà, ba ngày sau mới hiểu (vườn không nhà trống, 1285)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1285, nhà Trần rút quân, cho dân sơ tán và mang lương thực theo, để lại Thăng Long "
                 "trống không, gọi là kế **\"vườn không nhà trống\"**. Quân Nguyên chiếm được thành nhưng không có gì ăn, "
                 "dần đói, hao quân rồi phải bỏ Thăng Long. **Lưu ý:** chưa thấy nguồn chép dân tự **đốt** thóc, nên tập "
                 "phim dùng \"mang đi\". **Hư cấu:** Anh Tư, mẹ Anh Tư, các tình huống và lời thoại."),
        setting=("Vietnam, Trần dynasty, early 1285, a village near Thăng Long, a mountain hideout, and the empty "
                 "capital. Villagers with short cropped hair, black-lacquered teeth, brown clothes, carrying rice sacks "
                 "and baskets on shoulder poles; a village elder; Mongol-Yuan soldiers in leather armor and fur-trimmed "
                 f"hats. Anh Tư is {FACE}. His mother, Mẹ Anh Tư, is a tiny, fierce, sharp-tongued woman around 55 with "
                 "black teeth, chewing betel."),
        hook="POV: Khuân hết thóc đi / bỏ trống cả nhà",
        end="Ba ngày sau, giặc ăn gì? / Follow để xem Anh Tư / bị lệnh phải thua trận →",
        clips=[
            dict(name="Lệnh vô lý", label="Làng ven Thăng Long · đầu năm 1285",
                 img="First-person close-up of hands heaving a heavy rice sack onto a shoulder pole in a dim thatched granary, grains spilling, a tiny fierce old woman with black teeth grabbing the other end of the sack, a village elder with a torch at the door, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer heaves a heavy rice sack onto a shoulder pole; the village elder at the door orders: \"Mang hết thóc đi! Không để lại một hạt!\" 5-10s: Mẹ Anh Tư grabs the sack and glares at him: \"Giặc chưa đến mà nhà tôi đã bị cướp trước rồi!\"",
                 subs=[(0.5, 4.8, "Mang hết thóc đi! / Không để lại một hạt!"),
                       (5.0, 9.5, "Giặc chưa đến mà nhà tôi / đã bị cướp trước rồi!")]),
            dict(name="Vại cà", tiktok="bo", label="Sáng hôm sau",
                 img=f"First-person view on a steep mountain path, {FACE} staggering under a huge clay jar of pickled eggplant tied to his back, sweating, his tiny mother walking ahead carrying nothing, realistic, vertical 9:16.",
                 vid="0-5s: On a steep mountain path, Anh Tư staggers under a huge clay jar of pickled eggplant strapped to his back: \"Mẹ ơi, vại cà thì giặc ăn được à? Bỏ lại đi!\" 5-10s: His tiny mother, walking ahead carrying nothing, doesn't turn around: \"Giặc không ăn thì mày ăn. Vác.\"",
                 subs=[(0.5, 4.8, "Mẹ ơi, vại cà thì giặc ăn được à? / Bỏ lại đi!"),
                       (5.0, 9.5, "Giặc không ăn thì mày ăn. Vác.")]),
            dict(name="Mỗi bữa một nắm", label="Trên núi · ngày thứ hai",
                 img="First-person view in a crowded mountain hideout at dusk, a tiny fierce old woman pouring a single handful of rice into a pot, villagers sitting among hidden rice sacks, smoke rising from an empty city far below, realistic, vertical 9:16.",
                 vid="0-5s: In the mountain hideout, Mẹ Anh Tư drops exactly one handful of rice into the pot from a full sack and ties it shut again; Anh Tư stares: \"Cả bao thóc mà nấu một nắm... khổ thế này để làm gì?\" 5-10s: She points her chin down at the empty capital far below: \"Để đứa khác khổ hơn.\"",
                 subs=[(0.5, 4.8, "Cả bao thóc mà nấu một nắm... / khổ thế này để làm gì?"),
                       (5.0, 9.5, "Để đứa khác khổ hơn.")]),
            dict(name="Thành trống", tiktok="bo", label="Thăng Long · cùng lúc",
                 img="First-person view peeking over a wall in an empty ancient city, Mongol-Yuan soldiers kicking open empty granaries, one soldier shaking an empty basket upside down, another holding up a single forgotten pumpkin as others crowd around it, realistic, vertical 9:16.",
                 vid="0-5s: Sent down to scout, the viewer peeks over a wall: Mongol-Yuan soldiers kick open granary after granary, all empty; one shakes an empty basket upside down. 5-10s: A soldier holds up a single forgotten pumpkin; a crowd of soldiers immediately gathers around it, staring at it hungrily.",
                 subs=[]),
            dict(name="Câu chốt", label="Ba ngày sau",
                 img=f"First-person view from behind a bush on a hillside, thin exhausted Mongol-Yuan soldiers below digging for roots in an empty field, one chewing grass, a tiny fierce old woman with black teeth peeking beside {FACE}, realistic, vertical 9:16.",
                 vid="0-5s: Three days later; from behind a bush, they watch thin, exhausted enemy soldiers dig for roots, one chewing a blade of grass. Mẹ Anh Tư nods with satisfaction: \"Mời giặc vào nhà mà không mời cơm. Thế mới là lễ.\" 5-10s: Anh Tư turns to the camera, grinning with his chipped tooth: \"Mẹ em mà cầm quân... giặc còn đói sớm hơn!\"",
                 subs=[(0.5, 4.8, "Mời giặc vào nhà mà không mời cơm. / Thế mới là lễ."),
                       (5.0, 9.5, "Mẹ em mà cầm quân... / giặc còn đói sớm hơn!")]),
        ],
        caption=("Bị bắt khuân hết thóc đi, bỏ trống cả nhà, ba ngày sau mới hiểu 😏 Năm 1285, kế \"vườn không nhà "
                 "trống\" khiến quân Nguyên chiếm được Thăng Long mà không có gì ăn. Mẹ bạn có chịu bỏ lại vại cà "
                 "không? 👇"),
        tags="#vuonkhongnhatrong #nhatran #1285",
    ),
    # ------------------------------------------------------------------ 1288
    dict(
        slug="lenh-phai-thua-1288", prefix="nbt3",
        title="Bị lệnh phải thua trận mà không ai nói vì sao, tưởng thua thật, hóa ra... (Bạch Đằng, 1288)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1288, quân Trần cho thuyền nhỏ ra khiêu chiến thủy quân Nguyên của Ô Mã Nhi lúc "
                 "triều lên, rồi giả thua bỏ chạy, nhử thuyền giặc vào khúc sông Bạch Đằng đã cắm cọc. Triều rút, thuyền "
                 "giặc mắc cọc và bị đánh tan, Ô Mã Nhi bị bắt sống. **Hư cấu:** Anh Tư, chuyện ném trúng mũ tướng giặc "
                 "và mọi lời thoại."),
        setting=("Vietnam, Trần dynasty, spring 1288, the Bạch Đằng River estuary: tidal water, mangroves, small light "
                 "Vietnamese boats; huge Yuan warships with many sails; a burly bearded Yuan admiral in ornate armor and a "
                 "tall plumed helmet. Trần soldiers with short cropped hair, black-lacquered teeth, brown uniforms, "
                 f"'Sát Thát' tattooed on their forearms; a stern officer. Anh Tư is {FACE}, with 'Sát Thát' tattooed on "
                 "his forearm."),
        hook="POV: Bị lệnh phải thua / không ai nói vì sao",
        end="Thua một buổi sáng thì được gì? / Follow để xem Anh Tư / bị lệnh chạy thua cả ngày →",
        clips=[
            dict(name="Lệnh phải thua", label="Cửa sông Bạch Đằng · năm 1288",
                 img=f"First-person close-up of tattooed forearms digging a paddle into the water in a small light boat at dawn, {FACE} paddling in front and looking back, a stern officer in the next boat pointing at huge enemy sails on the horizon, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: tattooed forearms dig paddles into the water; the officer in the next boat shouts: \"Ra đánh vài nhát rồi chạy. Nhớ: phải thua!\" 5-10s: Anh Tư turns back to the viewer and grins: \"Thua thì em giỏi nhất đội!\"",
                 subs=[(0.5, 4.8, "Ra đánh vài nhát rồi chạy. / Nhớ: phải thua!"),
                       (5.0, 9.5, "Thua thì em giỏi nhất đội!")]),
            dict(name="Ném trúng", tiktok="bo", label="Triều lên",
                 img="First-person view from a small boat beside a huge Yuan warship, a burly bearded admiral at the rail with his tall plumed helmet knocked crooked by a spear, enemy soldiers shouting, a stern officer in a small boat glaring at a grinning tattooed fisherman, realistic, vertical 9:16.",
                 vid="0-5s: The small boats dart up to the warships; Anh Tư hurls a spear without aiming and knocks the Yuan admiral's tall plumed helmet clean off his head. 5-10s: The officer glares at him, furious: \"Ai bảo ném trúng?! Đã bảo là phải thua!\" Anh Tư shrinks: \"Em... em lỡ tay giỏi ạ.\"",
                 subs=[(5.0, 7.5, "Ai bảo ném trúng?! / Đã bảo là phải thua!"),
                       (7.5, 9.8, "Em... em lỡ tay giỏi ạ.")]),
            dict(name="Chạy thật", label="Ít phút sau",
                 img=f"First-person view paddling furiously in a small fleeing boat, looking back at a whole fleet of huge Yuan warships chasing with drums, arrows splashing around, {FACE} in front paddling in panic, realistic, vertical 9:16.",
                 vid="0-5s: The whole Yuan fleet is chasing; arrows splash all around as the small boats flee upstream. 5-10s: Anh Tư, paddling like crazy, shouts back over his shoulder: \"Diễn thua mà sao nó đuổi thật thế này anh ơi!\"",
                 subs=[(5.0, 9.5, "Diễn thua mà sao / nó đuổi thật thế này anh ơi!")]),
            dict(name="Nhận ra cọc", tiktok="bo", label="Giữa trưa · nước rút",
                 img=f"First-person view from a small boat hidden among mangroves, the river water dropping and rows of sharpened stakes rising out of it around huge enemy warships, {FACE} pointing at one stake excitedly, realistic, vertical 9:16.",
                 vid="0-5s: Hidden among the mangroves, the crew catches its breath; the water drops fast and rows of sharpened stakes rise out of the river around the enemy warships. 5-10s: Anh Tư points at one stake, delighted: \"Ơ! Cái cọc kia nhà em cắm hôm trước đây mà!\"",
                 subs=[(5.0, 9.5, "Ơ! Cái cọc kia / nhà em cắm hôm trước đây mà!")]),
            dict(name="Câu chốt", label="Ngay sau đó",
                 img=f"First-person view from a small boat charging out of the mangroves toward huge Yuan warships stuck and tilting on stakes, drums from both banks, {FACE} standing in the boat grinning at the camera, realistic, vertical 9:16.",
                 vid="0-5s: The giant warships grind onto the stakes, tilt and crack; drums roar from both banks and the small boats charge back out. 5-10s: Anh Tư stands up in the boat and turns to the camera: \"Thua một buổi, thắng cả cuộc chiến. Thua kiểu này, em xin thua cả đời!\"",
                 subs=[(5.0, 9.8, "Thua một buổi, / thắng cả cuộc chiến. / Thua kiểu này, em xin / thua cả đời!")]),
        ],
        caption=("Bị lệnh phải thua trận mà không ai nói vì sao, tưởng thua thật, hóa ra... 😎 Năm 1288, quân Trần giả "
                 "thua nhử thủy quân Nguyên vào bãi cọc sông Bạch Đằng. Bạn có \"lỡ tay giỏi\" như Anh Tư không? 👇"),
        tags="#bachdang #tranhungdao #1288",
    ),
    # ------------------------------------------------------------------ 1427
    dict(
        slug="chay-thua-chi-lang-1427", prefix="nbt4",
        title="Bị lệnh chạy thua cả ngày mà không ai nói vì sao, đến ải Chi Lăng mới hiểu (1427)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1427, viện binh nhà Minh do Liễu Thăng chỉ huy tiến vào từ Lạng Sơn. Theo kế của "
                 "Lê Lợi và Nguyễn Trãi, tướng Trần Lựu vừa đánh vừa lui, giả thua để nhử. Liễu Thăng đuổi gấp, tự dẫn "
                 "hơn trăm kỵ binh đi trước, lọt vào ải Chi Lăng nơi quân Lam Sơn mai phục, và bị giết. Các nguồn ghi "
                 "ngày khác nhau, nên tập phim chỉ ghi năm. **Hư cấu:** Anh Tư, các tình huống và mọi lời thoại."),
        setting=("Vietnam, Lam Sơn uprising, autumn 1427, the mountain road to the Chi Lăng pass in Lạng Sơn: steep "
                 "forested limestone cliffs, a narrow valley, rocky paths. Lam Sơn soldiers in plain brown and dark-blue "
                 "clothes with head wraps, spears and shields; a stern officer; Ming cavalry in red-and-black armor; a "
                 f"Ming general in ornate armor on a horse. Anh Tư is {FACE}, in a brown tunic and head wrap."),
        hook="POV: Bị lệnh chạy thua / cả ngày",
        end="Chạy cả ngày, giờ ai phải chạy? / Follow để xem Anh Tư / bị cấm đập muỗi cả đêm →",
        clips=[
            dict(name="Lệnh chạy chậm", label="Đường lên ải · năm 1427",
                 img=f"First-person close-up of muddy feet running on a rocky mountain path, {FACE} running beside the viewer with a spear, a stern officer ahead looking back, Ming banners appearing behind, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: muddy feet pound a rocky path; the officer ahead looks back and shouts: \"Chạy! Nhưng chạy chậm thôi, để nó đuổi kịp!\" 5-10s: Anh Tư, running beside the viewer, pants: \"Chạy thua mà còn phải canh tốc độ cho giặc à?!\"",
                 subs=[(0.5, 4.8, "Chạy! Nhưng chạy chậm thôi, / để nó đuổi kịp!"),
                       (5.0, 9.5, "Chạy thua mà còn phải / canh tốc độ cho giặc à?!")]),
            dict(name="Chạy nhanh quá", tiktok="bo", label="Giữa trưa",
                 img=f"First-person view on a mountain path, a stern officer grabbing {FACE} by the collar and pulling him back, Anh Tư jogging backwards and waving at Ming cavalry far behind, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư sprints far ahead; the officer grabs him by the collar and drags him back: \"Chạy nhanh thế nó mất dấu thì sao!\" 5-10s: Anh Tư turns, jogs backwards and waves both arms at the distant Ming riders: \"Bên này! Bên này cơ mà!\"",
                 subs=[(0.5, 4.8, "Chạy nhanh thế / nó mất dấu thì sao!"),
                       (5.0, 9.5, "Bên này! Bên này cơ mà!")]),
            dict(name="Bị giặc cười", label="Chiều",
                 img=f"First-person view looking back from a mountain path at a Ming general in ornate armor laughing on his horse, leading about a hundred cavalry, {FACE} beside the viewer red with anger, realistic, vertical 9:16.",
                 vid="0-5s: The viewer looks back: a Ming general in ornate armor rides ahead with about a hundred horsemen, laughing and pointing at them. Anh Tư, red with anger: \"Nó cười mình kìa anh!\" 5-10s: The officer answers without turning: \"Để nó cười. Cười nốt hôm nay.\"",
                 subs=[(0.5, 4.8, "Nó cười mình kìa anh!"),
                       (5.0, 9.5, "Để nó cười. Cười nốt hôm nay.")]),
            dict(name="Núi im lặng", tiktok="bo", label="Ải Chi Lăng",
                 img=f"First-person view running into a narrow pass between steep forested limestone cliffs, eerily silent, a spear tip glinting among the leaves above, {FACE} glancing up nervously, realistic, vertical 9:16.",
                 vid="0-5s: They run into a narrow pass between steep forested cliffs; suddenly it is completely silent. Anh Tư whispers: \"Sao núi im thế... chim cũng nín thở à?\" 5-10s: The viewer looks up and notices a spear tip glinting among the leaves, then another, then dozens.",
                 subs=[(0.5, 4.8, "Sao núi im thế... / chim cũng nín thở à?")]),
            dict(name="Câu chốt", label="Ngay sau đó",
                 img=f"First-person view in a narrow mountain pass, hundreds of Lam Sơn soldiers rising from hiding on both cliffsides with crossbows and banners, Ming cavalry trapped below, {FACE} turning around and cracking his knuckles with a grin, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; hundreds of hidden soldiers rise from both cliffsides with crossbows and banners; the Ming cavalry is trapped in the pass. The officer shouts: \"Hết giờ chạy. Quay lại!\" 5-10s: Anh Tư turns around, cracks his knuckles and grins at the camera: \"Chạy cả ngày rồi, giờ đến lượt nó! Giờ đổi vai: nó chạy, em đứng xem!\"",
                 subs=[(0.5, 4.8, "Hết giờ chạy. Quay lại!"),
                       (5.0, 9.8, "Chạy cả ngày rồi, / giờ đến lượt nó! Đổi vai: / nó chạy, em đứng xem!")]),
        ],
        caption=("Bị lệnh chạy thua cả ngày mà không ai nói vì sao, đến ải Chi Lăng mới hiểu 😤 Năm 1427, Trần Lựu "
                 "giả thua nhử Liễu Thăng vào ải Chi Lăng, nơi quân Lam Sơn mai phục sẵn. Bạn chịu bị giặc cười được "
                 "mấy tiếng? 👇"),
        tags="#chilang #leloi #lamson #1427",
    ),
    # ------------------------------------------------------------------ 1785
    dict(
        slug="cam-dap-muoi-rach-gam-1785", giong="Central Vietnamese (Bình Định) accent", prefix="nbt5",
        title="Bị cấm ho, cấm đập muỗi cả đêm mà không ai nói chờ gì, sáng ra mới hiểu (Rạch Gầm – Xoài Mút, 1785)",
        length=LEN_FULL,
        history=("**Lịch sử:** tháng 1 năm 1785, Nguyễn Huệ cho quân Tây Sơn mai phục trên khúc sông Tiền giữa rạch "
                 "Gầm và rạch Xoài Mút (Tiền Giang ngày nay). Khi thủy quân Xiêm lọt vào trận địa, quân Tây Sơn từ các "
                 "rạch và cù lao đổ ra đánh, thủy quân Xiêm gần như bị tiêu diệt. Các nguồn ghi ngày và quân số khác "
                 "nhau, nên tập phim không nêu con số. **Hư cấu:** Anh Tư, chuyện muỗi và mọi lời thoại."),
        setting=("Vietnam, Tây Sơn period, January 1785, the Tiền River in the Mekong Delta: wide brown river, narrow "
                 "creeks under nipa palms and mangroves, night mist, clouds of mosquitoes. Tây Sơn soldiers in brown "
                 "clothes with red head wraps, hiding motionless in small boats in the creeks; a stern officer; Siamese "
                 f"warships with tall sails on the main river. Anh Tư is {FACE}, in a brown shirt and red head wrap."),
        hook="POV: Cả đêm bị cấm ho / cấm đập muỗi",
        end="Sáng ấy, ai mới phải chạy? / Follow để xem đời sau nhà Anh Tư →",
        clips=[
            dict(name="Lệnh cấm", label="Sông Tiền · tháng 1 năm 1785",
                 img=f"First-person close-up at night of a hand gripping a paddle in a small boat hidden under nipa palm leaves, a fat mosquito landing on the back of the hand, {FACE} crouched beside staring at it in agony, realistic, vertical 9:16.",
                 vid="0-5s: Close-up at night: a hand grips a paddle under the nipa palms; an officer crawls past whispering: \"Cấm nói, cấm ho, cấm đập muỗi!\" A fat mosquito lands on the hand. 5-10s: Anh Tư whispers, horrified: \"Cấm đập muỗi... thế muỗi có bị cấm cắn không anh?\"",
                 subs=[(0.5, 4.8, "Cấm nói, cấm ho, cấm đập muỗi!"),
                       (5.0, 9.5, "Cấm đập muỗi... / thế muỗi có bị cấm cắn không anh?")]),
            dict(name="Cái hắt hơi", tiktok="0-5", label="Nửa đêm",
                 img=f"First-person view in a dark creek under nipa palms, {FACE} about to sneeze with his head tilted back, three soldiers lunging to pinch his nose and cover his mouth at the same time, realistic, vertical 9:16.",
                 vid="0-5s: Midnight; Anh Tư's face scrunches up, his head tilts back, he is about to sneeze; three soldiers lunge at once to pinch his nose and clamp his mouth. 5-10s: The sneeze dies with a tiny squeak; everyone freezes, listening; the officer slowly lets out his breath and glares at Anh Tư.",
                 subs=[]),
            dict(name="Thuyền giặc đi ngang", label="Rạng sáng",
                 img="First-person view peeking out from a hidden creek at dawn, a long line of Siamese warships with tall sails gliding past very close in the mist, a stern officer in the foreground with a mosquito sitting on his nose, not blinking, realistic, vertical 9:16.",
                 vid="0-5s: A line of Siamese warships glides past the creek mouth, so close the viewer can hear sailors chatting on deck. 5-10s: A mosquito lands right on the officer's nose; he doesn't blink. Anh Tư, beside the viewer, shakes with silent laughter, tears in his eyes, hands over his mouth.",
                 subs=[]),
            dict(name="Mặt sưng", tiktok="5-10", label="Cùng lúc",
                 img=f"First-person view in a small hidden boat, soldiers with faces swollen from mosquito bites gripping their weapons, {FACE} with one eye swollen shut grinning, Siamese sails visible through the leaves, realistic, vertical 9:16.",
                 vid="0-5s: The viewer looks around the boat: every face is swollen from mosquito bites; Anh Tư's left eye is completely swollen shut. 5-10s: Anh Tư whispers, still grinning: \"Giặc chưa đánh mình, muỗi đã đánh mình tan tác rồi.\"",
                 subs=[(5.0, 9.5, "Giặc chưa đánh mình, / muỗi đã đánh mình tan tác rồi.")]),
            dict(name="Câu chốt", label="Ngay sau đó",
                 img=f"First-person view from a small boat bursting out of a creek onto a wide river at dawn, dozens of Tây Sơn boats charging from creeks and islets on both sides, drums, the Siamese fleet trapped in the middle, {FACE} slapping a mosquito on his arm with a huge grin, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; boats burst out of every creek and islet at once, trapping the Siamese fleet in the middle of the river. 5-10s: Paddling hard, Anh Tư finally slaps the mosquito on his arm with a loud smack and shouts at the camera: \"Giờ thì đập được rồi! Đập muỗi xong... đập luôn giặc!\"",
                 subs=[(5.0, 9.8, "Giờ thì đập được rồi! / Đập muỗi xong... / đập luôn giặc!")]),
        ],
        caption=("Bị cấm ho, cấm đập muỗi cả đêm mà không ai nói chờ gì, sáng ra mới hiểu 🦟 Tháng 1 năm 1785, quân "
                 "Tây Sơn của Nguyễn Huệ mai phục ở khúc sông Tiền giữa Rạch Gầm và Xoài Mút, đánh tan thủy quân Xiêm. "
                 "Bạn nhịn được mấy con muỗi? 👇"),
        tags="#rachgamxoaimut #nguyenhue #tayson #1785",
    ),
    # ------------------------------------------------------------------ 1427 Đông Quan
    dict(
        slug="dong-thuyen-cho-giac-1427", prefix="nbt6",
        title="Bị bắt đóng năm trăm chiếc thuyền mà không ai nói để làm gì, đến bến sông mới hiểu (Hội thề Đông Quan, 1427)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** cuối năm 1427, sau các thắng lợi ở Chi Lăng, Xương Giang, Vương Thông xin hòa. Hai bên làm "
                 "lễ **Hội thề Đông Quan** (các nguồn ghi ngày khác nhau, khoảng tháng 11 đến tháng 12 năm 1427). Lê Lợi "
                 "và Nguyễn Trãi cho quân Minh rút về nước an toàn, cấp thuyền, ngựa và lương thực. Hơn 10 vạn quân Minh "
                 "rút hết. *Bình Ngô đại cáo* của Nguyễn Trãi, viết ngay sau sự kiện, chép: \"Mã Kỳ, Phương Chính, cấp "
                 "cho năm trăm chiếc thuyền, ra đến biển mà vẫn hồn bay phách lạc; Vương Thông, Mã Anh, phát cho vài nghìn "
                 "cỗ ngựa, về đến nước mà vẫn tim đập chân run.\" Con số \"năm trăm\" là của áng văn, có thể mang tính "
                 "văn chương. **Hư cấu:** Anh Tư, viên quan đốc thợ, người lính Minh và mọi lời thoại."),
        setting=("Vietnam, Lê dynasty founding, late 1427, the bank of the Red River near Đông Quan (Thăng Long): a huge "
                 "riverside boatyard with hundreds of wooden boats under construction, piles of planks, the smell of fresh "
                 "wood and tar; later a long line of tired, disarmed Ming soldiers in faded red-and-black uniforms walking "
                 "calmly down to the river, treated with dignity, no chains, no violence. Lam Sơn soldiers and villagers in "
                 "plain brown and dark-blue clothes with head wraps; a stern officer overseeing the work. Anh Tư is "
                 f"{FACE}, in a brown tunic and head wrap, covered in sawdust."),
        hook="POV: Đóng 500 thuyền / không ai nói làm gì",
        end="Thuyền ra đến biển rồi sao? / Follow để xem đời sau nhà Anh Tư →",
        clips=[
            dict(name="Năm trăm chiếc", label="Bến sông Đông Quan / cuối năm 1427",
                 img=f"First-person close-up of hands hammering a wooden peg into a boat plank in a huge riverside boatyard, sawdust flying, hundreds of boats under construction behind, {FACE} beside the viewer covered in sawdust, a stern officer pointing, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: hands hammer a wooden peg into a boat plank, sawdust flying; the officer walks past shouting: \"Đóng cho nhanh! Năm trăm chiếc!\" 5-10s: Anh Tư, covered in sawdust, stops hammering: \"Năm trăm chiếc? Mình đi đánh ở đâu mà xa thế anh?\"",
                 subs=[(0.5, 4.8, "Đóng cho nhanh! / Năm trăm chiếc!"),
                       (5.0, 9.5, "Năm trăm chiếc? / Mình đi đánh ở đâu mà xa thế anh?")]),
            dict(name="Cơm cho khách", tiktok="bo", label="Mấy hôm sau",
                 img=f"First-person view at a riverside camp, villagers packing huge baskets of rice balls and dried fish onto a growing mountain of supplies, {FACE} holding a basket and frowning, the stern officer nearby, realistic, vertical 9:16.",
                 vid="0-5s: Villagers pack rice balls and dried fish into a mountain of baskets; Anh Tư holds one up: \"Gói cơm đủ ăn cả tháng... cho ai mà nhiều thế này?\" 5-10s: The officer answers without looking up: \"Cho khách.\" Anh Tư stares at the mountain of baskets: \"Khách nhà ai mà đông thế...\"",
                 subs=[(0.5, 4.8, "Gói cơm đủ ăn cả tháng... / cho ai mà nhiều thế này?"),
                       (5.0, 7.0, "Cho khách."),
                       (7.0, 9.5, "Khách nhà ai mà đông thế...")]),
            dict(name="Khách là ai", label="Bến sông · ngày giao thuyền",
                 img=f"First-person view at a riverbank, a long line of tired, disarmed Ming soldiers in faded red-and-black uniforms walking calmly down to rows of new wooden boats, {FACE} frozen with a hammer in hand and his jaw dropped, no violence, realistic, vertical 9:16.",
                 vid="0-5s: A long line of tired, disarmed Ming soldiers walks calmly down to the rows of new boats; Anh Tư freezes, hammer in hand: \"Ơ... khách là... giặc à?\" 5-10s: He turns to the viewer, completely lost: \"Đánh nhau mười năm, giờ mình đóng thuyền tiễn nó về?\"",
                 subs=[(0.5, 4.8, "Ơ... khách là... giặc à?"),
                       (5.0, 9.8, "Đánh nhau mười năm, / giờ mình đóng thuyền / tiễn nó về?")]),
            dict(name="Tiễn về thì yên lâu", tiktok="bo", label="Ngay sau đó",
                 img=f"First-person view at a riverbank, {FACE} handing a basket of rice to a tired Ming soldier who bows in thanks, the stern officer standing beside them watching calmly, boats waiting, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư grudgingly hands a basket of rice to a tired Ming soldier, who bows deeply; Anh Tư mutters: \"Ăn cho no rồi đi luôn nhé, đừng quay lại!\" The soldier nods hard. 5-10s: The officer, watching, says quietly to Anh Tư: \"Giết thêm thì hận thêm. Tiễn về thì yên lâu.\" Anh Tư slowly nods.",
                 subs=[(0.5, 4.8, "Ăn cho no rồi đi luôn nhé, / đừng quay lại!"),
                       (5.0, 9.5, "Giết thêm thì hận thêm. / Tiễn về thì yên lâu.")]),
            dict(name="Ghi tên em vào sử", label="Rạng sáng · thuyền rời bến",
                 img=f"First-person view at dawn from a riverbank, hundreds of wooden boats sailing away down the wide misty Red River carrying soldiers home, {FACE} standing on the bank with arms crossed and a proud chipped-tooth grin, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; hundreds of boats glide away down the misty river. A calm narrator's voice says: \"Bình Ngô đại cáo chép: cấp cho năm trăm chiếc thuyền, ra đến biển mà vẫn hồn bay phách lạc.\" 5-10s: Anh Tư, arms crossed on the bank, turns to the camera with his chipped-tooth grin: \"Thuyền em đóng có trong Bình Ngô đại cáo đấy! Ghi tên em vào sử nhé!\"",
                 subs=[(0.3, 4.8, "Bình Ngô đại cáo chép: / cấp cho năm trăm / chiếc thuyền, ra đến biển / mà vẫn hồn bay phách lạc."),
                       (5.0, 9.8, "Thuyền em đóng / có trong Bình Ngô đại cáo! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Bị bắt đóng năm trăm chiếc thuyền mà không ai nói để làm gì, đến bến sông mới hiểu 😳 Cuối năm 1427, "
                 "sau Hội thề Đông Quan, Lê Lợi và Nguyễn Trãi cấp thuyền, ngựa, lương thực cho quân Minh về nước. Bình "
                 "Ngô đại cáo còn chép lại. Bạn có biết câu nào trong Bình Ngô đại cáo không? Viết dưới bình luận 👇"),
        tags="#hoithedongquan #binhngodaicao #leloi #nguyentrai #1427",
    ),
    # ------------------------------------------------------------------ khoảng 1797, Tây Sơn thuê cướp biển
    dict(
        slug="dong-doi-moi-tay-son-1797", prefix="nbt7",
        title="Được giao tiếp đón đồng đội mới, ai cũng xăm kín tay và không ai nói nghề cũ (thủy quân Tây Sơn, khoảng 1797)",
        length=LEN_FULL_45,
        history=("**Lịch sử:** từ những năm 1780, và nhiều nhất dưới thời vua **Cảnh Thịnh** (con Quang Trung, trị vì "
                 "1792–1802), nhà Tây Sơn thu nạp các nhóm cướp biển người Hoa ở Quảng Đông (sử Việt gọi là giặc Tàu Ô) "
                 "vào thủy quân, cấp thuyền, căn cứ và chức tước để đánh nhau với Nguyễn Ánh trên biển. Thủ lĩnh **Mạc "
                 "Quan Phù** được phong \"Đông Hải vương\", **Trịnh Thất** làm đô đốc. Sau khi Tây Sơn mất (1802), số "
                 "còn lại về Quảng Đông. Năm 1805 **Trịnh Nhất** lập liên minh sáu hạm đội theo màu cờ (Đỏ, Đen, Trắng, "
                 "Lục, Lam, Vàng). Sau khi ông mất năm 1807, vợ ông là **Trịnh Nhất Tẩu** chỉ huy, có lúc vài vạn người, "
                 "đến năm 1810 thì đầu hàng nhà Thanh. Nguồn: Dian Murray, *Pirates of the South China Coast, 1790–1810* "
                 "(1987), dựa trên hồ sơ triều Thanh, cùng sử nhà Nguyễn. Năm phong tước các nguồn ghi khác nhau, nên tập "
                 "phim chỉ ghi \"khoảng\". **Hư cấu:** Anh Tư, viên quan, người thủy thủ Quảng Đông và mọi lời thoại."),
        setting=("Vietnam, Tây Sơn dynasty, around 1797, a Tây Sơn naval harbor on the northern coast: big wooden "
                 "warships with eyes painted on the bow, ropes, oars, sea wind. Tây Sơn sailors with black-lacquered "
                 "teeth in brown and dark-indigo clothes with red headbands, barefoot; an officer in a dark-red "
                 "uniform. Newly arrived Cantonese seafarers of the 1790s with Qing-style shaved foreheads and long "
                 "braids, loose dark clothes, arms covered in tattoos, friendly and relaxed, speaking Cantonese. "
                 f"Anh Tư is {FACE}, in a brown shirt with a red headband. No fighting, no weapons being used."),
        hook="POV: Đồng đội mới / ai cũng xăm kín tay",
        end="Follow để xem đời sau / nhà Anh Tư bị giao việc gì →",
        clips=[
            dict(name="Đồng đội mới", label="Bến thủy quân Tây Sơn · khoảng 1797",
                 img=f"First-person close-up on a wooden harbor deck, the viewer's hands coiling a thick rope, {FACE} beside the viewer staring at a group of tattooed Cantonese seafarers with long braids stepping off a junk onto the pier, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer coils rope on the pier; Anh Tư watches a group of tattooed seafarers with long braids step off a junk, waving cheerfully, and whispers: \"Đồng đội mới... sao ai cũng xăm kín tay thế anh?\" 5-10s: The officer walks past without stopping: \"Tiếp cho tử tế. Đừng hỏi nghề cũ.\" Anh Tư slowly closes his mouth.",
                 subs=[(0.5, 4.8, "Đồng đội mới... / sao ai cũng xăm kín tay thế anh?"),
                       (5.0, 9.5, "Tiếp cho tử tế. / Đừng hỏi nghề cũ.")]),
            dict(name="Nghề cũ", label="Buổi trưa",
                 img=f"First-person view on a ship deck at noon, {FACE} sitting cross-legged sharing a bowl of rice with a grinning tattooed Cantonese seafarer with a long braid, both relaxed, realistic, vertical 9:16.",
                 vid="0-5s: Over a shared bowl of rice, Anh Tư asks the tattooed seafarer, miming with his hands: \"Trước anh làm nghề gì?\" The seafarer grins and mimes, with a friendly wink, grabbing a big ship and pulling it toward himself. 5-10s: Anh Tư nods slowly and says to the viewer, deadpan: \"...À. Ngành vận tải. Nhận hàng không cần hỏi chủ.\"",
                 subs=[(0.5, 4.8, "Trước anh làm nghề gì?"),
                       (5.0, 9.5, "...À. Ngành vận tải. / Nhận hàng không cần hỏi chủ.")]),
            dict(name="Sếp được phong vương", label="Lễ phong tước",
                 img=f"First-person view on a harbor at a solemn ceremony, a Tây Sơn official in red robes reading from a long scroll, a tattooed Cantonese captain with a long braid kneeling to receive a seal, {FACE} in the crowd of sailors with his jaw dropped, realistic, vertical 9:16.",
                 vid="0-5s: A Tây Sơn official reads loudly from a scroll: \"...phong làm Đông Hải vương!\" The tattooed captain kneels and receives a seal. 5-10s: Anh Tư turns to the viewer, whispering, completely lost: \"Sếp mới được phong vương... mà CV nghề cũ ghi là... cướp biển?\"",
                 subs=[(0.5, 4.8, "...phong làm Đông Hải vương!"),
                       (5.0, 9.8, "Sếp mới được phong vương... / mà CV nghề cũ / ghi là... cướp biển?")]),
            dict(name="Cờ màu", tiktok="0-5", label="Mấy hôm sau",
                 img=f"First-person view of a harbor, the Cantonese seafarers hoisting flags of different colors, red, black, white, on different junks, {FACE} holding a flag and looking confused, realistic, vertical 9:16.",
                 vid="0-5s: The seafarers hoist a different-colored flag on each junk: red, black, white. Anh Tư holds a black flag and asks: \"Cùng một quân, sao mỗi thuyền một màu cờ?\" 5-10s: The tattooed seafarer answers in broken Vietnamese, grinning: \"Đỏ, đen, trắng... dễ nhận nhà!\" Anh Tư nods to the viewer: \"Như áo đội bóng. Hiểu rồi.\"",
                 subs=[(0.5, 4.8, "Cùng một quân, / sao mỗi thuyền một màu cờ?"),
                       (5.0, 7.3, "Đỏ, đen, trắng... dễ nhận nhà!"),
                       (7.3, 9.6, "Như áo đội bóng. Hiểu rồi.")]),
            dict(name="Câu chốt", label="Nhiều năm sau",
                 img=f"First-person view at sunset from a hilltop over the open sea, a huge fleet of junks with red, black and white sails heading north toward the horizon, {FACE} standing beside the viewer with arms crossed, his chipped-tooth grin slowly fading, realistic, vertical 9:16.",
                 vid="0-5s: Sunset; a huge fleet of junks with colored flags sails north toward the horizon. A calm narrator's voice says: \"Năm 1802 Tây Sơn mất. Họ về Quảng Đông, lập sáu hạm đội cờ màu, vài vạn người.\" 5-10s: Anh Tư grins proudly at the camera: \"Em dạy họ đi đội hình đấy!\" Then his grin fades and he adds quickly: \"...Mà thôi, đừng ai biết là em.\"",
                 subs=[(0.3, 4.8, "Năm 1802 Tây Sơn mất. / Họ về Quảng Đông, / lập sáu hạm đội cờ màu."),
                       (5.0, 8.0, "Em dạy họ đi đội hình đấy!"),
                       (8.0, 9.8, "...Mà thôi, đừng ai biết là em.")]),
        ],
        caption=("Được giao tiếp đón đồng đội mới, ai cũng xăm kín tay, không ai nói nghề cũ 😳 Cuối thế kỷ 18, nhà Tây "
                 "Sơn từng thu nạp cướp biển Quảng Đông vào thủy quân, có người được phong \"Đông Hải vương\". Sau năm "
                 "1802 họ về nước, lập liên minh cướp biển cờ màu lớn nhất Biển Đông, có cả Hạm đội Cờ Đen, sau do một "
                 "người phụ nữ cầm đầu (theo nghiên cứu của Dian Murray). Bạn có biết người phụ nữ đó là ai không? Viết "
                 "dưới bình luận 👇"),
        tags="#taysoncanhthinh #cuopbientauo #trinhnhattau #hamdoicoden #thuyquantayson",
        tt_title="Đồng đội mới của thủy quân Tây Sơn: ai cũng xăm kín tay, không ai nói nghề cũ",
        hooks_alt=["POV: Sếp mới được phong vương / nghề cũ là cướp biển", "POV: Thủy quân Tây Sơn / tuyển thêm... cướp biển?"],
        pin=("Gợi ý: bà ấy được gọi là \"nữ hoàng cướp biển\" Biển Đông 🏴‍☠️ Ai đoán đúng tên, mình ghim bình luận "
             "lên đầu! Follow để xem đời sau nhà Anh Tư nhé!"),
        yt_title="Thủy quân Tây Sơn từng tuyển… cướp biển? POV Anh Tư",
        yt_tags=("tây sơn, cướp biển tàu ô, cảnh thịnh, quang trung, trịnh nhất tẩu, ching shih, hạm đội cờ đen, "
                 "thủy quân tây sơn, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1771 khởi nghĩa Tây Sơn
    dict(
        slug="chia-gao-tay-son-1771", giong="Central Vietnamese (Bình Định) accent", prefix="nbt8",
        title="Được chia gạo nhà giàu không mất một đồng, mấy năm sau mới biết người chia gạo là ai (khởi nghĩa Tây Sơn, 1771)",
        length=LEN_FULL,
        history=("**Lịch sử:** năm 1771, ba anh em Nguyễn Nhạc, Nguyễn Huệ, Nguyễn Lữ dấy binh ở ấp Tây Sơn (Bình Định), "
                 "chống quyền thần Trương Phúc Loan ở Đàng Trong. Họ lấy của nhà giàu chia cho dân nghèo nên được dân "
                 "theo đông; năm 1773 chiếm thành Quy Nhơn. Nguyễn Nhạc từng làm biện lại, tức chức thu thuế. Nguyễn Huệ "
                 "(sinh 1753, năm ấy khoảng 18 tuổi) cuối năm 1788 lên ngôi, hiệu **Quang Trung**, Tết Kỷ Dậu 1789 đánh "
                 "tan quân Thanh, vào Thăng Long. Sử nhà Nguyễn gọi Tây Sơn là \"giặc\", sử hiện đại gọi là khởi nghĩa; "
                 "tập phim theo cách gọi của sử hiện đại. Tả Nguyễn Huệ tóc quăn, mắt sáng, tiếng như chuông là theo "
                 "ghi chép đời sau, không chắc chắn. **Hư cấu:** Anh Tư, các tình huống và mọi lời thoại, kể cả lời của "
                 "Nguyễn Huệ và Nguyễn Nhạc trong phim."),
        setting=("Vietnam, Đàng Trong under the Nguyễn lords, 1771, the upland village of Tây Sơn in Bình Định: bamboo "
                 "hedges, dusty road, the big wooden granary of a rich landlord with its doors flung open, rice sacks "
                 "being carried out. Adult villagers only, in brown clothes and conical hats, black-lacquered teeth, "
                 "barefoot. The rebels wear plain dark-indigo clothes with red headbands. "
                 f"Anh Tư is {FACE}, a poor farmer in a patched brown shirt."),
        hook="POV: Có người chia gạo / không lấy một đồng",
        end="Follow để xem đời sau / nhà Anh Tư bị giao việc gì →",
        clips=[
            dict(name="Gạo không lấy tiền", label="Ấp Tây Sơn · năm 1771",
                 img=f"First-person view in a queue of adult villagers in front of a rich landlord's granary with its doors open, rebels in red headbands handing out rice, {FACE} in front of the viewer holding an empty sack and frowning suspiciously, realistic, vertical 9:16.",
                 vid=f"0-5s: In the queue, Anh Tư watches rebels in red headbands pour rice into villagers' sacks for free and whispers to the viewer: \"Gạo chia không lấy tiền... nghe đã thấy có chuyện.\" 5-10s: He reaches the front; {HUE} fills his sack and says clearly: \"Của nhà giàu. Trả lại cho dân.\" Anh Tư blinks.",
                 subs=[(0.5, 4.8, "Gạo chia không lấy tiền... / nghe đã thấy có chuyện."),
                       (5.0, 9.5, "Của nhà giàu. / Trả lại cho dân.")]),
            dict(name="Ông thu thuế", tiktok="0-5", label="Cùng buổi",
                 img=f"First-person view beside a rice-distribution table, a stout cheerful man in his thirties with a tally ledger at his belt counting sacks, {FACE} staring at him wide-eyed, realistic, vertical 9:16.",
                 vid="0-5s: A stout cheerful man with a ledger counts sacks; an old villager nudges Anh Tư: \"Ông anh cả đấy. Trước làm thu thuế.\" 5-10s: Anh Tư turns to the viewer, deeply confused: \"Người thu thuế... đi chia gạo? Ngược đời thật.\"",
                 subs=[(0.5, 4.8, "Ông anh cả đấy. / Trước làm thu thuế."),
                       (5.0, 9.5, "Người thu thuế... đi chia gạo? / Ngược đời thật.")]),
            dict(name="Đôi mắt", label="Lúc ra về",
                 img=f"First-person view on a dusty village road, {HUE} looking straight into the camera with an intense calm gaze, {FACE} next to the viewer clutching his rice sack nervously, realistic, vertical 9:16.",
                 vid=f"0-5s: As Anh Tư walks away with his sack, the young man with piercing eyes looks straight at him for a long silent moment. Anh Tư freezes. 5-10s: Anh Tư whispers to the viewer, sweating: \"Ông ấy nhìn em một cái... em suýt trả lại cả bao gạo.\"",
                 subs=[(5.0, 9.5, "Ông ấy nhìn em một cái... / em suýt trả lại cả bao gạo.")]),
            dict(name="Xin theo", tiktok="0-5", label="Mấy hôm sau",
                 img=f"First-person view in a rebel camp among bamboo, {FACE} standing eagerly in front of {HUE}, who looks him up and down, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư bows eagerly: \"Cho em theo với!\" The young man asks: \"Biết làm gì?\" Anh Tư thinks hard: \"Em... ăn khỏe ạ.\" 5-10s: The young man nods once: \"Được. Đi gánh gạo.\" Anh Tư grins and lifts two heavy baskets on a carrying pole.",
                 subs=[(0.5, 2.6, "Cho em theo với!"),
                       (2.6, 4.8, "Biết làm gì? / ...Em ăn khỏe ạ."),
                       (5.0, 9.5, "Được. Đi gánh gạo.")]),
            dict(name="Câu chốt", label="Thăng Long · Xuân 1789",
                 img=f"First-person view from a festive crowd on a Thăng Long street in spring 1789, a royal procession with yellow banners passing, a commander on horseback at a distance with curly hair and piercing eyes, {FACE} in the crowd, older now, pointing excitedly, realistic, vertical 9:16.",
                 vid="0-5s: Spring; a festive crowd lines a Thăng Long street as a royal procession with yellow banners passes, the commander on horseback seen at a distance. A calm narrator's voice says: \"Người chia gạo năm ấy là Nguyễn Huệ. Cuối năm 1788 lên ngôi, hiệu Quang Trung.\" 5-10s: Anh Tư, older, turns to the camera with his chipped-tooth grin: \"Ông ấy chia gạo cho em đấy! Bao gạo ấy... em chưa nỡ ăn.\"",
                 subs=[(0.3, 4.8, "Người chia gạo năm ấy / là Nguyễn Huệ. / Cuối năm 1788 lên ngôi, / hiệu Quang Trung."),
                       (5.0, 9.8, "Ông ấy chia gạo cho em đấy! / Bao gạo ấy... em chưa nỡ ăn.")]),
        ],
        caption=("Được chia gạo nhà giàu không mất một đồng, mấy năm sau mới biết người chia gạo là ai 😳 Năm 1771, ba anh "
                 "em nhà Tây Sơn dấy binh, lấy của nhà giàu chia cho dân nghèo (theo sử hiện đại gọi là khởi nghĩa Tây "
                 "Sơn). Người em thứ sau này là vua Quang Trung. Nếu được ông chia gạo, bạn sẽ xin theo không? Viết dưới "
                 "bình luận 👇"),
        tags="#khoinghiatayson #nguyenhue #quangtrung #nguyennhac #1771",
        tt_title="Được chia gạo nhà giàu không mất một đồng, mấy năm sau mới biết người chia là ai",
        hooks_alt=["POV: Người chia gạo cho bạn / có đôi mắt lạ lắm", "POV: Ông thu thuế / đi chia gạo miễn phí"],
        pin=("Năm 1771 người chia gạo ấy mới khoảng 18 tuổi 😳 Bạn có muốn xem Anh Tư gánh gạo theo Tây Sơn "
             "tiếp không? Follow để không lỡ nhé!"),
        yt_title="Được chia gạo nhà giàu miễn phí năm 1771… người chia gạo là ai? POV Anh Tư",
        yt_tags=("khởi nghĩa tây sơn, nguyễn huệ, quang trung, nguyễn nhạc, tây sơn 1771, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1786-1788 La Sơn Phu Tử
    dict(
        slug="dua-thu-la-son-1788", giong="Central Vietnamese (Nghệ An) accent", prefix="nbt9",
        title="Bị sai đưa thư mời một ông đồ trên núi, ba năm bị từ chối, đến khi ông nói một câu thì cả nước nhớ (La Sơn Phu Tử, 1786–1788)",
        length=LEN_FULL,
        history=("**Lịch sử:** Nguyễn Thiếp (1723–1804), hiệu La Sơn Phu Tử, bỏ quan về ở ẩn ở Nghệ An. Từ năm 1786, "
                 "Nguyễn Huệ nhiều lần gửi thư mời ông ra giúp nước; ông từ chối. Tháng 4 năm 1788, ông xuống núi gặp "
                 "Nguyễn Huệ ở Lam Thành nhưng vẫn chưa nhận lời (thư từ hai bên còn giữ được, Hoàng Xuân Hãn tập hợp "
                 "trong sách *La Sơn Phu Tử*). Cuối năm 1788, trên đường ra Bắc đánh quân Thanh, vua Quang Trung ghé "
                 "hỏi kế; theo *Hoàng Lê nhất thống chí* (tiểu thuyết lịch sử, mức C), ông nói quân Thanh ở xa đến, "
                 "không biết tình thế, \"không quá mười ngày\" sẽ bị phá. Mùng 5 Tết Kỷ Dậu (1789), vua vào Thăng Long. "
                 "Về sau ông đứng đầu Sùng chính viện, dịch sách sang chữ Nôm. **Hư cấu:** Anh Tư, việc đưa thư đúng "
                 "\"ba lần\" và mọi lời thoại."),
        setting=("Vietnam, 1786 to 1788, the forested Thiên Nhẫn mountains of Nghệ An: a steep stone path, bamboo groves, "
                 "a small thatched hermit house with a wooden desk and stacks of books, a stream. The hermit scholar "
                 "Nguyễn Thiếp is an elderly Vietnamese man in his sixties with a long thin white beard, a plain brown "
                 "scholar's robe and a calm, dry sense of humor. Tây Sơn soldiers in dark-red uniforms with red head "
                 f"wraps. Anh Tư is {FACE}, a Tây Sơn messenger with a cloth letter pouch."),
        hook="POV: Đưa thư mời / một ông đồ / ba năm bị từ chối",
        end="Follow để xem Anh Tư / theo hầu ông vua... giả →",
        clips=[
            dict(name="Thư lần thứ nhất", label="Núi Thiên Nhẫn, Nghệ An · năm 1786",
                 img=f"First-person view at the door of a small thatched hermit house on a forested mountain, the elderly white-bearded scholar holding an opened letter, {FACE} standing beside the viewer, sweaty from the climb, holding out a letter pouch, realistic, vertical 9:16.",
                 vid="0-5s: The elderly scholar reads the letter, folds it calmly and hands it back: \"Về thưa với tướng quân: già này chỉ biết dạy học.\" 5-10s: Anh Tư holds the returned letter, confused, and asks: \"Dạ... thế thư này em mang về, hay cụ giữ làm kỷ niệm?\" The scholar closes the door gently.",
                 subs=[(0.5, 4.8, "Về thưa với tướng quân: / già này chỉ biết dạy học."),
                       (5.0, 9.5, "Dạ... thế thư này em mang về, / hay cụ giữ làm kỷ niệm?")]),
            dict(name="Thư lần thứ hai", tiktok="0-5", label="Một năm sau",
                 img=f"First-person view on a steep stone mountain path, the elderly scholar standing at the top near his hut pointing down at the viewer, {FACE} below, panting, holding up a letter, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư climbs the last steps, panting, holding up a new letter. Before he can speak, the scholar at the top calls down: \"Lại là cậu à? Không!\" 5-10s: Anh Tư, out of breath, to the viewer: \"Em còn chưa kịp nói câu nào mà!\"",
                 subs=[(0.5, 4.8, "Lại là cậu à? Không!"),
                       (5.0, 9.5, "Em còn chưa kịp / nói câu nào mà!")]),
            dict(name="Thư lần thứ ba", label="Đầu năm 1788",
                 img=f"First-person view inside a thatched hermit house, the elderly scholar sitting at a wooden desk reading a letter with a slight smile, {FACE} kneeling in front of him with three worn-out pairs of straw sandals tied to his pouch, realistic, vertical 9:16.",
                 vid="0-5s: The scholar reads the third letter slowly, then looks up with a faint smile: \"Được. Ta xuống núi... gặp một lần.\" 5-10s: Anh Tư jumps up and holds out three worn-out pairs of sandals to the viewer: \"Ba năm, mòn ba đôi dép, cụ mới chịu xuống núi một lần!\"",
                 subs=[(0.5, 4.8, "Được. Ta xuống núi... / gặp một lần."),
                       (5.0, 9.5, "Ba năm, mòn ba đôi dép, / cụ mới chịu xuống núi một lần!")]),
            dict(name="Xuống núi để từ chối", tiktok="5-10", label="Lam Thành · tháng 4 năm 1788",
                 img=f"First-person view in a Tây Sơn camp tent, the elderly scholar bowing politely to a Tây Sơn commander seen from behind in a dark-red robe, {FACE} standing at the side holding the scholar's walking stick, realistic, vertical 9:16.",
                 vid="0-5s: In the camp, the scholar bows politely to the commander, seen only from behind, and says calmly: \"Đa tạ tấm lòng. Nhưng già này xin về núi.\" 5-10s: Anh Tư, holding the walking stick, whispers to the viewer, devastated: \"Xuống núi... để từ chối trực tiếp ạ?\"",
                 subs=[(0.5, 4.8, "Đa tạ tấm lòng. / Nhưng già này xin về núi."),
                       (5.0, 9.5, "Xuống núi... / để từ chối trực tiếp ạ?")]),
            dict(name="Câu chốt", label="Nghệ An · cuối năm 1788",
                 img=f"First-person view at dusk outside the hermit house, a great Tây Sơn army with torches and red banners marching along the valley below, a royal figure in a dark robe seen from behind talking with the elderly scholar at the gate, {FACE} beside the viewer, proud, realistic, vertical 9:16.",
                 vid="0-5s: Dusk; a great army with torches marches through the valley; the king, seen only from behind, speaks with the scholar at the gate. A calm narrator's voice says: \"Cuối năm 1788, vua Quang Trung ra Bắc, ghé hỏi kế. Ông đồ nói: không quá mười ngày, quân Thanh sẽ tan.\" 5-10s: Anh Tư turns to the camera with his chipped-tooth grin: \"Ông đồ ấy em mời đấy! Ba đôi dép... đáng lắm!\"",
                 subs=[(0.3, 4.8, "Vua Quang Trung ghé hỏi kế. / Ông đồ nói: không quá / mười ngày, quân Thanh sẽ tan."),
                       (5.0, 9.8, "Ông đồ ấy em mời đấy! / Ba đôi dép... đáng lắm!")]),
        ],
        caption=("Bị sai đưa thư mời một ông đồ trên núi, ba năm bị từ chối 😅 Ông đồ ấy là La Sơn Phu Tử Nguyễn Thiếp. "
                 "Cuối năm 1788, vua Quang Trung ghé hỏi kế trước khi đánh quân Thanh, và câu trả lời của ông được sách "
                 "Hoàng Lê nhất thống chí chép lại. Bạn có biết câu ông nói không? Viết dưới bình luận 👇"),
        tags="#quangtrung #lasonphutu #nguyenthiep #tayson #1788",
        tt_title="Đưa thư mời một ông đồ suốt ba năm, bị từ chối cả ba lần",
        hooks_alt=["POV: Ba năm mòn ba đôi dép / chỉ để đưa một lá thư", "POV: Ông đồ trên núi / từ chối cả tướng quân"],
        pin=("Gợi ý: câu ông đồ nói có hai chữ \"mười ngày\" 😏 Ai đoán trúng cả câu, mình ghim lên đầu! "
             "Follow để xem Anh Tư theo hầu ông vua... giả!"),
        yt_title="Đưa thư mời La Sơn Phu Tử suốt ba năm: ông đồ nói gì với vua Quang Trung?",
        yt_tags=("quang trung, la sơn phu tử, nguyễn thiếp, nguyễn huệ, tây sơn, đánh quân thanh 1789, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1790 vua giả mừng thọ Càn Long
    dict(
        slug="theo-hau-vua-gia-1790", giong="Central Vietnamese (Nghệ An) accent", prefix="nbt10",
        title="Được cử theo hầu nhà vua sang mừng thọ hoàng đế nhà Thanh, đi nửa đường mới biết vua là… người đóng thế (năm 1790)",
        length=LEN_FULL,
        history=("**Lịch sử:** năm 1790, hoàng đế Càn Long nhà Thanh mừng thọ 80 tuổi. Sứ bộ Đại Việt với danh nghĩa "
                 "\"An Nam quốc vương Nguyễn Quang Bình\" (tức Quang Trung) sang dự, được tiếp đón rất trọng hậu ở hành "
                 "cung Nhiệt Hà; sử nhà Thanh chép Càn Long cho làm lễ \"bão kiến\" (ôm gối, như cha con), một ân điển "
                 "hiếm có. **Sử Việt** (theo nhiều sách đời sau, như của Hoa Bằng) chép người sang là **Phạm Công Trị**, "
                 "cháu gọi vua bằng cậu, đóng giả vua; vua Quang Trung ở lại trong nước. Đến nay giới sử học **vẫn còn "
                 "tranh luận** người sang là ai; tập phim để ngỏ, không kết luận. **Hư cấu:** Anh Tư, việc chọn người "
                 "\"theo khuôn mặt\", buổi tập đi đứng, các bữa tiệc và mọi lời thoại."),
        setting=("1790. First in Nghệ An, Vietnam: a Tây Sơn courtyard with red-lacquered pillars, officials in dark-red "
                 "court robes. Then in Qing China: busy roadside towns with lantern-lit banquets, and the grand Qing "
                 "summer palace at Rehe (Chengde) with golden roofs, Manchu officials with queues in Qing court robes. "
                 "The Đại Việt envoy playing the king is a dignified Vietnamese man around 35 with curly hair and bright "
                 "eyes, in a yellow-and-red Vietnamese royal robe and hat. The Qianlong Emperor is a dignified elderly "
                 "man around 80 in a yellow dragon robe. No visible writing on robes, banners or signboards; no modern "
                 f"flags; no European clothing. Anh Tư is {FACE}, an attendant in a neat dark-red uniform."),
        hook="POV: Theo hầu vua / sang nước Thanh / mà vua... hơi lạ",
        end="Follow để xem đời sau / nhà Anh Tư bị giao việc gì →",
        clips=[
            dict(name="Chọn người", label="Nghệ An · mùa xuân năm 1790",
                 img=f"First-person view in a Tây Sơn courtyard, a stern official pointing at one man in a line of men, a dignified man with curly hair and bright eyes stepping forward, {FACE} beside the viewer frowning in confusion, realistic, vertical 9:16.",
                 vid="0-5s: A stern official walks along a line of men and stops at the one with curly hair and bright eyes: \"Người này. Từ mai, ông ấy là vua.\" 5-10s: Anh Tư whispers to the viewer: \"Đi sứ mà chọn người theo... khuôn mặt ạ?\" The official, without turning: \"Theo hầu cho tử tế. Không hỏi.\"",
                 subs=[(0.5, 4.8, "Người này. / Từ mai, ông ấy là vua."),
                       (5.0, 7.6, "Đi sứ mà chọn người / theo... khuôn mặt ạ?"),
                       (7.6, 9.6, "Theo hầu cho tử tế. / Không hỏi.")]),
            dict(name="Tập làm vua", tiktok="5-10", label="Mấy hôm sau",
                 img=f"First-person view in a courtyard, the curly-haired envoy in a royal robe practicing a slow regal walk and tripping on the long hem, {FACE} beside him coaching with both hands raised, realistic, vertical 9:16.",
                 vid="0-5s: The envoy practices a slow regal walk, trips on the long hem of the royal robe and steadies himself. Anh Tư coaches: \"Bác đi chậm thôi, vua mình đi oai như hổ...\" 5-10s: The envoy tries again and stumbles again; Anh Tư sighs: \"...Thôi, bác cứ đứng yên là giống nhất.\"",
                 subs=[(0.5, 4.8, "Bác đi chậm thôi, / vua mình đi oai như hổ..."),
                       (5.0, 9.5, "...Thôi, bác cứ đứng yên / là giống nhất.")]),
            dict(name="Tiệc dọc đường", tiktok="5-10", label="Đường sang Nhiệt Hà · bốn tháng",
                 img=f"First-person view at a lavish lantern-lit banquet table in a Qing town, endless dishes, Qing officials toasting the envoy in a royal robe, {FACE} beside the viewer, his cheeks full, loosening his belt, realistic, vertical 9:16.",
                 vid="0-5s: Another lavish banquet; Qing officials raise cups to the envoy in the royal robe; servants keep bringing dishes. 5-10s: Anh Tư, cheeks full, loosens his belt and whispers: \"Đi bốn tháng, tỉnh nào cũng mở tiệc... em lên năm cân rồi.\"",
                 subs=[(5.0, 9.5, "Đi bốn tháng, tỉnh nào / cũng mở tiệc... / em lên năm cân rồi.")]),
            dict(name="Lễ ôm", label="Hành cung Nhiệt Hà · mùa thu năm 1790",
                 img=f"First-person view from the back of a grand golden-roofed Qing palace hall, the elderly Qianlong Emperor in a yellow dragon robe warmly embracing the kneeling curly-haired Vietnamese envoy in a royal robe, rows of Manchu officials watching, {FACE} beside the viewer frozen with wide eyes, realistic, vertical 9:16.",
                 vid="0-5s: In the grand hall, the elderly emperor rises and warmly embraces the kneeling envoy like a father; the officials murmur in surprise. 5-10s: Anh Tư, frozen, whispers to the viewer through clenched teeth: \"Hoàng đế ôm ông ấy như cha con... em chỉ mong ông ấy đừng hắt hơi.\"",
                 subs=[(0.5, 4.8, "Sử nhà Thanh chép: / hoàng đế làm lễ ôm, / như cha con."),
                       (5.0, 9.5, "Hoàng đế ôm ông ấy / như cha con... em chỉ mong / ông ấy đừng hắt hơi.")]),
            dict(name="Câu chốt", label="Chiều hôm ấy",
                 img=f"First-person view at dusk in the courtyard of the Qing palace, the curly-haired envoy in the royal robe walking away calmly, {FACE} turning toward the viewer with a sly chipped-tooth grin and a finger on his lips, realistic, vertical 9:16.",
                 vid="0-5s: Dusk; the envoy walks calmly away across the palace courtyard. A calm narrator's voice says: \"Sử Thanh chép: vua Quang Trung sang mừng thọ. Sử Việt chép: người sang là Phạm Công Trị, đóng thế. Đến nay vẫn còn tranh luận.\" 5-10s: Anh Tư turns to the camera, finger on his lips, grinning: \"Em biết ai thật ai giả... nhưng em không nói đâu. Các bác đoán đi!\"",
                 subs=[(0.3, 4.8, "Sử Thanh: Quang Trung sang. / Sử Việt: người sang là / Phạm Công Trị, đóng thế."),
                       (5.0, 9.8, "Em biết ai thật ai giả... / nhưng em không nói đâu. / Các bác đoán đi!")]),
        ],
        caption=("Được cử theo hầu nhà vua sang mừng thọ hoàng đế Càn Long năm 1790, đi nửa đường mới thấy vua… hơi lạ 🤫 "
                 "Sử nhà Thanh chép vua Quang Trung sang tận nơi, còn sử Việt chép người sang là Phạm Công Trị đóng thế. "
                 "Đến nay vẫn còn tranh luận. Theo bạn, ai đã gặp Càn Long? Viết dưới bình luận 👇"),
        tags="#quangtrung #phamcongtri #canlong #tayson #1790",
        tt_title="Theo hầu nhà vua sang mừng thọ Càn Long, đi nửa đường mới thấy vua... hơi lạ",
        hooks_alt=["POV: Đi sứ mà được chọn / theo khuôn mặt", "POV: Hoàng đế nhà Thanh ôm vua mình / mà em run"],
        pin=("Bình chọn nhanh: người gặp Càn Long năm 1790 là ai? Thả ❤️ nếu bạn nghĩ là vua Quang Trung, "
             "bình luận \"Trị\" nếu bạn tin là Phạm Công Trị 👇 Follow để xem đời sau nhà Anh Tư!"),
        yt_title="Năm 1790, ai đã sang gặp hoàng đế Càn Long: vua Quang Trung hay người đóng thế?",
        yt_tags=("quang trung, phạm công trị, vua quang trung giả, càn long, mừng thọ càn long 1790, tây sơn, "
                 "nhà thanh, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1785 Rạch Gầm (tiền truyện tập 5)
    dict(
        slug="dan-duong-rach-gam-1785", prefix="nbt11",
        # Bản cuối đã quay nằm ở tap-11-dan-duong-rach-gam-1785.md (anh sửa trang phục, thuyền, cờ quân Xiêm 1785
        # và tách rõ hai người ở clip 2). File đó là nguồn đúng; ở đây chỉ còn dùng để sinh plan.txt.
        md_frozen=True,
        title="Được thuê dẫn đường cho đoàn thuyền giặc, dẫn đến khúc sông yên tĩnh nhất thì... (Rạch Gầm – Xoài Mút, 1785)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1784, theo lời cầu viện của Nguyễn Ánh, vua Xiêm sai quân thủy bộ sang đánh Gia Định, "
                 "chiếm nhiều nơi ở miền Tây; sử chép quân Xiêm cướp phá khiến dân oán. Nguyễn Huệ từ Quy Nhơn vào, chọn "
                 "khúc sông Tiền từ Rạch Gầm đến Xoài Mút (Tiền Giang ngày nay), giấu quân trên bờ, trên cù lao và trong "
                 "các rạch. Ngày 20 tháng Chạp năm Giáp Thìn (19/1/1785), đoàn thuyền Xiêm xuôi vào khúc sông ấy thì "
                 "bị đánh úp, gần như bị diệt; sử nhà Nguyễn chép chỉ vài nghìn người chạy thoát, và từ đó quân Xiêm "
                 "\"sợ Tây Sơn như sợ cọp\" (mức B). **Hư cấu:** Anh Tư làm người dẫn đường, đồng bạc, mọi lời thoại. "
                 "Tập này là **tiền truyện của tập 5** (đêm cấm đập muỗi)."),
        setting=("Vietnam, January 1785, the wide brown Tiền River in the Mekong delta: coconut and nipa palms, mangrove "
                 "islands, narrow side creeks hidden by vegetation. A large Siamese fleet of tall wooden warships with "
                 "high curved sterns and banners; Siamese soldiers and officers in Siamese military dress of the period. "
                 "Tây Sơn soldiers in dark-red uniforms with red head wraps, small fast boats. "
                 f"Anh Tư is {FACE}, a local fisherman in a dark-brown short tunic and cloth head wrap, rowing a small sampan."),
        hook="POV: Được thuê / dẫn đường cho giặc",
        end="Sử không ghi tên Anh Tư. / Follow để xem đời sau / nhà Anh Tư bị giao việc gì →",
        clips=[
            dict(name="Việc lạ", label="Sông Tiền · tháng Giêng năm 1785",
                 img=f"First-person view at night on the Tiền River lit by a lantern, a Tây Sơn officer in a dark-red uniform leaning from his boat toward a small sampan, {FACE} in the sampan beside the viewer, listening with a puzzled face, realistic, vertical 9:16.",
                 vid="0-5s: At night, a Tây Sơn officer leans from his boat and says quietly: \"Mai ra xin làm người dẫn đường cho thuyền Xiêm. Dẫn họ xuôi xuống khúc này.\" 5-10s: Anh Tư blinks: \"Dẫn giặc... đi tham quan ạ?\" The officer: \"Dẫn cho khéo. Không hỏi.\"",
                 subs=[(0.5, 4.8, "Mai xin làm người dẫn đường / cho thuyền Xiêm."),
                       (5.0, 7.4, "Dẫn giặc... / đi tham quan ạ?"),
                       (7.4, 9.6, "Dẫn cho khéo. Không hỏi.")]),
            dict(name="Được thuê", tiktok="bo", label="Sáng hôm sau",
                 img=f"First-person view on the deck of a tall Siamese warship, a Siamese officer placing a silver coin in the palm of {FACE}, who bows politely, realistic, vertical 9:16.",
                 vid="0-5s: On the Siamese warship, an officer drops a silver coin into Anh Tư's palm and points downstream; Anh Tư bows deeply and smiles. 5-10s: Anh Tư bites the coin, then whispers to the viewer: \"Hai bên cùng thuê em dẫn đường... mà chỉ bên này trả tiền.\"",
                 subs=[(5.0, 9.5, "Hai bên cùng thuê / em dẫn đường... mà chỉ / bên này trả tiền.")]),
            dict(name="Dẫn đường", label="",
                 img=f"First-person view from a small sampan at the head of a huge fleet of tall Siamese warships moving downstream on a wide river, {FACE} rowing at the front, turning back to wave cheerfully at the ships, realistic, vertical 9:16.",
                 vid="0-5s: Anh Tư rows at the head of the huge fleet, turning back to wave cheerfully and point downstream; the warships follow in a long line. 5-10s: He leans toward the viewer and whispers, still smiling: \"Thêm một khúc nữa thôi. Chỗ ấy cảnh đẹp lắm, ai đến cũng không muốn về.\"",
                 subs=[(5.0, 9.6, "Thêm một khúc nữa thôi. / Chỗ ấy cảnh đẹp lắm, / ai đến cũng không muốn về.")]),
            dict(name="Rạch nhỏ", tiktok="bo", label="Khúc Rạch Gầm – Xoài Mút",
                 img=f"First-person view from a sampan slipping into a narrow creek hidden by nipa palms, dozens of Tây Sơn soldiers crouching silently in boats, their arms covered in mosquito bites, glaring at {FACE}, realistic, vertical 9:16.",
                 vid="0-5s: The river turns quiet; birds fly up from the banks. Anh Tư calls back to the fleet: \"Em xin phép... đi vệ sinh tí!\" and slips his sampan into a narrow creek. 5-10s: Inside, dozens of hidden Tây Sơn soldiers covered in mosquito bites glare at him; one hisses: \"Cả đêm cấm đập muỗi... mày dẫn chậm thế!\"",
                 subs=[(0.5, 4.8, "Em xin phép... / đi vệ sinh tí!"),
                       (5.0, 9.5, "Cả đêm cấm đập muỗi... / mày dẫn chậm thế!")]),
            dict(name="Ghi tên em vào sử", label="",
                 img=f"First-person view from a creek mouth as hundreds of small Tây Sơn boats burst out from the palms and an island onto the wide river toward the Siamese fleet, war drums, {FACE} standing in his sampan with a huge chipped-tooth grin, no blood, realistic, vertical 9:16.",
                 vid="0-5s: War drums; hundreds of small boats burst out of the creeks and from behind the island onto the river; the tall warships try to turn. A calm narrator's voice says: \"Sử nhà Nguyễn chép: từ trận ấy, quân Xiêm sợ Tây Sơn như sợ cọp.\" 5-10s: Anh Tư turns to the camera with his chipped-tooth grin: \"Đường này em dẫn đấy! Ghi tên em vào sử nhé!\"",
                 subs=[(0.3, 4.8, "Sử nhà Nguyễn chép: / từ trận ấy, quân Xiêm / sợ Tây Sơn như sợ cọp."),
                       (5.0, 9.8, "Đường này em dẫn đấy! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Được thuê dẫn đường cho đoàn thuyền giặc, dẫn đến khúc sông yên tĩnh nhất thì... 🤫 Tháng Giêng năm 1785, "
                 "Nguyễn Huệ phục kích đoàn thuyền Xiêm ở khúc sông Tiền từ Rạch Gầm đến Xoài Mút. Ai đã xem tập \"cấm đập "
                 "muỗi\" thì nhận ra mấy anh lính trong rạch rồi đúng không? 👇"),
        tags="#rachgamxoaimut #nguyenhue #tayson #songtien #1785",
        tt_title="Được thuê dẫn đường cho đoàn thuyền giặc, dẫn đến khúc sông yên tĩnh nhất thì...",
        hooks_alt=["POV: Hai bên cùng thuê / mình dẫn đường", "POV: Dẫn giặc / đi tham quan sông Tiền"],
        pin=("Đây là tiền truyện của tập \"cấm đập muỗi\" 🦟 Bạn xem tập nào trước? Follow để xem đời sau nhà Anh Tư!"),
        yt_title="Được thuê dẫn đường cho thuyền giặc, dẫn đến khúc sông Rạch Gầm thì... (năm 1785)",
        yt_tags=("rạch gầm xoài mút, nguyễn huệ, tây sơn, trận rạch gầm, quân xiêm, sông tiền, 1785, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1789 cầu phao sông Nhị
    dict(
        slug="canh-cau-phao-1789", prefix="nbt12",
        title="Bị bắt canh cầu phao cho quân Thanh dịp Tết, sáng mùng 5 thấy Tổng đốc phi qua cầu mà ngựa chưa kịp đóng yên (Ngọc Hồi – Đống Đa, 1789)",
        length=LEN_FULL,
        history=("**Lịch sử:** cuối năm 1788, Tổng đốc Lưỡng Quảng Tôn Sĩ Nghị đem quân Thanh sang, đóng ở Thăng Long, "
                 "bắc cầu phao qua sông Nhị (sông Hồng) để tiện đi lại, định ra Giêng mới đánh tiếp. Vua Quang Trung "
                 "hành quân thần tốc ra Bắc; mùng 5 Tết Kỷ Dậu (30/1/1789) phá đồn Ngọc Hồi và Đống Đa, trưa hôm ấy "
                 "vào Thăng Long. Tôn Sĩ Nghị bỏ chạy qua cầu phao về phía bắc, cầu sập; sử chép ông bỏ lại cả ấn tín "
                 "(mức B), và nhà Thanh sau đó triệu ông về. Chi tiết \"ngựa không kịp đóng yên, người không kịp mặc "
                 "giáp\" theo *Hoàng Lê nhất thống chí* (tiểu thuyết lịch sử, mức C). **Hư cấu:** Anh Tư, người phiên "
                 "dịch và mọi lời thoại. Không dựng cảnh người rơi xuống sông."),
        setting=("Vietnam, Tết Kỷ Dậu (late January 1789), Thăng Long on the Red River: a long pontoon bridge of wooden "
                 "boats lashed together under planks, the Qing camp on the bank with plain banners without writing and red "
                 f"lanterns. {QING_EN} A Vietnamese interpreter in a dark Lê-era official robe. "
                 f"Anh Tư is {FACE}, a Thăng Long laborer in a patched brown shirt and cloth head wrap. "
                 "Tây Sơn troops in dark-red uniforms appear only at the end, at a distance."),
        visual=QING_VIS,
        hook="POV: Canh cầu phao / cho quân Thanh / dịp Tết",
        end="Follow để xem đời sau / nhà Anh Tư bị giao việc gì →",
        clips=[
            dict(name="Việc canh cầu", label="Thăng Long · Tết Kỷ Dậu 1789",
                 img=f"First-person view on a long pontoon bridge of boats and planks over a wide river, a Qing officer with a queue pointing at the ropes while a Vietnamese interpreter in a dark robe translates, {FACE} beside the viewer holding a coil of rope, realistic, vertical 9:16.",
                 vid="0-5s: A Qing officer points at the ropes and speaks; the interpreter translates: \"Ngày đêm giữ cầu cho chắc. Đại quân còn đi lại.\" 5-10s: Anh Tư asks politely: \"Cầu này... để đi sang hay để chạy về ạ?\" The interpreter glares: \"Đừng hỏi. Giữ cầu.\"",
                 subs=[(0.5, 4.8, "Ngày đêm giữ cầu cho chắc. / Đại quân còn đi lại."),
                       (5.0, 7.6, "Cầu này... để đi sang / hay để chạy về ạ?"),
                       (7.6, 9.6, "Đừng hỏi. Giữ cầu.")]),
            dict(name="Ăn Tết trước", tiktok="5-10", label="Mùng 3 Tết",
                 img=f"First-person view from the pontoon bridge at dusk, the Qing camp on the bank festive with red lanterns, soldiers feasting and setting off firecrackers, {FACE} tying ropes on the bridge, looking at the camp, realistic, vertical 9:16.",
                 vid="0-5s: In the lantern-lit camp, Qing soldiers feast and light firecrackers; the interpreter strolls past the bridge: \"Ra Giêng mới đánh. Tết thì cứ ăn đã.\" 5-10s: Anh Tư tightens a rope and mutters to the viewer: \"Người ta ăn Tết. Còn em... ăn dây thừng.\"",
                 subs=[(0.5, 4.8, "Ra Giêng mới đánh. / Tết thì cứ ăn đã."),
                       (5.0, 9.5, "Người ta ăn Tết. / Còn em... ăn dây thừng.")]),
            dict(name="Tiếng pháo mùng 5", tiktok="5-10", label="Sáng mùng 5 Tết",
                 img=f"First-person view at dawn from the pontoon bridge, distant smoke rising on the southern horizon, Qing soldiers in the camp stopping and turning toward the sound, {FACE} with a hand cupped behind his ear, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; deep booms roll from the south and smoke rises on the horizon; the camp falls silent, soldiers turn their heads. 5-10s: Anh Tư cups his ear and asks the viewer innocently: \"Ơ... pháo Tết nhà ai mà to thế?\"",
                 subs=[(5.0, 9.5, "Ơ... pháo Tết nhà ai / mà to thế?")]),
            dict(name="Tổng đốc qua cầu", label="Gần trưa",
                 img=f"First-person view from the side of the pontoon bridge, a high-ranking Qing commander without armor galloping across on a horse with no saddle, guards running behind him, {FACE} pressed against the rail holding his hat, mouth open, realistic, vertical 9:16.",
                 vid="0-5s: A high-ranking Qing commander, without armor, gallops across the swaying bridge on a horse with no saddle, his guards running behind; planks bounce. 5-10s: Anh Tư, pressed against the rail, whispers to the viewer: \"Tổng đốc chạy nhanh hơn cả ngựa... ngựa còn chưa kịp đóng yên.\"",
                 subs=[(0.5, 4.8, "Ngựa không kịp đóng yên, / người không kịp mặc giáp."),
                       (5.0, 9.5, "Tổng đốc chạy / nhanh hơn cả ngựa... / ngựa chưa kịp đóng yên.")]),
            dict(name="Câu chốt", label="Trưa mùng 5 Tết",
                 img=f"First-person view from the riverbank at noon, the pontoon bridge broken in the middle and drifting apart with no people on it, across the city a great Tây Sơn army with red banners entering Thăng Long in the distance, {FACE} holding a cut rope end, grinning, realistic, vertical 9:16.",
                 vid="0-5s: Noon; the pontoon bridge has broken in the middle and its boats drift apart, empty; in the distance a great army with red banners enters the city. A calm narrator's voice says: \"Trưa mùng 5 Tết Kỷ Dậu, vua Quang Trung vào Thăng Long. Tôn Sĩ Nghị chạy về nước, bỏ lại cả ấn tín.\" 5-10s: Anh Tư holds up a cut rope end and grins at the camera: \"Cầu này em giữ đấy... giữ đến lúc nó sập! Tết này em ăn bù!\"",
                 subs=[(0.3, 4.8, "Trưa mùng 5 Tết, vua / Quang Trung vào Thăng Long. / Tôn Sĩ Nghị bỏ lại ấn tín."),
                       (5.0, 9.8, "Cầu này em giữ đấy... / giữ đến lúc nó sập! / Tết này em ăn bù!")]),
        ],
        caption=("Bị bắt canh cầu phao cho quân Thanh dịp Tết, sáng mùng 5 thấy Tổng đốc phi qua cầu mà ngựa chưa kịp đóng "
                 "yên 😳 Mùng 5 Tết Kỷ Dậu (1789), vua Quang Trung phá đồn Ngọc Hồi, Đống Đa và vào Thăng Long. Bạn biết "
                 "gò Đống Đa ngày nay nằm ở đâu không? 👇"),
        tags="#ngochoidongda #quangtrung #tonsinghi #tetkydau #1789",
        tt_title="Canh cầu phao cho quân Thanh dịp Tết, sáng mùng 5 thấy Tổng đốc phi qua cầu",
        hooks_alt=["POV: Tổng đốc chạy / nhanh hơn cả ngựa", "POV: Pháo Tết mùng 5 / to bất thường"],
        pin=("Mùng 5 Tết là ngày giỗ trận Đống Đa, đến nay Hà Nội vẫn mở hội Gò Đống Đa 🎆 Bạn đã đi hội lần nào chưa? "
             "Follow để xem đời sau nhà Anh Tư!"),
        yt_title="Canh cầu phao cho quân Thanh dịp Tết, sáng mùng 5 thấy Tổng đốc phi qua cầu (năm 1789)",
        yt_tags=("ngọc hồi đống đa, quang trung, tôn sĩ nghị, tết kỷ dậu, cầu phao sông hồng, quân thanh, 1789, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#povnguoibinhthuong #anhtu",
          note=NOTE, unit="Tập", file_unit="tap")
