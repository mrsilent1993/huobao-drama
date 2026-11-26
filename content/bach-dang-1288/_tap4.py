#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 4 "Trận Vân Đồn": khoảng 70% thời lượng là mai phục và thủy chiến, mỗi clip một người nói,
khóa bối cảnh theo cảnh. Chạy: python3 _tap4.py → bd1288-tap4-van-don.md + bd1288-tap4.plan.txt + Word
"""
import os
import sys

from _tap3 import FACE, V_TU, V_KD, RULES, AUDIO, SO_RULE, noi, spoken

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("Epic cinematic naval battle film, live-action, photorealistic, dramatic natural light, volumetric mist and smoke, "
        "film grain, vertical 9:16. Đại Việt, January 1288, Vân Đồn (today's Bái Tử Long bay): hundreds of towering "
        "limestone karst islands, narrow channels with fast green water, caves and hidden coves. Trần sailors: hair in "
        "topknots, black-lacquered teeth, brown cotton tunics, bows, crossbows, oars and grappling hooks, in many small "
        "light flat-bottomed war boats. Yuan supply convoy: dozens of big, heavy, deep-hulled wooden cargo junks with "
        "matting sails, riding low in the water, decks piled high with rice sacks; their crews are mostly porters in grey "
        "tunics. No modern objects, no on-screen text, no subtitles, no legible writing, ABSOLUTELY NO FLAGS OR BANNERS OF "
        "ANY KIND, no blood, no gore, no dead or drowning bodies, nobody killed on screen, no children. The humor is in "
        "what Anh Tư says, not in his face; the general and the narrator stay serious.")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN "
          "voice-over; nobody on screen moves their lips")

SCENES = {
    "A": dict(name="Vịnh Vân Đồn từ trên cao, rạng sáng",
              lock=("SCENE A: high aerial over Vân Đồn bay at dawn, hundreds of limestone islands rising from silver mist, "
                    "narrow winding channels between them; far out, a long slow line of heavy Yuan cargo junks riding low in "
                    "the water enters the bay from the open sea."),
              img=("Epic high aerial at dawn over a bay with hundreds of limestone karst islands rising from silver mist, "
                   "narrow winding channels, far out a long slow line of heavy wooden cargo junks with matting sails riding "
                   "low in the water entering the bay, realistic, vertical 9:16."),
              amb="wind, distant gulls, deep drums very far away"),
    "B": dict(name="Vụng kín mai phục",
              lock=("SCENE B (keep IDENTICAL in every clip of this scene): a hidden cove between sheer karst walls with dark "
                    "caves, cool morning shadow, still green water; dozens of light Trần war boats packed side by side, every "
                    "boat camouflaged with green branches and leaves, soldiers crouching silent with bows and oars, no fire "
                    "anywhere. Trần Khánh Dư in a dark brown robe with a black sash stands on a flat rock at the mouth of the "
                    "cove, seen ONLY from behind. Anh Tư sits in the nearest boat with leafy branches tied on his back and head."),
              img=("Cinematic shot of a hidden cove between sheer limestone walls with dark caves, cool morning shadow, still "
                   "green water, dozens of light wooden war boats camouflaged with green branches, soldiers crouching silent "
                   "with bows, a general in a dark brown robe with a black sash seen only from behind on a rock at the cove "
                   "mouth, {FACE}, sitting in the nearest boat with leafy branches tied on his back and head, realistic, "
                   "vertical 9:16."),
              amb="dripping water in the caves, soft waves, total silence of men"),
    "C": dict(name="Luồng hẹp giữa núi đá, đoàn thuyền lương lọt vào",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): a narrow channel between two towering karst walls, "
                    "late morning sun in shafts through the mist, fast green current; the long line of heavy Yuan cargo junks "
                    "crawls slowly through it, decks piled with rice sacks. High on a rock ledge on the left, Trần Khánh Dư in "
                    "a dark brown robe with a black sash, seen ONLY from behind, with a soldier beside him at a big war drum."),
              img=("Epic shot of a narrow channel between two towering limestone walls, sun shafts through mist, a long line "
                   "of heavy wooden cargo junks piled with rice sacks crawling through the fast green current, high on a "
                   "rock ledge on the left a general in a dark brown robe seen only from behind beside a soldier with a big "
                   "war drum, realistic, vertical 9:16."),
              amb="creaking hulls, slow oars, current, wind in the cliffs"),
    "D": dict(name="Thủy chiến trong luồng",
              lock=("SCENE D (keep IDENTICAL in every clip of this scene): the SAME narrow channel between towering karst walls, "
                    "now a great naval ambush: hundreds of light Trần war boats burst out of every cove and cave and lock both "
                    "ends of the channel; volleys of fire arrows arc onto the matting sails, sails burning, thick smoke rolling "
                    "up the cliffs; grappling hooks fly, Trần sailors climb aboard the big junks; Yuan porters in grey tunics "
                    "flee into small boats; rice sacks everywhere. No blood, no bodies, nobody killed on screen."),
              img=("Epic naval ambush in a narrow channel between towering limestone walls, hundreds of small light war boats "
                   "surging out from coves toward a long line of heavy cargo junks, fire arrows arcing onto burning matting "
                   "sails, thick smoke rolling up the cliffs, grappling hooks flying, {FACE}, rowing hard in a small boat in "
                   "the foreground, realistic, vertical 9:16."),
              amb="war drums, roaring fire, crackling sails, splashing oars, battle shouts in the distance"),
    "E": dict(name="Cửa vịnh, Trương Văn Hổ bỏ chạy",
              lock=("SCENE E: the mouth of the bay toward the open sea, smoke behind; a big Yuan junk dumps rice sacks over its "
                    "side into the sea while a small fast boat with a dark sail flees out to the open sea; Trần boats in pursuit "
                    "far behind. No faces close enough to see."),
              img=("Epic wide shot at the mouth of a karst bay toward the open sea, smoke rising behind, a big wooden junk "
                   "dumping rice sacks over its side into the sea, a small fast boat with a dark sail fleeing to the horizon, "
                   "realistic, vertical 9:16."),
              amb="wind, waves, sacks splashing, distant drums"),
    "F": dict(name="Bãi biển sau trận, hoàng hôn",
              lock=("SCENE F (keep IDENTICAL in every clip of this scene): a grey beach at sunset after the battle, far out "
                    "the dark hulks of captured junks with thin smoke, dozens of waterlogged rice sacks washing in on the "
                    "waves, Trần soldiers carrying sacks up the beach in a long line. Anh Tư stands in the surf."),
              img=("Cinematic shot of a grey beach at sunset, far out dark hulks of captured junks with thin smoke, dozens of "
                   "waterlogged rice sacks washing ashore, soldiers carrying sacks up the beach in a long line, {FACE}, "
                   "standing in the surf, realistic, vertical 9:16."),
              amb="waves, evening wind, distant tired voices"),
}

# 12 clip: 1 mở, 9 clip mai phục và thủy chiến (2-10, khoảng 75%), 2 clip kết.
CLIPS = [
    dict(scene="A", who="narr", label="Vân Đồn · đầu năm 1288",
         line=(0.8, 9.2, "Đầu năm 1288. / Hạm đội Nguyên đi trước, / bỏ lại sau lưng / cả đoàn thuyền lương."),
         cam="slow epic aerial push over the islands toward the distant convoy; no faces visible"),
    dict(scene="B", who="kd",
         line=(0.4, 9.2, "Giấu thuyền vào khe đá, / phủ cành lên. / Không ai được đốt lửa, / không ai được lên tiếng."),
         cam="from behind Trần Khánh Dư on the rock, looking over the silent camouflaged boats; no other face close enough to see his mouth"),
    dict(scene="B", who="tu",
         line=(0.4, 9.2, "Cả đạo quân phủ lá / ngồi im từ sáng… / con cua nó bò qua, / tưởng em là hòn đá."),
         cam="close-up of Anh Tư alone in frame under his leafy branches, whispering to the camera; a small crab walks across the gunwale past his hand"),
    dict(scene="C", who="narr",
         line=(0.8, 9.2, "Thuyền chở nặng, / đáy sâu, đi chậm như rùa… / từng chiếc, từng chiếc / lọt vào giữa luồng hẹp."),
         cam="epic low angle from the water as the heavy junks crawl past between the towering walls, then a slow tilt up the cliff; no faces visible"),
    dict(scene="C", who="kd",
         line=(0.4, 9.2, "Đầu đoàn đã qua eo đá. / Chặn đầu! Chặn đuôi! / Không để chiếc nào / quay ra. Toàn quân… đánh!"),
         cam="from behind Trần Khánh Dư on the ledge, he raises his arm and brings it down; the drummer strikes the big drum; no faces visible"),
    dict(scene="D", who="narr", chuyen="fadewhite:0.3",
         line=(0.8, 9.2, "Hàng trăm thuyền nhẹ / từ khắp các khe đảo / lao ra như tên bắn, / khóa chặt hai đầu luồng."),
         cam="huge sweeping aerial: boats pour out of every cove and cave and close both ends of the channel around the convoy; no faces visible"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Chèo nhanh lên các bác! / Thuyền họ to như đình… / mà quay đầu chậm / như con trâu già."),
         cam="tracking shot alongside Anh Tư rowing hard in a small boat among the charging fleet, he speaks breathless but not shouting; no other speaking face"),
    dict(scene="D", who="narr",
         line=(0.8, 9.2, "Tên lửa trút xuống buồm. / Móc sắt quăng sang mạn. / Quân Trần áp sát, / nhảy lên / từng thuyền lương."),
         cam="slow-motion: a volley of fire arrows lights the sails, grappling hooks bite the hulls, sailors climb aboard through the smoke; seen from a distance, no faces"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Lính họ chạy hết, / chỉ còn gạo / ở lại tiếp em. / Gạo thì không chạy… / mà nặng hơn lính."),
         cam="Anh Tư alone on the deck of a captured junk among piles of rice sacks, smoke behind, he tries to lift one sack and sighs; enemy porters flee into small boats far behind"),
    dict(scene="E", who="narr",
         line=(0.8, 9.2, "Tướng Trương Văn Hổ / đổ lương xuống biển, / bỏ cả đoàn thuyền, / chạy một mạch về Hải Nam."),
         cam="wide shot: sacks splash into the sea from the big junk as the small dark-sailed boat races to the horizon; no faces visible"),
    dict(scene="F", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Quân Trần thu được / rất nhiều lương / và khí giới. / Ở Thăng Long, quân Nguyên / chờ mãi… không thấy gạo."),
         cam="slow aerial over the sunset beach and the long line of soldiers carrying sacks; Anh Tư seen small from behind in the surf; no faces visible"),
    dict(scene="F", who="tu",
         line=(0.4, 9.2, "Năm nay biển… / trả lương bằng gạo. / Bên kia đang chờ cơm… / mà cơm đang trên lưng em."),
         cam="Anh Tư in the surf hoists a wet rice sack onto his shoulder, turns to the camera, calm, a faint smile"),
]
WHO = {"tu": "ANH TƯ", "kd": "TRẦN KHÁNH DƯ (seen only from behind)",
       "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "kd": "Trần Khánh Dư", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "kd": V_KD, "narr": V_NARR}
PREFIX = {"kd": "Trần Khánh Dư: / ", "tu": "", "narr": ""}
BATTLE = {"B", "C", "D", "E"}


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
POV: Bạn mai phục / cả đoàn thuyền gạo / của giặc
```

Hook dự phòng:
```
POV: Ba hôm sau / ông tướng xin khất / đánh thật
POV: Năm nay biển / trả lương bằng gạo
```

**Tiêu đề:**
```
Trận Vân Đồn: mai phục cả đoàn thuyền lương của giặc | Bạch Đằng 1288 tập 4
```

**Mô tả và hashtag:**
```
Ba hôm trước ông Khánh Dư xin khất… hôm nay ông trả nợ bằng cả một trận thủy chiến 🔥 Cả đạo quân phủ lá ngồi im trong khe đá, chờ đoàn thuyền lương nặng trĩu lọt vào luồng hẹp, rồi chặn đầu, chặn đuôi, đánh. Quân Nguyên ở Thăng Long chờ mãi không thấy gạo. Đây là tập 4 của loạt Bạch Đằng 1288. Theo bạn, mất lương rồi quân Nguyên sẽ làm gì? 👇
#povlichsu #POV #lichsuvietnam #xuhuong #fyp #bachdang1288 #vandon #trankhanhdu #anhtu
```

**Bình luận ghim:**
```
Tập 5 ngày mai 19h: giặc vào được Thăng Long… mà cả kinh thành không còn một nồi cơm 🍚 Follow để không lỡ tập nào!
```

**Mẫu trả lời 60 phút đầu:**
1. (Về số thuyền) "Sử chép đoàn lương của Trương Văn Hổ có khoảng 70 thuyền (có sách chép nhiều hơn), chở hàng chục vạn thạch lương."
2. (Về Khánh Dư) "Mấy hôm trước ông để lọt hạm đội Ô Mã Nhi, bị Thượng hoàng sai bắt về hỏi tội, ông xin khất để lập công. Trận này là công đó, nên được tha."
3. (Về ý nghĩa) "Mất lương ở Vân Đồn, quân Nguyên ở Thăng Long đói, ít lâu sau phải rút, mở đường cho trận Bạch Đằng."

Khi đăng: bật nhãn "Nội dung do AI tạo".

## Đăng YouTube Shorts

**Tiêu đề:**
```
Trận Vân Đồn 1288: mai phục cả đoàn thuyền lương | Bạch Đằng 1288 tập 4 #Shorts
```

**Mô tả:**
```
Ba hôm trước ông Khánh Dư xin khất… hôm nay ông trả nợ bằng cả một trận thủy chiến 🔥 Cả đạo quân phủ lá ngồi im trong khe đá, chờ đoàn thuyền lương nặng trĩu lọt vào luồng hẹp, rồi chặn đầu, chặn đuôi, đánh. Đây là tập 4 của loạt Bạch Đằng 1288.

Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 10 tập.

#Shorts #povlichsu #lichsuvietnam #bachdang1288 #vandon #trankhanhdu #anhtu
```

**Thẻ:**
```
trận vân đồn, vân đồn 1288, trần khánh dư, trương văn hổ, thuyền lương, bạch đằng 1288, kháng chiến chống nguyên, thủy chiến, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts
```

Mục "Nội dung bị thay đổi" chọn **Có**.

## Đăng Facebook

**Caption:**
```
Cả nhà ơi, 19h tối nay có tập 4 loạt Bạch Đằng 1288 nè 🔥

Ba hôm trước ông Khánh Dư xin khất… hôm nay ông trả nợ bằng cả một trận thủy chiến. Cả đạo quân phủ lá ngồi im trong khe đá, chờ đoàn thuyền lương của giặc lọt vào luồng hẹp, rồi chặn đầu, chặn đuôi, đánh.

Năm nay biển trả lương bằng gạo 😂

Cả nhà đoán mất lương rồi quân Nguyên ở Thăng Long sẽ làm gì? 👇

#BachDang1288 #VanDon #TranKhanhDu #POVMotNgayODaiViet #LichSuVietNam
```

Đăng dạng **Reel**, cùng một bản với TikTok và YouTube. Bật "Thông tin về AI"."""


def main():
    base = "bd1288-tap4"
    md_name = base + "-van-don.md"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Bạn mai phục / cả đoàn thuyền gạo / của giặc", "end: Follow để xem / Kinh thành không một nồi cơm →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    battle = sum(1 for c in CLIPS if c["scene"] in BATTLE)
    md = ["# Bạch Đằng 1288, tập 4: Trận Vân Đồn", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          f"chung TikTok, YouTube, Facebook · **{battle}/{n} clip ({round(100 * battle / n)}%) là mai phục và thủy chiến.**", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); Trần Khánh Dư trầm, "
          "chắc; dẫn chuyện giọng Bắc trầm.", "",
          "## Cách dựng", "",
          "- **Mở 1 clip** (hạm đội đi trước, đoàn lương bị bỏ lại) · **mai phục 4 clip** (giấu thuyền, phủ lá, đoàn lương lọt "
          "luồng, lệnh đánh) · **thủy chiến 5 clip** (hàng trăm thuyền lao ra khóa hai đầu, Anh Tư chèo, tên lửa và móc sắt, "
          "lên thuyền lương, Trương Văn Hổ bỏ chạy) · **kết 2 clip** (thu lương, Thăng Long chờ gạo, câu chốt).",
          "- Mỗi clip một người nói, lời lấp gần kín 10 giây; cảnh nào khóa bối cảnh cảnh đó (đoạn `SCENE …` y nguyên, chung "
          "một ảnh khung đầu). Năm trong lời thoại đã viết thành chữ để Muse đọc đúng.",
          "- Lúc phát lệnh đánh (clip 5 → 6) chuyển cảnh **lóe trắng 0,3 giây** cho mạnh; các chỗ khác hòa hình 0,3 giây.",
          "- **Hoành tráng mà an toàn:** lửa cháy buồm, khói, móc sắt, nhảy lên thuyền; **không máu, không xác, không ai chết "
          "trên màn hình**, lính tải lương bỏ chạy sang thuyền nhỏ.", "",
          "## Lịch sử: em đã soát lại bản tóm tắt anh gửi", "",
          "- **Đúng, dùng trong video:** Khánh Dư để lọt hạm đội Ô Mã Nhi, bị bắt về hỏi tội, xin khất vài ba ngày để lập công "
          "(B, *Toàn thư*); hạm đội đi trước, đoàn thuyền lương Trương Văn Hổ đi sau; quân Trần phục kích đánh tan đoàn lương ở "
          "vùng biển Vân Đồn, thu được nhiều lương thực, khí giới; Văn Hổ đổ lương xuống biển, chạy về Quỳnh Châu (Hải Nam) (A, "
          "*Toàn thư* và *Nguyên sử* cùng chép); Khánh Dư được tha tội (B); mất lương, quân Nguyên ở Thăng Long đói, ít lâu sau "
          "phải rút (A).",
          "- **Sửa:** Thượng hoàng năm 1288 là **Trần Thánh Tông**, không phải Trần Nhân Tông (Nhân Tông là vua đang trị vì). "
          "Khánh Dư từng bị cách chức vì **chuyện riêng với công chúa Thiên Thụy**, không phải tham nhũng, và được **vua Nhân Tông** "
          "phục chức năm 1282; chuyện bán than kênh đã làm (video \"Ông tướng bán than\"), nên tập này không nhắc.",
          "- **Không nêu con số trong lời thoại:** 70 thuyền, 17 vạn thạch (có sách chép 70 vạn), \"hơn 10.000 tấn\", \"30 vạn "
          "quân\" vì các nguồn lệch nhau; chỉ để trong mẫu trả lời bình luận, có chữ \"sử chép\". Tháng rút quân: quyết định rút "
          "khoảng tháng 3, rút đầu tháng 4/1288, nên video nói \"ít lâu sau\".",
          "- **Phần dựng lại:** địa hình luồng lạch, phủ cành, cấm đốt lửa, khóa đầu khóa đuôi, tên lửa, móc sắt là cách dựng "
          "cho sinh động theo các bài nghiên cứu phổ thông, không phải chi tiết sử chép từng chữ. Lời Khánh Dư là hư cấu theo ý trận đánh.", "",
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
