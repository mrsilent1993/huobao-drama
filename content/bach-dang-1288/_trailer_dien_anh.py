#!/usr/bin/env python3
"""Trailer "Bạch Đằng 1288" bản ĐIỆN ẢNH (khoảng 65 giây, 7 clip Muse).
Tham khảo kiểu trailer cinematic của game chiến lược (người dẫn truyện giọng trầm kể như huyền sử, cảnh quay chậm,
thẻ tên địa danh, nhạc dồn lên cao trào, cắt đen đúng lúc gay cấn). Không chép cảnh, lời hay nhạc của trailer nào.
Sửa ở đây rồi chạy: python3 _trailer_dien_anh.py → trailer-dien-anh-bach-dang-1288.md + .plan.txt
"""
import os
from _gioi_thieu import ANH_TU_VOICE, FACE, STYLE, STAKE, REF_PROMPT, TAGS, YT_TAGS

HERE = os.path.dirname(os.path.abspath(__file__))

AUDIO = ("Audio: an original epic orchestral trailer score with a low male choir hum, deep war drums, low strings, horns "
         "and a lonely Vietnamese bamboo flute motif; it starts almost silent and builds clip by clip to a huge climax; "
         "mixed under the voice so every word stays clear; natural sound (wind, waves, creaking wood, ropes). The narrator "
         "speaks Vietnamese in a deep, grave, slow male baritone like a legend being told, long pauses, never rushed, the "
         "same narrator voice in every clip. Anh Tư speaks only in the last clip, lip-synced. " + ANH_TU_VOICE + ".")
SLOW = "Shot like a game cinematic trailer: slow motion, slow dolly and crane moves, deep shadows and god rays. "

HOOK = "Họ đã đến hai lần"
END = "BẠCH ĐẰNG 1288 / Follow để xem tập 1 →"
NHAN = "AI tái hiện · dựa trên sử liệu"

CLIPS = [
    dict(name="Biển tối", label="Cuối năm 1287",
         img=("Pre-dawn darkness over a vast sea, the horizon slowly filling with the dark silhouettes of hundreds of large "
              "wooden junks with matting sails, cold blue light, mist, realistic, vertical 9:16."),
         vid=(SLOW + "0-10s: Near silence, only wind and waves. Pre-dawn darkness over a vast sea; slowly, the dark "
              "silhouettes of hundreds of junks rise from the mist across the whole horizon; the first deep drum beat. The "
              "narrator, slow and grave: \"Họ đã đến... hai lần.\" A long pause, a second drum beat: \"Và lần này... họ mang "
              "theo cả biển.\""),
         subs=[(1.0, 4.4, "Họ đã đến... hai lần."), (5.4, 9.6, "Và lần này... / họ mang theo cả biển.")]),
    dict(name="Hạm đội và núi đá", label="Vân Đồn", chuyen="fadeblack:0.4",
         img=("Epic aerial at sunrise: an immense fleet of junks in long formation sailing between towering limestone karst "
              "islands, golden rays through the mist, realistic, vertical 9:16."),
         vid=(SLOW + "0-5s: Grand aerial sweep over an immense fleet of junks threading between towering limestone karsts at "
              "sunrise, the strings rise. 5-10s: Low angle on the deck of the lead junk: rows of Yuan soldiers in lamellar "
              "armor stand silent as the prow cuts the water in slow motion. The narrator: \"Hàng vạn quân. Hàng trăm chiến thuyền. "
              "Một đội quân... chưa từng biết thua.\""),
         subs=[(3.0, 9.6, "Hàng vạn quân. / Hàng trăm chiến thuyền. / Một đội quân... / chưa từng biết thua.")]),
    dict(name="Người đứng trên đồi", label="", chuyen="cat",
         img=("Dusk on a high hill above a wide winding river among karsts, a Trần commander in a dark robe seen only from "
              "behind, standing still, watching the river, wind in the grass, realistic, vertical 9:16."),
         vid=(SLOW + "0-10s: Dusk. A Trần commander in a dark robe, seen ONLY from behind, stands alone on a high hill above "
              "a wide winding river; the camera cranes up over his shoulder to reveal the river glinting all the way to the "
              "sea; the tide visibly drains, exposing broad mud flats; the bamboo flute plays alone. The narrator, low: "
              "\"Có một người... không nhìn ra biển. / Ông nhìn xuống dòng sông... và chờ nước rút.\""),
         subs=[(0.8, 4.4, "Có một người... / không nhìn ra biển."), (5.0, 9.6, "Ông nhìn xuống dòng sông... / và chờ nước rút.")]),
    dict(name="Rừng cọc trong đêm", label="Sông Bạch Đằng", chuyen="cat",
         img=(f"Night at low tide on the Bạch Đằng river, {STAKE} Hundreds of torches across the mud flats light rows upon "
              "rows of giant tree-trunk stakes spanning the river from bank to bank, teams of men hauling ropes on tall wooden "
              "tripods, the stakes tower over the men, karst silhouettes under the moon, realistic, vertical 9:16."),
         vid=(f"{STAKE} " + SLOW + "0-5s: Night at low tide: hundreds of torches across the mud flats; rows upon rows of giant "
              "tree-trunk stakes spanning the whole river; at dozens of tall tripods, teams haul ropes together and the heavy "
              "log rams slam down in slow motion exactly on the war-drum beats, spraying mud and sparks from the torches. "
              "5-10s: Extreme low angle at the foot of one enormous stake towering against the moon as the ram drops. The "
              "narrator: \"Suốt nhiều đêm... họ trồng xuống lòng sông... cả một khu rừng.\""),
         subs=[(3.0, 9.6, "Suốt nhiều đêm... / họ trồng xuống lòng sông... / cả một khu rừng.")]),
    dict(name="Nước lên", label="", chuyen="cat",
         img=("Dawn, high tide on the wide river between karsts, the water smooth and golden, the tips of hidden stakes "
              "just beneath the surface, the enemy fleet appearing at the bend, realistic, vertical 9:16."),
         vid=(f"{STAKE} " + SLOW + "0-5s: Grand time-lapse from high above: the tide floods in and swallows the whole forest "
              "of stakes until only smooth golden water remains at dawn. 5-10s: Underwater shot looking up: the dark hulls "
              "of great junks glide slowly overhead, passing just above the hidden stake points; the music holds one "
              "trembling note. The narrator, almost a whisper: \"Rồi nước lên... / và họ chờ.\""),
         subs=[(5.2, 9.6, "Rồi nước lên... / và họ chờ.")]),
    dict(name="Nước rút", label="", chuyen="cat",
         img=("Morning on the river, the tide falling, a huge junk lurching as its hull grinds onto unseen stakes, its mast "
              "tilting, spray and splinters in the air, karsts behind, realistic, vertical 9:16."),
         vid=(f"{STAKE} " + SLOW + "0-6s: The tide falls; in slow motion a huge junk lurches as its hull grinds onto the "
              "stakes, timbers crack, the mast tilts, spray and wood splinters fill the air; across the river dozens of "
              "junks shudder to a stop; the full orchestra and choir hit the climax; drums pound. No one is hurt on screen. "
              "The narrator: \"Nước lên, thuyền nổi. / Nước rút...\" 6-10s: Hard cut to black and total silence."),
         subs=[(1.0, 3.6, "Nước lên, thuyền nổi."), (3.8, 5.8, "Nước rút...")]),
    dict(name="Anh Tư", label="", chuyen="fadeblack:0.6",
         img=(f"Quiet misty morning, {FACE} standing knee-deep in the shallow river beside one giant ironwood stake that is "
              "taller than him, holding a wooden mallet, karsts behind, calm dry expression, realistic, vertical 9:16."),
         vid=(f"{FACE}. {STAKE} 0-10s: After the silence, birdsong and gentle water. A quiet misty morning: Anh Tư stands "
              "knee-deep in the shallows beside one giant stake far taller than him, a wooden mallet on his shoulder; he "
              "pats the stake like an old buffalo, looks at the camera and says, deadpan: \"Em chỉ đóng cọc thôi... / còn "
              "lại, để nước lo.\" The bamboo flute motif returns softly."),
         subs=[(2.0, 7.4, "Em chỉ đóng cọc thôi... / còn lại, để nước lo.")]),
]

CAPTION = ("Họ đã đến hai lần. Lần thứ ba, họ mang theo cả biển… còn bên này, có người chỉ nhìn xuống dòng sông và chờ "
           "nước rút. 🌊 Bạch Đằng 1288 qua mắt một người lính, mỗi ngày một tập. Theo bạn, \"nước rút\" thì chuyện gì xảy ra? 👇")
PIN = "Tập 1 lên sóng ngày mai 📅 Follow để xem từ đầu, theo đúng thứ tự từ cuối năm 1287 đến buổi sáng trên sông Bạch Đằng."
YT_TITLE = "BẠCH ĐẰNG 1288 | Trailer | Họ đã đến hai lần #Shorts"


def main():
    base = "trailer-dien-anh-bach-dang-1288"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            f"hook: {HOOK}", f"end: {END}", "end_giay: 2.0", f"nhan: {NHAN}", ""]
    subs = []
    md = ["# Trailer điện ảnh \"Bạch Đằng 1288\" (khoảng 65 giây)", "",
          "**Kiểu trailer điện ảnh** (tham khảo cách làm trailer game chiến lược, không chép cảnh hay lời): người dẫn truyện "
          "giọng trầm kể như huyền sử, cảnh quay chậm, thẻ địa danh, nhạc từ im lặng dồn lên cao trào, **cắt đen đúng lúc "
          "\"Nước rút...\"**, rồi Anh Tư chốt một câu. Cảnh chính là **rừng cọc khổng lồ**. Dùng song song hoặc thay cho "
          "bản giới thiệu hài (`gioi-thieu-bach-dang-1288.md`).", "",
          "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ.", "",
          "**Lịch sử (mức A/B):** quân Nguyên sang lần thứ ba cuối năm 1287 (hai lần trước: 1258, 1285); quân Trần đóng cọc "
          "ở Bạch Đằng, nhử địch lúc triều lên, đánh khi triều rút (9/4/1288). Quân số lệch nhiều giữa các nguồn nên lời dẫn "
          "chỉ nói \"hàng vạn quân, hàng trăm chiến thuyền\". Cọc 1288 là cả thân cây lim, **không bịt sắt**. Trần Hưng Đạo chỉ quay từ phía "
          "sau, không nói. Thuyền vỡ nhưng **không có cảnh người chết**. Không cờ, không chữ.", "",
          "**Anh Tư:** đính kèm `anh_tu_ref.png` ở clip 7 (ảnh khung đầu và video). Chưa có ảnh thì tạo bằng prompt:",
          "```", REF_PROMPT, "```",
          "**Giọng dẫn truyện** phải là một giọng duy nhất trong cả 6 clip đầu. Clip nào lệch giọng thì quay lại clip đó.", "",
          "**Thẻ địa danh** (\"Cuối năm 1287\", \"Vân Đồn\", \"Sông Bạch Đằng\") em chèn ở hậu kỳ, không để Muse viết chữ.", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"td-bd1288-{i}.mp4"
        md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{f}`", "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", f"{STYLE} {c['vid']} {AUDIO}", "```", ""]
        plan.append(f"clip: {f} | {c['label']}" + (f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""))
        subs += [f"sub: {i} | {a}-{b} | {t}" for a, b, t in c["subs"]]
    plan += [""] + subs
    yt_hash = " ".join(t for t in TAGS.split() if t not in ("#fyp", "#xuhuong"))
    md += ["## Đăng TikTok", "",
           "**Mô tả và hashtag:**", "```", CAPTION, TAGS, "```", "",
           "**Bình luận ghim:**", "```", PIN, "```", "",
           "Không trả lời đáp án \"nước rút thì sao\" trong bình luận. Bật nhãn \"Nội dung do AI tạo\".", "",
           "## Đăng YouTube Shorts", "",
           "**Tiêu đề:**", "```", YT_TITLE, "```", "",
           "**Mô tả:**", "```", CAPTION, "",
           "Video do AI tạo, dựa trên sử liệu; nhân vật Anh Tư và lời thoại là hư cấu.", "",
           f"#Shorts {yt_hash}", "```", "",
           "**Thẻ:**", "```", YT_TAGS, "```", "",
           "## Đăng Facebook", "",
           "Dùng mô tả TikTok, bỏ `#fyp #xuhuong`; bật \"Thông tin về AI\".", "",
           "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + ".md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
