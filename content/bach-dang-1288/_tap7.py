#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 7 "Ông thề thắng, em đi thua": nồi nước thơm (giải câu đố trailer), lời thề sông Hóa, nhử địch.
Mỗi clip một người nói, khóa bối cảnh theo cảnh. Chạy: python3 _tap7.py → bd1288-tap7-the-thang-di-thua.md + plan + Word
"""
import os
import sys

from _tap3 import FACE, V_TU, RULES, SO_RULE, noi, spoken
from _gioi_thieu import STAKE

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("EPIC cinematic historical film on a grand scale, live-action, photorealistic, sweeping aerial, crane and drone "
        "shots, thousands of extras, volumetric light through mist, rich film grain, vertical 9:16. Đại Việt, early April "
        "1288, the Trần kingdom and the Bạch Đằng estuary: wide brown tidal rivers between hundreds of towering limestone "
        "karsts, mangrove banks. Trần people: hair in topknots, black-lacquered teeth, brown or dark cotton tunics; Trần "
        "Hưng Đạo and other generals are seen ONLY from behind or far away, never their faces. Yuan fleet: big wooden "
        "war junks with matting sails, soldiers in lamellar armor. " + STAKE + " No modern objects, no on-screen text, no "
        "subtitles, no legible writing, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, no blood, no gore, no dead bodies, no "
        "children. The humor is in what Anh Tư says, not in his face; everyone else stays serious.")
AUDIO = "Audio: {amb}; any music stays UNDER the voice so every word is perfectly clear. All dialogue in Vietnamese."
EPIC = ("an original epic orchestral score with deep war drums, low male choir hum, low strings, horns and a bamboo "
        "flute motif")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN "
          "voice-over; nobody on screen moves their lips")
V_HD = ("Trần Hưng Đạo = a deep, resonant, unhurried male voice in his late 50s, Northern Vietnamese accent, grave and "
        "absolutely certain; he is seen ONLY from behind, his face and mouth never visible")
V_CAI = "the squad leader = a clipped, gruff male voice in his 40s, Northern Vietnamese accent, short commands"

SCENES = {
    "A": dict(name="Sân sau phủ Hưng Đạo, nồi nước thơm",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): the back courtyard of a great Trần prince's "
                    "residence in late afternoon golden light, dark wooden halls with red-lacquered pillars, an old frangipani "
                    "tree; a huge bronze cauldron steaming over a wood fire, pomelo leaves, lemongrass and herbs floating in "
                    "the fragrant water; a large wooden bathing tub on stone slabs beside it. Anh Tư tends the fire with a long "
                    "wooden ladle. Two Trần lords in dark silk robes, seen ONLY from behind, sit and stand by the tub: one "
                    "pours water with a wooden scoop over the shoulders of the other, who sits fully robed."),
              img=("Cinematic shot of the back courtyard of a great medieval Vietnamese residence in golden late-afternoon "
                   "light, red-lacquered pillars, an old frangipani tree, a huge steaming bronze cauldron with pomelo leaves "
                   "and herbs, a large wooden bathing tub on stone slabs, {FACE}, tending the fire with a long ladle, "
                   "realistic, vertical 9:16."),
              amb="crackling wood fire, bubbling water, birds in the frangipani, a soft bamboo flute melody"),
    "B": dict(name="Vượt sông Hóa",
              lock=("SCENE B (keep IDENTICAL in every clip of this scene): the Hóa river on a bright windy morning, a wide "
                    "brown river between green banks and karst hills; hundreds of boats carrying thousands of Trần soldiers "
                    "cross in a vast fleet behind; in the foreground a small wooden ferry: Trần Hưng Đạo in a dark robe and "
                    "black sash stands at the prow, seen ONLY from behind, gazing at the far bank; Anh Tư rows at the stern "
                    "with a long oar."),
              img=("Epic shot of a wide brown river on a bright windy morning, hundreds of boats carrying thousands of "
                   "soldiers crossing behind, in the foreground a small wooden ferry with a general in a dark robe seen only "
                   "from behind at the prow, {FACE}, rowing at the stern with a long oar, realistic, vertical 9:16."),
              amb=f"wind, water, thousands of oars, {EPIC} rising slowly"),
    "C": dict(name="Rạng sáng, đoàn thuyền nhẹ chuẩn bị",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): pre-dawn blue light at the Bạch Đằng river mouth, "
                    "mist on the water, karst silhouettes; a line of small light Trần war boats waiting, crews holding bows "
                    "and oars. The squad leader in a dark tunic with a sword stands in the lead boat. Anh Tư sits at the oar "
                    "in the next boat."),
              img=("Cinematic shot in pre-dawn blue light at a river mouth, mist on the water, limestone karst silhouettes, "
                   "a line of small light war boats waiting with crews holding bows and oars, {FACE}, sitting at the oar, "
                   "realistic, vertical 9:16."),
              amb="quiet water, a few creaking oars, distant gulls, very low drums"),
    "D": dict(name="Giả thua, hạm đội Nguyên đuổi vào sông",
              lock=("SCENE D (keep IDENTICAL in every clip of this scene): sunrise over the Bạch Đằng estuary between towering "
                    "karsts; the small light Trần boats flee upriver at full speed, looking back; behind them a vast Yuan "
                    "war fleet, more than a hundred big junks with matting sails, gives chase in a wide front, bow waves "
                    "foaming, arrows splashing harmlessly in the water. Anh Tư rows hard in one of the fleeing boats."),
              img=("Epic sunrise shot over a wide estuary between towering limestone karsts, small light war boats fleeing "
                   "upriver at full speed, behind them a vast fleet of more than a hundred big wooden junks with matting "
                   "sails chasing in a wide front, foaming bow waves, {FACE}, rowing hard in a fleeing boat, realistic, "
                   "vertical 9:16."),
              amb=f"rushing water, hundreds of oars, creaking sails, distant war cries, {EPIC} driving hard"),
    "E": dict(name="Nước lên che bãi cọc",
              lock=("SCENE E (keep IDENTICAL in every clip of this scene): morning high tide on the Bạch Đằng river: smooth "
                    "golden water covers the whole hidden forest of stakes, only faint ripples where the tips lie just "
                    "beneath; the great Yuan fleet sails deeper upriver right over them; on the far bank in the reeds, "
                    "beyond the stake field, the small light boats are pulled up and Anh Tư stands beside his boat, panting."),
              img=("Epic aerial at morning high tide over a wide river between karsts, smooth golden water with faint ripples "
                   "over hidden stake tips just beneath the surface, a great fleet of wooden junks sailing upriver over them, "
                   "small boats pulled up in the reeds on the far bank, {FACE}, standing beside his boat, realistic, "
                   "vertical 9:16."),
              amb=f"calm water, creaking hulls, gulls, {EPIC} holding one long tense note"),
}

CLIPS = [
    dict(scene="A", who="tu", label="Trước trận Bạch Đằng",
         line=(0.4, 9.2, "Nồi nước thơm thế này… / em xin tắm trước, / người ta bảo: / ủa rồi ai mượn? / Thôi em đun tiếp."),
         cam="Anh Tư alone in frame stirring the steaming cauldron, sniffing the fragrant steam, then looking at the camera"),
    dict(scene="A", who="narr",
         line=(0.8, 9.2, "Hưng Đạo vương / và Thượng tướng / Quang Khải / vốn không hòa thuận… / vậy mà ông tự tay / tắm cho Quang Khải."),
         cam="from behind the two lords at the wooden tub: one gently pours a scoop of fragrant water over the shoulders of the other, steam rising in the golden light; no faces visible"),
    dict(scene="A", who="tu",
         line=(0.4, 9.2, "Giận nhau mấy chục năm… / làm lành bằng chậu nước. / Em với vợ giận nhau, / đun cả nồi / vẫn chưa đủ wow."),
         cam="Anh Tư alone in frame by the fire, ladle in hand, eyebrows raised, a faint smile; the lords are out of frame"),
    dict(scene="B", who="narr", chuyen="fadeblack:0.6", label="Đầu tháng 4/1288",
         line=(0.8, 9.2, "Đầu tháng tư năm 1288, / Hưng Đạo vương / dẫn quân ra Bạch Đằng. / Qua sông Hóa…"),
         cam="grand aerial over the river as the vast fleet crosses, then descending toward the small ferry in front; no faces visible"),
    dict(scene="B", who="hd",
         line=(1.2, 8.8, "Trận này không phá xong / giặc Nguyên… / thì ta không về / đến sông này nữa!"),
         cam="from behind Trần Hưng Đạo at the prow as he raises his hand over the water and speaks each word slowly and gravely, with weight; one deep drum beat at the end; his face never visible; the oarsman is out of frame"),
    dict(scene="B", who="tu",
         line=(0.4, 9.2, "Ông thề không về / khúc sông này… / Em chèo về một mình / giữa đêm… / tới công chuyện rồi."),
         cam="Anh Tư alone in frame at the stern, still rowing, swallowing, then glancing at the camera; the general is out of frame"),
    dict(scene="C", who="cai", chuyen="fadeblack:0.6", label="Rạng sáng 9/4/1288",
         line=(0.4, 9.2, "Sáng nay đi thua. / Thua cho giống, / chạy cho chậm. / Ai lỡ thắng / thì về chịu phạt!"),
         cam="the squad leader standing in the lead boat faces the camera; Anh Tư is out of frame"),
    dict(scene="C", who="tu",
         line=(0.4, 9.2, "Cả quân thề thắng… / mỗi em được giao thua. / Đúng nhận, sai cãi… / mà lệnh thì / em không dám cãi."),
         cam="Anh Tư alone in frame at his oar in the blue mist, a short pause, a small sigh"),
    dict(scene="D", who="narr", chuyen="fade:0.3",
         line=(0.8, 9.2, "Thuyền nhẹ ra khiêu chiến / rồi giả thua. / Hạm đội Ô Mã Nhi / đuổi theo… / vào thẳng sông Bạch Đằng."),
         cam="huge aerial at sunrise: the small boats turn and flee, the vast fleet surges after them between the karsts; no faces close enough to see"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Chạy chậm thôi các bác… / họ theo thật rồi! / Trăm thuyền đuổi / một thuyền em… / Nín. Chèo tiếp."),
         cam="tracking shot alongside Anh Tư rowing hard; he glances back at the wall of sails closing in; nobody else speaks"),
    dict(scene="E", who="narr", chuyen="fade:0.5",
         line=(0.8, 9.2, "Nước triều đang lên, / che kín bãi cọc. / Không ai trên thuyền giặc / biết thứ đang chờ / dưới mặt sông."),
         cam="slow aerial descending to the water surface as the great fleet glides over the faint ripples; then underwater: dark hulls pass just above the giant stake tips; no faces visible"),
    dict(scene="E", who="tu",
         line=(0.4, 9.2, "Được lệnh thua… / mà phải thua cho khéo. / Giặc hỏi dưới sông / có gì à? / Dạ… gỗ lim ạ."),
         cam="Anh Tư beside his boat in the reeds, catching his breath, watching the fleet sail over the stakes, then turning to the camera, calm"),
]
WHO = {"tu": "ANH TƯ", "hd": "TRẦN HƯNG ĐẠO (seen only from behind)", "cai": "THE SQUAD LEADER",
       "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "hd": "Trần Hưng Đạo", "cai": "Cai đội", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "hd": V_HD, "cai": V_CAI, "narr": V_NARR}
PREFIX = {"tu": "", "hd": "Trần Hưng Đạo: / ", "cai": "", "narr": ""}


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
POV: Cả quân thề / phải thắng… / còn bạn được lệnh thua
```

Hook dự phòng:
```
POV: Bạn đun nồi nước thơm / xin tắm trước / thì bị hỏi: ai mượn?
POV: Được lệnh thua / mà phải thua cho khéo
```

**Tiêu đề:**
```
Lời thề sông Hóa và đoàn thuyền đi thua | Bạch Đằng 1288 tập 7
```

**Mô tả và hashtag:**
```
Nồi nước thơm trong trailer là để làm gì? Hai trụ cột nhà Trần giận nhau mấy chục năm… làm lành bằng một chậu nước 🛁 Rồi Hưng Đạo vương qua sông Hóa thề: không phá xong giặc thì không về khúc sông này. Còn Anh Tư? Được giao đi thua, mà phải thua cho khéo. Đây là tập 7 của loạt Bạch Đằng 1288. Theo bạn, vì sao phải thua cho giặc đuổi? 👇
#povlichsu #POV #lichsuvietnam #xuhuong #fyp #bachdang1288 #tranhungdao #bachdang #anhtu
```

**Bình luận ghim:**
```
Tập 8 ngày mai 19h: nước rút… sáng còn là sông, trưa đã thành rừng cọc 🌊 Follow để không lỡ trận Bạch Đằng!
```

**Mẫu trả lời 60 phút đầu:**
1. (Về nồi nước thơm) "Sử chép Hưng Đạo vương và Thượng tướng Trần Quang Khải vốn không hòa thuận; ông tự tay tắm cho Quang Khải bằng nước thơm để làm lành, từ đó hai người chung lòng."
2. (Về lời thề) "Qua sông Hóa, Hưng Đạo vương thề: trận này không phá xong giặc Nguyên thì không về đến sông này nữa (Toàn thư)."
3. (Về giả thua) "Quân Nguyễn Khoái dùng thuyền nhẹ khiêu chiến rồi giả thua, nhử hạm đội Ô Mã Nhi vào sông lúc triều lên, che kín bãi cọc."

Khi đăng: bật nhãn "Nội dung do AI tạo".

## Đăng YouTube Shorts

**Tiêu đề:**
```
Lời thề sông Hóa và đoàn thuyền đi thua | Bạch Đằng 1288 tập 7 #Shorts
```

**Mô tả:**
```
Hai trụ cột nhà Trần giận nhau mấy chục năm… làm lành bằng một chậu nước 🛁 Rồi Hưng Đạo vương qua sông Hóa thề: không phá xong giặc thì không về khúc sông này. Còn Anh Tư được giao đi thua. Đây là tập 7 của loạt Bạch Đằng 1288.

Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 10 tập.

#Shorts #povlichsu #lichsuvietnam #bachdang1288 #tranhungdao #anhtu
```

**Thẻ:**
```
lời thề sông hóa, trần hưng đạo, trần quang khải, nhử địch bạch đằng, nguyễn khoái, bạch đằng 1288, kháng chiến chống nguyên, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts
```

Mục "Nội dung bị thay đổi" chọn **Có**.

## Đăng Facebook

**Caption:**
```
Cả nhà ơi, 19h tối nay có tập 7 loạt Bạch Đằng 1288 nè 🛁

Nồi nước thơm trong trailer đây rồi: hai trụ cột nhà Trần giận nhau mấy chục năm… làm lành bằng một chậu nước.

Rồi cả quân thề phải thắng… mỗi tui được giao đi thua 😂 Đúng nhận, sai cãi… mà lệnh thì tui không dám cãi.

Cả nhà đoán vì sao phải thua cho giặc đuổi? 👇

#BachDang1288 #TranHungDao #POVMotNgayODaiViet #LichSuVietNam
```

Đăng dạng **Reel**, cùng một bản với TikTok và YouTube. Bật "Thông tin về AI"."""


def main():
    base = "bd1288-tap7"
    md_name = base + "-the-thang-di-thua.md"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Cả quân thề / phải thắng… / còn bạn được lệnh thua", "end: Follow để xem / Trận Bạch Đằng →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 7: Ông thề thắng, em đi thua", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook.", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); Trần Hưng Đạo trầm, "
          "vang, chắc; dẫn chuyện giọng Bắc trầm; cai đội gắt, ngắn.", "",
          "## Mạch tập", "",
          "- **Nồi nước thơm** (clip 1–3): giải câu đố trailer \"mai trả lời câu đầu tiên\": hai trụ cột nhà Trần làm lành "
          "bằng một chậu nước. Hai ông chỉ quay từ phía sau, mặc áo, không nói.",
          "- **Lời thề sông Hóa** (clip 4–6): hàng nghìn quân qua sông; Hưng Đạo vương thề (quay từ phía sau); Anh Tư chèo đò.",
          "- **Đi thua** (clip 7–10): lệnh giả thua; đoàn thuyền nhẹ khiêu chiến rồi chạy; hạm đội Nguyên hơn trăm chiếc đuổi vào sông.",
          "- **Nước lên che bãi cọc** (clip 11–12): hạm đội lướt qua ngay trên đầu cọc mà không biết; câu chốt dẫn sang trận Bạch Đằng.",
          "- **Âm thanh:** cảnh nồi nước chỉ có sáo trúc nhẹ; từ cảnh qua sông trở đi nhạc giao hưởng trống trận dâng dần, cảnh đuổi "
          "đánh mạnh nhất, cảnh nước lên giữ một nốt căng. Nhạc luôn nằm dưới lời nói.",
          "- **Câu trending 2026** (chỉ Anh Tư, mỗi clip tối đa một câu): \"ủa rồi ai mượn\", \"chưa đủ wow\", \"tới công chuyện rồi\", "
          "\"đúng nhận, sai cãi\", \"nín\", \"dạ… gỗ lim ạ\" (chế từ \"dạ gỗ xà cừ ạ\").",
          "- Mỗi clip một người nói, lời lấp gần kín 10 giây; cảnh nào khóa bối cảnh cảnh đó. Năm trong lời thoại đã viết thành chữ.", "",
          "**Lịch sử:** Hưng Đạo vương và Thượng tướng Trần Quang Khải vốn không hòa thuận, Hưng Đạo tự tay tắm cho Quang Khải bằng "
          "nước thơm để làm lành (B, *Toàn thư*; sử không ghi đúng ngày, video chỉ nói \"trước trận Bạch Đằng\" ở nhãn, không "
          "khẳng định năm). Đầu tháng 4/1288 Hưng Đạo dẫn quân ra Bạch Đằng, qua sông Hóa thề không phá xong giặc thì không về khúc "
          "sông này (B, *Toàn thư*; lời trong video phỏng theo ý sử chép). Sáng 9/4/1288 quân Nguyễn Khoái dùng thuyền nhẹ khiêu "
          "chiến, giả thua, nhử hạm đội Ô Mã Nhi vào sông lúc triều lên (A). **Hư cấu:** Anh Tư, cai đội, mọi lời thoại ngoài lời "
          "thề. Truyền thuyết Yết Kiêu để dành, không đưa vào tập này cho gọn.", "",
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
