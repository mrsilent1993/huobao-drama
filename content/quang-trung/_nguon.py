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

HUE = "Central Vietnamese (Huế) accent"
NGHE = "Central Vietnamese (Nghệ An) accent"
ARMY = "Tây Sơn soldiers with black-lacquered teeth in dark-red uniforms with red head wraps, spears and swords"
HUE_ = ("Nguyễn Huệ (later Emperor Quang Trung), seen ONLY from behind or far away: a broad-shouldered man in a dark "
        "battle robe")
SAFE = "Adults only, no children. No flags, no legible writing anywhere, no modern objects, no blood, no dead bodies."
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
               "Tướng ngồi ạ?\" The officer: \"Trải đi rồi biết.\" 5-10s: Anh Tư strokes the fine mat and grins: \"Chiếu đẹp "
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
              f"First-person view at the palace gate, townspeople who were anxious before now smiling and cheering, an old man bowing toward the palace, {FACE} grinning",
              ("0-5s: News spreads to the gate; the townspeople cheer: \"Phù Lê! Phù Lê!\" 5-10s: Anh Tư grins at the viewer: "
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
    dict(COMMON, slug="danh-cho-de-dai-toc-1788", prefix="qt2", giong=NGHE,
        voices={"village official": "a fussy, nasal male voice", "officer": "a stern, clipped male voice",
                "Quang Trung": "a powerful, thunderous, fiery male voice"},
        title="Q2 · Đang cày ruộng bị gọi ra bãi duyệt binh, nghe một câu mà nhớ cả đời (Nghệ An, cuối năm 1788)",
        history=("**Lịch sử:** cuối năm 1788, trên đường ra Bắc đánh quân Thanh, vua Quang Trung dừng ở Nghệ An hơn mười ngày "
                 "để **tuyển thêm quân**, cứ ba suất đinh lấy một người, rồi duyệt binh (*Hoàng Lê nhất thống chí*, mức B). Vua "
                 "dụ tướng sĩ: **\"Đánh cho để dài tóc, đánh cho để đen răng...\"** (có trong *Đại Nam chính biên liệt truyện* "
                 "và *Hoàng Lê nhất thống chí*; các nguồn ghi nơi đọc khác nhau: Nghệ An hoặc lễ thệ sư ở Thọ Hạc, Thanh Hóa, "
                 "mức B/C). \"Dài tóc, đen răng\" là phong tục của người Việt thời ấy. **Hư cấu:** Anh Tư, ông lý trưởng và "
                 "mọi lời thoại, trừ câu dụ. Chỉ đọc lời, không dựng cảnh đánh nhau."),
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
            c("Lời dụ", "5-10", "",
              f"First-person view from the ranks looking up at {HUE_} on the platform raising one arm, the army's spears rising like a forest, {FACE} with tears in his eyes",
              ("0-5s: The emperor, seen only from behind, raises his arm. 5-10s: His thunderous voice: \"Đánh cho để dài tóc! "
               "Đánh cho để đen răng!\" The whole army roars and raises their spears."),
              [(5.0, 9.5, "Đánh cho để dài tóc! / Đánh cho để đen răng!")]),
            c("Tóc dài răng đen", "5-10", "",
              f"Close first-person view as {FACE} touches his own long topknot and grins with his black-lacquered teeth, determined, the roaring army around him",
              ("0-5s: As the army roars, Anh Tư touches his long topknot, then grins showing his black teeth. 5-10s: He says to "
               "the viewer: \"Tóc em dài, răng em đen... thì em phải đánh.\""),
              [(5.0, 9.5, "Tóc em dài, răng em đen... / thì em phải đánh.")]),
            c("Câu chốt", "3-10", "",
              f"First-person view at dawn as the army marches north out of Nghệ An, {FACE} in a dark-red uniform now, spear upright, looking back once toward his village",
              ("0-4.5s: Dawn; the army marches north. A calm narrator's voice says: \"Cuối năm 1788, trên đường ra Bắc, vua "
               "Quang Trung tuyển thêm quân ở Nghệ An và dụ tướng sĩ.\" 4.5-10s: Anh Tư looks back toward his village and says "
               "to the camera: \"Ra đi là thằng cày ruộng... về làng là lính Quang Trung.\""),
              [(3.0, 6.0, "Năm 1788, trên đường ra Bắc, / vua Quang Trung tuyển quân / ở Nghệ An."),
               (6.1, 8.4, "Ra đi là thằng cày ruộng... / về làng là lính Quang Trung.")]),
        ],
        caption=("Đang cày ruộng bị gọi đi lính, ra bãi duyệt binh nghe một câu mà nhớ cả đời 🔥 \"Đánh cho để dài tóc, đánh cho "
                 "để đen răng...\" Cuối năm 1788, vua Quang Trung tuyển quân ở Nghệ An trước khi ra Bắc đánh quân Thanh. Bạn "
                 "thuộc tiếp được câu này không? 👇"),
        tags="#quangtrung #danhchodedaitoc #nghean #taysontungmoc #1788",
        tt_title="Đang cày ruộng bị gọi đi lính, nghe một câu mà nhớ cả đời",
        hooks_alt=["POV: Đánh cho để dài tóc / đánh cho để đen răng", "POV: Hôm qua cầm cày / hôm nay cầm giáo"],
        pin=("Câu đầy đủ còn dài hơn thế 🔥 Ai thuộc thì viết tiếp ở dưới nhé! Follow để xem loạt Quang Trung tập tiếp theo!"),
        yt_title="\"Đánh cho để dài tóc, đánh cho để đen răng\": tuyển quân Nghệ An 1788 | Loạt Quang Trung",
        yt_tags="đánh cho để dài tóc, đánh cho để đen răng, nghệ an, tuyển quân, 1788, " + YT),
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
              ("0-5s: Heavy rain; Anh Tư takes off his outer shirt and wraps the branch inside it. 5-10s: Soaked, he grins at "
               "the viewer: \"Em ướt hết... đào thì khô.\""),
              [(5.0, 9.5, "Em ướt hết... / đào thì khô.")]),
            c("Đếm bông", "5-10", "",
              f"Close first-person view at dawn by the roadside, {FACE} carefully counting the pink blossoms on the branch with one fingertip, exhausted but smiling",
              ("0-5s: At dawn Anh Tư counts the blossoms with one fingertip, lips moving. 5-10s: He sighs with relief: \"Đi "
               "bao nhiêu bông... về đủ bấy nhiêu bông.\""),
              [(5.0, 9.5, "Đi bao nhiêu bông... / về đủ bấy nhiêu bông.")]),
            c("Câu chốt", "3-10", "Phú Xuân",
              f"First-person view at the gate of the Phú Xuân palace, an adult palace attendant receiving the fresh peach branch with both hands, {FACE} mud-splattered and smiling",
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
              f"First-person view in the empty courtyard at dusk, {FACE} scraping the bottom of the giant pot and eating the burnt rice crust himself, smiling",
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
              f"First-person view at a palace gate, a line of scholars in dark robes with cloth bundles waiting to enter, {FACE} standing guard and grinning",
              ("0-5s: At the palace gate a line of scholars waits with their bundles. 5-10s: Anh Tư grins at the viewer: \"Hôm "
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
              ("0-5s: Anh Tư leans his spear against a tree and takes the plough handle. 5-10s: He grins at the viewer: \"Đánh "
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
              f"First-person view of an old woman in the front row slapping her knee in surprise, villagers nodding, {FACE} holding the edict and grinning",
              ("0-5s: An old woman slaps her knee: \"Ơ! Vua nói thế à?\" 5-10s: Anh Tư grins at the viewer: \"Lần đầu vua viết... "
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
              f"First-person view as {FACE} turns to the viewer on the mountain road, the procession behind him, a stunned, disbelieving grin on his face",
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
              f"First-person view at dusk on the road home in autumn, falling leaves, {FACE} walking slowly with the pole, looking down, then up at the camera with a sad, proud smile",
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
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#loatquangtrung #anhtu", note=NOTE, unit="Tập", file_unit="tap")
