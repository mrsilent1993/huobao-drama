#!/usr/bin/env python3
"""Nguồn của loạt "Điều sách giáo khoa không kể". Sửa ở đây rồi chạy: python3 _nguon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

EPISODES = [
    dict(
        slug="ly-thuong-kiet-danh-tong", prefix="sgk1",
        title="Lý Thường Kiệt đánh Tống: điều sách giáo khoa không kể",
        length="60 giây · 6 clip (lên đường, bài hịch, thành Ung Châu, Tô Giám, con số của sử Tống, rút quân)",
        history=(
            "**Những điều sách giáo khoa ít kể, đã kiểm tra nguồn:**\n\n"
            "1. **Đại tướng đã khoảng 56 tuổi.** Lý Thường Kiệt sinh năm 1019. Nhiều sách cũ (*Việt điện u linh*, "
            "*Đại Việt sử ký tiền biên*, *Lịch triều hiến chương loại chí*) chép ông là **hoạn quan**. Việc này **còn "
            "tranh cãi**: có ý kiến cho \"hoạn quan\" chỉ là làm quan, và có sách chép ông có vợ. Khi nói trong video, "
            "dùng cách nói \"sách cũ chép\", không khẳng định.\n"
            "2. **Bài hịch nhắm vào Vương An Thạch.** *Phạt Tống lộ bố văn*, được chép lại trong sách Tống *Tục tư trị "
            "thông giám trường biên*, đổ lỗi cho vua Tống nghe theo Vương An Thạch đặt ra phép \"thanh miêu\", \"trợ "
            "dịch\" làm dân khổ. Bài hịch tuyên bố quân Lý sang để \"cứu vớt muôn dân khỏi nơi chìm đắm\". Đây là đòn "
            "chiến tranh tâm lý, đánh đúng vào cuộc tranh cãi cải cách đang nóng trong triều Tống.\n"
            "3. **Tô Giám giữ Ung Châu 42 ngày.** Quân Lý đến khoảng 18/1/1076, thành vỡ khoảng 1/3/1076. Viên quan "
            "giữ thành Tô Giám phát hết tiền kho cho dân, phao tin viện binh sắp đến, giữ cả vợ con ở lại để dân không "
            "bỏ chạy. Khi thành vỡ, ông không hàng: cho người nhà tự vẫn rồi tự thiêu. Viện binh nhà Tống không bao giờ đến.\n"
            "4. **Con số của sử Tống.** Sử Tống chép rằng sau khi thành vỡ, quân Lý giết hơn 5 vạn người trong thành. "
            "Ở Liêm Châu, khoảng 8.000 người bị bắt đi khuân đồ cũng bị giết. Đây là số liệu do phía Tống chép, **có "
            "thể bị phóng đại**, nhưng sách giáo khoa hầu như không nhắc. Tập phim chỉ nói đến con số này một cách trầm "
            "lắng, không dựng cảnh máu me.\n"
            "5. **Mục tiêu là phá căn cứ, không phải chiếm đất.** Quân Lý phá các nơi nhà Tống tập trung quân lương ở "
            "Khâm Châu, Liêm Châu, Ung Châu rồi rút về. Sau chiến tranh, hai bên còn đàm phán nhiều năm, trao trả tù "
            "binh và đòi lại một số châu. Các nguồn chép mốc năm không thống nhất (khoảng 1078–1084).\n\n"
            "**Nguồn:** *Tục tư trị thông giám trường biên* (Tống), *Tống sử* (theo Viện Sử học Việt Nam, 2012), "
            "Hoàng Xuân Hãn *Lý Thường Kiệt*, *Việt điện u linh tập*; các bài Wikipedia tiếng Việt \"Trận Ung Châu\", "
            "\"Lý Thường Kiệt\", \"Phạt Tống lộ bố văn\" làm đầu mối tra cứu.\n\n"
            "**Hư cấu:** người lính kể chuyện, mọi lời thoại, và câu nói của người nông dân Tống là dựng thêm. Không "
            "có câu nói nào trong tập được gán là lời thật của Lý Thường Kiệt."
        ),
        setting=("Vietnam and southern Song China, Lý dynasty, winter 1075 to spring 1076. Đại Việt soldiers with short "
                 "cropped hair, black-lacquered teeth, brown and dark-red uniforms, rattan shields, spears, crossbows, "
                 "war elephants; General Lý Thường Kiệt is a lean, dignified man in his mid-50s with a smooth beardless "
                 "face, sharp calm eyes, dark armor and a red cloak; Song villagers and soldiers in Song-dynasty clothes "
                 "and armor; the walled city of Yongzhou (Ung Châu) with brick walls and watchtowers; the Song governor "
                 "Tô Giám is a stern, grey-bearded official in Song armor. No gore, no blood, no bodies on screen."),
        hook="Lý Thường Kiệt đánh Tống: / điều sách giáo khoa / không kể",
        end="Năm sau, quân Tống sang báo thù... / Follow để xem mai bạn giữ / phòng tuyến sông Như Nguyệt →",
        clips=[
            dict(name="Đánh giặc ở nhà giặc", label="Thăng Long · cuối năm 1075",
                 img="First-person view of a young soldier in an army camp outside an ancient Vietnamese capital in winter 1075, rows of soldiers and war elephants, a lean dignified general in his mid-50s with a smooth beardless face, dark armor and red cloak addressing the troops, realistic, vertical 9:16.",
                 vid="0-5s: The lean general in a red cloak addresses the troops calmly: \"Nhà Tống đang gom quân lương để sang đánh ta. Ta sang trước.\" The young viewer whispers to the soldier beside him: \"Đánh giặc... ở nhà giặc ạ?\" 5-10s: As the army starts marching, two veterans whisper behind him: \"Đại tướng năm nay ngoài năm mươi rồi đấy.\" \"Sách còn chép ông là hoạn quan.\" The viewer looks at the general's back, impressed: \"Thế mà dẫn cả mười vạn quân...\"",
                 subs=[(0.5, 3.0, "Nhà Tống đang gom quân lương để sang đánh ta. / Ta sang trước."),
                       (3.0, 4.9, "Đánh giặc... ở nhà giặc ạ?"),
                       (5.0, 7.5, "Đại tướng năm nay ngoài năm mươi rồi đấy. / Sách còn chép ông là hoạn quan."),
                       (7.5, 9.8, "Thế mà dẫn cả mười vạn quân...")]),
            dict(name="Bài hịch dán dọc đường", label="Đất Tống · đầu năm 1076",
                 img="First-person view on a village road in southern Song China, 1076, the viewer pasting a large written proclamation onto a wooden notice board, Song villagers crowding around to read it, an old Song farmer squinting at the text, realistic, vertical 9:16.",
                 vid="0-5s: The viewer pastes a large proclamation on a village notice board; an old Song farmer reads it aloud slowly: \"Quân Nam sang... để cứu dân Tống khỏi phép thanh miêu, trợ dịch của Vương An Thạch?\" 5-10s: The farmer turns to the viewer, hopeful: \"Thế các anh đánh xong có bỏ thuế cho tôi không?\" The viewer scratches his head: \"...Cái đó em không được dặn.\"",
                 subs=[(0.5, 4.8, "Quân Nam sang... để cứu dân Tống khỏi / phép thanh miêu, trợ dịch của Vương An Thạch?"),
                       (5.0, 7.5, "Thế các anh đánh xong / có bỏ thuế cho tôi không?"),
                       (7.5, 9.8, "...Cái đó em không được dặn.")]),
            dict(name="Viện binh sắp đến", label="Thành Ung Châu · ngày thứ 30 vây thành",
                 img="First-person view from outside the brick walls of a Song-dynasty city under siege, 1076, Đại Việt soldiers with shields and ladders, on the wall a stern grey-bearded Song governor in armor shouting down, banners, smoke, realistic, vertical 9:16.",
                 vid="0-5s: Outside the brick walls, day thirty of the siege; on the battlements the grey-bearded governor Tô Giám shouts to his men: \"Giữ vững! Viện binh sắp đến rồi!\" His soldiers cheer weakly. 5-10s: The viewer, crouching behind a rattan shield, mutters to the soldier next to him: \"Ông ấy hô câu đó từ ngày thứ ba rồi...\" Nobody on either side sees any reinforcements on the horizon.",
                 subs=[(0.5, 4.8, "Giữ vững! Viện binh sắp đến rồi!"),
                       (5.0, 9.8, "Ông ấy hô câu đó từ ngày thứ ba rồi...")]),
            dict(name="Người giữ thành", tiktok="bo", label="Ngày thứ 42 · thành vỡ",
                 img="First-person view inside a captured Song-dynasty city at dusk, 1076, smoke rising from the governor's residence in the distance, Đại Việt soldiers standing still and silent, a veteran soldier lowering his spear, no bodies, no blood, realistic, vertical 9:16.",
                 vid="0-5s: Dusk on the forty-second day; the city has fallen. In the distance, flames rise from the governor's residence; the soldiers around the viewer stop and stand silent. A veteran says quietly: \"Tô Giám không chịu hàng. Ông ấy tự thiêu rồi.\" 5-10s: The veteran lowers his spear and says: \"Bên nào cũng có người giữ thành đến cùng.\" The viewer looks at the smoke without a word. No bodies or blood are shown.",
                 subs=[(0.5, 4.8, "Tô Giám không chịu hàng. / Ông ấy tự thiêu rồi."),
                       (5.0, 9.5, "Bên nào cũng có người giữ thành đến cùng.")]),
            dict(name="Con số trong sử nhà Tống", tiktok="0-5", label="Sáng hôm sau",
                 img="First-person view walking slowly through the quiet, smoke-hazed streets of a captured ancient walled city in the early morning, 1076, empty streets, a fallen banner on the ground, the viewer's hand picking up a dropped wooden toy, no bodies, no blood, realistic, somber, vertical 9:16.",
                 vid="0-5s: Early morning; the viewer walks slowly through empty, smoke-hazed streets. A calm narrator's voice says: \"Sử nhà Tống chép: hơn năm vạn người trong thành đã chết.\" 5-10s: The viewer bends down and picks up a small dropped wooden toy, looks at it, then sets it gently on a doorstep. The narrator continues: \"Con số có thể bị phóng đại. Nhưng sách giáo khoa gần như không nhắc.\" No bodies or blood are shown.",
                 subs=[(0.5, 4.8, "Sử nhà Tống chép: / hơn năm vạn người trong thành đã chết."),
                       (5.0, 9.8, "Con số có thể bị phóng đại. / Nhưng sách giáo khoa gần như không nhắc.")]),
            dict(name="Rút quân", tiktok="5-10", label="Rút quân về nước · mùa xuân 1076",
                 img="First-person view of a long column of Đại Việt soldiers and elephants marching south on a road in spring, carts loaded with captured supplies, the lean general in a red cloak riding beside the viewer, realistic, vertical 9:16.",
                 vid="0-5s: A long column marches south with carts of captured supplies; the viewer, walking beside the general's horse, asks: \"Thưa đại tướng, mình thắng rồi sao không giữ đất?\" 5-10s: The general looks ahead and answers: \"Kho lương của chúng đã cháy, đường tiến quân đã phá. Chúng muốn sang, phải làm lại từ đầu.\" The viewer looks back north at the distant smoke.",
                 subs=[(0.5, 4.8, "Thưa đại tướng, / mình thắng rồi sao không giữ đất?"),
                       (5.0, 9.8, "Kho lương của chúng đã cháy, đường tiến quân đã phá. / Chúng muốn sang, phải làm lại từ đầu.")]),
        ],
        caption=("Đại tướng ngoài 50 tuổi, sách cũ chép là hoạn quan, dán hịch dọc đường bảo sang \"cứu dân Tống\" khỏi "
                 "cải cách của Vương An Thạch. Còn viên quan giữ Ung Châu thì cầm cự 42 ngày rồi tự thiêu chứ không hàng. "
                 "Sử Tống chép một con số mà sách giáo khoa gần như không nhắc. Bạn từng nghe điều nào trong số này chưa? 👇 "
                 "(Video dựng bằng AI, lời thoại là hư cấu, chi tiết lịch sử có nguồn trong phần mô tả.)"),
        tags="#lythuongkiet #nhaly #ungchau #1075 #sgkkhongke",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#dieusgkkhongke",
          unit="Tập", file_unit="tap")
