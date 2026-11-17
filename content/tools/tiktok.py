#!/usr/bin/env python3
"""Dựng video dọc 9:16 cho TikTok và YouTube Shorts từ các clip Muse theo một file kế hoạch.

Cách dùng:
    python3 tiktok.py plan.txt out.mp4                 # dựng mọi bản mà plan hỗ trợ
    python3 tiktok.py plan.txt out.mp4 --chi tiktok    # chỉ bản TikTok (hoặc --chi youtube)

Nếu plan có đánh dấu "tiktok=" ở dòng clip, script dựng HAI bản từ cùng một bộ clip:
    out-youtube.mp4  bản đầy đủ (mọi clip), lời kêu gọi cuối video dùng "Đăng ký"
    out-tiktok.mp4   bản rút gọn theo đánh dấu, lời kêu gọi dùng "Follow"
Nếu không có đánh dấu nào, dựng một bản out.mp4 như cũ.
Mỗi bản: 1080x1920, 30fps, H.264 + AAC, -14 LUFS, kèm ảnh bìa .jpg cùng tên.

Đánh dấu cắt cho bản TikTok (cột thứ ba của dòng clip):
    clip: tg-1.mp4 | Làng Phù Đổng                # không ghi: giữ nguyên cả clip
    clip: tg-2.mp4 | Một lúc sau | tiktok=5-10     # chỉ lấy giây 5 đến 10 của clip
    clip: tg-3.mp4 | Mấy hôm sau | tiktok=bo       # bỏ cả clip ở bản TikTok
Phụ đề tự cắt và dời theo đoạn được giữ.

plan.txt (dòng trống và dòng bắt đầu bằng # được bỏ qua; " / " là xuống dòng bắt buộc):
    hook: POV: Bạn là dân Hoa Lư / ngày dời đô năm 1010     # chữ lớn giữa màn hình, 0-2.5s
    end: Năm 1010, Lý Thái Tổ dời đô / về Đại La, đặt tên Thăng Long.   # 3 giây cuối
    clip: dl-1.mp4 | Hoa Lư · sáng sớm          # file | mốc thời gian hiện 3s đầu clip
    sub: 1 | 0.5-4.8 | Đang yên đang lành, vua lại bắt cả kinh thành dọn nhà!
    # sub: <số clip> | <giây bắt đầu>-<giây kết thúc trong clip đó> | lời thoại

Mọi chữ nằm trong vùng an toàn của TikTok: tránh ~200px trên (thanh tab), ~480px dưới
(caption, nhạc) và ~160px bên phải (nút tim, bình luận, chia sẻ).
Cần ffmpeg của hệ thống (có drawtext). Chữ tự xuống dòng; dòng có " / " thì giữ nguyên và tự thu nhỏ cho vừa.
"""
import os
import subprocess
import sys
import tempfile

W, H, FPS = 1080, 1920, 30
LUFS = -14
FONT = os.environ.get("TT_FONT", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
RIGHT_UI = 160            # chừa bên phải cho cột nút của TikTok
SAFE_TOP = 230            # dưới thanh "Đang follow / Dành cho bạn"
SUB_Y = int(H * 0.64)     # phụ đề nằm trên vùng caption ở đáy


def die(msg):
    sys.exit(f"Lỗi: {msg}")


USABLE_W = W - RIGHT_UI - 80   # bề rộng dành cho chữ
CHAR_W = 0.6                    # bề rộng trung bình một ký tự DejaVu Sans Bold, tính theo cỡ chữ


def layout(text, size):
    """Trả về (các dòng, cỡ chữ). Có ' / ' thì giữ đúng các dòng đó và thu nhỏ chữ cho vừa;
    không có thì tự xuống dòng theo bề rộng."""
    if " / " in text:
        parts = [p.strip() for p in text.split(" / ")]
        fit = min(size, int(USABLE_W / (max(len(p) for p in parts) * CHAR_W)))
        if fit >= size * 0.85:
            return parts, fit
        # dòng quá dài: không co chữ nhiều, tự xuống dòng từng đoạn ở cỡ gần chuẩn
        size = int(size * 0.9)
        return [l for p in parts for l in layout(p, size)[0]], size
    width = max(8, int(USABLE_W / (size * CHAR_W)))
    # chia đều các dòng để không có dòng cuối chỉ một chữ
    n_lines = -(-len(text) // width)
    width = min(width, -(-len(text) // n_lines) + 4)
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines, size


def probe_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def parse(plan_path):
    base = os.path.dirname(os.path.abspath(plan_path))
    plan = {"hook": "", "end": "", "clips": [], "subs": []}
    with open(plan_path, encoding="utf-8") as fh:
        for n, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if key in ("hook", "end"):
                plan[key] = val
            elif key == "clip":
                parts = [p.strip() for p in val.split("|")]
                f, cap = parts[0], (parts[1] if len(parts) > 1 else "")
                cut = None                      # None = cả clip, "bo" = bỏ, (a, b) = đoạn giữ lại
                for extra in parts[2:]:
                    k, _, v = extra.partition("=")
                    if k.strip() != "tiktok":
                        die(f"dòng {n}: không hiểu '{extra}'")
                    v = v.strip()
                    if v == "bo":
                        cut = "bo"
                    else:
                        try:
                            a, b = (float(x) for x in v.split("-"))
                        except ValueError:
                            die(f"dòng {n}: tiktok= phải là 'bo' hoặc dạng 0-5")
                        cut = (a, b)
                plan["clips"].append((f if os.path.isabs(f) else os.path.join(base, f), cap, cut))
            elif key == "sub":
                try:
                    idx, span, text = [p.strip() for p in val.split("|", 2)]
                    a, b = (float(x) for x in span.split("-"))
                    plan["subs"].append((int(idx), a, b, text))
                except ValueError:
                    die(f"dòng {n} sai định dạng sub: {line}")
            else:
                die(f"dòng {n} không hiểu: {line}")
    if not plan["clips"]:
        die("plan chưa có clip nào")
    return plan


def measure_lufs(path):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    summary = log[log.rfind("Integrated loudness"):]
    return float(summary.split("I:")[1].split("LUFS")[0])


def fix_loudness(path):
    """Ghép xong đo lại toàn bài; lệch quá 0.5 LU thì bù âm lượng (có limiter chặn đỉnh), giữ nguyên hình."""
    diff = LUFS - measure_lufs(path)
    if abs(diff) <= 0.5:
        return
    tmp_out = path + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-map", "0:v", "-map", "0:a", "-c:v", "copy",
                    "-af", f"volume={diff:.2f}dB,alimiter=limit=0.84:level=false",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", tmp_out],
                   check=True)
    os.replace(tmp_out, path)


def render(plan, out, version):
    """version: "full" (bản duy nhất như cũ), "youtube" (đủ clip) hoặc "tiktok" (theo đánh dấu cắt)."""
    tmp = tempfile.mkdtemp()
    counter = iter(range(10**6))

    def drawtext(text, size, y, enable, box=False):
        lines, size = layout(text, size)
        path = os.path.join(tmp, f"t{next(counter)}.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        style = (":box=1:boxcolor=black@0.55:boxborderw=18" if box
                 else ":borderw=5:bordercolor=black@0.9")
        # căn giữa trong phần khung không bị cột nút bên phải che
        return (f"drawtext=fontfile={FONT}:textfile={path}:fontsize={size}:fontcolor=white"
                f":line_spacing=12{style}:x=(w-{RIGHT_UI}-tw)/2+{RIGHT_UI // 4}:y={y}"
                f":enable='{enable}'")

    # chọn clip và đoạn giữ lại cho bản này
    picked = []
    for idx, (path, cap, cut) in enumerate(plan["clips"], 1):
        if not os.path.isfile(path):
            die(f"không thấy file {path}")
        dur = probe_duration(path)
        a, b = 0.0, dur
        if version == "tiktok" and cut == "bo":
            continue
        if version == "tiktok" and isinstance(cut, tuple):
            a, b = max(0.0, cut[0]), min(dur, cut[1])
        picked.append((idx, path, cap, a, b))
    if not picked:
        die("bản TikTok không còn clip nào")

    end_text = plan["end"]
    if version == "youtube":
        end_text = end_text.replace("Follow", "Đăng ký")

    inputs, chain = [], []
    n = len(picked)
    for i, (idx, path, cap, a, b) in enumerate(picked):
        d = b - a
        inputs += ["-i", path]
        v = [f"[{i}:v]trim=start={a}:end={b},setpts=PTS-STARTPTS,"
             f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}"]
        if cap:
            v.append(drawtext(cap, 50, SAFE_TOP, "lt(t,3)", box=True))
        if i == 0 and plan["hook"]:
            v.append(drawtext(plan["hook"], 76, "(h-th)*0.40", "lt(t,2.5)"))
        for sidx, sa, sb, text in plan["subs"]:
            if sidx != idx:
                continue
            s0, s1 = max(sa, a) - a, min(sb, b) - a
            if s1 - s0 >= 0.8:          # phụ đề còn lại quá ngắn thì bỏ
                v.append(drawtext(text, 54, SUB_Y, f"between(t,{s0:.2f},{s1:.2f})"))
        if i == n - 1 and end_text:
            v.append(f"drawbox=x=0:y=ih*0.36:w=iw:h=ih*0.22:color=black@0.6:t=fill:enable='gte(t,{d - 3})'")
            v.append(drawtext(end_text, 52, "(h-th)*0.45", f"gte(t,{d - 3})"))
        chain.append(",".join(v) + f",format=yuv420p[v{i}]")
        # loudnorm kéo dài đuôi âm thanh; cắt về đúng đoạn hình để không lệch tiếng
        chain.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,"
                     f"loudnorm=I={LUFS}:TP=-1.5:LRA=11,aresample=48000,atrim={a}:{b},asetpts=PTS-STARTPTS,"
                     f"afade=t=in:d=0.05,afade=t=out:st={d - 0.05}:d=0.05[a{i}]")
    chain.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a]")

    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(chain),
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-preset", "medium", "-crf", "18",
                    "-maxrate", "12M", "-bufsize", "24M", "-r", str(FPS),
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", out], check=True)
    fix_loudness(out)
    cover = os.path.splitext(out)[0] + ".jpg"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.2", "-i", out, "-frames:v", "1",
                    "-q:v", "2", cover], check=True)
    print(f"Đã xuất: {out} ({sum(p[4] - p[3] for p in picked):.0f} giây)\nẢnh bìa: {cover}")


def main():
    args = sys.argv[1:]
    only = None
    if "--chi" in args:
        k = args.index("--chi")
        only = args[k + 1] if k + 1 < len(args) else ""
        if only not in ("tiktok", "youtube"):
            die("--chi phải là tiktok hoặc youtube")
        del args[k:k + 2]
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    plan, out = parse(args[0]), args[1]
    has_cut = any(c[2] is not None for c in plan["clips"])
    if not has_cut and only is None:
        render(plan, out, "full")
        return
    stem = os.path.splitext(out)[0]
    for version in ("youtube", "tiktok"):
        if only in (None, version):
            render(plan, f"{stem}-{version}.mp4", version)


if __name__ == "__main__":
    main()
