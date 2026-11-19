#!/usr/bin/env python3
"""Xuất "phiếu sản xuất" theo một mẫu chuẩn cho từng video, gom vào content/xuat/phieu-san-xuat/.

Cách dùng (chạy từ content/):
    python3 tools/xuat_phieu.py              # xuất lại toàn bộ phiếu + MUC-LUC.md
    python3 tools/xuat_phieu.py --zip FILE   # xuất xong nén cả thư mục thành FILE (.zip)

Nguồn là các cặp <tên>.md + <tên>.plan.txt do _nguon.py của từng loạt sinh ra. Phiếu không thay thế file nguồn:
sửa nội dung thì sửa _nguon.py, chạy lại, rồi chạy lại công cụ này.
"""
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # content/
OUT = os.path.join(ROOT, "xuat", "phieu-san-xuat")

# Thư mục loạt -> tên hiển thị (theo thứ tự trong mục lục)
SERIES = [
    ("tu-hao-dai-viet", "Tự hào Đại Việt"),
    ("tet-ky-dau-1789", "Tết Kỷ Dậu 1789 (3 phần)"),
    ("quang-trung", "Loạt Quang Trung (Q1–Q8)"),
    ("tay-son-tung-moc", "Tây Sơn từng mốc"),
    ("pov-nguoi-binh-thuong", "POV người bình thường (Anh Tư)"),
    ("tran-danh-noi-tieng", "Trận đánh nổi tiếng"),
    ("thang-long-ky-truyen", "Thăng Long kỳ truyện"),
    ("bac-thuoc", "Làm thuê cho quan đô hộ (Bắc thuộc)"),
    ("bach-dang-938", "Bạch Đằng 938 (trailer và bản trận đánh)"),
    ("tra-loi-binh-luan", "Video trả lời bình luận"),
    ("bach-dang", "Ba lần Bạch Đằng"),
    ("bach-dang-ngoai-truyen", "Bạch Đằng ngoại truyện"),
    ("phia-ben-kia", "Phía bên kia"),
    ("chuyen-la-dai-viet", "Chuyện lạ Đại Việt"),
    ("sgk-khong-ke", "Điều sách giáo khoa không kể"),
    ("truyen-dai", "Truyện dài"),
]
# Video đã đăng (theo trang quản lý TikTok anh gửi ngày 18/11/2026); các video khác để ô trống cho anh tự đánh dấu.
POSTED = {
    "bach-dang/phan-1-ngo-quyen-938",
    "pov-nguoi-binh-thuong/tap-6-dong-thuyen-cho-giac-1427",
    "pov-nguoi-binh-thuong/tap-11-dan-duong-rach-gam-1785",
    "phia-ben-kia/tap-1-ngay-thu-42-ung-chau-1076",
    "bach-dang-ngoai-truyen/tap-1-linh-nam-han-938",
}

CHECKLIST = """- [ ] Tạo đủ {n} clip trên Muse, đặt đúng tên file ({first} … {last}).
- [ ] Clip có ghi chú **"Nối cảnh với clip trước"**: dùng khung cuối của clip trước làm ảnh khung đầu (`python3 tools/khung-cuoi.py`, hoặc gửi clip cho mình cắt).
- [ ] **Nghe lại giọng:** Anh Tư và người dẫn chuyện đúng giọng cố định của kênh; giọng vùng miền đúng như ghi trong prompt.
- [ ] **Xem lại hình:** không có cờ hiện đại hay chữ trên áo, biển, cờ; trang phục, thuyền đúng thời; cọc to (nếu có cảnh cọc); rồng kiểu thời Lý (nếu có).
- [ ] **An toàn:** không trẻ em cận cảnh, không máu, không cảnh chết; vua và danh nhân được dựng trang trọng.
- [ ] **Lời nói khớp phụ đề:** nếu Muse nói khác chữ trong mục "Chữ trên video", báo mình sửa phụ đề trước khi dựng.
- [ ] Gửi đủ clip qua Drive để mình dựng ra bản YouTube và bản TikTok.
- [ ] **Đăng TikTok:** bật nhãn "Nội dung do AI tạo"; dán tiêu đề, mô tả, hashtag; đăng xong ghim bình luận.
- [ ] **Đăng YouTube:** mục "Nội dung bị thay đổi" chọn **Có**; dán thẻ; ghim bình luận; thêm vào danh sách phát của loạt (nếu có)."""


def sections(md):
    """Tách file .md thành (tiêu đề #, phần mở đầu, [(tiêu đề ##, nội dung)])."""
    lines = md.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    intro, secs, cur = [], [], None
    for l in lines:
        if l.startswith("# ") and l[2:].strip() == title and cur is None and not intro:
            continue
        if l.startswith("## "):
            cur = [l[3:].strip(), []]
            secs.append(cur)
        elif cur is None:
            intro.append(l)
        else:
            cur[1].append(l)
    return title, "\n".join(intro).strip(), [(h, "\n".join(b).strip()) for h, b in secs]


def demote(text):
    """Hạ cấp tiêu đề bên trong một mục (### -> ####) để phiếu giữ đúng cấu trúc."""
    return re.sub(r"^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", text, flags=re.M)


def parse_plan(text):
    plan = {"hook": "", "tag": "AI tái hiện · lời thoại hư cấu", "trans": 0.4, "clips": []}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if k == "hook":
            plan["hook"] = v.replace(" / ", " ")
        elif k == "nhan":
            plan["tag"] = "" if v.lower() in ("khong", "không") else v
        elif k == "chuyen":
            kind, _, secs = v.replace(" ", ":", 1).partition(":")
            plan["trans"] = 0.0 if kind in ("cat", "cut") else float(secs or 0.4)
        elif k == "clip":
            parts = [p.strip() for p in v.split("|")]
            cut, tr = None, None
            for extra in parts[2:]:
                ek, _, ev = extra.partition("=")
                if ek.strip() == "tiktok":
                    cut = ev.strip()
                elif ek.strip() == "chuyen":
                    kind, _, secs = ev.strip().partition(":")
                    tr = 0.0 if kind in ("cat", "cut") else float(secs or 0.4)
            plan["clips"].append({"file": parts[0], "label": parts[1] if len(parts) > 1 else "", "cut": cut, "tr": tr})
    return plan


def durations(plan):
    cl = plan["clips"]
    tr = [plan["trans"] if c["tr"] is None else c["tr"] for c in cl]
    yt = 10 * len(cl) - sum(tr[1:])
    if not any(c["cut"] for c in cl):
        return yt, None, None
    picked = [(c, t) for c, t in zip(cl, tr) if c["cut"] != "bo"]
    tt = sum(10 if c["cut"] is None else float(c["cut"].split("-")[1]) - float(c["cut"].split("-")[0])
             for c, _ in picked) - sum(t for _, t in picked[1:])
    full = all(c["cut"] != "bo" for c in cl)
    return yt, tt, full


def cut_text(cut):
    if cut is None:
        return "giữ nguyên 10 giây"
    if cut == "bo":
        return "bỏ"
    a, b = cut.split("-")
    return f"giây {a}–{b}"


def build_sheet(folder, series_name, base, md, plan_text):
    title, intro, secs = sections(md)
    plan = parse_plan(plan_text)
    yt, tt, full = durations(plan)
    clips_sec = {h: b for h, b in secs if re.match(r"(Clip|Trailer) \d+", h)}
    names = {}
    for h, b in secs:
        m = re.match(r"(?:Clip|Trailer) (\d+): (.*)", h)
        if m:
            names[int(m.group(1))] = (m.group(2).strip(), "Nối cảnh với clip trước" in b)
    key = f"{folder}/{base}"
    n = len(plan["clips"])
    head = [f"# Phiếu sản xuất: {title}", "",
            "| Mục | Nội dung |", "|---|---|",
            f"| Loạt | {series_name} |",
            f"| File nguồn | `content/{folder}/{base}.md` (sửa nội dung ở `content/{folder}/_nguon.py`) |",
            f"| Số clip Muse | {n} (`{plan['clips'][0]['file']}` … `{plan['clips'][-1]['file']}`) |" if n else "| Số clip Muse | — |",
            f"| Bản YouTube | khoảng {yt:.0f} giây (đủ clip, đã trừ chuyển cảnh) |"]
    if tt is not None:
        head.append(f"| Bản TikTok | khoảng {tt:.0f} giây ({'vẫn đủ mọi cảnh' if full else 'rút gọn, bỏ một số clip'}) |")
    else:
        head.append("| Bản TikTok | dùng chung một bản với YouTube |")
    head += [f"| Hook giây đầu | {plan['hook'] or '—'} |",
             f"| Nhãn đầu video | {plan['tag'] or '(tắt)'} |",
             f"| Đã đăng | {'[x] đã đăng' if key in POSTED else '[ ] chưa đăng'} |", ""]
    out = head + ["## 1. Danh sách clip", "",
                  "| Clip | File Muse | Cảnh | Mốc thời gian trên video | Bản TikTok dùng | Nối cảnh |",
                  "|---|---|---|---|---|---|"]
    for i, c in enumerate(plan["clips"], 1):
        nm, noi = names.get(i, ("", False))
        out.append(f"| {i} | `{c['file']}` | {nm} | {c['label'] or '—'} | {cut_text(c['cut']) if tt is not None else '—'} "
                   f"| {'**có**: dùng khung cuối clip trước' if noi else '—'} |")
    # bỏ dòng thời lượng thô (chưa trừ chuyển cảnh) để không lệch với bảng thông tin chung
    intro = "\n".join(l for l in intro.splitlines() if not l.startswith("**Hai bản từ cùng một bộ clip:**"))
    intro = re.sub(r"\n{3,}", "\n\n", intro).strip()
    out += ["", "## 2. Bối cảnh, lịch sử, giọng nhân vật", "", demote(intro), ""]
    other = [(h, b) for h, b in secs if h not in clips_sec and not h.startswith(("Đăng", "Chữ trên video"))]
    for h, b in other:
        out += [f"### {h}", "", demote(b), ""]
    out += ["## 3. Prompt từng clip", ""]
    for h, b in secs:
        if h in clips_sec:
            out += [f"### {h}", "", demote(b), ""]
    out += ["## 4. Chữ trên video (mình chèn ở hậu kỳ)", "", "```", plan_text.strip(), "```", ""]
    post = [(h, b) for h, b in secs if h.startswith("Đăng")]
    out += ["## 5. Thông tin đăng", ""]
    for h, b in post:
        out += [f"### {h}", "", demote(b), ""]
    first = plan["clips"][0]["file"] if n else "-"
    last = plan["clips"][-1]["file"] if n else "-"
    out += ["## 6. Kiểm tra trước khi đăng", "", CHECKLIST.format(n=n, first=first, last=last), ""]
    return title, yt, tt, key in POSTED, n, "\n".join(out).rstrip() + "\n"


def main():
    zip_path = None
    if "--zip" in sys.argv:
        k = sys.argv.index("--zip")
        zip_path = sys.argv[k + 1] if k + 1 < len(sys.argv) else None
    if os.path.isdir(OUT):
        for dp, _, fs in os.walk(OUT):
            for f in fs:
                if f.endswith(".md"):
                    os.remove(os.path.join(dp, f))
    os.makedirs(OUT, exist_ok=True)
    index = ["# Mục lục phiếu sản xuất", "",
             "Mỗi video một phiếu theo cùng mẫu: thông tin chung, danh sách clip, bối cảnh và giọng, prompt từng clip, "
             "chữ trên video, thông tin đăng, bảng kiểm tra trước khi đăng. Xuất lại bằng `python3 tools/xuat_phieu.py` "
             "(chạy từ thư mục `content/`).", ""]
    total = 0
    for folder, name in SERIES:
        src = os.path.join(ROOT, folder)
        if not os.path.isdir(src):
            continue
        bases = sorted({f[:-9] for f in os.listdir(src) if f.endswith(".plan.txt")
                        and os.path.isfile(os.path.join(src, f[:-9] + ".md"))},
                       key=lambda b: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", b)])
        if not bases:
            continue
        os.makedirs(os.path.join(OUT, folder), exist_ok=True)
        index += [f"## {name}", "", "| # | Video | Clip | YouTube | TikTok | Đã đăng | Phiếu |", "|---|---|---|---|---|---|---|"]
        for k, base in enumerate(bases, 1):
            md = open(os.path.join(src, base + ".md"), encoding="utf-8").read()
            pl = open(os.path.join(src, base + ".plan.txt"), encoding="utf-8").read()
            title, yt, tt, posted, n, sheet = build_sheet(folder, name, base, md, pl)
            fname = f"{k:02d}-{base}.md"
            with open(os.path.join(OUT, folder, fname), "w", encoding="utf-8") as fh:
                fh.write(sheet)
            short = title.split(":", 1)[-1].strip() if ":" in title else title
            index.append(f"| {k} | {short} | {n} | ~{yt:.0f}s | {'~%.0fs' % tt if tt is not None else 'chung'} | "
                         f"{'✅' if posted else '☐'} | `{folder}/{fname}` |")
            total += 1
        index.append("")
    index.insert(4, f"**Tổng cộng {total} phiếu.** ✅ = đã đăng (theo trang quản lý TikTok ngày 18/11/2026), ☐ = chưa đăng.\n")
    with open(os.path.join(OUT, "MUC-LUC.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index).rstrip() + "\n")
    print(f"Đã xuất {total} phiếu vào {OUT}")
    if zip_path:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for dp, _, fs in os.walk(OUT):
                for f in sorted(fs):
                    p = os.path.join(dp, f)
                    z.write(p, os.path.join("phieu-san-xuat", os.path.relpath(p, OUT)))
        print(f"Đã nén: {zip_path}")


if __name__ == "__main__":
    main()
