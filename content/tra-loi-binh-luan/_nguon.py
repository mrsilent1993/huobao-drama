#!/usr/bin/env python3
"""Video trả lời bình luận: biến lời chê dưới các video cũ thành nội dung mới. Sửa ở đây rồi chạy: python3 _nguon.py

Đăng bằng tính năng "Trả lời bằng video" của TikTok để bình luận gốc hiện ngay trên video.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, hair in a topknot, a scar across his left eyebrow and a "
        "wide grin with a chipped front tooth, very expressive face")

NOTE = ("**Video trả lời bình luận:** Anh Tư nói thẳng với người xem, nhận lỗi một cách hài hước, rồi đưa thông tin "
        "thật. Đăng bằng **\"Trả lời bằng video\"** ngay dưới bình luận được chọn để bình luận gốc hiện trên video.")

EPISODES = [
    dict(
        slug="coc-bach-dang-that-to-co-nao", prefix="tl1",
        title="Trả lời bình luận: \"Cọc Bạch Đằng thật to cỡ nào?\"",
        length=("hai video từ cùng 5 clip: **bản dài** (YouTube, khoảng 48 giây) và **bản ngắn** (TikTok, khoảng 38 giây) "
                "vẫn đủ cả 5 cảnh"),
        history=("**Trả lời bình luận nào:** video \"Cắm cọc cả buổi sáng…\" (Bạch Đằng 938, 1,7 triệu lượt xem) có khoảng "
                 "30 bình luận chê cọc nhỏ. Nên trả lời bình luận **\"Cái cọc nó to như cột đình mà mấy con AI làm quả cọc "
                 "để xỉa răng hả =))\"** (vui, khớp ngay cảnh mở đầu). Bình luận dự phòng: \"Cọc bé thế kia thì đâm chìm "
                 "tàu kiểu gì, trong sách viết cọc gỗ to như cột nhà…\".\n\n"
                 "**Số liệu dùng trong video (báo chí trích các đợt khai quật; số liệu giữa các nguồn có chênh lệch):**\n\n"
                 "- **Bãi cọc Yên Giang** (thị xã Quảng Yên, Quảng Ninh): cọc chủ yếu là gỗ lim, gỗ táu, dài khoảng "
                 "2,6–2,8 m, đường kính 20–30 cm, phần mũi vót nhọn dài 0,5–1 m, các cọc cách nhau khoảng 0,9–1,5 m "
                 "([Báo Quảng Ninh](https://baoquangninh.vn/nhung-chiec-coc-go-lam-nen-chien-thang-bach-dang-lich-su-2303153.html), "
                 "[Tiền Phong](https://tienphong.vn/bai-coc-bach-dang-tro-thanh-di-tich-quoc-gia-dac-biet-post595084.tpo)).\n"
                 "- **Bãi cọc Cao Quỳ** (Thủy Nguyên, Hải Phòng), phát lộ gần đây: có cọc đường kính 37–40 cm, dài khoảng "
                 "3–4 m, niên đại đo được 1270–1430 "
                 "([Pháp luật Plus](https://phapluatplus.baophapluat.vn/bai-coc-gan-nghin-nam-tuoi-vua-phat-lo-co-the-lam-dao-lon-nhan-thuc-tran-thuy-chien-bach-dang-139134.html), "
                 "[Báo Lạng Sơn](https://baolangson.vn/phat-lo-bai-coc-gan-nghin-nam-tuoi-ben-song-bach-dang-1259359.html)).\n"
                 "- **Các bãi cọc đã khai quật là của trận năm 1288.** Bãi cọc trận năm 938 đến nay chưa tìm thấy. Cọc năm 938 "
                 "\"đầu bịt sắt\" là theo *Đại Việt sử ký toàn thư*; cọc 1288 khai quật được không thấy bịt sắt.\n"
                 "- Các bãi cọc nằm ở vùng bãi triều, lạch sông gần bờ thời đó, nay đã thành ruộng, đầm.\n\n"
                 "Cách đóng cọc thời xưa **chưa có kết luận chắc chắn**. Video chỉ nói \"nhiều người cùng làm, lúc nước ròng\", "
                 "không khẳng định cách nào. **Hư cấu:** Anh Tư và mọi lời thoại."),
        setting=("Vietnam, the Bạch Đằng river area at low tide: a wide muddy tidal flat beside mangroves, limestone hills "
                 "in the mist. Massive ironwood stakes lie on the mud or stand planted in rows: whole tree trunks about 20 "
                 "to 30 cm thick (as thick as a man's thigh), 2.6 to 2.8 m long, with long sharpened tips, NO iron caps. "
                 f"Anh Tư is {FACE}, shirtless with a brown cloth around his waist, muddy, talking straight to the camera "
                 "like a friendly vlogger. Villagers and soldiers of the Trần era in brown clothes with topknots and "
                 "black-lacquered teeth. No flags, no visible writing, no modern objects."),
        hook="Cọc Bạch Đằng / thật to cỡ nào?",
        end="Cảm ơn các bác đã góp ý! / Follow để xem cọc to / trong các tập sau →",
        end_secs=1.6,
        clips=[
            dict(name="Cọc xỉa răng", label="Trả lời bình luận",
                 img=f"First-person view on a muddy riverbank, {FACE} holding up a thin wooden twig no bigger than a chopstick and pretending to pick his teeth with it, grinning sheepishly at the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư holds up a thin wooden twig no bigger than a chopstick, pretends to pick his teeth with "
                      "it and says to the camera: \"Các bác bảo cọc nhà em... để xỉa răng.\" 5-10s: He tosses the twig "
                      "away, scratches his head and grins: \"Các bác nói đúng! Để em cho xem cọc thật.\""),
                 subs=[(0.5, 4.8, "Các bác bảo cọc nhà em... / để xỉa răng."),
                       (5.0, 9.5, "Các bác nói đúng! / Để em cho xem cọc thật.")]),
            dict(name="Cọc thật", tiktok="0-5", label="Bãi cọc Yên Giang",
                 img=f"First-person view on a tidal mudflat, a massive sharpened ironwood stake about 2.7 m long and thigh-thick lying on the mud, {FACE} lying down beside it to compare, the stake much longer than him, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư lies down on the mud beside a massive sharpened ironwood stake to compare: the stake is "
                      "much longer than he is. He says: \"Cọc thật dài gần ba mét, to bằng bắp đùi em.\" 5-10s: He "
                      "knocks on it with his knuckles: \"Gỗ lim đấy. Nặng như... cả nhà em cộng lại.\""),
                 subs=[(0.3, 4.8, "Yên Giang: dài 2,6–2,8 m, / to 20–30 cm, gỗ lim, gỗ táu."),
                       (5.0, 9.5, "Gỗ lim đấy. Nặng như... / cả nhà em cộng lại.")]),
            dict(name="Cọc to nhất", tiktok="5-10", label="Bãi cọc Cao Quỳ",
                 img=f"First-person view on a tidal flat, an enormous stake about 4 m tall and 40 cm thick standing upright, {FACE} standing beside it, the stake more than twice his height, looking up with his mouth open, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư walks up to an enormous upright stake, about four metres tall and forty centimetres "
                      "thick, and looks up and up. 5-10s: He turns to the camera, stunned: \"Cái này cao gấp đôi em... mà "
                      "người ta còn cắm được xuống bùn!\""),
                 subs=[(0.3, 4.8, "Bãi cọc Cao Quỳ: có cọc / đường kính gần 40 cm, / dài 3–4 m."),
                       (5.0, 9.5, "Cao gấp đôi em... mà người ta / còn cắm được xuống bùn!")]),
            dict(name="Cắm thế nào", label="Lúc nước ròng",
                 img=f"First-person view on a wide tidal mudflat at low tide, a team of about ten men in brown clothes working together to raise and plant a huge stake in the mud, rows of stakes about one metre apart behind them, {FACE} among them, pulling a rope, realistic, vertical 9:16.",
                 vid=("0-5s: At low tide, a team of about ten men works together with ropes to raise a huge stake and set "
                      "it deep in the mud; behind them, rows of stakes stand about a metre apart. 5-10s: Anh Tư, pulling a "
                      "rope, says to the camera: \"Một cọc... cả chục người. Cách nhau chừng một mét, thuyền nào vào là "
                      "mắc.\""),
                 subs=[(0.3, 4.8, "Cọc cắm ở bãi triều gần bờ, / lúc nước ròng, nhiều người / cùng làm. Cách nhau 0,9–1,5 m."),
                       (5.0, 9.5, "Một cọc... cả chục người. / Thuyền nào vào là mắc.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunset on the tidal flat, rows of massive stakes standing in the mud with the tide coming in, {FACE} leaning on one stake, grinning at the camera, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset; the tide creeps in around rows of massive stakes. A calm narrator's voice says: \"Bãi "
                      "cọc tìm được là của trận năm 1288. Bãi cọc năm 938 đến nay vẫn chưa ai tìm thấy.\" 5-10s: Anh Tư "
                      "leans on a huge stake and grins at the camera: \"Cọc to rồi đấy nhé... lần này các bác đừng chê "
                      "nữa!\""),
                 subs=[(0.3, 4.8, "Bãi cọc tìm được / là của trận 1288. Bãi cọc / năm 938 chưa tìm thấy."),
                       (5.0, 8.4, "Cọc to rồi đấy nhé... / lần này các bác đừng chê nữa!")]),
        ],
        caption=("Các bác nói đúng, cọc lần trước bé quá 😅 Cọc thật ở bãi cọc Yên Giang dài 2,6–2,8 m, to 20–30 cm, gỗ lim, "
                 "gỗ táu; bãi cọc Cao Quỳ có cọc to gần 40 cm, dài 3–4 m. Lưu ý: các bãi cọc đã tìm thấy là của trận 1288, "
                 "bãi cọc năm 938 vẫn chưa tìm ra. Bạn đã đến xem bãi cọc ở Quảng Yên chưa? 👇"),
        tags="#baicocbachdang #bachdang #coclim #khaoco #traloibinhluan",
        tt_title="Các bác bảo cọc Bạch Đằng bé như que xỉa răng: cọc thật to cỡ này",
        hooks_alt=["Cọc Bạch Đằng thật / to cỡ nào?", "Các bác bảo / cọc để xỉa răng"],
        pin=("Số liệu theo các đợt khai quật bãi cọc Yên Giang và Cao Quỳ (các nguồn có chênh lệch) 📏 Cọc thật đang trưng "
             "bày ở khu di tích bãi cọc Bạch Đằng (Quảng Yên) và Bảo tàng Lịch sử quốc gia. Ai đã xem tận mắt rồi? 👇"),
        yt_title="Cọc Bạch Đằng thật to cỡ nào? Trả lời các bác chê \"cọc xỉa răng\"",
        yt_tags=("bãi cọc bạch đằng, cọc bạch đằng, yên giang, cao quỳ, khảo cổ, gỗ lim, trận bạch đằng, 1288, 938, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#anhtu", note=NOTE, unit="Video", file_unit="video")
