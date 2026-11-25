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

HOOK = "Bạch Đằng 1288 / chuyện vui / sử ít kể"
END = "Bạch Đằng 1288 · 16 tập / Follow để xem tập 1 →"
NHAN = "AI tái hiện · có chi tiết truyền thuyết"

# Kiểu trailer "tràng cười": mỗi clip 2 cảnh 5 giây, mỗi cảnh một câu chốt, đều là chuyện thật (hoặc truyền thuyết có nhãn)
# sẽ có trong 16 tập. Thứ tự: khoác lác -> gia hạn -> gửi gạo -> chậu nước -> nín thở -> thủy triều.
CLIPS = [
    dict(name="Lên trời cũng đuổi", label="Bạch Đằng 1288 · 16 tập",
         img=("Cinematic low-angle shot at dawn of the prow of a large wooden Chinese-style junk with matting sails, a Yuan "
              "naval commander in leather lamellar armor and round helmet raising his arm boastfully, more junks behind in "
              "the mist, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. 0-5s: On the prow of a huge junk at dawn, a Yuan naval commander raises his arm and booms "
              "in Vietnamese with a light foreign accent: \"Lên trời, ta cũng đuổi theo!\" Drums. 5-10s: Cut to Anh Tư "
              "hiding in the reeds in a small boat; he looks at the camera and says quietly, deadpan: \"Ông ấy chưa biết... "
              "sông này có thủy triều.\""),
         subs=[(0.4, 4.8, "Lên trời, / ta cũng đuổi theo!"), (5.0, 9.6, "Ông ấy chưa biết... / sông này có thủy triều.")]),
    dict(name="Gia hạn và gửi gạo", label="", chuyen="cat",
         img=(f"Cinematic shot on a coastal camp, {FACE} holding a coil of rope in front of a broad-shouldered Trần general "
              "seen only from behind who raises three fingers, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. 0-5s: Anh Tư, holding a coil of rope, has come to arrest a general; the general, seen only "
              "from behind, raises three fingers and says: \"Cho ta ba hôm.\" Anh Tư says quietly to the camera: \"Đi bắt "
              "người ta... người ta xin gia hạn.\" 5-10s: Quick cut to a grey beach: Anh Tư drags a waterlogged rice sack out "
              "of the surf while more sacks float in: \"Giặc sang đánh mình... mà gửi gạo sang trước.\""),
         subs=[(0.3, 1.8, "Cho ta ba hôm."), (1.8, 4.9, "Đi bắt người ta... / người ta xin gia hạn."),
               (5.0, 9.6, "Giặc sang đánh mình... / mà gửi gạo sang trước.")]),
    dict(name="Chậu nước và nín thở", label="", chuyen="cat",
         img=(f"Cinematic shot by a hearth, {FACE} stirring a huge steaming pot of fragrant water with a long paddle, two "
              "dignified Trần nobles seen only from behind standing apart, ignoring each other, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. 0-5s: Anh Tư stirs a huge steaming pot of fragrant water; behind him two dignified nobles, "
              "seen only from behind, stand apart ignoring each other. He whispers to the camera: \"Đun nước tắm... cho hai "
              "ông giận nhau mấy chục năm.\" 5-10s: Quick cut to a river: Anh Tư bursts up out of the water gasping, while "
              "beside him a lean adult man's head stays calmly underwater, only bubbles rising. Anh Tư, panting: \"Em nín "
              "được một lúc... ông ấy nín cả buổi.\""),
         subs=[(0.3, 4.8, "Đun nước tắm... / cho hai ông / giận nhau mấy chục năm."),
               (5.0, 9.6, "Em nín được một lúc... / ông ấy nín cả buổi.")]),
    dict(name="Nước rút", label="", chuyen="fadeblack:0.5",
         img=(f"Cinematic wide shot at midday as the tide falls on a wide river estuary, a forest of massive ironwood stakes "
              f"emerging from the water, large junks tilted and stuck among them, small boats closing in, {FACE} in a small "
              "boat in the foreground, no bodies, realistic, vertical 9:16."),
         vid=(f"{STAKE} Anh Tư is {FACE}. 0-5s: The tide falls; a forest of massive stakes rises from the water; big junks "
              "lurch and stick fast with a deep crack of timber; drums on both banks. No bodies, no blood. A calm narrator's "
              "voice says: \"Và rồi... nước rút.\" 5-10s: Anh Tư in his small boat looks at the camera and says quietly: "
              "\"Mười sáu tập. Toàn việc lạ. Mai bắt đầu từ cái nồi nước.\""),
         subs=[(0.8, 4.6, "Và rồi... / nước rút."), (5.0, 8.2, "Mười sáu tập. Toàn việc lạ. / Mai bắt đầu từ cái nồi nước.")]),
]

TAGS = "#bachdang1288 #tranhungdao #nhatran #bachdang #anhtu #povlichsu #lichsuvietnam #xuhuong #fyp"
CAPTION = ("Năm 1288 có những chuyện sử ít kể 😂 Tướng giặc khoe \"lên trời cũng đuổi\", tướng ta bị bắt thì xin gia hạn, giặc "
           "sang đánh mà gửi gạo sang trước, hai ông tướng giận nhau làm lành bằng một chậu nước… 16 tập, mỗi ngày một "
           "tập. Bạn đoán chuyện nào là thật? 👇")
PIN = ("Tất cả đều có trong sử (riêng chuyện nín thở của Yết Kiêu là truyền thuyết) 📅 Mỗi ngày một tập, theo đúng thứ tự từ cuối "
       "năm 1287 đến sau trận Bạch Đằng 9/4/1288. Bạn mong tập nào nhất? Follow để không lỡ tập nào!")
YT_TITLE = "Bạch Đằng 1288: những chuyện vui sử ít kể (16 tập) #Shorts"
YT_TAGS = ("bạch đằng 1288, trần hưng đạo, trần khánh dư, ô mã nhi, yết kiêu, trương văn hổ, nhà trần, kháng chiến chống "
           "nguyên, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts")


def main():
    base = "gioi-thieu-bach-dang-1288"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            f"hook: {HOOK}", f"end: {END}", "end_giay: 1.6", f"nhan: {NHAN}", ""]
    subs = []
    md = ["# Video giới thiệu loạt \"Bạch Đằng 1288\" (khoảng 40 giây)", "",
          "**Một video, dùng chung cho TikTok, YouTube và Facebook.** 4 clip Muse quay kiểu trailer: quân Nguyên vượt biển, "
          "sáu câu chốt vui lấy từ các tập sau, rồi rừng cọc lúc nước rút và lời hẹn của Anh Tư. "
          "Đăng **một ngày trước tập 1**.", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          "**Lịch sử dùng trong video (mức A/B):** cuối năm 1287 quân Nguyên sang đánh Đại Việt lần thứ ba; quân Trần đóng "
          "cọc ở sông Bạch Đằng, lợi dụng thủy triều. Cọc 1288 là cả thân cây lim, **không bịt sắt**. Trần Hưng Đạo chỉ "
          "xuất hiện từ phía sau. Không cờ, không chữ, không cảnh chết.", "",
          "**Giọng:** người dẫn chuyện và Anh Tư dùng đúng giọng cố định của kênh (xem `../nghien-cuu/giong-nhan-vat.md`), "
          "giọng Bắc.", "",
          "**Kiểu \"tràng cười\":** mỗi clip 2 cảnh, mỗi cảnh 5 giây một câu chốt, nối bằng cắt thẳng cho nhịp nhanh. Nếu "
          "Muse khó ra 2 cảnh trong một clip, tạo 8 clip 5 giây (đặt tên `gt-bd1288-1a`, `1b`…) rồi gửi em ghép.", "",
          "**Các chuyện trong trailer (đều sẽ có trong 16 tập):** Ô Mã Nhi khoác lác \"lên trời cũng đuổi\" (B, câu nói chép "
          "năm 1285); Trần Khánh Dư bị sai người đến bắt, xin hoãn để lập công (B); Trương Văn Hổ ném lương xuống biển (A); "
          "Trần Hưng Đạo tắm cho Trần Quang Khải để làm lành (B); Yết Kiêu lặn giỏi (C, truyền thuyết: nhãn video ghi \"có chi "
          "tiết truyền thuyết\"); cọc và thủy triều Bạch Đằng (A).", ""]
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
