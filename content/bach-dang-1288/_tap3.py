#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 3 "Cho ta ba hôm": bản MỘT NGƯỜI NÓI MỖI CLIP (hết lỗi câu nói nhảy sang miệng người khác).
Chạy: python3 _tap3.py → bd1288-tap3-cho-ta-ba-hom.md + bd1288-tap3.plan.txt
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FACE = ("Anh Tư: the SAME man as in the attached reference image anh_tu_ref.png (same face, same age, same scar, same "
        "teeth, same hair): a Vietnamese man around 30 with deeply tanned skin, hair in a topknot with a faded brown cloth "
        "band, black-lacquered teeth, a thin scar across his left eyebrow and one chipped front tooth, a coarse dark-brown "
        "cotton tunic; he is cheerful, playful and cheeky, with lively natural expressions (smiles, a quick grin when he jokes, raised eyebrows, a wink, a shrug), like a funny real person telling a story to a friend, never over-the-top")
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
RULES = ("ONE VOICE ONLY: in this whole 10-second clip exactly ONE person speaks, {who}, and says ONE short line, "
         "completely, at a natural unhurried pace. Nobody else says a single word or makes any vocal sound; every other "
         "person on screen keeps his mouth CLOSED the whole time. The line is never split between two people and never "
         "continues in someone else's mouth. One continuous shot, NO cut or scene change inside this clip. The line ends "
         "before 9.0s; after that, silence.")
AUDIO = "Audio: {amb}. No background music. All dialogue in Vietnamese."

# Mỗi clip: MỘT người nói, MỘT câu ngắn (tối đa khoảng 14 chữ). Hai người cần đối đáp thì tách ra hai clip.
CLIPS = [
    dict(name="Thuyền không chào", label="Vân Đồn · tháng 12/1287", tiktok="0-9.3", who="tu",
         line=(0.6, 8.4, "Hàng trăm thuyền giặc / đi qua… mà không thuyền nào / chào em một câu!"),
         where="a rocky coast at Vân Đồn by day, hundreds of wooden warships far out at sea",
         cam="Anh Tư alone on the rocks waves cheekily at the distant fleet, then turns to the camera with a big amused grin and speaks",
         img=f"Cinematic shot on a rocky coast by day, hundreds of wooden warships far out at sea, {FACE}, waving cheekily at the fleet, realistic, vertical 9:16.",
         amb="sea waves, wind, distant drums", voice=V_TU),
    dict(name="Lệnh xiềng tướng", label="", tiktok="bo", who="su",
         line=(0.6, 7.8, "Giặc lọt qua Vân Đồn! / Xiềng Khánh Dư, / giải về kinh hỏi tội!"),
         where="a coastal military camp at Vân Đồn by day",
         cam="a stern court envoy in a dark brocade robe faces the camera and reads the order from a rolled scroll; in the foreground Anh Tư is seen ONLY from behind (back of his head and shoulders, his face never visible), holding a coil of rope; at the end his shoulders give a small nervous shrug",
         img="Cinematic shot in a coastal military camp by day, a stern court envoy in a dark brocade robe holding a rolled scroll facing the camera, in the foreground a soldier seen only from behind holding a coil of rope, realistic, vertical 9:16.",
         amb="camp murmuring, sea wind", voice=V_SU),
    dict(name="Cho ta ba hôm", label="", tiktok="0.3-9.3", who="kd",
         line=(0.6, 7.6, "Ta xin chịu tội. / Nhưng cho ta ba hôm… / để lập công."),
         where="the shore of Vân Đồn by day",
         cam="Trần Khánh Dư in a dark robe, seen ONLY from behind, stands alone on the shore facing the sea and raises three fingers; no other person's face is in the frame",
         img="Cinematic shot on a rocky shore by day, a Trần general in a dark robe seen only from behind, standing alone facing the sea, raising three fingers, realistic, vertical 9:16.",
         amb="sea waves, soft wind", voice=V_KD),
    dict(name="Người hẹn em ba hôm", label="", tiktok="0.3-9.3", who="tu",
         line=(0.6, 7.4, "Em đi bắt người… / mà người hẹn em / ba hôm!"),
         where="the edge of a coastal military camp at Vân Đồn by day",
         cam="close-up of Anh Tư alone, holding up the coil of rope, looking at it and then at the camera with a comically confused grin and a shrug",
         img=f"Close-up in a coastal camp by day, {FACE}, alone, holding up a coil of rope with a comically confused grin, realistic, vertical 9:16.",
         amb="camp murmuring, sea wind", voice=V_TU),
    dict(name="Thuyền lương đi sau", label="", tiktok="bo", who="kd",
         line=(0.6, 7.6, "Sau thuyền chiến / là thuyền lương. / Đánh tất phá được."),
         where="a high rocky cliff at Vân Đồn at dusk above the sea",
         cam="Trần Khánh Dư in a dark robe, seen ONLY from behind, alone on the cliff, points far out to sea; no other person's face is in the frame",
         img="Cinematic shot on a high rocky cliff at dusk, a Trần general in a dark robe seen only from behind, alone, pointing far out to sea, realistic, vertical 9:16.",
         amb="sea waves, dusk wind", voice=V_KD),
    dict(name="Đếm ba hôm", label="", tiktok="bo", who="tu",
         line=(0.6, 8.4, "Một hôm… hai hôm… / ba hôm… dây này / để trói ai đây?"),
         where="a coastal camp at Vân Đồn at night, a small fire",
         cam="Anh Tư sits alone by the fire carving one mark into a stick for each count, then dangles the rope and smiles mischievously at the camera",
         img=f"Cinematic shot in a coastal camp at night, {FACE}, sitting alone by a small fire carving marks into a wooden stick, realistic, vertical 9:16.",
         amb="fire crackling, night insects, sea wind", voice=V_TU),
    dict(name="Chịu thay", label="", tiktok="0.6-10", who="tu", chuyen="fadeblack:0.8",
         line=(1.0, 8.8, "Ba hôm nữa ông ấy / không về chịu tội… / thì em về chịu thay à?"),
         where="a rocky coast at Vân Đồn at dusk, an empty sea",
         cam="Anh Tư alone on the rocks turns from the empty sea to the camera, holding the rope, with a playful worried smile and a little shrug",
         img=f"Cinematic shot at dusk on a rocky coast, {FACE}, alone, holding a coil of rope, turning from the empty sea toward the camera, realistic, vertical 9:16.",
         amb="dusk birds, sea waves, soft wind", voice=V_TU),
]
WHO = {"tu": "ANH TƯ", "kd": "TRẦN KHÁNH DƯ (seen only from behind)", "su": "THE ENVOY"}
NAME = {"tu": "Anh Tư", "kd": "Trần Khánh Dư", "su": "Trung sứ"}
PREFIX = {"kd": "Trần Khánh Dư: / ", "su": "Trung sứ: / ", "tu": ""}


def spoken(t):
    return t.replace(" / ", " ")


def video_prompt(c):
    a, b, text = c["line"]
    face = FACE + "." if c["who"] == "tu" else ""
    return " ".join(x for x in [
        BASE, f"Setting: {c['where']}.", face, RULES.format(who=WHO[c["who"]]),
        f"0-{a:.1f}s: silence. {a:.1f}-{b:.1f}s: ONLY {WHO[c['who']]} speaks: \"{spoken(text)}\" {b:.1f}-10s: silence, hold the shot.",
        f"Camera: {c['cam']}.", f"VOICE: {c['voice']}.", AUDIO.format(amb=c["amb"])] if x)


def main():
    base = "bd1288-tap3"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (ra {base}-youtube.mp4 và {base}-tiktok.mp4)",
            "hook: POV: Đi bắt tướng / tướng xin khất / ba hôm", "end: Follow để xem / Biển trả lương bằng gạo →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.4", ""]
    subs = []
    md = ["# Bạch Đằng 1288, tập 3: Cho ta ba hôm (mỗi clip một người nói)", "",
          "**Loạt:** Bạch Đằng 1288, 10 tập · **YouTube** khoảng 67 giây (đủ 7 clip) · **TikTok** khoảng 35 giây (clip 1-3-4-7)",
          "", "**File Muse đặt tên:** `bd1288-tap3-1..7.mp4` · **Giọng:** Anh Tư giọng Huế, tươi vui; Khánh Dư, trung sứ giọng Bắc, nghiêm.", "",
          "## Cách chống lỗi câu nói nhảy sang miệng người khác", "",
          "1. **Mỗi clip 10 giây chỉ MỘT người nói, MỘT câu ngắn** (7 đến 14 chữ). Không còn chỗ nào để Muse chuyển giọng giữa chừng.",
          "2. **Hai người đối đáp thì tách thành hai clip liền nhau:** Khánh Dư xin ba hôm ở clip 3, Anh Tư đáp ở clip 4.",
          "3. **Khi người khác nói, mặt Anh Tư không có trong khung hình** (Khánh Dư đứng một mình, quay từ phía sau; trung sứ nói thì Anh Tư "
          "chỉ thấy lưng). Không có cái miệng nào khác để Muse khớp nhầm.",
          "4. **Câu nói xong trước giây 9**, sau đó im lặng, nên chuyển cảnh không cắt mất chữ cuối.",
          "5. **Anh Tư tươi vui:** cười toe, nháy mắt, nhún vai ở các clip của mình (1, 4, 6, 7).", "",
          "**Lịch sử (mức A/B):** tháng 12/1287 thủy quân Nguyên vượt biển qua Vân Đồn; Phó đô tướng quân Trần Khánh Dư không chặn "
          "được. Thượng hoàng sai trung sứ xiềng ông về kinh hỏi tội; ông xin khất vài ba ngày vì đoán đoàn thuyền lương đi sau không "
          "có quân giỏi hộ tống (*Toàn thư*). Lời Khánh Dư trong video là **phỏng theo ý sử chép**, không nhận là nguyên văn. Tập "
          "này dừng ở lúc chờ; trận đánh thuyền lương là tập 4.", "",
          "## Xem nhanh: clip nào ai nói", "", "| Clip | Người nói (duy nhất) | Câu |", "|---|---|---|"]
    md += [f"| {i} | {NAME[c['who']]} | {spoken(c['line'][2])} |" for i, c in enumerate(CLIPS, 1)] + [""]
    for i, c in enumerate(CLIPS, 1):
        f = f"{base}-{i}.mp4"
        a, b, text = c["line"]
        md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{f}` · Bản TikTok: "
               + ("lấy clip này" if c["tiktok"] != "bo" else "bỏ (chỉ YouTube)"), "",
               f"**Chỉ {NAME[c['who']]} nói ({a:.1f}–{b:.1f}s):** \"{spoken(text)}\"", "",
               "**Ảnh khung đầu**", "```", c["img"], "```", "",
               "**Video (Muse)**", "```", video_prompt(c), "```", ""]
        extra = f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""
        plan.append(f"clip: {f} | {c['label']} | tiktok={c['tiktok']}{extra}")
        subs.append(f"sub: {i} | {a}-{b} | {PREFIX[c['who']]}{text}")
    plan += [""] + subs
    with open(os.path.join(HERE, "_tap3_dang_bai.md"), encoding="utf-8") as fh:
        md += [fh.read().rstrip(), ""]
    md += ["## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + "-cho-ta-ba-hom.md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name)


if __name__ == "__main__":
    main()
