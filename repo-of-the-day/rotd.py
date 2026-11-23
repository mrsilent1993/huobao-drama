#!/usr/bin/env python3
"""Repo of the Day: chọn một repo GitHub đang lên, dựng video dọc 30–60 giây (giọng đọc tiếng Anh), đăng lên Trang Facebook.

Quy trình (phiên Claude chạy theo lịch mỗi sáng làm đúng 4 bước):
  1. python3 rotd.py pick      -> work/pick.json  (repo được chọn + README rút gọn)
  2. Claude đọc work/pick.json, viết work/script.json  (xem SCRIPT_FORMAT bên dưới)
  3. python3 rotd.py render    -> work/rotd.mp4  (giọng Piper + thẻ chữ 1080x1920)
  4. python3 rotd.py post      -> đăng lên Trang Facebook (cần FB_PAGE_ID và token đã lưu cho graph-video.facebook.com)

Không lặp repo: trước khi chọn, đọc các bài video gần đây của Trang và bỏ qua repo đã có link trong mô tả.
Chạy thử không đăng: python3 rotd.py pick && (viết script) && python3 rotd.py render
"""
import json
import os
import re
import subprocess
import sys
import textwrap
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
_ENV = os.path.join(HERE, ".env")                 # chạy trên máy cá nhân: FB_PAGE_ID=..., FB_ACCESS_TOKEN=...
if os.path.exists(_ENV):
    for _l in open(_ENV, encoding="utf-8"):
        if "=" in _l and not _l.lstrip().startswith("#"):
            _k, _v = _l.strip().split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"'))


def fb_auth():
    """Trên đám mây proxy tự gắn token; trên máy cá nhân lấy FB_ACCESS_TOKEN trong .env."""
    t = os.environ.get("FB_ACCESS_TOKEN")
    return {"Authorization": f"Bearer {t}"} if t else {}
WORK = os.path.join(HERE, "work")
VOICE_DIR = os.path.join(HERE, "voice")
VOICE = "en_US-ryan-high"
VOICE_URL = f"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/ryan/high/{VOICE}"
GRAPH = "https://graph-video.facebook.com/v21.0"
W, H = 1080, 1920
FONT_B = os.path.join(HERE, "motion", "fonts", "DejaVuSans-Bold.ttf")
FONT_R = os.path.join(HERE, "motion", "fonts", "DejaVuSans.ttf")
FONT_M = os.path.join(HERE, "motion", "fonts", "DejaVuSansMono.ttf")
BG, FG, MUTED, ACCENT, CARD = (13, 17, 23), (230, 237, 243), (139, 148, 158), (63, 185, 80), (22, 27, 34)

SCRIPT_FORMAT = """work/script.json:
{
  "lines": [                     # 6–7 câu tiếng Anh, tổng 115–145 từ (~40–55 giây), mỗi câu một thẻ
    "Repo of the day: <name>, ...",       # câu 1: hook, nói tên repo
    "...what problem it solves...",
    "...2–3 standout features...",
    "...who should use it / how to start...",
    "Link in the description. Follow for a new repo every morning."   # câu cuối cố định ý này
  ],
  "keywords": ["...", "..."],    # 2–4 từ khóa ngắn hiện trên thẻ tính năng (tùy chọn)
  "caption": "<mô tả bài Facebook bằng tiếng Anh, 2–4 câu, có link repo, 3–5 hashtag>"
}
Quy tắc: chỉ nói điều có trong README/mô tả, không bịa số liệu; không hứa hẹn bảo mật/hiệu năng nếu README không nói."""


def http_json(url, data=None, method=None, headers=None):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "repo-of-the-day-bot"}
    h.update(headers or {})
    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode()
        h["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def http_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": "repo-of-the-day-bot"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


# ----------------------------------------------------------------------------------------------- 1. chọn repo
def posted_repos():
    """Repo đã đăng: tìm link github.com/owner/repo trong mô tả các video gần đây của Trang."""
    page = page_id()
    if not page:
        return set()
    try:
        d = http_json(f"{GRAPH}/{page}/videos?fields=description&limit=100", headers=fb_auth())
    except Exception as e:  # noqa: BLE001
        print("cảnh báo: không đọc được bài cũ của Trang:", e)
        return set()
    out = set()
    for v in d.get("data", []):
        out |= {m.lower() for m in re.findall(r"github\.com/([\w.-]+/[\w.-]+)", v.get("description", ""))}
    return out


# Không giới thiệu: game/phần mềm thương mại bị dịch ngược, crack, cheat, khóa, công cụ tấn công, tiền mã hóa, 18+.
RISKY = re.compile(r"\b(crack|cheat|keygen|piracy|pirated|warez|bypass|jailbreak|exploit|malware|stealer|rat\b|"
                   r"ddos|botnet|phish|spam|airdrop|wallet drain|nsfw|porn|onlyfans|grand theft auto|gta ?(v|vi|6)|"
                   r"recompil|decompil|leak|torrent|account generator|unlocker)", re.I)


def pick():
    os.makedirs(WORK, exist_ok=True)
    done = posted_repos() | {x.lower() for x in sys.argv[2:]}     # thêm repo muốn bỏ qua: rotd.py pick owner/repo ...
    since = (date.today() - timedelta(days=7)).isoformat()
    q = urllib.parse.quote(f"created:>={since} stars:>200 archived:false fork:false")
    items = http_json(f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=30")["items"]
    for it in items:
        name = it["full_name"]
        if name.lower() in done or not it.get("description"):
            continue
        if RISKY.search(name + " " + it["description"] + " " + " ".join(it.get("topics", []))):
            print("bỏ qua (đề tài nhạy cảm):", name)
            continue
        if re.search(r"\d{4,}", it["owner"]["login"]) or it["forks_count"] < 10:
            continue                                   # bỏ tài khoản kiểu spam (nhiều chữ số) và repo chưa ai fork
        text = ""
        for fn in ("README.md", "readme.md", "README.MD", "Readme.md", "README.rst", "README"):
            try:
                text = http_bytes(f"https://raw.githubusercontent.com/{name}/HEAD/{fn}").decode("utf-8", "ignore")
                break
            except Exception:  # noqa: BLE001
                continue
        text = re.sub(r"<[^>]+>|!\[[^\]]*\]\([^)]*\)", "", text)          # bỏ HTML và ảnh
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if len(text) < 300 or RISKY.search(text[:3000]):
            continue
        info = dict(full_name=name, url=it["html_url"], description=it["description"],
                    stars=it["stargazers_count"], forks=it["forks_count"], language=it.get("language") or "",
                    license=(it.get("license") or {}).get("spdx_id") or "", topics=it.get("topics", [])[:5],
                    created=it["created_at"][:10], owner_avatar=it["owner"]["avatar_url"],
                    readme=text[:6000], picked_on=date.today().isoformat())
        json.dump(info, open(os.path.join(WORK, "pick.json"), "w"), ensure_ascii=False, indent=1)
        print(f"Đã chọn: {name} ({info['stars']} sao, {info['language']}) -> work/pick.json")
        print(SCRIPT_FORMAT)
        return info
    sys.exit("Không tìm được repo phù hợp hôm nay.")


# ----------------------------------------------------------------------------------------------- 2. giọng đọc
def ensure_voice():
    os.makedirs(VOICE_DIR, exist_ok=True)
    for ext in (".onnx", ".onnx.json"):
        p = os.path.join(VOICE_DIR, VOICE + ext)
        if not os.path.exists(p) or os.path.getsize(p) < 1000:
            print("tải giọng", VOICE + ext)
            open(p, "wb").write(http_bytes(VOICE_URL + ext))
    try:
        import piper  # noqa: F401
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "piper-tts"], check=True)


def tts(text, out):
    subprocess.run([sys.executable, "-m", "piper", "-m", os.path.join(VOICE_DIR, VOICE + ".onnx"), "-f", out,
                    "--length-scale", "0.95", "--sentence-silence", "0.15"],
                   input=text.encode(), check=True, capture_output=True)
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                          "csv=p=0", out]).decode().strip())


# ----------------------------------------------------------------------------------------------- 3. thẻ hình
def _font(path, size):
    from PIL import ImageFont
    return ImageFont.truetype(path, size)


def _wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def card(info, line, idx, total, keywords, avatar):
    from PIL import Image, ImageDraw
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # đầu thẻ
    d.text((80, 150), "REPO OF THE DAY", font=_font(FONT_B, 44), fill=ACCENT)
    d.text((80, 210), datetime.now().strftime("%b %d, %Y"), font=_font(FONT_R, 34), fill=MUTED)
    if avatar is not None:
        im.paste(avatar.resize((150, 150)), (W - 230, 140))
    owner, repo = info["full_name"].split("/", 1)
    y = 380
    d.text((80, y), owner + " /", font=_font(FONT_R, 46), fill=MUTED)
    fr = _font(FONT_B, 84 if len(repo) <= 16 else 64)
    for ln in _wrap(d, repo, fr, W - 160)[:2]:
        y += 70
        d.text((80, y), ln, font=fr, fill=FG)
    # dòng số liệu
    y += 130
    stats = [f"{info['stars']:,} stars", info["language"] or "", info["license"] or ""]
    x = 80
    for s in [s for s in stats if s]:
        f = _font(FONT_B, 36)
        wdt = d.textlength(s, font=f) + 50
        d.rounded_rectangle((x, y, x + wdt, y + 70), radius=35, fill=CARD, outline=(48, 54, 61), width=2)
        d.text((x + 25, y + 15), s, font=f, fill=FG)
        x += wdt + 20
    # câu đang đọc (phụ đề lớn)
    fl = _font(FONT_B, 62)
    lines = _wrap(d, line, fl, W - 160)
    by = 1050 - len(lines) * 40
    d.rounded_rectangle((50, by - 50, W - 50, by + len(lines) * 82 + 50), radius=40, fill=CARD)
    for i, ln in enumerate(lines):
        d.text((90, by + i * 82), ln, font=fl, fill=FG)
    # từ khóa ở các thẻ giữa
    if keywords and 0 < idx < total - 1:
        kw = keywords[(idx - 1) % len(keywords)]
        d.text((80, 1520), "# " + kw, font=_font(FONT_M, 46), fill=ACCENT)
    # chân thẻ
    d.text((80, H - 330), "github.com/" + info["full_name"], font=_font(FONT_M, 38 if len(info["full_name"]) < 30 else 30),
           fill=MUTED)
    d.text((80, H - 270), "AI voiceover", font=_font(FONT_R, 28), fill=MUTED)
    # thanh tiến độ
    d.rectangle((0, H - 12, int(W * (idx + 1) / total), H), fill=ACCENT)
    return im


def render():
    from PIL import Image
    import io
    info = json.load(open(os.path.join(WORK, "pick.json")))
    sc = json.load(open(os.path.join(WORK, "script.json")))
    lines = [l.strip() for l in sc["lines"] if l.strip()]
    assert 4 <= len(lines) <= 8, "script.json cần 4–8 câu"
    ensure_voice()
    try:
        avatar = Image.open(io.BytesIO(http_bytes(info["owner_avatar"] + "&s=300"))).convert("RGB")
    except Exception:  # noqa: BLE001
        avatar = None
    segs, total = [], 0.0
    for i, ln in enumerate(lines):
        wav = os.path.join(WORK, f"l{i}.wav")
        dur = tts(ln, wav) + 0.25
        png = os.path.join(WORK, f"c{i}.png")
        card(info, ln, i, len(lines), sc.get("keywords") or [], avatar).save(png)
        segs.append((png, wav, dur))
        total += dur
    if total > 60:
        print(f"cảnh báo: giọng đọc dài {total:.1f}s > 60s, nên rút gọn script")
    # ghép: mỗi thẻ một đoạn, âm thanh nối liền, mờ dần 0,2s đầu/cuối mỗi thẻ
    parts = []
    for i, (png, wav, dur) in enumerate(segs):
        out = os.path.join(WORK, f"s{i}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-t", f"{dur:.3f}",
                        "-i", png, "-i", wav, "-filter_complex",
                        f"[0:v]fade=t=in:st=0:d=0.2,fade=t=out:st={max(dur - 0.2, 0):.3f}:d=0.2,format=yuv420p[v];"
                        f"[1:a]apad=whole_dur={dur:.3f},aformat=sample_rates=48000:channel_layouts=stereo[a]",
                        "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "veryfast",
                        "-crf", "20", "-c:a", "aac", "-b:a", "160k", out], check=True)
        parts.append(out)
    lst = os.path.join(WORK, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    final = os.path.join(WORK, "rotd.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-af",
                    "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-movflags", "+faststart", final], check=True)
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                       final]).decode())
    print(f"Đã dựng {final} ({d:.1f} giây)")


# ----------------------------------------------------------------------------------------------- 3b. bản đồ họa chuyển động
def render_motion():
    """Dựng kiểu 'motion graphics' (motion/engine.html) khi script.json có khóa "scenes" (mỗi câu một cảnh)."""
    info = json.load(open(os.path.join(WORK, "pick.json")))
    sc = json.load(open(os.path.join(WORK, "script.json")))
    lines = [l.strip() for l in sc["lines"] if l.strip()]
    scenes = sc["scenes"]
    assert len(scenes) == len(lines), "scenes phải có đúng số phần tử bằng lines"
    ensure_voice()
    wavs, durs = [], []
    for i, ln in enumerate(lines):
        wav = os.path.join(WORK, f"l{i}.wav")
        durs.append(round(tts(ln, wav) + 0.35, 3))
        wavs.append(wav)
    total = round(sum(durs), 3)
    # âm thanh: nối các câu, mỗi câu đệm cho đủ thời lượng cảnh
    fc = "".join(f"[{i}:a]apad=whole_dur={d},aformat=sample_rates=48000:channel_layouts=stereo[a{i}];"
                 for i, d in enumerate(durs)) + "".join(f"[a{i}]" for i in range(len(durs))) + \
        f"concat=n={len(durs)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    audio = os.path.join(WORK, "voice.m4a")
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for w in wavs:
        cmd += ["-i", w]
    subprocess.run(cmd + ["-filter_complex", fc, "-map", "[a]", "-c:a", "aac", "-b:a", "160k", audio], check=True)
    avatar = None
    try:
        import base64
        avatar = "data:image/png;base64," + base64.b64encode(http_bytes(info["owner_avatar"] + "&s=300")).decode()
    except Exception:  # noqa: BLE001
        pass
    data = dict(repo=info["full_name"], stars=info["stars"], date=datetime.now().strftime("%b %d, %Y").upper(),
                avatar=avatar, lines=lines, scenes=scenes, keywords=sc.get("keywords") or [], durs=durs, total=total,
                brand=sc.get("brand") or "REPO OF THE DAY")
    dj = os.path.join(WORK, "motion.json")
    json.dump(data, open(dj, "w"), ensure_ascii=False)
    silent = os.path.join(WORK, "motion.mp4")
    subprocess.run(["node", os.path.join(HERE, "motion", "render_motion.js"), dj, silent], check=True)
    final = os.path.join(WORK, "rotd.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", audio, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "copy", "-shortest", "-movflags", "+faststart", final], check=True)
    print(f"Đã dựng {final} ({total:.1f} giây, kiểu motion graphics)")


# ----------------------------------------------------------------------------------------------- 4. đăng Facebook
def page_id():
    """ID Trang Facebook: biến môi trường FB_PAGE_ID, hoặc file config.json {"fb_page_id": "..."} cạnh script."""
    if os.environ.get("FB_PAGE_ID"):
        return os.environ["FB_PAGE_ID"]
    cfg = os.path.join(HERE, "config.json")
    return json.load(open(cfg)).get("fb_page_id") if os.path.exists(cfg) else None


def post():
    page = page_id() or sys.exit("Thiếu ID Trang Facebook (FB_PAGE_ID hoặc config.json)")
    info = json.load(open(os.path.join(WORK, "pick.json")))
    sc = json.load(open(os.path.join(WORK, "script.json")))
    cap = sc["caption"]
    if info["url"] not in cap:
        cap += "\n\n" + info["url"]
    cap += "\n\nVoiceover generated with AI."
    final = os.path.join(WORK, "rotd.mp4")
    # multipart qua curl (token do proxy tự gắn vào header Authorization cho host graph-video.facebook.com)
    hdr = [x for k, v in fb_auth().items() for x in ("-H", f"{k}: {v}")]
    r = subprocess.run(["curl", "-sS", "--max-time", "600", "-X", "POST", *hdr, f"{GRAPH}/{page}/videos",
                        "-F", f"source=@{final};type=video/mp4",
                        "--form-string", f"title=Repo of the Day: {info['full_name']}",
                        "--form-string", f"description={cap}"], capture_output=True, text=True)
    print(r.stdout or r.stderr)
    try:
        vid = json.loads(r.stdout)["id"]
    except Exception:  # noqa: BLE001
        sys.exit("Đăng thất bại.")
    print(f"Đã đăng: https://www.facebook.com/{page}/videos/{vid}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    {"pick": pick, "post": post, "render": lambda: render_motion() if "scenes" in json.load(open(os.path.join(WORK, "script.json"))) else render()}.get(cmd, lambda: sys.exit(__doc__))()
