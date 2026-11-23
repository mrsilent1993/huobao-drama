# Repo of the Day

Mỗi sáng (khoảng 7h, giờ Việt Nam) một phiên Claude chạy theo lịch:
1. `python3 rotd.py pick`: tìm repo GitHub mới tạo trong 7 ngày, nhiều sao nhất, có README; bỏ repo đã đăng (đọc mô tả các video cũ của Trang), bỏ đề tài nhạy cảm (crack, cheat, game dịch ngược, công cụ tấn công, tiền mã hóa, 18+) và tài khoản kiểu spam.
2. Claude đọc `work/pick.json`, viết `work/script.json` (6–7 câu tiếng Anh, 115–145 từ, chỉ nói điều có trong README).
3. `python3 rotd.py render`: giọng đọc Piper (en_US-ryan-high, tự tải lần đầu) + thẻ chữ 1080x1920 → `work/rotd.mp4` (30–60 giây).
4. `python3 rotd.py post`: đăng video lên Trang Facebook (Graph API, host `graph-video.facebook.com`; token do proxy tự gắn, không nằm trong repo).

Cấu hình: `config.json` = `{"fb_page_id": "<ID Trang>"}` hoặc biến môi trường `FB_PAGE_ID`.
Chạy thử không đăng: làm bước 1–3.

## Kiểu đồ họa chuyển động (mặc định từ 23/11/2026)

Nếu `work/script.json` có khóa `"scenes"` (đúng một cảnh cho mỗi câu), `rotd.py render` dựng bằng `motion/engine.html` + `motion/render_motion.js` (Playwright chụp từng khung, 30 khung/giây): nền kem chấm bi, chữ lớn, thẻ viền đen bóng đổ, màu nhấn xanh lá; phụ đề sáng dần theo nhịp đọc, từ khóa tô màu.

Loại cảnh: `hook` (kicker, title), `flow` (title, steps[{t,s}]), `list` (title, items), `bigstat` (kicker, value, unit, label, sub), `chips` (title, items, target), `cta` (title, stats[{v,k}]). Trong `title`: `_chữ_` = tô xanh, `*chữ*` = gạch nền.

## Cài trên máy cá nhân (macOS)

1. Clone repo, vào thư mục `repo-of-the-day/`, chạy `bash setup_mac.sh` (cài ffmpeg, node, piper-tts, Playwright Chromium, lịch launchd 6:46 sáng).
2. Cài Claude Code CLI và đăng nhập một lần (`claude`). Mỗi sáng `run_daily.sh` gọi `claude -p` để viết `work/script.json` theo `prompt_script.md`.
3. Điền `.env`: `FB_PAGE_ID=...` và `FB_ACCESS_TOKEN=...` (token Trang, quyền pages_manage_posts, publish_video). File `.env` không bao giờ được commit.
4. Chạy thử: `bash run_daily.sh`. Nhật ký ở `work/daily-YYYY-MM-DD.log`.
Máy phải bật và không ngủ lúc 6:46 (hoặc đặt lại giờ trong `~/Library/LaunchAgents/com.repooftheday.daily.plist`).
Phông chữ Inter (SIL OFL) và DejaVu đi kèm trong `motion/fonts/` cùng giấy phép.
