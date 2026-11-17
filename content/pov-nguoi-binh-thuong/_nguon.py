#!/usr/bin/env python3
"""Nguồn của loạt "POV người bình thường". Sửa ở đây rồi chạy: python3 _nguon.py

Công thức (lấy từ video Bạch Đằng 938, 1,4 triệu lượt xem, 43,6% xem hết, 14 nghìn lượt chia sẻ):
- Khung hình đầu: lao động chân tay cận cảnh (chân lội bùn, tay đóng cọc...), chuyển động ngay giây 0.
- Người dân thường được giao một việc nghe vô lý, KHÔNG AI GIẢI THÍCH.
- Ít nhất một câu "đáng gửi cho bạn bè": ngắn, đời thường, dùng như meme.
- Cú vỡ lẽ ở clip cuối.
- Bản TikTok 30 giây = clip 1, 3, 5. Bản YouTube 50 giây = đủ 5 clip.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

NOTE = ("**Công thức của loạt:** khung hình đầu là lao động cận cảnh, người dân được giao việc vô lý mà không ai "
        "giải thích, có một câu đáng gửi cho bạn bè, và vỡ lẽ ở cuối. Bản TikTok 30 giây gồm clip 1, 3, 5; bản "
        "YouTube 50 giây gồm đủ 5 clip.")

EPISODES = [
    # ------------------------------------------------------------------ 1077
    dict(
        slug="dap-luy-nhu-nguyet-1077", prefix="nbt1",
        title="Đắp lũy cắm tre cả đêm mà không ai nói để làm gì, sáng ra mới hiểu",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1077, quân Lý dựng phòng tuyến dọc bờ nam sông Như Nguyệt (sông Cầu): lũy đất, "
                 "cọc tre cắm dày nhiều tầng làm giậu, dưới bãi sông có hố chông ngầm, quân đóng thành nhiều trại. Quân "
                 "Tống do Quách Quỳ chỉ huy kéo đến bờ bắc, chờ thủy binh để vượt sông, nhiều lần đánh sang nhưng không "
                 "qua được, rồi phải giảng hòa rút quân. **Hư cấu:** người dân đắp lũy và mọi lời thoại."),
        setting=("Vietnam, Lý dynasty, early 1077, the south bank of the Như Nguyệt River (Cầu River). Villagers and "
                 "soldiers with short cropped hair, black-lacquered teeth, brown clothes, barefoot, carrying baskets of "
                 "earth on shoulder poles, hammering sharpened bamboo stakes; an officer in a dark-red uniform; across "
                 "the river, a huge Song army camp with banners. Night scenes lit only by moonlight."),
        hook="Đắp lũy cả đêm / không ai nói để làm gì",
        end="Quân Tống đứng bên kia sông bao lâu? / Follow để xem mai bạn được lệnh / mang hết thóc đi →",
        clips=[
            dict(name="Cắm tre giữa đêm", label="Bờ sông Như Nguyệt · đêm 1077",
                 img="First-person close-up at night by moonlight, the viewer's muddy hands hammering a sharpened bamboo stake into an earthen rampart with a wooden mallet, rows of bamboo stakes behind, other villagers working silently, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's muddy hands hammer a sharpened bamboo stake into an earthen rampart by moonlight; the villager next to him whispers: \"Cắm tre dày thế này, định làm hàng rào nuôi vịt à anh?\" 5-10s: An officer walks past and says only: \"Cắm thêm hai hàng nữa. Trước khi trời sáng.\" The viewer stares at the endless line of stakes along the river and sighs.",
                 subs=[(0.5, 4.8, "Cắm tre dày thế này, / định làm hàng rào nuôi vịt à anh?"),
                       (5.0, 9.5, "Cắm thêm hai hàng nữa. / Trước khi trời sáng.")]),
            dict(name="Hố dưới bãi sông", tiktok="bo", label="Nửa đêm",
                 img="First-person view knee-deep in mud on a riverbank at night, the viewer digging a pit and placing sharpened bamboo spikes at the bottom, covering it with reeds, other villagers doing the same along the bank, realistic, vertical 9:16.",
                 vid="0-5s: Knee-deep in mud, the viewer digs a pit on the river flat, sets sharpened bamboo spikes inside, and covers it with reeds and mud. 5-10s: The villager beside him whispers: \"Đào hố rồi lấp lại cho kín... thế đào làm gì?\" The viewer shrugs and keeps covering it.",
                 subs=[(5.0, 9.5, "Đào hố rồi lấp lại cho kín... / thế đào làm gì?")]),
            dict(name="Ngủ gục trên lũy", label="Gần sáng",
                 img="First-person view at dawn lying exhausted on top of a finished earthen rampart lined with dense bamboo stakes, muddy feet in frame, mist over the river, a sleeping villager beside, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; the viewer collapses on top of the finished rampart, muddy feet in frame, mist over the river; the villager beside him mumbles: \"Cả đêm đắp đất, cắm tre... mà chẳng ai nói để làm gì.\" 5-10s: A distant drumbeat rolls across the water; both of them slowly sit up.",
                 subs=[(0.5, 4.8, "Cả đêm đắp đất, cắm tre... / mà chẳng ai nói để làm gì.")]),
            dict(name="Bên kia sông", tiktok="bo", label="Sáng sớm",
                 img="First-person view from the top of an earthen rampart at morning, looking across a river at a huge Song army with thousands of banners and soldiers lining the far bank, mist lifting, realistic, vertical 9:16.",
                 vid="0-5s: The mist lifts: across the river, a huge Song army fills the far bank, thousands of banners, soldiers and horses as far as the eye can see. 5-10s: The viewer's jaw drops; the villager beside him whispers: \"Ơ... đông thế kia mà sang được bên này thì...\"",
                 subs=[(5.0, 9.5, "Ơ... đông thế kia mà sang được bên này thì...")]),
            dict(name="Không qua được", label="Mấy tuần sau",
                 img="First-person view from an earthen rampart lined with bamboo stakes, Song soldiers on the far bank sitting idle by their camp, some fishing, a Vietnamese villager on the rampart cooking rice and waving across the river, realistic, vertical 9:16.",
                 vid="0-5s: Weeks later; across the river, Song soldiers sit idle by their camp, one of them even fishing, staring at the wall of bamboo stakes. 5-10s: The villager beside the viewer stirs a pot of rice on the rampart, looks across and grins: \"Cắm có một đêm, mà nó đứng nhìn cả tháng. Đáng công!\"",
                 subs=[(5.0, 9.5, "Cắm có một đêm, / mà nó đứng nhìn cả tháng. Đáng công!")]),
        ],
        caption=("Đắp lũy cắm tre cả đêm mà không ai nói để làm gì, sáng ra mới hiểu 😳 Năm 1077, phòng tuyến sông Như "
                 "Nguyệt với lũy đất, cọc tre nhiều tầng và hố chông ngầm khiến quân Tống không vượt sông được. Nếu là "
                 "bạn, bạn sẽ cắm mấy hàng tre? 👇"),
        tags="#nhunguyet #lythuongkiet #1077",
    ),
    # ------------------------------------------------------------------ 1285
    dict(
        slug="vuon-khong-nha-trong-1285", prefix="nbt2",
        title="Được lệnh mang hết thóc đi, bỏ trống cả nhà, ba ngày sau mới hiểu",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1285, trước sức mạnh của quân Nguyên, nhà Trần rút quân và cho dân sơ tán, mang "
                 "theo lương thực, để lại Thăng Long trống không, gọi là kế **\"vườn không nhà trống\"**. Quân Nguyên "
                 "vào được thành nhưng không có gì ăn, dần rơi vào cảnh đói, quân số hao mòn, rồi phải bỏ Thăng Long "
                 "rút đi. **Lưu ý:** mình chưa tìm thấy nguồn chép dân tự **đốt** thóc của mình, nên tập phim dùng "
                 "\"mang đi, cất giấu\". **Hư cấu:** gia đình người dân và mọi lời thoại."),
        setting=("Vietnam, Trần dynasty, early 1285, a village near Thăng Long and the capital itself. Villagers with "
                 "short cropped hair, black-lacquered teeth, brown clothes, barefoot, carrying sacks of rice and baskets "
                 "on shoulder poles, leading buffaloes; an old village elder; later Mongol-Yuan soldiers in leather "
                 "armor and fur-trimmed hats in an empty city. The viewer's mother is a sharp-tongued woman around 50."),
        hook="Được lệnh mang hết thóc đi / bỏ trống cả nhà",
        end="Giặc đói thì làm gì tiếp? / Follow để xem mai bạn chèo thuyền / được lệnh thua trận →",
        clips=[
            dict(name="Khuân thóc trong đêm", label="Làng ven Thăng Long · đầu năm 1285",
                 img="First-person close-up of the viewer's hands hoisting a heavy sack of rice onto a shoulder pole in a dim thatched granary, rice grains spilling, a village elder holding a torch at the door, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's hands heave a heavy sack of rice onto a shoulder pole, grains spilling; the village elder at the door orders: \"Mang hết thóc đi, không để lại một hạt!\" 5-10s: The viewer's mother grabs the sack, outraged: \"Thóc nhà mình cấy cả năm, giờ khuân đi đâu? Giặc chưa đến đã như bị cướp!\"",
                 subs=[(0.5, 4.8, "Mang hết thóc đi, không để lại một hạt!"),
                       (5.0, 9.8, "Thóc nhà mình cấy cả năm, giờ khuân đi đâu? / Giặc chưa đến đã như bị cướp!")]),
            dict(name="Bỏ cả nhà", tiktok="bo", label="Sáng hôm sau",
                 img="First-person view at the door of a thatched house being emptied, 1285, the viewer's mother taking the last pot off the stove, a buffalo being led away, other families leaving the village with baskets, realistic, vertical 9:16.",
                 vid="0-5s: The family strips the house: pots, mats, even the water jar; the viewer leads the buffalo out of the yard. 5-10s: The mother looks back at the empty house and grumbles: \"Nhà thì để không, giặc vào ở sướng nhé!\" The elder answers calmly: \"Ở thì được. Ăn thì không.\"",
                 subs=[(5.0, 7.5, "Nhà thì để không, giặc vào ở sướng nhé!"),
                       (7.5, 9.8, "Ở thì được. Ăn thì không.")]),
            dict(name="Trốn trong núi", label="Trên núi · ngày thứ nhất",
                 img="First-person view in a crowded mountain hideout at dusk, villagers sitting among sacks of rice and baskets, a buffalo tied to a tree, the viewer's mother cooking a tiny pot of rice, realistic, vertical 9:16.",
                 vid="0-5s: In a crowded mountain hideout, villagers sit among hidden sacks of rice; the mother cooks a tiny pot and whispers: \"Thóc mang theo cả bao mà mỗi bữa chỉ được nấu một nắm. Khổ thế này để làm gì?\" 5-10s: Far below, smoke rises over the empty capital; the viewer stares at it, puzzled.",
                 subs=[(0.5, 4.8, "Thóc mang theo cả bao mà mỗi bữa / chỉ được nấu một nắm. Khổ thế này để làm gì?")]),
            dict(name="Giặc vào thành trống", tiktok="bo", label="Thăng Long · cùng lúc",
                 img="First-person view from a hiding spot behind a wall in an empty ancient city, Mongol-Yuan soldiers in leather armor searching empty houses and an empty granary, lifting empty baskets, realistic, vertical 9:16.",
                 vid="0-5s: From behind a wall, the viewer, sent down to scout, watches Mongol-Yuan soldiers kick open granary doors: empty. One lifts an empty basket and shakes it. 5-10s: Another soldier opens an empty water jar, looks inside, then looks at his comrades in silence.",
                 subs=[]),
            dict(name="Ba ngày sau", label="Ba ngày sau",
                 img="First-person view from behind a bush on a hillside, below a group of thin, tired Mongol-Yuan soldiers digging in an empty field for roots, one chewing grass, the viewer's mother peeking beside the viewer, realistic, vertical 9:16.",
                 vid="0-5s: Three days later; from behind a bush, the viewer and his mother watch thin, exhausted enemy soldiers dig in an empty field for roots; one chews a blade of grass. 5-10s: The mother slowly understands, then nods with satisfaction: \"À... thế mới gọi là mời giặc vào nhà mà không mời cơm.\"",
                 subs=[(5.0, 9.5, "À... thế mới gọi là / mời giặc vào nhà mà không mời cơm.")]),
        ],
        caption=("Được lệnh mang hết thóc đi, bỏ trống cả nhà, ba ngày sau mới hiểu 😏 Năm 1285, kế \"vườn không nhà "
                 "trống\" khiến quân Nguyên chiếm được Thăng Long mà không có gì ăn. Mẹ bạn sẽ phản ứng thế nào nếu bị "
                 "bắt khuân hết thóc đi? 👇"),
        tags="#vuonkhongnhatrong #nhatran #1285",
    ),
    # ------------------------------------------------------------------ 1288
    dict(
        slug="cheo-thuyen-nhu-giac-1288", prefix="nbt3",
        title="Chèo thuyền nhử giặc rồi bỏ chạy, tưởng thua, hóa ra...",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1288, quân Trần cho thuyền nhỏ ra khiêu chiến thủy quân Nguyên của Ô Mã Nhi lúc "
                 "triều lên, rồi giả thua bỏ chạy, nhử thuyền giặc vào khu sông Bạch Đằng đã cắm cọc. Triều rút, thuyền "
                 "giặc mắc cọc và bị đánh tan, Ô Mã Nhi bị bắt sống. **Hư cấu:** người chèo thuyền và mọi lời thoại."),
        setting=("Vietnam, Trần dynasty, spring 1288, the Bạch Đằng River estuary. Trần soldiers with short cropped "
                 "hair, black-lacquered teeth, brown uniforms, 'Sát Thát' tattooed on their forearms, paddling small "
                 "light boats; huge Yuan warships with many sails; mangroves; tidal water."),
        hook="Chèo thuyền nhử giặc / rồi bỏ chạy",
        end="Thuyền giặc mắc cọc rồi ra sao? / Follow để xem mai bạn được lệnh / chạy thua cả ngày →",
        clips=[
            dict(name="Lệnh lạ", label="Cửa sông Bạch Đằng · năm 1288",
                 img="First-person close-up of the viewer's tattooed forearms gripping a wooden paddle in a small light boat at dawn, water splashing, other small boats beside, an officer in a boat pointing toward huge enemy sails on the horizon, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's tattooed forearms dig a paddle into the water; the officer in the next boat shouts: \"Ra đánh vài nhát rồi quay đầu chạy. Nhớ: phải thua!\" 5-10s: The rower behind the viewer whispers: \"Đi đánh trận mà được lệnh thua... lần đầu em nghe đấy.\"",
                 subs=[(0.5, 4.8, "Ra đánh vài nhát rồi quay đầu chạy. / Nhớ: phải thua!"),
                       (5.0, 9.8, "Đi đánh trận mà được lệnh thua... / lần đầu em nghe đấy.")]),
            dict(name="Chọc giặc", tiktok="bo", label="Triều lên",
                 img="First-person view from a small boat right beside a huge Yuan warship with many sails, Vietnamese soldiers throwing spears and shooting arrows up at it, enemy soldiers shouting angrily over the rail, realistic, vertical 9:16.",
                 vid="0-5s: The small boats dart up to the giant warships; the viewer's crew throws a few spears and shouts insults; angry enemy faces appear over the rail. 5-10s: The officer yells: \"Đủ rồi! Chạy!\" The viewer spins the boat around as drums thunder from the warships.",
                 subs=[(5.0, 9.0, "Đủ rồi! Chạy!")]),
            dict(name="Chạy thật", label="Ít phút sau",
                 img="First-person view paddling furiously in a small boat fleeing upstream, looking back over the shoulder at a fleet of huge Yuan warships chasing, arrows splashing in the water around, realistic, vertical 9:16.",
                 vid="0-5s: The viewer paddles like crazy upstream, looking back: the whole Yuan fleet is chasing, arrows splashing all around. The rower behind gasps: \"Diễn thua mà sao giống thua thật thế này!\" 5-10s: The viewer shouts back without stopping: \"Thì cứ chạy đi, thua cho ra thua!\"",
                 subs=[(0.5, 4.8, "Diễn thua mà sao / giống thua thật thế này!"),
                       (5.0, 9.5, "Thì cứ chạy đi, thua cho ra thua!")]),
            dict(name="Nước rút", tiktok="bo", label="Giữa trưa",
                 img="First-person view from a small boat hidden among mangroves, watching the river water drop fast, sharpened wooden stakes rising out of the water in rows around the huge enemy warships, realistic, vertical 9:16.",
                 vid="0-5s: Hidden among the mangroves, the crew catches its breath; the water drops fast, and rows of sharpened stakes rise out of the river all around the enemy warships. 5-10s: The rower behind the viewer whispers, wide-eyed: \"Ơ... cọc ở đâu ra lắm thế?\"",
                 subs=[(5.0, 9.5, "Ơ... cọc ở đâu ra lắm thế?")]),
            dict(name="Hóa ra...", label="Ngay sau đó",
                 img="First-person view from a small boat charging out of the mangroves, huge Yuan warships stuck and tilting on stakes ahead, Vietnamese boats swarming in with drums, the officer laughing, realistic, vertical 9:16.",
                 vid="0-5s: The giant warships grind onto the stakes, tilt and crack; drums roar from both banks and the small boats charge back out. 5-10s: The officer, paddling past the viewer, laughs: \"Thua một buổi sáng, thắng cả cuộc chiến. Giờ thì đánh thật!\"",
                 subs=[(5.0, 9.8, "Thua một buổi sáng, thắng cả cuộc chiến. / Giờ thì đánh thật!")]),
        ],
        caption=("Chèo thuyền nhử giặc rồi bỏ chạy, tưởng thua, hóa ra... 😎 Năm 1288, quân Trần giả thua nhử thủy "
                 "quân Nguyên vào bãi cọc sông Bạch Đằng, triều rút là thuyền giặc mắc cọc. Bạn có diễn thua được "
                 "giống như thật không? 👇"),
        tags="#bachdang #tranhungdao #1288",
    ),
    # ------------------------------------------------------------------ 1427
    dict(
        slug="chay-thua-chi-lang-1427", prefix="nbt4",
        title="Được lệnh chạy thua cả ngày mà không ai nói vì sao, đến ải Chi Lăng mới hiểu",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1427, viện binh nhà Minh do Liễu Thăng chỉ huy tiến vào từ Lạng Sơn. Theo kế của "
                 "Lê Lợi và Nguyễn Trãi, tướng Trần Lựu vừa đánh vừa lui, giả thua để nhử. Liễu Thăng đuổi gấp, tự dẫn "
                 "hơn trăm kỵ binh đi trước, lọt vào ải Chi Lăng nơi quân Lam Sơn mai phục, và bị giết. Các nguồn ghi "
                 "ngày khác nhau (khoảng tháng 9–10 năm 1427), nên tập phim chỉ ghi năm. **Hư cấu:** người lính và mọi "
                 "lời thoại."),
        setting=("Vietnam, Lam Sơn uprising, autumn 1427, the mountain road from the border to the Chi Lăng pass in "
                 "Lạng Sơn: steep limestone mountains, a narrow valley, forest, muddy paths. Lam Sơn soldiers in plain "
                 "brown and dark-blue clothes with head wraps, spears, shields, crossbows; Ming cavalry in red-and-black "
                 "armor with banners; a Ming general in ornate armor on a horse."),
        hook="Được lệnh chạy thua / cả ngày",
        end="Liễu Thăng đuổi vào ải rồi sao? / Follow để xem mai bạn nấp cả đêm / mà bị cấm ho →",
        clips=[
            dict(name="Lệnh chạy", label="Đường biên giới Lạng Sơn · năm 1427",
                 img="First-person close-up of the viewer's muddy feet running on a rocky mountain path, a spear in hand, Lam Sơn soldiers running ahead, an officer looking back and waving them on, Ming banners appearing behind, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's muddy feet pound a rocky path; the officer ahead looks back and shouts: \"Đánh vài hiệp rồi chạy! Chạy cho chậm thôi, để chúng đuổi kịp!\" 5-10s: The soldier running beside the viewer pants: \"Chạy thua mà còn phải canh cho giặc đuổi kịp... nghề gì mà khó thế!\"",
                 subs=[(0.5, 4.8, "Đánh vài hiệp rồi chạy! / Chạy cho chậm thôi, để chúng đuổi kịp!"),
                       (5.0, 9.8, "Chạy thua mà còn phải canh cho giặc đuổi kịp... / nghề gì mà khó thế!")]),
            dict(name="Vừa đánh vừa lui", tiktok="bo", label="Giữa trưa",
                 img="First-person view in a narrow valley, Lam Sơn soldiers turning to fight briefly against Ming cavalry then retreating again, dust and banners, the viewer raising a shield, realistic, vertical 9:16.",
                 vid="0-5s: In a narrow valley the soldiers turn, clash briefly with Ming riders, then fall back again on the officer's signal. 5-10s: The viewer, raising his shield, mutters: \"Đánh được thì lại không cho đánh. Chạy mãi thế này người ta tưởng mình sợ thật.\"",
                 subs=[(5.0, 9.8, "Đánh được thì lại không cho đánh. / Chạy mãi thế này người ta tưởng mình sợ thật.")]),
            dict(name="Giặc cười", label="Chiều",
                 img="First-person view looking back from a mountain path at a Ming general in ornate armor on a horse laughing and pointing forward, leading about a hundred cavalry ahead of his army, limestone cliffs on both sides, realistic, vertical 9:16.",
                 vid="0-5s: The viewer looks back: a Ming general in ornate armor rides ahead of his army with about a hundred horsemen, laughing and pointing at the fleeing soldiers. 5-10s: The soldier beside the viewer grumbles: \"Nó cười mình kìa. Chạy cả ngày rồi mà vẫn chưa được đánh!\"",
                 subs=[(5.0, 9.8, "Nó cười mình kìa. / Chạy cả ngày rồi mà vẫn chưa được đánh!")]),
            dict(name="Vào ải", tiktok="bo", label="Ải Chi Lăng",
                 img="First-person view running into a narrow pass between steep limestone cliffs covered with dense forest, eerily quiet, the viewer glancing up at the cliffs, Ming cavalry following behind, realistic, vertical 9:16.",
                 vid="0-5s: The soldiers run into a narrow pass between steep, forested limestone cliffs; suddenly it is eerily quiet, no birds. 5-10s: The viewer glances up at the cliffs and notices the tip of a spear glinting among the leaves; he swallows and keeps running.",
                 subs=[]),
            dict(name="Đến ải mới hiểu", label="Ngay sau đó",
                 img="First-person view in a narrow mountain pass, hundreds of Lam Sơn soldiers rising from hiding on both forested cliffsides with crossbows and banners, the Ming cavalry trapped below, the officer finally turning around with a grin, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; hundreds of hidden soldiers rise from both cliffsides with crossbows and banners; the Ming cavalry below is trapped in the pass. 5-10s: The officer finally turns around, grinning at the exhausted viewer: \"Chạy xong rồi. Giờ thì quay lại mà đánh!\"",
                 subs=[(5.0, 9.8, "Chạy xong rồi. / Giờ thì quay lại mà đánh!")]),
        ],
        caption=("Được lệnh chạy thua cả ngày mà không ai nói vì sao, đến ải Chi Lăng mới hiểu 😤 Năm 1427, Trần Lựu "
                 "giả thua nhử Liễu Thăng vào ải Chi Lăng, nơi quân Lam Sơn mai phục sẵn. Bạn chịu được mấy tiếng bị "
                 "giặc cười mà không quay lại đánh? 👇"),
        tags="#chilang #leloi #lamson #1427",
    ),
    # ------------------------------------------------------------------ 1785
    dict(
        slug="nap-rach-gam-1785", prefix="nbt5",
        title="Nấp trong rạch cả đêm, bị cấm ho cấm đập muỗi, sáng ra mới hiểu",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** tháng 1 năm 1785, Nguyễn Huệ cho quân Tây Sơn mai phục trên khúc sông Tiền giữa rạch "
                 "Gầm và rạch Xoài Mút (Tiền Giang ngày nay). Khi thủy quân Xiêm kéo vào trận địa, quân Tây Sơn từ các "
                 "rạch và cù lao đổ ra đánh, thủy quân Xiêm gần như bị tiêu diệt. Các nguồn ghi ngày (19 hoặc 20/1/1785) "
                 "và quân số khác nhau, nên tập phim không nêu con số. **Hư cấu:** người lính, chuyện muỗi và mọi lời thoại."),
        setting=("Vietnam, Tây Sơn period, January 1785, the Tiền River in the Mekong Delta: wide brown river, narrow "
                 "side creeks overhung with nipa palms and mangroves, river islets, night mist. Tây Sơn soldiers in "
                 "plain brown and dark-red clothes with red head wraps, hiding in small boats inside the creeks; Siamese "
                 "warships with tall sails on the main river; Nguyễn Huệ, a strong commander around 30 with a fierce "
                 "gaze, seen briefly."),
        hook="Nấp trong rạch cả đêm / bị cấm ho, cấm đập muỗi",
        end="Sáng hôm ấy sông Tiền ra sao? / Follow để xem tập sau →",
        clips=[
            dict(name="Lệnh im lặng", label="Sông Tiền · tháng 1 năm 1785",
                 img="First-person close-up at night of the viewer's hands holding a paddle still in a small boat hidden under nipa palm leaves in a narrow creek, a mosquito landing on the back of the hand, other soldiers crouched silently, realistic, vertical 9:16.",
                 vid="0-5s: Close-up at night: the viewer's hand grips a paddle in a small boat hidden under nipa palms; an officer crawls past whispering: \"Cấm nói, cấm ho, cấm đập muỗi. Ai động là chết cả rạch.\" 5-10s: A mosquito lands on the back of the viewer's hand; he stares at it, trembling, but does not move.",
                 subs=[(0.5, 4.8, "Cấm nói, cấm ho, cấm đập muỗi. / Ai động là chết cả rạch.")]),
            dict(name="Muỗi miền Tây", tiktok="bo", label="Nửa đêm",
                 img="First-person view in a dark creek under nipa palms, soldiers in small boats sitting perfectly still, faces covered with mosquito bites, one soldier with his cheeks puffed out holding in a cough, realistic, vertical 9:16.",
                 vid="0-5s: Midnight; clouds of mosquitoes hum around the motionless soldiers; one soldier's cheeks puff out as he desperately holds in a cough. 5-10s: The soldier next to the viewer whispers through clenched teeth: \"Giặc chưa thấy đâu, muỗi đã đánh mình tan tác rồi...\"",
                 subs=[(5.0, 9.8, "Giặc chưa thấy đâu, / muỗi đã đánh mình tan tác rồi...")]),
            dict(name="Không ai nói gì", label="Gần sáng",
                 img="First-person view at dawn through nipa palm leaves, a soldier with a swollen, bitten face looking at the viewer with a pleading expression, mist on the creek, realistic, vertical 9:16.",
                 vid="0-5s: Near dawn, the soldier beside the viewer, his face swollen with bites, whispers: \"Cả đêm ngồi im cho muỗi ăn, mà chẳng ai nói chờ cái gì.\" 5-10s: Through the leaves, the viewer sees the dark shapes of tall sails slowly gliding along the main river in the mist.",
                 subs=[(0.5, 4.8, "Cả đêm ngồi im cho muỗi ăn, / mà chẳng ai nói chờ cái gì.")]),
            dict(name="Thuyền Xiêm vào", tiktok="bo", label="Rạng sáng",
                 img="First-person view peeking out from a hidden creek at a long line of Siamese warships with tall sails sailing past on a wide misty river, very close, soldiers on deck unaware, realistic, vertical 9:16.",
                 vid="0-5s: A long line of Siamese warships glides past the mouth of the creek, so close the viewer can hear the sailors talking on deck, unaware. 5-10s: Every soldier in the creek holds his breath; a mosquito lands on the officer's nose and he doesn't even blink.",
                 subs=[]),
            dict(name="Sáng ra mới hiểu", label="Ngay sau đó",
                 img="First-person view from a small boat bursting out of a creek onto a wide river at dawn, dozens of Tây Sơn boats charging from creeks and islets on both sides, drums, the trapped Siamese fleet in the middle, realistic, vertical 9:16.",
                 vid="0-5s: A drum booms; boats burst out of every creek and islet on both banks at once, trapping the Siamese fleet in the middle of the river. 5-10s: Paddling hard, the viewer finally slaps the mosquito on his arm with a loud smack and shouts: \"Giờ thì đập được rồi!\"",
                 subs=[(5.0, 9.5, "Giờ thì đập được rồi!")]),
        ],
        caption=("Nấp trong rạch cả đêm, bị cấm ho cấm đập muỗi, sáng ra mới hiểu 🦟 Tháng 1 năm 1785, quân Tây Sơn "
                 "của Nguyễn Huệ mai phục ở khúc sông Tiền giữa Rạch Gầm và Xoài Mút, đánh tan thủy quân Xiêm. Bạn "
                 "nhịn được mấy con muỗi? 👇"),
        tags="#rachgamxoaimut #nguyenhue #tayson #1785",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#povnguoibinhthuong",
          note=NOTE, unit="Tập", file_unit="tap")
