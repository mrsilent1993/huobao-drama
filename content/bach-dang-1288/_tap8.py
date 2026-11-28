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
    "A": dict(name="Hạm đội Nguyên tiến vào lúc triều lên",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): early morning, full high tide on the wide Bạch Đằng "
                    "river between towering limestone karsts, golden mist; more than a hundred big Yuan war junks with full "
                    "matting sails sail proudly upriver in long columns, chasing a few small light Trần boats fleeing far "
                    "ahead; soldiers in lamellar armor crowd the decks. On the prow of the lead junk stands the Yuan officer: a tall man in his 40s with a thin mustache, lamellar armor with bronze plates and a round helmet with a red tassel."),
              img=("Epic aerial in early morning golden mist over a wide river between towering limestone karsts at full high "
                   "tide, more than a hundred big wooden war junks with full matting sails sailing upriver in long columns, "
                   "chasing a few small boats far ahead, soldiers in lamellar armor on the decks, realistic, vertical 9:16."),
              amb=f"wind in full sails, creaking hulls, war drums from the fleet, {EPIC} confident and rising"),
    "R": dict(name="Bãi lau mai phục",
              lock=("SCENE R: tall reeds and mangroves on the Bạch Đằng riverbank in early morning mist; Trần soldiers lie "
                    "hidden in the reeds with bows and spears, completely still; through the reeds the great Yuan fleet sails "
                    "past on the high tide. Anh Tư lies flat in the reeds beside a notched bamboo measuring pole."),
              img=("Cinematic shot from inside tall reeds on a riverbank in morning mist, soldiers lying hidden with bows, "
                   "through the reeds a great fleet of wooden war junks sailing past on the high tide, {FACE}, lying flat "
                   "beside a notched bamboo measuring pole, realistic, vertical 9:16."),
              amb="rustling reeds, lapping water, the fleet's drums passing, mosquitoes buzzing close"),
    "B": dict(name="Đoàn thuyền đang tiến vào thì nước rút",
              lock=(STAKE + " SCENE B (keep IDENTICAL in every clip of this scene): mid-morning on the Bạch Đằng river between "
                    "towering karsts: the great Yuan fleet, more than a hundred big war junks with full matting sails, is "
                    "STILL SAILING UPRIVER in long columns, soldiers in lamellar armor crowding the decks; the tide is falling "
                    "fast, the waterline visibly sinking along the muddy banks; just beneath and then above the surface, rows "
                    "of giant pointed ironwood stake tips appear right in front of and between the ships. The lead junks "
                    "jolt to a sudden stop as their hulls scrape onto the stakes, masts whip forward, sails flap; soldiers "
                    "are thrown off balance, grab ropes and rails, rush to the sides and stare down in shock, officers shout "
                    "and point; the ships behind cannot stop and bump into the stuck ones ahead. Nobody falls into the water, "
                    "no injuries. On the bank among the reeds, Anh Tư stands by his notched bamboo measuring pole."),
              img=("Epic shot at mid-morning on a wide river between limestone karsts: a great fleet of big wooden war junks "
                   "with full matting sails still sailing upriver in long columns, soldiers in lamellar armor crowding the "
                   "decks, the tide falling fast with the waterline sinking along muddy banks, rows of giant pointed wooden "
                   "stake tips breaking the surface right in front of the lead ships, the first junk jolting to a stop with "
                   "its mast whipping forward and soldiers grabbing the rails in shock, {FACE}, watching from the reeds by a "
                   "bamboo measuring pole, realistic, vertical 9:16."),
              amb=f"creaking hulls, wind in full sails, water draining, a sudden grinding crunch of wood on wood, shouting on the decks, {EPIC} rising"),
    "C": dict(name="Quân Trần ba mặt đánh vào",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): the great battle on the Bạch Đằng river at late "
                    "morning: from upstream and from both banks hundreds of small light Trần war boats charge in at full "
                    "speed, oars flashing; Trần infantry pour out of the reeds and mangroves on both banks; volleys of "
                    "arrows arc over the water; on a high hill far away a dark-robed general stands by a giant war drum, "
                    "seen only from behind; the big Yuan junks stuck on the stakes cannot move. Smoke drifts across the karsts. The squad leader in a dark tunic "
                    "with a sword stands in the bow of the nearest Trần boat; Anh Tư rows in the boat beside it."),
              img=("Epic aerial of a great naval battle on a wide river between limestone karsts, hundreds of small light war "
                   "boats charging from upstream and both banks, infantry pouring out of the mangroves, volleys of arrows, "
                   "big wooden junks stuck among giant stakes, smoke drifting, a general by a giant war drum on a far "
                   "hill seen from behind, {FACE}, rowing hard in a small boat in the foreground, realistic, vertical 9:16."),
              amb=f"thundering war drums, hundreds of oars, battle cries, cracking timber, {EPIC} at full power"),
    "D": dict(name="Giữa bãi cọc, thuyền giặc mắc kẹt",
              lock=(STAKE + " SCENE D (keep IDENTICAL in every clip of this scene): in the middle of the stake field at low "
                    "tide: a huge Yuan war junk is impaled on giant ironwood stakes, its hull cracked, its mast leaning, its "
                    "matting sail torn; mud and shallow water around; light Trần boats circle it; on its tilted deck " 
                    "the Yuan officer: a tall man in his 40s with a thin mustache, lamellar armor with bronze plates and a round helmet with a red tassel grips the rail. Anh Tư stands in a small boat beside one "
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
         line=(0.8, 9.2, "Ngày chín tháng tư / năm 1288. / Hạm đội Nguyên / đuổi vào sông Bạch Đằng / lúc triều lên."),
         cam="grand low aerial racing alongside the proud fleet sailing upriver on the high tide, the small boats fleeing far ahead; no faces close enough to see"),
    dict(scene="A", who="quan",
         line=(0.4, 9.2, "Thuyền nhỏ chạy hết rồi! / Đuổi theo! / Sông rộng thế này, / thuyền ta to thế này… / còn sợ cái gì!"),
         cam="the Yuan officer on the prow of the lead junk, wind in his face, points his sword upriver and laughs confidently; nobody else in frame speaks"),
    dict(scene="R", who="tu",
         line=(0.4, 9.2, "Muỗi đốt bốn mươi phát / em không dám đập. / Còn ông hỏi / sợ cái gì à? / Chờ nước rút… / ông tự biết."),
         cam="close-up of Anh Tư lying flat in the reeds, a mosquito on his nose; he crosses his eyes at it without moving, then whispers to the camera as the fleet passes behind the reeds"),
    dict(scene="B", who="narr", chuyen="fade:0.5",
         line=(0.8, 9.2, "Đoàn thuyền vẫn tiến vào… / thì nước bắt đầu rút. / Cọc lim nhô lên / ngay trước mũi thuyền. / Giặc trở tay không kịp."),
         cam="three beats in one continuous move: 0-3s low aerial following the fleet as it sails proudly upriver on calm water; "
             "3-6s the camera drops close to the water as the level sinks and the giant stake tips rise just ahead of the bows; "
             "6-10s the lead junk crunches onto the stakes and jolts to a stop, the mast whips forward, soldiers stumble, grab the "
             "rails and rush to look over the side in shock while the next ship bumps into it from behind; no faces close enough "
             "to see anyone speak"),
    dict(scene="B", who="tu",
         line=(0.4, 9.2, "Rút rồi! À không… sóng. / Rút thật rồi! / Mấy cái que / em ôm không hết… / giờ nhô lên chào giặc!"),
         cam="Anh Tư alone on the bank glances at his measuring pole, then jumps up and stares at the river as the stakes appear in front of the fleet"),
    dict(scene="C", who="narr", chuyen="fadewhite:0.3",
         line=(0.8, 9.2, "Từ thượng lưu, / Hưng Đạo vương / đánh xuống. / Hai vua Trần / đem quân từ hai bên / ập vào."),
         cam="huge sweeping aerial as the boats charge from upstream and both banks and the infantry pour out; the general by the drum is a tiny figure from behind; no faces close enough to see"),
    dict(scene="C", who="cai",
         line=(0.4, 9.2, "Áp sát! Áp sát! / Bắn vào buồm! / Đừng bắn vào cọc… / cọc nhà mình đấy, / bắn gãy là tao phạt!"),
         cam="the squad leader in the bow of the charging boat turns back and shouts the order, pointing his sword at the sails; Anh Tư is out of frame"),
    dict(scene="C", who="tu",
         line=(0.4, 9.2, "Thuyền họ to như đình… / giờ đứng im / như đình thật. / Em chèo ngang qua / còn kịp vái một cái."),
         cam="tracking shot alongside Anh Tư rowing past a huge stuck junk; he gives it a quick respectful bow of the head without stopping rowing; nobody else speaks"),
    dict(scene="D", who="narr",
         line=(0.8, 9.2, "Hàng trăm thuyền lớn / mắc cọc, vỡ ván, / gãy buồm. / Càng cố lùi ra… / càng mắc chặt."),
         cam="slow-motion low angle as the huge junk grinds on the stakes, timbers crack, the mast leans; then wide on many junks stuck the same way; no faces close enough to see"),
    dict(scene="D", who="quan",
         line=(0.4, 9.2, "Lùi lại! Lùi lại! / Nước đâu hết rồi? / Sao thuyền không đi? / Dưới sông này… / mọc cái gì thế này?!"),
         cam="the same Yuan officer, now gripping the rail on the tilted deck, shouts down in disbelief; nobody else in frame speaks"),
    dict(scene="D", who="tu",
         line=(0.4, 9.2, "Dạ… cọc nhà em ạ. / Cắm cả tuần đấy. / Ông đứng yên cho, / đừng giãy… / giãy là gãy cọc em."),
         cam="Anh Tư alone in frame in his small boat, both hands protectively on the giant stake that pierces the hull, looking up at the officer with polite worry"),
    dict(scene="E", who="tu", chuyen="fadeblack:0.6",
         line=(0.4, 9.2, "Đánh từ sáng đến tối… / sáng còn là sông, / tối đã thành rừng cọc. / Vợ hỏi cả tuần làm gì… / em chỉ ra sông."),
         cam="sunset: Anh Tư on the bow of his boat turns to the camera, then proudly points his thumb back at the river full of stuck junks, a faint smile"),
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
POV: Giặc hỏi dưới sông / mọc cái gì… / dạ, cọc nhà em
```

Hook dự phòng:
```
POV: Bạn chỉ được giao / đứng nhìn nước
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
            "hook: POV: Giặc hỏi dưới sông / mọc cái gì… / dạ, cọc nhà em", "end: Follow để xem / Người từng đòi lên trời →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 8: Sông thành rừng (trận Bạch Đằng)", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook · **9/12 clip (75%) là nước rút và trận đánh.**", "",
          f"**File Muse đặt tên:** `{base}-1..{n}.mp4` · **Giọng:** Anh Tư giọng Bắc (một giọng cố định); dẫn chuyện giọng Bắc "
          "trầm; cai đội gắt; quan Nguyên (một người, xuất hiện 2 lần) từ tự tin đến hốt hoảng.", "",
          "## Mạch tập", "",
          "- **Hạm đội vào bẫy** (clip 1–3): triều lên, hạm đội hơn trăm chiếc căng buồm đuổi theo thuyền nhẹ; quan Nguyên đứng mũi thuyền: \"còn sợ cái gì!\"; Anh Tư nằm trong bãi lau cho muỗi đốt: \"chờ nước rút… ông tự biết\".",
          "- **Đang tiến vào thì nước rút** (clip 4–5): cọc lim nhô lên ngay trước mũi thuyền, thuyền đầu va cọc khựng lại, lính chao đảo, thuyền sau đâm thuyền trước: trở tay không kịp.",
          "- **Ba mặt đánh vào** (clip 6–8): Hưng Đạo vương từ thượng lưu, hai vua Trần từ hai bên; cai đội: \"bắn vào buồm, đừng bắn vào cọc, cọc nhà mình đấy!\"; Anh Tư chèo ngang \"vái\" thuyền to như đình.",
          "- **Giữa bãi cọc** (clip 9–11): càng lùi càng mắc; **cùng ông quan** lúc sáng giờ bám mạn: \"dưới sông mọc cái gì thế này?!\"; Anh Tư ôm cọc: \"giãy là gãy cọc em\".",
          "- **Hoàng hôn** (clip 12): đánh từ sáng đến tối, câu chốt nhắc chuyện vợ hỏi (tập 6).",
          "- **Hoành tráng mà an toàn:** thuyền vỡ, buồm rách, khói, tên bay; **không máu, không xác, không ai chết trên màn hình**. "
          "Chuyện bắt Ô Mã Nhi để dành cho tập 9.",
          "- **Âm thanh:** rạng sáng gần như im lặng; nước rút thì nhạc dâng dần; lúc ba mặt đánh vào (clip 6) lóe trắng và trống trận "
          "mạnh nhất; hoàng hôn còn sáo trúc nhẹ. Nhạc luôn rất nhỏ dưới lời nói.",
          "- **Hài (làm lại):** quan Nguyên khoe \"còn sợ cái gì\" ở clip 2 rồi chính ông hỏi \"dưới sông mọc cái gì\" ở clip 10; muỗi đốt bốn mươi phát không dám đập; cọc \"nhô lên chào giặc\"; chèo ngang thuyền to như đình \"còn kịp vái một cái\"; "
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
