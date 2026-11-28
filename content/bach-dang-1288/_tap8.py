#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 8 "Sông thành rừng": trận Bạch Đằng 9/4/1288, triều rút, thuyền giặc mắc cọc.
Mỗi clip một người nói, lời tiếng Việt đặt đầu prompt, khóa bối cảnh theo cảnh.
Chạy: python3 _tap8.py → bd1288-tap8-song-thanh-rung.md + bd1288-tap8.plan.txt + Word
"""
import os
import sys

from _tap3 import FACE, V_TU, SO_RULE, noi, spoken
from _gioi_thieu import STAKE
from series import loi_muse, tieng_viet

HERE = os.path.dirname(os.path.abspath(__file__))

BASE = ("Epic cinematic historical naval battle film, live-action, photorealistic, sweeping aerial and crane shots, "
        "thousands of extras, vertical 9:16. Vietnam, Trần dynasty, 9 April 1288, the Bạch Đằng river between towering "
        "limestone karsts: Trần soldiers with topknots, black-lacquered teeth, brown cotton tunics, small light war boats; "
        "Yuan fleet of big wooden war junks with matting sails, soldiers in lamellar armor. Trần kings and Trần Hưng Đạo "
        "seen ONLY from far away or from behind. No text, no subtitles, NO FLAGS OR BANNERS, no blood, no gore, no dead or "
        "drowning bodies, nobody killed on screen, no children.")
AUDIO = "Audio: {amb}; any music stays far UNDER the voice, so every Vietnamese word is perfectly clear."
EPIC = ("an original epic orchestral score with thundering war drums, low male choir, low strings, horns and a bamboo "
        "flute motif")
V_NARR = ("a calm, deep, slow male baritone with a Northern Vietnamese accent, documentary style, OFF-SCREEN voice-over; "
          "nobody on screen moves their lips")
V_CAI = "a clipped, gruff male voice in his 40s, Northern Vietnamese accent, short commands, low and tense"
V_QUAN = ("a harsh, panicked male voice in his 40s speaking Vietnamese with a slight foreign accent, shouting orders "
          "but every word clear")

SCENES = {
    "A": dict(name="Bãi lau mai phục, rạng sáng",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): dawn on the Bạch Đằng riverbank, tall reeds and "
                    "mangroves, mist on the water, towering karsts; on the full high tide in the distance the great Yuan "
                    "fleet sits at anchor, hundreds of sails. Hidden in the reeds: Trần soldiers lying low with bows and "
                    "spears. The squad leader in a dark tunic with a sword crouches at the front. Anh Tư crouches beside a "
                    "notched bamboo measuring pole stuck in the mud at the water's edge."),
              img=("Cinematic shot at dawn from tall reeds on a riverbank, mist, towering limestone karsts, the great "
                   "wooden fleet with hundreds of sails anchored on the full tide in the distance, soldiers hidden in the "
                   "reeds with bows, {FACE}, crouching beside a notched bamboo measuring pole at the water's edge, "
                   "realistic, vertical 9:16."),
              amb="soft lapping water, birds waking, total silence of hidden men, a very low drum far away"),
    "B": dict(name="Nước rút, rừng cọc nhô lên",
              lock=(STAKE + " SCENE B (keep IDENTICAL in every clip of this scene): mid-morning on the Bạch Đằng river, the "
                    "tide visibly draining; row after row of giant pointed ironwood stake tips rise out of the falling "
                    "water across the whole river, like a forest growing out of the river; the big Yuan junks among them "
                    "begin to lurch and tilt. Anh Tư stands on the bank by his measuring pole."),
              img=("Epic aerial at mid-morning over a wide river between limestone karsts, the tide draining, rows of giant "
                   "pointed wooden stake tips rising out of the water across the whole river like a forest, big wooden "
                   "junks beginning to tilt among them, {FACE}, standing on the bank by a bamboo measuring pole, "
                   "realistic, vertical 9:16."),
              amb=f"draining water, creaking hulls, gulls, {EPIC} building slowly"),
    "C": dict(name="Quân Trần ba mặt đánh vào",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): the great battle on the Bạch Đằng river at late "
                    "morning: from upstream and from both banks hundreds of small light Trần war boats charge in at full "
                    "speed, oars flashing; Trần infantry pour out of the reeds and mangroves on both banks; volleys of "
                    "arrows arc over the water; on a high hill far away a dark-robed general stands by a giant war drum, "
                    "seen only from behind; the big Yuan junks stuck on the stakes cannot move. Smoke drifts across the karsts."),
              img=("Epic aerial of a great naval battle on a wide river between limestone karsts, hundreds of small light war "
                   "boats charging from upstream and both banks, infantry pouring out of the mangroves, volleys of arrows, "
                   "big wooden junks stuck among giant stakes, smoke drifting, a general by a giant war drum on a far "
                   "hill seen from behind, {FACE}, rowing hard in a small boat in the foreground, realistic, vertical 9:16."),
              amb=f"thundering war drums, hundreds of oars, battle cries, cracking timber, {EPIC} at full power"),
    "D": dict(name="Giữa bãi cọc, thuyền giặc mắc kẹt",
              lock=(STAKE + " SCENE D (keep IDENTICAL in every clip of this scene): in the middle of the stake field at low "
                    "tide: a huge Yuan war junk is impaled on giant ironwood stakes, its hull cracked, its mast leaning, its "
                    "matting sail torn; mud and shallow water around; light Trần boats circle it; on its tilted deck a Yuan "
                    "officer in lamellar armor and a round helmet grips the rail. Anh Tư stands in a small boat beside one "
                    "giant stake that pierces the hull."),
              img=("Epic close shot in a field of giant pointed ironwood stakes at low tide, a huge wooden war junk impaled "
                   "on the stakes with a cracked hull, leaning mast and torn matting sail, small light boats circling, a "
                   "Yuan officer in lamellar armor gripping the rail on the tilted deck, {FACE}, standing in a small boat "
                   "beside a giant stake piercing the hull, realistic, vertical 9:16."),
              amb=f"groaning timber, water rushing out between the stakes, distant battle, {EPIC}"),
    "E": dict(name="Hoàng hôn trên sông Bạch Đằng",
              lock=("SCENE E (keep IDENTICAL in every clip of this scene): sunset over the Bạch Đằng river, the sky burning "
                    "orange behind the karsts; as far as the eye can see, hundreds of big Yuan junks stuck and tilted among "
                    "the stakes, thin smoke rising, Trần boats moving calmly between them. Anh Tư sits on the bow of his "
                    "small boat tied to a stake."),
              img=("Epic wide shot at sunset over a wide river between limestone karsts, burning orange sky, hundreds of big "
                   "wooden junks stuck and tilted among giant stakes, thin smoke rising, small boats moving calmly between "
                   "them, {FACE}, sitting on the bow of a small boat tied to a stake, realistic, vertical 9:16."),
              amb=f"calm water, distant voices, gulls, the bamboo flute motif of {EPIC}, soft"),
}

CLIPS = [
    dict(scene="A", who="narr", label="Sông Bạch Đằng · sáng 9/4/1288",
         line=(0.8, 9.2, "Sáng ngày chín tháng tư / năm 1288. / Hạm đội Nguyên / đã vào sâu / trong sông Bạch Đằng."),
         cam="slow aerial gliding over the misty reeds toward the anchored fleet on the high tide; no faces close enough to see"),
    dict(scene="A", who="cai",
         line=(0.4, 9.2, "Nằm im, nhìn nước. / Hết nước thì đánh. / Đứa nào ho… / ra sông mà ho / với cá."),
         cam="the squad leader crouching in the reeds faces the camera and whispers the order; Anh Tư is out of frame"),
    dict(scene="A", who="tu",
         line=(0.4, 9.2, "Em nằm đây từ sáng… / muỗi đốt bốn mươi phát, / không dám đập. / Đập một cái… / là lộ cả đạo quân."),
         cam="close-up of Anh Tư alone lying in the reeds, a mosquito lands on his nose; he crosses his eyes at it but does not move, whispering to the camera"),
    dict(scene="B", who="narr", chuyen="fade:0.5",
         line=(0.8, 9.2, "Rồi nước bắt đầu rút. / Từng đầu cọc lim / nhô lên giữa lòng sông, / như một khu rừng mọc dậy."),
         cam="grand time-lapse aerial as the water drains and the stake tips rise row after row across the river; no faces close enough to see"),
    dict(scene="B", who="tu",
         line=(0.8, 8.8, "Rút rồi! À không… sóng. / Rút thật rồi! / Mấy cái que / em ôm không hết… / giờ nhô lên chào giặc!"),
         cam="Anh Tư alone on the bank watching his measuring pole, then staring at the river as the stakes appear"),
    dict(scene="C", who="narr", chuyen="fadewhite:0.3",
         line=(0.8, 9.2, "Từ thượng lưu, / Hưng Đạo vương / đánh xuống. / Hai vua Trần / đem quân từ hai bên / ập vào."),
         cam="huge sweeping aerial as the boats charge from upstream and both banks and the infantry pour out; the general by the drum is a tiny figure from behind; no faces close enough to see"),
    dict(scene="C", who="tu",
         line=(0.4, 9.2, "Thuyền họ to như đình… / giờ đứng im / như đình thật. / Em chèo ngang qua / còn kịp vái một cái."),
         cam="tracking shot alongside Anh Tư rowing past a huge stuck junk; he gives it a quick respectful bow of the head without stopping rowing; nobody else speaks"),
    dict(scene="D", who="narr",
         line=(0.8, 9.2, "Hàng trăm thuyền lớn / mắc cọc, vỡ ván, / gãy buồm. / Càng cố lùi ra… / càng mắc chặt."),
         cam="slow-motion low angle as the huge junk grinds on the stakes, timbers crack, the mast leans; then wide on many junks stuck the same way; no faces close enough to see"),
    dict(scene="D", who="quan",
         line=(0.4, 9.2, "Lùi lại! Lùi lại! / Nước đâu hết rồi? / Sao thuyền không đi? / Dưới sông này… / có cái gì thế này?!"),
         cam="the Yuan officer gripping the rail on the tilted deck shouts down to his crew; nobody else in frame speaks"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Dạ… cọc nhà em ạ. / Cắm cả tuần đấy. / Ông đứng yên cho, / đừng giãy… / giãy là gãy cọc em."),
         cam="Anh Tư alone in frame in his small boat, both hands protectively on the giant stake that pierces the hull, looking up at the officer with polite worry"),
    dict(scene="E", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 9.2, "Trận đánh kéo dài / từ sáng đến chiều tối. / Cả khúc sông Bạch Đằng / thành cái bẫy / của hạm đội Nguyên."),
         cam="grand slow aerial over the sunset river full of stuck junks; no faces close enough to see"),
    dict(scene="E", who="tu",
         line=(0.4, 9.2, "Sáng còn là sông… / trưa đã thành rừng cọc. / Vợ em hỏi / cả tuần làm gì… / giờ em chỉ ra sông là đủ."),
         cam="Anh Tư on the bow of his boat turns to the camera, then proudly points his thumb back at the river full of stuck junks, a faint smile"),
]
WHO = {"tu": "ANH TƯ", "cai": "THE SQUAD LEADER", "quan": "THE YUAN OFFICER", "narr": "the NARRATOR (off-screen voice-over)"}
NAME = {"tu": "Anh Tư", "cai": "Cai đội", "quan": "Quan Nguyên", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "cai": V_CAI, "quan": V_QUAN, "narr": V_NARR}
PREFIX = {k: "" for k in NAME}


def video_prompt(c):
    """Lời tiếng Việt đặt ĐẦU prompt, rồi mới tới bối cảnh, máy quay, âm thanh (Muse đọc rõ hơn)."""
    a, b, text = c["line"]
    sc = SCENES[c["scene"]]
    face = FACE + "." if c["who"] == "tu" or "Anh Tư" in c["cam"] else ""
    return " ".join(x for x in [
        tieng_viet(WHO[c["who"]], VOICE[c["who"]], loi_muse(text), a, b),
        "One continuous 10-second shot, no cut.", f"Camera: {c['cam']}.", sc["lock"], face, BASE,
        AUDIO.format(amb=sc["amb"]), SO_RULE] if x)


DANG_BAI = """## Đăng TikTok

**Hook** (chữ to ở giây đầu, dùng luôn làm chữ trên ảnh bìa):
```
POV: Bạn chỉ được giao / đứng nhìn nước
```

Hook dự phòng:
```
POV: Sáng còn là sông / trưa đã thành rừng cọc
POV: Hạm đội Nguyên / mắc cọc Bạch Đằng
```

**Tiêu đề:**
```
Trận Bạch Đằng 1288: sáng còn là sông, trưa đã thành rừng cọc | Bạch Đằng 1288 tập 8
```

**Mô tả và hashtag:**
```
Cả tuần ngồi xem nước… và rồi nước rút 🌊 Từng đầu cọc lim nhô lên giữa sông Bạch Đằng, hàng trăm thuyền lớn của hạm đội Nguyên mắc kẹt. Hưng Đạo vương đánh từ thượng lưu, hai vua Trần đánh từ hai bên. Trận đánh kéo dài từ sáng đến chiều tối. Đây là tập 8 của loạt Bạch Đằng 1288. Theo bạn, tướng Ô Mã Nhi sẽ ra sao? 👇
#povlichsu #POV #lichsuvietnam #xuhuong #fyp #bachdang1288 #tranbachdang #tranhungdao #anhtu
```

**Bình luận ghim:**
```
Tập 9 ngày mai 19h: Anh Tư được giao canh một ông tướng… người từng đòi "lên trời cũng đuổi theo" 👀 Follow để không lỡ tập nào!
```

**Mẫu trả lời 60 phút đầu:**
1. (Về trận đánh) "Sáng 9/4/1288 (8/3 âm lịch), quân Trần nhử hạm đội Ô Mã Nhi vào sông lúc triều lên; triều rút, thuyền giặc mắc cọc. Theo Nguyên sử, trận đánh kéo dài từ giờ Mão đến giờ Dậu."
2. (Về các mũi đánh) "Hưng Đạo vương đánh từ thượng lưu, hai vua Trần đem quân từ hai bên đánh vào, bộ binh mai phục hai bờ."
3. (Về kết quả) "Hơn 400 chiến thuyền bị bắt, nhiều tướng giặc bị bắt sống. Chuyện Ô Mã Nhi ở tập 9."

Khi đăng: bật nhãn "Nội dung do AI tạo".

## Đăng YouTube Shorts

**Tiêu đề:**
```
Trận Bạch Đằng 1288: sáng còn là sông, trưa đã thành rừng cọc | tập 8 #Shorts
```

**Mô tả:**
```
Cả tuần ngồi xem nước… và rồi nước rút 🌊 Từng đầu cọc lim nhô lên giữa sông Bạch Đằng, hàng trăm thuyền lớn của hạm đội Nguyên mắc kẹt. Đây là tập 8 của loạt Bạch Đằng 1288.

Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 10 tập.

#Shorts #povlichsu #lichsuvietnam #bachdang1288 #tranhungdao #anhtu
```

**Thẻ:**
```
trận bạch đằng 1288, bãi cọc bạch đằng, trần hưng đạo, ô mã nhi, kháng chiến chống nguyên, thủy chiến, nhà trần, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts
```

Mục "Nội dung bị thay đổi" chọn **Có**.

## Đăng Facebook

**Caption:**
```
Cả nhà ơi, 19h tối nay có tập 8: trận Bạch Đằng 🌊

Tui ngồi xem nước cả tuần, sáng nay lại nằm xem nước… rồi nước rút thật! Từng đầu cọc lim nhô lên, cả hạm đội Nguyên mắc kẹt giữa sông.

Sáng còn là sông… trưa đã thành rừng cọc 😎

Cả nhà đoán tướng Ô Mã Nhi sẽ ra sao? 👇

#BachDang1288 #TranBachDang #TranHungDao #POVMotNgayODaiViet #LichSuVietNam
```

Đăng dạng **Reel**, cùng một bản với TikTok và YouTube. Bật "Thông tin về AI"."""


def main():
    base = "bd1288-tap8"
    md_name = base + "-song-thanh-rung.md"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Bạn chỉ được giao / đứng nhìn nước", "end: Follow để xem / Người từng đòi lên trời →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 8: Sông thành rừng (trận Bạch Đằng)", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook · **9/12 clip (75%) là nước rút và trận đánh.**", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); dẫn chuyện giọng Bắc "
          "trầm; cai đội thì thầm gắt; quan Nguyên hốt hoảng.", "",
          "## Mạch tập", "",
          "- **Chờ nước** (clip 1–3): hạm đội Nguyên vào sâu trong sông; cai đội dặn nằm im xem nước; Anh Tư nằm cho muỗi đốt mà không dám đập.",
          "- **Nước rút** (clip 4–5): đầu cọc lim nhô lên hàng hàng lớp lớp, như rừng mọc dậy giữa sông.",
          "- **Ba mặt đánh vào** (clip 6–7): Hưng Đạo vương từ thượng lưu, hai vua Trần từ hai bên, bộ binh hai bờ; hàng trăm thuyền nhẹ lao ra.",
          "- **Giữa bãi cọc** (clip 8–10): thuyền lớn mắc cọc, vỡ ván, gãy buồm, càng lùi càng mắc; quan Nguyên hốt hoảng; Anh Tư vỗ cây cọc.",
          "- **Hoàng hôn** (clip 11–12): trận kéo dài tới chiều tối, cả khúc sông thành cái bẫy; câu chốt.",
          "- **Hoành tráng mà an toàn:** thuyền vỡ, buồm rách, khói, tên bay; **không máu, không xác, không ai chết trên màn hình**. "
          "Chuyện bắt Ô Mã Nhi để dành cho tập 9.",
          "- **Âm thanh:** rạng sáng gần như im lặng; nước rút thì nhạc dâng dần; lúc ba mặt đánh vào (clip 6) lóe trắng và trống trận "
          "mạnh nhất; hoàng hôn còn sáo trúc nhẹ. Nhạc luôn rất nhỏ dưới lời nói.",
          "- **Hài hơn (sửa theo yêu cầu):** muỗi đốt bốn mươi phát không dám đập; cọc \"nhô lên chào giặc\"; chèo ngang thuyền to như đình \"còn kịp vái một cái\"; "
          "quan Nguyên hỏi dưới sông có gì, Anh Tư lo… gãy cọc nhà mình; vợ hỏi cả tuần làm gì, chỉ ra sông là đủ. Cai đội: \"đứa nào ho, ra sông mà ho với cá\".",
          "- **Để Muse nói đúng tiếng Việt:** câu nói đặt ngay đầu prompt, lời gửi Muse không có dấu \"…\", năm viết thành chữ; prompt gọn.", "",
          "**Lịch sử (mức A):** sáng 9/4/1288 (8/3 âm lịch Mậu Tý), hạm đội Ô Mã Nhi bị nhử vào sông Bạch Đằng lúc triều lên; triều "
          "rút, thuyền mắc cọc, vỡ, kẹt. Trần Hưng Đạo đánh từ thượng lưu, hai vua Trần đem quân từ hai bên đánh vào, bộ binh mai "
          "phục hai bờ. Theo *Nguyên sử*, trận đánh kéo dài từ giờ Mão đến giờ Dậu (sáng đến chiều tối). **Phần dựng lại:** cách "
          "dàn trận trên màn hình, cây trống trên đồi. **Hư cấu:** Anh Tư, cai đội, quan Nguyên và mọi lời thoại. Không nêu thương vong.", "",
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
