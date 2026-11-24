#!/usr/bin/env python3
"""Video giới thiệu loạt "Bạch Đằng 1288" (khoảng 40 giây, 4 clip Muse, quay kiểu trailer).
Sửa ở đây rồi chạy: python3 _gioi_thieu.py
Sinh ra gioi-thieu-bach-dang-1288.md (prompt dán thẳng + thông tin đăng) và .plan.txt (dựng). Một bản dùng chung mọi nền tảng.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FACE = ("a Vietnamese man around 30 with deeply tanned skin, hair in a topknot, black-lacquered teeth, a scar across his "
        "left eyebrow and a chipped front tooth; he acts naturally and understated, like a real person, not a performer")
STYLE = ("Cinematic epic trailer shot, live-action realistic, dramatic natural light, sweeping camera, vertical 9:16. "
         "Vietnam, 1287–1288, Trần dynasty. Trần soldiers and boatmen with hair in topknots and black-lacquered teeth, in "
         "brown or dark cotton tunics, barefoot, with spears and bows, small light wooden boats. Yuan forces: large wooden "
         "Chinese-style junks with matting sails, soldiers in leather lamellar armor and round helmets. Trần Hưng Đạo and the "
         "Trần kings are seen ONLY from behind or far away, never their faces. No modern objects, no on-screen text, no "
         "visible writing anywhere, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, no blood, no gore, no dead bodies, no "
         "children. Natural, understated acting; nobody laughs at the camera.")
AUDIO = ("Audio: deep war drums and natural ambient sound (wind, water, wood creaking); the narrator speaks Vietnamese in "
         "a calm, deep, slow male baritone (documentary style, the same narrator voice as every video of the channel); "
         "Anh Tư, when he speaks, has a bright, slightly husky male voice around 30, natural and conversational, dry humor, "
         "with a natural Northern Vietnamese (Hà Nội) accent, lip-synced; no modern music.")
STAKE = ("The stakes are whole ironwood tree trunks about 20 to 30 cm thick and 2.5 to 3 m long, sharpened (no iron tips), "
         "driven into the riverbed at low tide by teams of men lifting and dropping a heavy wooden ram on ropes; never thin "
         "sticks, never small hand hammers.")

HOOK = "Bạch Đằng 1288 / qua mắt / một người lính"
END = "Bạch Đằng 1288 · 16 tập / Follow để xem tập 1 →"

CLIPS = [
    dict(name="Giặc sang lần thứ ba", label="Bạch Đằng 1288 · 16 tập",
         img=("Cinematic wide shot at dawn over a misty grey sea, a long line of large wooden Chinese-style junks with "
              "matting sails approaching a coast of limestone islands, realistic, vertical 9:16."),
         vid=("0-4s: Slow aerial push over a misty sea at dawn; a long line of large junks with matting sails approaches a "
              "coast of limestone islands; deep drums begin. 4-10s: Low angle on the water as a huge prow passes overhead. "
              "A calm narrator's voice says: \"Cuối năm 1287. Quân Nguyên sang đánh Đại Việt lần thứ ba.\""),
         subs=[(4.0, 9.6, "Cuối năm 1287. / Quân Nguyên sang / đánh Đại Việt lần thứ ba.")]),
    dict(name="Những việc lạ", label="", chuyen="fadewhite:0.3",
         img=(f"Cinematic close shot by a hearth, {FACE}, stirring a huge steaming pot of fragrant water with a long paddle, "
              "puzzled, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. Fast cinematic montage of four short shots, about 2.5 seconds each, no flags anywhere: "
              "(1) Anh Tư stirs a huge steaming pot of fragrant water, puzzled; (2) he carries a heavy lacquered gift chest "
              "on a pole behind envoys walking away; (3) he wades on a beach dragging a waterlogged sack of rice out of the "
              "surf; (4) he and other men hack apart a small wooden bridge over a stream. Over the montage Anh Tư's voice "
              "says, deadpan: \"Đun nước. Khiêng lễ. Mò gạo. Phá cầu. Không ai nói em để làm gì.\""),
         subs=[(0.3, 5.4, "Đun nước. Khiêng lễ. / Mò gạo. Phá cầu."),
               (5.5, 9.6, "Không ai nói em / để làm gì.")]),
    dict(name="Rừng cọc", label="", chuyen="fadeblack:0.6",
         img=("Cinematic wide shot at low tide on a muddy river estuary, teams of men lifting and dropping a heavy wooden "
              "ram on ropes onto massive ironwood stakes, rows of stakes rising from the mud, a commander seen only from "
              "behind on the bank in a dark cloak, realistic, vertical 9:16."),
         vid=(f"{STAKE} 0-5s: Low tide on the Bạch Đằng estuary; teams of men drop a heavy wooden ram onto massive stakes, "
              "thud after thud; a commander seen only from behind watches from the bank. 5-10s: Time-lapse as the tide rises "
              "and swallows the stakes until only smooth water remains. The narrator says: \"Có người tính từng con nước. "
              "Có người đóng từng cây cọc.\""),
         subs=[(0.5, 4.8, "Có người tính / từng con nước."), (5.0, 9.6, "Có người đóng / từng cây cọc.")]),
    dict(name="Anh Tư", label="", chuyen="fadeblack:0.5",
         img=(f"Cinematic medium shot at sunrise on a small wooden boat on a wide brown river, {FACE}, holding an oar and "
              "looking at the camera with a calm, dry expression, limestone hills and mist behind, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. 0-5s: On a small boat at sunrise Anh Tư looks at the camera and says quietly: \"Em là Anh "
              "Tư. Năm 1288 em có mặt từ đầu đến cuối... mà chẳng ai nói em làm gì.\" 5-10s: He dips the oar into the "
              "water and adds: \"Mai bắt đầu từ cái nồi nước. Mỗi ngày một tập.\""),
         subs=[(0.5, 4.8, "Em là Anh Tư. Năm 1288 / em có mặt từ đầu đến cuối... / mà chẳng ai nói em làm gì."),
               (5.0, 8.2, "Mai bắt đầu từ cái nồi nước. / Mỗi ngày một tập.")]),
]

TAGS = "#bachdang1288 #tranhungdao #nhatran #bachdang #anhtu #povlichsu #lichsuvietnam #xuhuong #fyp"
CAPTION = ("Năm 1288, một người lính bị giao toàn việc lạ: đun nước, khiêng lễ, mò gạo, phá cầu… và không ai nói để làm gì 😳 "
           "16 tập, mỗi ngày một tập, từ lúc giặc sang đến trận Bạch Đằng. Bạn đoán cái nồi nước ở tập 1 là để làm gì? 👇")
PIN = ("Lịch đăng: mỗi ngày một tập, theo đúng thứ tự từ cuối năm 1287 đến sau trận Bạch Đằng 9/4/1288 📅 Bạn mong tập nào "
       "nhất: Trần Khánh Dư ở Vân Đồn, rừng cọc giữa trưa hay bắt sống Ô Mã Nhi? Follow để không lỡ tập nào!")
YT_TITLE = "Bạch Đằng 1288 qua mắt một người lính: 16 tập, mỗi ngày một tập #Shorts"
YT_TAGS = ("bạch đằng 1288, trần hưng đạo, nhà trần, kháng chiến chống nguyên, bạch đằng, vân đồn, ô mã nhi, lịch sử việt "
           "nam, pov lịch sử, anh tư, đại việt, shorts")


def main():
    base = "gioi-thieu-bach-dang-1288"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            f"hook: {HOOK}", f"end: {END}", "end_giay: 1.6", "nhan: AI tái hiện · lời thoại hư cấu", ""]
    subs = []
    md = ["# Video giới thiệu loạt \"Bạch Đằng 1288\" (khoảng 40 giây)", "",
          "**Một video, dùng chung cho TikTok, YouTube và Facebook.** 4 clip Muse quay kiểu trailer: quân Nguyên vượt biển, "
          "chuỗi việc lạ của Anh Tư (gợi tò mò cho các tập sau), rừng cọc và thủy triều, cảnh cuối Anh Tư tự giới thiệu. "
          "Đăng **một ngày trước tập 1**.", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          "**Lịch sử dùng trong video (mức A/B):** cuối năm 1287 quân Nguyên sang đánh Đại Việt lần thứ ba; quân Trần đóng "
          "cọc ở sông Bạch Đằng, lợi dụng thủy triều. Cọc 1288 là cả thân cây lim, **không bịt sắt**. Trần Hưng Đạo chỉ "
          "xuất hiện từ phía sau. Không cờ, không chữ, không cảnh chết.", "",
          "**Giọng:** người dẫn chuyện và Anh Tư dùng đúng giọng cố định của kênh (xem `../nghien-cuu/giong-nhan-vat.md`), "
          "giọng Bắc.", "",
          "**Clip 2 là clip ghép nhanh 4 cảnh:** nếu Muse khó ra đủ 4 cảnh trong một clip, tạo 4 clip ngắn rồi gửi em, em "
          "ghép thành 10 giây.", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"gt-bd1288-{i}.mp4"
        md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{f}`", "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", f"{STYLE} {c['vid']} {AUDIO}", "```", ""]
        plan.append(f"clip: {f} | {c['label']}" + (f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""))
        subs += [f"sub: {i} | {a}-{b} | {t}" for a, b, t in c["subs"]]
    plan += [""] + subs
    hook_line = HOOK.replace(" / ", " ")
    yt_hash = " ".join(t for t in TAGS.split() if t not in ("#fyp", "#xuhuong"))
    md += ["## Đăng TikTok", "",
           "**Hook** (chữ to ở giây đầu, đã có trong video; dùng làm chữ trên ảnh bìa):", "```", hook_line, "```", "",
           "**Tiêu đề:**", "```", "Bạch Đằng 1288 qua mắt một người lính: 16 tập, mỗi ngày một tập", "```", "",
           "**Mô tả và hashtag:**", "```", CAPTION, TAGS, "```", "",
           "**Bình luận ghim:**", "```", PIN, "```", "",
           "**Ghim video này lên trang cá nhân** trong suốt thời gian đăng loạt. Bật nhãn \"Nội dung do AI tạo\".", "",
           "## Đăng YouTube Shorts", "",
           "**Tiêu đề:**", "```", YT_TITLE, "```", "",
           "**Mô tả:**", "```", CAPTION, "",
           "Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 16 tập.", "",
           f"#Shorts {yt_hash}", "```", "",
           "**Thẻ:**", "```", YT_TAGS, "```", "",
           "**Bình luận ghim:**", "```", PIN.replace("Follow", "Đăng ký"), "```", "",
           "Tạo **danh sách phát \"Bạch Đằng 1288\"**, đặt video này đầu tiên. Mục \"Nội dung bị thay đổi\" chọn **Có**.", "",
           "## Đăng Facebook", "",
           "Dùng mô tả TikTok, bỏ `#fyp #xuhuong`; bật \"Thông tin về AI\". Ghim bài lên đầu Trang trong thời gian đăng loạt.", "",
           "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + ".md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
