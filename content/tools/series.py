"""Sinh file prompt dán thẳng (*.md) và file chữ trên video (*.plan.txt) cho một loạt POV.

Mỗi loạt có một file _nguon.py định nghĩa EPISODES rồi gọi build(EPISODES, thư_mục).
Xem content/bach-dang/_nguon.py làm mẫu.
"""
import os

POV = ("First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, "
       "the viewer's own hands sometimes visible at the bottom of the frame, live-action realistic, "
       "cinematic natural lighting, vertical 9:16. No modern objects, no on-screen text. "
       "No children in close-up, no children's faces, no children crying or in distress; "
       "any child appears only from behind or at a distance. "
       "No modern national flags anywhere (never a red flag with a yellow star); no flags at all unless the "
       "scene describes a period-accurate one.")
# Giọng mặc định: Bắc (người xem chê giọng Nam trong trận Bạch Đằng, Thăng Long). Tập ở miền Trung, miền Nam ghi đè bằng
# khóa giong="Central Vietnamese (Bình Định) accent" hoặc "Southern Vietnamese (Mekong delta) accent".
ACCENT = "a natural Northern Vietnamese (Hà Nội) accent"
AUDIO = ("Audio: natural ambient sound, Vietnamese dialogue spoken naturally with lip sync in "
         f"{ACCENT}, no background music.")
# Người xem chê "cọc bé như que tăm": mọi cảnh có cọc tự kèm mô tả cỡ cọc và cách đóng (xem nghien-cuu/chuan-hinh-anh-quan-doi.md).
STAKE_SPEC = ("The stakes are massive: whole ironwood tree trunks about 20 to 30 cm thick (as thick as a man's thigh) "
              "and 2.5 to 3 m long, sharpened at the tip, driven deep into the riverbed mud at low tide by teams of "
              "several men working together, lifting and dropping a heavy wooden ram on ropes or standing on a lashed "
              "crossbar to press each stake down; never thin sticks, never small hand hammers.")
DRAGON_SPEC = ("Any dragon shown is in Lý dynasty style: a slender, sinuous, snake-like body in continuous wave-like "
               "loops, a small head with a long curling crest and no horns; never a heavy horned Chinese Qing dragon.")
# Bảng giọng cố định: cùng một nhân vật luôn nhận đúng một mô tả giọng ở mọi clip, mọi tập (Muse tạo tiếng riêng
# từng clip nên dễ đổi giọng). Khóa = từ khóa tìm trong prompt clip; giá trị = (tên hiển thị, mô tả giọng).
# Mô tả chỉ nói âm sắc, tuổi, nhịp nói; vùng miền do ACCENT / khóa giong quyết định.
VOICES = [
    ("Anh Tư", ("Anh Tư", "a bright, slightly husky male voice around 30, quick and cheerful, a little cheeky when "
                "joking, the SAME voice in every clip")),
    ("narrator", ("người dẫn chuyện", "a calm, deep, slow male baritone, documentary style, warm and serious, the SAME "
                  "narrator voice in every video of the channel")),
    ("Anh Tư's mother", ("mẹ Anh Tư", "a sharp, quick-tongued woman's voice in her 50s, slightly raspy")),
    ("Mẹ Anh Tư", ("mẹ Anh Tư", "a sharp, quick-tongued woman's voice in her 50s, slightly raspy")),
    ("Nguyễn Nhạc", ("Nguyễn Nhạc", "a jovial, round, booming male voice in his late 30s, unhurried")),
    ("Ngô Quyền", ("Ngô Quyền", "a low, steady, authoritative male voice around 40, few words, never shouting")),
    ("Thái sư", ("Trần Thủ Độ", "an old, dry, very calm male voice in his 60s, slow and unshakeable")),
    ("officer", ("viên chỉ huy", "a gruff, clipped male voice in his 40s, short commands, clearly different from Anh "
                 "Tư's voice")),
    ("messenger", ("sứ giả, người đưa tin", "a formal, crisp male voice, slightly breathless")),
    ("envoy", ("sứ giả, người đưa tin", "a formal, crisp male voice, slightly breathless")),
    ("old woman", ("bà cụ", "a warm, raspy elderly woman's voice")),
    ("old farmer", ("ông cụ", "a creaky, grumpy elderly man's voice")),
    ("interpreter", ("người phiên dịch", "a nervous, precise, thin male voice in his 30s")),
]

VOICE_EN = {"người dẫn chuyện": "Narrator", "mẹ Anh Tư": "Anh Tư's mother", "viên chỉ huy": "The officer",
            "sứ giả, người đưa tin": "The messenger or envoy", "bà cụ": "The old woman", "ông cụ": "The old farmer",
            "người phiên dịch": "The interpreter", "Trần Thủ Độ": "Thái sư Trần Thủ Độ"}


def voices_prompt(vl):
    if not vl:
        return ""
    return ("VOICES (keep each character's voice exactly the same in every clip; each speaking character sounds "
            "clearly different from the others): "
            + "; ".join(f"{VOICE_EN.get(n, n)} = {d}" for n, d in vl) + ". ")


def voice_lines(text, extra=None):
    """Mô tả giọng cho các nhân vật có mặt trong clip (theo từ khóa) + giọng riêng của tập (khóa voices)."""
    found, seen = [], set()
    for key, (name, desc) in VOICES:
        if key.lower() in text.lower() and name not in seen:
            found.append((name, desc)); seen.add(name)
    for name, desc in (extra or {}).items():
        if name.lower() in text.lower() and name not in seen:
            found.append((name, desc)); seen.add(name)
    return found


AI_TAG = "AI tái hiện · lời thoại hư cấu"
AI_TAG_LEGEND = "AI tái hiện · theo truyền thuyết"
TAGS = "#povlichsu #POV #lichsuvietnam #xuhuong #fyp"
# Clip có noi=True: nối liền cảnh với clip trước (ảnh khung đầu = khung cuối clip trước, cắt bằng tools/khung-cuoi.py)
NOI_NOTE = '**Nối cảnh với clip trước:** tạo clip trước xong, chạy `python3 ../tools/khung-cuoi.py <file clip trước>` (hoặc gửi clip cho mình cắt), rồi dùng ảnh `...-cuoi.png` làm **ảnh khung đầu** cho clip này. Prompt ảnh bên dưới chỉ để dự phòng.'
CONT = 'Continue seamlessly from the previous shot: the first frame is exactly the last frame of the previous clip, same people, clothes, light and camera position.'
# Mặc định khi tập không tự khai báo. Từng tập có thể ghi đè bằng các khóa:
# tt_title, hooks_alt (list), pin, yt_title, yt_tags, yt_pin, yt_desc_extra.
# Tập: visual="..." (đoạn chuẩn trang phục/thuyền/cờ in vào file .md), md_frozen=True (file .md là bản cuối đã quay,
#      không ghi đè). Clip: setting="..." (bối cảnh riêng cho clip, thay bối cảnh chung của tập).
# Mỗi clip có thể thêm chuyen="fadeblack:0.8" (chuyển cảnh vào clip đó; mặc định fade 0.4 của tools/tiktok.py).
PIN_DEFAULT = "Bạn đoán đúng cái kết từ giây thứ mấy? 👇 Follow để xem tập tiếp theo nhé!"
YT_DESC_EXTRA = ("Video do AI tạo, dựa trên sử liệu; nhân vật và lời thoại là hư cấu. "
                 "Đăng ký kênh để xem mỗi ngày một ngày sống ở Đại Việt.")
YT_TAGS_BASE = ["lịch sử việt nam", "pov lịch sử", "pov", "đại việt", "sử việt", "shorts", "hài lịch sử"]


# Độ dài chuẩn từ 19/11/2026 (anh duyệt): TikTok 30–35 giây, YouTube 60–70 giây, linh động theo video.
# Tập mới đặt muc=MUC_MOI; build() tính thời lượng sau chuyển cảnh và cảnh báo nếu lệch khoảng.
MUC_MOI = {"youtube": (60, 70), "tiktok": (30, 35)}


def _tran(c):
    """Thời lượng chuyển cảnh vào clip c (mặc định fade 0.4; 'cat' = 0)."""
    ch = c.get("chuyen") or ""
    if ch.startswith("cat"):
        return 0.0
    return float(ch.split(":")[1]) if ":" in ch else 0.4


def thoi_luong(clips, ban):
    """Ước tính giây của bản 'youtube' (đủ clip) hoặc 'tiktok' (theo tiktok=) sau khi trừ chuyển cảnh."""
    tong, dung = 0.0, []
    for c in clips:
        cut = c.get("tiktok")
        if ban == "tiktok" and cut == "bo":
            continue
        tong += 10 if (ban == "youtube" or not cut) else float(cut.split("-")[1]) - float(cut.split("-")[0])
        dung.append(c)
    return tong - sum(_tran(c) for c in dung[1:])


def build(episodes, here, series_tag="", note="", unit="Phần", file_unit="phan"):
    lines = []
    for n, ep in enumerate(episodes, 1):
        base = f"{file_unit}-{n}-{ep['slug']}"
        cuts = [c.get("tiktok") for c in ep["clips"]]
        yt_len = 10 * len(cuts)
        tt_len = sum(0 if c == "bo" else (10 if c is None else
                     float(c.split("-")[1]) - float(c.split("-")[0])) for c in cuts)
        md = [f"# {unit} {n}: {ep['title']}", "",
              f"**Độ dài:** {ep['length']}", ""]
        if any(c is not None for c in cuts):
            md += [f"**Hai bản từ cùng một bộ clip:** YouTube Shorts {yt_len:.0f} giây (đủ clip) · "
                   f"TikTok {tt_len:.0f} giây (rút gọn theo ghi chú \"Bản TikTok\" ở từng clip).", ""]
        md += [
              "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", ""]
        if note:
            md += [note, ""]
        md += [ep["history"], ""]
        allv = voice_lines(" ".join(f"{c.get('setting', ep['setting'])} {c['vid']}" for c in ep["clips"]), ep.get("voices"))
        if allv:
            md += ["**Giọng nhân vật (đã chèn sẵn vào prompt từng clip, giữ nguyên ở mọi clip):**", ""]
            md += [f"- **{n}:** {d}" for n, d in allv]
            md += ["", "Nếu Muse cho chọn hoặc tải **giọng tham chiếu** (voice reference), hãy dùng đúng một giọng cho mỗi "
                   "nhân vật ở mọi clip, nhất là Anh Tư và người dẫn chuyện. Xem `../nghien-cuu/giong-nhan-vat.md`.", ""]
        if ep.get("visual"):             # chuẩn trang phục, thuyền, cờ dùng chung cả tập (xem nghien-cuu/chuan-hinh-anh-quan-doi.md)
            md += [ep["visual"], ""]
        plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4"
                + (f"  (ra {base}-youtube.mp4 và {base}-tiktok.mp4)" if any(
                    c.get("tiktok") for c in ep["clips"]) else ""),
                f"hook: {ep['hook']}", f"end: {ep['end']}",
                f"nhan: {AI_TAG_LEGEND if ep.get('legend') else AI_TAG}"]
        if ep.get("end_secs"):
            plan.append(f"end_giay: {ep['end_secs']}")
        plan.append("")
        subs = []
        for i, c in enumerate(ep["clips"], 1):
            fname = f"{ep['prefix']}-{i}.mp4"
            # clip có thể ghi đè bối cảnh riêng (ví dụ cảnh chỉ có một phe: liệt kê rõ ai có, ai tuyệt đối không có)
            scene = f"{c.get('setting', ep['setting'])} {c['vid']}".lower()
            audio = AUDIO.replace(ACCENT, ep["giong"]) if ep.get("giong") else AUDIO
            vl = voice_lines(f"{c.get('setting', ep['setting'])} {c['vid']}", ep.get("voices"))
            voices = voices_prompt(vl)
            video = (f"{POV} {c.get('setting', ep['setting'])} " + (f"{CONT} " if c.get("noi") else "")
                     + f"{c['vid']} " + (f"{STAKE_SPEC} " if "stake" in scene else "")
                     + (f"{DRAGON_SPEC} " if "dragon" in scene else "") + voices + audio)
            cut = c.get("tiktok")
            cut_note = ("" if cut is None else
                        "**Bản TikTok:** bỏ clip này." if cut == "bo" else
                        f"**Bản TikTok:** chỉ dùng giây {cut.replace('-', ' đến ')} của clip này.")
            md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{fname}`", ""]
            if cut_note:
                md += [cut_note, ""]
            if c.get("noi"):
                md += [NOI_NOTE, ""]
            md += [
                   "**Ảnh khung đầu**", "```", c["img"], "```", "",
                   "**Video (Muse)**", "```", video, "```", ""]
            plan.append(f"clip: {fname} | {c['label']}" + (f" | tiktok={cut}" if cut else "")
                        + (f" | chuyen={c['chuyen']}" if c.get("chuyen") else ""))
            subs += [f"sub: {i} | {a}-{b} | {t}" for a, b, t in c["subs"]]
        plan += [""] + subs
        tags = " ".join(t for t in (TAGS, series_tag, ep["tags"]) if t)
        hook_line = ep["hook"].replace(" / ", " ")
        tt_title = ep.get("tt_title", hook_line)
        pin = ep.get("pin", PIN_DEFAULT)
        md += ["## Đăng TikTok", "",
               "**Hook** (chữ to ở giây đầu, đã có sẵn trong video; dùng luôn làm chữ trên ảnh bìa):",
               "```", hook_line, "```", ""]
        if ep.get("hooks_alt"):
            md += ["Hook dự phòng (nếu đăng lại hoặc muốn đổi ảnh bìa):", "```",
                   "\n".join(h.replace(" / ", " ") for h in ep["hooks_alt"]), "```", ""]
        md += ["**Tiêu đề** (ô Tiêu đề, hoặc dòng đầu của mô tả nếu không có ô này):", "```", tt_title, "```", "",
               "**Mô tả và hashtag:**", "```", ep["caption"], tags, "```", "",
               "**Bình luận ghim** (đăng xong tự bình luận rồi ghim lên đầu):", "```", pin, "```", "",
               "Khi đăng: bật nhãn \"Nội dung do AI tạo\".", ""]
        if any(c is not None for c in cuts):
            yt_title = ep.get("yt_title", hook_line)
            yt_hash = " ".join(t for t in tags.split() if t not in ("#fyp", "#xuhuong"))
            yt_tags = ep.get("yt_tags") or ", ".join(dict.fromkeys(
                [t.lstrip("#") for t in tags.split() if t not in ("#fyp", "#xuhuong", "#POV")] + YT_TAGS_BASE))
            yt_pin = ep.get("yt_pin", pin.replace("Follow", "Đăng ký").replace("follow", "đăng ký"))
            md += ["## Đăng YouTube Shorts (bản đầy đủ)", "",
                   "**Tiêu đề** (tối đa 100 ký tự):", "```", f"{yt_title} #Shorts", "```", "",
                   "**Mô tả:**", "```", ep["caption"], "", ep.get("yt_desc_extra", YT_DESC_EXTRA), "",
                   f"#Shorts {yt_hash}", "```", "",
                   "**Thẻ** (ô Thẻ/Tags trong \"Hiện thêm\", dán nguyên dòng):", "```", yt_tags, "```", "",
                   "**Bình luận ghim:**", "```", yt_pin, "```", "",
                   "Khi đăng: ở mục \"Nội dung bị thay đổi\" (Altered content) chọn **Có**, vì video do AI tạo.", ""]
        md += [
               "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
        md_path = os.path.join(here, base + ".md")
        if ep.get("md_frozen") and os.path.isfile(md_path):
            pass                         # bản cuối đã dùng để quay: giữ nguyên, không ghi đè
        else:
            with open(md_path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(md))
        with open(os.path.join(here, base + ".plan.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(plan) + "\n")
        lines.append(f"{base}: {len(ep['clips'])} clip")
        if ep.get("muc"):
            for ban, (lo, hi) in ep["muc"].items():
                t = thoi_luong(ep["clips"], ban)
                lines.append(f"  {ban} ≈ {t:.1f} giây" + ("" if lo <= t <= hi else f"  ⚠ NGOÀI KHOẢNG {lo}–{hi} giây"))
    print("\n".join(lines))
