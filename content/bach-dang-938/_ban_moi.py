#!/usr/bin/env python3
"""Bạch Đằng 938, BẢN MỚI 45–60 giây (22/11/2026), viết lại theo mọi tiêu chuẩn đã bổ sung:
cọc đúng cỡ (STAKE_SPEC, đầu bịt sắt theo Toàn thư), quân Nam Hán đúng chuẩn, không cờ hiện đại/không chữ, giọng Bắc,
diễn tự nhiên, câu gạt riêng, câu chốt riêng, Ngô Quyền chỉ thấy từ phía sau, YouTube đủ cảnh, TikTok giữ trọn câu thoại.
Góc kể MỚI (không lặp video "cắm cọc cả buổi sáng"): Anh Tư là người canh con nước.
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
           f"Anh Tư is {FACE}, a soldier who watches the tide. {SAFE} {ACTING}")
VISUAL = ("**Chuẩn hình ảnh:** quân ta búi tóc, răng đen, áo nâu hoặc cởi trần; quân Nam Hán giáp vảy cuối thời Đường, mũ "
          "che gáy, lâu thuyền nhiều tầng, **cờ đỏ trơn không chữ**; cấm giáp tấm, thuyền buồm kiểu châu Âu, cờ hiện đại. "
          "**Cọc:** cả thân cây lim dày 20–30 cm, dài 2,5–3 m, đầu bịt sắt (theo *Toàn thư*), nhiều người dùng vồ gỗ nặng "
          "đóng lúc triều rút; không que nhỏ, không búa tay. **Ngô Quyền chỉ thấy từ phía sau.**")

EPISODES = [
    dict(
        slug="canh-con-nuoc-bach-dang-938", prefix="bd938n",
        length=("**YouTube** đủ 6 cảnh, khoảng 58 giây; **TikTok** 5 cảnh giữ trọn câu thoại, khoảng 46 giây (bỏ cảnh 3)"),
        muc={"youtube": (45, 60), "tiktok": (40, 50)}, tiktok_canh=[1, 2, 4, 5, 6],
        voices={"officer": "a gruff, clipped male voice in his 40s, short commands",
                "Ngô Quyền": "a low, steady, authoritative male voice around 40, few words, never shouting"},
        title="Bị sai ngồi canh một cây sào giữa bãi bùn, cả ngày khắc mực nước, không ai nói để làm gì (Bạch Đằng, 938)",
        history=("**Lịch sử:** năm 938, quân Nam Hán do Hoằng Tháo chỉ huy theo đường biển sang. Ngô Quyền cho **đóng cọc lớn "
                 "đầu bịt sắt** ở cửa sông Bạch Đằng, **lợi dụng thủy triều**: khi triều lên, dùng thuyền nhẹ nhử thuyền giặc "
                 "vào; khi triều rút, cọc nhô lên, thuyền giặc mắc cọc, vỡ đắm, quân ta đánh mạnh, quân Nam Hán thua to, Hoằng "
                 "Tháo tử trận (*Đại Việt sử ký toàn thư*, mức B; chi tiết cọc đầu bịt sắt theo *Toàn thư*). Chiến thắng chấm "
                 "dứt hơn một nghìn năm Bắc thuộc; năm 939 Ngô Quyền xưng vương. **Cỡ cọc** theo các bãi cọc khai quật (của "
                 "trận 1288, mức ước lượng). **Hư cấu:** Anh Tư canh con nước, cây sào khắc vạch và mọi lời thoại. Cái chết "
                 "chỉ ghi ở đây, phim không dựng cảnh chết."),
        setting=SETTING,
        visual=VISUAL,
        hook="POV: Cả ngày / ngồi canh / một cây sào",
        end="Follow để xem / thêm chuyện / Đại Việt →",
        end_secs=1.6,
        clips=[
            dict(name="Cây sào", label="Cửa sông Bạch Đằng · 938",
                 img=f"First-person view on a wide muddy riverbank at low tide, a gruff officer handing {FACE} a tall bamboo pole and a small knife, the brown river and limestone hills behind, realistic, vertical 9:16.",
                 vid=("0-5s: The officer hands Anh Tư a tall bamboo pole and a knife: \"Cắm sào ra bãi. Nước lên xuống thế nào, "
                      "khắc vào.\" Anh Tư: \"Khắc nước... để làm gì ạ?\" The officer: \"Để cả quân khỏi phải đoán.\" 5-10s: Anh Tư "
                      "looks at the other soldiers carrying spears and says quietly: \"Người ta cầm giáo... em cầm cây sào.\""),
                 subs=[(0.3, 2.2, "Cắm sào ra bãi. / Nước lên xuống thế nào, / khắc vào."), (2.2, 3.4, "Khắc nước... / để làm gì ạ?"),
                       (3.4, 4.9, "Để cả quân / khỏi phải đoán."), (5.2, 9.5, "Người ta cầm giáo... / em cầm cây sào.")]),
            dict(name="Cọc mọc theo nước", label="",
                 img=f"First-person view at low tide on the mudflat, teams of men driving massive ironwood stakes with iron-capped tips into the riverbed with a heavy wooden ram on ropes, {FACE} in the foreground cutting a notch into his bamboo pole, realistic, vertical 9:16.",
                 vid=("0-5s: At low tide, teams of men lift a heavy wooden ram on ropes and drop it on a massive iron-capped "
                      "stake; thud after thud; rows of stakes rise from the mud. Anh Tư cuts a notch at the waterline on his "
                      "pole. 5-10s: He says quietly to the viewer: \"Nước rút đến đâu... người ta đóng cọc đến đấy.\""),
                 subs=[(0.5, 4.8, "Một, hai... thả!"), (5.0, 9.5, "Nước rút đến đâu... / người ta đóng cọc / đến đấy.")]),
            dict(name="Nước lên che cọc", label="",
                 img=f"First-person view at night by torchlight as the rising tide slowly covers the rows of stakes until only dark water remains, {FACE} standing waist-deep holding his notched bamboo pole, realistic, vertical 9:16.",
                 vid=("0-5s: Night; the tide rises and slowly swallows the rows of stakes until only smooth dark water is left. "
                      "5-10s: Anh Tư, waist-deep, cuts another notch: \"Nước lên che hết cọc... chỉ còn cây sào của em.\""),
                 subs=[(5.0, 9.5, "Nước lên che hết cọc... / chỉ còn cây sào của em.")]),
            dict(name="Bao giờ nước rút", label="",
                 img=f"First-person view at dawn on the riverbank, {NGO} standing beside {FACE}'s notched bamboo pole and looking at the water, Anh Tư standing very straight, nervous, realistic, vertical 9:16.",
                 vid=("0-5s: At dawn Ngô Quyền, seen only from behind, stops beside the pole and asks in a low voice: \"Bao giờ "
                      "nước rút?\" Anh Tư points to a notch: \"Bẩm... quá trưa ạ.\" Ngô Quyền nods once and walks away. 5-10s: "
                      "Anh Tư lets out a breath and says quietly to the viewer: \"Cả đạo quân chờ... một vạch khắc của em.\""),
                 subs=[(0.5, 2.2, "Bao giờ nước rút?"), (2.2, 4.8, "Bẩm... / quá trưa ạ."),
                       (5.0, 9.5, "Cả đạo quân chờ... / một vạch khắc của em.")]),
            dict(name="Thuyền giặc vào", label="",
                 img=f"First-person view from the reeds at high tide, a fleet of tall multi-deck warships with plain red banners entering the river mouth chasing a few small light boats, the stakes hidden under the water, {FACE} gripping his pole and watching the waterline, realistic, vertical 9:16.",
                 vid=("0-5s: High tide; a few small boats row away upriver; the tall warships with plain red banners chase them "
                      "into the river mouth, right over the hidden stakes. 5-10s: Anh Tư watches the waterline at his notch and "
                      "whispers: \"Nước đang lên... thuyền nó vào đúng lúc em khắc.\""),
                 subs=[(5.0, 9.5, "Nước đang lên... / thuyền nó vào / đúng lúc em khắc.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at midday as the tide falls, a forest of iron-capped stakes emerging from the water, tall warships tilting and stuck among them, many small Vietnamese boats closing in, {FACE} in the foreground pulling his bamboo pole out of the mud, no bodies, realistic, vertical 9:16.",
                 vid=("0-5s: The water drops below the notch; a forest of iron-capped stakes rises; the tall warships lurch and "
                      "stick fast, timber cracking; war drums on both banks; small boats close in. No bodies, no blood. A calm "
                      "narrator's voice says: \"Năm 938, Ngô Quyền tính con nước, cắm cọc ở cửa sông Bạch Đằng. Triều rút, thuyền "
                      "Nam Hán mắc cọc. Hơn một nghìn năm Bắc thuộc chấm dứt.\" 5-10s: Anh Tư pulls his pole out of the mud and "
                      "says quietly to the camera: \"Cả trận đánh... em chỉ ngồi nhìn nước.\""),
                 subs=[(0.3, 4.8, "Năm 938, Ngô Quyền / tính con nước, cắm cọc. / Hơn nghìn năm Bắc thuộc / chấm dứt."),
                       (5.0, 8.4, "Cả trận đánh... / em chỉ ngồi nhìn nước.")]),
        ],
        caption=("Bị sai ngồi canh một cây sào giữa bãi bùn, cả ngày khắc mực nước, không ai nói để làm gì 🌊 Năm 938, Ngô Quyền "
                 "tính đúng con nước: triều lên nhử thuyền giặc vào, triều rút cọc nhô lên. Bạn có biết cọc thật to cỡ nào "
                 "không? 👇"),
        tags="#bachdang #ngoquyen #938 #lichsuvietnam #thuytrieu",
        tt_title="Bị sai ngồi canh một cây sào giữa bãi bùn, cả ngày khắc mực nước",
        hooks_alt=["POV: Cả đạo quân chờ / một vạch khắc của em", "POV: Người ta cầm giáo / em cầm cây sào"],
        pin=("Cọc trận 938 là cả thân cây lim, đầu bịt sắt theo Toàn thư 🔥 Còn thủy triều ở cửa Bạch Đằng lên xuống mấy lần một "
             "ngày, bạn biết không? Follow để xem thêm chuyện Đại Việt!"),
        yt_title="Bạch Đằng 938: người canh con nước cho Ngô Quyền | POV lịch sử",
        yt_tags=("bạch đằng 938, ngô quyền, thủy triều, cọc bạch đằng, cọc bịt sắt, nam hán, hoằng tháo, chấm dứt bắc thuộc, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#povlichsu #anhtu", note=("**Bản mới 45–60 giây** (22/11/2026), viết lại theo mọi "
          "tiêu chuẩn đã bổ sung. Góc kể mới: Anh Tư canh con nước, khác video \"cắm cọc cả buổi sáng\" đã đăng."),
          unit="Bản mới", file_unit="ban-moi")
