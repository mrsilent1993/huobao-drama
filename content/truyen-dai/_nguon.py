#!/usr/bin/env python3
"""Nguồn của loạt "Truyện xưa bản dài" (45–60 giây). Sửa ở đây rồi chạy: python3 _nguon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

VAN_LANG = ("Ancient Vietnam, Hùng king era (Văn Lang): people with hair in topknots or cut short, black-lacquered "
            "teeth, brown and indigo woven clothes, loincloths for poor men, bronze bracelets, feather headdresses for "
            "nobles; thatched stilt houses, bronze drums, wooden boats.")

EPISODES = [
    # ------------------------------------------------------------------ 1
    dict(
        slug="chu-dong-tu", prefix="cdt", title="Bạn hầu công chúa Tiên Dung đi tắm",
        length="60 giây · 6 clip (truyện có nhiều khúc: gặp gỡ, cưới, bị vua giận, thành tiên)",
        history=("**Truyền thuyết:** Chử Đồng Tử nghèo đến mức hai cha con chỉ có chung một cái khố. Khi cha mất, "
                 "chàng mặc khố cho cha rồi chôn, còn mình thì không có gì che thân. Một hôm công chúa Tiên Dung, con "
                 "vua Hùng thứ 18, dạo thuyền đến bãi Chử Xá, quây màn tắm đúng chỗ Chử Đồng Tử vùi mình dưới cát để "
                 "trốn. Nước dội trôi cát, hai người gặp nhau. Công chúa cho là duyên trời và kết làm vợ chồng. Vua giận "
                 "không cho về cung. Về sau hai người học đạo, và cả thành của họ bay lên trời chỉ trong một đêm. Chỗ đất "
                 "sụt thành đầm Nhất Dạ (Dạ Trạch, Hưng Yên). Đây là truyện truyền thuyết."),
        setting=(f"{VAN_LANG} A wide sandy riverbank of the Red River with reeds; a royal dragon boat with feather "
                 "banners; Princess Tiên Dung is a graceful young woman around 18 with long hair, a white-and-gold "
                 "dress and a feather hairpin; Chử Đồng Tử is a skinny, kind-faced young fisherman around 20; palace "
                 "maids in brown dresses (the viewer is one of them)."),
        hook="POV: Bạn hầu công chúa Tiên Dung / đi tắm ở bãi sông",
        end="Cả thành bay lên trời trong một đêm, / người hầu ở lại ra sao? / Follow để xem mai bạn / đúc ngựa sắt cho Thánh Gióng →",
        clips=[
            dict(name="Quây màn", label="Bãi Chử Xá · đời Hùng Vương thứ 18",
                 img="First-person view of a palace maid on a wide sandy riverbank with reeds in ancient Vietnam, the viewer's hands holding up a long cloth curtain on bamboo poles around a clump of reeds, a graceful princess in a white-and-gold dress stepping off a royal dragon boat, realistic, vertical 9:16.",
                 vid="0-5s: The royal dragon boat lands; Princess Tiên Dung looks around the empty sandy bank and says: \"Bãi cát đẹp quá. Quây màn chỗ bụi lau kia cho ta tắm.\" 5-10s: The viewer and another maid stretch a long curtain around the reeds; the other maid grumbles: \"Bãi hoang thế này có ma nào đâu mà phải quây kín thế không biết.\"",
                 subs=[(0.5, 4.8, "Bãi cát đẹp quá. / Quây màn chỗ bụi lau kia cho ta tắm."),
                       (5.0, 9.8, "Bãi hoang thế này có ma nào đâu / mà phải quây kín thế không biết.")]),
            dict(name="Dưới cát có người", label="Vài phút sau",
                 img="First-person view inside a cloth curtain enclosure on a sandy riverbank in ancient Vietnam, the viewer's hands pouring water from a clay jar onto the sand, the sand washing away to reveal a young man's face and shoulders buried underneath, eyes wide open in shock, realistic, PG, vertical 9:16.",
                 vid="0-5s: The viewer pours water from a clay jar onto the sand inside the curtain; the sand washes away and reveals a young man's face and bare shoulders buried underneath, his eyes wide open, staring back. 5-10s: The viewer screams and drops the jar: \"Á! Dưới cát có người!\" The young man, still half buried, says weakly: \"Dạ... con chào cô ạ.\"",
                 subs=[(5.0, 7.5, "Á! Dưới cát có người!"),
                       (7.5, 9.8, "Dạ... con chào cô ạ.")]),
            dict(name="Chung một cái khố", label="Bãi Chử Xá · ít phút sau",
                 img="First-person view on a sandy riverbank in ancient Vietnam, a skinny young fisherman sitting in a shallow sand pit holding a huge banana leaf in front of himself, embarrassed, palace maids staring with hands over their mouths, realistic, PG, vertical 9:16.",
                 vid="0-5s: The young man, holding a huge banana leaf in front of himself, explains with a red face: \"Nhà con nghèo, hai cha con chung một cái khố. Cha mất, con mặc khố cho cha rồi...\" 5-10s: The viewer repeats in disbelief: \"Chung... một cái khố?!\" The other maid slowly turns away, shoulders shaking with laughter.",
                 subs=[(0.5, 4.8, "Nhà con nghèo, hai cha con chung một cái khố. / Cha mất, con mặc khố cho cha rồi..."),
                       (5.0, 9.8, "Chung... một cái khố?!")]),
            dict(name="Duyên trời", label="Một lúc sau",
                 img="First-person view on a sandy riverbank in ancient Vietnam, a graceful princess in a white-and-gold dress holding the hand of a skinny young fisherman wrapped in a borrowed cloth, palace maids frozen in shock, realistic, vertical 9:16.",
                 vid="0-5s: Princess Tiên Dung looks at the young man for a long time, then takes his hand and says calmly: \"Ta quây màn đúng chỗ chàng nằm. Đây là duyên trời, ta với chàng thành vợ chồng.\" 5-10s: The viewer whispers to the other maid in shock: \"Công chúa cưới người... không có khố à?\" The princess, without turning: \"Thì may cho chàng một cái.\"",
                 subs=[(0.5, 4.8, "Ta quây màn đúng chỗ chàng nằm. / Đây là duyên trời, ta với chàng thành vợ chồng."),
                       (5.0, 7.5, "Công chúa cưới người... không có khố à?"),
                       (7.5, 9.8, "Thì may cho chàng một cái.")]),
            dict(name="Từ không khố thành giàu nhất vùng", label="Vài năm sau",
                 img="First-person view of a busy riverside market town in ancient Vietnam, the young couple now dressed richly greeting traders, boats loaded with goods, the palace maid carrying a basket of coins, realistic, vertical 9:16.",
                 vid="0-5s: A messenger from the palace shouts: \"Vua Hùng giận, không cho công chúa về cung nữa!\" The princess just shrugs. 5-10s: Years later, a bustling riverside market; the couple, now richly dressed, greet traders; the viewer, carrying a heavy basket of coins, mutters: \"Từ không có cái khố mà giờ giàu nhất vùng...\"",
                 subs=[(0.5, 4.8, "Vua Hùng giận, / không cho công chúa về cung nữa!"),
                       (5.0, 9.8, "Từ không có cái khố / mà giờ giàu nhất vùng...")]),
            dict(name="Thành bay lên trời", label="Một đêm",
                 img="First-person view at night on open ground in ancient Vietnam, looking up at an entire glowing town with houses and gates rising into the sky among clouds and light, wind blowing, the palace maid left alone on the ground with a basket, realistic, vertical 9:16.",
                 vid="0-5s: Night, a strong wind; the viewer runs out of a storehouse holding a basket and stops: the whole glowing town, houses, gates and all, is slowly rising into the sky among the clouds. 5-10s: The ground where the town stood sinks into dark water; the viewer, left alone on the shore, shouts up at the sky: \"Ơ... còn con thì sao ạ?!\"",
                 subs=[(5.0, 9.5, "Ơ... còn con thì sao ạ?!")]),
        ],
        caption="Đi hầu công chúa tắm thì dội nước trúng... một người dưới cát 😳 Truyền thuyết Chử Đồng Tử và Tiên Dung: nghèo đến mức hai cha con chung một cái khố, rồi thành tiên bay lên trời trong một đêm, nơi ấy thành đầm Nhất Dạ. Bạn nghĩ người hầu còn lại đã đi đâu? 👇",
        tags="#chudongtu #tiendung #truyenthuyet #damnhatda",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="thanh-giong", prefix="tg", title="Bạn đúc ngựa sắt cho Thánh Gióng",
        length="60 giây · 6 clip (từ lúc biết nói đến lúc bay về trời)",
        history=("**Truyền thuyết:** đời Hùng Vương thứ 6, giặc Ân sang xâm lược. Ở làng Phù Đổng có cậu bé lên ba "
                 "chưa biết nói, nghe sứ giả rao tìm người tài thì bỗng nói, xin vua đúc ngựa sắt, roi sắt, áo giáp sắt. "
                 "Cậu lớn nhanh như thổi, cả làng góp gạo nuôi. Khi ngựa sắt đúc xong, cậu vươn vai thành tráng sĩ, ngựa "
                 "phun lửa, roi gãy thì nhổ tre đánh giặc. Thắng giặc, Gióng phi ngựa lên núi Sóc rồi bay về trời. Hội "
                 "Gióng ở đền Phù Đổng và đền Sóc là di sản văn hóa phi vật thể của nhân loại (UNESCO)."),
        setting=(f"{VAN_LANG} The village of Phù Đổng with bamboo hedges and thatched houses; a royal herald with a "
                 "bronze drum; the village blacksmith's forge with clay furnaces and bellows (the viewer is a young "
                 "blacksmith); Gióng first as a 3-year-old boy, then a giant young warrior in iron armor on a huge iron "
                 "horse; Mẹ Gióng is a thin peasant woman around 45."),
        hook="POV: Bạn là thợ rèn / đúc ngựa sắt cho Thánh Gióng",
        end="Ngựa bay rồi, lò rèn ai trả tiền? / Follow để xem mai bạn ra đảo hoang / cùng Mai An Tiêm →",
        clips=[
            dict(name="Cậu bé ba tuổi biết nói", label="Làng Phù Đổng · đời Hùng Vương thứ 6",
                 img="First-person view in a dirt yard of an ancient Vietnamese village, a royal herald beating a bronze drum, villagers gathered, a thin peasant mother holding a 3-year-old boy who is pointing at the herald with a serious face, realistic, vertical 9:16.",
                 vid="0-5s: A royal herald beats a bronze drum and shouts: \"Giặc Ân sang! Ai đánh được giặc, vua ban thưởng!\" 5-10s: In his mother's arms, a 3-year-old boy suddenly points at the herald and says clearly, in a deep serious voice: \"Về tâu vua đúc cho ta một con ngựa sắt, một roi sắt, một áo giáp sắt!\" The whole crowd freezes.",
                 subs=[(0.5, 4.8, "Giặc Ân sang! / Ai đánh được giặc, vua ban thưởng!"),
                       (5.0, 9.8, "Về tâu vua đúc cho ta một con ngựa sắt, / một roi sắt, một áo giáp sắt!")]),
            dict(name="Đơn hàng rõ ràng", label="Một lúc sau",
                 img="First-person view in a village yard in ancient Vietnam, the viewer (a young blacksmith with a leather apron) staring at a 3-year-old boy sitting on a bamboo cot, the mother looking stunned, the herald writing on a bamboo slip, realistic, vertical 9:16.",
                 vid="0-5s: The mother stares at her son, stunned: \"Ba năm nay nó chưa nói câu nào, giờ nói một câu là đặt hàng luôn!\" 5-10s: The herald turns to the viewer, the village blacksmith, and hands him a bamboo slip: \"Lò rèn làng này nhận đơn đi.\" The viewer reads it and gulps: \"Ba tuổi mà đặt hàng rõ ràng thế...\"",
                 subs=[(0.5, 4.8, "Ba năm nay nó chưa nói câu nào, / giờ nói một câu là đặt hàng luôn!"),
                       (5.0, 7.5, "Lò rèn làng này nhận đơn đi."),
                       (7.5, 9.8, "Ba tuổi mà đặt hàng rõ ràng thế...")]),
            dict(name="Cả làng nuôi cơm", label="Mấy hôm sau",
                 img="First-person view at the door of a thatched house in ancient Vietnam, villagers lined up carrying pots of rice and baskets of eggplant, a boy who is suddenly the size of a teenager eating from a huge pot, his small clothes torn at the seams, realistic, vertical 9:16.",
                 vid="0-5s: A line of villagers carries pots of rice and baskets of eggplant into the house; inside, the boy, already as big as a teenager, eats a whole pot in one go, his clothes tearing at the seams. 5-10s: A neighbor sets down another pot and complains to the viewer: \"Nhà tôi góp bảy nồi rồi đấy! Ăn thế này lò rèn của anh làm nhanh lên!\"",
                 subs=[(5.0, 9.8, "Nhà tôi góp bảy nồi rồi đấy! / Ăn thế này lò rèn của anh làm nhanh lên!")]),
            dict(name="Đúc ngựa sắt", label="Lò rèn làng",
                 img="First-person view in a hot village blacksmith forge in ancient Vietnam, glowing furnaces, the viewer's hands hammering a huge iron horse's leg, a massive iron horse half finished, sparks flying, an old master smith wiping sweat, realistic, vertical 9:16.",
                 vid="0-5s: Sparks fly as the viewer hammers the leg of a gigantic iron horse; the old master smith wipes his sweat and asks: \"Ngựa nặng cả nghìn cân, đứa nào cưỡi nổi?\" 5-10s: The viewer keeps hammering and answers: \"Đơn của thằng bé ba tuổi đấy bác ạ.\" The master stops, looks at the giant horse, then at the viewer, speechless.",
                 subs=[(0.5, 4.8, "Ngựa nặng cả nghìn cân, / đứa nào cưỡi nổi?"),
                       (5.0, 9.8, "Đơn của thằng bé ba tuổi đấy bác ạ.")]),
            dict(name="Vươn vai", label="Ngày giao hàng",
                 img="First-person view in a village yard in ancient Vietnam, a giant young warrior in shining iron armor standing up taller than the bamboo, mounting a huge iron horse whose mouth spews flames, villagers falling back, realistic, vertical 9:16.",
                 vid="0-5s: The boy stands up, stretches, and grows into a giant warrior taller than the bamboo; he puts on the iron armor and leaps onto the iron horse; the horse roars and spews fire from its mouth. 5-10s: The viewer falls back on the ground, staring, and shouts: \"Ơ! Tôi đâu có lắp cái phun lửa!\"",
                 subs=[(5.0, 9.5, "Ơ! Tôi đâu có lắp cái phun lửa!")]),
            dict(name="Nhổ tre, bay về trời", label="Sau trận đánh",
                 img="First-person view at the foot of a mountain in ancient Vietnam, a giant warrior on an iron horse rising into the sky from the mountain top among clouds, burnt bamboo groves below, the young blacksmith waving from the ground, realistic, vertical 9:16.",
                 vid="0-5s: Far away, the giant warrior's iron whip snaps; he rips out whole bamboo clumps and sweeps the enemy away; then he rides up to the mountain top, and horse and rider rise into the sky among the clouds. 5-10s: The viewer runs to the foot of the mountain, waving a bamboo slip, and shouts at the sky: \"Ngựa với roi chưa thanh toán đâu đấy!\"",
                 subs=[(5.0, 9.5, "Ngựa với roi / chưa thanh toán đâu đấy!")]),
        ],
        caption="Thằng bé ba tuổi nói câu đầu tiên là đặt hàng ngựa sắt, và ngựa giao xong thì... phun lửa 🔥 Truyền thuyết Thánh Gióng, cậu bé làng Phù Đổng đánh tan giặc Ân rồi bay về trời từ núi Sóc. Hội Gióng nay là di sản văn hóa phi vật thể của nhân loại. Bạn đã đi hội Gióng bao giờ chưa? 👇",
        tags="#thanhgiong #phudong #truyenthuyet #hoigiong",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug="mai-an-tiem", prefix="mat", title="Bạn theo Mai An Tiêm ra đảo hoang",
        length="50 giây · 5 clip (bị đày, sinh tồn, tìm ra dưa hấu, được đón về)",
        history=("**Truyền thuyết:** Mai An Tiêm là con nuôi vua Hùng. Vì nói câu \"Của biếu là của lo, của cho là "
                 "của nợ\" (ý là của cải phải do sức mình làm ra), ông bị vua giận, đày ra đảo hoang. Một hôm thấy chim "
                 "thả hạt, ông đem trồng, được thứ quả vỏ xanh, ruột đỏ, hạt đen, ăn ngọt mát: đó là quả dưa hấu. Ông "
                 "khắc tên lên quả rồi thả xuống biển, người đất liền vớt được. Vua biết chuyện, hối hận và cho đón về. "
                 "Đây là truyện truyền thuyết."),
        setting=(f"{VAN_LANG} First a royal hall with a feast; then a deserted sandy island with rocks, wild grass and "
                 "the open sea. Mai An Tiêm is a calm, stubborn man around 35 with a topknot and a plain brown tunic; "
                 "the Hùng king is an old man with a feather crown; the viewer is his loyal servant."),
        hook="POV: Bạn theo Mai An Tiêm / ra đảo hoang",
        end="Về đất liền, ông có bớt nói không? / Follow để xem mai bạn khuân đá / giúp trạng cân voi →",
        clips=[
            dict(name="Một câu nói", label="Hoàng cung · đời Hùng Vương",
                 img="First-person view of a servant kneeling at a royal feast in an ancient Vietnamese hall, a calm man around 35 with a topknot raising a cup and speaking, an old king with a feather crown frowning at him, guests holding gifts, realistic, vertical 9:16.",
                 vid="0-5s: At the royal feast, guests flatter Mai An Tiêm about the gifts the king gave him; he raises his cup and says calmly: \"Của biếu là của lo, của cho là của nợ.\" 5-10s: The old king slams down his cup: \"Đã thế ra đảo hoang mà sống bằng sức mình!\" The viewer, kneeling behind, whispers: \"Ông chủ ơi... nói ít thôi ạ...\"",
                 subs=[(0.5, 4.8, "Của biếu là của lo, / của cho là của nợ."),
                       (5.0, 7.5, "Đã thế ra đảo hoang / mà sống bằng sức mình!"),
                       (7.5, 9.8, "Ông chủ ơi... nói ít thôi ạ...")]),
            dict(name="Đảo hoang", label="Đảo hoang ngoài biển",
                 img="First-person view on a deserted sandy island with rocks and wild grass in ancient times, a boat sailing away into the distance, a calm man with a topknot already chopping driftwood with a stone axe, realistic, vertical 9:16.",
                 vid="0-5s: The boat that brought them sails away; the viewer looks around the empty rocky island in despair and says: \"Đảo không có gì ăn, ông chủ còn câu nào hay nữa không ạ?\" 5-10s: Mai An Tiêm calmly keeps chopping driftwood and says: \"Có tay thì có ăn. Đi nhặt củi.\"",
                 subs=[(0.5, 4.8, "Đảo không có gì ăn, / ông chủ còn câu nào hay nữa không ạ?"),
                       (5.0, 9.5, "Có tay thì có ăn. Đi nhặt củi.")]),
            dict(name="Hạt của chim", label="Vài tháng sau",
                 img="First-person view on a sandy island, a flock of birds flying overhead dropping small black seeds onto the sand, a calm man with a topknot crouching and picking up the seeds, realistic, vertical 9:16.",
                 vid="0-5s: A flock of birds flies over and drops small black seeds on the sand; Mai An Tiêm picks some up and says: \"Chim ăn được thì người ăn được. Trồng!\" 5-10s: The viewer frowns: \"Nhỡ chim ăn được mà người không ăn được thì sao ạ?\" Mai An Tiêm hands him a digging stick without a word.",
                 subs=[(0.5, 4.8, "Chim ăn được thì người ăn được. Trồng!"),
                       (5.0, 9.8, "Nhỡ chim ăn được / mà người không ăn được thì sao ạ?")]),
            dict(name="Dưa hấu", label="Mùa thu hoạch",
                 img="First-person view on an island field of green striped round melons, the viewer's hands holding a split melon showing bright red flesh and black seeds, a calm man with a topknot carving a name onto another melon's rind, realistic, vertical 9:16.",
                 vid="0-5s: The viewer splits open a big green melon: bright red flesh and black seeds; he bites it and his eyes widen: \"Ngọt! Ngọt quá ông chủ ơi!\" 5-10s: Mai An Tiêm carves his name into the rind of several melons and rolls them into the sea; the viewer asks: \"Gửi qua đường biển không ghi địa chỉ à ông?\" He answers: \"Ghi tên là đủ.\"",
                 subs=[(0.5, 4.8, "Ngọt! Ngọt quá ông chủ ơi!"),
                       (5.0, 7.5, "Gửi qua đường biển / không ghi địa chỉ à ông?"),
                       (7.5, 9.8, "Ghi tên là đủ.")]),
            dict(name="Thuyền vua đến đón", label="Một năm sau",
                 img="First-person view on the beach of an island, a royal boat with feather banners landing, the old king stepping down with open arms, a calm man with a topknot standing among piles of green melons, realistic, vertical 9:16.",
                 vid="0-5s: A royal boat lands; the old king steps onto the sand and says, moved: \"An Tiêm, ta biết lỗi rồi. Về thôi con.\" 5-10s: As Mai An Tiêm opens his mouth to answer, the viewer quickly whispers: \"Ông chủ, lần này về nhớ nói ít thôi!\" Mai An Tiêm smiles and starts: \"Của biếu là...\" and the viewer claps a hand over his mouth.",
                 subs=[(0.5, 4.8, "An Tiêm, ta biết lỗi rồi. Về thôi con."),
                       (5.0, 8.0, "Ông chủ, lần này về nhớ nói ít thôi!"),
                       (8.0, 9.8, "Của biếu là...")]),
        ],
        caption="Bị đày ra đảo hoang chỉ vì một câu nói, ông chủ vẫn không bớt nói 😂 Truyền thuyết Mai An Tiêm và quả dưa hấu: vỏ xanh, ruột đỏ, hạt đen, được gửi về đất liền qua đường biển. Bạn hiểu câu \"Của biếu là của lo, của cho là của nợ\" thế nào? 👇",
        tags="#maiantiem #duahau #truyenthuyet #sutichduahau",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        slug="luong-the-vinh", prefix="ltv", title="Bạn khuân đá giúp trạng Lương Thế Vinh cân voi",
        length="50 giây · 5 clip (đề bài, cách làm, khuân đá, ra kết quả, câu đố thêm)",
        history=("**Lịch sử và giai thoại:** Lương Thế Vinh đỗ Trạng nguyên năm 1463 đời vua Lê Thánh Tông, giỏi "
                 "toán, được gọi là \"Trạng Lường\" và được cho là tác giả sách toán *Đại thành toán pháp*. Giai thoại "
                 "kể sứ nhà Minh thách cân một con voi. Ông cho dắt voi xuống thuyền, vạch mực nước, rồi dắt voi lên và "
                 "chất đá xuống đến đúng vạch, cân số đá ấy là ra sức nặng con voi. Giai thoại cũng kể ông đo được độ dày "
                 "một tờ giấy bằng cách đo cả quyển sách rồi chia cho số tờ."),
        setting=("Vietnam, Lê dynasty, around 1470, Thăng Long. A riverbank with a large wooden boat; a big grey "
                 "elephant with a mahout; Lương Thế Vinh is a cheerful, clever scholar around 30 in a dark blue official "
                 "robe and black hat; the Ming envoy is a tall, arrogant official in a rich red robe; Vietnamese "
                 "officials sweating nervously; workers in brown clothes (the viewer is one of them)."),
        hook="POV: Bạn khuân đá / giúp trạng Lương Thế Vinh cân voi",
        end="Sứ Tàu còn đố gì nữa? / Follow để xem tập sau →",
        clips=[
            dict(name="Đề bài của sứ", label="Thăng Long · đời Lê Thánh Tông",
                 img="First-person view in a courtyard in 15th-century Thăng Long, a tall arrogant Ming envoy in a red robe pointing at a big grey elephant, Vietnamese officials sweating, a cheerful scholar in a dark blue robe stepping forward with a smile, realistic, vertical 9:16.",
                 vid="0-5s: The tall Ming envoy points at a big grey elephant and sneers: \"Nước Nam có ai cân được con voi này không?\" The officials sweat and look at each other; nobody speaks. 5-10s: Lương Thế Vinh steps forward with a cheerful smile: \"Có gì khó. Ra bờ sông là xong.\" The viewer, a worker holding the elephant's rope, whispers: \"Cân voi ở bờ sông á?\"",
                 subs=[(0.5, 4.8, "Nước Nam có ai cân được / con voi này không?"),
                       (5.0, 7.5, "Có gì khó. Ra bờ sông là xong."),
                       (7.5, 9.8, "Cân voi ở bờ sông á?")]),
            dict(name="Voi xuống thuyền", label="Bờ sông",
                 img="First-person view on a riverbank, a big grey elephant standing on a large wooden boat which sinks low in the water, a cheerful scholar in a dark blue robe painting a black line on the side of the boat at the waterline, realistic, vertical 9:16.",
                 vid="0-5s: The elephant steps onto a large wooden boat, which sinks low in the water; Lương Thế Vinh paints a black line on the hull exactly at the waterline. 5-10s: The viewer, holding the rope, asks: \"Trạng ơi, trạng định cho voi đi tắm ạ?\" Lương Thế Vinh laughs: \"Voi xong việc rồi. Giờ đến lượt các anh.\"",
                 subs=[(5.0, 7.5, "Trạng ơi, trạng định cho voi đi tắm ạ?"),
                       (7.5, 9.8, "Voi xong việc rồi. / Giờ đến lượt các anh.")]),
            dict(name="Khuân đá", label="Cả buổi chiều",
                 img="First-person view of a worker carrying a heavy stone in his arms toward a large wooden boat on a riverbank, other workers carrying stones in a long line, the boat slowly sinking toward a painted black line, the sun getting low, realistic, vertical 9:16.",
                 vid="0-5s: Lương Thế Vinh points at the boat: \"Chất đá xuống thuyền, đến đúng vạch mực thì dừng.\" A long line of workers starts carrying stones. 5-10s: Hours later, sweating, the viewer drops another stone into the boat and groans: \"Người ta cân voi, mình cân cả quả núi!\" The waterline creeps toward the black mark.",
                 subs=[(0.5, 4.8, "Chất đá xuống thuyền, / đến đúng vạch mực thì dừng."),
                       (5.0, 9.8, "Người ta cân voi, / mình cân cả quả núi!")]),
            dict(name="Ra kết quả", label="Chiều tối",
                 img="First-person view on a riverbank at sunset, workers weighing stones one by one on a wooden steelyard scale, a cheerful scholar in a dark blue robe calculating quickly, the tall Ming envoy watching with a stiff face, realistic, vertical 9:16.",
                 vid="0-5s: The water touches the black line exactly; workers weigh each stone on a wooden steelyard scale while Lương Thế Vinh adds the numbers in his head, fingers flying. 5-10s: He turns to the envoy and announces the elephant's weight; the envoy's face stiffens; the Vietnamese officials burst out cheering.",
                 subs=[]),
            dict(name="Câu đố thêm", label="Ngay sau đó",
                 img="First-person view on a riverbank at dusk, the tall Ming envoy holding up a single thin sheet of paper with a challenging look, the cheerful scholar holding a thick book and smiling, exhausted workers sitting on the ground, realistic, vertical 9:16.",
                 vid="0-5s: The envoy, not giving up, holds up a single thin sheet of paper: \"Thế tờ giấy mỏng này dày bao nhiêu?\" Lương Thế Vinh picks up a whole book: \"Đo cả quyển, rồi chia cho số tờ.\" 5-10s: The viewer, collapsed on the ground among the stones, raises a hand weakly: \"Thôi trạng ơi... đừng ai đố thêm câu nào nữa...\"",
                 subs=[(0.5, 2.8, "Thế tờ giấy mỏng này dày bao nhiêu?"),
                       (2.8, 4.9, "Đo cả quyển, rồi chia cho số tờ."),
                       (5.0, 9.8, "Thôi trạng ơi... / đừng ai đố thêm câu nào nữa...")]),
        ],
        caption="Sứ Tàu thách cân con voi, trạng nghĩ ra cách trong một nốt nhạc, còn người khuân đá thì mệt cả buổi chiều 😂 Giai thoại Lương Thế Vinh, \"Trạng Lường\" giỏi toán nhất thời Lê. Nếu là bạn, bạn sẽ cân voi bằng cách nào? 👇",
        tags="#luongthevinh #tranglung #canvoi #toanhoc #nhale",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), unit="Tập", file_unit="tap")
