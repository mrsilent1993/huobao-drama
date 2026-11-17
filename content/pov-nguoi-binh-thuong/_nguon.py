#!/usr/bin/env python3
"""Nguồn của loạt "POV người bình thường" (bản 2). Sửa ở đây rồi chạy: python3 _nguon.py

Công thức (từ video Bạch Đằng 938: 1,4 triệu lượt xem, 43,6% xem hết, 14 nghìn lượt chia sẻ):
- Nhân vật quen mặt: ANH TƯ (sẹo ngang lông mày trái, răng cửa mẻ, cười toe). Mỗi tập là một đời con cháu,
  đời nào cũng bị giao một việc vô lý mà không ai giải thích.
- Giây 0: lao động cận cảnh + câu lệnh vô lý. Mỗi clip đúng MỘT câu chốt ngắn.
- Clip cuối: vỡ lẽ bằng cảnh lớn + câu cửa miệng "Ghi tên em vào sử nhé!"
- TikTok 30 giây = clip 1, 3, 5. YouTube 50 giây = đủ 5 clip (clip 2, 4 là trò cười riêng, không phải clip đệm).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")

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
        end="Sử không ghi tên Anh Tư. / Follow để xem đời sau nhà Anh Tư / bị bắt khuân hết thóc đi →",
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
            dict(name="Ghi tên em vào sử", label="Mấy tuần sau",
                 img=f"First-person view from an earthen rampart lined with bamboo stakes, across the river Song soldiers sitting idle at their camp, one fishing, {FACE} on the rampart eating a rice ball and waving at them cheerfully, realistic, vertical 9:16.",
                 vid="0-5s: Weeks later; across the river, Song soldiers sit idle, one of them fishing, staring at the wall of bamboo. 5-10s: Anh Tư, eating a rice ball on the rampart, waves at them, then turns to the camera with his chipped-tooth grin: \"Cắm một đêm, nó đứng nhìn cả tháng. Ghi tên em vào sử nhé!\"",
                 subs=[(5.0, 9.8, "Cắm một đêm, nó đứng nhìn cả tháng. / Ghi tên em vào sử nhé!")]),
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
        end="Ba ngày sau, giặc ăn gì? / Follow để xem đời sau nhà Anh Tư / bị lệnh phải thua trận →",
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
            dict(name="Ghi tên mẹ em vào sử", label="Ba ngày sau",
                 img=f"First-person view from behind a bush on a hillside, thin exhausted Mongol-Yuan soldiers below digging for roots in an empty field, one chewing grass, a tiny fierce old woman with black teeth peeking beside {FACE}, realistic, vertical 9:16.",
                 vid="0-5s: Three days later; from behind a bush, they watch thin, exhausted enemy soldiers dig for roots, one chewing a blade of grass. Mẹ Anh Tư nods with satisfaction: \"Mời giặc vào nhà mà không mời cơm. Thế mới là lễ.\" 5-10s: Anh Tư turns to the camera, grinning with his chipped tooth: \"Ghi tên mẹ em vào sử nhé!\"",
                 subs=[(0.5, 4.8, "Mời giặc vào nhà mà không mời cơm. / Thế mới là lễ."),
                       (5.0, 9.5, "Ghi tên mẹ em vào sử nhé!")]),
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
        end="Thua một buổi sáng thì được gì? / Follow để xem đời sau nhà Anh Tư / bị lệnh chạy thua cả ngày →",
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
            dict(name="Ghi tên em vào sử", label="Ngay sau đó",
                 img=f"First-person view from a small boat charging out of the mangroves toward huge Yuan warships stuck and tilting on stakes, drums from both banks, {FACE} standing in the boat grinning at the camera, realistic, vertical 9:16.",
                 vid="0-5s: The giant warships grind onto the stakes, tilt and crack; drums roar from both banks and the small boats charge back out. 5-10s: Anh Tư stands up in the boat and turns to the camera: \"Thua một buổi, thắng cả cuộc chiến. Ghi tên em vào sử nhé!\"",
                 subs=[(5.0, 9.8, "Thua một buổi, thắng cả cuộc chiến. / Ghi tên em vào sử nhé!")]),
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
        end="Chạy cả ngày, giờ ai phải chạy? / Follow để xem đời sau nhà Anh Tư / bị cấm đập muỗi cả đêm →",
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
            dict(name="Ghi tên em vào sử", label="Ngay sau đó",
                 img=f"First-person view in a narrow mountain pass, hundreds of Lam Sơn soldiers rising from hiding on both cliffsides with crossbows and banners, Ming cavalry trapped below, {FACE} turning around and cracking his knuckles with a grin, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; hundreds of hidden soldiers rise from both cliffsides with crossbows and banners; the Ming cavalry is trapped in the pass. The officer shouts: \"Hết giờ chạy. Quay lại!\" 5-10s: Anh Tư turns around, cracks his knuckles and grins at the camera: \"Chạy cả ngày rồi, giờ đến lượt nó! Ghi tên em vào sử nhé!\"",
                 subs=[(0.5, 4.8, "Hết giờ chạy. Quay lại!"),
                       (5.0, 9.8, "Chạy cả ngày rồi, giờ đến lượt nó! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Bị lệnh chạy thua cả ngày mà không ai nói vì sao, đến ải Chi Lăng mới hiểu 😤 Năm 1427, Trần Lựu "
                 "giả thua nhử Liễu Thăng vào ải Chi Lăng, nơi quân Lam Sơn mai phục sẵn. Bạn chịu bị giặc cười được "
                 "mấy tiếng? 👇"),
        tags="#chilang #leloi #lamson #1427",
    ),
    # ------------------------------------------------------------------ 1785
    dict(
        slug="cam-dap-muoi-rach-gam-1785", prefix="nbt5",
        title="Bị cấm ho, cấm đập muỗi cả đêm mà không ai nói chờ gì, sáng ra mới hiểu (Rạch Gầm – Xoài Mút, 1785)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
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
            dict(name="Cái hắt hơi", tiktok="bo", label="Nửa đêm",
                 img=f"First-person view in a dark creek under nipa palms, {FACE} about to sneeze with his head tilted back, three soldiers lunging to pinch his nose and cover his mouth at the same time, realistic, vertical 9:16.",
                 vid="0-5s: Midnight; Anh Tư's face scrunches up, his head tilts back, he is about to sneeze; three soldiers lunge at once to pinch his nose and clamp his mouth. 5-10s: The sneeze dies with a tiny squeak; everyone freezes, listening; the officer slowly lets out his breath and glares at Anh Tư.",
                 subs=[]),
            dict(name="Thuyền giặc đi ngang", label="Rạng sáng",
                 img="First-person view peeking out from a hidden creek at dawn, a long line of Siamese warships with tall sails gliding past very close in the mist, a stern officer in the foreground with a mosquito sitting on his nose, not blinking, realistic, vertical 9:16.",
                 vid="0-5s: A line of Siamese warships glides past the creek mouth, so close the viewer can hear sailors chatting on deck. 5-10s: A mosquito lands right on the officer's nose; he doesn't blink. Anh Tư, beside the viewer, shakes with silent laughter, tears in his eyes, hands over his mouth.",
                 subs=[]),
            dict(name="Mặt sưng", tiktok="bo", label="Cùng lúc",
                 img=f"First-person view in a small hidden boat, soldiers with faces swollen from mosquito bites gripping their weapons, {FACE} with one eye swollen shut grinning, Siamese sails visible through the leaves, realistic, vertical 9:16.",
                 vid="0-5s: The viewer looks around the boat: every face is swollen from mosquito bites; Anh Tư's left eye is completely swollen shut. 5-10s: Anh Tư whispers, still grinning: \"Giặc chưa đánh mình, muỗi đã đánh mình tan tác rồi.\"",
                 subs=[(5.0, 9.5, "Giặc chưa đánh mình, / muỗi đã đánh mình tan tác rồi.")]),
            dict(name="Ghi tên em vào sử", label="Ngay sau đó",
                 img=f"First-person view from a small boat bursting out of a creek onto a wide river at dawn, dozens of Tây Sơn boats charging from creeks and islets on both sides, drums, the Siamese fleet trapped in the middle, {FACE} slapping a mosquito on his arm with a huge grin, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; boats burst out of every creek and islet at once, trapping the Siamese fleet in the middle of the river. 5-10s: Paddling hard, Anh Tư finally slaps the mosquito on his arm with a loud smack and shouts at the camera: \"Giờ thì đập được rồi! Ghi tên em vào sử nhé!\"",
                 subs=[(5.0, 9.8, "Giờ thì đập được rồi! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Bị cấm ho, cấm đập muỗi cả đêm mà không ai nói chờ gì, sáng ra mới hiểu 🦟 Tháng 1 năm 1785, quân "
                 "Tây Sơn của Nguyễn Huệ mai phục ở khúc sông Tiền giữa Rạch Gầm và Xoài Mút, đánh tan thủy quân Xiêm. "
                 "Bạn nhịn được mấy con muỗi? 👇"),
        tags="#rachgamxoaimut #nguyenhue #tayson #1785",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#povnguoibinhthuong #anhtu",
          note=NOTE, unit="Tập", file_unit="tap")
