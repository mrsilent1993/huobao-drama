# Tập 4 · clip 5 và 6 cho Veo 3.1 (thử)

Veo 3.1 cho mỗi clip tối đa **8 giây** (không phải 10 giây như Muse), nên lời đã canh cho vừa 8 giây.
Cài đặt: **khung dọc 9:16 · 8 giây · bật âm thanh**. Nếu có ô *Negative prompt* thì dán khối "Negative" bên dưới.
Ảnh tham chiếu (Ingredients / ảnh khung đầu): clip 5 dùng ảnh cảnh C `bd1288-tap4-canh-C.png`, clip 6 dùng ảnh cảnh D `bd1288-tap4-canh-D.png` (prompt ảnh nằm trong file tập 4). Hai clip này không có Anh Tư nên không cần `anh_tu_ref.png`.

## Clip 5 · Lệnh đánh (chỉ Trần Khánh Dư nói)

```
Epic cinematic historical war film, live-action, photorealistic, vertical 9:16, 8 seconds, one continuous shot.
Vietnam, January 1288, Vân Đồn bay: a narrow channel between two towering limestone karst walls, late-morning sun shafts through mist, fast green water. A long line of heavy, deep-hulled wooden cargo junks with matting sails, decks piled with rice sacks, crawls slowly through the channel below.
High on a rock ledge on the left stands the Vietnamese general Trần Khánh Dư in a dark brown robe with a black sash and a topknot, seen ONLY from behind, his face never visible. Beside him a bare-chested soldier stands at a huge war drum.
Camera: starts behind the general's shoulder looking down at the convoy, slow push-in. At 6 seconds he raises his right arm high and swings it down; the drummer strikes the drum hard; birds burst from the cliffs.
Dialogue (0.5–7s), only the general speaks (his mouth is never visible), calm and steady deep male voice in his late 40s, Northern Vietnamese accent, in Vietnamese: "Đầu đoàn đã qua eo đá. Chặn đầu! Chặn đuôi! Không để chiếc nào quay ra. Toàn quân… đánh!"
No other voice. Nobody else speaks.
Audio: creaking hulls, slow oars, rushing current, wind in the cliffs, then one massive war drum hit on the last word. No music.
```

**Phụ đề (em chèn khi dựng):** `Trần Khánh Dư: / Đầu đoàn đã qua eo đá. / Chặn đầu! Chặn đuôi! / Không để chiếc nào / quay ra. Toàn quân… đánh!` (0.5–7,0s)

## Clip 6 · Hàng trăm thuyền lao ra (chỉ người dẫn chuyện nói)

```
Epic cinematic historical naval battle, live-action, photorealistic, vertical 9:16, 8 seconds, one continuous shot.
Vietnam, January 1288, Vân Đồn bay: the same narrow channel between towering limestone karst walls with dark caves, late-morning sun, mist and rising smoke.
Huge sweeping aerial shot: hundreds of small, light, flat-bottomed Vietnamese war boats burst out at full speed from every cove and cave on both sides, oars flashing, sailors with topknots in brown tunics rowing hard. They pour across the water and lock both ends of the channel, trapping the long line of heavy wooden cargo junks loaded with rice sacks. The first fire arrows arc toward the matting sails at the very end.
No blood, no bodies, nobody killed on screen. No flags or banners of any kind. No text on screen.
Narration (0.5–7.5s), off-screen voice-over, nobody on screen speaks: a calm, deep, slow male baritone, documentary style, Northern Vietnamese accent, in Vietnamese: "Hàng trăm thuyền nhẹ từ khắp các khe đảo lao ra như tên bắn, khóa chặt hai đầu luồng."
Audio: thunderous war drums, hundreds of oars splashing, battle cries echoing off the cliffs, wind. No music.
```

**Phụ đề:** `Hàng trăm thuyền nhẹ / từ khắp các khe đảo / lao ra như tên bắn, / khóa chặt hai đầu luồng.` (0.5–7,5s)

## Negative (dán vào ô Negative prompt nếu có)

```
subtitles, captions, on-screen text, watermark, flags, banners, modern objects, blood, gore, dead bodies, drowning, children, cartoon, anime, extra speakers, music
```

## Mẹo khi chạy Veo 3.1

- Giữ đúng **9:16** và **8 giây**. Hai clip này nối nhau bằng chuyển cảnh lóe trắng 0,3 giây khi dựng.
- Nếu Veo cho tiếng Việt chưa rõ: tạo lại 2–3 lần rồi chọn bản đọc tròn chữ nhất; hoặc để Veo làm hình và âm thanh trận, phần lời em ghép giọng đọc riêng khi dựng.
- Nếu Veo vẽ ra mặt tướng: thêm câu `The general stays with his back to the camera for the entire shot.` vào cuối prompt clip 5.
- Gửi em hai clip Veo, em ghép thử vào bản dựng tập 4 cùng các clip Muse để so chất lượng.
