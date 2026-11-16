"""Sinh file prompt dán thẳng (*.md) và file chữ trên video (*.plan.txt) cho một loạt POV.

Mỗi loạt có một file _nguon.py định nghĩa EPISODES rồi gọi build(EPISODES, thư_mục).
Xem content/bach-dang/_nguon.py làm mẫu.
"""
import os

POV = ("First-person POV video, handheld camera at eye level as if seen through the viewer's own eyes, "
       "the viewer's own hands sometimes visible at the bottom of the frame, live-action realistic, "
       "cinematic natural lighting, vertical 9:16. No modern objects, no on-screen text.")
AUDIO = "Audio: natural ambient sound, Vietnamese dialogue spoken naturally with lip sync, no background music."
TAGS = "#povlichsu #POV #lichsuvietnam #xuhuong #fyp"


def build(episodes, here, series_tag="", note="", unit="Phần", file_unit="phan"):
    lines = []
    for n, ep in enumerate(episodes, 1):
        base = f"{file_unit}-{n}-{ep['slug']}"
        md = [f"# {unit} {n}: {ep['title']}", "",
              f"**Độ dài:** {ep['length']}", "",
              "Copy từng khối dán thẳng vào phần mềm. Prompt đã ghép đủ, không cần thay gì.", ""]
        if note:
            md += [note, ""]
        md += [ep["history"], ""]
        plan = [f"# Dựng: python3 ../tools/tiktok.py {base}.plan.txt {base}.mp4",
                f"hook: {ep['hook']}", f"end: {ep['end']}", ""]
        subs = []
        for i, c in enumerate(ep["clips"], 1):
            fname = f"{ep['prefix']}-{i}.mp4"
            video = f"{POV} {ep['setting']} {c['vid']} {AUDIO}"
            md += [f"## Clip {i}: {c['name']}", f"File Muse đặt tên: `{fname}`", "",
                   "**Ảnh khung đầu**", "```", c["img"], "```", "",
                   "**Video (Muse)**", "```", video, "```", ""]
            plan.append(f"clip: {fname} | {c['label']}")
            subs += [f"sub: {i} | {a}-{b} | {t}" for a, b, t in c["subs"]]
        plan += [""] + subs
        tags = " ".join(t for t in (TAGS, series_tag, ep["tags"]) if t)
        md += ["## Đăng TikTok", "", "```", ep["caption"], tags, "```", "",
               "Khi đăng: bật nhãn \"Nội dung do AI tạo\".", "",
               "## Chữ trên video (mình chèn ở hậu kỳ)", "", "```", "\n".join(plan).strip(), "```", ""]
        with open(os.path.join(here, base + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md))
        with open(os.path.join(here, base + ".plan.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(plan) + "\n")
        lines.append(f"{base}: {len(ep['clips'])} clip")
    print("\n".join(lines))
