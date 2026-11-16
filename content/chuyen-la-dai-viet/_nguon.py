#!/usr/bin/env python3
"""Nguồn của loạt "Chuyện lạ Đại Việt" (50–60 giây). Sửa ở đây rồi chạy: python3 _nguon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

TRAN = ("Vietnam, late Trần dynasty: people with short cropped hair, black-lacquered teeth, brown and indigo clothes, "
        "barefoot commoners; officials in dark-red and blue robes with black hats; tiled-roof wooden houses, markets "
        "under banyan trees.")

EPISODES = [
    # ------------------------------------------------------------------ 1
    dict(
        slug="tien-giay-1396", prefix="cl1", title="Bạn đi chợ bằng tiền giấy năm 1396",
        length="50 giây · 5 clip (lệnh đổi tiền, đổi tiền, đi chợ, gặp mưa, chôn tiền đồng)",
        history=("**Lịch sử (độ tin cậy B):** theo *Đại Việt sử ký toàn thư*, năm 1396, dưới quyền Hồ Quý Ly, triều "
                 "đình phát hành tiền giấy **\"Thông bảo hội sao\"** và bắt dân đổi tiền đồng lấy tiền giấy. Ai làm giả "
                 "bị tội nặng. Mỗi mệnh giá vẽ một hình: tờ 10 đồng vẽ rong, 30 đồng vẽ sóng, 1 tiền vẽ mây, 2 tiền vẽ "
                 "rùa, 3 tiền vẽ lân, 5 tiền vẽ phượng, 1 quan vẽ rồng. Đây là tiền giấy đầu tiên của nước ta. Chuyện "
                 "dân lén cất tiền đồng trong tập là chi tiết dựng thêm để gây cười."),
        setting=(f"{TRAN} Year 1396, a village market and a small thatched house; a town crier official with a drum; "
                 "paper banknotes are rectangular sheets of coarse paper printed with simple pictures (a turtle, a "
                 "cloud, a dragon); old copper coins with square holes strung on cords; clay jars. The viewer is a young "
                 "villager; the fishmonger is a sharp-tongued woman around 55 with black teeth."),
        hook="POV: Bạn đi chợ bằng tiền giấy / năm 1396",
        end="Tiền giấy nhà Hồ dùng được bao lâu? / Follow để xem mai bạn cầm quả cam / cho Trần Quốc Toản →",
        clips=[
            dict(name="Lệnh đổi tiền", label="Năm 1396 · cổng làng",
                 img="First-person view at a village gate in 1396 Vietnam, an official in a dark-red robe beating a drum and holding up a paper banknote printed with a dragon, villagers crowding around, the viewer's arms hugging a heavy clay jar full of copper coins, realistic, vertical 9:16.",
                 vid="0-5s: An official beats a drum and holds up a sheet of paper printed with a dragon: \"Từ nay dùng tiền giấy! Ai còn giữ tiền đồng thì bị phạt!\" The crowd murmurs. 5-10s: The viewer hugs a heavy clay jar of copper coins tighter and whispers to a neighbor: \"Tiền mà làm bằng giấy... gió thổi bay thì sao?\"",
                 subs=[(0.5, 4.8, "Từ nay dùng tiền giấy! / Ai còn giữ tiền đồng thì bị phạt!"),
                       (5.0, 9.8, "Tiền mà làm bằng giấy... / gió thổi bay thì sao?")]),
            dict(name="Đổi tiền", label="Nhà quan · đổi tiền",
                 img="First-person view at a wooden counter in 1396 Vietnam, the viewer pouring a whole clay jar of copper coins onto the counter, a clerk handing back a thin stack of paper banknotes, realistic, vertical 9:16.",
                 vid="0-5s: The viewer pours a whole heavy jar of copper coins onto the counter with a loud clatter; the clerk counts, then hands back a thin stack of paper notes. 5-10s: The viewer weighs the paper in one hand, then looks at the mountain of coins: \"Cả hũ tiền đồng nặng trĩu, đổi được mấy tờ giấy nhẹ tênh...\"",
                 subs=[(5.0, 9.8, "Cả hũ tiền đồng nặng trĩu, / đổi được mấy tờ giấy nhẹ tênh...")]),
            dict(name="Mua cá bằng con rùa", label="Chợ phiên",
                 img="First-person view at a fish stall in a village market in 1396 Vietnam, a sharp-tongued old fishmonger with black teeth holding up a paper banknote printed with a turtle and squinting at it suspiciously, baskets of fish, realistic, vertical 9:16.",
                 vid="0-5s: The viewer hands a paper note printed with a turtle to the old fishmonger; she squints at it: \"Tờ giấy vẽ con rùa mà đòi mua con cá của tôi à?\" The viewer insists: \"Tờ con rùa là hai tiền đấy bà!\" 5-10s: She flips it over, unimpressed: \"Thế tờ vẽ con rồng thì mua được cả thuyền à?\" Customers around burst out laughing.",
                 subs=[(0.5, 2.8, "Tờ giấy vẽ con rùa / mà đòi mua con cá của tôi à?"),
                       (2.8, 4.9, "Tờ con rùa là hai tiền đấy bà!"),
                       (5.0, 9.8, "Thế tờ vẽ con rồng / thì mua được cả thuyền à?")]),
            dict(name="Mưa", label="Đường về · mưa rào",
                 img="First-person view in a small yard after rain in 1396 Vietnam, the viewer hanging wet paper banknotes on a string line like laundry with bamboo clips, a neighbor peeking over the fence, realistic, vertical 9:16.",
                 vid="0-5s: A sudden downpour on the way home; the viewer stuffs the paper notes under his shirt, but they are soaked. 5-10s: At home, the viewer hangs the wet banknotes on a string like laundry; the neighbor peeks over the fence and says: \"Nhà anh phơi tiền à? Giàu thế!\"",
                 subs=[(5.0, 9.5, "Nhà anh phơi tiền à? Giàu thế!")]),
            dict(name="Nửa đêm", label="Nửa đêm",
                 img="First-person view at night under a banana tree in a village yard, 1396, the viewer holding a small clay jar and a shovel, a neighbor caught in the act of burying his own jar of copper coins, both frozen, moonlight, realistic, vertical 9:16.",
                 vid="0-5s: Midnight; the viewer sneaks into the yard with a small clay jar and a shovel, and finds the neighbor already digging under the banana tree, burying his own jar of copper coins. 5-10s: They stare at each other's jars in silence; then both put a finger to their lips at the same time and whisper: \"Suỵt!\"",
                 subs=[(6.0, 9.5, "Suỵt!")]),
        ],
        caption="Đổi cả hũ tiền đồng lấy mấy tờ giấy vẽ con rùa, ra chợ bị bà bán cá hỏi vặn 😂 Năm 1396, nước ta phát hành tiền giấy \"Thông bảo hội sao\": tờ 1 quan vẽ rồng, tờ 2 tiền vẽ rùa. Nếu sống năm đó, bạn có dám dùng tiền giấy không? 👇",
        tags="#tiengiay #hoquyly #nhaho #chuyenla #1396",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="tran-quoc-toan", prefix="cl2", title="Bạn cầm quả cam cho Trần Quốc Toản",
        length="50 giây · 5 clip (không được dự bàn, bóp nát quả cam, tự mộ quân, thêu cờ, ra quân)",
        history=("**Lịch sử (độ tin cậy B):** năm 1282, vua Trần họp các vương hầu ở Bình Than bàn việc chống quân "
                 "Nguyên. Theo *Toàn thư*, Hoài Văn hầu **Trần Quốc Toản** khi ấy mới khoảng 15 tuổi, không được dự "
                 "bàn. Vua ban cho một quả cam, ông giận mà bóp nát lúc nào không biết. Về nhà, ông tập hợp gia nhân, "
                 "thân thuộc được hơn nghìn người, sắm vũ khí, đóng thuyền, giương cờ đề sáu chữ **\"Phá cường địch, "
                 "báo hoàng ân\"** (phá giặc mạnh, đền ơn vua)."),
        setting=(f"{TRAN} Year 1282, Bình Than wharf with royal boats and banners; then a noble's house with a "
                 "courtyard. Trần Quốc Toản is a fierce, proud 15-year-old boy in a dark blue noble's robe and small "
                 "black hat; the viewer is his slightly younger, nervous servant; guards in dark-red uniforms; household "
                 "servants and relatives."),
        hook="POV: Bạn là người hầu / của Trần Quốc Toản",
        end="Đội quân trẻ con ấy ra trận thế nào? / Follow để xem mai bạn cầm kim xăm / đuổi theo vua →",
        clips=[
            dict(name="Không được vào", label="Bến Bình Than · năm 1282",
                 img="First-person view at a busy riverside wharf with royal boats and banners in 1282 Vietnam, a proud 15-year-old boy in a dark blue noble's robe being stopped by two guards with crossed spears, the boy furious, realistic, vertical 9:16.",
                 vid="0-5s: At the wharf, two guards cross their spears in front of the proud 15-year-old boy; one says politely: \"Hầu còn nhỏ, chưa được dự bàn việc nước ạ.\" 5-10s: The boy turns red with anger; the viewer, behind him, whispers: \"Cậu ơi, thôi mình đứng ngoài nghe lỏm cũng được...\"",
                 subs=[(0.5, 4.8, "Hầu còn nhỏ, chưa được dự bàn việc nước ạ."),
                       (5.0, 9.8, "Cậu ơi, thôi mình đứng ngoài / nghe lỏm cũng được...")]),
            dict(name="Quả cam", label="Ít phút sau",
                 img="First-person view at a wharf in 1282 Vietnam, a furious 15-year-old noble boy squeezing an orange in his fist, juice dripping between his fingers, the nervous servant staring at it in shock, royal boats behind, realistic, vertical 9:16.",
                 vid="0-5s: A palace attendant hands the boy an orange: \"Vua ban cho hầu quả cam.\" The viewer whispers: \"Cậu ăn đi cho đỡ giận...\" 5-10s: Staring at the boats, the boy clenches his fist harder and harder; juice drips between his fingers. The viewer stares at it: \"Cậu ơi... cam vua ban... nát rồi kìa...\"",
                 subs=[(0.5, 2.8, "Vua ban cho hầu quả cam."),
                       (2.8, 4.9, "Cậu ăn đi cho đỡ giận..."),
                       (5.0, 9.8, "Cậu ơi... cam vua ban... nát rồi kìa...")]),
            dict(name="Tự mộ quân", label="Về nhà",
                 img="First-person view in the courtyard of a noble's house in 1282 Vietnam, a determined 15-year-old boy standing on a step addressing a crowd of household servants and relatives, the nervous servant at the front, realistic, vertical 9:16.",
                 vid="0-5s: In the courtyard, the boy stands on a step and declares: \"Người ta bảo ta nhỏ? Ta tự mộ quân đi đánh giặc!\" 5-10s: The viewer raises a hand timidly: \"Dạ... mộ quân lấy ai ạ?\" The boy points at the crowd of servants, cooks and cousins, then at the viewer: \"Cả nhà này. Cả mày nữa!\"",
                 subs=[(0.5, 4.8, "Người ta bảo ta nhỏ? / Ta tự mộ quân đi đánh giặc!"),
                       (5.0, 7.0, "Dạ... mộ quân lấy ai ạ?"),
                       (7.0, 9.8, "Cả nhà này. Cả mày nữa!")]),
            dict(name="Thêu cờ", label="Đêm hôm ấy",
                 img="First-person view at night by an oil lamp, the viewer's hands stitching large Chinese characters in yellow thread onto a big red flag, a 15-year-old noble boy watching over his shoulder, realistic, vertical 9:16.",
                 vid="0-5s: By an oil lamp, the viewer stitches big yellow characters onto a red flag while the boy recites: \"Phá cường địch, báo hoàng ân. Sáu chữ, thêu cho đẹp.\" 5-10s: The viewer holds up a tangled mess of thread and groans: \"Chữ 'địch' nhiều nét quá cậu ơi, em thêu thành con nhện rồi!\"",
                 subs=[(0.5, 4.8, "Phá cường địch, báo hoàng ân. / Sáu chữ, thêu cho đẹp."),
                       (5.0, 9.8, "Chữ \"địch\" nhiều nét quá cậu ơi, / em thêu thành con nhện rồi!")]),
            dict(name="Ra quân", label="Sáng hôm sau",
                 img="First-person view at dawn on a riverbank in 1282 Vietnam, a big red flag with yellow characters flying, a 15-year-old boy on a horse in armor, a long line of young servants and relatives with spears boarding boats, realistic, vertical 9:16.",
                 vid="0-5s: Dawn; the red flag with six characters flies high; the 15-year-old boy, now in armor on a horse, leads more than a thousand servants and relatives with spears toward the boats. 5-10s: The viewer, marching beside the horse, looks around at the young faces: \"Cậu mười lăm, em mười bốn, cả đội toàn trẻ con!\" The boy grins: \"Thì giặc càng coi thường ta!\"",
                 subs=[(5.0, 7.5, "Cậu mười lăm, em mười bốn, / cả đội toàn trẻ con!"),
                       (7.5, 9.8, "Thì giặc càng coi thường ta!")]),
        ],
        caption="Không được dự bàn việc nước vì còn nhỏ, cậu bóp nát quả cam vua ban rồi về tự mộ quân 🍊🔥 Trần Quốc Toản mới 15 tuổi đã giương cờ \"Phá cường địch, báo hoàng ân\". Năm 15 tuổi bạn đang làm gì? 👇",
        tags="#tranquoctoan #bopquacam #nhatran #1282",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug="vua-tron-xam-rong", prefix="cl3", title="Bạn cầm kim xăm đuổi theo vua Trần Anh Tông",
        length="50 giây · 5 clip (gia pháp, vua né, rượt đuổi, trốn, Thượng hoàng đến)",
        history=("**Lịch sử (độ tin cậy B):** nhà Trần gốc làm nghề sông nước. Theo *Toàn thư*, nhà Trần có lệ thích "
                 "(xăm) hình rồng lên đùi để tỏ ý không quên gốc. Thượng hoàng Trần Nhân Tông muốn xăm cho vua Trần Anh "
                 "Tông, nhưng vua tìm cách lánh đi, không chịu xăm. Người thợ xăm và cuộc rượt đuổi trong tập là chi "
                 "tiết dựng thêm để gây cười."),
        setting=(f"{TRAN} Around 1293–1300, the Thăng Long royal palace: lacquered red pillars, silk screens, long "
                 "corridors, a garden. Retired Emperor Trần Nhân Tông is a calm, wise man around 40 in a brown-and-"
                 "yellow robe; young Emperor Trần Anh Tông is around 18, clever and squeamish, in a yellow imperial robe; "
                 "the viewer is the palace tattoo master carrying a tray of needles and an ink bowl."),
        hook="POV: Bạn là thợ xăm trong cung / và vua thì sợ kim",
        end="Đời sau, vua Trần còn xăm rồng? / Follow để xem mai bạn giữ kho / nỏ thần Cổ Loa →",
        clips=[
            dict(name="Gia pháp", label="Hoàng cung Thăng Long · thời Trần",
                 img="First-person view in a royal palace hall with red lacquered pillars, a calm retired emperor in a brown-and-yellow robe speaking, a young emperor in a yellow robe listening uneasily, the viewer's hands holding a tray of fine needles and a bowl of black ink, realistic, vertical 9:16.",
                 vid="0-5s: The calm retired emperor says to the young emperor: \"Gia pháp nhà ta: con cháu phải xăm rồng ở đùi, để nhớ gốc làm nghề sông nước.\" 5-10s: He nods at the viewer, who steps forward with a tray of needles; the young emperor stares at the needles and swallows hard.",
                 subs=[(0.5, 4.8, "Gia pháp nhà ta: con cháu phải xăm rồng ở đùi, / để nhớ gốc làm nghề sông nước.")]),
            dict(name="Bận việc nước", label="Ít phút sau",
                 img="First-person view in a palace hall, a young emperor in a yellow robe backing away from a tray of needles with a forced smile, gesturing toward the door, realistic, vertical 9:16.",
                 vid="0-5s: The retired emperor leaves; the viewer bows: \"Mời bệ hạ ngồi, thần xăm nhẹ tay thôi ạ.\" 5-10s: The young emperor backs toward the door with a forced smile: \"Hôm nay trẫm... bận việc nước. Mai xăm.\" He slips out; the viewer stands alone holding the tray.",
                 subs=[(0.5, 4.8, "Mời bệ hạ ngồi, / thần xăm nhẹ tay thôi ạ."),
                       (5.0, 9.8, "Hôm nay trẫm... bận việc nước. / Mai xăm.")]),
            dict(name="Rượt đuổi", label="Hành lang hoàng cung",
                 img="First-person view running down a long palace corridor with red pillars, holding a tray of needles, the young emperor in a yellow robe running ahead and glancing back, startled maids stepping aside, realistic, vertical 9:16.",
                 vid="0-5s: The viewer runs down a long red-pillared corridor holding the needle tray, calling: \"Bệ hạ ơi! Thượng hoàng dặn phải xăm hôm nay ạ!\" 5-10s: Ahead, the young emperor lifts his robe and runs faster, glancing back; palace maids flatten themselves against the pillars as both race past.",
                 subs=[(0.5, 4.8, "Bệ hạ ơi! / Thượng hoàng dặn phải xăm hôm nay ạ!")]),
            dict(name="Thương lượng", label="Sau bình phong",
                 img="First-person view peeking behind a silk folding screen in a palace room, a young emperor in a yellow robe crouching there, holding up a brush and an ink stone with a hopeful expression, realistic, vertical 9:16.",
                 vid="0-5s: The viewer peeks behind a silk screen and finds the young emperor crouching there; the emperor holds up a brush: \"Hay là... vẽ bằng mực, rồi khai với Thượng hoàng là xăm rồi?\" 5-10s: The viewer, panting, answers: \"Bệ hạ ơi, mực vẽ thì tắm một lần là con rồng trôi mất ạ!\"",
                 subs=[(0.5, 4.8, "Hay là... vẽ bằng mực, / rồi khai với Thượng hoàng là xăm rồi?"),
                       (5.0, 9.8, "Mực vẽ thì tắm một lần / là con rồng trôi mất ạ!")]),
            dict(name="Thượng hoàng đến", label="Đúng lúc ấy",
                 img="First-person view in a palace room, the calm retired emperor standing in the doorway with arms behind his back, the young emperor and the tattoo master frozen behind a silk screen, realistic, vertical 9:16.",
                 vid="0-5s: Footsteps; the retired emperor appears in the doorway, arms behind his back; the young emperor and the viewer freeze behind the screen. 5-10s: The retired emperor looks at them for a long moment, then sighs and smiles: \"Thôi... đời nó khác đời ta.\" He turns and walks away; the viewer slowly lowers the needle tray.",
                 subs=[(5.0, 9.5, "Thôi... đời nó khác đời ta.")]),
        ],
        caption="Gia pháp nhà Trần là phải xăm rồng ở đùi, và vua Trần Anh Tông thì... sợ kim 😂 Theo Đại Việt sử ký toàn thư, nhà Trần có lệ xăm rồng để nhớ gốc làm nghề sông nước, nhưng vua Anh Tông đã lánh đi không chịu xăm. Bạn có dám đi xăm không? 👇",
        tags="#trananhtong #trannhantong #nhatran #chuyenla #xamrong",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        slug="no-than-co-loa", prefix="cl4", title="Bạn giữ kho nỏ thần thành Cổ Loa",
        length="60 giây · 6 clip (kho nỏ, phò mã hỏi han, đêm lén, chia tay, nỏ mất linh, lông ngỗng)",
        history=("**Truyền thuyết (độ tin cậy C) và khảo cổ (độ tin cậy A):** truyện An Dương Vương trong *Lĩnh Nam "
                 "chích quái* kể rùa vàng giúp vua xây thành Cổ Loa và cho móng làm lẫy nỏ thần. Triệu Đà cầu hòa, cho "
                 "con là Trọng Thủy lấy Mỵ Châu rồi đánh tráo lẫy nỏ. Khi giặc đánh, nỏ mất linh. Vua chạy, Mỵ Châu rắc "
                 "lông ngỗng dọc đường làm dấu, dẫn giặc đuổi theo. Về khảo cổ, thành Cổ Loa có nhiều vòng thành đất "
                 "còn đến nay. Năm 1959, người ta tìm thấy một kho lớn mũi tên đồng ở khu Cầu Vực, Cổ Loa."),
        setting=("Ancient Âu Lạc, around the 3rd–2nd century BC, Cổ Loa citadel: huge earthen ramparts in several rings "
                 "with wooden palisades, thatched halls, an armory with racks of large wooden crossbows and baskets of "
                 "bronze arrowheads. Soldiers with hair in topknots, bare chests, bronze axes and crossbows; Trọng Thủy is "
                 "a handsome, charming young man around 22 in a foreign-style dark robe; Mỵ Châu is a sweet, naive "
                 "princess around 18 with a feather cloak; the viewer is a young armory guard."),
        hook="POV: Bạn giữ kho nỏ thần / thành Cổ Loa",
        end="Lông ngỗng dẫn giặc đến đâu? / Follow để xem mai bạn đánh du kích / trong đầm Dạ Trạch →",
        clips=[
            dict(name="Kho nỏ thần", label="Thành Cổ Loa · nước Âu Lạc",
                 img="First-person view inside an ancient armory with racks of large wooden crossbows and baskets of bronze arrowheads, a glowing special crossbow on an altar in the center, a stern captain with a topknot pointing at it, realistic, vertical 9:16.",
                 vid="0-5s: Inside the armory, the stern captain points at a glowing crossbow on an altar: \"Nỏ thần bắn một phát chết trăm giặc. Canh cho kỹ, mất là mất nước!\" 5-10s: The viewer stands straight with a spear; the captain leaves; the viewer whispers to the crossbow: \"Mày ngoan nhé, đừng để tao mất việc.\"",
                 subs=[(0.5, 4.8, "Nỏ thần bắn một phát chết trăm giặc. / Canh cho kỹ, mất là mất nước!"),
                       (5.0, 9.8, "Mày ngoan nhé, đừng để tao mất việc.")]),
            dict(name="Phò mã hỏi han", label="Mấy hôm sau",
                 img="First-person view at an armory door, a handsome charming young man in a dark foreign-style robe leaning on the doorframe smiling and pointing at the glowing crossbow inside, the guard blocking with a spear, realistic, vertical 9:16.",
                 vid="0-5s: Trọng Thủy leans on the armory door with a charming smile: \"Lẫy nỏ thần làm bằng gì thế? Cho ta cầm thử chút thôi?\" 5-10s: The viewer blocks the door with his spear, smiling awkwardly: \"Phò mã... hôm nay hỏi kỹ quá ạ.\" Trọng Thủy laughs and walks off, glancing back at the crossbow.",
                 subs=[(0.5, 4.8, "Lẫy nỏ thần làm bằng gì thế? / Cho ta cầm thử chút thôi?"),
                       (5.0, 9.8, "Phò mã... hôm nay hỏi kỹ quá ạ.")]),
            dict(name="Đêm lén", label="Nửa đêm",
                 img="First-person view at night in an armory doorway lit by a single torch, a handsome young man in a dark robe sneaking out holding something small behind his back, the sleepy guard just waking up, realistic, vertical 9:16.",
                 vid="0-5s: The viewer dozes against the wall; a creak wakes him: Trọng Thủy is tiptoeing out of the armory, hiding something small behind his back. 5-10s: Trọng Thủy freezes, then smiles: \"Ta đi... dạo.\" The viewer rubs his eyes: \"Đi dạo... trong kho vũ khí ạ?\" Trọng Thủy is already gone.",
                 subs=[(5.0, 7.0, "Ta đi... dạo."),
                       (7.0, 9.8, "Đi dạo... trong kho vũ khí ạ?")]),
            dict(name="Chia tay", label="Sáng hôm sau · cổng thành",
                 img="First-person view at the gate of an ancient earthen citadel, a handsome young man on a horse saying goodbye to a sweet princess in a feather cloak, the guard standing nearby with a spear, realistic, vertical 9:16.",
                 vid="0-5s: At the gate, Trọng Thủy on horseback says to Mỵ Châu: \"Ta về thăm cha. Nếu có biến, nàng chạy đường nào?\" She answers sweetly: \"Thiếp sẽ rắc lông ngỗng ở ngã ba đường làm dấu.\" 5-10s: The viewer, standing guard, winces and whispers: \"Công chúa ơi... cái này... nói to quá...\"",
                 subs=[(0.5, 2.5, "Ta về thăm cha. / Nếu có biến, nàng chạy đường nào?"),
                       (2.5, 4.9, "Thiếp sẽ rắc lông ngỗng / ở ngã ba đường làm dấu."),
                       (5.0, 9.8, "Công chúa ơi... cái này... nói to quá...")]),
            dict(name="Nỏ mất linh", label="Ít lâu sau · giặc đến",
                 img="First-person view on top of an earthen rampart, the viewer aiming the special crossbow at an enemy army charging below, pulling the trigger with nothing happening, soldiers around panicking, smoke, realistic, vertical 9:16.",
                 vid="0-5s: Enemy drums; a huge army charges the ramparts; the viewer aims the glowing crossbow and pulls the trigger: the glow fades and nothing happens. 5-10s: He pulls again and again, then turns to the soldiers in horror: \"Nỏ thần... hết linh rồi!\" The ramparts erupt in panic.",
                 subs=[(5.0, 9.5, "Nỏ thần... hết linh rồi!")]),
            dict(name="Lông ngỗng", label="Trên đường chạy",
                 img="First-person view running along a dirt road out of an ancient citadel, white goose feathers scattered along the road and at every fork, the sound of horses behind, other fleeing soldiers, realistic, vertical 9:16.",
                 vid="0-5s: Fleeing along a dirt road with the king's party, the viewer looks down: white goose feathers are scattered all along the road, piled up at every fork. 5-10s: He stops, picks one up, hears hoofbeats getting closer behind them, and shouts: \"Ai... ai rắc lông ngỗng khắp đường thế này?!\"",
                 subs=[(5.0, 9.5, "Ai... ai rắc lông ngỗng / khắp đường thế này?!")]),
        ],
        caption="Phò mã hỏi han kho nỏ hơi nhiều, nửa đêm còn \"đi dạo\" trong kho vũ khí 🤨 Truyền thuyết nỏ thần và Mỵ Châu – Trọng Thủy. Còn khảo cổ thì có thật: năm 1959, một kho mũi tên đồng lớn được tìm thấy ở Cổ Loa. Nếu là lính gác, bạn có cho phò mã vào kho không? 👇",
        tags="#coloa #nothan #anduongvuong #mychau #trongthuy #truyenthuyet",
    ),
    # ------------------------------------------------------------------ 5
    dict(
        slug="da-trach-vuong", prefix="cl5", title="Bạn đánh du kích cùng Dạ Trạch Vương",
        length="50 giây · 5 clip (cấm khói bếp, cơm nguội, thuyền đêm, đánh úp, móng rồng)",
        history=("**Lịch sử (độ tin cậy B) và truyền thuyết (C):** thế kỷ 6, sau khi Lý Nam Đế thua quân Lương, Triệu "
                 "Quang Phục rút vào **đầm Dạ Trạch** (Hưng Yên). Theo *Toàn thư*, đầm rộng mênh mông, cỏ lau um tùm; "
                 "ban ngày tuyệt không có khói lửa, ban đêm dùng thuyền độc mộc ra đánh úp trại giặc, nên người đương "
                 "thời gọi ông là **Dạ Trạch Vương**. Truyền thuyết kể thần Chử Đồng Tử cưỡi rồng hiện về, trao cho ông "
                 "một móng rồng để cài lên mũ đâu mâu. Đầm Dạ Trạch cũng chính là đầm Nhất Dạ trong truyện Chử Đồng Tử."),
        setting=("Vietnam, mid-6th century, the vast Dạ Trạch swamp: endless tall reeds and marsh grass, narrow water "
                 "channels, a hidden island of high ground with small huts; dugout canoes. Fighters with short cropped "
                 "hair, black-lacquered teeth, simple brown clothes and leaf camouflage; Triệu Quang Phục is a calm, "
                 "sharp commander around 35 in simple dark armor; enemy Liang soldiers in heavy armor; the viewer is a "
                 "young fighter who loves to eat."),
        hook="POV: Bạn đánh du kích / trong đầm Dạ Trạch",
        end="Móng rồng ấy giúp ông thế nào? / Follow để xem tập sau →",
        clips=[
            dict(name="Cấm khói bếp", label="Đầm Dạ Trạch · thế kỷ 6",
                 img="First-person view on a hidden island in a vast reed swamp, the viewer crouching by a small clay stove about to light a fire, an officer in simple armor stamping it out urgently, tall reeds all around, realistic, vertical 9:16.",
                 vid="0-5s: The viewer crouches by a small clay stove and strikes a flint; the officer rushes over and stamps out the spark: \"Ban ngày cấm đỏ lửa! Khói bay lên là giặc biết chỗ!\" 5-10s: The viewer looks sadly at the pot of raw rice in his hands; somewhere in the reeds, his stomach growls.",
                 subs=[(0.5, 4.8, "Ban ngày cấm đỏ lửa! / Khói bay lên là giặc biết chỗ!")]),
            dict(name="Cơm nguội", label="Ngày thứ mười",
                 img="First-person view in a reed hut on a swamp island, a group of tired fighters eating cold rice balls in silence, the viewer holding a hard cold rice ball and looking miserable, realistic, vertical 9:16.",
                 vid="0-5s: Fighters sit in a reed hut chewing cold, hard rice balls in silence. 5-10s: The viewer stares at his rice ball and says, deeply serious: \"Đánh giặc thì em chịu được. Nhịn khói bếp mười ngày thì em chịu không nổi.\" The man next to him nods solemnly in agreement.",
                 subs=[(5.0, 9.8, "Đánh giặc thì em chịu được. / Nhịn khói bếp mười ngày thì em chịu không nổi.")]),
            dict(name="Thuyền độc mộc", label="Đêm · ra quân",
                 img="First-person view from a narrow dugout canoe gliding silently through tall reeds at night under moonlight, a line of other canoes ahead, a calm commander in dark armor at the front raising a hand for silence, realistic, vertical 9:16.",
                 vid="0-5s: Moonlight; a line of dugout canoes glides silently through the reeds; Triệu Quang Phục at the front whispers: \"Chèo nhẹ thôi. Lau động là lộ.\" 5-10s: Total silence, then the viewer's stomach growls loudly; every canoe stops; everyone slowly turns to stare at him in the dark.",
                 subs=[(0.5, 4.8, "Chèo nhẹ thôi. Lau động là lộ.")]),
            dict(name="Đánh úp", label="Trại giặc",
                 img="First-person view at the edge of an enemy camp at night near a swamp, fighters jumping out of canoes with spears and torches, startled enemy soldiers in heavy armor, then fleeing into tall reeds, realistic, vertical 9:16.",
                 vid="0-5s: The canoes hit the bank; fighters leap out, strike the sleeping enemy camp with torches and spears, then vanish back into the reeds. 5-10s: Enemy soldiers in heavy armor chase into the swamp and get lost among identical reeds; one shouts in frustration: \"Đầm gì mà không có đường ra thế này!\"",
                 subs=[(5.0, 9.5, "Đầm gì mà không có đường ra thế này!")]),
            dict(name="Móng rồng", label="Rạng sáng",
                 img="First-person view at dawn on a swamp island, mist, a glowing divine figure riding a dragon appearing above the reeds and handing a shining dragon claw to a kneeling commander in dark armor, the young fighter staring with his mouth open, realistic, vertical 9:16.",
                 vid="0-5s: At dawn mist, a glowing figure riding a dragon appears above the reeds and hands a shining dragon claw to the kneeling Triệu Quang Phục: \"Cài móng rồng lên mũ, đánh đâu thắng đó.\" 5-10s: The viewer, mouth wide open, whispers to his neighbor: \"Thần... thần ở đầm này thật à? Thần có mang cơm nóng không?\"",
                 subs=[(0.5, 4.8, "Cài móng rồng lên mũ, / đánh đâu thắng đó."),
                       (5.0, 9.8, "Thần ở đầm này thật à? / Thần có mang cơm nóng không?")]),
        ],
        caption="Đánh du kích trong đầm lầy, ban ngày cấm khói bếp, ăn cơm nguội mười ngày, và bụng réo đúng lúc đi đánh úp 😂 Triệu Quang Phục được gọi là Dạ Trạch Vương nhờ lối đánh này. Đầm Dạ Trạch cũng chính là đầm Nhất Dạ trong truyện Chử Đồng Tử. Bạn chịu được mấy ngày không ăn cơm nóng? 👇",
        tags="#trieuquangphuc #datrachvuong #dukich #vanxuan",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#chuyenladaiviet",
          unit="Tập", file_unit="tap")
