#!/usr/bin/env python3
"""Video giới thiệu loạt "Bạch Đằng 1288" (khoảng 48 giây, 5 clip Muse, quay kiểu trailer).
Sửa ở đây rồi chạy: python3 _gioi_thieu.py
Sinh ra gioi-thieu-bach-dang-1288.md (prompt dán thẳng + thông tin đăng) và .plan.txt (dựng). Một bản dùng chung mọi nền tảng.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FACE = ("Anh Tư: the SAME man as in the attached reference image anh_tu_ref.png (same face, same age, same scar, same "
        "teeth, same hair): a Vietnamese man around 30 with deeply tanned skin, hair in a topknot with a faded brown cloth "
        "band, black-lacquered teeth, a thin scar across his left eyebrow and one chipped front tooth, a coarse dark-brown "
        "cotton tunic; he acts naturally and understated, like a real person, not a performer")
ANH_TU_VOICE = ("Anh Tư's own voice, identical in every clip of every episode: a bright, slightly husky male voice around "
                "30 with a natural Central Vietnamese (Huế) accent, natural and conversational, dry humor, never shouting")
STYLE = ("Epic cinematic trailer shot, live-action photorealistic, grand sweeping landscapes, golden dramatic light, volumetric "
         "mist, wide aerial and crane camera moves, film grain, vertical 9:16. Vietnam, 1287–1288, Trần dynasty, the "
         "Bạch Đằng estuary region: wide brown tidal rivers, towering limestone karst islands and cliffs, mangrove banks, the "
         "sea. Trần soldiers and boatmen with hair in topknots and black-lacquered teeth, in brown or dark cotton tunics, "
         "barefoot, with spears and bows, small light wooden boats. Yuan forces: large wooden Chinese-style junks with matting "
         "sails, soldiers in leather lamellar armor and round helmets. Trần Hưng Đạo and the Trần kings are seen ONLY from "
         "behind or far away, never their faces. No modern objects, no on-screen text, no visible writing anywhere, "
         "ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, no blood, no gore, no dead bodies, no children. Natural, understated "
         "acting; nobody laughs at the camera.")
AUDIO = ("Audio: an original epic orchestral trailer score (deep war drums, low strings, horns, a Vietnamese bamboo flute "
         "motif) building to a climax, mixed under the dialogue so every word stays clear, plus natural sound (wind, water, "
         "creaking wood). The narrator speaks Vietnamese in a calm, deep, slow male baritone, documentary style, the same "
         f"narrator voice as every video of the channel. When Anh Tư speaks: {ANH_TU_VOICE}, lip-synced.")
STAKE = ("The stakes are whole ironwood tree trunks about 20 to 30 cm thick and 2.5 to 3 m long, sharpened (no iron tips), "
         "driven into the riverbed at low tide by teams of men lifting and dropping a heavy wooden ram on ropes; never thin "
         "sticks, never small hand hammers.")
REF_PROMPT = ("Vertical 9:16 character reference portrait, head and shoulders, front view, of a Vietnamese man around 30 in "
              "1288: deeply tanned skin, hair tied in a neat topknot with a faded brown cloth band, black-lacquered teeth "
              "visible as he speaks, a thin horizontal scar across his left eyebrow, one chipped front tooth, short stubble, "
              "a coarse dark-brown cotton tunic, calm neutral expression (not smiling), soft overcast daylight, plain "
              "blurred river background, photorealistic historical film photography, no text.")

HOOK = "Năm 1288 / 16 việc lạ / không ai giải thích"
END = "Mai trả lời câu đầu tiên / Follow để xem tập 1 →"
NHAN = "AI tái hiện · có chi tiết truyền thuyết"

# Kiểu trailer ÚP MỞ, cảnh hùng vĩ, nhạc nền hoành tráng: mỗi cảnh chỉ hé MỘT việc lạ, cắt trước lời giải.
CLIPS = [
    dict(name="Hạm đội vào cửa sông", label="Bạch Đằng 1288 · 16 tập",
         img=("Epic aerial shot at sunrise over a vast misty estuary between towering limestone karst islands, hundreds of "
              "large wooden Chinese-style junks with matting sails sailing in a long formation into a wide brown river mouth, "
              "golden light and sun rays through the mist, realistic, vertical 9:16."),
         vid=("0-6s: Slow epic aerial push over a vast misty estuary at sunrise; hundreds of junks with matting sails glide in "
              "formation between towering limestone karsts into the river mouth; sun rays pierce the mist; the orchestral "
              "score swells with deep drums. A calm narrator's voice says: \"Cuối năm 1287. Quân Nguyên sang lần thứ ba.\" "
              "6-10s: Low angle on the prow of the lead junk: a Yuan naval commander in lamellar armor raises his arm and "
              "booms in Vietnamese with a light foreign accent: \"Lên trời, ta cũng đuổi theo!\""),
         subs=[(0.6, 5.6, "Cuối năm 1287. / Quân Nguyên sang lần thứ ba."), (6.2, 9.6, "Lên trời, / ta cũng đuổi theo!")]),
    dict(name="Lau sậy và ba hôm", label="", chuyen="cat",
         img=(f"Cinematic shot from tall reeds on a riverbank, {FACE} crouching in a small boat in the foreground, behind him "
              "the giant enemy fleet passing between limestone cliffs, realistic, vertical 9:16."),
         vid=(f"{FACE}. 0-5s: Anh Tư crouches in a small boat among tall reeds while the giant fleet passes behind him "
              "between limestone cliffs; he glances at the water, then at the camera, and starts quietly: \"Ông ấy chưa "
              "biết...\" — hard cut before he finishes. 5-10s: A windswept coastal camp above a stormy sea: a general seen "
              "only from behind raises three fingers: \"Cho ta ba hôm.\" Anh Tư, holding a coil of rope, blinks: \"Ba hôm... "
              "để làm gì ạ?\""),
         subs=[(0.4, 4.6, "Ông ấy chưa biết..."), (5.0, 6.8, "Cho ta ba hôm."), (6.8, 9.6, "Ba hôm... / để làm gì ạ?")]),
    dict(name="Gạo và nồi nước", label="", chuyen="cat",
         img=(f"Epic wide shot of a grey beach under a dramatic storm sky with limestone islands on the horizon, dozens of "
              f"rice sacks washing in on huge waves, {FACE} standing in the surf, realistic, vertical 9:16."),
         vid=(f"{FACE}. 0-5s: Wide shot of a grey beach under a dramatic storm sky; dozens of waterlogged rice sacks wash in on "
              "big waves; Anh Tư stands in the surf, staring: \"Gạo ở đâu... trôi vào nhiều thế này?\" 5-10s: Night, a "
              "grand wooden hall of the Trần court lit by many oil lamps; Anh Tư stirs a huge steaming pot of fragrant herbal "
              "water and asks a passing servant: \"Nước thơm thế này... tắm cho ai ạ?\" The servant only shakes his head."),
         subs=[(0.4, 4.8, "Gạo ở đâu... / trôi vào nhiều thế này?"), (5.0, 9.6, "Nước thơm thế này... / tắm cho ai ạ?")]),
    dict(name="Người dưới sông và bãi cọc", label="", chuyen="cat",
         img=(f"Epic shot of a wide river beneath towering limestone cliffs at dawn, {FACE} surfacing from the water gasping, "
              "calm water beside him with a few bubbles rising, realistic, vertical 9:16."),
         vid=(f"{STAKE} {FACE}. 0-5s: A wide river beneath towering limestone cliffs at dawn; Anh Tư surfaces, gasping, and "
              "stares at the calm water beside him where a man dived long ago; only bubbles rise: \"Ông ấy... lặn từ nãy đến "
              "giờ?\" 5-10s: Epic aerial over the estuary at low tide: hundreds of men drive massive stakes with heavy wooden "
              "rams; time-lapse as the tide rises and swallows them until only smooth golden water remains. The narrator "
              "says: \"Tất cả trông vào... một buổi sáng.\""),
         subs=[(0.4, 4.6, "Ông ấy... / lặn từ nãy đến giờ?"), (5.2, 9.6, "Tất cả trông vào... / một buổi sáng.")]),
    dict(name="Anh Tư", label="", chuyen="fadeblack:0.5",
         img=(f"Epic cinematic shot at sunrise, {FACE} standing in a small wooden boat on a vast calm river, towering "
              "limestone karsts and golden mist behind him, looking at the camera with a calm, dry expression, realistic, "
              "vertical 9:16."),
         vid=(f"{FACE}. 0-5s: Slow push-in on Anh Tư standing in a small boat on the vast calm river at sunrise, karsts and "
              "golden mist behind; the score drops to a single bamboo flute. He looks at the camera and says quietly: "
              "\"Mười sáu việc lạ.\" 5-10s: He dips his oar; the drums return softly: \"Mai em kể việc đầu tiên.\""),
         subs=[(0.8, 4.6, "Mười sáu việc lạ."), (5.0, 8.2, "Mai em kể / việc đầu tiên.")]),
]

TAGS = "#bachdang1288 #tranhungdao #nhatran #bachdang #anhtu #povlichsu #lichsuvietnam #xuhuong #fyp"
CAPTION = ("Năm 1288, một người lính bị giao toàn việc lạ: đi bắt tướng thì tướng xin \"cho ba hôm\", ra biển thì gạo trôi vào "
           "bờ, đun cả nồi nước thơm mà không biết tắm cho ai… 🤔 16 tập, mỗi ngày một tập. Bạn đoán \"ba hôm\" để làm gì? 👇")
PIN = ("Đáp án nằm trong 16 tập, theo đúng thứ tự từ cuối năm 1287 đến trận Bạch Đằng 📅 Ai đoán đúng \"ba hôm\" để làm gì "
       "trước khi tập đó lên sóng thì comment nhé! Follow để không lỡ tập nào.")
YT_TITLE = "Năm 1288: 16 việc lạ không ai giải thích | Bạch Đằng 1288 #Shorts"
YT_TAGS = ("bạch đằng 1288, trần hưng đạo, nhà trần, kháng chiến chống nguyên, bạch đằng, lịch sử việt nam, pov lịch sử, "
           "anh tư, đại việt, shorts")


def main():
    base = "gioi-thieu-bach-dang-1288"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            f"hook: {HOOK}", f"end: {END}", "end_giay: 1.6", f"nhan: {NHAN}", ""]
    subs = []
    md = ["# Video giới thiệu loạt \"Bạch Đằng 1288\" (khoảng 48 giây)", "",
          "**Một video, dùng chung cho TikTok, YouTube và Facebook.** 5 clip Muse quay kiểu trailer hùng vĩ, nhạc nền hoành tráng: mở bằng hạm đội quân Nguyên vào cửa sông, "
          "kiểu úp mở: mỗi cảnh chỉ đưa ra một việc lạ hoặc một câu hỏi, cắt trước lời giải; cảnh cuối bãi cọc chìm dưới nước và lời hẹn của Anh Tư. "
          "Đăng **một ngày trước tập 1**.", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", "",
          "**Lịch sử dùng trong video (mức A/B):** cuối năm 1287 quân Nguyên sang đánh Đại Việt lần thứ ba; quân Trần đóng "
          "cọc ở sông Bạch Đằng, lợi dụng thủy triều. Cọc 1288 là cả thân cây lim, **không bịt sắt**. Trần Hưng Đạo chỉ "
          "xuất hiện từ phía sau. Không cờ, không chữ, không cảnh chết.", "",
          "**Một mặt, một giọng cho Anh Tư:**", "",
          "1. **Tạo ảnh tham chiếu một lần**, lưu thành `anh_tu_ref.png`, rồi **đính kèm ảnh này ở mọi clip** (ảnh khung đầu và "
          "video) trong cả loạt:", "```", REF_PROMPT, "```",
          "2. **Giọng Anh Tư cố định, giọng miền Trung (Huế):** câu mô tả giọng đã chèn y hệt vào mọi prompt. Nếu Muse có chọn "
          "giọng, chọn **một giọng duy nhất** cho Anh Tư và dùng lại mãi. Clip nào lệch giọng, em có thể đổi giọng hậu kỳ về "
          "giọng mẫu (giữ nguyên khẩu hình).", "",
          "**Nhạc nền:** prompt yêu cầu nhạc giao hưởng hoành tráng tự sáng tác (trống trận, dây trầm, kèn, sáo trúc). Nếu Muse "
          "không ra nhạc, em ghép nhạc khi dựng (tạo nhạc riêng bằng Gemini Lyria hoặc dùng thư viện nhạc của nền tảng), không "
          "dùng nhạc có bản quyền của người khác.", "",
          "**Kiểu úp mở:** mỗi cảnh 5 giây chỉ hé một việc lạ, **không cảnh nào nói lời giải**. Lời giải nằm trong các tập: "
          "lời thách \"lên trời cũng đuổi\" (tập 13), \"cho ta ba hôm\" (tập 4), gạo trôi vào bờ (tập 5), nồi nước thơm (tập 1), "
          "người lặn mãi không lên (tập 11, truyền thuyết Yết Kiêu: nhãn video ghi \"có chi tiết truyền thuyết\"), bãi cọc "
          "(tập 8, 12). Nếu Muse khó ra 2 cảnh trong một clip, tạo 8 clip 5 giây (`gt-bd1288-1a`, `1b`…) rồi gửi em ghép.", ""]
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
           "**Không trả lời đáp án trong bình luận** cho đến khi tập đó lên sóng; chỉ thả tim các bình luận đoán.", "",
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
