#!/usr/bin/env python3
"""Video giới thiệu chuỗi "Tây Sơn từng mốc" (khoảng 40 giây, 4 clip Muse, quay kiểu trailer).
Sửa ở đây rồi chạy: python3 _gioi_thieu.py

Sinh ra gioi-thieu-tay-son.md (prompt dán thẳng + thông tin đăng) và gioi-thieu-tay-son.plan.txt (dựng).
Một bản dùng chung cho TikTok và YouTube.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
import series  # noqa: E402,F401  (dùng chung đường dẫn công cụ)

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
STYLE = ("Cinematic epic trailer shot, live-action realistic, dramatic natural light, sweeping camera, vertical 9:16. "
         "No modern objects, no on-screen text, no visible writing anywhere, NO FLAGS OF ANY KIND (no modern national "
         "flags, no banners with symbols), no blood, no gore, no children. Vietnam, late 18th century. Tây Sơn fighters "
         "with black-lacquered teeth in plain dark-red or brown clothes with red head wraps. The emperor Quang Trung is "
         "seen ONLY from behind or at a distance, never his face.")
AUDIO = ("Audio: deep war drums and natural ambient sound; the narrator speaks Vietnamese in a calm, deep, slow male "
         "baritone (documentary style, the same narrator voice as every video of the channel); Anh Tư, when he speaks, "
         "has a bright, slightly husky male voice around 30 with a Central Vietnamese (Bình Định) accent, lip-synced; "
         "no modern music.")

HOOK = "Từ người áo vải / đến hoàng đế / Quang Trung"
END = "Tây Sơn từng mốc · 16 tập / Follow để xem mốc 1 →"

CLIPS = [
    dict(name="Năm 1771", label="Tây Sơn từng mốc · 16 tập",
         img=("Cinematic wide shot at dawn over misty green highland hills of Tây Sơn (Bình Định), three young Vietnamese "
              "men in plain brown peasant clothes seen from behind standing on a ridge looking out over the valley, "
              "rice fields and bamboo villages below, realistic, vertical 9:16."),
         vid=("0-4s: Slow aerial push over misty highland hills at dawn toward three young men in peasant clothes standing "
              "on a ridge, seen from behind. 4-10s: Low angle as villagers in the valley below look up at them; drums "
              "begin. A calm narrator's voice says: \"Năm 1771, ba anh em nông dân ở ấp Tây Sơn đứng lên.\""),
         subs=[(4.0, 9.6, "Năm 1771, ba anh em nông dân / ở ấp Tây Sơn đứng lên.")]),
    dict(name="Những trận đánh", label="", chuyen="fadewhite:0.3",
         img=("Cinematic shot at dawn on a wide brown river in the Mekong delta, hundreds of small fast boats bursting out "
              "of palm-lined creeks, mist and spray, realistic, vertical 9:16."),
         vid=("Fast cinematic montage, no flags anywhere: 0-3s: hundreds of small boats burst out of palm-lined creeks onto "
              "a wide misty river. 3-6s: at night a long column of soldiers with torches marches fast along a winter road, "
              "breath steaming. 6-10s: at dawn an army pours across flat winter fields toward an earthen fort in smoke, no "
              "blood. The narrator says over the drums: \"Đánh tan quân Xiêm trên sông Tiền. Phá quân Thanh giữa mấy ngày "
              "Tết.\""),
         subs=[(0.5, 4.6, "Đánh tan quân Xiêm / trên sông Tiền."),
               (5.0, 9.6, "Phá quân Thanh / giữa mấy ngày Tết.")]),
    dict(name="Ngai vàng", label="", chuyen="fadeblack:0.6",
         img=("Cinematic shot at dawn on a pine-covered hill, a square three-tiered earthen altar with incense smoke, the "
              "emperor in a yellow robe seen only from behind at the top facing north, rows of officials kneeling below, "
              "realistic, vertical 9:16."),
         vid=("0-5s: Dawn on the hill; incense smoke drifts; the emperor, seen only from behind, stands at the top of the "
              "altar facing north while rows of officials kneel. 5-10s: The camera rises high above the altar toward a "
              "vast army waiting below. The narrator says: \"Từ ấp Tây Sơn đến ngai vàng Quang Trung. Mười sáu mốc. Và một "
              "người lính có mặt ở tất cả.\""),
         subs=[(0.5, 4.8, "Từ ấp Tây Sơn / đến ngai vàng Quang Trung."),
               (5.0, 9.6, "Mười sáu mốc. / Và một người lính / có mặt ở tất cả.")]),
    dict(name="Anh Tư", label="", chuyen="fadeblack:0.5",
         img=(f"Cinematic medium shot at sunrise on a hill above a river, {FACE}, in a brown shirt with a red head wrap, "
              "facing the camera with a huge chipped-tooth grin, a carrying pole on his shoulder, an army camp blurred "
              "behind, realistic, vertical 9:16."),
         vid=(f"Anh Tư is {FACE}. 0-5s: Anh Tư faces the camera, grins and says: \"Em là Anh Tư. Mốc nào em cũng có "
              "mặt... và lần nào cũng bị giao việc lạ nhất.\" 5-10s: He shifts the carrying pole on his shoulder, winks "
              "and says: \"Mai bắt đầu từ năm 1771. Mỗi ngày một mốc!\""),
         subs=[(0.5, 4.8, "Em là Anh Tư. / Mốc nào em cũng có mặt... / lần nào cũng bị giao việc lạ."),
               (5.0, 8.2, "Mai bắt đầu từ năm 1771. / Mỗi ngày một mốc!")]),
]

TAGS = "#taysontungmoc #quangtrung #nguyenhue #tayson #anhtu #povlichsu #lichsuvietnam #xuhuong #fyp"
CAPTION = ("Từ ba anh em nông dân ở ấp Tây Sơn năm 1771 đến hoàng đế Quang Trung: 16 mốc, mỗi ngày một video 🔥 Và Anh Tư "
           "có mặt ở tất cả, lần nào cũng bị giao việc lạ nhất. Mai bắt đầu mốc 1. Bạn mong mốc nào nhất? 👇")
PIN = ("Lịch đăng: mỗi ngày một mốc, từ năm 1771 đến năm 1792 📅 Bạn muốn xem mốc nào trước: Rạch Gầm, đêm Hà Hồi hay "
       "vua Quang Trung lên ngôi? Follow để không lỡ mốc nào!")
YT_TITLE = "Tây Sơn từng mốc: từ người áo vải đến hoàng đế Quang Trung (16 tập) #Shorts"
YT_TAGS = ("tây sơn, quang trung, nguyễn huệ, tây sơn từng mốc, khởi nghĩa tây sơn, rạch gầm, ngọc hồi đống đa, "
           "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts")


def main():
    base = "gioi-thieu-tay-son"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok và YouTube)",
            f"hook: {HOOK}", f"end: {END}", "end_giay: 1.6", "nhan: AI tái hiện · lời thoại hư cấu", ""]
    subs = []
    md = ["# Video giới thiệu chuỗi \"Tây Sơn từng mốc\" (khoảng 40 giây)", "",
          "**Một video, dùng chung cho TikTok và YouTube.** 4 clip Muse quay kiểu trailer: 3 cảnh lướt nhanh hành trình từ "
          "ấp Tây Sơn đến ngai vàng Quang Trung, cảnh cuối Anh Tư tự giới thiệu là người có mặt ở mọi mốc. Đăng **một "
          "ngày trước mốc 1**.", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          "**Lịch sử dùng trong video (mức B):** năm 1771 ba anh em Nguyễn Nhạc, Nguyễn Huệ, Nguyễn Lữ dấy binh ở ấp Tây "
          "Sơn; năm 1785 thắng quân Xiêm ở Rạch Gầm – Xoài Mút (sông Tiền); Tết Kỷ Dậu 1789 phá quân Thanh; cuối năm 1788 "
          "Nguyễn Huệ lên ngôi ở núi Bân, niên hiệu Quang Trung. Vua chỉ xuất hiện từ phía sau. Không cờ, không chữ.", "",
          "**Giọng:** người dẫn chuyện và Anh Tư dùng đúng giọng cố định của kênh (xem `../nghien-cuu/giong-nhan-vat.md`).", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"gt-tayson-{i}.mp4"
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
           "**Tiêu đề:**", "```", "Từ người áo vải đến hoàng đế Quang Trung: 16 mốc, mỗi ngày một video", "```", "",
           "**Mô tả và hashtag:**", "```", CAPTION, TAGS, "```", "",
           "**Bình luận ghim:**", "```", PIN, "```", "",
           "**Ghim video này lên trang cá nhân** trong suốt thời gian đăng loạt, thay cho một video đang ghim, để người "
           "mới vào biết có cả chuỗi. Bật nhãn \"Nội dung do AI tạo\".", "",
           "## Đăng YouTube Shorts", "",
           "**Tiêu đề:**", "```", YT_TITLE, "```", "",
           "**Mô tả:**", "```", CAPTION, "",
           "Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu. Đăng ký kênh để xem đủ 16 mốc.", "",
           f"#Shorts {yt_hash}", "```", "",
           "**Thẻ:**", "```", YT_TAGS, "```", "",
           "**Bình luận ghim:**", "```", PIN.replace("Follow", "Đăng ký"), "```", "",
           "Tạo **danh sách phát \"Tây Sơn từng mốc\"** trên YouTube, đặt video này đầu tiên, các mốc thêm vào theo thứ "
           "tự. Mục \"Nội dung bị thay đổi\" chọn **Có**.", "",
           "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + ".md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
