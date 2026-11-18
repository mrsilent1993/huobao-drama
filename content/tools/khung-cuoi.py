#!/usr/bin/env python3
"""Cắt khung hình cuối của từng clip Muse thành ảnh PNG, để làm ảnh khung đầu cho clip kế tiếp.

Dùng khi hai clip liền nhau cùng một cảnh: tạo clip trước xong, lấy khung cuối của nó đưa vào Muse làm
ảnh khung đầu của clip sau, thì người, ánh sáng và góc máy nối liền, không bị nhảy cảnh.

Cách dùng:
    python3 khung-cuoi.py bd938-04.mp4                  # một clip -> khung-cuoi/bd938-04-cuoi.png
    python3 khung-cuoi.py thu-muc-clip/                 # mọi .mp4 trong thư mục
    python3 khung-cuoi.py thu-muc-clip/ --so-sanh       # thêm bảng chấm độ liền mạch giữa các clip liền nhau
    python3 khung-cuoi.py a.mp4 b.mp4 -o anh/           # chọn thư mục ra

--so-sanh: so khung cuối clip trước với khung đầu clip sau, ra độ chênh từ 0 (giống hệt) đến 1 (khác hẳn),
tính trên ảnh thu nhỏ nên phản ánh bố cục, ánh sáng và màu. Ngưỡng (0,08 và 0,18) là ước lượng thô để lọc
nhanh, không phải phán quyết: chỗ cố ý đổi cảnh (đêm sang ngày) thì nhảy là đúng.
Ảnh PNG giữ nguyên độ phân giải gốc của clip.
"""
import os
import re
import subprocess
import sys


def die(msg):
    print(f"Lỗi: {msg}", file=sys.stderr)
    sys.exit(1)


def natural(path):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", os.path.basename(path).lower())]


def run(args):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        die("ffmpeg lỗi:\n" + r.stderr.strip()[-800:])


def last_frame(clip, png):
    # đọc 1 giây cuối, ghi đè liên tục vào cùng một ảnh: ảnh còn lại là khung cuối cùng
    run(["-sseof", "-1", "-i", clip, "-update", "1", "-an", png])
    if not os.path.isfile(png):
        die(f"không lấy được khung cuối của {clip}")


def first_frame(clip, png):
    run(["-i", clip, "-frames:v", "1", "-an", png])


def thumb(png):
    """Thu ảnh về 36x64 điểm màu (RGB) để so tổng thể: bố cục, ánh sáng, màu."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", png, "-vf", "scale=36:64:flags=area,format=rgb24",
                        "-f", "rawvideo", "-"], capture_output=True)
    return r.stdout


def difference(a, b):
    """0 = giống hệt, 1 = khác hoàn toàn (trung bình chênh lệch màu từng điểm)."""
    x, y = thumb(a), thumb(b)
    if not x or len(x) != len(y):
        return None
    return sum(abs(p - q) for p, q in zip(x, y)) / (255 * len(x))


def main():
    args = sys.argv[1:]
    compare = "--so-sanh" in args
    args = [a for a in args if a != "--so-sanh"]
    out_dir = None
    if "-o" in args:
        k = args.index("-o")
        if k + 1 >= len(args):
            die("-o cần tên thư mục")
        out_dir = args[k + 1]
        del args[k:k + 2]
    if not args:
        print(__doc__)
        sys.exit(1)

    clips = []
    for a in args:
        if os.path.isdir(a):
            clips += [os.path.join(a, f) for f in os.listdir(a) if f.lower().endswith((".mp4", ".mov"))]
        elif os.path.isfile(a):
            clips.append(a)
        else:
            die(f"không thấy {a}")
    if not clips:
        die("không có clip .mp4 hoặc .mov nào")
    clips.sort(key=natural)
    out_dir = out_dir or os.path.join(os.path.dirname(os.path.abspath(clips[0])), "khung-cuoi")
    os.makedirs(out_dir, exist_ok=True)

    lasts = []
    for c in clips:
        stem = os.path.splitext(os.path.basename(c))[0]
        png = os.path.join(out_dir, f"{stem}-cuoi.png")
        last_frame(c, png)
        lasts.append(png)
        print(f"{os.path.basename(c)} -> {png}")

    if compare and len(clips) > 1:
        print("\nĐộ liền mạch giữa các clip liền nhau (khung cuối clip trước so với khung đầu clip sau):")
        for i in range(1, len(clips)):
            head = os.path.join(out_dir, ".dau-tam.png")
            first_frame(clips[i], head)
            score = difference(lasts[i - 1], head)
            os.remove(head)
            if score is None:
                verdict = "không đo được"
            elif score <= 0.08:
                verdict = "liền mạch"
            elif score <= 0.18:
                verdict = "hơi nhảy"
            else:
                verdict = "nhảy cảnh (đúng ý nếu cố ý đổi cảnh)"
            shown = f"{score:.2f}" if score is not None else "-"
            print(f"  {os.path.basename(clips[i - 1])} -> {os.path.basename(clips[i])}: {shown}  {verdict}")


if __name__ == "__main__":
    main()
