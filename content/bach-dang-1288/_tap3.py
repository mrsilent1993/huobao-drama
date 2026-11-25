#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 3 "Cho ta ba hôm": bản sửa lượt lời (người nào nói câu người nấy, nói xong người sau mới nói).
Chạy: python3 _tap3.py → bd1288-tap3-cho-ta-ba-hom.md + bd1288-tap3.plan.txt
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FACE = ("Anh Tư: the SAME man as in the attached reference image anh_tu_ref.png (same face, same age, same scar, same "
        "teeth, same hair): a Vietnamese man around 30 with deeply tanned skin, hair in a topknot with a faded brown cloth "
        "band, black-lacquered teeth, a thin scar across his left eyebrow and one chipped front tooth, a coarse dark-brown "
        "cotton tunic; he is cheerful, playful and cheeky; while someone else is speaking he listens quietly with his mouth closed, with lively natural expressions (smiles, a quick grin when he jokes, raised eyebrows, a wink, a shrug), like a funny real person telling a story to a friend, never over-the-top")
BASE = ("Cinematic live-action, photorealistic, natural light, film grain, vertical 9:16. Vietnam, December 1287, Trần "
        "dynasty, Vân Đồn coast: soldiers in brown cotton tunics, hair in topknots, black-lacquered teeth. No modern "
        "objects, no on-screen text, no subtitles, no visible writing anywhere, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, "
        "no blood, no dead bodies, no children. Light, cheerful comedic tone; Anh Tư is playful and smiling, while the officials, the general and the envoy stay serious.")
V_TU = ("Anh Tư = a bright, slightly husky male voice around 30 with a natural Central Vietnamese (Huế) accent, cheerful and playful, warm and full of humor, "
        "never shouting, the SAME voice in every clip")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern accent, documentary style, OFF-SCREEN voice-over: "
          "nobody on screen moves their lips while the narrator speaks")
V_KD = ("Trần Khánh Dư = a calm, steady male voice in his late 40s, slow and certain, Northern accent, clearly different "
        "from Anh Tư's voice; he is seen ONLY from behind, his mouth is never visible")
V_SU = "the envoy = a clipped, impatient male voice in his 50s, Northern accent, clearly different from Anh Tư's voice"
RULES = ("STRICT TURN-TAKING: only ONE person speaks at a time. Each line is spoken COMPLETELY, at a natural unhurried "
         "pace, before the next person starts. No overlapping, no interrupting, no one speaks over anyone. The listener "
         "keeps his mouth CLOSED and still while the other person talks; lips move ONLY for the person whose turn it is. "
         "One continuous shot, NO cut or scene change inside this clip. Last word ends before 9.4s; the final 0.6s is "
         "silent.")
AUDIO = "Audio: {amb}. No background music. All dialogue in Vietnamese."

# Mỗi lượt: (ai, bắt đầu, kết thúc, lời nói, phụ đề, cách quay trong lượt đó)
# Lời nói = đúng chữ phụ đề (bỏ dấu " / "), đủ ngắn để nói trọn trong khung giờ.
CLIPS = [
    dict(name="Biển động", label="Vân Đồn · tháng 12/1287", tiktok="0-9.3",
         where="a rocky coast at Vân Đồn by day, hundreds of wooden warships far out at sea",
         img=f"Cinematic shot on a rocky coast by day, hundreds of wooden warships far out at sea, {FACE}, standing on the shore watching the fleet with his mouth closed, realistic, vertical 9:16.",
         amb="sea waves, wind, distant drums", voices=[V_NARR, V_TU],
         turns=[("narr", 0.5, 4.6, "Tháng chạp năm 1287. / Hàng trăm thuyền giặc / vượt biển vào Vân Đồn.",
                 "wide shot of the fleet at sea; Anh Tư seen small on the shore, back to camera, silent"),
                ("tu", 5.4, 9.2, "Thuyền nào cũng đi qua… / không thuyền nào chào em.",
                 "medium close-up of Anh Tư turning to the camera with a cheeky grin, pretending to wave at the ships")]),
    dict(name="Lệnh bắt ông tướng", label="", tiktok="bo",
         where="a coastal military camp at Vân Đồn by day, a court envoy in a dark brocade robe holding a rolled scroll",
         img=f"Cinematic shot in a coastal military camp by day, a court envoy in a dark brocade robe holding a rolled scroll, {FACE}, holding a coil of rope, listening with his mouth closed, realistic, vertical 9:16.",
         amb="camp murmuring, sea wind", voices=[V_SU, V_TU],
         turns=[("su", 0.5, 4.4, "Giặc lọt qua Vân Đồn. / Xiềng Khánh Dư, / giải về kinh.",
                 "the envoy faces the camera and reads the order; Anh Tư at the edge of frame, mouth closed, only listening"),
                ("tu", 5.2, 9.2, "Em đi bắt tướng… / dây em cầm, / tướng thì đằng kia.",
                 "the envoy has finished and stays silent; push in on Anh Tư holding up the rope, raising his eyebrows at the camera with a playful smile")]),
    dict(name="Cho ta ba hôm", label="", tiktok="0.3-9.4",
         where="a coastal military camp at Vân Đồn by day; Trần Khánh Dư in a dark robe, seen ONLY from behind, facing a court envoy in a dark brocade robe",
         img=f"Cinematic shot in a coastal military camp by day, Trần Khánh Dư seen only from behind in a dark robe, facing a court envoy in a dark brocade robe, {FACE}, standing aside holding a coil of rope, mouth closed, realistic, vertical 9:16.",
         amb="camp murmuring, sea wind", voices=[V_KD, V_TU],
         turns=[("kd", 0.5, 5.0, "Xử theo quân pháp, / tôi xin chịu tội. / Nhưng xin khất ba hôm / để lập công.",
                 "over-the-shoulder shot from behind Trần Khánh Dư toward the envoy; Anh Tư in the background, mouth closed, listening seriously, eyes moving between them"),
                ("tu", 5.8, 9.2, "Em cầm dây đứng đây… / không biết siết hay chờ.",
                 "Khánh Dư and the envoy are silent and still; Anh Tư leans toward the camera, holds the rope up with a comically confused smile and whispers playfully")]),
    dict(name="Thuyền lương đi sau", label="", tiktok="bo",
         where="a rocky coast at Vân Đồn at dusk; Trần Khánh Dư in a dark robe, seen ONLY from behind, pointing at the sea",
         img=f"Cinematic shot on a rocky coast at dusk, Trần Khánh Dư seen only from behind in a dark robe pointing at the sea, {FACE}, standing beside him listening with his mouth closed, realistic, vertical 9:16.",
         amb="sea waves, dusk wind", voices=[V_KD, V_TU],
         turns=[("kd", 0.5, 4.8, "Sau thuyền chiến / là thuyền lương. / Không quân giỏi hộ tống. / Đánh tất phá được.",
                 "from behind Khánh Dư as he points out to sea; Anh Tư beside him in profile, mouth closed, listening seriously"),
                ("tu", 5.6, 9.2, "Dễ thế… / sao ông không nói sớm / ba hôm?",
                 "Khánh Dư lowers his arm and stays silent; Anh Tư turns to the camera with a big amused grin and a shrug")]),
    dict(name="Đếm ba hôm", label="", tiktok="0.4-9.3",
         where="a coastal military camp at Vân Đồn at night, a small fire",
         img=f"Cinematic shot in a coastal camp at night, {FACE}, sitting alone by a small fire carving three marks into a wooden stick, realistic, vertical 9:16.",
         amb="fire crackling, night insects, sea wind", voices=[V_TU],
         turns=[("tu", 0.6, 4.4, "Một hôm… / hai hôm… / ba hôm.",
                 "close-up of Anh Tư alone by the fire, carving one mark for each count"),
                ("tu", 5.4, 9.2, "Ba hôm không thấy / thuyền lương… / thì dây này / để trói ai?",
                 "he looks up at the camera, smiles mischievously and dangles the rope; he is the only person in the shot")]),
    dict(name="Bố trí chờ", label="", tiktok="bo",
         where="a rocky coast at Vân Đồn at dawn; Trần Khánh Dư in a dark robe seen ONLY from behind; soldiers hiding behind rocks and trees",
         img=f"Cinematic shot on a rocky coast at dawn, Trần Khánh Dư seen only from behind in a dark robe, soldiers hiding behind rocks and trees, {FACE}, crouching behind a rock with his mouth closed, realistic, vertical 9:16.",
         amb="dawn birds, sea waves, soft wind", voices=[V_KD, V_TU],
         turns=[("kd", 0.5, 4.4, "Gom quân còn lại. / Phục từ Vân Đồn / tới Lục Thủy.",
                 "wide shot from behind Khánh Dư giving the order; soldiers move to hide; Anh Tư small in frame, mouth closed"),
                ("tu", 5.2, 9.0, "Hết cầm dây… / giờ em cầm đá.",
                 "Khánh Dư has walked out of frame; close-up of Anh Tư crouching behind a rock with a stone in his hand, tossing the stone in his hand and whispering to camera with a cheeky smile")]),
    dict(name="Kết: ba hôm", label="", tiktok="0.7-10", chuyen="fadeblack:0.8",
         where="a rocky coast at Vân Đồn at dusk, an empty sea",
         img=f"Cinematic shot at dusk on a rocky coast, {FACE}, holding a coil of rope, looking out at the empty sea, mouth closed, realistic, vertical 9:16.",
         amb="dusk birds, sea waves, soft wind", voices=[V_NARR, V_TU],
         turns=[("narr", 0.9, 4.4, "Ba hôm đó… / cả Vân Đồn cùng chờ.",
                 "wide shot of the empty sea at dusk; Anh Tư seen from behind on the rocks, silent"),
                ("tu", 5.0, 9.6, "Ba hôm nữa ông ấy / không về chịu tội… / thì em về chịu thay à?",
                 "Anh Tư turns around to face the camera, holding the rope, with a playful worried smile and a little shrug")]),
]
WHO = {"narr": "the NARRATOR (off-screen)", "tu": "ANH TƯ", "kd": "TRẦN KHÁNH DƯ (seen only from behind)",
       "su": "THE ENVOY"}
PREFIX = {"kd": "Trần Khánh Dư: / ", "su": "", "narr": "", "tu": ""}


def spoken(t):
    return t.replace(" / ", " ")


def video_prompt(c):
    parts = [BASE, f"Setting: {c['where']}.", FACE + "." if any(t[0] == "tu" for t in c["turns"]) else "", RULES]
    prev_end = 0.0
    for i, (who, a, b, text, cam) in enumerate(c["turns"], 1):
        if a - prev_end >= 0.5 and i > 1:
            parts.append(f"{prev_end:.1f}-{a:.1f}s: SILENCE, nobody speaks, everyone holds still.")
        parts.append(f"TURN {i} ({a:.1f}-{b:.1f}s), ONLY {WHO[who]} speaks, the whole line: \"{spoken(text)}\" "
                     f"Camera: {cam}.")
        prev_end = b
    parts.append(f"{prev_end:.1f}-10s: silence, hold the shot.")
    parts.append("VOICES (each person keeps his own voice, never swapped or merged): " + "; ".join(c["voices"]) + ".")
    parts.append(AUDIO.format(amb=c["amb"]))
    return " ".join(p for p in parts if p)


def main():
    base = "bd1288-tap3"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (ra {base}-youtube.mp4 và {base}-tiktok.mp4)",
            "hook: POV: Đi bắt tướng / tướng xin khất / ba hôm", "end: Follow để xem / Biển trả lương bằng gạo →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.4", ""]
    subs = []
    md = ["# Bạch Đằng 1288, tập 3: Cho ta ba hôm (bản sửa lượt lời)", "",
          "**Loạt:** Bạch Đằng 1288, 10 tập · **YouTube** khoảng 67 giây (đủ 7 cảnh) · **TikTok** khoảng 35 giây (cảnh 1-3-5-7)",
          "", "**File Muse đặt tên:** `bd1288-tap3-1..7.mp4` · **Giọng:** Anh Tư giọng Huế; dẫn chuyện giọng Bắc trầm; "
          "Khánh Dư, trung sứ giọng Bắc.", "",
          "## Sửa gì so với bản trước", "",
          "1. **Mỗi clip tối đa 2 lượt lời, chia giờ rõ ràng:** lượt 1 nói trọn câu, **lặng khoảng 0,8 giây**, rồi lượt 2 mới nói. "
          "Prompt ghi `ONLY … speaks` cho từng lượt và bắt người nghe **ngậm miệng**, nên Muse không còn khớp miệng nhầm sang người bên cạnh.",
          "2. **Câu ngắn lại cho vừa giờ.** Bản cũ nhét câu 25 chữ vào 5 giây (clip 3, 4, 7) nên Muse nói vội hoặc bị cắt giữa câu. "
          "Giờ mỗi lượt chỉ 7 đến 15 chữ, nói chậm vẫn kịp.",
          "3. **Lời nói = đúng chữ phụ đề.** Bản cũ cho nói dài hơn phụ đề, nên phụ đề tắt mà miệng vẫn còn nói.",
          "4. **Không chuyển cảnh giữa câu:** mỗi clip là một cảnh quay liền, lời cuối xong trước giây 9,4; chuyển cảnh 0,4 giây "
          "chỉ rơi vào khoảng lặng cuối clip. Câu đầu clip bắt đầu sau giây 0,5 (clip 7 sau giây 0,9 vì vào bằng tối dần 0,8 giây).",
          "5. **Anh Tư tươi vui, lém lỉnh:** cười, nháy mắt, nhún vai khi tới lượt pha trò; lúc người khác nói thì ngậm miệng, nghe nghiêm túc. Khánh Dư, trung sứ, người dẫn chuyện giữ nghiêm.",
          "6. **Người dẫn chuyện là giọng ngoài khung hình:** prompt ghi rõ không ai trên màn hình mấp máy môi khi dẫn chuyện nói. "
          "Trần Khánh Dư chỉ quay từ phía sau, không thấy miệng.",
          "7. Số liệu: \"năm trăm thuyền\" đổi thành \"hàng trăm thuyền\" vì các nguồn chép lệch nhau (500 đến 600 thuyền), "
          "đúng tiêu chuẩn kênh không nêu con số còn lệch.", "",
          "**Nếu Muse vẫn khớp nhầm miệng:** tạo riêng hai nửa clip (0-5 giây và 5-10 giây, mỗi nửa một người nói), đặt tên "
          "`bd1288-tap3-3a.mp4`, `3b`… rồi gửi em ghép.", "",
          "**Lịch sử (mức A/B):** tháng 12/1287 thủy quân Nguyên vượt biển qua Vân Đồn; Phó đô tướng quân Trần Khánh Dư không chặn "
          "được. Thượng hoàng sai trung sứ xiềng ông về kinh hỏi tội; ông xin khất vài ba ngày vì đoán đoàn thuyền lương đi sau không "
          "có quân giỏi hộ tống (*Toàn thư*). Lời Khánh Dư trong video là **phỏng theo ý sử chép**, không nhận là nguyên văn. Tập "
          "này dừng ở lúc chờ; trận đánh thuyền lương là tập 4.", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"{base}-{i}.mp4"
        lines = [f"- **{s0:.1f}–{s1:.1f}s · {('Dẫn chuyện' if w == 'narr' else 'Anh Tư' if w == 'tu' else 'Trần Khánh Dư' if w == 'kd' else 'Trung sứ')}:** "
                 f"\"{spoken(t)}\"" for w, s0, s1, t, _ in c["turns"]]
        md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{f}` · Bản TikTok: "
               + ("lấy đủ clip" if c["tiktok"] != "bo" else "bỏ (chỉ YouTube)"), "",
               "**Ai nói, lúc nào** (người kia im, ngậm miệng):", *lines, "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", video_prompt(c), "```", ""]
        extra = f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""
        plan.append(f"clip: {f} | {c['label']} | tiktok={c['tiktok']}{extra}")
        subs += [f"sub: {i} | {a}-{b} | {PREFIX[w]}{t}" for w, a, b, t, _ in c["turns"]]
    plan += [""] + subs
    with open(os.path.join(HERE, "_tap3_dang_bai.md"), encoding="utf-8") as fh:
        md += [fh.read().rstrip(), ""]
    md += [
           "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + "-cho-ta-ba-hom.md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
