#!/usr/bin/env python3
"""Loạt "Làm thuê cho quan đô hộ" (thời Bắc thuộc). Sửa ở đây rồi chạy: python3 _nguon.py

Công thức Anh Tư: người thường bị giao việc vô lý, không ai giải thích, có câu đáng gửi bạn bè, vỡ lẽ ở cuối.
Giọng hài nhắm vào VIỆC VÔ LÝ và QUAN THAM, không bêu riếu dân tộc nào. Trang phục theo
../nghien-cuu/chuan-hinh-anh-quan-doi.md (các mục thời Bắc thuộc là ⚠️ hiểu biết chung).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
NO_TEXT = ("No visible writing or characters on clothes, documents, signboards or banners; no flags; no European "
           "clothing or armor.")
LOCAL = ("local Giao Chỉ people with short-cut hair or simple topknots, black-lacquered teeth, barefoot, in plain "
         "undyed or brown wrap clothes")
HAN = ("Han dynasty officials in dark wide-sleeved robes with a sash and black cloth caps, guards with long spears "
       "in simple dark tunics")
TANG = ("Tang dynasty officials in round-collared robes (red, green or blue by rank) with black futou hats and leather "
        "belts, guards in Tang-style lamellar armor")
VIS_HAN = ("**Chuẩn hình ảnh (⚠️ hiểu biết chung, xem `../nghien-cuu/chuan-hinh-anh-quan-doi.md`):** quan nhà Hán mặc áo "
           "rộng tay sẫm màu, thắt đai, đội mũ vải đen; dân Giao Chỉ tóc cắt ngắn hoặc búi, răng đen, chân đất, áo vải "
           "trơn quấn quanh người. Không có chữ trên giấy tờ, biển hay áo; không cờ.")
VIS_TANG = ("**Chuẩn hình ảnh (⚠️ hiểu biết chung, xem `../nghien-cuu/chuan-hinh-anh-quan-doi.md`):** quan nhà Đường mặc "
            "áo cổ tròn (màu theo phẩm hàm), đội mũ phốc đầu đen, đeo đai da; lính mặc giáp vảy kiểu Đường; dân bản "
            "địa răng đen, chân đất, áo vải nâu. Không có chữ trên giấy tờ, biển hay áo; không cờ.")

NOTE = ("**Làm thuê cho quan đô hộ:** loạt thời Bắc thuộc theo công thức Anh Tư (sẹo ngang lông mày trái, răng cửa "
        "mẻ, cười toe; ảnh tham chiếu trong `../bach-dang/README.md`). Câu đùa nhắm vào việc vô lý và quan tham, "
        "không nhắm vào dân tộc nào. **Bản TikTok 30 giây** gồm clip 1, 3, 5; **bản YouTube 50 giây** gồm đủ 5 clip.")

END = "Sử không ghi tên Anh Tư. / Follow để xem Anh Tư / làm thuê cho quan đô hộ →"

EPISODES = [
    # ------------------------------------------------------------------ năm 105
    dict(
        slug="cho-vai-hoa-toc-105", prefix="bt105",
        title="Bị bắt chạy tiếp sức chở một giỏ hàng hỏa tốc lên kinh đô, mở ra mới biết là... quả vải (năm 105)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** thời Đông Hán, vùng Lĩnh Nam (trong đó có Giao Chỉ) phải cống vải và nhãn tươi lên kinh "
                 "đô Lạc Dương. Để quả còn tươi, triều đình đặt \"mười dặm một trạm, năm dặm một chốt\", người và ngựa "
                 "chạy tiếp sức ngày đêm qua núi hiểm, người phu chết nối nhau trên đường. Năm Nguyên Hưng thứ nhất "
                 "(105), quan huyện Lâm Vũ là Đường Khương dâng sớ can; vua Hán Hòa Đế bãi lệ cống (*Hậu Hán thư*, mức "
                 "A). **Hư cấu:** Anh Tư, người đưa thư, cảnh kiểm từng quả và mọi lời thoại. Chuyện người phu chết chỉ "
                 "nhắc bằng lời trong phần lịch sử, không dựng thành cảnh."),
        setting=("Southern China and northern Vietnam around the year 100: a steep mountain relay road through jungle, "
                 "small wooden relay stations with tired horses, baskets of fresh lychees and longans wrapped in leaves. "
                 f"{HAN}. {LOCAL}. Anh Tư is {FACE}, a relay runner in a plain brown wrap shirt with a cloth head band, "
                 f"barefoot. {NO_TEXT}"),
        visual=VIS_HAN,
        hook="POV: Chạy tiếp sức / chở hàng hỏa tốc / lên kinh đô",
        end=END,
        clips=[
            dict(name="Hàng hỏa tốc", label="Lĩnh Nam · khoảng năm 100",
                 img=f"First-person view at a small wooden relay station on a jungle mountain road, a Han official in a dark wide-sleeved robe pushing a lidded basket into the arms of {FACE}, a tired horse behind, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is a Han official in a dark wide-sleeved robe and black cloth cap; "
                      "the RECEIVER is Anh Tư, a barefoot relay runner in a plain brown wrap shirt. 0-5s: The official shoves "
                      "a lidded basket into Anh Tư's arms: \"Mười dặm một trạm, năm dặm một chốt. Quả hỏng là phạt.\" "
                      "5-10s: Anh Tư lifts the lid, stares inside at fresh lychees, then at the viewer: \"Hàng hỏa tốc... "
                      "là quả vải ạ?\""),
                 subs=[(0.5, 4.8, "Mười dặm một trạm, / năm dặm một chốt. / Quả hỏng là phạt."),
                       (5.0, 9.5, "Hàng hỏa tốc... / là quả vải ạ?")]),
            dict(name="Ngồi kiệu", tiktok="bo", label="",
                 img=f"First-person view running on a steep jungle path holding a lidded basket carefully with both arms, {FACE} running ahead, sweating, a tired horse resting at a station in the distance, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư sprints barefoot up a steep jungle path, holding the basket level like something precious; "
                      "behind them a horse rests at a station. 5-10s: Panting, he says to the viewer: \"Ngựa được nghỉ, "
                      "người phải chạy... còn quả vải thì ngồi kiệu.\""),
                 subs=[(5.0, 9.5, "Ngựa được nghỉ, / người phải chạy... còn / quả vải thì ngồi kiệu.")]),
            dict(name="Nhanh hơn người đưa thư", label="",
                 img=f"First-person view on a mountain road, {FACE} sprinting past a slow official courier who carries rolled letters on his back and stares in shock, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư sprints past a slow official courier walking with a bundle of rolled letters; the courier "
                      "stops and stares. 5-10s: Anh Tư glances back over his shoulder and shouts, laughing: \"Quả vải "
                      "đi nhanh hơn cả thư của quan!\""),
                 subs=[(0.5, 4.8, "Tránh ra! Hàng của vua!"),
                       (5.0, 9.5, "Quả vải đi nhanh hơn / cả thư của quan!")]),
            dict(name="Kiểm từng quả", tiktok="bo", label="Trạm tiếp theo",
                 img=f"First-person view at a relay station in the rain, a Han official inspecting lychees one by one and holding up a bruised one, {FACE} soaked and panting beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: In the rain, the official inspects the lychees one by one and holds up a slightly bruised one: "
                      "\"Quả này dập. Phạt.\" 5-10s: Anh Tư, soaked and panting, whispers to the viewer: \"Người dập cả "
                      "rồi... mà chỉ đếm quả dập.\""),
                 subs=[(0.5, 4.8, "Quả này dập. Phạt."),
                       (5.0, 9.5, "Người dập cả rồi... / mà chỉ đếm quả dập.")]),
            dict(name="Ghi tên em vào sử", label="Năm 105",
                 img=f"First-person view at a relay station at sunset, an official reading an order to the runners, baskets put down on the ground, {FACE} sitting down on a step for the first time, stretching his legs with a huge chipped-tooth grin, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset; an official reads out an order (no visible text) and the runners put their baskets down. "
                      "A calm narrator's voice says: \"Năm 105, quan huyện Đường Khương dâng sớ can. Vua Hán bãi lệ cống "
                      "vải, nhãn.\" 5-10s: Anh Tư finally sits down on a step, stretches his legs and grins at the camera: "
                      "\"Từ nay quả vải... tự đi bộ! Ghi tên em vào sử nhé!\""),
                 subs=[(0.3, 4.8, "Năm 105, quan huyện / Đường Khương dâng sớ can. / Vua Hán bãi lệ cống vải."),
                       (5.0, 9.8, "Từ nay quả vải... tự đi bộ! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Bị bắt chạy tiếp sức chở một giỏ hàng hỏa tốc lên kinh đô, mở ra mới biết là... quả vải 🍒 Thời Đông Hán, "
                 "vải nhãn phương Nam phải chạy trạm ngày đêm lên Lạc Dương, \"mười dặm một trạm, năm dặm một chốt\". "
                 "Năm 105, một quan huyện dâng sớ can và vua bãi lệ cống (Hậu Hán thư). Ship hỏa tốc thời nay có nhanh "
                 "bằng không? 👇"),
        tags="#lamthuequandoho #bacthuoc #quavai #hauhanthu #nam105",
        tt_title="Chạy tiếp sức chở hàng hỏa tốc lên kinh đô, mở ra mới biết là quả vải",
        hooks_alt=["POV: Quả vải / đi nhanh hơn người", "POV: Ship hỏa tốc / từ năm 105"],
        pin=("Sử chép: mười dặm một trạm, năm dặm một chốt, chỉ để vua ăn vải tươi 😳 Bạn đoán chạy từ phương Nam lên "
             "Lạc Dương mất bao lâu? Follow để xem Anh Tư làm thuê cho quan đô hộ!"),
        yt_title="Năm 105: chạy tiếp sức chở hàng hỏa tốc lên kinh đô... hàng là quả vải",
        yt_tags=("bắc thuộc, cống vải, quả vải, hậu hán thư, đường khương, lĩnh nam, giao chỉ, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ năm 541
    dict(
        slug="xin-viec-thua-cai-ho-541", prefix="bt541",
        title="Đi theo một ông đồ giỏi lên kinh đô xin làm quan, bị loại chỉ vì... cái họ (Tinh Thiều, khoảng năm 541)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** theo *Đại Việt sử ký toàn thư* (mức B), Tinh Thiều người Giao Châu, giỏi văn, sang kinh "
                 "đô nhà Lương xin được bổ làm quan. Thượng thư bộ Lại Sái Tôn chê họ Tinh xưa nay không có ai danh giá, "
                 "chỉ cho làm Quảng Dương môn lang (chức coi cổng). Tinh Thiều xấu hổ, bỏ về theo Lý Bí. Năm 541 Lý Bí "
                 "khởi nghĩa; năm 544 lên ngôi, đặt quốc hiệu Vạn Xuân, cho Tinh Thiều đứng đầu hàng quan văn. **Hư "
                 "cấu:** Anh Tư theo hầu, viên thư lại tra sổ họ, cảnh ở cổng thành và mọi lời thoại."),
        setting=("Kiến Khang (the capital of the Liang dynasty in southern China), around 540: a government office hall "
                 "with wooden pillars and rows of waiting candidates, a city gate with heavy wooden doors. Liang officials "
                 "in wide-sleeved robes with black lacquered gauze caps. Tinh Thiều is a thin, refined Vietnamese scholar "
                 "around 30 with a short beard, in a plain grey scholar's robe, carrying rolled scrolls. "
                 f"Anh Tư is {FACE}, his attendant in a plain brown tunic carrying a scroll box. {NO_TEXT}"),
        visual=("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** quan nhà Lương mặc áo rộng tay, đội mũ sa đen; ông đồ Tinh "
                "Thiều mặc áo nho sinh xám trơn; không có chữ trên cuộn văn, sổ sách hay biển; không cờ."),
        hook="POV: Đi xin việc / bị loại / vì cái họ",
        end=END,
        clips=[
            dict(name="Văn hay", label="Kinh đô nhà Lương · năm 540",
                 img=f"First-person view in a crowded government waiting hall with rows of candidates, a thin refined Vietnamese scholar in a grey robe holding scrolls and smiling calmly, {FACE} beside him holding a scroll box proudly, realistic, vertical 9:16.",
                 vid=("0-5s: In the crowded waiting hall, Anh Tư pats the scroll box and whispers to the viewer: \"Văn anh "
                      "Thiều hay nhất xứ Giao Châu, kiểu gì cũng làm quan to!\" 5-10s: Tinh Thiều smiles modestly: "
                      "\"Người ta tuyển người tài mà.\""),
                 subs=[(0.5, 4.8, "Văn anh Thiều hay nhất / xứ Giao Châu, kiểu gì / cũng làm quan to!"),
                       (5.0, 9.5, "Người ta tuyển / người tài mà.")]),
            dict(name="Tra họ", tiktok="bo", label="",
                 img=f"First-person view at a clerk's desk with a huge thick register book, a clerk running his finger down the pages and frowning, the scholar waiting, {FACE} leaning in, realistic, vertical 9:16.",
                 vid=("0-5s: A clerk asks without looking up: \"Họ gì?\" \"Họ Tinh.\" He flips through a huge register, "
                      "frowning: \"Họ Tinh... chưa có ai làm quan to.\" 5-10s: Anh Tư whispers to the viewer: \"Tra họ "
                      "trước... đọc văn sau ạ?\""),
                 subs=[(0.5, 4.8, "Họ Tinh... / chưa có ai làm quan to."),
                       (5.0, 9.5, "Tra họ trước... / đọc văn sau ạ?")]),
            dict(name="Thua cái họ", label="",
                 img=f"First-person view in an audience hall, a senior official in a wide-sleeved robe waving his hand dismissively without reading the scrolls, the scholar's face falling, {FACE} beside the viewer stunned, realistic, vertical 9:16.",
                 vid=("0-5s: The senior official glances at the unopened scrolls, waves his hand: \"Cho làm... coi cổng "
                      "thành.\" Tinh Thiều's face falls. 5-10s: Anh Tư whispers to the viewer: \"Giỏi cỡ nào... cũng "
                      "thua cái họ.\""),
                 subs=[(0.5, 4.8, "Cho làm... / coi cổng thành."),
                       (5.0, 9.5, "Giỏi cỡ nào... / cũng thua cái họ.")]),
            dict(name="Coi cổng", tiktok="bo", label="Mấy hôm sau",
                 img=f"First-person view at a heavy wooden city gate at dawn, the thin scholar in a gatekeeper's plain tunic pushing the door open, officials in robes walking in past him, {FACE} beside him holding a big key, realistic, vertical 9:16.",
                 vid=("0-5s: At dawn the scholar, now in a gatekeeper's tunic, pushes open the heavy gate; well-dressed "
                      "officials walk in past him without a glance. 5-10s: Anh Tư whispers: \"Anh mở cổng cho người ta vào "
                      "làm quan... còn anh đứng ngoài.\" Tinh Thiều takes the big key from Anh Tư, sets it down gently and "
                      "says: \"Về quê.\""),
                 subs=[(0.5, 4.8, "Anh mở cổng cho người ta / vào làm quan... / còn anh đứng ngoài."),
                       (5.0, 9.5, "Về quê.")]),
            dict(name="Ghi tên em vào sử", label="Năm 544",
                 img=f"First-person view in a simple wooden palace hall in Giao Châu, a new king seen from behind on a plain throne, the thin scholar now in a dignified official robe standing first among the officials, {FACE} beside the viewer grinning, realistic, vertical 9:16.",
                 vid=("0-5s: In a simple wooden palace hall, officials bow to a new king seen only from behind; the scholar, "
                      "now in a dignified robe, stands at the head of the civil officials. A calm narrator's voice says: "
                      "\"Tinh Thiều bỏ về theo Lý Bí. Năm 544, Lý Bí lập nước Vạn Xuân, Tinh Thiều đứng đầu hàng quan văn.\" "
                      "5-10s: Anh Tư grins at the camera: \"Ông thượng thư ấy chắc giờ tiếc lắm! Ghi tên em vào sử nhé!\""),
                 subs=[(0.3, 4.8, "Tinh Thiều về theo Lý Bí. / Năm 544, nước Vạn Xuân ra đời, / Tinh Thiều đứng đầu quan văn."),
                       (5.0, 9.8, "Ông thượng thư ấy / chắc giờ tiếc lắm! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Đi theo một ông đồ giỏi lên kinh đô xin làm quan, bị loại chỉ vì... cái họ 😤 Sử chép Tinh Thiều giỏi "
                 "văn mà chỉ được cho làm chức coi cổng vì \"họ Tinh không ai danh giá\". Ông bỏ về theo Lý Bí, rồi đứng "
                 "đầu hàng quan văn nước Vạn Xuân. Bạn đã bao giờ bị loại vì lý do vô lý chưa? 👇"),
        tags="#lamthuequandoho #bacthuoc #tinhthieu #lybi #vanxuan",
        tt_title="Đi xin làm quan bị loại chỉ vì cái họ, ông đồ bỏ về... lập nước",
        hooks_alt=["POV: Giỏi cỡ nào / cũng thua cái họ", "POV: Tra họ trước / đọc văn sau"],
        pin=("Năm 544, nước Vạn Xuân ra đời, và người bị chê \"họ không danh giá\" đứng đầu hàng quan văn 😏 Bạn đã bao "
             "giờ bị đánh giá qua cái tên chưa? Follow để xem Anh Tư làm thuê cho quan đô hộ!"),
        yt_title="Xin làm quan bị loại vì cái họ, ông đồ về giúp lập nước Vạn Xuân",
        yt_tags=("tinh thiều, lý bí, lý nam đế, nước vạn xuân, bắc thuộc, nhà lương, lịch sử việt nam, pov lịch sử, "
                 "anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ năm 687
    dict(
        slug="thue-gap-doi-687", prefix="bt687",
        title="Đang nộp nửa thuế bỗng bị bắt nộp gấp đôi, cả làng đứng dậy (Lý Tự Tiên, Đinh Kiến, năm 687)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** dân bản địa ở An Nam đô hộ phủ thời Đường vốn chỉ phải nộp nửa mức thuế. Năm 687, đô hộ Lưu "
                 "Diên Hựu bắt nộp đủ, tức gấp đôi. Dân oán; Lý Tự Tiên mưu nổi dậy, rồi Đinh Kiến tập hợp dân vây phủ thành "
                 "Tống Bình (Hà Nội ngày nay), Lưu Diên Hựu bị giết (*Đại Việt sử ký toàn thư*, sử nhà Đường cũng chép, mức "
                 "B). **Hư cấu:** Anh Tư, chiếc cân, buổi họp đêm và mọi lời thoại. Không dựng cảnh giao tranh hay chết chóc."),
        setting=("Tống Bình (Hanoi), year 687, under the Tang: a dusty tax yard in front of a wooden government building, "
                 "a big wooden balance scale, sacks and baskets of rice, a village with thatched houses and a banyan "
                 f"tree. {TANG}. Local farmers with black-lacquered teeth, barefoot, in brown clothes. Anh Tư is {FACE}, "
                 f"a farmer in a patched brown shirt. {NO_TEXT}"),
        visual=VIS_TANG,
        hook="POV: Lương không tăng / thuế tăng gấp đôi",
        end=END,
        clips=[
            dict(name="Nộp đủ", label="Tống Bình · năm 687",
                 img=f"First-person view in a dusty tax yard, a Tang official in a green round-collared robe and black futou hat announcing to a crowd of farmers, {FACE} beside the viewer holding a basket of rice, frowning, realistic, vertical 9:16.",
                 vid=("0-5s: The official announces to the crowd: \"Từ năm nay, nộp đủ thuế. Không còn nộp nửa nữa.\" "
                      "5-10s: Anh Tư, holding his basket, whispers to the viewer: \"Lương không tăng... mà thuế tăng gấp "
                      "đôi?\""),
                 subs=[(0.5, 4.8, "Từ năm nay, nộp đủ thuế. / Không còn nộp nửa nữa."),
                       (5.0, 9.5, "Lương không tăng... / mà thuế tăng gấp đôi?")]),
            dict(name="Cái cân", tiktok="bo", label="",
                 img=f"First-person view at a big wooden balance scale, a clerk quietly pressing his foot on the scale beam while weighing a farmer's rice, {FACE} staring at the foot, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư pours his rice onto the big scale; the clerk quietly presses his foot on the beam and "
                      "shakes his head: \"Thiếu.\" 5-10s: Anh Tư points at the foot and whispers to the viewer: \"Cân nhà "
                      "quan... có thêm một bàn chân.\""),
                 subs=[(0.5, 4.8, "Thiếu."),
                       (5.0, 9.5, "Cân nhà quan... / có thêm một bàn chân.")]),
            dict(name="Sang năm", label="",
                 img=f"First-person view leaving the tax yard, {FACE} carrying an empty basket, looking back at the mountain of rice sacks piled by the officials, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư walks away with an empty basket, looking back at the mountain of sacks behind the "
                      "officials. 5-10s: He says to the viewer: \"Năm ngoái nộp một bao, năm nay hai bao... sang năm chắc "
                      "nộp luôn cả em.\""),
                 subs=[(5.0, 9.5, "Năm ngoái một bao, / năm nay hai bao... sang năm / chắc nộp luôn cả em.")]),
            dict(name="Họp đêm", tiktok="bo", label="Đêm hôm ấy",
                 img=f"First-person view at night under a banyan tree lit by a small fire, village men gathered in a circle, a broad-shouldered leader seen only from behind speaking quietly, {FACE} beside the viewer listening, realistic, vertical 9:16.",
                 vid=("0-5s: Under the banyan tree at night, a broad-shouldered leader seen only from behind says quietly: "
                      "\"Không nộp nữa.\" The men nod one by one. 5-10s: Anh Tư whispers to the viewer: \"Ơ... thế bao "
                      "thóc thứ hai... em giữ lại nấu cơm được không?\""),
                 subs=[(0.5, 4.8, "Không nộp nữa."),
                       (5.0, 9.5, "Thế bao thóc thứ hai... / em giữ lại nấu cơm được không?")]),
            dict(name="Ghi tên em vào sử", label="",
                 img=f"First-person view at dawn of a huge crowd of farmers with torches and bamboo poles surrounding the wooden walls of a government citadel, no fighting, {FACE} in the crowd raising his empty basket, grinning, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn; a huge crowd of farmers with torches and bamboo poles surrounds the citadel walls, "
                      "shouting together; no fighting shown. A calm narrator's voice says: \"Năm 687, đô hộ Lưu Diên Hựu "
                      "bắt nộp thuế gấp đôi. Đinh Kiến cùng dân nổi dậy, vây phủ thành Tống Bình.\" 5-10s: Anh Tư raises his "
                      "empty basket and grins at the camera: \"Bao thóc thứ hai ấy, em không nộp! Ghi tên em vào sử nhé!\""),
                 subs=[(0.3, 4.8, "Năm 687, đô hộ bắt nộp / thuế gấp đôi. Đinh Kiến / cùng dân vây phủ thành."),
                       (5.0, 9.8, "Bao thóc thứ hai ấy, / em không nộp! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Đang nộp nửa thuế bỗng bị bắt nộp gấp đôi, cả làng đứng dậy 😤 Năm 687, đô hộ Lưu Diên Hựu bắt dân An Nam "
                 "nộp đủ thuế thay vì một nửa như trước. Lý Tự Tiên, Đinh Kiến cùng dân nổi dậy, vây phủ thành Tống Bình. "
                 "Lương không tăng mà thuế tăng, nghe có quen không? 👇"),
        tags="#lamthuequandoho #bacthuoc #dinhkien #lytutien #nam687",
        tt_title="Đang nộp nửa thuế bỗng bị bắt nộp gấp đôi, cả làng đứng dậy",
        hooks_alt=["POV: Cân nhà quan / có thêm bàn chân", "POV: Năm nay hai bao / sang năm nộp luôn cả em"],
        pin=("Đinh Kiến và Lý Tự Tiên là hai cái tên ít người biết của thời Bắc thuộc 😮 Bạn có biết thêm cuộc khởi nghĩa "
             "nào vì thuế không? Follow để xem Anh Tư làm thuê cho quan đô hộ!"),
        yt_title="Năm 687: thuế tăng gấp đôi, cả làng đứng dậy vây phủ thành",
        yt_tags=("đinh kiến, lý tự tiên, lưu diên hựu, bắc thuộc, nhà đường, tống bình, an nam đô hộ phủ, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ năm 819
    dict(
        slug="thang-chuc-duong-thanh-819", prefix="bt819",
        title="Sếp được \"thăng chức\", rồi bị giao việc khó nhất, nửa đêm sếp quay quân về (Dương Thanh, năm 819)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** theo *Đại Việt sử ký toàn thư* (mức B), đô hộ An Nam là Lý Tượng Cổ tham lam, hà khắc. "
                 "Hào trưởng đất Hoan Châu là Dương Thanh bị ông ta nghi kỵ, đưa về làm nha môn tướng để dễ kiềm chế, "
                 "rồi sai đi đánh dẹp vùng Hoàng Động. Năm 819, Dương Thanh nhân lòng oán của quân sĩ, nửa đêm quay quân "
                 "về đánh chiếm phủ thành, lật đổ Lý Tượng Cổ. **Hư cấu:** Anh Tư, bữa tiệc của quan đô hộ và mọi lời "
                 "thoại. Kết cục của Lý Tượng Cổ chỉ nhắc bằng lời, không dựng thành cảnh."),
        setting=("An Nam protectorate, year 819, under the Tang: a government compound in Tống Bình with wooden halls, a "
                 f"jungle road to the mountains at night. {TANG}. The local commander Dương Thanh is a broad, stern "
                 "Vietnamese man around 45, seen only from behind or in profile, in simple lamellar armor. "
                 f"Anh Tư is {FACE}, one of his soldiers in a plain brown tunic with a spear. {NO_TEXT}"),
        visual=VIS_TANG,
        hook="POV: Sếp được / thăng chức / mà cả đội khổ",
        end=END,
        clips=[
            dict(name="Thăng chức", label="Phủ Tống Bình · năm 819",
                 img=f"First-person view in a government courtyard, soldiers gathered around a messenger announcing news, a stern commander seen from behind, {FACE} beside the viewer, excited, realistic, vertical 9:16.",
                 vid=("0-5s: A messenger announces: \"Ông Thanh được thăng làm nha môn tướng!\" The soldiers cheer. "
                      "Anh Tư claps: \"Thăng chức! Thế lương có tăng không?\" 5-10s: An older soldier answers flatly: "
                      "\"Không. Nhưng được đứng gần quan đô hộ.\""),
                 subs=[(0.5, 4.8, "Thăng chức! / Thế lương có tăng không?"),
                       (5.0, 9.5, "Không. Nhưng được đứng / gần quan đô hộ.")]),
            dict(name="Đứng gần sếp", tiktok="bo", label="",
                 img=f"First-person view at the door of a lavish banquet hall, a plump Tang official in a red round-collared robe eating from many dishes and counting coins, {FACE} standing guard at the door with a spear, swallowing, realistic, vertical 9:16.",
                 vid=("0-5s: Inside, the plump official in a red robe feasts on many dishes and counts coins. Anh Tư stands "
                      "guard at the door, smelling the food. 5-10s: He whispers to the viewer: \"Đứng gần sếp... để ngửi "
                      "mùi cỗ.\""),
                 subs=[(5.0, 9.5, "Đứng gần sếp... / để ngửi mùi cỗ.")]),
            dict(name="Việc khó nhất", label="",
                 img=f"First-person view in an audience hall, a plump Tang official in a red robe pointing at a map scroll of jungle mountains (no visible writing), the stern commander seen from behind, {FACE} beside the viewer, jaw dropped, realistic, vertical 9:16.",
                 vid=("0-5s: The plump official points at a map of jungle mountains: \"Thăng chức rồi thì đi đánh Hoàng "
                      "Động. Đường rừng, nhiều thú dữ.\" 5-10s: Anh Tư whispers to the viewer: \"Thăng chức kiểu gì... mà "
                      "nhận việc khó nhất?\""),
                 subs=[(0.5, 4.8, "Thăng chức rồi thì / đi đánh Hoàng Động. / Đường rừng, nhiều thú dữ."),
                       (5.0, 9.5, "Thăng chức kiểu gì... / mà nhận việc khó nhất?")]),
            dict(name="Quay về", tiktok="bo", label="Nửa đêm, giữa rừng",
                 img=f"First-person view at night on a jungle road lit by torches, a column of soldiers halted, the stern commander seen from behind raising his hand and turning his horse around, {FACE} beside the viewer confused, realistic, vertical 9:16.",
                 vid=("0-5s: At night in the jungle, the commander, seen only from behind, raises his hand and turns his "
                      "horse around: \"Quay về.\" 5-10s: Anh Tư whispers to the viewer: \"Quay về... đánh rừng hay đánh "
                      "ai ạ?\" The column turns back silently."),
                 subs=[(0.5, 4.8, "Quay về."),
                       (5.0, 9.5, "Quay về... / đánh rừng hay đánh ai ạ?")]),
            dict(name="Ghi tên em vào sử", label="",
                 img=f"First-person view at night as a column of soldiers with torches pours through an open citadel gate, no fighting shown, {FACE} at the gate grinning, realistic, vertical 9:16.",
                 vid=("0-5s: At night, soldiers with torches pour through the open citadel gate; no fighting shown. A calm "
                      "narrator's voice says: \"Năm 819, Dương Thanh quay quân về giữa đêm, chiếm phủ thành, lật đổ quan đô "
                      "hộ tham tàn Lý Tượng Cổ.\" 5-10s: Anh Tư grins at the camera: \"Sếp giao việc khó... thì nhận kết "
                      "quả khó! Ghi tên em vào sử nhé!\""),
                 subs=[(0.3, 4.8, "Năm 819, Dương Thanh / quay quân về, lật đổ / quan đô hộ Lý Tượng Cổ."),
                       (5.0, 9.8, "Sếp giao việc khó... / thì nhận kết quả khó! / Ghi tên em vào sử nhé!")]),
        ],
        caption=("Sếp được \"thăng chức\", rồi bị giao việc khó nhất, nửa đêm sếp quay quân về 😏 Năm 819, đô hộ Lý Tượng "
                 "Cổ đưa Dương Thanh về làm nha môn tướng để kiềm chế, rồi sai đi đánh vùng rừng núi. Dương Thanh quay quân "
                 "về chiếm phủ thành. Bạn đã bao giờ được \"thăng chức\" kiểu này chưa? 👇"),
        tags="#lamthuequandoho #bacthuoc #duongthanh #lytuongco #nam819",
        tt_title="Sếp được thăng chức rồi bị giao việc khó nhất, nửa đêm sếp quay quân về",
        hooks_alt=["POV: Thăng chức / mà lương không tăng", "POV: Đứng gần sếp / để ngửi mùi cỗ"],
        pin=("\"Thăng chức\" để dễ kiềm chế, rồi giao việc khó nhất: chiêu này có từ năm 819 😅 Tag người cần xem! "
             "Follow để xem Anh Tư làm thuê cho quan đô hộ!"),
        yt_title="Năm 819: được thăng chức, bị giao việc khó nhất, nửa đêm quay quân về",
        yt_tags=("dương thanh, lý tượng cổ, bắc thuộc, nhà đường, an nam đô hộ phủ, hoan châu, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#lamthuequandoho #anhtu", note=NOTE, unit="Tập", file_unit="tap")
