"""Sinh file prompt dán thẳng (*.md) và file chữ trên video (*.plan.txt) cho một loạt POV.

Mỗi loạt có một file _nguon.py định nghĩa EPISODES rồi gọi build(EPISODES, thư_mục).
Xem content/bach-dang/_nguon.py làm mẫu.
"""
import os

POV = ("First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, "
       "the viewer's own hands sometimes visible at the bottom of the frame, live-action realistic, "
       "cinematic natural lighting, vertical 9:16. No modern objects, no on-screen text. "
       "No children in close-up, no children's faces, no children crying or in distress; "
       "any child appears only from behind or at a distance.")
AUDIO = "Audio: natural ambient sound, Vietnamese dialogue spoken naturally with lip sync, no background music."
TAGS = "#povlichsu #POV #lichsuvietnam #xuhuong #fyp"
# Mặc định khi tập không tự khai báo. Từng tập có thể ghi đè bằng các khóa:
# tt_title, hooks_alt (list), pin, yt_title, yt_tags, yt_pin, yt_desc_extra.
PIN_DEFAULT = "Bạn đoán đúng cái kết từ giây thứ mấy? 👇 Follow để xem tập tiếp theo nhé!"
YT_DESC_EXTRA = ("Video do AI tạo, dựa trên sử liệu; nhân vật và lời thoại là hư cấu. "
                 "Đăng ký kênh để xem mỗi ngày một ngày sống ở Đại Việt.")
YT_TAGS_BASE = ["lịch sử việt nam", "pov lịch sử", "pov", "đại việt", "sử việt", "shorts", "hài lịch sử"]


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
        plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4"
                + (f"  (ra {base}-youtube.mp4 và {base}-tiktok.mp4)" if any(
                    c.get("tiktok") for c in ep["clips"]) else ""),
                f"hook: {ep['hook']}", f"end: {ep['end']}"]
        if ep.get("end_secs"):
            plan.append(f"end_giay: {ep['end_secs']}")
        plan.append("")
        subs = []
        for i, c in enumerate(ep["clips"], 1):
            fname = f"{ep['prefix']}-{i}.mp4"
            video = f"{POV} {ep['setting']} {c['vid']} {AUDIO}"
            cut = c.get("tiktok")
            cut_note = ("" if cut is None else
                        "**Bản TikTok:** bỏ clip này." if cut == "bo" else
                        f"**Bản TikTok:** chỉ dùng giây {cut.replace('-', ' đến ')} của clip này.")
            md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{fname}`", ""]
            if cut_note:
                md += [cut_note, ""]
            md += [
                   "**Ảnh khung đầu**", "```", c["img"], "```", "",
                   "**Video (Muse)**", "```", video, "```", ""]
            plan.append(f"clip: {fname} | {c['label']}" + (f" | tiktok={cut}" if cut else ""))
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
        with open(os.path.join(here, base + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md))
        with open(os.path.join(here, base + ".plan.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(plan) + "\n")
        lines.append(f"{base}: {len(ep['clips'])} clip")
    print("\n".join(lines))
