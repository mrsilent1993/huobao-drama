#!/usr/bin/env python3
"""Tập 3 (Sát Thát 1285): 2 mẫu kịch bản thay thế để anh chọn. Chạy: python3 _nguon.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from series import build  # noqa: E402
from _nguon import FACE, TRAN, END, LEN6, NOTE  # noqa: E402

HIST = ("**Lịch sử:** khi quân Nguyên chuẩn bị sang đánh Đại Việt lần thứ hai (cuối 1284, đầu 1285), quân sĩ nhà Trần "
        "đều thích (xăm) vào cánh tay hai chữ **\"Sát Thát\" (殺韃)**, nghĩa là \"đánh giặc Thát\" (quân Mông Cổ, Nguyên sang "
        "xâm lược), để tỏ quyết tâm (*Đại Việt sử ký toàn thư*, mức B; Sử gia cần đối chiếu nguyên văn). Năm 1288, quân "
        "Nguyên thua lớn ở sông Bạch Đằng và rút hẳn. Thời Trần chưa có chữ quốc ngữ, nên trên tay là chữ Hán 殺韃, phụ "
        "đề ghi \"Sát Thát\". **Hư cấu:** Anh Tư, người thợ xăm, anh lính đòi xăm tên người yêu và mọi lời thoại. Không "
        "dựng cảnh đánh nhau, không máu.")
SET = ("Đại Việt, late 1284: a huge Trần army camp at night by a wide river, hundreds of torches and campfires, bamboo "
       "huts. " + TRAN + ". Tattooers use bundles of fine bamboo needles and bowls of black ink; soldiers sit calmly with "
       "one sleeve rolled up, no blood, only clean black ink. The ONLY legible writing anywhere is the two Chinese "
       "characters 殺韃 tattooed in black ink on soldiers' forearms, written clearly and correctly. Generals and princes "
       "are seen ONLY from behind. Adults only, no children. "
       f"Anh Tư is {FACE}, a camp helper. No flags, no other writing, no modern objects, no dead bodies.")
VIS = ("**Chuẩn hình ảnh:** quân Trần búi tóc, răng đen, áo nâu, chân đất. Chữ **殺韃** xăm rõ trên cánh tay, mực đen, "
       "không máu; ngoài hai chữ này không có chữ nào khác. Nếu Muse vẽ sai nét chữ Hán, chọn khung hình đúng nhất.")
COMMON = dict(length=LEN6, history=HIST, setting=SET, visual=VIS, end=END, end_secs=1.6,
              tags="#tuhaodaiviet #satthat #nhatran #khangchienchongnguyen #1285")

EPISODES = [
    # ------------------------------------------------------------------ Mẫu A: Mực không trôi
    dict(COMMON,
        slug="sat-that-muc-khong-troi", prefix="th1285a",
        voices={"tattooer": "a gruff, calm middle-aged male voice, few words",
                "young soldier": "a cheeky, cheerful young adult male voice",
                "old soldier": "a deep, slow, weathered male voice"},
        title="Mẫu A · Mực không trôi: pha mực cả đêm, sáng ra cả đạo quân có chung hai chữ (Sát Thát, 1285)",
        hook="POV: Pha mực / phải không trôi / được cả đời",
        clips=[
            dict(name="Mực loãng", tiktok="5-10", label="Trại quân nhà Trần · cuối 1284",
                 img=f"First-person view at night in a Trần army camp, a gruff tattooer dipping a finger into a bowl of watery grey ink and frowning, {FACE} holding a pestle beside a stone mortar, guilty look, realistic, vertical 9:16.",
                 vid=("0-5s: The tattooer dips a finger in Anh Tư's watery grey ink, wipes it off easily and frowns: \"Mực "
                      "này rửa là trôi. Pha lại.\" 5-10s: Anh Tư: \"Mực để viết thư thôi mà, cần gì đặc thế ạ?\" The "
                      "tattooer: \"Không phải viết thư. Mực này... phải không trôi được cả đời.\""),
                 subs=[(0.5, 4.8, "Mực này rửa là trôi. / Pha lại."),
                       (5.0, 7.4, "Viết thư thôi mà, / cần gì đặc thế ạ?"),
                       (7.4, 9.6, "Mực này phải không trôi / được cả đời.")]),
            dict(name="Thử mực", tiktok="5-10", label="",
                 img=f"First-person view at the river bank at night, {FACE} scrubbing a black ink mark on the back of his own hand with sand and water, it does not come off, an old soldier watching and nodding, realistic, vertical 9:16.",
                 vid=("0-5s: At the river Anh Tư scrubs a black ink mark on his own hand with sand; it does not come off. "
                      "He panics. 5-10s: An old soldier nods approvingly: \"Đúng. Phải thế.\" Anh Tư whispers: \"Em thử mực... "
                      "giờ tay em cũng đen luôn rồi.\""),
                 subs=[(0.5, 4.8, "Sao không trôi... / sao không trôi!"),
                       (5.0, 6.8, "Đúng. Phải thế."),
                       (6.8, 9.6, "Em thử mực... / giờ tay em đen luôn rồi.")]),
            dict(name="Cả trại xếp hàng", tiktok="5-10", label="",
                 img=f"First-person wide view of an endless line of Trần soldiers with torches stretching into the dark along the river, each rolling up one sleeve, {FACE} carrying a heavy bowl of black ink, awed, realistic, vertical 9:16.",
                 vid=("0-5s: An endless line of soldiers with torches stretches into the dark along the river, each rolling up "
                      "one sleeve. 5-10s: Anh Tư, carrying the heavy ink bowl, whispers: \"Một bát mực... cho cả một đạo "
                      "quân?\""),
                 subs=[(5.0, 9.5, "Một bát mực... / cho cả một đạo quân?")]),
            dict(name="Tên người yêu", label="",
                 img=f"First-person view as a cheeky young soldier holds out his forearm already tattooed with 殺韃 and looks hopefully at the tattooer, a few soldiers smirking, {FACE} in the foreground, trying not to smile, realistic, vertical 9:16.",
                 vid=("0-5s: A cheeky young soldier with 殺韃 fresh on his forearm asks: \"Thầy ơi, còn chỗ trống, thêm tên "
                      "người yêu em được không?\" The tattooer: \"Hai chữ thôi.\" A few soldiers snort. 5-10s: Anh Tư to the viewer: "
                      "\"Cả đạo quân xăm cùng một chữ... không ai xăm tên người yêu.\""),
                 subs=[(0.5, 3.2, "Còn chỗ trống, / thêm tên người yêu em?"),
                       (3.2, 4.8, "Hai chữ thôi."),
                       (5.0, 9.5, "Cả đạo quân / xăm cùng một chữ... / không ai xăm tên người yêu.")]),
            dict(name="Cả tướng cũng xăm", tiktok="5-10", label="",
                 img=f"First-person view of a Trần general in dark armor and a red cloak seen ONLY from behind, sitting down in the line and rolling up his sleeve like the soldiers, {FACE} staring with his mouth open, realistic, vertical 9:16.",
                 vid=("0-5s: A general in dark armor and a red cloak, seen only from behind, quietly sits down in the line and "
                      "rolls up his sleeve like everyone else. 5-10s: Anh Tư whispers, stunned: \"Tướng... cũng xếp hàng? Thế "
                      "thì em trốn đằng nào?\" He rolls up his own sleeve."),
                 subs=[(5.0, 9.5, "Tướng cũng xếp hàng... / thế thì em trốn đằng nào?")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunrise, years later, by a wide river with wooden stakes in the water, an older {FACE} with grey in his hair raising his forearm with faded 殺韃 tattoo toward the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Sunrise over a wide river. A calm narrator's voice says: \"Năm 1285, quân sĩ nhà Trần thích vào "
                      "cánh tay hai chữ Sát Thát. Ba năm sau, quân Nguyên thua ở Bạch Đằng, rút hẳn về nước.\" 5-10s: Anh Tư, "
                      "older with grey hair, raises his tattooed forearm: \"Mực em pha đấy... chữ vẫn còn. Giặc thì "
                      "không.\""),
                 subs=[(0.3, 4.8, "Năm 1285, quân nhà Trần / xăm hai chữ Sát Thát. / Năm 1288, / quân Nguyên rút hẳn."),
                       (5.0, 8.4, "Mực em pha đấy... / chữ vẫn còn. / Giặc thì không.")]),
        ],
        caption=("Bị bắt pha mực \"không trôi được cả đời\" mà không ai nói để làm gì 😳 Sáng ra cả đạo quân, cả tướng, đều có "
                 "chung hai chữ trên tay: Sát Thát. Năm 1285, quân sĩ nhà Trần xăm chữ lên tay để tỏ quyết tâm đánh giặc Nguyên. "
                 "Nếu là bạn, bạn có đưa tay ra không? 👇"),
        tt_title="Pha mực không trôi được cả đời, sáng ra cả đạo quân có chung hai chữ",
        hooks_alt=["POV: Cả đạo quân xăm một chữ / không ai xăm tên người yêu", "POV: Chữ vẫn còn / giặc thì không"],
        pin=("Hai chữ \"Sát Thát\" là lời thề đánh giặc Nguyên của quân nhà Trần 🔥 Ba năm sau là trận Bạch Đằng 1288. Follow "
             "để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1285: mực \"Sát Thát\" trên tay cả đạo quân nhà Trần | Tự hào Đại Việt",
        yt_tags=("sát thát, quân nhà trần, kháng chiến chống nguyên, 1285, bạch đằng 1288, xăm chữ sát thát, tự hào đại "
                 "việt, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ Mẫu B: Người cầm đèn
    dict(COMMON,
        slug="sat-that-nguoi-cam-den", prefix="th1285b",
        voices={"tattooer": "a gruff, calm middle-aged male voice, few words",
                "young soldier": "a cheeky, cheerful young adult male voice",
                "officer": "a short, stern male voice"},
        title="Mẫu B · Người cầm đèn: sợ kim nhất trại, lại bị sai cầm đèn cho thợ xăm cả đêm (Sát Thát, 1285)",
        hook="POV: Sợ kim nhất trại / bị sai cầm đèn / cho thợ xăm",
        clips=[
            dict(name="Cầm đèn", tiktok="5-10", label="Trại quân nhà Trần · cuối 1284",
                 img=f"First-person view at night in a Trần army camp, a stern officer handing an oil lamp to {FACE}, behind them a tattooer laying out bundles of bamboo needles, Anh Tư staring at the needles in horror, realistic, vertical 9:16.",
                 vid=("0-5s: The officer hands Anh Tư an oil lamp: \"Cầm đèn cho thợ. Cả đêm.\" Anh Tư sees the bundles of "
                      "needles and freezes. 5-10s: Anh Tư whispers: \"Em... sợ kim nhất trại đấy ạ.\" The officer: \"Thì cầm "
                      "đèn, có phải cầm kim đâu.\""),
                 subs=[(0.5, 4.8, "Cầm đèn cho thợ. / Cả đêm."),
                       (5.0, 7.6, "Em... sợ kim / nhất trại đấy ạ."),
                       (7.6, 9.6, "Thì cầm đèn, / có phải cầm kim đâu.")]),
            dict(name="Người xăm không kêu", tiktok="5-10", label="",
                 img=f"First-person close view by lamplight, a calm soldier with his forearm stretched out while the tattooer works with a bamboo needle bundle, no blood, {FACE} holding the lamp with his eyes squeezed shut, realistic, vertical 9:16.",
                 vid=("0-5s: By lamplight the tattooer works on a soldier's forearm; the soldier chats calmly. Anh Tư, holding "
                      "the lamp, squeezes his eyes shut and goes \"Ối... ối...\" 5-10s: The soldier looks up at him: \"Tao xăm "
                      "chứ mày có xăm đâu?\""),
                 subs=[(0.5, 4.8, "Ối... ối..."),
                       (5.0, 9.5, "Tao xăm / chứ mày có xăm đâu?")]),
            dict(name="Hai chữ", tiktok="5-10", label="",
                 img=f"Close view of a soldier's forearm with the two Chinese characters 殺韃 freshly tattooed in clean black ink, lit by the oil lamp in {FACE}'s shaking hand, no blood, realistic, vertical 9:16.",
                 vid=("0-5s: The lamp shakes over a forearm with 殺韃 freshly done in clean black ink. Anh Tư peeks: \"Hai "
                      "chữ gì mà xăm cả trại thế ạ?\" 5-10s: The tattooer, without looking up: \"Sát Thát. Đánh giặc Thát. "
                      "Cầm đèn cho vững.\""),
                 subs=[(0.5, 4.8, "Hai chữ gì / mà xăm cả trại thế ạ?"),
                       (5.0, 9.5, "Sát Thát. Đánh giặc Thát. / Cầm đèn cho vững.")]),
            dict(name="Tên người yêu", label="",
                 img=f"First-person view by lamplight as a cheeky young soldier holds out his arm to the tattooer, hopeful, the tattooer shaking his head, a few soldiers smirking, {FACE} biting his lip, the lamp swaying, realistic, vertical 9:16.",
                 vid=("0-5s: A cheeky young soldier holds out his arm: \"Thầy xăm thêm tên người yêu em vào được không?\" The "
                      "tattooer: \"Hai chữ thôi.\" A few soldiers snort; the lamp swings. 5-10s: Anh Tư to the viewer: \"Cả đạo quân "
                      "xăm cùng một chữ... không ai xăm tên người yêu.\""),
                 subs=[(0.5, 3.2, "Xăm thêm tên người yêu em / được không thầy?"),
                       (3.2, 4.8, "Hai chữ thôi."),
                       (5.0, 9.5, "Cả đạo quân / xăm cùng một chữ... / không ai xăm tên người yêu.")]),
            dict(name="Đến lượt", tiktok="5-10", label="",
                 img=f"First-person view near dawn, the lamp burned low, the tattooer patting the empty mat and looking at {FACE}, Anh Tư swallowing hard, a soldier taking the lamp from his hand, realistic, vertical 9:16.",
                 vid=("0-5s: Near dawn the lamp burns low. The tattooer pats the empty mat: \"Hết người rồi. Còn mày.\" A soldier "
                      "takes the lamp from Anh Tư's hand. 5-10s: Anh Tư swallows hard, sits down and holds out his arm: \"Thôi... "
                      "đến lượt người khác cầm đèn cho em.\""),
                 subs=[(0.5, 4.8, "Hết người rồi. / Còn mày."),
                       (5.0, 9.5, "Thôi... đến lượt người khác / cầm đèn cho em.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunrise, {FACE} with eyes open and calm while the tattooer finishes 殺韃 on his forearm, soldiers marching behind, Anh Tư surprised at himself, realistic, vertical 9:16.",
                 vid=("0-5s: Sunrise. The tattooer finishes 殺韃 on Anh Tư's forearm; Anh Tư has not flinched once. A calm "
                      "narrator's voice says: \"Năm 1285, trước khi quân Nguyên sang lần thứ hai, quân sĩ nhà Trần đều thích vào "
                      "cánh tay hai chữ: Sát Thát.\" 5-10s: Anh Tư looks at his arm, then at the camera: \"Lạ thật... nghĩ đến "
                      "giặc thì không thấy đau.\""),
                 subs=[(0.3, 4.8, "Năm 1285, quân sĩ nhà Trần / thích vào cánh tay / hai chữ: Sát Thát."),
                       (5.0, 8.4, "Lạ thật... / nghĩ đến giặc / thì không thấy đau.")]),
        ],
        caption=("Sợ kim nhất trại mà bị sai cầm đèn cho thợ xăm suốt đêm 😳 Lính xăm không kêu, người cầm đèn thì kêu. Năm "
                 "1285, quân sĩ nhà Trần xăm hai chữ \"Sát Thát\" lên tay để tỏ quyết tâm đánh giặc Nguyên. Bạn có dám ngồi "
                 "xuống chiếu không? 👇"),
        tt_title="Sợ kim nhất trại mà bị sai cầm đèn cho thợ xăm cả đêm",
        hooks_alt=["POV: Cả đạo quân xăm một chữ / không ai xăm tên người yêu", "POV: Nghĩ đến giặc / thì không thấy đau"],
        pin=("Hai chữ \"Sát Thát\" là lời thề đánh giặc Nguyên của quân nhà Trần 🔥 Bạn sợ kim không? Follow để xem Tự hào "
             "Đại Việt tập tiếp theo!"),
        yt_title="Sợ kim nhất trại, cầm đèn cho cả đạo quân xăm \"Sát Thát\" | Tự hào Đại Việt",
        yt_tags=("sát thát, quân nhà trần, kháng chiến chống nguyên, 1285, xăm chữ sát thát, tự hào đại việt, lịch sử việt "
                 "nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

ACTING = ("Acting: natural and understated, like real people filmed in a documentary; small reactions (a sigh, a glance, a pause, a shake of the head) instead of big expressions. Anh Tư smiles at most once in the whole clip and never laughs at the camera; no exaggerated mugging or cartoonish faces.")
for _ep in EPISODES:
    _ep["setting"] = _ep["setting"] + " " + ACTING
    for _c in _ep["clips"]:
        if _c.get("setting"):
            _c["setting"] = _c["setting"] + " " + ACTING


if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#tuhaodaiviet #anhtu", note=NOTE, unit="Mẫu", file_unit="mau")
