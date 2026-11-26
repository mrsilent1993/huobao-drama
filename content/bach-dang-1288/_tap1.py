#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 1 "Vua cáo ốm": bản đầy đủ dưới 2 phút, mỗi clip một người nói, khóa bối cảnh theo cảnh.
Chạy: python3 _tap1.py → bd1288-tap1-vua-cao-om.md + bd1288-tap1.plan.txt
"""
import os

from _tap3 import FACE, V_TU, RULES, AUDIO, spoken

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("Cinematic live-action, photorealistic, natural light, film grain, vertical 9:16. Đại Việt, Trần dynasty, late "
        "13th century, Thăng Long palace: dark wooden halls with red-lacquered pillars, brick courtyards, clay roof tiles; "
        "Trần people in brown or dark cotton tunics, hair in topknots, black-lacquered teeth; the Yuan envoy in a dark "
        "brocade robe and a round fur-trimmed hat. No modern objects, no on-screen text, no subtitles, no legible writing "
        "on any scroll, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, no blood, no children. Light, natural comedic tone like "
        "a documentary-style drama: the humor is in what Anh Tư says, not in his face; he smiles at most once, softly. "
        "The king, the officials and the envoy stay serious.")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN "
          "voice-over; nobody on screen moves their lips")
V_SU = "the Yuan envoy = a deep, cold, formal male voice in his 50s, speaking Vietnamese with a slight foreign accent"
V_VUA = ("the Trần king = a calm, soft-spoken, dignified male voice in his 30s, Northern Vietnamese accent; he is seen ONLY "
         "from behind, his face and mouth never visible")

SCENES = {
    "A": dict(name="Sân điện, sứ đọc chiếu (ban ngày)",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): the brick courtyard in front of the main palace "
                    "hall at Thăng Long, late morning, soft hazy sunlight, a wide stone staircase leading up to the hall with "
                    "red-lacquered pillars, two bronze incense burners at the foot of the stairs, a large old banyan tree on "
                    "the left, Trần officials in dark robes standing in two silent rows. The Yuan envoy stands at the foot of "
                    "the stairs holding an unrolled scroll. Anh Tư, a palace guard with a spear, stands by the gate on the right."),
              img=("Cinematic shot of a brick palace courtyard at Thăng Long, late morning hazy sunlight, a wide stone staircase "
                   "up to a hall with red-lacquered pillars, two bronze incense burners, a large banyan tree on the left, Trần "
                   "officials in two silent rows, a Yuan envoy in a dark brocade robe and round fur-trimmed hat holding an "
                   "unrolled scroll at the foot of the stairs, {FACE}, standing guard with a spear by the gate on the right, "
                   "realistic, vertical 9:16."),
              amb="courtyard birds, soft wind, rustling scroll"),
    "B": dict(name="Trong điện, vua trả lời sứ",
              lock=("SCENE B (keep IDENTICAL in every clip of this scene): inside the dim palace hall, red-lacquered pillars, "
                    "warm light from oil lamps and from the open doors behind, a low dais. The Trần king in a dark robe sits on "
                    "the dais and is seen ONLY from behind. The Yuan envoy stands below the dais, facing the king. Anh Tư stands "
                    "beside a pillar on the left, holding a tea tray."),
              img=("Cinematic shot inside a dim palace hall, red-lacquered pillars, warm oil-lamp light and bright open doors "
                   "behind, a Trần king in a dark robe seated on a low dais seen only from behind, a Yuan envoy in a dark "
                   "brocade robe standing below facing him, {FACE}, beside a pillar holding a tea tray, realistic, vertical 9:16."),
              amb="quiet hall, faint wind through the doors"),
    "C": dict(name="Hành lang cung, đêm",
              lock=("SCENE C: a palace corridor at night, a row of red-lacquered pillars, small oil lamps on stands, a wooden "
                    "railing and a dark garden beyond. Anh Tư is alone, leaning on a pillar with his spear."),
              img=("Cinematic shot of a palace corridor at night, red-lacquered pillars, small oil lamps, a wooden railing and "
                   "dark garden, {FACE}, alone, leaning on a pillar with his spear, realistic, vertical 9:16."),
              amb="night insects, distant footsteps"),
    "D": dict(name="Tường thành, hoàng hôn",
              lock=("SCENE D (keep IDENTICAL in every clip of this scene): the top of the palace wall at dusk, orange sky, "
                    "below a long dirt road winding north through rice fields into the hills, the roofs of Thăng Long on the "
                    "other side. Anh Tư stands alone on the wall with his spear."),
              img=("Cinematic shot from the top of a palace wall at dusk, orange sky, a long dirt road winding north through "
                   "rice fields into the hills, the roofs of Thăng Long on the other side, {FACE}, alone on the wall with "
                   "his spear, realistic, vertical 9:16."),
              amb="evening birds, soft wind"),
    "E": dict(name="Sân điện, sứ khác sang (vài năm sau)",
              lock=("SCENE E (keep IDENTICAL in every clip of this scene): the SAME brick courtyard as scene A, with the same "
                    "staircase, incense burners and banyan tree, but on a grey overcast day; a different, older Yuan envoy in a "
                    "dark brocade robe and round fur-trimmed hat reads a sealed scroll at the foot of the stairs; Anh Tư stands "
                    "guard by the gate on the right."),
              img=("Cinematic shot of a brick palace courtyard on a grey overcast day, the same stone staircase, bronze incense "
                   "burners and banyan tree, an older Yuan envoy in a dark brocade robe and round fur-trimmed hat reading a "
                   "sealed scroll, {FACE}, standing guard by the gate on the right, realistic, vertical 9:16."),
              amb="grey wind, rustling scroll"),
    "F": dict(name="Sân kho, hoàng hôn",
              lock=("SCENE F (keep IDENTICAL in every clip of this scene): a palace storeroom yard at dusk, a row of heavy "
                    "wooden gift chests with bronze corners, bolts of silk and baskets stacked beside them, a thatched "
                    "storehouse behind. Anh Tư sits alone on one of the chests."),
              img=("Cinematic shot of a palace storeroom yard at dusk, a row of heavy wooden gift chests with bronze corners, "
                   "bolts of silk and baskets, a thatched storehouse behind, {FACE}, sitting alone on one of the chests, "
                   "realistic, vertical 9:16."),
              amb="dusk birds, soft wind"),
}

# Mỗi clip: một cảnh, MỘT người nói, lời lấp gần kín 10 giây (khoảng 20 đến 26 chữ, nói vừa phải).
CLIPS = [
    dict(scene="A", who="su", label="Thăng Long · thời Trần",
         line=(0.4, 9.0, "Hoàng đế có chiếu: / vua nước Nam / phải thân hành sang chầu, / không được sai / người khác thay!"),
         cam="the envoy at the foot of the stairs faces the camera and reads from the scroll; officials silent behind; Anh Tư far away by the gate, too small to see his mouth"),
    dict(scene="A", who="narr",
         line=(0.8, 9.2, "Năm 1267, / nhà Nguyên đòi sáu điều. / Điều đầu tiên, / cũng là điều khó nhất: / vua phải sang chầu."),
         cam="slow high aerial over the courtyard and the hall roofs; people seen only as small figures from above; no faces visible"),
    dict(scene="A", who="tu",
         line=(0.4, 9.2, "Còn đòi con tin, kê dân, / bắt lính, nộp thuế… / Đi chợ còn mặc cả, / đằng này đòi một lèo / sáu món, không bớt."),
         cam="close-up of Anh Tư alone by the gate, quietly counting on his fingers, then a glance at the camera; the envoy is out of frame"),
    dict(scene="B", who="vua",
         line=(0.4, 9.2, "Ta sinh trưởng / trong thâm cung, / không quen cưỡi ngựa, / không hợp thủy thổ, / e chết dọc đường."),
         cam="from behind the king on the dais, looking toward the envoy below, who listens with his mouth closed; Anh Tư out of frame"),
    dict(scene="B", who="tu",
         line=(0.4, 9.2, "Vua bảo không quen / cưỡi ngựa… / Em cưỡi giỏi nhất làng / mà có ai mời đâu. / Đi sứ cũng phải có số."),
         cam="Anh Tư alone in frame beside the pillar holding the tea tray, speaking quietly toward the camera; the king and the envoy are out of frame"),
    dict(scene="C", who="tu", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Bệnh này lạ lắm: / sứ sang là sốt, / sứ về là khỏi. / Thầy thuốc bắt mạch xong / chỉ hỏi: sứ về chưa?"),
         cam="medium close-up of Anh Tư alone leaning on the pillar, a short pause before the last words, a faint smile"),
    dict(scene="D", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Đi, có thể bị giữ / làm con tin. / Không đi, giặc có cớ / động binh. / Cáo ốm thì còn / kéo thêm được thời gian."),
         cam="wide shot of the long road winding north at dusk; Anh Tư seen small and from behind on the wall; no faces visible"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Đằng nào cũng khó… / thì chọn cái khó ở nhà. / Ở nhà còn cơm vợ nấu, / sang đấy ăn gì, / ai mà biết."),
         cam="Anh Tư turns from the road to the camera, calm, a small nod"),
    dict(scene="E", who="su", chuyen="fadeblack:0.6", label="Năm 1281",
         line=(0.8, 9.2, "Ngươi cáo bệnh / không sang, thì cứ ở nhà / mà thuốc thang. / Hoàng đế đã lập / người khác làm vua!"),
         cam="the older envoy faces the camera and reads the sealed scroll, cold; Anh Tư far away by the gate, too small to see his mouth"),
    dict(scene="E", who="tu",
         line=(0.4, 9.2, "Xin nghỉ ốm một hôm… / mà sếp cho nghỉ hẳn, / tuyển luôn người mới. / Có điều vua mình / vẫn chưa nộp đơn."),
         cam="close-up of Anh Tư alone by the gate, eyebrows raised, a short glance at the camera; the envoy is out of frame"),
    dict(scene="F", who="narr", chuyen="fadeblack:0.6", label="Năm 1286",
         line=(0.8, 9.3, "Năm 1286, nhà Nguyên / phong Trần Ích Tắc / làm vua An Nam, / đóng thuyền, gom quân… / chuẩn bị sang / lần thứ ba."),
         cam="slow push along the row of gift chests in the dusk light; Anh Tư seen only from behind at the end of the row; no faces visible"),
    dict(scene="F", who="tu",
         line=(0.4, 9.2, "Gần hai mươi năm, / quà thì gửi đủ mùa, / thư thì gửi đủ lời. / Lễ vật thì gửi… / người thì không đi."),
         cam="Anh Tư sitting on a gift chest pats the lid, looks at the camera, calm, with a faint resigned smile"),
]
WHO = {"tu": "ANH TƯ", "su": "THE YUAN ENVOY", "vua": "THE TRẦN KING (seen only from behind)",
       "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "su": "Sứ Nguyên", "vua": "Vua Trần", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "su": V_SU, "vua": V_VUA, "narr": V_NARR}
PREFIX = {"su": "Sứ Nguyên: / ", "vua": "Vua Trần: / ", "tu": "", "narr": ""}


def video_prompt(c):
    a, b, text = c["line"]
    sc = SCENES[c["scene"]]
    return " ".join(x for x in [
        BASE, sc["lock"], FACE + ".", RULES.format(who=WHO[c["who"]]),
        f"0-{a:.1f}s: silence. {a:.1f}-{b:.1f}s: ONLY {WHO[c['who']]} speaks: \"{spoken(text)}\" {b:.1f}-10s: a short silent beat, hold the shot.",
        f"Camera: {c['cam']}.", f"VOICE: {VOICE[c['who']]}.", AUDIO.format(amb=sc["amb"])] if x)


def main():
    base = "bd1288-tap1"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Vua ốm / chỉ phát khi / sứ sang", "end: Follow để xem / Anh đan sọt →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 1: Vua cáo ốm (bản đầy đủ)", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook. Thay cho bản v3 (`prompts-bach-dang-1288-tap1-vua-cao-om-v3.md`).", "",
          f"**File Muse đặt tên:** `bd1288-tap1-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc, tự nhiên, hài nhẹ; vua Trần trầm, "
          "chậm; sứ Nguyên lạnh, trang trọng; dẫn chuyện giọng Bắc trầm.", "",
          "## Sửa gì so với bản v3", "",
          "1. **Mỗi clip một người nói, lời lấp gần kín 10 giây** (khoảng 20 đến 24 chữ, nói từ giây 0,4 đến 9,2, nhịp vừa phải, khoảng 2,5 chữ/giây). "
          "Bản v3 dồn 30 đến 40 chữ vào một clip nên Muse nói vội và nhảy giọng; bản trước của em lại quá ngắn, trống 2 đến 3 giây mỗi clip. Giờ ở giữa hai cái đó.",
          "2. **Ai nói lời người nấy:** sứ tự đọc chiếu và thư, vua tự trả lời (quay từ phía sau), Anh Tư chỉ pha trò. Đối đáp thì "
          "mỗi người một clip liền nhau, chuyển nhẹ 0,3 giây.",
          "3. **Khóa bối cảnh theo cảnh (A đến F):** các clip cùng cảnh dùng y nguyên đoạn `SCENE …` và chung một ảnh khung đầu.",
          "4. **Người dẫn chuyện chỉ nói ở cảnh không thấy mặt ai** (quay từ trên cao, quay con đường, quay hàng hòm), nên không lồng "
          "vào giọng Anh Tư.",
          "5. **Bỏ con số \"12 lần đòi chầu\"** vì chưa có nguồn chắc; nói \"cứ sứ sang là ốm\".",
          "6. Anh Tư diễn vui vẻ bình thường như các clip đầu; giọng Bắc theo yêu cầu mới.", "",
          "**Lịch sử (mức A/B):** năm 1267 Hốt Tất Liệt đòi sáu điều: vua sang chầu, con em làm con tin, kê khai dân số, chịu "
          "quân dịch, nộp thuế, đặt quan Đạt lỗ hoa xích (A). Các vua Trần nhiều lần cáo bệnh, không sang chầu; một lần trả lời sứ "
          "Sài Thung rằng sinh trưởng trong thâm cung, không quen cưỡi ngựa, không quen thủy thổ, sợ chết dọc đường (B). Năm 1281 nhà "
          "Nguyên lập Trần Di Ái làm vua An Nam; năm 1286 phong Trần Ích Tắc làm An Nam quốc vương và chuẩn bị đánh lần thứ ba (A). "
          "**Lời vua (clip 4) và thư (clip 9) là phỏng theo ý sử chép, không nhận là nguyên văn; cần đối chiếu *Toàn thư* và *Nguyên "
          "sử* trước khi đăng, nhất là câu clip 4 là lời vua nào, năm nào.** Kể trung tính về Trần Di Ái và Trần Ích Tắc.", "",
          "## Xem nhanh: toàn bộ hội thoại", "", "| Clip | Cảnh | Người nói (duy nhất) | Câu |", "|---|---|---|---|"]
    md += [f"| {i} | {c['scene']} · {SCENES[c['scene']]['name']} | {NAME[c['who']]} | {spoken(c['line'][2])} |"
           for i, c in enumerate(CLIPS, 1)] + [""]
    md += ["## Ảnh khung đầu từng cảnh (tạo một lần, dùng chung cho các clip cùng cảnh, kèm `anh_tu_ref.png`)", ""]
    for k, sc in SCENES.items():
        clips = ", ".join(str(i) for i, c in enumerate(CLIPS, 1) if c["scene"] == k)
        md += [f"**Cảnh {k} · {sc['name']}** (clip {clips}): lưu thành `{base}-canh-{k}.png`", "```",
               sc["img"].format(FACE=FACE), "```", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"{base}-{i}.mp4"
        a, b, text = c["line"]
        md += [f"## Clip {i} · cảnh {c['scene']}",
               f"File Muse đặt tên: `{f}` · Ảnh khung đầu: `{base}-canh-{c['scene']}.png` + `anh_tu_ref.png`", "",
               f"**Chỉ {NAME[c['who']]} nói ({a:.1f}–{b:.1f}s):** \"{spoken(text)}\"", "",
               "**Video (Muse)**", "```", video_prompt(c), "```", ""]
        extra = f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""
        plan.append(f"clip: {f} | {c.get('label', '')}{extra}")
        subs.append(f"sub: {i} | {a}-{b} | {PREFIX[c['who']]}{text}")
    plan += [""] + subs
    with open(os.path.join(HERE, "_tap1_dang_bai.md"), encoding="utf-8") as fh:
        md += [fh.read().rstrip(), ""]
    md += ["## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + "-vua-cao-om.md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name, round(total, 1))


if __name__ == "__main__":
    main()
