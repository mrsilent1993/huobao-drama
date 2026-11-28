#!/usr/bin/env python3
"""Kiểm tra clip Muse so với kịch bản: kỹ thuật, lời nói (Gemini nghe và chép lại), ảnh tờ khung hình để soát hình.

Dùng:
  python3 kiem_tra_clip.py <thư_mục_clip> <file.plan.txt> [--out báo_cáo.md]
  - Clip đặt tên như trong plan: bd1288-tap8-1.mp4 … (plan ghi "clip: <tên> | …" và "sub: <số> | a-b | lời").
  - Cần ffmpeg/ffprobe và mạng tới generativelanguage.googleapis.com (khóa do proxy gắn sẵn).

Với mỗi clip, báo cáo có:
  1. Kỹ thuật: độ dài, khung (phải 9:16), có tiếng không, độ to.
  2. Lời nói: Gemini nghe và chép lại; so với câu trong kịch bản (% khớp chữ), số người nói, giọng vùng miền,
     tiếng có rõ không, có lẫn tiếng nước ngoài/âm vô nghĩa không, câu có bị cắt cuối không.
  3. Ảnh tờ khung hình (6 khung rải đều) lưu cạnh báo cáo để soát hình bằng mắt: mặt Anh Tư, cờ, chữ, cọc nhỏ…
"""
import base64
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from series import loi_muse  # noqa: E402

MODELS = [m for m in os.environ.get("KT_MODEL", "gemini-3.5-flash,gemini-3-flash-preview,gemini-2.5-flash").split(",") if m]
API = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
             "-of", "json", path])
    d = json.loads(r.stdout or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    a = any(s.get("codec_type") == "audio" for s in d.get("streams", []))
    return float(d.get("format", {}).get("duration", 0)), v.get("width"), v.get("height"), a


def loudness(path):
    r = run(["ffmpeg", "-hide_banner", "-i", path, "-af", "volumedetect", "-f", "null", "-"])
    m = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else None


def contact_sheet(path, out_jpg, dur):
    tmp = tempfile.mkdtemp()
    frames = []
    for i in range(6):
        t = dur * (i + 0.5) / 6
        f = os.path.join(tmp, f"f{i}.jpg")
        run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1", "-vf",
             "scale=270:-2", f])
        if os.path.exists(f):
            frames.append(f)
    if frames:
        inputs = sum((["-i", f] for f in frames), [])
        run(["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex",
             f"hstack=inputs={len(frames)}" if len(frames) > 1 else "null", out_jpg])
    for f in frames:
        os.remove(f)
    os.rmdir(tmp)


def gemini_listen(path, expected):
    wav = tempfile.mktemp(suffix=".mp3")
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k", wav])
    data = base64.b64encode(open(wav, "rb").read()).decode()
    os.remove(wav)
    ask = ("Bạn là người soát tiếng cho video tiếng Việt. Nghe đoạn âm thanh và trả về JSON đúng mẫu, không thêm chữ nào khác:\n"
           '{"transcript": "chép lại NGUYÊN VĂN những gì nghe được, có dấu tiếng Việt", '
           '"so_nguoi_noi": số người nói khác nhau, '
           '"giong": "Bắc | Trung | Nam | lơ lớ nước ngoài | không rõ", '
           '"ro_chu": điểm 1-5 (5 = nghe rõ từng chữ), '
           '"co_tieng_la": true/false (có tiếng nước ngoài hoặc âm vô nghĩa không), '
           '"bi_cat_cuoi": true/false (câu cuối có bị cắt ngang không), '
           '"ghi_chu": "lỗi phát âm hoặc vấn đề khác, ngắn gọn"}\n'
           f"Câu đúng theo kịch bản (để bạn biết họ định nói gì, KHÔNG được chép câu này nếu không nghe thấy): \"{expected}\"")
    body = {"contents": [{"parts": [{"inline_data": {"mime_type": "audio/mp3", "data": data}}, {"text": ask}]}],
            "generationConfig": {"temperature": 0, "responseMimeType": "application/json"}}
    last = None
    for model in MODELS:
        for attempt in range(3):
            try:
                req = urllib.request.Request(API.format(model), data=json.dumps(body).encode(),
                                             headers={"Content-Type": "application/json", "x-goog-api-key": "proxy"})
                r = json.load(urllib.request.urlopen(req, timeout=180))
                txt = r["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(txt)
            except Exception as e:  # noqa: BLE001 — quá tải (503/429) thì chờ rồi thử lại, hết lượt thì đổi model
                last = e
                time.sleep(4 * (attempt + 1))
    raise RuntimeError(f"Gemini không trả lời ({last})")


def words(s):
    s = unicodedata.normalize("NFC", s.lower())
    return re.findall(r"[\wà-ỹđ]+", s)


def parse_plan(plan):
    clips, subs = [], {}
    for line in open(plan, encoding="utf-8"):
        line = line.strip()
        if line.startswith("clip:"):
            clips.append(line[5:].split("|")[0].strip())
        elif line.startswith("sub:"):
            n, _, txt = [x.strip() for x in line[4:].split("|", 2)]
            subs.setdefault(int(n), []).append(txt.split(": / ", 1)[-1] if txt.split(": / ", 1)[0].count(" ") < 4 else txt)
    return clips, subs


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    folder, plan = sys.argv[1], sys.argv[2]
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(folder, "bao-cao-kiem-tra.md")
    clips, subs = parse_plan(plan)
    rep = [f"# Báo cáo kiểm tra clip · {os.path.basename(plan)}", ""]
    summary = []
    for i, name in enumerate(clips, 1):
        path = os.path.join(folder, name)
        rep += [f"## Clip {i} · `{name}`", ""]
        if not os.path.exists(path):
            rep += ["**Chưa có file.**", ""]
            summary.append((i, "thiếu file"))
            continue
        dur, w, h, has_a = probe(path)
        vol = loudness(path) if has_a else None
        issues = []
        if abs(dur - 10) > 0.6:
            issues.append(f"độ dài {dur:.1f}s (cần 10s)")
        if w and h and abs(w / h - 9 / 16) > 0.02:
            issues.append(f"khung {w}x{h} không phải 9:16")
        if not has_a:
            issues.append("không có tiếng")
        rep.append(f"- **Kỹ thuật:** {dur:.1f}s · {w}x{h} · tiếng: {'có' if has_a else 'KHÔNG'}"
                   + (f" · độ to trung bình {vol:.0f} dB" if vol is not None else ""))
        expected = " ".join(loi_muse(s) for s in subs.get(i, []))
        if has_a and expected:
            try:
                g = gemini_listen(path, expected)
                ratio = difflib.SequenceMatcher(None, words(expected), words(g.get("transcript", ""))).ratio()
                rep += [f"- **Kịch bản:** {expected}", f"- **Nghe được:** {g.get('transcript', '')}",
                        f"- **Khớp chữ:** {ratio * 100:.0f}% · người nói: {g.get('so_nguoi_noi')} · giọng: {g.get('giong')} · "
                        f"rõ chữ: {g.get('ro_chu')}/5 · tiếng lạ: {'có' if g.get('co_tieng_la') else 'không'} · "
                        f"cắt cuối: {'có' if g.get('bi_cat_cuoi') else 'không'}"]
                if g.get("ghi_chu"):
                    rep.append(f"- **Ghi chú:** {g['ghi_chu']}")
                if ratio < 0.8:
                    issues.append(f"lời khớp {ratio * 100:.0f}%")
                if (g.get("so_nguoi_noi") or 1) > 1:
                    issues.append(f"{g.get('so_nguoi_noi')} người nói")
                if (g.get("ro_chu") or 5) < 4:
                    issues.append(f"rõ chữ {g.get('ro_chu')}/5")
                if g.get("co_tieng_la"):
                    issues.append("có tiếng lạ")
                if g.get("bi_cat_cuoi"):
                    issues.append("bị cắt cuối câu")
            except Exception as e:  # noqa: BLE001
                rep.append(f"- **Lời nói:** không kiểm được ({e})")
                issues.append("CHƯA kiểm được lời nói")
        sheet = os.path.join(os.path.dirname(out), f"khung-{os.path.splitext(name)[0]}.jpg")
        contact_sheet(path, sheet, dur)
        rep += [f"- **Tờ khung hình:** `{os.path.basename(sheet)}`", ""]
        summary.append((i, "; ".join(issues) if issues else "ĐẠT (phần tự động)"))
    rep[2:2] = ["| Clip | Kết quả tự động |", "|---|---|"] + [f"| {i} | {s} |" for i, s in summary] + [""]
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(rep) + "\n")
    print(out)


if __name__ == "__main__":
    main()
