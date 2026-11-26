#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 5 "Dọn sạch kinh thành, phá hết cầu": mỗi clip một người nói, khóa bối cảnh theo cảnh.
Chạy: python3 _tap5.py → bd1288-tap5-don-sach-kinh-thanh.md + bd1288-tap5.plan.txt + Word
"""
import os
import sys

from _tap3 import FACE, V_TU, RULES, AUDIO, SO_RULE, noi, spoken

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("EPIC cinematic historical film on a grand scale, live-action, photorealistic, sweeping aerial, crane and "
        "drone shots, thousands of extras, volumetric light through mist and dust, rich film grain, vertical 9:16. Đại "
        "Việt, February–March 1288, the capital Thăng Long and the vast Red River delta: a great walled city with hundreds "
        "of clay-tile roofs, curved palace roofs, the wide Red River, endless rice fields, canals and wooden bridges, "
        "limestone hills on the horizon. Trần people: hair in topknots, black-lacquered teeth, brown or dark cotton "
        "tunics. Yuan army: leather lamellar armor, round helmets, many horses. No modern objects, no on-screen text, no "
        "subtitles, no legible writing, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, no blood, no gore, no dead bodies, no "
        "children in close-up. The humor is in what Anh Tư says, not in his face; everyone else stays natural and serious.")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN "
          "voice-over; nobody on screen moves their lips")
V_LINH = ("the Yuan soldier = a rough, tired male voice in his 30s speaking Vietnamese with a slight foreign accent, "
          "frustrated, not shouting")
V_CAI = "the squad leader = a clipped, gruff male voice in his 40s, Northern Vietnamese accent, short commands"
V_BA = "the old woman = a sharp, lively elderly woman's voice in her 60s, Northern Vietnamese countryside accent"

SCENES = {
    "A": dict(name="Cả kinh thành Thăng Long sơ tán, sáng sớm",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): dawn over the great walled capital of Thăng Long, "
                    "golden light breaking through cold mist over hundreds of clay-tile roofs and the curved palace roofs; "
                    "tens of thousands of people leave the city in endless quiet columns through three great wooden city "
                    "gates, with carrying poles, baskets of rice, ox carts and buffalo; on the wide Red River hundreds of "
                    "boats loaded with rice sacks drift away downstream. Down in one brick lane near the main gate, Anh Tư "
                    "walks in the crowd with a bamboo carrying pole: a big black cooking pot on one end, a rooster in a bamboo "
                    "cage on the other."),
              img=("Epic aerial at golden dawn over a great walled medieval Vietnamese capital, hundreds of clay-tile roofs "
                   "and curved palace roofs in mist, tens of thousands of people leaving in endless columns through three "
                   "great wooden gates with carrying poles, ox carts and buffalo, hundreds of rice boats on the wide river, "
                   "and in the foreground lane {FACE}, carrying a bamboo pole with a big black pot and a caged rooster, "
                   "realistic, vertical 9:16."),
              amb="the deep murmur of a huge crowd, thousands of footsteps, ox carts, a rooster clucking close by"),
    "B": dict(name="Biển lau ven sông, hoàng hôn",
              lock=("SCENE B: a sea of tall silver reeds stretching to the horizon along a wide river at golden sunset, a huge "
                    "sky with flocks of birds; Anh Tư alone has buried a big clay jar of rice and ties three reeds together "
                    "above it as a marker; millions of identical reeds sway around him."),
              img=("Epic wide shot of a sea of tall silver reeds stretching to the horizon along a wide river at golden "
                   "sunset, huge sky with flocks of birds, {FACE}, tiny in the vast field, tying three reeds together "
                   "above a freshly buried clay jar, realistic, vertical 9:16."),
              amb="wind sweeping through the reeds, birds, distant river"),
    "C": dict(name="Đại quân Nguyên tiến vào kinh thành trống",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): under a heavy grey sky the great main gate of "
                    "Thăng Long stands wide open; a vast Yuan army, thousands of cavalry and infantry in lamellar armor, "
                    "pours through it in endless columns, dust rising; inside, the whole capital is completely empty and "
                    "silent: every door open, not one person, no smoke from any of the hundreds of kitchens. Inside one house "
                    "an empty kitchen: a cold stove, overturned empty rice jars."),
              img=("Epic aerial under a heavy grey sky: a vast army of thousands of cavalry and infantry in lamellar armor "
                   "pouring through the open main gate of a great empty walled Vietnamese capital, dust rising, every street "
                   "empty and silent, no kitchen smoke anywhere, realistic, vertical 9:16."),
              amb="thousands of hooves, armor clanking, then the eerie silence of an empty city, wind through open doors"),
    "D": dict(name="Đại doanh Nguyên trong mưa tháng ba",
              lock=("SCENE D: an enormous Yuan army camp stretching to the horizon on a muddy plain in March rain under dark "
                    "clouds, thousands of sagging tents, smoke from weak fires, endless rows of upside-down empty rice "
                    "baskets, tired hungry soldiers huddled in groups, many men lying sick under blankets (alive, coughing); "
                    "no faces close enough to see."),
              img=("Epic aerial of an enormous army camp stretching to the horizon on a muddy plain in March rain, thousands "
                   "of sagging tents, thin smoke from weak fires, rows of empty upside-down rice baskets, dark storm clouds, "
                   "realistic, vertical 9:16."),
              amb="heavy rain, coughing, low murmurs, horses, distant thunder"),
    "E": dict(name="Phá cầu khắp vùng đồng bằng",
              lock=("SCENE E (keep IDENTICAL in every clip of this scene): a big old wooden bridge over a wide canal between "
                    "vast rice fields, clear morning light; the bridge is half chopped away; all across the delta behind it, "
                    "teams of Trần soldiers chop down other bridges and fell huge trees across the roads, several bridges "
                    "collapsing into the water in the distance, dust and splashes everywhere. On the near bank a bamboo grove; "
                    "on the far bank a village gate. The squad leader in a dark tunic with a sword stands on the near bank. Anh "
                    "Tư stands on the near bank with an axe. An old woman with a basket of green vegetables on a carrying "
                    "pole waits on the far bank."),
              img=("Epic shot of a big old wooden bridge half chopped away over a wide canal between vast rice fields, "
                   "morning light, across the delta behind it teams of soldiers felling huge trees and several distant "
                   "bridges collapsing into the water, {FACE}, on the near bank with an axe, an old woman with a basket of "
                   "green vegetables on the far bank, realistic, vertical 9:16."),
              amb="axe chops, trees crashing, timber splashing into water, shouted commands far away, birds"),
    "F": dict(name="Toàn cảnh đồng bằng đến sông Bạch Đằng, hoàng hôn",
              lock=("SCENE F (keep IDENTICAL in every clip of this scene): a high hilltop at a blazing sunset above the whole "
                    "delta: below, dozens of broken bridges and felled trees blocking every road and canal as far as the eye "
                    "can see, thin smoke columns rising; far away the one wide Bạch Đằng river winds between hundreds of "
                    "limestone karsts to the sea, burning gold. Anh Tư stands alone on the hilltop with his axe."),
              img=("Epic aerial at a blazing sunset from a high hilltop over a vast delta, dozens of broken bridges and felled "
                   "trees blocking every road and canal, thin smoke columns, far away one wide river winding between hundreds "
                   "of limestone karsts to the sea glowing gold, {FACE}, standing alone on the hilltop with an axe, "
                   "realistic, vertical 9:16."),
              amb="strong evening wind, distant drums, birds"),
}

CLIPS = [
    dict(scene="A", who="narr", label="Thăng Long · tháng 2/1288",
         line=(0.8, 9.2, "Đầu năm 1288. / Giặc tiến về Thăng Long. / Lệnh truyền xuống: / bỏ trống kinh thành."),
         cam="huge sweeping drone shot from high above the palace roofs down over the city gates and the endless columns of people leaving, ending on the rice boats on the river; no faces close enough to see"),
    dict(scene="A", who="tu",
         line=(0.4, 9.2, "Nhà em có mỗi / cái nồi với con gà… / Giờ con gà / cũng phải đi sơ tán, / mà nó kêu to hơn em."),
         cam="tracking shot walking with Anh Tư under his carrying pole in the huge crowd at the great gate; the rooster in the cage clucks loudly; he glances at it and sighs"),
    dict(scene="B", who="tu", chuyen="fade:0.5",
         line=(0.4, 9.2, "Em chôn chum gạo / giữa bãi lau, / đánh dấu bằng ba cây sậy… / mà bãi này / có cả vạn cây sậy."),
         cam="Anh Tư finishes tying three reeds and looks around; the camera rises into a vast aerial revealing millions of identical reeds to the horizon; Anh Tư becomes a tiny dot"),
    dict(scene="C", who="narr", chuyen="fadeblack:0.6", label="Mấy hôm sau",
         line=(0.8, 9.2, "Quân Nguyên tràn vào / kinh thành. / Nhà cửa còn nguyên, / cửa mở toang… / mà không còn một hạt gạo."),
         cam="epic low angle at the great gate as endless columns of cavalry thunder past in slow motion, then a rising aerial over the silent empty capital; no faces close enough to see"),
    dict(scene="C", who="linh",
         line=(0.4, 9.2, "Kho trống, bếp trống… / lục khắp kinh thành / từ sáng đến giờ, / không còn lấy / một cái nồi!"),
         cam="inside the empty kitchen, a Yuan soldier in lamellar armor lifts the lid of an empty rice jar, turns to the camera and speaks; nobody else in frame"),
    dict(scene="D", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Lương ở Vân Đồn đã mất. / Giặc đói, giặc ốm, / bị đánh khắp nơi. / Tháng ba, Thoát Hoan / quyết định rút quân."),
         cam="slow epic aerial over the enormous rain-soaked camp to the horizon, lightning in the clouds; no faces close enough to see"),
    dict(scene="E", who="cai", chuyen="fadeblack:0.6", label="Tháng 3/1288",
         line=(0.4, 9.2, "Phá hết cầu, / chặt cây chắn đường. / Chừa đúng một lối… / để giặc tự đi / vào chỗ của nó."),
         cam="the squad leader on the near bank faces the camera and points at the bridge while behind him, across the delta, distant bridges collapse into the water; Anh Tư is out of frame"),
    dict(scene="E", who="tu",
         line=(0.4, 9.2, "Ông em xây cái cầu này / mất ba năm… / Em phá có một buổi sáng. / Ông mà biết / thì em ăn đòn."),
         cam="Anh Tư alone in frame on the near bank, axe in hand, looking at the half-chopped bridge, then at the camera"),
    dict(scene="E", who="ba",
         line=(0.4, 9.2, "Cầu đâu rồi cháu? / Bà sang chợ bên kia / bán mớ rau muống… / giờ bà đi đường nào / hả cháu?"),
         cam="the old woman on the far bank with her basket of vegetables, calling across the water; nobody else's face in frame"),
    dict(scene="E", who="tu",
         line=(0.4, 9.2, "Bà đi đường vòng… / ba hôm thôi ạ. / Đến nơi thì rau tươi / thành rau khô, / bà bán được giá hơn."),
         cam="Anh Tư alone in frame on the near bank, answering politely across the canal, a faint smile"),
    dict(scene="F", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Mọi ngả đều bị chặn. / Đường về của / thủy quân Nguyên / chỉ còn một: / sông Bạch Đằng."),
         cam="grand sweeping aerial from the hilltop out over the broken bridges and felled trees all the way to the golden Bạch Đằng river and the karsts at the sea; Anh Tư a small figure from behind on the hill; no faces visible"),
    dict(scene="F", who="tu",
         line=(0.4, 9.2, "Phá hết đường, / chừa đúng đường / nó phải đi. / Mà vừa hết phá cầu… / họ lại bảo em / đi chặt que."),
         cam="Anh Tư on the hilltop turns from the river to the camera, axe on his shoulder, calm, a faint smile"),
]
WHO = {"tu": "ANH TƯ", "linh": "THE YUAN SOLDIER", "cai": "THE SQUAD LEADER", "ba": "THE OLD WOMAN",
       "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "linh": "Lính Nguyên", "cai": "Cai đội", "ba": "Bà đi chợ", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "linh": V_LINH, "cai": V_CAI, "ba": V_BA, "narr": V_NARR}
PREFIX = {"tu": "", "narr": "", "linh": "", "cai": "", "ba": ""}


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
POV: Bạn phải dọn sạch / cả kinh thành / trước khi giặc đến
```

Hook dự phòng:
```
POV: Giặc vào kinh thành / mà không còn / một cái nồi
POV: Bạn được giao / phá cầu ông nội xây
```

**Tiêu đề:**
```
Giặc vào Thăng Long mà không còn một hạt gạo | Bạch Đằng 1288 tập 5
```

**Mô tả và hashtag:**
```
Cả kinh thành dọn đi hết, đến con gà cũng phải đi sơ tán 🐓 Giặc vào Thăng Long: nhà cửa còn nguyên mà không còn một hạt gạo. Mất lương ở Vân Đồn, đói, ốm, bị đánh khắp nơi, quân Nguyên phải rút… còn quân Trần thì phá hết cầu, chừa đúng một con đường. Đây là tập 5 của loạt Bạch Đằng 1288. Theo bạn, con đường được chừa lại dẫn đi đâu? 👇
#povlichsu #POV #lichsuvietnam #xuhuong #fyp #bachdang1288 #vuonkhongnhatrong #anhtu
```

**Bình luận ghim:**
```
Tập 6 ngày mai 19h: Anh Tư được sai "đi chặt que"… mà que to ôm không hết 🪵 Follow để không lỡ tập nào!
```

**Mẫu trả lời 60 phút đầu:**
1. (Về vườn không nhà trống) "Quân dân nhà Trần mang hết lương thực đi, để lại kinh thành trống. Giặc vào được mà không có gì ăn."
2. (Về rút quân) "Mất đoàn thuyền lương ở Vân Đồn, lại đói, ốm, bị đánh khắp nơi, khoảng tháng 3/1288 Thoát Hoan quyết định rút: thủy quân theo sông Bạch Đằng, bộ binh theo Lạng Sơn."
3. (Về phá cầu) "Quân Trần chặn các ngả, phá cầu, để thủy quân Nguyên chỉ còn đường về qua sông Bạch Đằng."

Khi đăng: bật nhãn "Nội dung do AI tạo".

## Đăng YouTube Shorts

**Tiêu đề:**
```
Giặc vào Thăng Long mà không còn một hạt gạo | Bạch Đằng 1288 tập 5 #Shorts
```

**Mô tả:**
```
Cả kinh thành dọn đi hết, đến con gà cũng phải đi sơ tán 🐓 Giặc vào Thăng Long: nhà cửa còn nguyên mà không còn một hạt gạo. Quân Nguyên phải rút… còn quân Trần thì phá hết cầu, chừa đúng một con đường. Đây là tập 5 của loạt Bạch Đằng 1288.

Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 10 tập.

#Shorts #povlichsu #lichsuvietnam #bachdang1288 #anhtu
```

**Thẻ:**
```
vườn không nhà trống, thăng long 1288, thoát hoan rút quân, bạch đằng 1288, kháng chiến chống nguyên, nhà trần, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts
```

Mục "Nội dung bị thay đổi" chọn **Có**.

## Đăng Facebook

**Caption:**
```
Cả nhà ơi, 19h tối nay có tập 5 loạt Bạch Đằng 1288 nè 🐓

Cả kinh thành dọn đi hết, đến con gà cũng phải đi sơ tán. Giặc vào Thăng Long: nhà cửa còn nguyên mà không còn một hạt gạo.

Còn tui thì được giao phá cái cầu ông nội xây ba năm… phá có một buổi sáng 😂

Cả nhà đoán con đường được chừa lại dẫn đi đâu? 👇

#BachDang1288 #VuonKhongNhaTrong #POVMotNgayODaiViet #LichSuVietNam
```

Đăng dạng **Reel**, cùng một bản với TikTok và YouTube. Bật "Thông tin về AI"."""


def main():
    base = "bd1288-tap5"
    md_name = base + "-don-sach-kinh-thanh.md"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Bạn phải dọn sạch / cả kinh thành / trước khi giặc đến", "end: Follow để xem / Chặt que →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 5: Dọn sạch kinh thành, phá hết cầu", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook.", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); dẫn chuyện giọng Bắc "
          "trầm; lính Nguyên, cai đội, bà đi chợ mỗi người một giọng riêng.", "",
          "## Mạch tập", "",
          "- **Bỏ trống kinh thành** (clip 1–3): lệnh bỏ trống Thăng Long, Anh Tư gánh nồi với con gà đi sơ tán, chôn chum gạo "
          "giữa bãi lau (gài cho tập 10: đào cả cánh đồng mới thấy).",
          "- **Giặc vào thành trống** (clip 4–6): kinh thành còn nguyên mà không còn hạt gạo; lính Nguyên lục khắp không thấy "
          "một cái nồi; mất lương Vân Đồn, đói, ốm, Thoát Hoan quyết định rút.",
          "- **Phá cầu, chừa một lối** (clip 7–12): cai đội ra lệnh, Anh Tư phá cầu ông nội xây, bà đi chợ hỏi đường, mọi ngả bị "
          "chặn chỉ còn sông Bạch Đằng, câu chốt dẫn sang tập 6 \"chặt que\".",
          "- **Khung cảnh hoành tráng:** quay từ trên cao toàn kinh thành với hàng vạn người sơ tán, đại quân Nguyên hàng nghìn kỵ binh tràn qua cổng thành trống, đại doanh trong mưa kéo tới chân trời, cả vùng đồng bằng phá cầu chặt cây, toàn cảnh tới sông Bạch Đằng lúc hoàng hôn.",
          "- Mỗi clip một người nói, lời lấp gần kín 10 giây; cảnh nào khóa bối cảnh cảnh đó. Năm trong lời thoại đã viết thành "
          "chữ để Muse đọc đúng. Đổi cảnh nhảy thời gian thì tối dần 0,6 giây.", "",
          "**Lịch sử (mức A):** tháng 2/1288 quân Nguyên vào Thăng Long nhưng kinh thành đã bỏ trống, lương thực mang đi hết; mất "
          "đoàn thuyền lương ở Vân Đồn, quân Nguyên thiếu lương, dịch bệnh, bị đánh tiêu hao; khoảng tháng 3/1288 Thoát Hoan quyết "
          "định rút, thủy quân theo sông Bạch Đằng, bộ binh theo Lạng Sơn; quân Trần phá cầu, chặn đường, buộc thủy quân đi qua "
          "Bạch Đằng. **Hư cấu:** Anh Tư, cai đội, lính Nguyên, bà đi chợ và mọi lời thoại. Không nêu quân số; không nhắc chuyện "
          "quân Nguyên đào lăng (chuyện nhạy cảm, không hợp giọng vui của tập).", "",
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
