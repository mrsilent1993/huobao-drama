#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 6 "Chặt que": đóng cọc ở sông Bạch Đằng, cảnh và âm thanh hoành tráng; mỗi clip một người nói,
khóa bối cảnh theo cảnh. Chạy: python3 _tap6.py → bd1288-tap6-chat-que.md + bd1288-tap6.plan.txt + Word
"""
import os
import sys

from _tap3 import FACE, V_TU, RULES, SO_RULE, noi, spoken
from _gioi_thieu import STAKE

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("EPIC cinematic historical film on a grand scale, live-action, photorealistic, sweeping aerial, crane and drone "
        "shots, thousands of extras, volumetric light through mist, mud spray and water droplets in slow motion, rich film "
        "grain, vertical 9:16. Đại Việt, late March 1288, the Bạch Đằng river estuary: a very wide brown tidal river "
        "between hundreds of towering limestone karst islands, mangrove banks, ironwood forests on the hills. Trần soldiers "
        "and villagers: hair in topknots, black-lacquered teeth, brown cotton tunics rolled up, bare legs in the mud. "
        + STAKE + " No modern objects, no on-screen text, no subtitles, no legible writing, ABSOLUTELY NO FLAGS OR BANNERS OF "
        "ANY KIND, no blood, no injuries, no children. The humor is in what Anh Tư says, not in his face; everyone else "
        "works hard and stays serious.")
# Tập này anh muốn âm thanh hoành tráng: có nhạc giao hưởng tự sáng tác, nhịp trống khớp nhịp búa nện, nằm DƯỚI lời nói.
AUDIO = ("Audio: an original EPIC orchestral score (deep taiko-like war drums whose beat matches the falling log rams, a low "
         "male choir hum, low strings, horns and a lonely Vietnamese bamboo flute motif) building in power, mixed UNDER the "
         "voice so every word stays perfectly clear; plus big natural sound: {amb}. All dialogue in Vietnamese.")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN "
          "voice-over; nobody on screen moves their lips")
V_CAI = "the squad leader = a clipped, gruff male voice in his 40s, Northern Vietnamese accent, short commands"
V_TRUONG = ("the stake-team leader = a big, powerful, rhythmic male voice in his 40s, Northern Vietnamese accent, calling "
            "the hauling rhythm loud and steady like a work chant, but not screaming")
V_LAIDO = "the old boatman = a slow, dry, gravelly elderly male voice in his 70s, Northern Vietnamese coastal accent"

SCENES = {
    "A": dict(name="Rừng lim trên đồi, buổi sáng",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): an ancient ironwood forest on a steep hill above the "
                    "Bạch Đằng river in morning mist and god rays, giant straight trunks as thick as a man's waist; hundreds "
                    "of soldiers and villagers fell trees with axes and saws, giant trunks crash down one after another, birds "
                    "burst out of the canopy. The squad leader in a dark tunic with a sword stands by a felled trunk. Anh Tư "
                    "holds a small knife beside a giant standing ironwood trunk."),
              img=("Epic shot of an ancient ironwood forest on a steep hill above a wide river in morning mist and god rays, "
                   "giant straight trunks, hundreds of men felling trees with axes and saws, a giant trunk crashing down, "
                   "{FACE}, holding a small knife beside a giant ironwood trunk, realistic, vertical 9:16."),
              amb="axes, saws, huge trees crashing down, birds bursting from the canopy, echoing shouts"),
    "B": dict(name="Bờ sông, kéo gỗ và đẽo cọc, giữa trưa",
              lock=("SCENE B (keep IDENTICAL in every clip of this scene): the wide riverbank at midday, a huge timber yard: "
                    "thousands of stripped ironwood trunks lie in rows, hundreds of men drag more trunks down the hill on "
                    "rollers with long ropes and water buffalo, log rafts float down the river, carpenters hew the tips to "
                    "crude points with adzes, wood chips flying. A team of eight men carries one trunk on shoulder poles; Anh "
                    "Tư walks in front of them holding a torch."),
              img=("Epic wide shot of a huge riverside timber yard at midday, thousands of stripped ironwood trunks in rows, "
                   "hundreds of men dragging trunks on rollers with ropes and water buffalo, log rafts on the wide river, "
                   "carpenters hewing points with adzes, eight men carrying one trunk on shoulder poles, {FACE}, walking in "
                   "front of them holding a torch, realistic, vertical 9:16."),
              amb="hundreds of ropes creaking, buffalo, adzes chopping, the river, a distant work chant"),
    "C": dict(name="Lòng sông lúc nước ròng: đóng cọc",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): the vast Bạch Đằng riverbed exposed at low tide "
                    "under a dramatic sky with sun shafts, glistening mud flats stretching from bank to bank between towering "
                    "karsts; dozens of tall wooden tripods stand in long rows across the whole river, at each one a team of a "
                    "dozen bare-legged men hauls ropes in unison to lift a heavy log ram and drop it on top of a giant pointed "
                    "ironwood stake, mud spraying with every blow; rows upon rows of finished stakes already stand taller than "
                    "the men, slanting toward the sea. The stake-team leader in a brown tunic with a red cloth headband stands "
                    "on a plank beside the nearest tripod. Anh Tư hauls a rope in the nearest team, knee-deep in mud."),
              img=("Epic shot of a vast tidal riverbed at low tide under a dramatic sky with sun shafts, mud flats from bank to "
                   "bank between towering limestone karsts, dozens of tall wooden tripods in long rows, teams of a dozen men "
                   "hauling ropes to drop heavy log rams onto giant pointed ironwood stakes taller than the men, mud "
                   "spraying, rows of finished stakes slanting toward the sea, {FACE}, knee-deep in mud hauling a rope in "
                   "the nearest team, realistic, vertical 9:16."),
              amb="the thunderous rhythmic thud of dozens of log rams in unison, mud splashes, ropes, gulls, wind"),
    "D": dict(name="Bờ sông ban đêm, xem con nước",
              lock=("SCENE D (keep IDENTICAL in every clip of this scene): night on the riverbank under a big full moon over "
                    "the karsts, the tide line glittering; a tall bamboo measuring pole with notches stands in the water; a "
                    "small fire; the old boatman with a white beard, a conical hat on his back and a bamboo pipe sits on an "
                    "upturned boat; Anh Tư sits on a rock beside the fire."),
              img=("Cinematic shot at night on a riverbank under a big full moon over limestone karsts, glittering tide line, "
                   "a tall notched bamboo measuring pole in the water, a small fire, an old white-bearded boatman with a "
                   "conical hat on his back sitting on an upturned boat, {FACE}, sitting on a rock by the fire, realistic, "
                   "vertical 9:16."),
              amb="lapping water, night insects, crackling fire"),
    "E": dict(name="Bình minh, triều lên nuốt rừng cọc",
              lock=("SCENE E: dawn over the Bạch Đằng estuary, the sky burning orange and pink behind the karsts; the tide "
                    "flooding in and swallowing the whole forest of stakes row by row until only smooth golden water remains. "
                    "Anh Tư stands alone on a rock on the bank."),
              img=("Epic shot at dawn over a wide estuary, orange and pink sky behind limestone karsts, the tide flooding in "
                   "over rows of giant pointed wooden stakes half swallowed by golden water, {FACE}, standing alone on a "
                   "rock on the bank, realistic, vertical 9:16."),
              amb="the rushing tide, wind, gulls, a last soft drum"),
}

CLIPS = [
    dict(scene="A", who="narr", label="Sông Bạch Đằng · cuối tháng 3/1288",
         line=(0.8, 9.2, "Cuối tháng ba năm 1288. / Hưng Đạo vương cho / đóng cọc chắn ngang / sông Bạch Đằng."),
         cam="huge aerial gliding over the misty forest as giant trees fall one after another in slow motion; no faces close enough to see"),
    dict(scene="A", who="cai",
         line=(0.4, 9.2, "Chặt que. / Que to bằng đùi mày, / dài hơn hai người. / Chặt cả cây lim, / đừng hỏi lại."),
         cam="the squad leader beside the felled trunk faces the camera and points up at the forest; Anh Tư is out of frame"),
    dict(scene="A", who="tu",
         line=(0.4, 9.2, "Họ bảo đi chặt que… / ủa alo, que gì / mà ôm không hết? / Cây này mà là que / thì em là con kiến."),
         cam="Anh Tư alone in frame tries to wrap both arms around the giant trunk, his hands far from meeting; he looks down at his small knife, then at the camera"),
    dict(scene="B", who="narr", chuyen="fade:0.5",
         line=(0.8, 9.2, "Hàng nghìn thân lim / được kéo xuống bờ sông, / đẽo nhọn, không bịt sắt… / chỉ chờ nước ròng."),
         cam="epic sweeping crane shot over the timber yard, the buffalo teams, the rafts and the flying wood chips; no faces close enough to see"),
    dict(scene="B", who="tu",
         line=(0.4, 9.2, "Tám người khiêng một que… / em cầm đuốc / giữa ban ngày. / Không khiêng gì cả / mà vẫn đỉnh nóc / kịch trần."),
         cam="tracking shot in front of Anh Tư walking with the torch in bright midday sun while eight straining men carry the giant trunk behind him; the men stay silent"),
    dict(scene="C", who="narr", chuyen="fadeblack:0.6", label="Nước ròng",
         line=(0.8, 9.2, "Nước ròng. / Cả lòng sông lộ ra. / Hàng trăm giá ba chân / dựng lên cùng một lúc."),
         cam="massive aerial reveal over the exposed riverbed as the rows of tripods rise and the first rams drop in unison with the drums; no faces close enough to see"),
    dict(scene="C", who="truong",
         line=(0.4, 9.2, "Kéo… thả! / Kéo… thả! / Mỗi nhát một tấc! / Nước lên mà chưa xong / hàng này thì đừng ai về!"),
         cam="the stake-team leader on the plank faces the camera calling the rhythm, and behind him the ram rises and slams down on every 'thả'; nobody else speaks"),
    dict(scene="C", who="tu",
         line=(0.4, 9.2, "Em hô sớm một nhịp… / cả đội quay lại nhìn. / Ét ô ét… / từ giờ em chỉ kéo, / không hô nữa."),
         cam="Anh Tư alone in close-up, knee-deep in mud, hauling the rope, mud splattered on his face; a short sigh"),
    dict(scene="C", who="narr",
         line=(0.8, 9.2, "Hàng nối hàng, / cọc lim chắn ngang / cả lòng sông rộng, / đầu nhọn chĩa ra biển."),
         cam="extreme low angle at the foot of one enormous stake towering against the sun as the ram drops a final time, then a rising aerial over the endless rows across the river to the sea; no faces visible"),
    dict(scene="D", who="laido", chuyen="fadeblack:0.6",
         line=(0.4, 9.2, "Nước rút đúng giờ Thìn. / Cọc phải thấp hơn / mặt nước lên… / thì thuyền lớn mới mắc."),
         cam="the old boatman on the upturned boat faces the camera, pointing his pipe at the notched measuring pole; Anh Tư is out of frame"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Ngồi xem nước cả tuần… / vợ hỏi làm gì, / em bảo: lo việc nước. / Đúng mà… / nước sông Bạch Đằng."),
         cam="Anh Tư alone by the fire, looking from the moonlit water to the camera, a faint smile"),
    dict(scene="E", who="tu", chuyen="fadeblack:0.6",
         line=(0.4, 9.2, "Nước lên… / cọc biến mất. / Giặc mà qua đây… / là tới công chuyện. / Cả trận trông vào / nước rút."),
         cam="grand time-lapse: the tide swallows the stakes behind Anh Tư while he stands on the rock; at the end he turns to the camera, calm"),
]
WHO = {"tu": "ANH TƯ", "cai": "THE SQUAD LEADER", "truong": "THE STAKE-TEAM LEADER", "laido": "THE OLD BOATMAN",
       "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "cai": "Cai đội", "truong": "Trưởng toán đóng cọc", "laido": "Ông lái đò", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "cai": V_CAI, "truong": V_TRUONG, "laido": V_LAIDO, "narr": V_NARR}
PREFIX = {k: "" for k in NAME}


def video_prompt(c):
    a, b, text = c["line"]
    sc = SCENES[c["scene"]]
    face = FACE + "." if c["who"] == "tu" or "{FACE}" in sc["img"] else ""
    return " ".join(x for x in [
        BASE, sc["lock"], face, RULES.format(who=WHO[c["who"]]),
        f"0-{a:.1f}s: silence. {a:.1f}-{b:.1f}s: ONLY {WHO[c['who']]} speaks: \"{noi(text)}\" {b:.1f}-10s: a short beat, hold the shot.",
        f"Camera: {c['cam']}.", f"VOICE: {VOICE[c['who']]}.", AUDIO.format(amb=sc["amb"]), SO_RULE] if x)


DANG_BAI = """## Đăng TikTok

**Hook** (chữ to ở giây đầu, dùng luôn làm chữ trên ảnh bìa):
```
POV: Bạn được giao / đi chặt que
```

Hook dự phòng:
```
POV: Que to bằng đùi / tám người khiêng
POV: Cả trận đánh / trông vào giờ nước rút
```

**Tiêu đề:**
```
Đóng cọc sông Bạch Đằng: "chặt que" mà ôm không hết | Bạch Đằng 1288 tập 6
```

**Mô tả và hashtag:**
```
Được giao đi chặt que… mà que là cả cây lim, tám người khiêng 🪵 Nước ròng, cả lòng sông lộ ra, hàng trăm giá ba chân dựng lên cùng lúc, cọc lim chắn ngang sông Bạch Đằng, đầu nhọn chĩa ra biển. Rồi nước lên, cọc biến mất. Đây là tập 6 của loạt Bạch Đằng 1288. Theo bạn, vì sao cọc phải thấp hơn mặt nước lên? 👇
#povlichsu #POV #lichsuvietnam #xuhuong #fyp #bachdang1288 #bachdang #tranhungdao #anhtu
```

**Bình luận ghim:**
```
Tập 7 ngày mai 19h: cả quân thề phải thắng… còn Anh Tư được lệnh đi thua 😅 Follow để không lỡ tập nào!
```

**Mẫu trả lời 60 phút đầu:**
1. (Về cọc) "Cọc trận 1288 là cả thân cây lim và các loại gỗ cứng, đẽo nhọn, không bịt sắt. Bãi cọc còn tìm thấy ở Quảng Yên (Quảng Ninh) và Thủy Nguyên (Hải Phòng)."
2. (Về con nước) "Cọc cắm thấp hơn mặt nước lúc triều lên: thuyền giặc đi qua không thấy, đến khi triều rút thì mắc cọc."
3. (Về cách đóng) "Cách dựng giá ba chân, búa gỗ trong video là phần dựng lại cho sinh động; sử chỉ chép việc cắm cọc lúc nước ròng."

Khi đăng: bật nhãn "Nội dung do AI tạo".

## Đăng YouTube Shorts

**Tiêu đề:**
```
Đóng cọc sông Bạch Đằng 1288: "chặt que" mà ôm không hết | Bạch Đằng 1288 tập 6 #Shorts
```

**Mô tả:**
```
Được giao đi chặt que… mà que là cả cây lim, tám người khiêng 🪵 Nước ròng, hàng trăm giá ba chân dựng lên, cọc lim chắn ngang sông Bạch Đằng. Rồi nước lên, cọc biến mất. Đây là tập 6 của loạt Bạch Đằng 1288.

Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 10 tập.

#Shorts #povlichsu #lichsuvietnam #bachdang1288 #tranhungdao #anhtu
```

**Thẻ:**
```
cọc bạch đằng, đóng cọc 1288, bãi cọc bạch đằng, trần hưng đạo, bạch đằng 1288, kháng chiến chống nguyên, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts
```

Mục "Nội dung bị thay đổi" chọn **Có**.

## Đăng Facebook

**Caption:**
```
Cả nhà ơi, 19h tối nay có tập 6 loạt Bạch Đằng 1288 nè 🪵

Tui được giao đi chặt que… que to bằng đùi, tám người khiêng, còn tui cầm đuốc chỉ đường giữa ban ngày 😂

Nước ròng, hàng trăm giá ba chân dựng lên cùng lúc, cọc lim chắn ngang cả sông Bạch Đằng. Rồi nước lên… cọc biến mất.

Cả nhà đoán vì sao cọc phải thấp hơn mặt nước lên? 👇

#BachDang1288 #TranHungDao #POVMotNgayODaiViet #LichSuVietNam
```

Đăng dạng **Reel**, cùng một bản với TikTok và YouTube. Bật "Thông tin về AI"."""


def main():
    base = "bd1288-tap6"
    md_name = base + "-chat-que.md"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Bạn được giao / đi chặt que", "end: Follow để xem / Ông thề thắng, em đi thua →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 6: Chặt que (đóng cọc sông Bạch Đằng)", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook · **8/12 clip là cảnh đẵn gỗ, kéo gỗ, đóng cọc, triều lên.**", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); dẫn chuyện giọng Bắc "
          "trầm; cai đội, trưởng toán đóng cọc, ông lái đò mỗi người một giọng riêng.", "",
          "## Mạch tập", "",
          "- **Rừng lim** (clip 1–3): lệnh đóng cọc; \"chặt que, que to bằng đùi mày\"; Anh Tư ôm cây lim không hết.",
          "- **Kéo gỗ, đẽo cọc** (clip 4–5): hàng nghìn thân lim, trâu kéo, bè gỗ trôi sông; tám người khiêng một cây, Anh Tư cầm đuốc đi trước giữa ban ngày.",
          "- **Đóng cọc lúc nước ròng** (clip 6–9, cảnh chính): cả lòng sông lộ ra, hàng trăm giá ba chân, búa gỗ nện đồng loạt theo nhịp trống; trưởng toán hô \"Kéo… thả!\"; cọc lim chắn ngang cả sông, đầu nhọn chĩa ra biển.",
          "- **Xem con nước** (clip 10–11) và **triều lên nuốt cọc** (clip 12, câu chốt).",
          "- **Âm thanh hoành tráng** (theo yêu cầu): nhạc giao hưởng tự sáng tác, trống trận khớp nhịp búa nện, dàn hợp xướng nam, kèn, sáo trúc; nhạc nằm **dưới** lời nói để nghe rõ từng chữ. Nếu Muse không ra nhạc, em ghép nhạc khi dựng.",
          "- **Cọc phải bự** (góp ý người xem): mô tả cỡ cọc có trong mọi prompt: cả thân lim to bằng đùi, dài 2,5–3 m, 6–10 người khiêng, cắm xong vẫn cao hơn người, không bịt sắt.",
          "- **Câu trending (anh yêu cầu):** chỉ Anh Tư nói, mỗi clip tối đa một câu: \"ủa alo\", \"đỉnh nóc kịch trần\", \"ét ô ét\", \"lo việc nước\" (chơi chữ), \"tới công chuyện\". Người khác giữ nghiêm.",
          "- Mỗi clip một người nói, lời lấp gần kín 10 giây; cảnh nào khóa bối cảnh cảnh đó. Năm trong lời thoại đã viết thành chữ.", "",
          "**Lịch sử:** cuối tháng 3/1288 Trần Hưng Đạo cho đóng cọc lớn đầu nhọn ở lòng sông Bạch Đằng gần cửa biển, cắm lúc "
          "nước ròng, lợi dụng thủy triều (A; bãi cọc khảo cổ ở Quảng Yên, Thủy Nguyên). Cọc 1288 **không bịt sắt** (khác trận 938). "
          "**Phần dựng lại:** rừng lim, trâu kéo gỗ, giá ba chân, búa gỗ, giờ nước \"giờ Thìn\" của ông lái đò là chi tiết dựng "
          "cho sinh động, không phải sử chép từng chữ. **Hư cấu:** Anh Tư, cai đội, trưởng toán, ông lái đò và mọi lời thoại.", "",
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
        md += [f"## Clip {i} · cảnh {c['scene']} · {SCENES[c['scene']]['name']}",
               f"File Muse đặt tên: `{f}` · Ảnh khung đầu: `{base}-canh-{c['scene']}.png`"
               + (" + `anh_tu_ref.png`" if c["who"] == "tu" or "{FACE}" in SCENES[c["scene"]]["img"] else ""), "",
               f"**Chỉ {NAME[c['who']]} nói ({a:.1f}–{b:.1f}s):** \"{spoken(text)}\""
               + (f" · *Muse đọc:* \"{noi(text)}\"" if noi(text) != spoken(text) else ""), "",
               "**Video (Muse)**", "```", video_prompt(c), "```", ""]
        extra = f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""
        plan.append(f"clip: {f} | {c.get('label', '')}{extra}")
        subs.append(f"sub: {i} | {a}-{b} | {PREFIX[c['who']]}{text}")
    plan += [""] + subs
    md += [DANG_BAI, "", "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((md_name, md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name, round(total, 1))
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import xuat_word
    print(xuat_word.convert(os.path.join(HERE, md_name)))


if __name__ == "__main__":
    main()
