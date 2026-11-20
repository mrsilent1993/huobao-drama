#!/usr/bin/env python3
"""Loạt Quang Trung: 8 sự kiện nổi tiếng còn thiếu (Q1–Q8), ghép với Tây Sơn từng mốc thành danh sách phát "Quang Trung".
Chuẩn 7 clip, YouTube 60–70s, TikTok 30–35s. Mỗi tập một câu gạt riêng (không "Không hỏi."). Chạy: python3 _nguon.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tay-son-tung-moc"))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build, MUC_MOI  # noqa: E402
from _nguon import FACE, QING_EN, QING_VIS  # noqa: E402
FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a chipped front tooth; he acts naturally and understated, like a real person, not a performer")

HUE = "Central Vietnamese (Huế) accent"
NGHE = "Central Vietnamese (Nghệ An) accent"
ARMY = "Tây Sơn soldiers with black-lacquered teeth in dark-red uniforms with red head wraps, spears and swords"
HUE_ = ("Nguyễn Huệ (later Emperor Quang Trung), seen ONLY from behind or far away: a broad-shouldered man in a dark "
        "battle robe")
SAFE = "Adults only, no children. No flags, no legible writing anywhere, no modern objects, no blood, no dead bodies."
QT_VOICE = ("Quang Trung's own voice, used ONLY for him and identical in every clip: a deep, booming, thunderous male voice "
            "of a commander in his mid-thirties with a Central Vietnamese (Bình Định) accent; slow, heavy and powerful, each "
            "phrase struck like a war drum and echoing across the field; clearly different from Anh Tư and from the calm narrator")
QT_LOOK = ("Emperor Quang Trung is seen ONLY from behind or far away: a tall, broad-shouldered man in a dark-red battle robe "
           "with a gold-trimmed collar, a black turban, a long sword, standing on a high wooden platform.")
QT_SHOT = "Emperor Quang Trung seen ONLY from behind, tall and broad-shouldered in a dark-red battle robe and black turban"
NOTE = ("**Loạt Quang Trung (Q1–Q8):** những sự kiện nổi tiếng còn thiếu, ghép với loạt Tây Sơn từng mốc thành một danh sách "
        "phát. Kể theo công thức Anh Tư; Nguyễn Huệ, vua Quang Trung và vua Lê chỉ xuất hiện từ phía sau hoặc từ xa. "
        "**Hai video từ cùng 7 clip:** YouTube khoảng 67 giây, TikTok khoảng 35 giây, vẫn đủ 7 cảnh.")
LEN = ("hai video từ cùng 7 clip: **YouTube** khoảng 67 giây và **TikTok** khoảng 35 giây, vẫn đủ 7 cảnh (mỗi clip lấy "
       "khoảng 5 giây chứa câu chính, cảnh cuối 7 giây)")
END = "Follow để xem / loạt Quang Trung / tập tiếp theo →"
COMMON = dict(length=LEN, muc=MUC_MOI, giong=HUE, end=END, end_secs=1.6)
YT = "quang trung, nguyễn huệ, tây sơn, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"


def c(name, cut, label, img, vid, subs, **kw):
    return dict(name=name, tiktok=cut, label=label, img=img + ", realistic, vertical 9:16.", vid=vid, subs=subs, **kw)


EPISODES = [
    # ================================================================== Q1 · 1786 quỳ lạy vua Lê
    dict(COMMON, slug="quy-lay-vua-le-1786", prefix="qt1",
        voices={"officer": "a stern, clipped male voice", "old king": "a frail, trembling, very old male voice",
                "townswoman": "an anxious middle-aged woman's voice, Northern accent"},
        title="Q1 · Trải chiếu cho ông tướng vừa thắng cả Bắc Hà, hóa ra để ông… quỳ lạy (phù Lê, 1786)",
        history=("**Lịch sử:** giữa năm 1786, Nguyễn Huệ đem quân ra Bắc, lật đổ họ Trịnh đã lấn quyền vua Lê hơn 200 năm, với "
                 "danh nghĩa **\"phù Lê diệt Trịnh\"**. Vào Thăng Long, ông vào triều **ra mắt vua Lê Hiển Tông** (khi ấy đã "
                 "già yếu), được vua phong Nguyên súy, Uy quốc công (sử nhà Nguyễn, *Hoàng Lê nhất thống chí*, mức B). **Hư "
                 "cấu:** Anh Tư trải chiếu, người dân xì xào và mọi lời thoại. Không dựng cảnh chiến trận."),
        setting=("Thăng Long, summer 1786: the old Lê royal palace with red-lacquered pillars and faded gold, an empty Trịnh "
                 f"lord's mansion, anxious townspeople in Northern dress in the streets. {ARMY}. {HUE_}. The old Lê king, "
                 "frail, in a yellow robe on a throne, seen ONLY from far away or from behind. "
                 f"Anh Tư is {FACE}, a Tây Sơn soldier. {SAFE}"),
        hook="POV: Trải chiếu / cho ông tướng / vừa thắng cả Bắc Hà",
        clips=[
            c("Cuộn chiếu", "0-5", "Thăng Long · 1786",
              f"First-person view in a palace courtyard, a stern officer handing {FACE} a large rolled-up fine sedge mat",
              ("0-5s: The officer hands Anh Tư a large rolled mat: \"Vào điện trải chiếu. Trải cho phẳng.\" Anh Tư: \"Để ông "
               "Tướng ngồi ạ?\" The officer: \"Trải đi rồi biết.\" 5-10s: Anh Tư strokes the fine mat: \"Chiếu đẹp "
               "thế này... chắc để ông ấy ngồi lên ngai.\""),
              [(0.3, 2.2, "Vào điện trải chiếu. / Trải cho phẳng."), (2.2, 3.4, "Để ông Tướng ngồi ạ?"),
               (3.4, 4.9, "Trải đi rồi biết."), (5.2, 9.5, "Chiếu đẹp thế này... / chắc để ông ấy ngồi lên ngai.")]),
            c("Phủ chúa trống", "5-10", "",
              f"First-person view inside an abandoned lavish mansion, overturned stools, scattered silk cushions, a lone cat on a lacquered chair, {FACE} peeking in",
              ("0-5s: Anh Tư peeks into the empty Trịnh lord's mansion: overturned stools, scattered cushions, a lone cat. "
               "5-10s: He whispers: \"Chúa chạy rồi... phủ chúa còn mỗi con mèo.\""),
              [(5.0, 9.5, "Chúa chạy rồi... / phủ chúa còn mỗi con mèo.")]),
            c("Dân xì xào", "5-10", "",
              f"First-person view in a Thăng Long street, anxious townspeople whispering behind doorways and watching the soldiers, {FACE} passing with the mat on his shoulder",
              ("0-5s: A townswoman whispers to her neighbor: \"Quân Tây Sơn vào... vua Lê còn không?\" 5-10s: Anh Tư, carrying "
               "the mat, whispers to the viewer: \"Dân sợ ông Tướng nhà em... cướp luôn ngôi vua.\""),
              [(0.5, 4.8, "Quân Tây Sơn vào... / vua Lê còn không?"),
               (5.0, 9.5, "Dân sợ ông Tướng nhà em... / cướp luôn ngôi vua.")]),
            c("Quỳ lạy", "5-10", "Điện Kính Thiên",
              f"First-person view from the side of a grand hall, {HUE_} kneeling and bowing deeply on the fine mat before a frail old king on a distant throne, {FACE} at the edge of the hall, mouth open",
              ("0-5s: In the grand hall, Nguyễn Huệ, seen only from behind, walks to the mat Anh Tư laid... and kneels, bowing "
               "deeply before the frail old king on the distant throne. 5-10s: Anh Tư, stunned, whispers: \"Đánh thắng cả Bắc "
               "Hà... rồi vào quỳ lạy vua.\""),
              [(5.0, 9.5, "Đánh thắng cả Bắc Hà... / rồi vào quỳ lạy vua.")]),
            c("Vua già", "5-10", "",
              f"First-person view from far back in the hall, the frail old king in yellow on the throne raising a trembling hand, officials bowing, {FACE} watching quietly",
              ("0-5s: From the distant throne the old king's trembling voice: \"Khanh có công lớn với nhà Lê.\" 5-10s: Anh Tư, "
               "quietly: \"Vua già yếu thế kia... mà người thắng trận vẫn cúi đầu.\""),
              [(0.5, 4.8, "Khanh có công lớn / với nhà Lê."),
               (5.0, 9.5, "Vua già yếu thế kia... / mà người thắng trận / vẫn cúi đầu.")]),
            c("Dân reo", "5-10", "",
              f"First-person view at the palace gate, townspeople who were anxious before now smiling and cheering, an old man bowing toward the palace, {FACE} watching, relieved",
              ("0-5s: News spreads to the gate; the townspeople cheer: \"Phù Lê! Phù Lê!\" 5-10s: Anh Tư says quietly to the viewer: "
               "\"Hôm qua dân sợ... hôm nay dân reo.\""),
              [(0.5, 4.8, "Phù Lê! Phù Lê!"), (5.0, 9.5, "Hôm qua dân sợ... / hôm nay dân reo.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at sunset in the empty hall, {FACE} carefully rolling up the fine mat, a soft light through the doors",
              ("0-4.5s: Sunset; Anh Tư rolls up the mat. A calm narrator's voice says: \"Năm 1786, Nguyễn Huệ ra Bắc lật đổ "
               "họ Trịnh, rồi vào triều ra mắt vua Lê Hiển Tông.\" 4.5-10s: Anh Tư tucks the mat under his arm and says to "
               "the camera: \"Em trải chiếu cả đời... lần đầu thấy người thắng quỳ.\""),
              [(3.0, 6.0, "Năm 1786, Nguyễn Huệ / lật đổ họ Trịnh, rồi vào / ra mắt vua Lê Hiển Tông."),
               (6.1, 8.4, "Em trải chiếu cả đời... / lần đầu thấy người thắng quỳ.")]),
        ],
        caption=("Trải chiếu cho ông tướng vừa thắng cả Bắc Hà, hóa ra để ông quỳ lạy 😳 Năm 1786, Nguyễn Huệ ra Bắc lật đổ họ "
                 "Trịnh rồi vào triều ra mắt vua Lê Hiển Tông, với danh nghĩa \"phù Lê\". Bạn nghĩ vì sao ông làm vậy? 👇"),
        tags="#quangtrung #nguyenhue #phuledietrinh #taysontungmoc #1786",
        tt_title="Trải chiếu cho ông tướng vừa thắng cả Bắc Hà, hóa ra để ông quỳ lạy",
        hooks_alt=["POV: Đánh thắng cả Bắc Hà / rồi vào quỳ lạy vua", "POV: Phủ chúa trống / còn mỗi con mèo"],
        pin=("\"Phù Lê diệt Trịnh\": thắng rồi vẫn giữ lễ với vua Lê 🔥 Bạn có biết vua Lê phong Nguyễn Huệ chức gì không? "
             "Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="Năm 1786: thắng cả Bắc Hà, Nguyễn Huệ vào quỳ lạy vua Lê | Loạt Quang Trung",
        yt_tags="phù lê diệt trịnh, lê hiển tông, 1786, thăng long, " + YT),
    # ================================================================== Q2 · 1788 tuyển quân Nghệ An
    dict(COMMON, slug="dat-nao-sao-ay-nghe-an-1788", prefix="qt2", giong=NGHE,
        voices={"village official": "a fussy, nasal male voice", "officer": "a stern, clipped male voice",
                "Quang Trung": QT_VOICE},
        title="Q2 · Đang cày ruộng bị gọi ra bãi duyệt binh, nghe vua nói một câu mà nhớ cả đời (Nghệ An, cuối năm 1788)",
        history=("**Lịch sử:** cuối năm 1788, trên đường ra Bắc đánh quân Thanh, vua Quang Trung dừng ở Nghệ An hơn mười ngày "
                 "để **tuyển thêm quân**, cứ ba suất đinh lấy một người, rồi cưỡi voi ra doanh dụ quân sĩ: **\"Trong khoảng vũ "
                 "trụ, đất nào sao ấy, đều đã phân biệt rõ ràng, phương Nam phương Bắc chia nhau mà cai trị...\"** Quân sĩ đồng "
                 "thanh: \"Xin vâng lệnh, không dám hai lòng!\" (*Hoàng Lê nhất thống chí*, hồi 14, mức B). Câu \"Đánh cho để dài "
                 "tóc...\" là truyền tụng, có tập riêng (tập 9). **Hư cấu:** Anh Tư, ông lý trưởng và mọi lời thoại, trừ lời dụ "
                 "và câu đáp của quân sĩ. Chỉ đọc lời, không dựng cảnh đánh nhau."),
        setting=("Nghệ An, December 1788: muddy winter rice fields with a water buffalo and plough, then a huge parade ground "
                 "outside the Nghệ An citadel with tens of thousands of soldiers and new recruits in lines, drums, many "
                 f"spears. {ARMY}; new recruits still in brown peasant clothes. {HUE_}, now Emperor Quang Trung in a dark "
                 "battle robe on a high wooden platform, seen ONLY from behind. Men have long hair in topknots and black-"
                 f"lacquered teeth. Anh Tư is {FACE}, a farmer. {SAFE}"),
        hook="POV: Đang cày ruộng / bị gọi đi lính",
        clips=[
            c("Đến lượt", "0-5", "Nghệ An · cuối năm 1788",
              f"First-person view in a muddy rice field, a fussy village official with a bamboo list stopping beside {FACE} who is ploughing behind a water buffalo",
              ("0-5s: The village official stops at the field: \"Ba suất đinh lấy một. Nhà mày đến lượt.\" Anh Tư: \"Đang cày "
               "dở mà ông?\" The official: \"Trâu cày tiếp được.\" 5-10s: Anh Tư looks at the buffalo and sighs: \"Trâu ở nhà "
               "cày... người ra trận.\""),
              [(0.3, 2.2, "Ba suất đinh lấy một. / Nhà mày đến lượt."), (2.2, 3.4, "Đang cày dở mà ông?"),
               (3.4, 4.9, "Trâu cày tiếp được."), (5.2, 9.5, "Trâu ở nhà cày... / người ra trận.")]),
            c("Cầm ngược", "5-10", "",
              f"First-person view on a parade ground, an officer flipping the spear in the hands of {FACE}, who was holding it upside down like a plough handle",
              ("0-5s: On the parade ground Anh Tư holds his spear like a plough handle, point down. The officer flips it: "
               "\"Mũi giáo quay về phía giặc!\" 5-10s: Anh Tư, embarrassed: \"Hôm qua em cầm cày... hôm nay cầm giáo ngược.\""),
              [(0.5, 4.8, "Mũi giáo / quay về phía giặc!"), (5.0, 9.5, "Hôm qua em cầm cày... / hôm nay cầm giáo ngược.")]),
            c("Mười ngày", "5-10", "",
              f"First-person view of rows of new recruits in peasant clothes drilling with spears in time to drums, {FACE} in the middle, sweating and out of step",
              ("0-5s: Rows of new recruits drill to the drums: thrust, step, turn. Anh Tư is half a beat behind. 5-10s: He "
               "pants to the viewer: \"Mười ngày... mà phải thành lính.\""),
              [(0.5, 4.8, "Một! Hai! Đâm!"), (5.0, 9.5, "Mười ngày... / mà phải thành lính.")]),
            c("Im phăng phắc", "5-10", "",
              f"First-person wide view of tens of thousands of soldiers in silent lines facing a high wooden platform, {HUE_} stepping onto it, {FACE} in the ranks holding his breath",
              ("0-5s: The drums stop. The emperor, seen only from behind, steps onto the high platform. Tens of thousands fall "
               "silent. 5-10s: Anh Tư whispers: \"Cả bãi mấy vạn người... im như đêm.\""),
              [(5.0, 9.5, "Cả bãi mấy vạn người... / im như đêm.")]),
            c("Lời dụ", "5-10", "Vua Quang Trung",
              f"First-person view from the ranks looking up at {HUE_} on the platform raising one arm, the army's spears rising like a forest, {FACE} with tears in his eyes",
              ("0-5s: The emperor, seen only from behind, raises his arm. 5-10s: ONLY Quang Trung speaks, his booming voice coming from the platform while Anh Tư keeps his mouth closed: \"Trong khoảng vũ trụ, "
               "đất nào sao ấy, đều đã phân biệt rõ ràng!\" The whole army roars and raises their spears."),
              [(5.0, 9.5, "Vua Quang Trung: / Trong khoảng vũ trụ, / đất nào sao ấy, / đều đã phân biệt rõ ràng!")]),
            c("Đất nhà mình", "5-10", "",
              f"Close first-person view as {FACE} looks down at the dried mud of his rice field still on his bare feet, then up, determined, the roaring army around him",
              ("0-5s: As the army roars, Anh Tư looks down at the mud of Nghệ An still on his feet. 5-10s: He says quietly to "
               "the viewer: \"Đất nào sao ấy... thì đất này là của nhà mình.\""),
              [(5.0, 9.5, "Đất nào sao ấy... / thì đất này / là của nhà mình.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dawn as the army marches north out of Nghệ An, {FACE} in a dark-red uniform now, spear upright, looking back once toward his village",
              ("0-4.5s: Dawn; the army marches north. A calm narrator's voice says: \"Cuối năm 1788, trên đường ra Bắc, vua "
               "Quang Trung tuyển thêm quân ở Nghệ An và dụ tướng sĩ.\" 4.5-10s: Anh Tư looks back toward his village and says "
               "to the camera: \"Ra đi là thằng cày ruộng... về làng là lính Quang Trung.\""),
              [(3.0, 6.0, "Năm 1788, trên đường ra Bắc, / vua Quang Trung tuyển quân / ở Nghệ An."),
               (6.1, 8.4, "Ra đi là thằng cày ruộng... / về làng là lính Quang Trung.")]),
        ],
        caption=("Đang cày ruộng bị gọi đi lính, ra bãi duyệt binh nghe vua nói một câu mà nhớ cả đời 🔥 \"Trong khoảng vũ trụ, "
                 "đất nào sao ấy, đều đã phân biệt rõ ràng...\" Cuối năm 1788, vua Quang Trung tuyển quân ở Nghệ An trước khi ra "
                 "Bắc đánh quân Thanh. Quê bạn ở Nghệ An không? 👇"),
        tags="#quangtrung #datnaosaoay #nghean #taysontungmoc #1788",
        tt_title="Đang cày ruộng bị gọi đi lính, nghe một câu mà nhớ cả đời",
        hooks_alt=["POV: Đất nào sao ấy / đất này của nhà mình", "POV: Hôm qua cầm cày / hôm nay cầm giáo"],
        pin=("Lời dụ ở Nghệ An còn kể tên Trưng Nữ Vương, Đinh Tiên Hoàng, Lê Đại Hành, Trần Hưng Đạo, Lê Thái Tổ 🔥 Còn câu \"Đánh cho để dài tóc\" thì sao? Xem tập riêng của loạt Quang Trung!"),
        yt_title="\"Đất nào sao ấy\": vua Quang Trung tuyển quân ở Nghệ An 1788 | Loạt Quang Trung",
        yt_tags="đất nào sao ấy, lời dụ nghệ an, hoàng lê nhất thống chí, nghệ an, tuyển quân, 1788, " + YT),
    # ================================================================== Q3 · Tết 1789 cành đào
    dict(COMMON, slug="canh-dao-ve-phu-xuan-1789", prefix="qt3", legend=True,
        voices={"officer": "a stern, clipped male voice", "station keeper": "a sleepy, gruff old male voice"},
        title="Q3 · Phi ngựa mấy ngày đêm từ Thăng Long về Phú Xuân, chỉ để giữ một cành đào không rụng (Tết 1789, theo truyền tụng)",
        history=("**Truyền tụng (mức C):** sau chiến thắng Tết Kỷ Dậu 1789, vua Quang Trung sai ngựa trạm đem **một cành đào "
                 "Thăng Long** về Phú Xuân tặng hoàng hậu, như báo tin thắng trận; đến nơi hoa vẫn còn tươi. Chuyện được kể "
                 "lại nhiều đời nhưng chưa thấy chính sử chép, nên video gắn nhãn \"theo truyền thuyết\". **Hư cấu:** Anh Tư và "
                 "mọi lời thoại. Hoàng hậu không xuất hiện trong khung hình."),
        setting=("Vietnam, early spring 1789: from Thăng Long south along the old royal post road: relay stations with fresh "
                 "horses, the windy Ngang pass over the sea, rain on the coastal plain, then the gate of the Phú Xuân palace. "
                 "A single branch of pink Thăng Long peach blossoms carried upright in a small lacquered bamboo tube. "
                 f"Anh Tư is {FACE}, a royal courier in a dark-red uniform on horseback. {SAFE}"),
        hook="POV: Phi ngựa / mấy ngày đêm / giữ một cành đào",
        clips=[
            c("Cành đào", "0-5", "Thăng Long · Tết 1789",
              f"First-person view at a palace courtyard in Thăng Long, a stern officer handing {FACE} a single pink peach blossom branch in a lacquered bamboo tube, a saddled horse waiting",
              ("0-5s: The officer hands Anh Tư a peach branch in a bamboo tube: \"Đưa về Phú Xuân. Không rụng một bông.\" Anh "
               "Tư: \"Xa cả nghìn dặm mà ạ?\" The officer: \"Thế thì phi nhanh.\" 5-10s: Anh Tư holds the delicate branch like "
               "a bomb: \"Giặc thì em không sợ... em sợ cái cành này.\""),
              [(0.3, 2.2, "Đưa về Phú Xuân. / Không rụng một bông."), (2.2, 3.4, "Xa cả nghìn dặm mà ạ?"),
               (3.4, 4.9, "Thế thì phi nhanh."), (5.2, 9.5, "Giặc thì em không sợ... / em sợ cái cành này.")]),
            c("Phi ngựa", "5-10", "",
              f"First-person view galloping on a dirt post road, {FACE} riding hard with one hand on the reins and the other holding the peach branch high and perfectly still",
              ("0-5s: Anh Tư gallops down the post road, one hand on the reins, the other holding the branch perfectly still. "
               "5-10s: Through gritted teeth: \"Ngựa thì phải phi nhanh... mà đào thì phải đi êm.\""),
              [(5.0, 9.5, "Ngựa thì phải phi nhanh... / mà đào thì phải đi êm.")]),
            c("Đổi ngựa", "5-10", "",
              f"First-person view at a roadside relay station at night, a sleepy old station keeper holding a fresh horse, {FACE} leaping across with the peach branch held above his head",
              ("0-5s: At a relay station the sleepy keeper holds a fresh horse: \"Thư hỏa tốc à?\" 5-10s: Anh Tư leaps across, "
               "branch above his head: \"Không. Đào hỏa tốc!\""),
              [(0.5, 4.8, "Thư hỏa tốc à?"), (5.0, 9.5, "Không. / Đào hỏa tốc!")]),
            c("Gió đèo", "5-10", "Đèo Ngang",
              f"First-person view on the windy Ngang mountain pass above the sea, {FACE} turning his back to a strong gust and shielding the peach branch with his whole body and hat",
              ("0-5s: A violent gust on the Ngang pass; Anh Tư turns his back and shields the branch with his body and hat. "
               "5-10s: He whispers to the viewer: \"Sợ nhất không phải giặc... mà rụng một bông đào.\""),
              [(5.0, 9.5, "Sợ nhất không phải giặc... / mà rụng một bông đào.")]),
            c("Mưa", "5-10", "",
              f"First-person view in heavy rain on the coastal plain, {FACE} soaked to the skin, the peach branch wrapped dry inside his shirt",
              ("0-5s: Heavy rain; Anh Tư takes off his outer shirt and wraps the branch inside it. 5-10s: Soaked, he says to "
               "the viewer: \"Em ướt hết... đào thì khô.\""),
              [(5.0, 9.5, "Em ướt hết... / đào thì khô.")]),
            c("Đếm bông", "5-10", "",
              f"Close first-person view at dawn by the roadside, {FACE} carefully counting the pink blossoms on the branch with one fingertip, exhausted, relieved",
              ("0-5s: At dawn Anh Tư counts the blossoms with one fingertip, lips moving. 5-10s: He sighs with relief: \"Đi "
               "bao nhiêu bông... về đủ bấy nhiêu bông.\""),
              [(5.0, 9.5, "Đi bao nhiêu bông... / về đủ bấy nhiêu bông.")]),
            c("Câu chốt", "3-10", "Phú Xuân",
              f"First-person view at the gate of the Phú Xuân palace, an adult palace attendant receiving the fresh peach branch with both hands, {FACE} mud-splattered, quietly relieved",
              ("0-4.5s: At the Phú Xuân palace gate an adult palace attendant receives the fresh branch with both hands. A "
               "calm narrator's voice says: \"Theo truyền tụng, Tết Kỷ Dậu 1789, vua Quang Trung gửi cành đào Thăng Long về "
               "Phú Xuân. Đến nơi, hoa vẫn tươi.\" 4.5-10s: Anh Tư, mud-splattered, to the camera: \"Người ta báo tin thắng "
               "trận bằng thư... vua báo bằng một cành đào.\""),
              [(3.0, 6.0, "Theo truyền tụng, vua gửi / cành đào Thăng Long / về Phú Xuân. Hoa vẫn tươi."),
               (6.1, 8.4, "Người ta báo thắng trận / bằng thư... vua báo / bằng một cành đào.")]),
        ],
        caption=("Phi ngựa mấy ngày đêm từ Thăng Long về Phú Xuân, chỉ để giữ một cành đào không rụng 🌸 Theo truyền tụng, Tết "
                 "Kỷ Dậu 1789, vua Quang Trung báo tin thắng trận bằng một cành đào. Nếu là bạn, bạn gửi gì cho người ở nhà? 👇"),
        tags="#quangtrung #canhdao #tetkydau #taysontungmoc #1789",
        tt_title="Phi ngựa mấy ngày đêm chỉ để giữ một cành đào không rụng",
        hooks_alt=["POV: Thư hỏa tốc? / Không. Đào hỏa tốc!", "POV: Sợ nhất không phải giặc / mà rụng một bông đào"],
        pin=("Chuyện cành đào là truyền tụng, sử chưa chép, nhưng ai nghe cũng thích 🌸 Bạn tin không? Follow để xem loạt Quang "
             "Trung tập tiếp theo!"),
        yt_title="Cành đào Thăng Long về Phú Xuân: vua Quang Trung báo tin thắng trận (truyền tụng) | Loạt Quang Trung",
        yt_tags="cành đào thăng long, tết kỷ dậu, phú xuân, ngựa trạm, 1789, " + YT),
    # ================================================================== Q4 · 1789 trả tù binh
    dict(COMMON, slug="tra-tu-binh-ve-nuoc-1789", prefix="qt4",
        voices={"officer": "a stern, clipped male voice",
                "Qing prisoner": "a tired young adult male voice speaking a few words of Vietnamese with a Chinese accent"},
        title="Q4 · Vừa thắng trận đã bị sai nấu cơm cho tù binh giặc ăn no rồi về (trả tù binh nhà Thanh, 1789)",
        history=("**Lịch sử:** sau chiến thắng Ngọc Hồi – Đống Đa (Tết Kỷ Dậu 1789), vua Quang Trung cho **nuôi ăn tù binh và "
                 "hàng binh nhà Thanh**, rồi **thả về nước**, đồng thời sai Ngô Thì Nhậm soạn thư từ ngoại giao để giảng hòa "
                 "với nhà Thanh (sử nhà Nguyễn, *Hoàng Lê nhất thống chí*, mức B). Nhờ đó hai nước sớm nối lại hòa hiếu. **Hư "
                 "cấu:** Anh Tư, cảnh nấu cơm, gói cơm và mọi lời thoại. Giọng kể là nhân nghĩa của ta, không hạ thấp ai."),
        setting=("Thăng Long, early 1789, a few days after the battle: a large courtyard camp with huge iron rice pots over "
                 f"wood fires, leftover bánh chưng, bundles of cloth coats. {ARMY}. {QING_EN} Here the Qing are unarmed, "
                 "tired prisoners sitting calmly in rows, treated decently. "
                 f"Anh Tư is {FACE}, a Tây Sơn soldier with a big ladle. {SAFE}"),
        visual=QING_VIS,
        hook="POV: Thắng trận xong / bị sai nấu cơm / cho giặc",
        clips=[
            c("Nấu cơm", "0-5", "Thăng Long · Tết 1789",
              f"First-person view in a courtyard camp, a stern officer pointing at a giant iron rice pot and rows of seated Qing prisoners, {FACE} holding a big ladle",
              ("0-5s: The officer points at a giant pot and rows of prisoners: \"Nấu cơm. Nấu cho cả trại tù binh.\" Anh Tư: "
               "\"Cho giặc ăn ạ?\" The officer: \"Ăn no mới đi đường xa được.\" 5-10s: Anh Tư stirs the pot: \"Hôm qua em đánh "
               "nó... hôm nay em nấu cơm cho nó.\""),
              [(0.3, 2.2, "Nấu cơm. / Nấu cho cả trại tù binh."), (2.2, 3.4, "Cho giặc ăn ạ?"),
               (3.4, 4.9, "Ăn no mới / đi đường xa được."), (5.2, 9.5, "Hôm qua em đánh nó... / hôm nay em nấu cơm cho nó.")]),
            c("Bánh chưng", "5-10", "",
              f"First-person view as {FACE} hands slices of bánh chưng to a row of tired Qing prisoners, one of them eating hungrily",
              ("0-5s: Anh Tư hands out leftover bánh chưng; a prisoner wolfs it down. 5-10s: Anh Tư, amused, to the viewer: "
               "\"Bánh chưng nhà em... nó ăn còn nhanh hơn em.\""),
              [(5.0, 9.5, "Bánh chưng nhà em... / nó ăn còn nhanh hơn em.")]),
            c("Áo ấm", "5-10", "",
              f"First-person view as the officer hands out new cloth coats to shivering prisoners, {FACE} looking down at his own torn sleeve",
              ("0-5s: The officer hands out new cloth coats to the shivering prisoners. 5-10s: Anh Tư looks at his own torn "
               "sleeve: \"Áo em còn rách... nó được áo mới.\""),
              [(5.0, 9.5, "Áo em còn rách... / nó được áo mới.")]),
            c("Gói cơm", "5-10", "",
              f"First-person view of {FACE} pressing rice balls into banana leaves and tying them with string, a long row of parcels ready for a journey",
              ("0-5s: Anh Tư presses rice balls into banana leaves and ties them, a long row of parcels for the road. 5-10s: He "
               "shakes his head at the viewer: \"Thắng xong... còn gói cơm cho giặc ăn đường.\""),
              [(5.0, 9.5, "Thắng xong... / còn gói cơm cho giặc ăn đường.")]),
            c("Hỏi đường", "5-10", "",
              f"First-person view as a young adult Qing prisoner with a rice parcel gestures, asking the way, {FACE} pointing firmly north up the road",
              ("0-5s: A young prisoner with a rice parcel gestures, asking: \"Đường... về nhà?\" 5-10s: Anh Tư points firmly "
               "north: \"Thẳng đường này. Đi thẳng... đừng quay lại.\""),
              [(0.5, 4.8, "Đường... về nhà?"), (5.0, 9.5, "Thẳng đường này. / Đi thẳng... đừng quay lại.")]),
            c("Lên đường", "5-10", "",
              f"First-person view of a long column of Qing prisoners walking north along a road with rice parcels, {FACE} waving his ladle after them",
              ("0-5s: A long column of prisoners walks north with their rice parcels. 5-10s: Anh Tư waves his ladle: \"Về nói "
               "với người bên ấy... cơm Đại Việt ngon, nhưng đừng sang ăn nữa.\""),
              [(5.0, 9.5, "Cơm Đại Việt ngon... / nhưng đừng sang ăn nữa.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view in the empty courtyard at dusk, {FACE} scraping the bottom of the giant pot and eating the burnt rice crust himself",
              ("0-4.5s: Dusk; the courtyard is empty. A calm narrator's voice says: \"Sau chiến thắng Kỷ Dậu 1789, vua Quang "
               "Trung cho nuôi ăn tù binh nhà Thanh rồi thả về nước, mở đường giảng hòa.\" 4.5-10s: Anh Tư eats the burnt crust "
               "from the pot: \"Đánh cho nó sợ... nuôi cho nó nhớ.\""),
              [(3.0, 6.0, "Vua Quang Trung cho nuôi ăn / tù binh rồi thả về nước, / mở đường giảng hòa."),
               (6.1, 8.4, "Đánh cho nó sợ... / nuôi cho nó nhớ.")]),
        ],
        caption=("Vừa thắng trận đã bị sai nấu cơm cho tù binh giặc ăn no rồi về 😳 Sau chiến thắng Tết Kỷ Dậu 1789, vua Quang "
                 "Trung cho nuôi ăn tù binh nhà Thanh rồi thả về nước. \"Đánh cho nó sợ, nuôi cho nó nhớ.\" Bạn nghĩ sao? 👇"),
        tags="#quangtrung #tutbinh #nhannghia #taysontungmoc #1789",
        tt_title="Vừa thắng trận đã bị sai nấu cơm cho tù binh giặc ăn no rồi về",
        hooks_alt=["POV: Thắng xong / còn gói cơm cho giặc", "POV: Hôm qua đánh nó / hôm nay nấu cơm cho nó"],
        pin=("Cùng tinh thần với năm 1427, Lê Lợi đóng thuyền tiễn quân Minh về 🔥 Bạn còn biết lần nào tổ tiên mình tha cho "
             "giặc không? Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="Năm 1789: thắng trận xong, nấu cơm cho tù binh nhà Thanh về nước | Loạt Quang Trung",
        yt_tags="trả tù binh, nhân nghĩa, ngô thì nhậm, giảng hòa, 1789, " + YT),
    # ================================================================== Q5 · chiếu cầu hiền
    dict(COMMON, slug="chieu-cau-hien-1789", prefix="qt5",
        voices={"officer": "a stern, clipped male voice", "old scholar": "a proud, dignified old male voice, Northern accent"},
        title="Q5 · Bị sai đi dán chiếu mời người tài ra làm quan, mà người tài toàn là người từng chống vua (chiếu cầu hiền, 1789)",
        history=("**Lịch sử:** sau khi lên ngôi và đánh đuổi quân Thanh, vua Quang Trung ban **Chiếu cầu hiền** do Ngô Thì Nhậm "
                 "soạn, mời các sĩ phu Bắc Hà, nhiều người từng làm quan cho nhà Lê và đang lánh đi ở ẩn, ra giúp nước (mức "
                 "B; năm ban chiếu các tài liệu ghi khác nhau, khoảng 1788–1789). Nhiều người như Ngô Thì Nhậm, Phan Huy Ích, "
                 "Ninh Tốn đã ra làm việc cho triều Tây Sơn. **Hư cấu:** Anh Tư, ông đồ trong tập và mọi lời thoại."),
        setting=("Thăng Long and nearby villages, 1789: a busy market with a wooden notice wall, thatched houses of scholars "
                 "with bookshelves and ink stones, a palace gate. Edict sheets are sheets of paper with a red seal; all writing "
                 f"on them is blurred and unreadable. {ARMY}. Northern scholars in dark robes and black turbans. "
                 f"Anh Tư is {FACE}, a Tây Sơn soldier with a bowl of rice paste and a brush. {SAFE}"),
        hook="POV: Đi dán chiếu / mời người tài / ra làm quan",
        clips=[
            c("Mời người tài", "0-5", "Thăng Long · 1789",
              f"First-person view at a market, a stern officer handing {FACE} a thick stack of sealed edict sheets and a bowl of rice paste",
              ("0-5s: The officer hands Anh Tư a stack of edicts and a bowl of paste: \"Dán khắp chợ. Mời người tài ra làm "
               "quan.\" Anh Tư: \"Người tài ở đâu ạ?\" The officer: \"Ở chỗ họ đang trốn.\" 5-10s: Anh Tư scratches his head: "
               "\"Mời người... mà người ta đang trốn mình.\""),
              [(0.3, 2.2, "Dán khắp chợ. / Mời người tài ra làm quan."), (2.2, 3.4, "Người tài ở đâu ạ?"),
               (3.4, 4.9, "Ở chỗ họ đang trốn."), (5.2, 9.5, "Mời người... / mà người ta đang trốn mình.")]),
            c("Dán chiếu", "5-10", "",
              f"First-person view of {FACE} pasting an edict sheet on a wooden market wall, a crowd gathering to read it over his shoulder",
              ("0-5s: Anh Tư slaps an edict on the market wall; a crowd gathers to read. 5-10s: He whispers to the viewer: "
               "\"Em dán cả trăm tờ... không đọc được chữ nào.\""),
              [(5.0, 9.5, "Em dán cả trăm tờ... / không đọc được chữ nào.")]),
            c("Ông đồ ở ẩn", "5-10", "",
              f"First-person view at the half-open door of a thatched house, a proud old scholar in a dark robe looking suspiciously at {FACE}, who holds out an edict",
              ("0-5s: A proud old scholar opens his door a crack: \"Ta từng làm quan nhà Lê. Ta từng chống Tây Sơn.\" 5-10s: "
               "Anh Tư checks the edict, then nods: \"Thế thì vua mời đúng người rồi.\""),
              [(0.5, 4.8, "Ta từng làm quan nhà Lê. / Ta từng chống Tây Sơn."), (5.0, 9.5, "Thế thì vua mời / đúng người rồi.")]),
            c("Ông đồ đọc", "5-10", "",
              f"First-person view inside the scholar's house, the old scholar reading the edict by the window, his hands trembling slightly, {FACE} waiting",
              ("0-5s: The old scholar reads the edict by the window; his proud face slowly softens. 5-10s: Anh Tư whispers to "
               "the viewer: \"Hôm qua còn chống vua... hôm nay được vua mời.\""),
              [(5.0, 9.5, "Hôm qua còn chống vua... / hôm nay được vua mời.")]),
            c("Xếp hàng", "5-10", "",
              f"First-person view at a palace gate, a line of scholars in dark robes with cloth bundles waiting to enter, {FACE} standing guard, eyebrows raised",
              ("0-5s: At the palace gate a line of scholars waits with their bundles. 5-10s: Anh Tư says quietly to the viewer: \"Hôm "
               "qua trốn kỹ thế... hôm nay xếp hàng dài thế.\""),
              [(5.0, 9.5, "Hôm qua trốn kỹ thế... / hôm nay xếp hàng dài thế.")]),
            c("Mày thì sao", "5-10", "",
              f"First-person view as the officer jokingly hands {FACE} a blank sheet and a brush, Anh Tư holding the brush like a paste brush",
              ("0-5s: The officer hands Anh Tư a blank sheet and a brush: \"Mày cũng thi thử đi.\" 5-10s: Anh Tư holds the brush "
               "like a paste brush: \"Em tài nhất trại... khoản dán giấy.\""),
              [(0.5, 4.8, "Mày cũng thi thử đi."), (5.0, 9.5, "Em tài nhất trại... / khoản dán giấy.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dusk in the market, {FACE} pasting the very last edict, the old scholar now in an official's robe walking past and nodding to him",
              ("0-4.5s: Dusk; Anh Tư pastes the last edict. The old scholar, now in an official's robe, walks past and nods. A "
               "calm narrator's voice says: \"Vua Quang Trung ban Chiếu cầu hiền do Ngô Thì Nhậm soạn, mời sĩ phu Bắc Hà ra "
               "giúp nước.\" 4.5-10s: Anh Tư to the camera: \"Thắng giặc bằng gươm... giữ nước bằng người tài.\""),
              [(3.0, 6.0, "Vua Quang Trung ban / Chiếu cầu hiền, mời / sĩ phu Bắc Hà giúp nước."),
               (6.1, 8.4, "Thắng giặc bằng gươm... / giữ nước bằng người tài.")]),
        ],
        caption=("Bị sai đi dán chiếu mời người tài ra làm quan, mà người tài toàn là người từng chống vua 😳 Vua Quang Trung ban "
                 "Chiếu cầu hiền, mời cả các sĩ phu từng làm quan nhà Lê ra giúp nước. Nếu là bạn, bạn có ra không? 👇"),
        tags="#quangtrung #chieucauhien #ngothinham #taysontungmoc #1789",
        tt_title="Đi dán chiếu mời người tài, mà người tài toàn là người từng chống vua",
        hooks_alt=["POV: Hôm qua còn chống vua / hôm nay được vua mời", "POV: Mời người tài / mà người ta đang trốn"],
        pin=("Chiếu cầu hiền do Ngô Thì Nhậm soạn, người từng làm quan nhà Lê 🔥 Bạn có biết ông còn giúp vua việc gì nữa không? "
             "Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="Chiếu cầu hiền: vua Quang Trung mời cả người từng chống mình | Loạt Quang Trung",
        yt_tags="chiếu cầu hiền, ngô thì nhậm, sĩ phu bắc hà, trọng người tài, " + YT),
    # ================================================================== Q6 · chiếu khuyến nông
    dict(COMMON, slug="chieu-khuyen-nong-1789", prefix="qt6",
        voices={"officer": "a stern, clipped male voice", "villager": "a doubtful middle-aged male voice, Northern accent"},
        title="Q6 · Vừa thắng giặc chưa kịp ăn mừng, bị sai đi gọi dân về… cày ruộng (Chiếu khuyến nông, 1789)",
        history=("**Lịch sử:** năm 1789, sau nhiều năm chiến tranh và đói kém, ruộng đất bỏ hoang rất nhiều. Vua Quang Trung ban "
                 "**Chiếu khuyến nông** (do Ngô Thì Nhậm soạn): dân phiêu tán phải trở về quê cũ, ruộng bỏ hoang phải khai "
                 "khẩn cày cấy; làng nào để ruộng hoang thì bị xử phạt. Chỉ vài năm sau, mùa màng trở lại (mức B). **Hư cấu:** "
                 "Anh Tư, người dân trong tập và mọi lời thoại."),
        setting=("Northern Vietnam, spring 1789: abandoned villages with weeds taller than a man in the rice fields, a crowded "
                 "town where displaced villagers have gathered, then later the same fields green with young rice. Peasants in "
                 f"brown clothes, water buffaloes, ploughs. {ARMY}. Anh Tư is {FACE}, a Tây Sơn soldier with a wooden "
                 f"watchman's clapper (mõ). {SAFE}"),
        hook="POV: Thắng giặc xong / bị sai đi / gọi dân về cày",
        clips=[
            c("Gọi dân về", "0-5", "Bắc Hà · 1789",
              f"First-person view in a town square, a stern officer handing {FACE} a wooden watchman's clapper and pointing at the countryside",
              ("0-5s: The officer hands Anh Tư a wooden clapper: \"Đi gọi dân về làng. Về cày.\" Anh Tư: \"Vừa thắng giặc... "
               "không ăn mừng ạ?\" The officer: \"Ăn mừng xong thì đói.\" 5-10s: Anh Tư turns the clapper over: \"Đánh giặc "
               "em quen... gọi người về cày thì lần đầu.\""),
              [(0.3, 2.2, "Đi gọi dân về làng. / Về cày."), (2.2, 3.4, "Vừa thắng giặc... / không ăn mừng ạ?"),
               (3.4, 4.9, "Ăn mừng xong thì đói."), (5.2, 9.5, "Đánh giặc em quen... / gọi người về cày / thì lần đầu.")]),
            c("Cỏ cao hơn người", "5-10", "",
              f"First-person view at the edge of an abandoned rice field overgrown with weeds taller than a man, {FACE} pushing through them",
              ("0-5s: Anh Tư pushes into an abandoned field; the weeds are taller than him. 5-10s: Only his head pops out: \"Cỏ "
               "cao hơn người... ruộng bỏ mấy năm rồi.\""),
              [(5.0, 9.5, "Cỏ cao hơn người... / ruộng bỏ mấy năm rồi.")]),
            c("Gõ mõ", "5-10", "",
              f"First-person view in a crowded town street full of displaced villagers with bundles, {FACE} beating the wooden clapper and calling out, a villager looking doubtful",
              ("0-5s: Anh Tư beats the clapper: \"Ai về quê cày ruộng thì được yên ổn làm ăn!\" A villager squints: \"Thật "
               "không? Về lại có giặc thì sao?\" 5-10s: Anh Tư whispers to the viewer: \"Người ta chạy giặc mấy năm... giờ mới "
               "dám về.\""),
              [(0.3, 2.6, "Ai về quê cày ruộng / thì được yên ổn làm ăn!"), (2.6, 4.8, "Thật không? / Về lại có giặc thì sao?"),
               (5.0, 9.5, "Người ta chạy giặc mấy năm... / giờ mới dám về.")]),
            c("Gác giáo cầm cày", "5-10", "",
              f"First-person view in a field as {FACE} leans his spear against a tree and takes a plough from a farmer, a water buffalo waiting",
              ("0-5s: Anh Tư leans his spear against a tree and takes the plough handle. 5-10s: He says quietly to the viewer: \"Đánh "
               "giặc xong... việc tiếp theo là cày.\""),
              [(5.0, 9.5, "Đánh giặc xong... / việc tiếp theo là cày.")]),
            c("Phạt", "5-10", "",
              f"First-person view in a village courtyard, the officer warning a group of village elders while pointing at a weedy field, {FACE} beside him nodding seriously",
              ("0-5s: The officer warns the village elders: \"Làng nào để ruộng hoang... thì bị phạt.\" 5-10s: Anh Tư, to the "
               "viewer: \"Ngày xưa sợ giặc... giờ sợ cỏ.\""),
              [(0.5, 4.8, "Làng nào để ruộng hoang... / thì bị phạt."), (5.0, 9.5, "Ngày xưa sợ giặc... / giờ sợ cỏ.")]),
            c("Lúa xanh", "5-10", "",
              f"First-person wide view months later of the same fields now bright green with young rice, farmers working, {FACE} standing on the dike, amazed",
              ("0-5s: Months later the same fields are bright green with young rice; farmers bend in rows. 5-10s: Anh Tư on the "
               "dike: \"Mùa trước là chiến trường... mùa này là ruộng lúa.\""),
              [(5.0, 9.5, "Mùa trước là chiến trường... / mùa này là ruộng lúa.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at harvest time, {FACE} lifting the lid of a rice pot in a farmer's kitchen, steam rising, the farmer's family smiling",
              ("0-4.5s: Harvest time; a farmer's family invites Anh Tư to eat. A calm narrator's voice says: \"Năm 1789, vua "
               "Quang Trung ban Chiếu khuyến nông, gọi dân phiêu tán về quê, khai khẩn ruộng hoang.\" 4.5-10s: Anh Tư lifts the "
               "pot lid, steam rising: \"Giữ được nước rồi... giờ giữ cái nồi cơm.\""),
              [(3.0, 6.0, "Năm 1789, vua Quang Trung / ban Chiếu khuyến nông, / gọi dân về khai hoang."),
               (6.1, 8.4, "Giữ được nước rồi... / giờ giữ cái nồi cơm.")]),
        ],
        caption=("Vừa thắng giặc chưa kịp ăn mừng, bị sai đi gọi dân về cày ruộng 😂 Năm 1789, vua Quang Trung ban Chiếu khuyến "
                 "nông: dân phiêu tán về quê, ruộng hoang phải cày lại. \"Giữ được nước rồi, giờ giữ cái nồi cơm.\" Quê bạn ở "
                 "đâu? 👇"),
        tags="#quangtrung #chieukhuyennong #nhanong #taysontungmoc #1789",
        tt_title="Vừa thắng giặc chưa kịp ăn mừng, bị sai đi gọi dân về cày ruộng",
        hooks_alt=["POV: Đánh giặc xong / việc tiếp theo là cày", "POV: Ngày xưa sợ giặc / giờ sợ cỏ"],
        pin=("Chỉ vài năm sau Chiếu khuyến nông, mùa màng trở lại 🌾 Bạn có biết chiếu này do ai soạn không? Follow để xem loạt "
             "Quang Trung tập tiếp theo!"),
        yt_title="Chiếu khuyến nông 1789: thắng giặc xong, vua Quang Trung gọi dân về cày | Loạt Quang Trung",
        yt_tags="chiếu khuyến nông, nông nghiệp, ruộng hoang, 1789, " + YT),
    # ================================================================== Q7 · chữ Nôm
    dict(COMMON, slug="chu-nom-chieu-vua-1791", prefix="qt7", giong=NGHE,
        voices={"village chief": "a fussy, nasal old male voice", "old woman": "a surprised, croaky old woman's voice",
                "old farmer": "a stubborn, loud old male voice"},
        title="Q7 · Bị sai đọc chiếu vua cho cả làng, lần đầu tiên cả làng nghe là hiểu (chữ Nôm thời Quang Trung, 1791)",
        history=("**Lịch sử:** thời Quang Trung, **chữ Nôm** (chữ ghi tiếng Việt) được đề cao: nhiều chiếu, biểu và văn bản của "
                 "triều đình viết bằng chữ Nôm. Năm 1791, vua lập **Viện Sùng Chính** ở Nghệ An, giao La Sơn Phu Tử Nguyễn "
                 "Thiếp đứng đầu, dịch sách chữ Hán ra chữ Nôm (mức B). Trước đó, giấy tờ nhà nước gần như toàn bằng chữ Hán, "
                 "dân thường nghe không hiểu. **Hư cấu:** Anh Tư, ông lý trưởng, dân làng và mọi lời thoại. Chữ trên giấy làm "
                 "mờ, không đọc được."),
        setting=("A village in Nghệ An, 1791: a communal house (đình) yard, villagers gathered on mats, a village chief in a "
                 "dark robe, an edict on paper with a red seal (all writing blurred), later a scholars' hall with old men "
                 f"translating books with brushes. Peasants in brown clothes. Anh Tư is {FACE}, the village crier. {SAFE}"),
        hook="POV: Đọc chiếu vua / cả làng / nghe là hiểu",
        clips=[
            c("Đọc chiếu", "0-5", "Nghệ An · 1791",
              f"First-person view in a communal house yard, a fussy village chief handing {FACE} a sealed edict scroll, villagers gathering on mats",
              ("0-5s: The village chief hands Anh Tư a sealed scroll: \"Đọc chiếu vua cho cả làng nghe.\" Anh Tư: \"Chữ Hán em "
               "đọc như chim hót mà ông?\" The chief: \"Lần này chữ nhà mình.\" 5-10s: Anh Tư unrolls it and blinks: \"Chữ này... "
               "em đọc ra tiếng mình.\""),
              [(0.3, 2.2, "Đọc chiếu vua / cho cả làng nghe."), (2.2, 3.4, "Chữ Hán em đọc / như chim hót mà ông?"),
               (3.4, 4.9, "Lần này chữ nhà mình."), (5.2, 9.5, "Chữ này... / em đọc ra tiếng mình.")]),
            c("Mọi lần", "5-10", "Mấy năm trước",
              f"First-person view of an earlier day in the same yard, {FACE} reading a scroll in a monotone while villagers doze, one snoring",
              ("0-5s: Earlier years: Anh Tư reads a Hán edict in a flat monotone; villagers doze, one snores. 5-10s: Anh Tư to "
               "the viewer: \"Mọi lần em đọc... cả làng ngủ.\""),
              [(5.0, 9.5, "Mọi lần em đọc... / cả làng ngủ.")]),
            c("Cả làng nghe", "5-10", "",
              f"First-person view of villagers leaning forward, wide awake and listening intently as {FACE} reads the edict aloud",
              ("0-5s: Now Anh Tư reads the edict in plain Vietnamese; the villagers lean forward, wide awake. 5-10s: He whispers "
               "to the viewer: \"Lần này em đọc... cả làng vểnh tai.\""),
              [(5.0, 9.5, "Lần này em đọc... / cả làng vểnh tai.")]),
            c("Vua nói thế à", "5-10", "",
              f"First-person view of an old woman in the front row slapping her knee in surprise, villagers nodding, {FACE} holding the edict",
              ("0-5s: An old woman slaps her knee: \"Ơ! Vua nói thế à?\" 5-10s: Anh Tư says quietly to the viewer: \"Lần đầu vua viết... "
               "mà cả làng nghe hiểu.\""),
              [(0.5, 4.8, "Ơ! Vua nói thế à?"), (5.0, 9.5, "Lần đầu vua viết... / mà cả làng nghe hiểu.")]),
            c("Cãi nhau", "5-10", "",
              f"First-person view of two stubborn old farmers arguing loudly over what the edict means, villagers taking sides, {FACE} between them",
              ("0-5s: Two old farmers argue loudly: \"Vua bảo thế này!\" \"Không, vua bảo thế kia!\" 5-10s: Anh Tư, between "
               "them, to the viewer: \"Hiểu được rồi... thì bắt đầu cãi nhau.\""),
              [(0.5, 4.8, "Vua bảo thế này! / Không, vua bảo thế kia!"), (5.0, 9.5, "Hiểu được rồi... / thì bắt đầu cãi nhau.")]),
            c("Viện Sùng Chính", "5-10", "Viện Sùng Chính",
              f"First-person view inside a quiet scholars' hall, old scholars bent over low desks copying and translating books with brushes, {FACE} delivering a basket of paper",
              ("0-5s: Anh Tư delivers paper to a quiet hall where old scholars translate books with brushes. 5-10s: He whispers: "
               "\"Cả viện ngồi... dịch sách ra tiếng mình.\""),
              [(5.0, 9.5, "Cả viện ngồi... / dịch sách ra tiếng mình.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dusk in the village, {FACE} rolling up the edict, villagers walking home still talking about it",
              ("0-4.5s: Dusk; villagers walk home still talking. A calm narrator's voice says: \"Thời Quang Trung, chữ Nôm được "
               "dùng trong chiếu chỉ. Năm 1791, Viện Sùng Chính dịch sách chữ Hán ra chữ Nôm.\" 4.5-10s: Anh Tư rolls up the "
               "edict: \"Vua nói tiếng của dân... thì dân nghe lời vua.\""),
              [(3.0, 6.0, "Thời Quang Trung, chữ Nôm / vào chiếu vua. Năm 1791, / Viện Sùng Chính dịch sách."),
               (6.1, 8.4, "Vua nói tiếng của dân... / thì dân nghe lời vua.")]),
        ],
        caption=("Bị sai đọc chiếu vua cho cả làng, lần đầu cả làng nghe là hiểu 😳 Thời Quang Trung, chữ Nôm (chữ ghi tiếng Việt) "
                 "được dùng trong chiếu chỉ; năm 1791 Viện Sùng Chính dịch sách chữ Hán ra chữ Nôm. Bạn có đọc được chữ Nôm "
                 "không? 👇"),
        tags="#quangtrung #chunom #viensungchinh #taysontungmoc #1791",
        tt_title="Đọc chiếu vua cho cả làng, lần đầu cả làng nghe là hiểu",
        hooks_alt=["POV: Mọi lần đọc chiếu / cả làng ngủ", "POV: Hiểu được rồi / thì bắt đầu cãi nhau"],
        pin=("Người đứng đầu Viện Sùng Chính chính là La Sơn Phu Tử, ông đồ từng từ chối vua ba lần 🔥 Follow để xem loạt Quang "
             "Trung tập tiếp theo!"),
        yt_title="Chữ Nôm vào chiếu vua: lần đầu cả làng nghe là hiểu (1791) | Loạt Quang Trung",
        yt_tags="chữ nôm, viện sùng chính, nguyễn thiếp, la sơn phu tử, 1791, " + YT),
    # ================================================================== Q8 · 1792 cầu hôn
    dict(COMMON, slug="hoi-vo-luong-quang-1792", prefix="qt8",
        voices={"officer": "a stern, clipped male voice", "envoy": "a formal, dignified older male voice"},
        title="Q8 · Khiêng lễ vật đi hỏi vợ cho vua, mà của hồi môn đòi kèm là… hai tỉnh (sứ bộ năm 1792, theo một số sách chép)",
        history=("**Theo một số sách chép (mức B/C, sử còn tranh cãi):** đầu năm 1792, vua Quang Trung sai sứ bộ sang nhà Thanh, "
                 "**cầu hôn một công chúa nhà Thanh và xin đất Lưỡng Quảng** (Quảng Đông, Quảng Tây); văn thư được cho là còn "
                 "chép trong *Bang giao hảo thoại* của Ngô Thì Nhậm. Nhà Thanh chưa trả lời thì **mùa thu năm ấy (16/9/1792), "
                 "vua Quang Trung mất** ở Phú Xuân. Ý định thật của nhà vua còn nhiều cách hiểu. **Hư cấu:** Anh Tư, cảnh khiêng "
                 "lễ vật, cảnh chờ ở biên giới và mọi lời thoại. Không dựng cảnh nhà vua mất, chỉ nhắc bằng lời. Công chúa và "
                 "triều Thanh không xuất hiện."),
        setting=("Vietnam, early 1792: a long diplomatic procession on a mountain road toward the northern border, porters "
                 "carrying red-lacquered gift chests on bamboo poles, an envoy in formal dark court robes, a quiet border post "
                 f"with a wooden gate in the mist. {ARMY} as escorts. Anh Tư is {FACE}, a porter-soldier. {SAFE}"),
        hook="POV: Khiêng lễ vật / đi hỏi vợ / cho vua",
        clips=[
            c("Hỏi vợ", "0-5", "Phú Xuân · đầu năm 1792",
              f"First-person view in a palace courtyard full of red-lacquered gift chests, a stern officer pointing {FACE} to a heavy chest on a bamboo pole",
              ("0-5s: The officer points at a heavy red chest: \"Khiêng lễ vật. Đi hỏi vợ cho vua.\" Anh Tư: \"Hỏi con gái nhà "
               "ai ạ?\" The officer: \"Nhà to nhất phương Bắc.\" 5-10s: Anh Tư shoulders the pole and sighs: \"Em đi hỏi vợ cho "
               "mình... còn chưa xong.\""),
              [(0.3, 2.2, "Khiêng lễ vật. / Đi hỏi vợ cho vua."), (2.2, 3.4, "Hỏi con gái nhà ai ạ?"),
               (3.4, 4.9, "Nhà to nhất phương Bắc."), (5.2, 9.5, "Em đi hỏi vợ cho mình... / còn chưa xong.")]),
            c("Lễ vật", "5-10", "",
              f"First-person view of a long procession of porters carrying dozens of red-lacquered chests along a road, {FACE} counting them and losing count",
              ("0-5s: A long procession of red chests stretches down the road; Anh Tư counts and loses count. 5-10s: He whispers: "
               "\"Lễ nhiều thế này... nhà gái chắc phải ưng.\""),
              [(5.0, 9.5, "Lễ nhiều thế này... / nhà gái chắc phải ưng.")]),
            c("Danh sách", "5-10", "",
              f"First-person view at a roadside rest, a dignified envoy in dark court robes reading from an unrolled list (no legible writing) to his staff, {FACE} listening with his mouth open",
              ("0-5s: At a rest stop the envoy reads the list to his staff: \"Xin cưới công chúa... và xin đất Lưỡng Quảng.\" "
               "5-10s: Anh Tư nearly drops his pole: \"Xin... cái gì cơ ạ?\""),
              [(0.5, 4.8, "Xin cưới công chúa... / và xin đất Lưỡng Quảng."), (5.0, 9.5, "Xin... / cái gì cơ ạ?")]),
            c("Của hồi môn", "5-10", "",
              f"First-person view as {FACE} turns to the viewer on the mountain road, the procession behind him, a stunned, disbelieving look",
              ("0-5s: Anh Tư walks on, still stunned. 5-10s: He turns to the viewer: \"Đi hỏi vợ... mà đòi của hồi môn là hai "
               "tỉnh.\""),
              [(5.0, 9.5, "Đi hỏi vợ... / mà đòi của hồi môn / là hai tỉnh.")]),
            c("Đường xa", "5-10", "",
              f"First-person view from a high mountain road looking north over misty ridges, the procession winding ahead, {FACE} resting the pole on his shoulder",
              ("0-5s: The procession winds through misty northern ridges. 5-10s: Anh Tư, resting, to the viewer: \"Ngày xưa người "
               "ta sang đánh mình... giờ mình sang hỏi vợ.\""),
              [(5.0, 9.5, "Ngày xưa người ta / sang đánh mình... / giờ mình sang hỏi vợ.")]),
            c("Chờ hồi âm", "5-10", "",
              f"First-person view at a quiet misty border post with a wooden gate, the gift chests stacked, porters waiting and dozing, {FACE} staring at the closed gate",
              ("0-5s: At a quiet border post the chests are stacked; days pass; the gate stays closed. 5-10s: Anh Tư sighs: \"Chờ "
               "mãi... nhà gái chưa trả lời.\""),
              [(5.0, 9.5, "Chờ mãi... / nhà gái chưa trả lời.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dusk on the road home in autumn, falling leaves, {FACE} walking slowly with the pole, looking down, then up at the camera with quiet pride",
              ("0-4.5s: Autumn dusk on the road home. A calm narrator's voice says: \"Theo một số sách chép, năm 1792 vua Quang "
               "Trung sai sứ cầu hôn công chúa nhà Thanh và xin đất Lưỡng Quảng. Chưa có hồi âm, mùa thu năm ấy, vua mất.\" "
               "4.5-10s: Anh Tư looks up at the camera: \"Đám hỏi chưa xong... mà cả nước đã nhớ ông ấy.\""),
              [(3.0, 6.0, "Năm 1792, vua sai sứ / cầu hôn, xin Lưỡng Quảng. / Mùa thu năm ấy, vua mất."),
               (6.1, 8.4, "Đám hỏi chưa xong... / mà cả nước đã nhớ ông ấy.")]),
        ],
        caption=("Khiêng lễ vật đi hỏi vợ cho vua, mà của hồi môn đòi kèm là hai tỉnh 😳 Theo một số sách chép, năm 1792 vua Quang "
                 "Trung sai sứ sang nhà Thanh cầu hôn công chúa và xin đất Lưỡng Quảng. Sử còn tranh cãi về ý định thật. Bạn "
                 "nghĩ sao? 👇"),
        tags="#quangtrung #luongquang #taysontungmoc #lichsuvietnam #1792",
        tt_title="Khiêng lễ vật đi hỏi vợ cho vua, mà của hồi môn đòi kèm là hai tỉnh",
        hooks_alt=["POV: Đi hỏi vợ / mà đòi hồi môn / là hai tỉnh", "POV: Ngày xưa người ta sang đánh mình / giờ mình sang hỏi vợ"],
        pin=("Chuyện cầu hôn và xin Lưỡng Quảng có trong một số sách, sử còn tranh cãi 🤔 Tập này khép lại loạt Quang Trung. Bạn "
             "muốn xem loạt nào tiếp theo?"),
        yt_title="Năm 1792: vua Quang Trung cầu hôn công chúa nhà Thanh, xin Lưỡng Quảng? | Loạt Quang Trung",
        yt_tags="lưỡng quảng, cầu hôn công chúa nhà thanh, bang giao hảo thoại, 1792, " + YT),
    # ================================================================== Tập 9 · Lời dụ "Đánh cho để dài tóc" (truyền tụng)
    dict(COMMON, slug="loi-du-danh-cho-de-dai-toc-1788", prefix="qt9",
        nhan="AI tái hiện · lời dụ theo truyền tụng",
        voices={"Quang Trung": QT_VOICE,
                "officer": "a short, stern, low male voice",
                "old soldier": "a raspy, low whisper of an old male soldier"},
        title="Tập 9 · Đứng giữa mấy vạn quân nghe vua đọc lời dụ: \"Đánh cho để dài tóc, đánh cho để đen răng\" (cuối năm 1788, theo truyền tụng)",
        history=("**Truyền tụng (mức C):** trên đường ra Bắc đánh quân Thanh cuối năm 1788, vua Quang Trung dụ tướng sĩ:\n\n"
                 "> *Đánh cho để dài tóc,*  \n> *Đánh cho để đen răng,*  \n> *Đánh cho nó chích luân bất phản* (không một bánh "
                 "xe quay về),  \n> *Đánh cho nó phiến giáp bất hoàn* (không một mảnh giáp trở về),  \n> *Đánh cho sử tri Nam "
                 "quốc anh hùng chi hữu chủ* (cho sử biết nước Nam anh hùng là có chủ).\n\n"
                 "Các nguồn ghi nơi đọc khác nhau: lễ thệ sư ở Thọ Hạc, Thanh Hóa (Bảo tàng Lịch sử Quốc gia) hoặc lễ lên ngôi ở "
                 "núi Bân, 22/12/1788 (báo Quân đội nhân dân). *Hoàng Lê nhất thống chí* **không chép** câu này; chưa tìm thấy văn "
                 "bản gốc, nên video gắn nhãn \"lời dụ theo truyền tụng\" và dựng ở **lễ thệ sư** (không nêu tên địa danh trong "
                 "phim). \"Dài tóc, đen răng\" là phong tục của người Việt thời ấy. Hơn một tháng sau, mùng 5 Tết Kỷ Dậu (1789), "
                 "vua vào Thăng Long (mức B). **Hư cấu:** Anh Tư, viên chỉ huy, ông lính già và lời thoại của họ. Không dựng cảnh "
                 "đánh nhau."),
        setting=("Vietnam, late 1788, dawn: an oath-taking ceremony (lễ thệ sư) on a vast open field, tens of thousands of "
                 f"soldiers in silent ranks, war drums, war elephants, rows of torches still burning in the mist. {ARMY}. "
                 f"{QT_LOOK} Men have long hair in topknots and black-lacquered teeth. Anh Tư is {FACE}, a soldier in the "
                 f"ranks. {SAFE}"),
        hook="POV: Đứng giữa / mấy vạn quân / nghe vua đọc lời dụ",
        clips=[
            c("Hôm nay vua nói", "0-5", "Lễ thệ sư · cuối năm 1788",
              f"First-person view from inside silent ranks at dawn, a stern officer walking along the line straightening a spear, stopping beside {FACE}",
              ("0-5s: The officer straightens Anh Tư's spear: \"Đứng thẳng. Hôm nay vua nói.\" Anh Tư whispers: \"Nói với cả "
               "mấy vạn người ạ?\" The officer: \"Nghe bằng cả ngực mày.\" 5-10s: Anh Tư looks along the endless silent ranks "
               "and whispers: \"Mấy vạn người... im đến nghe được tiếng đuốc cháy.\""),
              [(0.3, 2.2, "Đứng thẳng. / Hôm nay vua nói."), (2.2, 3.4, "Nói với cả mấy vạn người ạ?"),
               (3.4, 4.9, "Nghe bằng cả ngực mày."), (5.2, 9.5, "Mấy vạn người... / im đến nghe được / tiếng đuốc cháy.")]),
            c("Vua bước lên đài", "5-10", "Vua Quang Trung",
              f"First-person view from the ranks toward a high wooden platform, {QT_SHOT}, climbing the steps, the drummers lowering their sticks, {FACE} holding his breath",
              ("0-5s: Three great drumbeats, then silence. Quang Trung, seen only from behind, climbs onto the high platform and "
               "turns to face the army; we only see his back and broad shoulders. 5-10s: Anh Tư whispers very low: \"Vua chưa nói "
               "câu nào... cả bãi đã đứng thẳng.\""),
              [(0.5, 4.8, "(Ba hồi trống)"), (5.0, 9.5, "Vua chưa nói câu nào... / cả bãi đã đứng thẳng.")]),
            c("Dài tóc, đen răng", "5-10", "Vua Quang Trung",
              f"First-person view from the ranks looking up at {QT_SHOT}, his right arm raised high with a sword, the army frozen, {FACE} in the foreground with his mouth firmly closed",
              ("0-5s: Quang Trung, seen only from behind on the platform, slowly raises his sword. 5-10s: ONLY Quang Trung "
               "speaks, his voice booming across the field from the platform; Anh Tư and the soldiers keep their mouths closed: "
               "\"Đánh cho để dài tóc! Đánh cho để đen răng!\""),
              [(5.0, 7.2, "Vua Quang Trung: / Đánh cho để dài tóc!"), (7.2, 9.5, "Vua Quang Trung: / Đánh cho để đen răng!")]),
            c("Không một bánh xe", "5-10", "Vua Quang Trung",
              f"First-person low-angle view of {QT_SHOT} on the platform against the rising sun, sword pointing north, rows of spears below, {FACE} silent in the ranks",
              ("0-5s: Quang Trung, seen only from behind, turns and points his sword north. 5-10s: ONLY Quang Trung speaks, "
               "each phrase like a war drum; no one else's lips move: \"Đánh cho nó chích luân bất phản! Đánh cho nó phiến giáp "
               "bất hoàn!\""),
              [(5.0, 7.2, "Vua Quang Trung: / Đánh cho nó / chích luân bất phản!"), (7.2, 9.5, "Vua Quang Trung: / Đánh cho nó / phiến giáp bất hoàn!")]),
            c("Nghĩa là gì", "5-10", "",
              f"Close first-person view inside the ranks, {FACE} leaning slightly toward an old soldier with a grey topknot beside him, both whispering without moving their heads",
              ("0-5s: The echo of the king's voice fades. Anh Tư leans toward the old soldier beside him. 5-10s: Anh Tư, very "
               "low: \"Chích luân... là gì hả bác?\" The old soldier, without turning his head: \"Không một cái xe, không một mảnh "
               "giáp nào của giặc được về.\""),
              [(5.0, 6.6, "Chích luân... / là gì hả bác?"), (6.6, 9.5, "Không một cái xe, / không một mảnh giáp / nào được về.")]),
            c("Nam quốc anh hùng", "5-10", "Vua Quang Trung",
              f"First-person wide view of {QT_SHOT} on the platform with both arms raised, tens of thousands of spears rising like a forest, {FACE} raising his spear with them",
              ("0-5s: Quang Trung, seen only from behind, lifts both arms. 5-10s: ONLY Quang Trung speaks, the loudest line of "
               "all: \"Đánh cho sử tri Nam quốc anh hùng chi hữu chủ!\" Then the whole army roars \"Đánh!\" and raises their "
               "spears."),
              [(5.0, 8.4, "Vua Quang Trung: / Đánh cho sử tri / Nam quốc anh hùng / chi hữu chủ!"), (8.4, 9.6, "ĐÁNH!")]),
            c("Câu chốt", "3-10", "",
              f"First-person view as the army begins to march north at sunrise, {FACE} marching with his spear upright, glancing back once at the empty platform",
              ("0-4.5s: The army marches north at sunrise. A calm, quiet narrator's voice (clearly different from the king's) "
               "says: \"Theo truyền tụng, cuối năm 1788, vua Quang Trung dụ tướng sĩ như thế. Mùng 5 Tết Kỷ Dậu, vua vào Thăng "
               "Long.\" 4.5-10s: Anh Tư, marching, says quietly to the camera: \"Em không hiểu hết chữ của vua... nhưng em hiểu "
               "phải đánh.\""),
              [(3.0, 6.0, "Theo truyền tụng, năm 1788, / vua Quang Trung dụ tướng sĩ. / Mùng 5 Tết, vào Thăng Long."),
               (6.1, 8.4, "Em không hiểu hết / chữ của vua... / nhưng em hiểu phải đánh.")]),
        ],
        caption=("\"Đánh cho để dài tóc, đánh cho để đen răng...\" 🔥 Theo truyền tụng, cuối năm 1788, trên đường ra Bắc đánh "
                 "quân Thanh, vua Quang Trung dụ tướng sĩ bằng năm câu này. Hơn một tháng sau, mùng 5 Tết Kỷ Dậu, vua vào Thăng "
                 "Long. Bạn thuộc được mấy câu? 👇"),
        tags="#quangtrung #danhchodedaitoc #danhchodedenrang #taysontungmoc #1788",
        tt_title="Vua Quang Trung đọc lời dụ: Đánh cho để dài tóc, đánh cho để đen răng",
        hooks_alt=["POV: Đánh cho để dài tóc / đánh cho để đen răng", "POV: Vua chưa nói câu nào / cả bãi đã đứng thẳng"],
        pin=("Năm câu đầy đủ: dài tóc · đen răng · chích luân bất phản · phiến giáp bất hoàn · sử tri Nam quốc anh hùng chi hữu "
             "chủ 🔥 Đây là lời truyền tụng, sách Hoàng Lê nhất thống chí không chép. Bạn nghe câu này lần đầu ở đâu?"),
        yt_title="\"Đánh cho để dài tóc, đánh cho để đen răng\": lời dụ của vua Quang Trung | Loạt Quang Trung",
        yt_tags=("đánh cho để dài tóc, đánh cho để đen răng, chích luân bất phản, phiến giáp bất hoàn, nam quốc anh hùng chi "
                 "hữu chủ, lễ thệ sư, 1788, " + YT)),
    # ================================================================== Tập 10 · Thầy giáo Hiến (trước 1771)
    dict(COMMON, slug="thay-giao-hien-an-thai", prefix="qt10", giong="Central Vietnamese (Bình Định) accent",
        nhan="AI tái hiện · có chi tiết truyền tụng",
        voices={"teacher": "a slow, dry, wise old male voice with a Nghệ An accent, few words",
                "officer": "a short, stern male voice"},
        title="Tập 10 · Gánh nước cho một ông thầy dạy cả chữ lẫn võ, ai ngờ học trò của thầy sau này thành vua (thầy Hiến, An Thái, trước 1771)",
        history=("**Lịch sử:** Trương Văn Hiến (thường gọi giáo Hiến), người xứ Nghệ, từng là môn khách của Thái phó Trương "
                 "Văn Hạnh; khi ông Hạnh bị Trương Phúc Loan giết, ông lánh vào Quy Nhơn, mở trường ở ấp An Thái, **dạy anh em "
                 "Nguyễn Nhạc, Nguyễn Lữ, Nguyễn Huệ cả văn lẫn võ** (sử nhà Nguyễn, *Lịch sử Việt Nam* tập 4, mức B; quê quán "
                 "các nguồn ghi khác nhau). **Truyền tụng (mức C):** thầy để lại cho học trò câu sấm \"Tây khởi nghĩa, Bắc thu "
                 "công\". **Hư cấu:** Anh Tư, việc gánh nước, làm cọc tập võ và mọi lời thoại. Ba anh em đã là người lớn, chỉ "
                 "thấy từ phía sau."),
        setting=("An Thái hamlet (Bình Định), late 1760s: a thatched village school under big trees, low desks, ink stones, "
                 "a sandy yard with wooden staffs and a practice post, a well, rice fields and the Tây Sơn hills behind. A thin "
                 "old teacher with a long white beard in a faded dark robe. His students are ADULT young men in brown clothes "
                 f"with topknots, the three Nguyễn brothers seen ONLY from behind. Anh Tư is {FACE}, the school's handyman. "
                 f"{SAFE}"),
        hook="POV: Gánh nước / cho ông thầy / dạy cả chữ lẫn võ",
        clips=[
            c("Bút và gậy", "0-5", "An Thái · trước năm 1771",
              f"First-person view in a village school yard, a thin old teacher with a white beard handing {FACE} a carrying pole with two buckets, a wooden staff and a writing brush lying side by side on a bench",
              ("0-5s: The old teacher hands Anh Tư a carrying pole: \"Sáng gánh nước. Chiều cầm gậy.\" Anh Tư: \"Em học chữ "
               "hay học võ ạ?\" The teacher: \"Học cả hai mới đủ một người.\" 5-10s: Anh Tư looks at the bench and murmurs: "
               "\"Trường gì... mà bút với gậy để chung một góc.\""),
              [(0.3, 2.2, "Sáng gánh nước. / Chiều cầm gậy."), (2.2, 3.4, "Em học chữ / hay học võ ạ?"),
               (3.4, 4.9, "Học cả hai / mới đủ một người."), (5.2, 9.5, "Trường gì... / mà bút với gậy / để chung một góc.")]),
            c("Buổi sáng", "5-10", "",
              f"First-person view inside the thatched school in the morning, adult students bent over low desks writing with brushes, {FACE} at the back grinding ink with blackened fingers",
              ("0-5s: Morning; adult students write quietly; Anh Tư grinds ink at the back. 5-10s: He looks at his black "
               "fingers and says quietly to the viewer: \"Sáng mài mực... tay đen.\""),
              [(5.0, 9.5, "Sáng mài mực... / tay đen.")]),
            c("Buổi chiều", "5-10", "",
              f"First-person view in the sandy yard in the afternoon, adult students practicing with long wooden staffs, the three brothers seen only from behind, {FACE} holding a padded practice post that is being struck",
              ("0-5s: Afternoon; students practice with staffs; Anh Tư holds the padded practice post as the blows land, wincing. "
               "5-10s: He rubs his arm: \"Chiều làm cọc cho người ta tập... tay tím.\""),
              [(5.0, 9.5, "Chiều làm cọc / cho người ta tập... / tay tím.")]),
            c("Văn và võ", "5-10", "",
              f"First-person view of the old teacher standing between the desks and the sandy yard, speaking to the students, {FACE} listening while holding both a brush and a staff",
              ("0-5s: The teacher addresses the students: \"Văn mà không võ thì yếu. Võ mà không văn thì liều.\" 5-10s: Anh Tư, "
               "holding a brush in one hand and a staff in the other, sighs: \"Thầy dạy một câu... em nhớ được nửa câu.\""),
              [(0.5, 4.8, "Văn mà không võ thì yếu. / Võ mà không văn thì liều."),
               (5.0, 9.5, "Thầy dạy một câu... / em nhớ được nửa câu.")]),
            c("Sáu chữ", "5-10", "",
              f"First-person view at night through a half-open door, the old teacher by an oil lamp speaking quietly to an adult student seen only from behind, {FACE} outside holding a bucket, listening",
              ("0-5s: At night, by an oil lamp, the teacher speaks quietly to the eldest student: \"Tây khởi nghĩa, Bắc thu "
               "công.\" 5-10s: Outside the door, Anh Tư holds his breath: \"Sáu chữ thôi... mà nghe như sấm.\""),
              [(0.5, 4.8, "Tây khởi nghĩa, / Bắc thu công."), (5.0, 9.5, "Sáu chữ thôi... / mà nghe như sấm.")]),
            c("Lên núi", "5-10", "",
              f"First-person view at dawn as the three brothers, seen only from behind, walk out of the hamlet toward the hills with swords and bundles, {FACE} left standing by the well with two buckets",
              ("0-5s: Dawn; the three brothers, seen only from behind, walk off toward the hills with swords and bundles. "
               "5-10s: Anh Tư, left by the well with his buckets: \"Họ mang gươm lên núi... em ở lại với hai thùng nước.\""),
              [(5.0, 9.5, "Họ mang gươm lên núi... / em ở lại / với hai thùng nước.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view years later at the same well, an older {FACE} drawing water, looking up as distant drums sound from the hills",
              ("0-4.5s: Years later at the same well. A calm narrator's voice says: \"Thầy Trương Văn Hiến dạy anh em Tây Sơn "
               "cả văn lẫn võ. Người học trò nhỏ nhất, sau này là vua Quang Trung.\" 4.5-10s: Anh Tư sets down the bucket and "
               "says quietly to the camera: \"Cùng học một thầy... người thành vua, em vẫn gánh nước.\""),
              [(3.0, 6.0, "Thầy Trương Văn Hiến / dạy anh em Tây Sơn / cả văn lẫn võ."),
               (6.1, 8.4, "Cùng học một thầy... / người thành vua, / em vẫn gánh nước.")]),
        ],
        caption=("Gánh nước cho một ông thầy dạy cả chữ lẫn võ, ai ngờ học trò của thầy sau này thành vua 😳 Thầy Trương Văn "
                 "Hiến ở An Thái dạy anh em Tây Sơn văn võ song toàn. Bạn còn nhớ thầy cô nào dạy mình không? 👇"),
        tags="#quangtrung #truongvanhien #tayson #binhdinh #thaygiao",
        tt_title="Gánh nước cho ông thầy dạy cả chữ lẫn võ, ai ngờ học trò sau này thành vua",
        hooks_alt=["POV: Cùng học một thầy / người thành vua", "POV: Bút với gậy / để chung một góc"],
        pin=("Câu \"Tây khởi nghĩa, Bắc thu công\" là truyền tụng, sử chưa chép rõ 🤔 Bạn có biết võ Bình Định nổi tiếng từ "
             "đâu không? Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="Thầy giáo Hiến: người dạy văn võ cho anh em Tây Sơn | Loạt Quang Trung",
        yt_tags="trương văn hiến, giáo hiến, an thái, võ bình định, văn võ song toàn, " + YT),
    # ================================================================== Tập 11 · Nguyễn Thiếp "không quá mười ngày" (cuối 1788)
    dict(COMMON, slug="khong-qua-muoi-ngay-1788", prefix="qt11", giong=NGHE,
        voices={"Quang Trung": QT_VOICE,
                "Nguyễn Thiếp": "a calm, thin, unhurried old male voice with a Nghệ An accent, wise and certain",
                "officer": "a short, stern male voice", "comrade": "a cheeky young adult male voice"},
        title="Tập 11 · Đi mời ông đồ từng từ chối vua, ông chỉ nói một câu mà cả quân yên lòng (\"không quá mười ngày\", 1788)",
        history=("**Lịch sử:** cuối năm 1788, trên đường ra Bắc, ở Nghệ An vua Quang Trung hỏi ý La Sơn Phu Tử Nguyễn Thiếp: "
                 "*\"Quân Thanh sang đánh, tôi sắp đem binh ra chống cự. Mưu đánh và giữ, cơ được hay thua, tiên sinh nghĩ như "
                 "thế nào?\"* Nguyễn Thiếp đáp: *\"Chúa công đi ra chuyến này, không quá mười ngày, quân Thanh sẽ bị dẹp tan.\"* "
                 "(*Hoàng Lê nhất thống chí*, hồi 14, mức B/C). Mùng 5 Tết Kỷ Dậu, vua vào Thăng Long. Trước đó Nguyễn Thiếp "
                 "nhiều lần từ chối ra làm quan (xem tập \"Đưa thư mời La Sơn Phu Tử\"). **Hư cấu:** Anh Tư, việc đi mời, việc "
                 "cược bánh chưng và lời thoại của Anh Tư, viên chỉ huy, người đồng đội. Lời vua và lời Nguyễn Thiếp theo sách."),
        setting=("Nghệ An, late December 1788: a simple scholar's house at the foot of a mountain, then a lamplit army tent. "
                 "Nguyễn Thiếp is a thin, very old scholar with a long white beard in a plain dark robe and black turban, "
                 f"calm. {QT_LOOK} {ARMY}. Anh Tư is {FACE}, a soldier. {SAFE}"),
        hook="POV: Đi mời ông đồ / từng từ chối vua",
        clips=[
            c("Mời bằng được", "0-5", "Nghệ An · cuối năm 1788",
              f"First-person view at an army camp, a stern officer pointing toward a mountain path, {FACE} tightening his sandals",
              ("0-5s: The officer points up the mountain path: \"Đi mời ông đồ. Mời bằng được.\" Anh Tư: \"Ông ấy từ chối vua "
               "mấy lần rồi mà?\" The officer: \"Lần này nước có giặc.\" 5-10s: Anh Tư sets off and says quietly to the viewer: "
               "\"Mời mấy năm không được... giặc đến thì chắc được.\""),
              [(0.3, 2.2, "Đi mời ông đồ. / Mời bằng được."), (2.2, 3.4, "Ông ấy từ chối vua / mấy lần rồi mà?"),
               (3.4, 4.9, "Lần này / nước có giặc."), (5.2, 9.5, "Mời mấy năm không được... / giặc đến thì chắc được.")]),
            c("Ông đồ đứng dậy", "5-10", "",
              f"First-person view at the door of a simple scholar's house, a very old scholar with a long white beard silently putting on his outer robe and picking up his walking stick, {FACE} at the door, surprised",
              ("0-5s: Anh Tư bows at the door and starts his speech; the old scholar, without a word, puts on his robe and "
               "picks up his stick. 5-10s: Anh Tư, surprised, to the viewer: \"Em chưa nói hết câu... ông ấy đã đứng dậy đi.\""),
              [(5.0, 9.5, "Em chưa nói hết câu... / ông ấy đã đứng dậy đi.")]),
            c("Vua cúi đầu", "5-10", "Vua Quang Trung",
              f"First-person view inside a lamplit tent, {QT_SHOT}, bowing his head respectfully to the old scholar who has just entered, {FACE} at the tent flap",
              ("0-5s: In the lamplit tent the emperor, seen only from behind, rises and bows his head to the old scholar. "
               "5-10s: Anh Tư whispers at the tent flap: \"Vua cầm mấy vạn quân... mà cúi đầu trước ông đồ.\""),
              [(5.0, 9.5, "Vua cầm mấy vạn quân... / mà cúi đầu trước ông đồ.")]),
            c("Vua hỏi", "5-10", "Vua Quang Trung",
              f"First-person view from the tent flap, {QT_SHOT}, leaning toward the old scholar across a low table, {FACE} silent in the foreground",
              ("0-5s: The emperor sits across a low table from the old scholar. 5-10s: ONLY Quang Trung speaks, his deep voice "
               "low and serious; Anh Tư keeps his mouth closed: \"Mưu đánh và giữ, cơ được hay thua, tiên sinh nghĩ thế nào?\""),
              [(5.0, 9.5, "Vua Quang Trung: / Mưu đánh và giữ, / được hay thua, / tiên sinh nghĩ thế nào?")]),
            c("Mười ngày", "5-10", "Nguyễn Thiếp",
              f"First-person view of the very old scholar Nguyễn Thiếp across the low table, calm, raising one thin hand, {QT_SHOT} listening, {FACE} silent at the edge of frame",
              ("0-5s: The old scholar is quiet for a moment, then raises one thin hand. 5-10s: ONLY Nguyễn Thiếp speaks, calm "
               "and certain; no one else's lips move: \"Chúa công đi ra chuyến này, không quá mười ngày, quân Thanh sẽ bị dẹp "
               "tan.\""),
              [(5.0, 9.5, "Nguyễn Thiếp: / Không quá mười ngày, / quân Thanh / sẽ bị dẹp tan.")]),
            c("Cược", "5-10", "",
              f"First-person view outside the tent at night, {FACE} and a cheeky comrade crouching by a campfire, the comrade holding up half a bánh chưng",
              ("0-5s: By the fire the comrade holds up half a bánh chưng: \"Mười ngày? Tao cược nửa cái bánh.\" 5-10s: Anh Tư, "
               "quietly: \"Ông đồ không cầm gươm... mà nói chắc hơn tướng.\""),
              [(0.5, 4.8, "Mười ngày? / Tao cược nửa cái bánh."), (5.0, 9.5, "Ông đồ không cầm gươm... / mà nói chắc hơn tướng.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view in the afternoon at a Thăng Long gate, soldiers marching in, {FACE} counting days on his fingers, the comrade handing him half a bánh chưng",
              ("0-4.5s: At a Thăng Long gate the army marches in; the comrade hands Anh Tư the half bánh chưng. A calm narrator's "
               "voice says: \"Theo Hoàng Lê nhất thống chí, Nguyễn Thiếp đoán không quá mười ngày. Mùng 5 Tết, vua vào Thăng "
               "Long.\" 4.5-10s: Anh Tư counts on his fingers and says quietly: \"Ông đồ đoán mười ngày... vua không để đến ngày "
               "thứ mười.\""),
              [(3.0, 6.0, "Nguyễn Thiếp đoán / không quá mười ngày. / Mùng 5 Tết, vào Thăng Long."),
               (6.1, 8.4, "Ông đồ đoán mười ngày... / vua không để đến / ngày thứ mười.")]),
        ],
        caption=("Đi mời ông đồ từng từ chối vua, ông chỉ nói một câu mà cả quân yên lòng 🔥 \"Chúa công đi ra chuyến này, không "
                 "quá mười ngày, quân Thanh sẽ bị dẹp tan.\" Cuối năm 1788, La Sơn Phu Tử Nguyễn Thiếp nói với vua Quang Trung "
                 "như thế. Bạn tin lời đoán ấy không? 👇"),
        tags="#quangtrung #nguyenthiep #lasonphutu #taysontungmoc #1788",
        tt_title="Đi mời ông đồ từng từ chối vua, ông chỉ nói một câu mà cả quân yên lòng",
        hooks_alt=["POV: Không quá mười ngày / quân Thanh sẽ tan", "POV: Vua cầm mấy vạn quân / mà cúi đầu trước ông đồ"],
        pin=("Đây là ông đồ từng từ chối vua mấy lần, xem tập \"Đưa thư mời La Sơn Phu Tử\" 🔥 Follow để xem loạt Quang Trung "
             "tập tiếp theo!"),
        yt_title="\"Không quá mười ngày\": lời đoán của La Sơn Phu Tử với vua Quang Trung | Loạt Quang Trung",
        yt_tags="nguyễn thiếp, la sơn phu tử, không quá mười ngày, hoàng lê nhất thống chí, nghệ an, 1788, " + YT),
    # ================================================================== Tập 12 · Tam Điệp "Quân thua chém tướng" (cuối 1788)
    dict(COMMON, slug="quan-thua-chem-tuong-tam-diep-1788", prefix="qt12",
        voices={"Quang Trung": QT_VOICE, "officer": "a short, stern male voice",
                "comrade": "a nervous young adult male voice"},
        title="Tập 12 · Bỏ Thăng Long chạy về núi, giờ đứng chờ vua xử tội, vua chỉ nói một câu (Tam Điệp, cuối năm 1788)",
        history=("**Lịch sử:** khi quân Thanh vào Thăng Long, tướng Tây Sơn Ngô Văn Sở, Phan Văn Lân theo kế của Ngô Thì Nhậm "
                 "rút quân về giữ Tam Điệp. Vua Quang Trung ra đến nơi, các tướng xin chịu tội. Vua nói: *\"Binh pháp dạy rằng: "
                 "'Quân thua chém tướng'\"*, rồi giải thích việc để Ngô Thì Nhậm ở lại *\"chính là lo về điều đó\"*, tha tội và "
                 "khen việc giữ quân; vua nói thêm *\"Chẳng qua mươi ngày có thể đuổi được người Thanh\"* và *\"Chờ mười năm "
                 "nữa... bấy giờ nước giàu quân mạnh, thì ta có sợ gì chúng?\"* (*Hoàng Lê nhất thống chí*, hồi 14, mức B/C; "
                 "lời trong phim rút gọn từ sách). **Hư cấu:** Anh Tư, người đồng đội và lời thoại của họ. Không dựng cảnh xử tội."),
        setting=("Tam Điệp pass (Ninh Bình), late January 1789: a camp among limestone mountains, cold mist, campfires. Two "
                 "Tây Sơn generals in dark armor kneeling respectfully, seen from the side at a distance; Ngô Thì Nhậm is a "
                 f"thin scholar-official in a dark robe. {QT_LOOK} {ARMY}. Anh Tư is {FACE}, a soldier who retreated from "
                 f"Thăng Long. {SAFE}"),
        hook="POV: Bỏ Thăng Long / chạy về núi / giờ chờ vua xử",
        clips=[
            c("Đứng cuối hàng", "0-5", "Tam Điệp · cuối năm 1788",
              f"First-person view in a misty mountain camp, a stern officer pushing {FACE} into the last row of a long line of soldiers waiting for someone",
              ("0-5s: The officer pushes Anh Tư into the last row: \"Ra đón vua. Đứng cuối hàng.\" Anh Tư: \"Mình bỏ Thăng Long "
               "chạy về... vua có giận không?\" The officer: \"Cầu cho vua đừng nhớ mặt mày.\" 5-10s: Anh Tư pulls his head "
               "wrap lower and says quietly: \"Đứng cuối hàng... vẫn thấy mình cao quá.\""),
              [(0.3, 2.2, "Ra đón vua. / Đứng cuối hàng."), (2.2, 3.4, "Vua có giận không?"),
               (3.4, 4.9, "Cầu cho vua / đừng nhớ mặt mày."), (5.2, 9.5, "Đứng cuối hàng... / vẫn thấy mình cao quá.")]),
            c("Xin chịu tội", "5-10", "",
              f"First-person view from the ranks, two generals in dark armor kneeling and bowing their heads before {QT_SHOT}, the whole camp silent, {FACE} holding his breath",
              ("0-5s: Two generals kneel and bow their heads before the emperor, seen only from behind. The whole camp is "
               "silent. 5-10s: Anh Tư whispers: \"Hai ông tướng quỳ xin chịu tội... cả trại không ai dám thở.\""),
              [(5.0, 9.5, "Hai ông tướng quỳ / xin chịu tội... / cả trại không ai dám thở.")]),
            c("Quân thua chém tướng", "5-10", "Vua Quang Trung",
              f"First-person view from the ranks of {QT_SHOT} standing over the kneeling generals, the mist swirling, {FACE} swallowing hard, mouth closed",
              ("0-5s: The emperor, seen only from behind, looks down at the kneeling generals. 5-10s: ONLY Quang Trung speaks, "
               "slow and heavy; no one else's lips move: \"Binh pháp dạy rằng: Quân thua chém tướng.\" Anh Tư swallows hard."),
              [(5.0, 9.5, "Vua Quang Trung: / Binh pháp dạy rằng: / Quân thua chém tướng.")]),
            c("Là kế", "5-10", "Vua Quang Trung",
              f"First-person view of {QT_SHOT} gesturing toward a thin scholar-official in a dark robe standing aside, the kneeling generals lifting their heads, {FACE} blinking in surprise",
              ("0-5s: ONLY Quang Trung speaks, gesturing toward the thin scholar-official: \"Ta để Ngô Thì Nhậm ở lại... chính "
               "là lo về điều đó.\" The generals lift their heads. 5-10s: Anh Tư whispers: \"Tưởng bị xử vì chạy... hóa ra chạy "
               "đúng kế.\""),
              [(0.5, 4.8, "Vua Quang Trung: / Ta để Ngô Thì Nhậm ở lại... / chính là lo về điều đó."),
               (5.0, 9.5, "Tưởng bị xử vì chạy... / hóa ra chạy đúng kế.")]),
            c("Mươi ngày", "5-10", "Vua Quang Trung",
              f"First-person wide view of {QT_SHOT} turning to the whole army with one arm pointing north toward the mist, soldiers straightening, {FACE} silent",
              ("0-5s: The emperor turns to the whole army and points north. 5-10s: ONLY Quang Trung speaks: \"Chẳng qua mươi "
               "ngày có thể đuổi được người Thanh.\" A murmur runs through the ranks."),
              [(5.0, 9.5, "Vua Quang Trung: / Chẳng qua mươi ngày / có thể đuổi được người Thanh.")]),
            c("Mười năm", "5-10", "",
              f"First-person view of {QT_SHOT} speaking quietly to the generals and the scholar-official by a campfire, {FACE} nearby feeding the fire, listening",
              ("0-5s: By the fire, the emperor speaks quietly to the generals: \"Chờ mười năm nữa, nước giàu quân mạnh, thì ta "
               "có sợ gì chúng?\" 5-10s: Anh Tư, feeding the fire, says quietly to the viewer: \"Đánh giặc thì hẹn mười ngày... "
               "lo nước thì tính mười năm.\""),
              [(0.5, 4.8, "Vua Quang Trung: / Chờ mười năm nữa, / nước giàu quân mạnh, / thì ta có sợ gì chúng?"),
               (5.0, 9.5, "Đánh giặc hẹn mười ngày... / lo nước tính mười năm.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dusk as the army forms up to march north out of the pass, {FACE} shouldering his spear, looking toward the road he fled down",
              ("0-4.5s: Dusk; the army forms up to march north. A calm narrator's voice says: \"Ở Tam Điệp, vua Quang Trung tha "
               "tội cho các tướng đã rút khỏi Thăng Long, vì đó là kế giữ quân.\" 4.5-10s: Anh Tư shoulders his spear and says "
               "quietly to the camera: \"Em chạy từ Thăng Long về... giờ được chạy ra Thăng Long.\""),
              [(3.0, 6.0, "Ở Tam Điệp, vua tha tội / cho các tướng rút quân, / vì đó là kế giữ quân."),
               (6.1, 8.4, "Em chạy từ Thăng Long về... / giờ được chạy ra Thăng Long.")]),
        ],
        caption=("Bỏ Thăng Long chạy về núi, giờ đứng chờ vua xử tội 😳 Vua Quang Trung nói: \"Quân thua chém tướng\"... rồi tha, vì "
                 "rút về Tam Điệp là kế giữ quân của Ngô Thì Nhậm. Bạn đã xem tập \"rút về Tam Điệp\" chưa? 👇"),
        tags="#quangtrung #tamdiep #ngothinham #taysontungmoc #1788",
        tt_title="Bỏ Thăng Long chạy về núi, giờ đứng chờ vua xử tội",
        hooks_alt=["POV: Tưởng bị xử vì chạy / hóa ra chạy đúng kế", "POV: Quân thua chém tướng"],
        pin=("Tập này nối tiếp mốc \"Bỏ Thăng Long rút về Tam Điệp\" 🔥 Bạn có biết vua giao việc giảng hòa sau trận cho ai "
             "không? Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="\"Quân thua chém tướng\": vua Quang Trung ở Tam Điệp 1788 | Loạt Quang Trung",
        yt_tags="quân thua chém tướng, tam điệp, ngô thì nhậm, ngô văn sở, hoàng lê nhất thống chí, 1788, " + YT),
    # ================================================================== Tập 13 · Tiền Quang Trung thông bảo
    dict(COMMON, slug="duc-tien-quang-trung-thong-bao", prefix="qt13",
        voices={"foreman": "a gruff, practical middle-aged male voice", "old woman": "a sharp, croaky old woman's voice, Northern accent"},
        title="Tập 13 · Bị sai khắc tên vua lên đồng tiền nhỏ bằng móng tay (tiền Quang Trung thông bảo)",
        history=("**Lịch sử:** triều Tây Sơn thời Quang Trung (1788–1792) đúc tiền đồng **Quang Trung thông bảo** (光中通寶), có "
                 "loại mặt sau đúc hai chữ **An Nam** (安南), thường được cho là đúc sau khi nhà Thanh phong vua làm An Nam quốc "
                 "vương năm 1789 (hiện vật còn nhiều trong các bộ sưu tập, mức A; năm đúc từng loại chưa xác định được). Tiền "
                 "đúc bằng khuôn cát, đồng nóng chảy rót vào thành \"cây tiền\", rồi bẻ ra từng đồng. **Hư cấu:** Anh Tư, xưởng "
                 "đúc và mọi lời thoại."),
        setting=("Phú Xuân or Thăng Long, about 1789–1792: a hot casting workshop with sand moulds, a glowing furnace, crucibles "
                 "of molten bronze, a 'coin tree' of freshly cast coins, then a busy market. Round bronze coins with a square "
                 "hole; any characters on them are small and blurred, never readable on screen. Workers bare-chested in "
                 f"brown trousers. Anh Tư is {FACE}, a workshop helper. {SAFE}"),
        hook="POV: Khắc tên vua / lên đồng tiền / bằng móng tay",
        clips=[
            c("Tên vua", "0-5", "Xưởng đúc tiền · thời Quang Trung",
              f"First-person view in a hot casting workshop, a gruff foreman holding up a tiny carved coin pattern between two fingers in front of {FACE}",
              ("0-5s: The foreman holds up a tiny coin pattern: \"Đúc tiền mới. Đồng nào cũng có tên vua.\" Anh Tư: \"Nhỏ thế "
               "này khắc sao ạ?\" The foreman: \"Thì nheo mắt lại.\" 5-10s: Anh Tư squints at it: \"Tên vua to thế... mà phải "
               "nhét vào cái đồng bằng móng tay.\""),
              [(0.3, 2.2, "Đúc tiền mới. / Đồng nào cũng có tên vua."), (2.2, 3.4, "Nhỏ thế này / khắc sao ạ?"),
               (3.4, 4.9, "Thì nheo mắt lại."), (5.2, 9.5, "Tên vua to thế... / mà phải nhét vào / cái đồng bằng móng tay.")]),
            c("Rót đồng", "5-10", "",
              f"First-person view as workers pour glowing molten bronze from a crucible into sand moulds, sparks flying, {FACE} holding the mould frame steady, sweating",
              ("0-5s: Glowing molten bronze is poured into the sand moulds; sparks fly. 5-10s: Anh Tư, sweating, holds the frame: "
               "\"Đồng chảy đỏ như lửa... mà em phải đứng sát.\""),
              [(5.0, 9.5, "Đồng chảy đỏ như lửa... / mà em phải đứng sát.")]),
            c("Cây tiền", "5-10", "",
              f"First-person view as the sand mould is broken open revealing a 'coin tree': a branching bronze casting with dozens of coins attached, {FACE} holding it up, amazed",
              ("0-5s: The mould is broken open: a branching bronze \"tree\" with dozens of coins attached. 5-10s: Anh Tư holds "
               "it up: \"Người ta trồng cây ra quả... xưởng này đúc cây ra tiền.\""),
              [(5.0, 9.5, "Người ta trồng cây ra quả... / xưởng này / đúc cây ra tiền.")]),
            c("Hai chữ mặt sau", "5-10", "",
              f"Close first-person view of {FACE} filing the edge of a bronze coin, the foreman beside him tapping the back of another coin",
              ("0-5s: Anh Tư files a coin and turns it over: \"Mặt sau khắc gì đấy ạ?\" The foreman: \"An Nam. Cho đủ lễ với "
               "nước lớn.\" 5-10s: Anh Tư, filing slowly: \"Thắng trận rồi... vẫn phải giữ lễ.\""),
              [(0.5, 2.6, "Mặt sau khắc gì đấy ạ?"), (2.6, 4.8, "An Nam. / Cho đủ lễ với nước lớn."),
               (5.0, 9.5, "Thắng trận rồi... / vẫn phải giữ lễ.")]),
            c("Ra chợ", "5-10", "",
              f"First-person view at a busy market, a sharp old woman biting a new bronze coin to test it, then dropping it into her pouch, {FACE} watching",
              ("0-5s: At the market an old woman bites a new coin, squints at it, then nods and pockets it. 5-10s: Anh Tư says "
               "quietly to the viewer: \"Đồng tiền nhỏ bằng móng tay... mà mang cả tên một ông vua.\""),
              [(5.0, 9.5, "Đồng tiền nhỏ bằng móng tay... / mà mang cả tên / một ông vua.")]),
            c("Giữ một đồng", "5-10", "",
              f"First-person view at night, {FACE} threading a single bronze coin on a red string and tucking it inside his shirt",
              ("0-5s: At night Anh Tư threads one coin on a red string. 5-10s: He tucks it inside his shirt: \"Em đúc cả nghìn "
               "đồng... giữ lại một đồng, không tiêu.\""),
              [(5.0, 9.5, "Em đúc cả nghìn đồng... / giữ lại một đồng, / không tiêu.")]),
            c("Câu chốt", "3-10", "",
              f"Close view of an old worn bronze coin with a square hole lying on a dark cloth, soft light, characters too worn to read, then {FACE} in the old workshop looking at the camera",
              ("0-4.5s: An old worn coin on dark cloth. A calm narrator's voice says: \"Thời Quang Trung, triều Tây Sơn đúc tiền "
               "Quang Trung thông bảo. Hơn hai trăm năm sau, những đồng tiền ấy vẫn còn.\" 4.5-10s: Anh Tư in the old workshop "
               "says quietly to the camera: \"Người tiêu thì đi hết rồi... đồng tiền thì vẫn còn leng keng.\""),
              [(3.0, 6.0, "Tiền Quang Trung thông bảo. / Hơn hai trăm năm sau, / những đồng tiền ấy vẫn còn."),
               (6.1, 8.4, "Người tiêu thì đi hết rồi... / đồng tiền / vẫn còn leng keng.")]),
        ],
        caption=("Bị sai khắc tên vua lên đồng tiền nhỏ bằng móng tay 😳 Thời Quang Trung, triều Tây Sơn đúc tiền Quang Trung thông "
                 "bảo, có loại mặt sau đúc hai chữ An Nam. Nhà bạn còn giữ đồng tiền xưa nào không? 👇"),
        tags="#quangtrung #quangtrungthongbao #tiencoxua #taysontungmoc #lichsutiente",
        tt_title="Bị sai khắc tên vua lên đồng tiền nhỏ bằng móng tay",
        hooks_alt=["POV: Xưởng này / đúc cây ra tiền", "POV: Đồng tiền bằng móng tay / mang tên một ông vua"],
        pin=("Tiền Quang Trung thông bảo vẫn còn trong nhiều bộ sưu tập ngày nay 🪙 Bạn đã từng cầm đồng tiền xưa chưa? Follow "
             "để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="Đúc tiền Quang Trung thông bảo: tên vua trên đồng tiền bằng móng tay | Loạt Quang Trung",
        yt_tags="quang trung thông bảo, tiền tây sơn, tiền cổ việt nam, an nam, đúc tiền, " + YT),
    # ================================================================== Tập 14 · Phú Xuân 1786
    dict(COMMON, slug="danh-roi-la-thu-phu-xuan-1786", prefix="qt14",
        voices={"officer": "a short, stern male voice", "comrade": "a cheeky young adult male voice"},
        title="Tập 14 · Được giao mang thư đến gần thành giặc rồi… đánh rơi cho khéo (Nguyễn Huệ lấy thành Phú Xuân, 1786)",
        history=("**Lịch sử:** giữa năm 1786, Nguyễn Huệ đánh thành Phú Xuân do quân Trịnh trấn giữ (trấn thủ Phạm Ngô Cầu, phó "
                 "tướng Hoàng Đình Thể). Theo các tài liệu: Nguyễn Huệ nhờ Nguyễn Hữu Chỉnh viết **thư dụ hàng gửi Hoàng Đình "
                 "Thể, cố ý để thư lọt vào tay Phạm Ngô Cầu**, khiến hai người nghi kỵ nhau. **Đêm 20 tháng 5 âm lịch (khoảng "
                 "15/6/1786), nước dâng ngập chân thành**; thủy quân Tây Sơn tiến sát nã pháo vào thành, quân trong thành cạn "
                 "thuốc súng. Hoàng Đình Thể chiến đấu đến cùng và tử trận; Phạm Ngô Cầu ra hàng. Chỉ trong vài ngày, đất Thuận "
                 "Hóa đến sông Gianh về tay Tây Sơn (sử nhà Nguyễn và các tài liệu tổng hợp, mức B; chi tiết cách ra hàng các "
                 "nguồn ghi khác nhau). **Hư cấu:** Anh Tư là người \"đánh rơi\" thư, cảnh quan sát và mọi lời thoại. Không dựng "
                 "cảnh chết; quân trong thành là người Việt dưới quyền chúa Trịnh, giọng kể trung tính, không chế giễu."),
        setting=("Phú Xuân (Huế), June 1786, rainy season: a large old earthen-and-brick citadel by the Perfume River, Trịnh "
                 "soldiers in dark-blue tunics on the walls, Tây Sơn war boats on the river at night, rising flood water "
                 f"lapping at the foot of the walls. {ARMY}. {HUE_}. Anh Tư is {FACE}, a Tây Sơn soldier. {SAFE}"),
        hook="POV: Mang thư / đến gần thành giặc / rồi đánh rơi",
        clips=[
            c("Đánh rơi cho khéo", "0-5", "Phú Xuân · 1786",
              f"First-person view in a riverside camp at dusk, a stern officer handing {FACE} a sealed letter",
              ("0-5s: The officer hands Anh Tư a sealed letter: \"Mang đến gần thành. Đánh rơi cho khéo.\" Anh Tư: \"Đưa thư... "
               "mà đánh rơi ạ?\" The officer: \"Rơi đúng chỗ thì hơn trăm khẩu súng.\" 5-10s: Anh Tư tucks it in his shirt and "
               "says quietly: \"Lần đầu em được giao việc... làm rơi đồ.\""),
              [(0.3, 2.2, "Mang đến gần thành. / Đánh rơi cho khéo."), (2.2, 3.4, "Đưa thư... / mà đánh rơi ạ?"),
               (3.4, 4.9, "Rơi đúng chỗ / thì hơn trăm khẩu súng."), (5.2, 9.5, "Lần đầu em được giao việc... / làm rơi đồ.")]),
            c("Rơi ba lần", "5-10", "",
              f"First-person view from behind bushes near the citadel road, a letter lying on the path, a Trịnh patrol walking past it, {FACE} crouching and holding his breath",
              ("0-5s: Anh Tư drops the letter on the path and dives into the bushes; the Trịnh patrol walks right past it. "
               "He crawls out, moves it closer, hides again. 5-10s: Finally a soldier picks it up. Anh Tư sighs: \"Em làm rơi "
               "ba lần... nó mới chịu nhặt.\""),
              [(5.0, 9.5, "Em làm rơi ba lần... / nó mới chịu nhặt.")]),
            c("Trong thành cãi nhau", "5-10", "",
              f"First-person view from the riverbank looking at the citadel wall, two Trịnh officers on the wall arguing and pointing at each other, {FACE} watching from the reeds",
              ("0-5s: On the wall two officers argue loudly, one waving a letter. 5-10s: Anh Tư, in the reeds, whispers: \"Một "
               "lá thư... mà trong thành cãi to hơn ngoài thành.\""),
              [(5.0, 9.5, "Một lá thư... / mà trong thành / cãi to hơn ngoài thành.")]),
            c("Nước dâng", "5-10", "",
              f"First-person view at night from a Tây Sơn war boat, flood water rising up to the foot of the citadel walls, rain, {FACE} at the oars",
              ("0-5s: Night, heavy rain; the river rises until water laps at the foot of the walls; the boats glide right up "
               "to them. 5-10s: Anh Tư, rowing, whispers: \"Nước lên tận chân thành... ông trời mở đường hộ.\""),
              [(5.0, 9.5, "Nước lên tận chân thành... / ông trời mở đường hộ.")]),
            c("Súng im", "5-10", "",
              f"First-person view from a boat as Tây Sơn cannons fire flashes toward the citadel, the cannons on the wall silent, {FACE} covering his ears",
              ("0-5s: Tây Sơn boat cannons fire toward the citadel; the cannons on the wall answer once, then fall silent. "
               "5-10s: Anh Tư lowers his hands from his ears: \"Thành có súng... mà hết tiếng.\""),
              [(5.0, 9.5, "Thành có súng... / mà hết tiếng.")]),
            c("Nhặt cả tòa thành", "5-10", "",
              f"First-person view at grey dawn of the citadel gate slowly opening, a white cloth hanging over the wall, Tây Sơn soldiers wading toward it, {FACE} among them",
              ("0-5s: Grey dawn; a white cloth hangs over the wall and the gate slowly opens. No bodies, no blood. 5-10s: Anh Tư "
               "wades toward the gate and says quietly to the viewer: \"Đánh rơi một lá thư... nhặt được cả tòa thành.\""),
              [(5.0, 9.5, "Đánh rơi một lá thư... / nhặt được cả tòa thành.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view in the morning inside the citadel, Tây Sơn soldiers taking over the walls, {HUE_} far away on the wall looking north, {FACE} in the foreground",
              ("0-4.5s: Morning inside the citadel; far away on the wall, Nguyễn Huệ, seen only from behind, looks north. A calm "
               "narrator's voice says: \"Tháng 6 năm 1786, Nguyễn Huệ lấy thành Phú Xuân. Chỉ vài ngày sau, cả Thuận Hóa đến "
               "sông Gianh về tay Tây Sơn.\" 4.5-10s: Anh Tư says quietly to the camera: \"Cả đời em làm rơi đồ bị mắng... lần "
               "này được khen.\""),
              [(3.0, 6.0, "Năm 1786, Nguyễn Huệ / lấy thành Phú Xuân, / rồi cả Thuận Hóa."),
               (6.1, 8.4, "Cả đời em làm rơi đồ / bị mắng... / lần này được khen.")]),
        ],
        caption=("Được giao mang thư đến gần thành giặc rồi đánh rơi cho khéo 😳 Năm 1786, Nguyễn Huệ dùng một lá thư làm hai "
                 "tướng trong thành Phú Xuân nghi nhau, rồi chờ đêm nước dâng mới đánh. Bạn nghĩ mẹo nào lợi hại hơn? 👇"),
        tags="#quangtrung #nguyenhue #phuxuan #taysontungmoc #1786",
        tt_title="Được giao mang thư đến gần thành giặc rồi đánh rơi cho khéo",
        hooks_alt=["POV: Đánh rơi một lá thư / nhặt được cả tòa thành", "POV: Đưa thư / mà phải đánh rơi"],
        pin=("Lấy Phú Xuân xong, Nguyễn Huệ ra Bắc \"phù Lê diệt Trịnh\" 🔥 Xem tập \"Quỳ lạy vua Lê\" nhé! Follow để xem loạt "
             "Quang Trung tập tiếp theo!"),
        yt_title="Năm 1786: Nguyễn Huệ lấy thành Phú Xuân bằng một lá thư | Loạt Quang Trung",
        yt_tags="thành phú xuân, 1786, nguyễn hữu chỉnh, phạm ngô cầu, hoàng đình thể, ly gián, " + YT),
    # ================================================================== Tập 15 · Vũ Văn Nhậm 1788
    dict(COMMON, slug="khac-an-vu-van-nham-1788", prefix="qt15",
        voices={"steward": "a smug, oily middle-aged male voice", "comrade": "a nervous young adult male voice"},
        title="Tập 15 · Được thuê khắc một cái ấn thật to mà không ai nói ấn của ai (Nguyễn Huệ ra Bắc bắt Vũ Văn Nhậm, 1788)",
        history=("**Lịch sử:** năm 1787–1788, tướng Tây Sơn Vũ Văn Nhậm (con rể Nguyễn Nhạc) được sai ra Bắc diệt Nguyễn Hữu "
                 "Chỉnh, rồi ở lại Thăng Long **chuyên quyền**: lập Lê Duy Cận làm giám quốc, sửa thành, **làm ấn riêng**, có ý "
                 "tự lập. Ngô Văn Sở, Phan Văn Lân mật báo về Phú Xuân. Khoảng tháng 4 năm 1788, Nguyễn Huệ **bí mật đem quân ra "
                 "Bắc**, bất ngờ vào Thăng Long ban đêm, bắt Nhậm rồi xử tử; sau đó giao Bắc Hà cho Ngô Văn Sở, dùng Ngô Thì "
                 "Nhậm và các sĩ phu Bắc Hà (*Khâm định Việt sử*, sử nhà Nguyễn, mức B; năm tháng các nguồn ghi hơi khác nhau). "
                 "**Hư cấu:** Anh Tư khắc ấn, người quản gia và mọi lời thoại. Việc xử tử chỉ nhắc bằng lời người dẫn chuyện, "
                 "không dựng cảnh trói hay hành hình."),
        setting=("Thăng Long, spring 1788: a seal-carver's small workshop with stone and wood blocks, chisels and red ink; the "
                 "streets and a mansion courtyard at night lit by lanterns. Vũ Văn Nhậm is a proud Tây Sơn general in a fine "
                 f"dark robe, seen ONLY from behind or far away. {ARMY}. {HUE_}. Anh Tư is {FACE}, a seal carver. Seals and "
                 f"papers have no readable writing. {SAFE}"),
        hook="POV: Khắc một cái ấn / thật to / mà không biết của ai",
        clips=[
            c("Ấn của ai", "0-5", "Thăng Long · 1788",
              f"First-person view in a small seal-carving workshop, a smug steward in a fine robe dropping a big block of stone on the bench in front of {FACE}",
              ("0-5s: A smug steward drops a big stone block on the bench: \"Khắc một cái ấn. To hơn ấn của tướng.\" Anh Tư: \"Ấn "
               "của ai ạ?\" The steward: \"Của người trả tiền.\" 5-10s: Anh Tư weighs the block and says quietly: \"Khắc ấn cho "
               "người ta... mà không biết người ta là ai.\""),
              [(0.3, 2.2, "Khắc một cái ấn. / To hơn ấn của tướng."), (2.2, 3.4, "Ấn của ai ạ?"),
               (3.4, 4.9, "Của người trả tiền."), (5.2, 9.5, "Khắc ấn cho người ta... / mà không biết / người ta là ai.")]),
            c("Như chủ", "5-10", "",
              f"First-person view in a Thăng Long street, a proud general in a fine dark robe on horseback seen only from behind, guards clearing the way, townspeople bowing, {FACE} carrying a bundle",
              ("0-5s: A proud general rides through the street, seen only from behind; guards clear the way, people bow. "
               "5-10s: Anh Tư, stepping aside, murmurs: \"Ông ấy ở Thăng Long... đi đứng như chủ nhà.\""),
              [(5.0, 9.5, "Ông ấy ở Thăng Long... / đi đứng như chủ nhà.")]),
            c("Đèn không ngủ", "5-10", "",
              f"First-person view late at night down a dark street, a single lit window where an officer writes a letter, a rider waiting outside with a horse, {FACE} passing with a lantern",
              ("0-5s: Late at night, one window is still lit; an officer seals a letter and hands it to a waiting rider, who "
               "gallops off south. 5-10s: Anh Tư lowers his lantern: \"Cả kinh thành ngủ... chỉ có một ngọn đèn không ngủ.\""),
              [(5.0, 9.5, "Cả kinh thành ngủ... / chỉ có một ngọn đèn / không ngủ.")]),
            c("Ấn to quá", "5-10", "",
              f"Close first-person view of {FACE} blowing stone dust off a finished, very large carved seal, then comparing it nervously with a smaller seal on the shelf",
              ("0-5s: Anh Tư finishes the big seal and blows off the dust, then sets it beside an ordinary general's seal: it is "
               "twice as big. 5-10s: He swallows: \"Khắc ấn to quá... là khắc luôn cả cái họa.\""),
              [(5.0, 9.5, "Khắc ấn to quá... / là khắc luôn cả cái họa.")]),
            c("Không trống không loa", "5-10", "",
              f"First-person view at night in a lantern-lit courtyard as {HUE_} strides in with a small group of guards, the household frozen, {FACE} peeking from behind a pillar",
              ("0-5s: Night; no drums, no announcement; Nguyễn Huệ, seen only from behind, strides into the courtyard with a few "
               "guards. Everyone freezes. 5-10s: Anh Tư, behind a pillar, whispers: \"Không trống, không loa... ông ấy đã đứng "
               "giữa sân.\""),
              [(5.0, 9.5, "Không trống, không loa... / ông ấy đã đứng giữa sân.")]),
            c("Giấu ấn", "5-10", "",
              f"First-person view at night by a courtyard well, {FACE} quietly lowering the big carved seal into the dark well on a rope, guards in the background escorting a man in a fine robe away, seen only from behind",
              ("0-5s: In the background guards escort the proud general away, seen only from behind; no struggle shown. Anh Tư "
               "quietly lowers the big seal into the well. 5-10s: He whispers: \"Ấn em khắc cả tháng... giờ chỉ mong không ai "
               "biết em khắc.\""),
              [(5.0, 9.5, "Ấn em khắc cả tháng... / giờ chỉ mong / không ai biết em khắc.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view the next morning in the seal workshop, {FACE} hanging a small wooden sign (no readable writing) by the door and looking at the camera",
              ("0-4.5s: Next morning in the workshop. A calm narrator's voice says: \"Năm 1788, Vũ Văn Nhậm chuyên quyền ở Thăng "
               "Long. Nguyễn Huệ bí mật ra Bắc, bắt Nhậm và xử tử, rồi giao Bắc Hà cho Ngô Văn Sở.\" 4.5-10s: Anh Tư hangs a "
               "small sign by the door and says quietly to the camera: \"Từ nay ai thuê khắc ấn... em hỏi tên trước.\""),
              [(3.0, 6.0, "Năm 1788, Vũ Văn Nhậm / chuyên quyền. Nguyễn Huệ / ra Bắc bắt Nhậm, xử tử."),
               (6.1, 8.4, "Từ nay ai thuê khắc ấn... / em hỏi tên trước.")]),
        ],
        caption=("Được thuê khắc một cái ấn thật to mà không ai nói ấn của ai 😳 Năm 1788, Vũ Văn Nhậm chuyên quyền ở Thăng Long, "
                 "làm ấn riêng. Nguyễn Huệ bí mật ra Bắc, vào thành ban đêm, không trống không loa. Bạn có biết ai mật báo cho "
                 "Nguyễn Huệ không? 👇"),
        tags="#quangtrung #nguyenhue #vuvannham #taysontungmoc #1788",
        tt_title="Được thuê khắc một cái ấn thật to mà không ai nói ấn của ai",
        hooks_alt=["POV: Khắc ấn to quá / là khắc luôn cái họa", "POV: Không trống không loa / ông ấy đã đứng giữa sân"],
        pin=("Người mật báo về Phú Xuân sau này chính là tướng giữ Bắc Hà khi quân Thanh sang 🔥 Đoán xem là ai? Follow để xem "
             "loạt Quang Trung tập tiếp theo!"),
        yt_title="Năm 1788: Nguyễn Huệ bí mật ra Bắc bắt Vũ Văn Nhậm | Loạt Quang Trung",
        yt_tags="vũ văn nhậm, 1788, ngô văn sở, ra bắc lần hai, thăng long, " + YT),
]

ACTING = ("Acting: natural and understated, like real people filmed in a documentary; small reactions (a sigh, a glance, a pause, a shake of the head) instead of big expressions. Anh Tư smiles at most once in the whole clip and never laughs at the camera; no exaggerated mugging or cartoonish faces.")
for _ep in EPISODES:
    _ep["setting"] = _ep["setting"] + " " + ACTING
    for _c in _ep["clips"]:
        if _c.get("setting"):
            _c["setting"] = _c["setting"] + " " + ACTING


if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#loatquangtrung #anhtu", note=NOTE, unit="Tập", file_unit="tap")
