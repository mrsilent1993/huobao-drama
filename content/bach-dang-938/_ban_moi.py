#!/usr/bin/env python3
"""Bạch Đằng 938, BẢN MỚI 45–60 giây (22/11/2026), viết lại theo mọi tiêu chuẩn đã bổ sung:
cọc đúng cỡ (STAKE_SPEC, đầu bịt sắt theo Toàn thư), quân Nam Hán đúng chuẩn, không cờ hiện đại/không chữ, giọng Bắc,
diễn tự nhiên, câu gạt riêng, câu chốt riêng, Ngô Quyền chỉ thấy từ phía sau, YouTube đủ cảnh, TikTok giữ trọn câu thoại.
Anh chọn giữ câu chốt gốc "Cọc này là của em đóng đấy, các bác ghi tên em vào sử nhé" (ngoại lệ có chủ ý).
Chạy: python3 _ban_moi.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, hair in a topknot, black-lacquered teeth, a scar across his "
        "left eyebrow and a chipped front tooth; he acts naturally and understated, like a real person, not a performer")
NGO = ("Ngô Quyền, seen ONLY from behind or far away: a broad-shouldered commander in dark lacquered leather armor and a "
       "deep-red cloak")
SAFE = ("Adults only, no children. No flags with writing, no modern flags, no legible writing anywhere, no modern objects, "
        "no blood, no dead bodies.")
ACTING = ("Acting: natural and understated, like real people filmed in a documentary; small reactions (a sigh, a glance, "
          "a pause) instead of big expressions; Anh Tư smiles at most once in the whole clip and never laughs at the camera.")
SETTING = ("Vietnam, winter of 938, the Bạch Đằng River estuary near the sea: a wide brown tidal river, mangrove banks, "
           "limestone hills, broad mudflats at low tide. Vietnamese soldiers with hair in topknots and black-lacquered teeth, "
           "in brown tunics or bare-chested, with spears, bows and small light wooden boats. The Southern Han forces: tall "
           "multi-deck wooden warships with PLAIN red banners (no writing), soldiers in late-Tang-style lamellar armor and "
           "helmets with neck guards. Absolutely NO European plate armor, NO European sailing ships. "
           f"Anh Tư is {FACE}, a soldier driving stakes. {SAFE} {ACTING}")
VISUAL = ("**Chuẩn hình ảnh:** quân ta búi tóc, răng đen, áo nâu hoặc cởi trần; quân Nam Hán giáp vảy cuối thời Đường, mũ "
          "che gáy, lâu thuyền nhiều tầng, **cờ đỏ trơn không chữ**; cấm giáp tấm, thuyền buồm kiểu châu Âu, cờ hiện đại. "
          "**Cọc:** cả thân cây lim dày 20–30 cm, dài 2,5–3 m, đầu bịt sắt (theo *Toàn thư*), nhiều người dùng vồ gỗ nặng "
          "đóng lúc triều rút; không que nhỏ, không búa tay. **Ngô Quyền chỉ thấy từ phía sau.**")

EPISODES = [
    dict(
        slug="dong-coc-bach-dang-938", prefix="bd938n",
        length=("**YouTube** đủ 6 cảnh, khoảng 58 giây; **TikTok** 5 cảnh giữ trọn câu thoại, khoảng 47 giây (bỏ cảnh 3, bịt sắt)"),
        muc={"youtube": (45, 60), "tiktok": (40, 50)}, tiktok_canh=[1, 2, 4, 5, 6],
        voices={"officer": "a gruff, clipped male voice in his 40s, short commands",
                "Ngô Quyền": "a low, steady, authoritative male voice around 40, few words, never shouting"},
        title="Bị sai ra bãi bùn đóng những cây cọc to bằng cái đùi, không ai nói để làm gì (Bạch Đằng, 938)",
        history=("**Lịch sử:** năm 938, quân Nam Hán do Hoằng Tháo chỉ huy theo đường biển sang. Ngô Quyền cho **đóng cọc lớn "
                 "đầu bịt sắt** ở cửa sông Bạch Đằng, **lợi dụng thủy triều**: khi triều lên, dùng thuyền nhẹ nhử thuyền giặc "
                 "vào; khi triều rút, cọc nhô lên, thuyền giặc mắc cọc, vỡ đắm, quân ta đánh mạnh, quân Nam Hán thua to, Hoằng "
                 "Tháo tử trận (*Đại Việt sử ký toàn thư*, mức B; chi tiết cọc đầu bịt sắt theo *Toàn thư*). Chiến thắng chấm "
                 "dứt hơn một nghìn năm Bắc thuộc; năm 939 Ngô Quyền xưng vương. **Cỡ cọc** theo các bãi cọc khai quật (của "
                 "trận 1288, mức ước lượng). **Hư cấu:** Anh Tư và mọi lời thoại. Cái chết "
                 "chỉ ghi ở đây, phim không dựng cảnh chết."),
        setting=SETTING,
        visual=VISUAL,
        hook="POV: Đóng cọc / to bằng cái đùi / giữa sông",
        end="Follow để xem / thêm chuyện / Đại Việt →",
        end_secs=1.6,
        clips=[
            dict(name="Ra bãi đóng cọc", label="Cửa sông Bạch Đằng · 938",
                 img=f"First-person view on a wide muddy riverbank at low tide, a gruff officer pointing at a pile of huge ironwood tree trunks with sharpened tips, {FACE} beside the viewer staring at them, the brown river and limestone hills behind, realistic, vertical 9:16.",
                 vid=("0-5s: The officer points at a pile of huge sharpened ironwood trunks: \"Ra bãi đóng cọc. Đóng cho sâu.\" "
                      "Anh Tư: \"Đóng cọc giữa sông... để làm gì ạ?\" The officer: \"Nước rút thì biết.\" 5-10s: Anh Tư puts his "
                      "hand on a trunk and says quietly to the viewer: \"Cọc gì... to bằng cái đùi em.\""),
                 subs=[(0.3, 2.2, "Ra bãi đóng cọc. / Đóng cho sâu."), (2.2, 3.4, "Đóng cọc giữa sông... / để làm gì ạ?"),
                       (3.4, 4.9, "Nước rút thì biết."), (5.2, 9.5, "Cọc gì... / to bằng cái đùi em.")]),
            dict(name="Mười người một cọc", label="",
                 img=f"First-person view on the mudflat at low tide, a team of ten men lifting a heavy wooden ram on ropes above a massive ironwood stake and dropping it, {FACE} pulling a rope, mud splashing, realistic, vertical 9:16.",
                 vid=("0-5s: A team of ten men haul ropes to lift a heavy wooden ram and drop it on a massive stake: \"Một, hai... "
                      "thả!\" Thud. The stake sinks only a little. 5-10s: Anh Tư, panting, says quietly to the viewer: \"Mười người "
                      "một cây cọc... mà nó lún có một gang.\""),
                 subs=[(0.5, 4.8, "Một, hai... thả!"), (5.0, 9.5, "Mười người một cây cọc... / mà nó lún có một gang.")]),
            dict(name="Bịt sắt", label="",
                 img=f"First-person view at a riverside forge, a blacksmith fitting a pointed iron cap onto the sharpened tip of a massive ironwood stake, sparks flying, {FACE} holding the stake steady, realistic, vertical 9:16.",
                 vid=("0-5s: At a riverside forge a blacksmith hammers a pointed iron cap onto the tip of a massive stake; sparks "
                      "fly. 5-10s: Anh Tư, holding the stake, sighs: \"Cọc đã to... còn bịt thêm sắt.\""),
                 subs=[(5.0, 9.5, "Cọc đã to... / còn bịt thêm sắt.")]),
            dict(name="Nước lên mất cọc", label="",
                 img=f"First-person view at dusk as the rising tide slowly covers rows of iron-capped stakes until only smooth brown water remains, {FACE} standing on the bank, staring, realistic, vertical 9:16.",
                 vid=("0-5s: Dusk; the tide rises and slowly swallows the rows of stakes until only smooth brown water is left. "
                      "5-10s: Anh Tư stares at the water: \"Đóng cả ngày... nước lên một cái là mất hết.\""),
                 subs=[(5.0, 9.5, "Đóng cả ngày... / nước lên một cái / là mất hết.")]),
            dict(name="Thuyền giặc vào", label="",
                 img=f"First-person view from the reeds at high tide, a fleet of tall multi-deck warships with plain red banners entering the river mouth chasing a few small light boats, the stakes hidden under the water, {FACE} crouching in the reeds, realistic, vertical 9:16.",
                 vid=("0-5s: High tide; a few small boats row away upriver; the tall warships with plain red banners chase them "
                      "into the river mouth, right over the hidden stakes. 5-10s: Anh Tư, in the reeds, whispers: \"Thuyền nó to "
                      "thế... đi ngay trên đầu cọc em mà không biết.\""),
                 subs=[(5.0, 9.5, "Thuyền nó to thế... / đi ngay trên đầu cọc em / mà không biết.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at midday as the tide falls, a forest of iron-capped stakes emerging from the water, tall warships tilting and stuck among them, many small Vietnamese boats closing in, {FACE} in the foreground with one hand on a stake, no bodies, realistic, vertical 9:16.",
                 vid=("0-5s: The tide falls; a forest of iron-capped stakes rises; the tall warships lurch and stick fast, timber "
                      "cracking; war drums on both banks; small boats close in. No bodies, no blood. A calm narrator's voice says: "
                      "\"Năm 938, Ngô Quyền cắm cọc ở cửa sông Bạch Đằng. Triều rút, thuyền Nam Hán mắc cọc. Hơn một nghìn năm "
                      "Bắc thuộc chấm dứt.\" 5-10s: Anh Tư pats the nearest stake and says to the camera: \"Cọc này là của em đóng "
                      "đấy... các bác ghi tên em vào sử nhé!\""),
                 subs=[(0.3, 4.8, "Năm 938, Ngô Quyền / cắm cọc ở cửa Bạch Đằng. / Hơn nghìn năm Bắc thuộc / chấm dứt."),
                       (5.0, 8.4, "Cọc này là của em đóng đấy... / các bác ghi tên em / vào sử nhé!")]),
        ],
        caption=("Bị sai ra bãi bùn đóng những cây cọc to bằng cái đùi, không ai nói để làm gì 😳 Năm 938, Ngô Quyền cắm cọc "
                 "đầu bịt sắt ở cửa sông Bạch Đằng: triều lên nhử thuyền giặc vào, triều rút cọc nhô lên. Bạn đoán mười người "
                 "đóng một cây cọc mất bao lâu? 👇"),
        tags="#bachdang #ngoquyen #938 #lichsuvietnam #cocbachdang",
        tt_title="Bị sai ra bãi bùn đóng những cây cọc to bằng cái đùi",
        hooks_alt=["POV: Mười người một cây cọc / lún có một gang", "POV: Đóng cả ngày / nước lên là mất hết"],
        pin=("Cọc trận 938 là cả thân cây lim, đầu bịt sắt theo Toàn thư 🔥 Các bác đã ghi tên Anh Tư vào sử chưa? Follow để xem "
             "thêm chuyện Đại Việt!"),
        yt_title="Bạch Đằng 938: đóng cọc cho Ngô Quyền | POV lịch sử",
        yt_tags=("bạch đằng 938, ngô quyền, cọc bạch đằng, cọc bịt sắt, thủy triều, nam hán, hoằng tháo, chấm dứt bắc thuộc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#povlichsu #anhtu", note=("**Bản mới 45–60 giây** (22/11/2026), viết lại theo mọi "
          "tiêu chuẩn đã bổ sung. Giữ câu chốt gốc của kênh theo ý anh."),
          unit="Bản mới", file_unit="ban-moi")
