#!/usr/bin/env python3
"""Đồng nhất giọng nhân vật: đổi giọng nói trong clip Muse về MỘT giọng mẫu, giữ nguyên nhịp nói (khẩu hình vẫn khớp).

Cách làm cho mỗi clip:
  1. Tách tiếng nói khỏi tiếng nền bằng Demucs (htdemucs, chạy CPU).
  2. Chỉ những đoạn thời gian được chọn (mặc định: cả clip) mới đổi giọng bằng OpenVoice v2 (coqui-tts),
     về giọng mẫu (ví dụ voice/anh-tu-mau.wav). Đoạn khác giữ nguyên, để giọng người khác trong clip không bị đổi.
  3. Trộn lại với tiếng nền, gắn vào video (hình giữ nguyên, không mã hóa lại).

Dùng:
  python3 dong-giong.py --mau anh-tu-mau.wav --ra out/ clip1.mp4 clip2.mp4 ...
  python3 dong-giong.py --mau anh-tu-mau.wav --doan 5.0-9.6 clip3.mp4      # chỉ đổi giây 5.0–9.6 (câu của Anh Tư)
  python3 dong-giong.py --mau anh-tu-mau.wav --doan "0.3-2.2,5.2-9.5" ...  # nhiều đoạn

Cài một lần (môi trường ảo riêng, khoảng 2 GB):
  python3 -m venv vc && . vc/bin/activate
  pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
  pip install "coqui-tts[codec]" six demucs soundfile
Mô hình tự tải lần đầu (OpenVoice v2 từ Hugging Face, Demucs). Đặt COQUI_TOS_AGREED=1.
"""
import argparse
import os
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf

SR = 44100


def run(*a):
    subprocess.run(a, check=True)


def tach_giong(wav, outdir):
    """Demucs 2 nguồn: vocals / no_vocals."""
    run(sys.executable, "-m", "demucs", "--two-stems", "vocals", "-n", "htdemucs", "-o", outdir, wav)
    name = os.path.splitext(os.path.basename(wav))[0]
    d = os.path.join(outdir, "htdemucs", name)
    return os.path.join(d, "vocals.wav"), os.path.join(d, "no_vocals.wav")


def doi_giong(vc, src, mau, out):
    vc.voice_conversion_to_file(source_wav=src, target_wav=mau, file_path=out)


def load(path, sr=SR):
    y, s = sf.read(path, always_2d=True)
    y = y.mean(axis=1)
    if s != sr:
        tmp = path + f".{sr}.wav"
        run("ffmpeg", "-y", "-loglevel", "error", "-i", path, "-ar", str(sr), "-ac", "1", tmp)
        y, _ = sf.read(tmp)
    return y.astype(np.float32)


def xu_ly(clip, mau, doan, ra, vc):
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "a.wav")
        run("ffmpeg", "-y", "-loglevel", "error", "-i", clip, "-vn", "-ac", "2", "-ar", str(SR), wav)
        voc, bg = tach_giong(wav, tmp)
        voc_y, bg_y = load(voc), load(bg)
        n = len(voc_y)
        doi = np.zeros_like(voc_y)
        ranges = doan or [(0.0, n / SR)]
        out_voc = voc_y.copy()
        for k, (a, b) in enumerate(ranges):
            i, j = int(a * SR), min(int(b * SR), n)
            if j - i < SR * 0.3:
                continue
            seg = os.path.join(tmp, f"s{k}.wav")
            sf.write(seg, voc_y[i:j], SR)
            conv = os.path.join(tmp, f"c{k}.wav")
            doi_giong(vc, seg, mau, conv)
            c = load(conv)[: j - i]
            c = np.pad(c, (0, (j - i) - len(c)))
            # khớp độ to với đoạn gốc, chồng mờ 30 ms ở hai đầu
            g = (np.sqrt(np.mean(voc_y[i:j] ** 2)) + 1e-6) / (np.sqrt(np.mean(c ** 2)) + 1e-6)
            c *= min(g, 4.0)
            f = min(int(0.03 * SR), (j - i) // 4)
            ramp = np.linspace(0, 1, f, dtype=np.float32)
            c[:f] = c[:f] * ramp + out_voc[i:i + f] * (1 - ramp)
            c[-f:] = c[-f:] * ramp[::-1] + out_voc[j - f:j] * (1 - ramp[::-1])
            out_voc[i:j] = c
        mix = out_voc + bg_y[:n]
        peak = np.max(np.abs(mix)) + 1e-6
        if peak > 0.98:
            mix *= 0.98 / peak
        mixwav = os.path.join(tmp, "mix.wav")
        sf.write(mixwav, mix, SR)
        os.makedirs(ra, exist_ok=True)
        out = os.path.join(ra, os.path.basename(clip))
        run("ffmpeg", "-y", "-loglevel", "error", "-i", clip, "-i", mixwav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k", "-shortest", out)
        print("đã đổi giọng:", out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mau", required=True, help="file giọng mẫu của nhân vật (10–60 giây, chỉ một người nói)")
    ap.add_argument("--doan", default="", help="đoạn cần đổi, ví dụ '5.0-9.6' hoặc '0.3-2.2,5.2-9.5'; bỏ trống = cả clip")
    ap.add_argument("--ra", default="da-doi-giong", help="thư mục ra")
    ap.add_argument("clips", nargs="+")
    a = ap.parse_args()
    doan = [tuple(float(x) for x in p.split("-")) for p in a.doan.split(",") if p.strip()]
    os.environ.setdefault("COQUI_TOS_AGREED", "1")
    from TTS.api import TTS
    vc = TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2").to("cpu")
    for c in a.clips:
        xu_ly(c, a.mau, doan, a.ra, vc)


if __name__ == "__main__":
    main()
