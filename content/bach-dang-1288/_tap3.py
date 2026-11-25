#!/usr/bin/env python3
"""Bạch Đằng 1288, tập 3 "Cho ta ba hôm": bản đầy đủ dưới 2 phút: mỗi clip một người nói, các clip cùng cảnh khóa chung bối cảnh.
Chạy: python3 _tap3.py → bd1288-tap3-cho-ta-ba-hom.md + bd1288-tap3.plan.txt
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FACE = ("Anh Tư: the SAME man as in the attached reference image anh_tu_ref.png (same face, same age, same scar, same "
        "teeth, same hair): a Vietnamese man around 30 with deeply tanned skin, hair in a topknot with a faded brown cloth "
        "band, black-lacquered teeth, a thin scar across his left eyebrow and one chipped front tooth, a coarse dark-brown "
        "cotton tunic; he acts naturally like a real person, relaxed and good-humored, with small natural reactions (a glance, a sigh, a raised eyebrow, a faint smile); no grinning, no winking, no exaggerated faces")
BASE = ("Cinematic live-action, photorealistic, natural light, film grain, vertical 9:16. Vietnam, December 1287, Trần "
        "dynasty, Vân Đồn coast: soldiers in brown cotton tunics, hair in topknots, black-lacquered teeth. No modern "
        "objects, no on-screen text, no subtitles, no visible writing anywhere, ABSOLUTELY NO FLAGS OR BANNERS OF ANY KIND, "
        "no blood, no dead bodies, no children. Light, natural comedic tone like a documentary-style drama: the humor is in what Anh Tư says, not in his face; he smiles at most once, softly. The officials, the general and the envoy stay serious.")
V_TU = ("Anh Tư = a bright, slightly husky male voice around 30 with a natural Central Vietnamese (Huế) accent, natural and conversational, gentle dry humor, "
        "never shouting, the SAME voice in every clip")
V_NARR = ("Narrator = a calm, deep, slow male baritone with a Northern accent, documentary style, OFF-SCREEN voice-over: "
          "nobody on screen moves their lips while the narrator speaks")
V_KD = ("Trần Khánh Dư = a calm, steady male voice in his late 40s, slow and certain, Northern accent, clearly different "
        "from Anh Tư's voice; he is seen ONLY from behind, his mouth is never visible")
V_SU = "the envoy = a clipped, impatient male voice in his 50s, Northern accent, clearly different from Anh Tư's voice"
RULES = ("ONE VOICE ONLY: in this whole 10-second clip exactly ONE person speaks, {who}, and says ONE short line, "
         "completely, at a natural unhurried pace. Nobody else says a single word or makes any vocal sound; every other "
         "person on screen keeps his mouth CLOSED the whole time. The line is never split between two people and never "
         "continues in someone else's mouth. One continuous shot, NO cut inside this clip. The line ends before 9.0s; "
         "after that, silence.")
AUDIO = "Audio: {amb}. No background music. All dialogue in Vietnamese."

# CẢNH: mọi clip cùng cảnh dùng y nguyên đoạn mô tả này (cùng nơi, cùng giờ, cùng ánh sáng, cùng đồ vật, cùng vị trí người)
# và dùng chung MỘT ảnh khung đầu, để chuyển từ người nói này sang người nói kia mà bối cảnh vẫn đồng nhất.
SCENES = {
    "A": dict(name="Bờ đá Vân Đồn, ban ngày",
              lock=("SCENE A (keep IDENTICAL in every clip of this scene): a rocky shore at Vân Đồn, late morning, overcast "
                    "silver light, grey-green sea with white caps, a cold northeast wind, hundreds of wooden warships with "
                    "matting sails far out at sea moving left to right, two big dark limestone islands on the horizon, a "
                    "gnarled pine tree on the right edge of the rocks."),
              img=("Cinematic shot of a rocky shore at Vân Đồn, late morning, overcast silver light, grey-green sea with white "
                   "caps, hundreds of wooden warships with matting sails far out at sea, two dark limestone islands on the "
                   "horizon, a gnarled pine tree on the right edge of the rocks, {FACE}, standing on the rocks, realistic, vertical 9:16."),
              amb="sea waves, strong wind, distant drums"),
    "B": dict(name="Sân doanh trại, giữa trưa",
              lock=("SCENE B (keep IDENTICAL in every clip of this scene): the yard of a coastal military camp at Vân Đồn at "
                    "midday, flat grey daylight, packed earth ground, a row of brown thatched huts behind, a wooden weapon "
                    "rack with spears on the left, a tall bamboo fence and the grey sea beyond it, soldiers in brown tunics "
                    "walking in the far background. The court envoy wears a dark blue brocade robe and a black hat and holds a "
                    "rolled scroll; he stands facing the huts. Anh Tư stands opposite him with a coil of rope over his shoulder."),
              img=("Cinematic shot of the yard of a coastal military camp at midday, flat grey daylight, packed earth, brown "
                   "thatched huts behind, a wooden weapon rack with spears on the left, a bamboo fence and grey sea beyond, a "
                   "court envoy in a dark blue brocade robe and black hat holding a rolled scroll, facing {FACE}, who has a coil "
                   "of rope over his shoulder, realistic, vertical 9:16."),
              amb="camp murmuring, wind, distant sea"),
    "C": dict(name="Trước lều Trần Khánh Dư, chiều",
              lock=("SCENE C (keep IDENTICAL in every clip of this scene): in front of the general's large brown canvas tent "
                    "on a low bluff above the sea at Vân Đồn, mid-afternoon, warm low sunlight from the left, a small wooden "
                    "table with a clay teapot, a sand map with pebbles on the ground (no writing), the sea and two limestone "
                    "islands behind. Trần Khánh Dư wears a dark brown robe with a black sash, hair in a topknot, and is seen ONLY "
                    "from behind, standing by the table facing the sea. Anh Tư stands a few steps to the side, the coil of rope "
                    "in his hands."),
              img=("Cinematic shot in front of a large brown canvas tent on a low bluff above the sea, mid-afternoon warm low "
                   "sunlight from the left, a small wooden table with a clay teapot, a sand map with pebbles, two limestone "
                   "islands behind, a Trần general in a dark brown robe with a black sash seen only from behind facing the sea, "
                   "{FACE}, a few steps to the side holding a coil of rope, realistic, vertical 9:16."),
              amb="sea below, soft wind, a gull"),
    "D": dict(name="Đống lửa, đêm",
              lock=("SCENE D: night in the same camp, a small campfire on the rocks, sea and dark islands under the moon behind, "
                    "Anh Tư alone sitting on a rock by the fire."),
              img=("Cinematic shot at night by a small campfire on rocks, sea and dark islands under the moon behind, {FACE}, "
                   "sitting alone carving marks into a wooden stick, the coil of rope beside him, realistic, vertical 9:16."),
              amb="fire crackling, night insects, waves"),
    "E": dict(name="Bờ đá, hoàng hôn ngày thứ ba",
              lock=("SCENE E (keep IDENTICAL in every clip of this scene): the SAME rocky shore as scene A, with the same gnarled "
                    "pine tree, at sunset, orange sky, calm empty sea, no ships, the two limestone islands dark on the horizon."),
              img=("Cinematic shot of a rocky shore at sunset, orange sky, calm empty sea, two dark limestone islands on the "
                   "horizon, a gnarled pine tree on the right, {FACE}, standing on the rocks holding a coil of rope, realistic, vertical 9:16."),
              amb="gentle waves, evening birds"),
}

# Mỗi clip: một cảnh, MỘT người nói, MỘT câu (tối đa khoảng 15 chữ).
CLIPS = [
    dict(scene="A", who="narr", label="Vân Đồn · tháng 12/1287",
         line=(0.8, 8.2, "Tháng chạp năm 1287. / Thủy quân Nguyên vượt biển… / lọt qua Vân Đồn."),
         cam="wide aerial over the sea: the fleet sails past the islands; on the shore Anh Tư is a tiny figure seen from behind; no faces visible"),
    dict(scene="A", who="tu",
         line=(0.6, 8.4, "Hàng trăm thuyền giặc / đi qua… / mà không thuyền nào / chào em một câu!"),
         cam="medium shot of Anh Tư alone on the rocks watching the fleet pass, then turning to the camera with a faint smile"),
    dict(scene="B", who="su",
         line=(0.6, 8.2, "Thượng hoàng có lệnh: / xiềng Trần Khánh Dư, / giải về kinh hỏi tội!"),
         cam="the envoy faces the camera and reads from the scroll, stern; in the foreground Anh Tư is seen ONLY from behind (back of his head and shoulders, face never visible)"),
    dict(scene="B", who="tu",
         line=(0.6, 7.8, "Dạ… em đi bắt / một ông tướng… / bằng sợi dây này ạ?"),
         cam="reverse angle: close-up of Anh Tư alone in frame (the envoy is out of frame), glancing down at the coil of rope in his hands, then up at the envoy, a little unsure"),
    dict(scene="B", who="su",
         line=(0.6, 6.0, "Mày cầm xích. / Ông ấy tự đi."),
         cam="back to the envoy facing the camera, unimpressed; Anh Tư again seen ONLY from behind in the foreground"),
    dict(scene="C", who="tu",
         line=(0.6, 7.6, "Thưa ngài… / em xin phép… / trói ngài nhẹ thôi ạ."),
         cam="Anh Tư alone in frame beside the tent, bowing slightly and holding out the rope politely, a little awkward; the general is out of frame"),
    dict(scene="C", who="kd",
         line=(0.6, 8.4, "Theo quân pháp, / ta xin chịu tội. / Nhưng cho ta ba hôm… / để lập công."),
         cam="Trần Khánh Dư seen ONLY from behind at the table facing the sea, he raises three fingers; no other face in the frame"),
    dict(scene="C", who="kd",
         line=(0.6, 8.4, "Sau thuyền chiến của giặc / là thuyền lương, / không quân giỏi hộ tống. / Đánh tất phá được."),
         cam="from behind Trần Khánh Dư, he moves a pebble on the sand map and points out to sea; no other face in the frame"),
    dict(scene="C", who="tu",
         line=(0.6, 7.4, "Em đi bắt người… / mà người hẹn em / ba hôm!"),
         cam="close-up of Anh Tư alone in frame, looking at the rope, then at the camera, a short pause and a small sigh"),
    dict(scene="D", who="tu", chuyen="fadeblack:0.6",
         line=(0.6, 8.4, "Một hôm… hai hôm… / ba hôm… dây này / để trói ai đây?"),
         cam="Anh Tư alone by the fire carves one mark for each count, then glances at the rope beside him and looks at the camera"),
    dict(scene="E", who="narr", chuyen="fadeblack:0.6",
         line=(0.8, 7.6, "Ba hôm đó… / cả Vân Đồn cùng chờ / một đoàn thuyền lương."),
         cam="wide shot of the empty sea at sunset; Anh Tư seen small and from behind on the rocks; no faces visible"),
    dict(scene="E", who="tu",
         line=(0.6, 8.6, "Ba hôm nữa ông ấy / không về chịu tội… / thì em về chịu thay à?"),
         cam="Anh Tư turns from the empty sea to the camera, holding the rope, calm, with a faint resigned smile"),
]
WHO = {"tu": "ANH TƯ", "kd": "TRẦN KHÁNH DƯ (seen only from behind)", "su": "THE ENVOY", "narr": "the NARRATOR (off-screen voice-over, nobody on screen moves their lips)"}
NAME = {"tu": "Anh Tư", "kd": "Trần Khánh Dư", "su": "Trung sứ", "narr": "Dẫn chuyện"}
VOICE = {"tu": V_TU, "kd": V_KD, "su": V_SU, "narr": V_NARR}
PREFIX = {"kd": "Trần Khánh Dư: / ", "su": "Trung sứ: / ", "tu": "", "narr": ""}


def spoken(t):
    return t.replace(" / ", " ")


def video_prompt(c):
    a, b, text = c["line"]
    sc = SCENES[c["scene"]]
    face = FACE + "." if c["who"] == "tu" or c["scene"] in "BC" else ""
    return " ".join(x for x in [
        BASE, sc["lock"], face, RULES.format(who=WHO[c["who"]]),
        f"0-{a:.1f}s: silence. {a:.1f}-{b:.1f}s: ONLY {WHO[c['who']]} speaks: \"{spoken(text)}\" {b:.1f}-10s: silence, hold the shot.",
        f"Camera: {c['cam']}.", f"VOICE: {VOICE[c['who']]}.", AUDIO.format(amb=sc["amb"])] if x)


def main():
    base = "bd1288-tap3"
    plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4  (một bản dùng chung TikTok, YouTube, Facebook)",
            "hook: POV: Đi bắt tướng / tướng xin khất / ba hôm", "end: Follow để xem / Biển trả lương bằng gạo →",
            "nhan: AI tái hiện · lời thoại hư cấu", "end_giay: 1.6", "chuyen: fade 0.3", ""]
    subs = []
    n = len(CLIPS)
    trans = sum(float(c["chuyen"].split(":")[1]) if c.get("chuyen") else 0.3 for c in CLIPS[1:])
    total = n * 10 - trans
    md = ["# Bạch Đằng 1288, tập 3: Cho ta ba hôm (bản đầy đủ)", "",
          f"**Loạt:** Bạch Đằng 1288, 10 tập · **{n} clip, khoảng {int(total // 60)} phút {int(total % 60)} giây**, một bản dùng "
          "chung TikTok, YouTube, Facebook (dưới 2 phút, đủ hội thoại).", "",
          f"**File Muse đặt tên:** `bd1288-tap3-1..{n}.mp4` · **Giọng:** Anh Tư giọng Huế, tự nhiên, hài nhẹ; Khánh Dư, trung sứ giọng Bắc, "
          "nghiêm; dẫn chuyện giọng Bắc trầm.", "",
          "## Cách làm cho hội thoại không lỗi và bối cảnh đồng nhất", "",
          "1. **Mỗi clip 10 giây chỉ MỘT người nói, MỘT câu.** Hai người đối đáp thì mỗi người một clip liền nhau, chuyển cảnh "
          "nhẹ 0,3 giây (hòa hình), như phim cắt qua lại giữa hai người.",
          "2. **Khóa bối cảnh theo cảnh (A đến E).** Các clip cùng cảnh dùng **y nguyên đoạn `SCENE …`** trong prompt: cùng nơi, "
          "cùng giờ, cùng ánh sáng, cùng đồ vật (cây thông, lều, bàn trà, giá giáo…), cùng trang phục, cùng vị trí người đứng.",
          "3. **Dùng chung một ảnh khung đầu cho cả cảnh:** tạo ảnh của cảnh một lần, đính kèm cho mọi clip của cảnh đó (kèm "
          "`anh_tu_ref.png`). Nếu Muse cho chọn ảnh khung đầu từ video, lấy **khung cuối của clip trước** làm khung đầu clip sau "
          "(gửi em clip, em tách khung cuối bằng FFmpeg cho anh).",
          "4. **Người khác nói thì mặt Anh Tư không trong khung** (chỉ thấy lưng hoặc ra khỏi khung); Khánh Dư luôn quay từ phía sau.",
          "5. **Câu xong trước giây 9**, sau đó im lặng, nên chuyển cảnh không cắt chữ.",
          "6. Đổi cảnh (sang đêm, sang ngày thứ ba) thì tối dần 0,6 giây.", "",
          "**Lịch sử (mức A/B):** tháng 12/1287 thủy quân Nguyên vượt biển qua Vân Đồn; Phó đô tướng quân Trần Khánh Dư không chặn "
          "được. Thượng hoàng sai trung sứ xiềng ông về kinh hỏi tội; ông xin khất vài ba ngày vì đoán đoàn thuyền lương đi sau không "
          "có quân giỏi hộ tống (*Toàn thư*). Lời Khánh Dư là **phỏng theo ý sử chép**, không nhận là nguyên văn. Câu \"Mày cầm "
          "xích. Ông ấy tự đi.\" của trung sứ là hư cấu. Tập này dừng ở lúc chờ; trận đánh thuyền lương là tập 4.", "",
          "## Xem nhanh: toàn bộ hội thoại", "", "| Clip | Cảnh | Người nói (duy nhất) | Câu |", "|---|---|---|---|"]
    md += [f"| {i} | {c['scene']} · {SCENES[c['scene']]['name']} | {NAME[c['who']]} | {spoken(c['line'][2])} |"
           for i, c in enumerate(CLIPS, 1)] + [""]
    md += ["## Ảnh khung đầu từng cảnh (tạo một lần, dùng chung cho các clip cùng cảnh)", ""]
    for k, sc in SCENES.items():
        clips = ", ".join(str(i) for i, c in enumerate(CLIPS, 1) if c["scene"] == k)
        md += [f"**Cảnh {k} · {sc['name']}** (clip {clips}): lưu thành `bd1288-tap3-canh-{k}.png`", "```",
               sc["img"].format(FACE=FACE), "```", ""]
    for i, c in enumerate(CLIPS, 1):
        f = f"{base}-{i}.mp4"
        a, b, text = c["line"]
        md += [f"## Clip {i} · cảnh {c['scene']}", f"File Muse đặt tên: `{f}` · Ảnh khung đầu: `bd1288-tap3-canh-{c['scene']}.png`"
               + (" + `anh_tu_ref.png`" if c["who"] == "tu" or c["scene"] in "BC" else ""), "",
               f"**Chỉ {NAME[c['who']]} nói ({a:.1f}–{b:.1f}s):** \"{spoken(text)}\"", "",
               "**Video (Muse)**", "```", video_prompt(c), "```", ""]
        extra = f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""
        plan.append(f"clip: {f} | {c.get('label', '')}{extra}")
        subs.append(f"sub: {i} | {a}-{b} | {PREFIX[c['who']]}{text}")
    plan += [""] + subs
    with open(os.path.join(HERE, "_tap3_dang_bai.md"), encoding="utf-8") as fh:
        md += [fh.read().rstrip(), ""]
    md += ["## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
    for name, lines in ((base + "-cho-ta-ba-hom.md", md), (base + ".plan.txt", plan)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(name, round(total, 1))


if __name__ == "__main__":
    main()
