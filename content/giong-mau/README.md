# Giọng mẫu nhân vật

| File | Nhân vật | Nguồn | Ghi chú |
|---|---|---|---|
| `anh-tu-mau.wav` | **Anh Tư** | Gemini TTS (gemini-3.8-flash-tts, giọng "Charon", lời dặn: nam miền Trung, giọng Huế, khoảng 30 tuổi, tỉnh bơ), tạo 25/11/2026 | 25,6 giây. **Bản thử**: nếu anh tự thu hoặc chọn được giọng ưng hơn, thay file này (10–60 giây, chỉ một người nói, không nhạc nền) |

Dùng với `../tools/dong-giong.py` để đổi giọng Anh Tư trong mọi clip Muse về đúng giọng này:

```
python3 ../tools/dong-giong.py --mau anh-tu-mau.wav --doan 5.0-9.6 --ra da-doi-giong tkd1-1.mp4 tkd1-2.mp4 ...
```

`--doan` chỉ định giây có câu của Anh Tư (thường 5–10 giây của mỗi clip, xem phụ đề trong `.plan.txt`), để giọng viên chỉ huy, người dẫn chuyện… trong cùng clip giữ nguyên. Bỏ `--doan` nếu cả clip chỉ có Anh Tư nói.
