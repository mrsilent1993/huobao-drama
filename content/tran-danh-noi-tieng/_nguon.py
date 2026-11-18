#!/usr/bin/env python3
"""Loạt "Trận đánh nổi tiếng": mỗi trận một tập 5 clip, công thức Anh Tư. Sửa ở đây rồi chạy: python3 _nguon.py

Các trận đã có ở loạt khác (Bạch Đằng 938/981/1288, Như Nguyệt, Ung Châu, Chi Lăng, Rạch Gầm, Ngọc Hồi) không làm lại.
Chuẩn trang phục: ../nghien-cuu/chuan-hinh-anh-quan-doi.md (các mục ở đây là ⚠️ hiểu biết chung).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from series import build  # noqa: E402

FACE = ("a Vietnamese man around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin with a "
        "chipped front tooth, very expressive face")
NO_TEXT = ("No visible writing or characters on clothes, boats, banners or signs; no flags; no European clothing, "
           "armor or ships; no blood, no dead bodies.")
TRAN = ("Trần dynasty Vietnamese soldiers and boatmen with hair in topknots and black-lacquered teeth, in brown or dark "
        "cotton tunics, barefoot, with spears and bows")
MONGOL = ("Mongol soldiers in long fur-trimmed deel robes or leather lamellar armor, fur-lined pointed hats or round "
          "helmets, composite bows, small sturdy horses")
YUAN = ("Yuan army soldiers in leather lamellar armor and round helmets, fur-trimmed robes, composite bows; large "
        "wooden Chinese-style junks with matting sails")
MING = ("Ming soldiers in red padded cotton coats, round iron helmets with a red tassel, some in studded brigandine "
        "armor, with spears and swords; officers in round-collared robes and black gauze caps")
VIS = {
    "mong": ("**Chuẩn hình ảnh (⚠️ hiểu biết chung, xem `../nghien-cuu/chuan-hinh-anh-quan-doi.md`):** quân Trần búi "
             "tóc, răng đen, áo vải nâu sẫm, chân đất; quân Mông Cổ mặc áo dài viền lông hoặc giáp vảy da, mũ lông "
             "nhọn, cung sừng, ngựa thấp. Không có chữ, không cờ, không máu."),
    "nguyen": ("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** quân Trần búi tóc, răng đen, áo vải nâu sẫm, cánh tay có vết "
               "xăm sẫm không đọc được chữ; quân Nguyên mặc giáp vảy da, mũ tròn; thuyền lương là thuyền gỗ lớn buồm "
               "cót. Không có chữ, không cờ, không máu."),
    "minh": ("**Chuẩn hình ảnh (⚠️ hiểu biết chung):** quân Minh mặc áo bông độn màu đỏ, mũ sắt tròn có tua đỏ, một số "
             "mặc giáp đinh; nghĩa quân Lam Sơn áo vải nâu, khăn quấn đầu. Không có chữ, không cờ, không máu."),
}

NOTE = ("**Trận đánh nổi tiếng:** mỗi trận một tập theo công thức Anh Tư (sẹo ngang lông mày trái, răng cửa mẻ, cười "
        "toe; ảnh tham chiếu trong `../bach-dang/README.md`). Các vị tướng, vua chỉ xuất hiện trang trọng; mọi câu đùa "
        "nhắm vào Anh Tư. **Bản TikTok 30 giây** gồm clip 1, 3, 5; **bản YouTube 50 giây** gồm đủ 5 clip.")
END = "Follow để xem / trận đánh tiếp theo →"

EPISODES = [
    # ------------------------------------------------------------------ 1258
    dict(
        slug="cheo-thuyen-vua-dong-bo-dau-1258", prefix="td1258",
        title="Chèo thuyền đưa vua đi lánh giặc, nghe ông Thái sư nói một câu mà hết sợ (Đông Bộ Đầu, 1258)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** cuối năm 1257, quân Mông Cổ do Ngột Lương Hợp Thai chỉ huy tràn vào Đại Việt. Vua Trần Thái "
                 "Tông lui quân, theo đường sông rời kinh đô. Vua hỏi Thái sư Trần Thủ Độ, ông đáp: \"Đầu thần chưa rơi "
                 "xuống đất, xin bệ hạ đừng lo\" (*Đại Việt sử ký toàn thư*, mức B). Tháng Chạp năm Đinh Tỵ (đầu năm "
                 "1258), vua đem quân thủy ngược sông đánh úp ở Đông Bộ Đầu (Hà Nội); quân Mông Cổ rút về. Sử chép dọc "
                 "đường rút, quân giặc mỏi mệt không cướp phá, người đương thời gọi là \"giặc Phật\" (mức B). Sử nhà Nguyên "
                 "cũng chép cuộc tiến quân này. **Hư cấu:** Anh Tư chèo thuyền và mọi lời thoại ngoài câu của Trần Thủ Độ. "
                 "Không dựng cảnh Thăng Long bị tàn phá."),
        setting=("Vietnam, winter 1257 to early 1258, the wide Red River: a long royal wooden boat with a carved dragon "
                 "prow (no writing), many smaller boats, misty riverbanks. The king is seen only from behind in a yellow "
                 "robe. Thái sư Trần Thủ Độ is a stern elderly Vietnamese man around 64 with a grey beard, in a dark "
                 f"official robe, utterly calm. {TRAN}. {MONGOL} appear only in the last clip, at a distance. "
                 f"Anh Tư is {FACE}, a boatman in a brown tunic with a head wrap. {NO_TEXT}"),
        visual=VIS["mong"],
        hook="POV: Chèo thuyền / đưa vua / đi lánh giặc",
        end=END,
        clips=[
            dict(name="Chèo đều", label="Sông Hồng · cuối năm 1257",
                 img=f"First-person view from the oars of a long royal boat with a carved dragon prow on a misty river, the king seen only from behind under a canopy, {FACE} rowing beside the viewer with trembling hands, realistic, vertical 9:16.",
                 vid=("0-5s: An officer walks along the royal boat: \"Chèo đều. Vua đi lánh giặc, không được hoảng.\" "
                      "5-10s: Anh Tư, rowing, whispers to the viewer: \"Em không hoảng... tay em tự run thôi ạ.\""),
                 subs=[(0.5, 4.8, "Chèo đều. Vua đi lánh giặc, / không được hoảng."),
                       (5.0, 9.5, "Em không hoảng... / tay em tự run thôi ạ.")]),
            dict(name="Các quan bàn", tiktok="bo", label="",
                 img=f"First-person view on the royal boat, officials in dark robes whispering anxiously in a group, {FACE} rowing nearby and leaning his ear toward them, realistic, vertical 9:16.",
                 vid=("0-5s: Officials huddle and whisper anxiously about where to flee; one points far to the north, "
                      "another far to the south. 5-10s: Anh Tư leans toward the viewer: \"Các quan bàn đi đâu... mà nghe "
                      "toàn tên nước khác.\""),
                 subs=[(5.0, 9.5, "Các quan bàn đi đâu... / mà nghe toàn tên nước khác.")]),
            dict(name="Đầu thần chưa rơi", label="",
                 img=f"First-person view on a small boat approaching the royal boat, the stern grey-bearded Thái sư sitting perfectly calm, the king seen from behind leaning toward him, {FACE} at the oars staring, realistic, vertical 9:16.",
                 vid=("0-5s: The king, seen only from behind, asks a question; the grey-bearded Thái sư answers slowly "
                      "and calmly: \"Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo.\" 5-10s: Anh Tư whispers to the "
                      "viewer, amazed: \"Ông ấy nói câu đó... mà mặt tỉnh như đi chợ.\""),
                 subs=[(0.5, 4.8, "Đầu thần chưa rơi xuống đất, / xin bệ hạ đừng lo."),
                       (5.0, 9.5, "Ông ấy nói câu đó... / mà mặt tỉnh như đi chợ.")]),
            dict(name="Chèo ngược", tiktok="bo", label="Đêm hôm ấy",
                 img=f"First-person view at night on the river, dozens of boats turning around upstream silently with no lanterns, {FACE} rowing hard and confused, realistic, vertical 9:16.",
                 vid=("0-5s: At night, all the boats turn around silently and head back upstream without lanterns. Anh Tư "
                      "blinks: \"Ơ... chạy rồi, giờ chèo ngược lại ạ?\" 5-10s: The officer whispers: \"Đêm nay đánh. Chèo "
                      "khẽ thôi.\""),
                 subs=[(0.5, 4.8, "Ơ... chạy rồi, / giờ chèo ngược lại ạ?"),
                       (5.0, 9.5, "Đêm nay đánh. / Chèo khẽ thôi.")]),
            dict(name="Câu chốt", label="Đông Bộ Đầu · đầu năm 1258",
                 img=f"First-person view at dawn from a boat on the river, on the far bank a long column of Mongol horsemen retreating north in an orderly line, villagers watching from a distance, {FACE} at the oars with a huge chipped-tooth grin, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn; on the far bank a long column of Mongol horsemen retreats north quietly, passing villages "
                      "without stopping. A calm narrator's voice says: \"Đầu năm 1258, vua Trần đánh úp ở Đông Bộ Đầu. Quân "
                      "Mông Cổ rút về, dọc đường không dám cướp phá, dân gọi là giặc Phật.\" 5-10s: Anh Tư grins at the "
                      "camera: \"Thuyền vua em chèo đấy! Tay em giờ hết run rồi!\""),
                 subs=[(0.3, 4.8, "Năm 1258, vua Trần / đánh úp ở Đông Bộ Đầu. / Giặc rút, dân gọi \"giặc Phật\"."),
                       (5.0, 9.8, "Thuyền vua em chèo đấy! / Tay em giờ hết run rồi!")]),
        ],
        caption=("Chèo thuyền đưa vua đi lánh giặc, nghe ông Thái sư nói một câu mà hết sợ 😮 Năm 1258, Trần Thủ Độ nói: "
                 "\"Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo.\" Ít ngày sau, quân Trần thắng ở Đông Bộ Đầu, lần đầu "
                 "đánh lui quân Mông Cổ. Bạn có biết vì sao dân gọi quân Mông Cổ lúc rút là \"giặc Phật\" không? 👇"),
        tags="#trandanhnoitieng #dongbodau #tranthudo #nhatran #1258",
        tt_title="Chèo thuyền đưa vua đi lánh giặc, nghe Thái sư nói một câu mà hết sợ",
        hooks_alt=["POV: Đầu thần chưa rơi / xin bệ hạ đừng lo", "POV: Chạy rồi / giờ chèo ngược lại"],
        pin=("\"Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo\": câu nói nổi tiếng nhất của Trần Thủ Độ 🔥 Bạn còn nhớ "
             "câu nào khác của nhà Trần không? Follow để xem trận đánh tiếp theo!"),
        yt_title="Năm 1258: \"Đầu thần chưa rơi xuống đất\", lần đầu đánh lui quân Mông Cổ",
        yt_tags=("đông bộ đầu, trần thủ độ, đầu thần chưa rơi xuống đất, kháng chiến chống mông cổ, 1258, nhà trần, "
                 "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1285
    dict(
        slug="mac-giap-nha-tong-ham-tu-1285", voices={'Song refugee': "a warm older man's voice speaking Vietnamese with a light Chinese accent", 'Trần Nhật Duật': "a lively, quick, cheerful young nobleman's voice"}, prefix="td1285",
        title="Bị bắt mặc giáp của nước khác ra trận, giặc vừa nhìn thấy đã bỏ chạy (Hàm Tử, 1285)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** sau khi nhà Tống mất (1279), tướng Tống là Triệu Trung cùng thủ hạ chạy sang Đại Việt. Năm "
                 "1285, trong cuộc kháng chiến chống Nguyên lần hai, Chiêu Văn vương Trần Nhật Duật cùng quân Triệu Trung "
                 "đánh quân Toa Đô ở cửa Hàm Tử (Hưng Yên). Theo *Đại Việt sử ký toàn thư* (mức B), quân Nguyên thấy quân "
                 "Triệu Trung mặc giáp, cầm cung kiểu Tống thì tưởng nhà Tống sang đánh, hoảng sợ bỏ chạy. Trần Nhật Duật "
                 "nổi tiếng thông thạo tiếng nói nhiều dân tộc. Thơ Trần Quang Khải ghi lại: \"Chương Dương cướp giáo giặc, "
                 "Hàm Tử bắt quân thù.\" **Hư cấu:** Anh Tư mặc giáp Tống, người lính Tống dạy nói và mọi lời thoại."),
        setting=("Vietnam, spring 1285, the Hàm Tử crossing on the Red River (Hưng Yên): river flats, reeds, boats. "
                 f"{TRAN}, some with dark tattoo marks on their forearms (not legible). Song refugee soldiers are friendly "
                 "Chinese men in Song-style lamellar armor with crested helmets and red-brown robes, holding Song bows. "
                 "Prince Trần Nhật Duật is a lively Vietnamese nobleman in his twenties in fine armor, seen in profile. "
                 f"{YUAN} appear only on the far bank. Anh Tư is {FACE}. {NO_TEXT}"),
        visual=VIS["nguyen"],
        hook="POV: Mặc giáp / nước khác / ra trận",
        end=END,
        clips=[
            dict(name="Hôm nay mày là người Tống", label="Hàm Tử · mùa xuân năm 1285",
                 img=f"First-person view in a riverside camp, an officer holding out a Song-style crested helmet and lamellar armor, {FACE} in a plain brown tunic staring at it, Song refugee soldiers in the same armor behind, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is a Trần officer in dark armor; the RECEIVER is Anh Tư in a "
                      "plain brown tunic. 0-5s: The officer pushes a Song-style crested helmet into Anh Tư's hands: \"Mặc "
                      "vào. Hôm nay mày là người Tống.\" 5-10s: Anh Tư holds the helmet, baffled: \"Em... người Tống từ bao "
                      "giờ ạ?\""),
                 subs=[(0.5, 4.8, "Mặc vào. / Hôm nay mày là người Tống."),
                       (5.0, 9.5, "Em... người Tống / từ bao giờ ạ?")]),
            dict(name="Học nói", tiktok="bo", label="",
                 img=f"First-person view in camp, a friendly older Song refugee soldier in Song armor teaching {FACE} a phrase, both laughing, realistic, vertical 9:16.",
                 vid=("0-5s: A friendly older Song soldier says a short phrase in Chinese and gestures for Anh Tư to repeat; "
                      "Anh Tư tries and mangles it completely. 5-10s: The Song soldier laughs, pats his shoulder and says in "
                      "accented Vietnamese: \"Thôi... cứ im là giống nhất.\""),
                 subs=[(5.0, 9.5, "Thôi... / cứ im là giống nhất.")]),
            dict(name="Giặc nhìn thấy", label="",
                 img=f"First-person view from a line of soldiers in Song-style armor on a riverbank, across the water Yuan soldiers pointing in alarm and starting to run, {FACE} in a Song crested helmet beside the viewer, grinning, realistic, vertical 9:16.",
                 vid=("0-5s: The line of Song-armored soldiers steps forward on the bank; across the water Yuan soldiers "
                      "point, shout in alarm and begin to fall back in panic. 5-10s: Anh Tư, in his borrowed helmet, "
                      "whispers to the viewer: \"Mặc nhầm áo... mà giặc chạy mất dép.\""),
                 subs=[(0.5, 4.8, "Quân Nguyên tưởng / nhà Tống sang đánh!"),
                       (5.0, 9.5, "Mặc nhầm áo... / mà giặc chạy mất dép.")]),
            dict(name="Ông hoàng nói tiếng nước người", tiktok="bo", label="",
                 img=f"First-person view in camp, a lively young Vietnamese prince in fine armor seen in profile chatting cheerfully with Song refugee soldiers, {FACE} beside the viewer watching, amazed, realistic, vertical 9:16.",
                 vid=("0-5s: The young prince, seen in profile, chats fluently and cheerfully with the Song soldiers in their "
                      "language; they laugh together. 5-10s: Anh Tư whispers to the viewer: \"Ông hoàng nói được tiếng nước "
                      "người ta... em nói tiếng nước mình còn ngọng.\""),
                 subs=[(5.0, 9.5, "Ông hoàng nói được / tiếng nước người... em nói / tiếng nước mình còn ngọng.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view at sunset on the riverbank after victory, Trần and Song refugee soldiers cheering together, captured Yuan weapons piled up, {FACE} taking off the Song helmet with a huge chipped-tooth grin, realistic, vertical 9:16.",
                 vid=("0-5s: Sunset; Trần and Song soldiers cheer together beside a pile of captured weapons. A calm narrator's "
                      "voice says: \"Năm 1285, Trần Nhật Duật cùng quân Triệu Trung thắng ở Hàm Tử. Thơ Trần Quang Khải: "
                      "Chương Dương cướp giáo giặc, Hàm Tử bắt quân thù.\" 5-10s: Anh Tư takes off the helmet and grins at the "
                      "camera: \"Bộ giáp ấy em mặc! Mặc nhầm áo một lần, giặc nhớ cả đời!\""),
                 subs=[(0.3, 4.8, "Năm 1285, thắng ở Hàm Tử. / \"Chương Dương cướp giáo giặc, / Hàm Tử bắt quân thù.\""),
                       (5.0, 9.8, "Bộ giáp ấy em mặc! / Mặc nhầm áo một lần, / giặc nhớ cả đời!")]),
        ],
        caption=("Bị bắt mặc giáp của nước khác ra trận, giặc vừa nhìn thấy đã bỏ chạy 😂 Năm 1285 ở Hàm Tử, quân của tướng "
                 "Tống Triệu Trung (chạy sang Đại Việt sau khi nhà Tống mất) đánh cùng quân Trần, quân Nguyên tưởng nhà Tống "
                 "sang đánh nên hoảng sợ. Bạn có biết câu thơ \"Chương Dương cướp giáo giặc\" là của ai không? 👇"),
        tags="#trandanhnoitieng #hamtu #trannhatduat #chongnguyen #1285",
        tt_title="Bị bắt mặc giáp của nước khác ra trận, giặc vừa nhìn thấy đã bỏ chạy",
        hooks_alt=["POV: Mặc nhầm áo / mà giặc chạy", "POV: Hôm nay / mày là người Tống"],
        pin=("Gợi ý: tác giả câu thơ là một vị tướng nhà Trần, đánh thắng ở Chương Dương 😏 Ai đoán đúng tên, mình ghim "
             "lên đầu! Follow để xem trận đánh tiếp theo!"),
        yt_title="Năm 1285: mặc giáp nhà Tống ra trận, quân Nguyên nhìn thấy đã bỏ chạy (Hàm Tử)",
        yt_tags=("hàm tử, trần nhật duật, triệu trung, chương dương cướp giáo giặc, kháng chiến chống nguyên, 1285, "
                 "nhà trần, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1288 (bản đầy đủ 7 cảnh)
    dict(
        slug="ong-tuong-ban-than-van-don-1288", voices={'Trần Khánh Dư': 'a low, dry, unhurried male voice around 40, calm even under pressure'}, prefix="td1288",
        title="Khách quen bán than trên sông nói chuyện toàn binh pháp, mấy năm sau ông ấy cứu cả cuộc kháng chiến (Vân Đồn, 1288)",
        length=("hai video từ cùng 7 clip: **bản dài** (YouTube, khoảng 68 giây sau chuyển cảnh) và **bản ngắn** "
                "(TikTok, khoảng 43 giây) vẫn đủ cả 7 cảnh: mỗi cảnh cắt lấy 5 giây chứa câu quan trọng nhất, riêng "
                "cảnh lệnh bắt và cảnh kết giữ nguyên 10 giây"),
        history=("**Lịch sử (theo *Đại Việt sử ký toàn thư*, mức B; sử nhà Nguyên cũng chép việc mất thuyền lương, mức A):**\n\n"
                 "- **Năm 1282:** Trần Khánh Dư, một tướng giỏi, đang bị cách chức và tịch thu gia sản, về Chí Linh làm nghề "
                 "buôn than. Vua Trần Nhân Tông đi thuyền qua, thấy một chiếc thuyền buôn than, người lái đội nón lá, mặc áo "
                 "ngắn, nhận ra là Khánh Dư, liền cho mời về triều và dùng lại.\n"
                 "- **Cuối năm 1287:** ông làm phó tướng trấn giữ Vân Đồn (Quảng Ninh). Đoàn chiến thuyền của Ô Mã Nhi đánh "
                 "vượt qua được. Thượng hoàng sai sứ đến bắt ông về trị tội; ông xin khoan vài ngày để lập công chuộc tội.\n"
                 "- **Mấy hôm sau:** đoàn thuyền lương của Trương Văn Hổ theo sau đến nơi; Trần Khánh Dư đánh tan, bắt được "
                 "rất nhiều lương thực, khí giới. Thượng hoàng tha tội, nói rằng quân Nguyên trông vào lương thực, nay đã bị "
                 "bắt thì thế giặc không còn hung hăng được nữa. Hết lương, quân Nguyên phải tính đường rút, dẫn tới trận "
                 "Bạch Đằng tháng 4 năm 1288.\n\n"
                 "**Hư cấu:** Anh Tư, chuyện mặc cả hai đồng, mọi lời thoại (câu của sứ giả và Trần Khánh Dư phỏng theo ý sử "
                 "chép, không phải nguyên văn). Không dựng chuyện riêng tư dẫn tới việc ông bị cách chức. Không dựng cảnh "
                 "người chết đuối."),
        setting=("Vietnam, 1280s, northern Đại Việt. Trần Khánh Dư is a lean, sharp-eyed Vietnamese man around 40 with a "
                 "short beard: first as a charcoal trader in a conical hat and short brown tunic with charcoal-black hands "
                 "on a small wooden boat loaded with charcoal sacks; later in dark Trần-era armor. "
                 f"{TRAN}, some with dark tattoo marks on their forearms (not legible). {YUAN}. "
                 f"Anh Tư is {FACE}, first a villager in a brown shirt, later a sailor. {NO_TEXT}"),
        visual=VIS["nguyen"],
        hook="POV: Ông bán than / nói chuyện / toàn binh pháp",
        end="Ba tháng sau: Bạch Đằng 1288. / Follow để xem / trận đánh tiếp theo →",
        end_secs=1.6,
        clips=[
            dict(name="Ông bán than", tiktok="5-10", label="Chí Linh · năm 1282",
                 img=f"First-person view at a riverbank landing, a small wooden boat loaded with charcoal sacks, a lean sharp-eyed man in a conical hat with charcoal-black hands arranging charcoal pieces in neat rows on a mat, {FACE} holding an empty basket and watching, realistic, vertical 9:16.",
                 vid=("0-5s: On his charcoal boat at the landing, the trader arranges charcoal pieces in neat rows on a mat "
                      "and says calmly: \"Xếp than cũng như xếp quân: xếp đúng thì mới cháy đều.\" 5-10s: Anh Tư, holding "
                      "his basket, whispers to the viewer: \"Bác bán than... sao nói toàn binh pháp?\""),
                 subs=[(0.5, 4.8, "Xếp than cũng như xếp quân: / xếp đúng thì mới cháy đều."),
                       (5.0, 9.5, "Bác bán than... / sao nói toàn binh pháp?")]),
            dict(name="Vua mời", tiktok="0-5", noi=True, label="",
                 img=f"First-person view at the same riverbank landing, a long royal boat with a carved dragon prow stopping beside the small charcoal boat, a royal messenger bowing low to the charcoal trader, {FACE} beside the viewer with his basket, realistic, vertical 9:16.",
                 vid=("0-5s: A royal boat glides up and stops beside the charcoal boat; a messenger bows low to the trader: "
                      "\"Bệ hạ nhận ra ông. Mời ông về triều.\" 5-10s: Anh Tư drops his basket, charcoal rolling everywhere, "
                      "and whispers to the viewer: \"Em vừa mặc cả với ông ấy... mất hai đồng!\""),
                 subs=[(0.5, 4.8, "Bệ hạ nhận ra ông. / Mời ông về triều."),
                       (5.0, 9.5, "Em vừa mặc cả với ông ấy... / mất hai đồng!")]),
            dict(name="Lên làm tướng", tiktok="5-10", label="Vân Đồn · cuối năm 1287",
                 img=f"First-person view on a Trần war boat among steep rocky limestone islands in a bay, the lean sharp-eyed man now in dark armor addressing sailors, {FACE} among the sailors with an oar, amazed, realistic, vertical 9:16.",
                 vid=("0-5s: Among the rocky islands of the bay, the former charcoal trader, now in dark armor, addresses the "
                      "sailors: \"Giữ Vân Đồn. Không để thuyền giặc nào qua.\" 5-10s: Anh Tư, among the sailors, whispers to "
                      "the viewer: \"Hôm trước bán than... hôm nay giữ cả cửa biển.\""),
                 subs=[(0.5, 4.8, "Giữ Vân Đồn. / Không để thuyền giặc nào qua."),
                       (5.0, 9.5, "Hôm trước bán than... / hôm nay giữ cả cửa biển.")]),
            dict(name="Giặc vượt qua", tiktok="0-5", label="",
                 img=f"First-person view from a small Trần war boat as huge Yuan warships with matting sails push through a channel between rocky islands, small boats unable to stop them, {FACE} rowing desperately, realistic, vertical 9:16.",
                 vid=("0-5s: Huge Yuan warships with matting sails force their way through the channel between the rocks; the "
                      "small Trần boats cannot stop them. Anh Tư, rowing desperately, shouts: \"To quá, cản không nổi!\" "
                      "5-10s: The general stands on his boat, jaw clenched, silently watching the enemy fleet sail away "
                      "toward the mainland."),
                 subs=[(0.5, 4.8, "To quá, cản không nổi!"),
                       (5.0, 9.5, "Đoàn chiến thuyền của Ô Mã Nhi / vượt qua được Vân Đồn.")]),
            dict(name="Lệnh bắt", label="Mấy hôm sau",
                 img=f"First-person view on the deck of a war boat, a royal envoy holding out an arrest order (no visible text) to the lean general in dark armor, the general bowing calmly, {FACE} beside the viewer holding an oar, tense, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the envoy in a dark court robe holds the order; the general in dark armor "
                      "bows. 0-5s: The envoy: \"Thượng hoàng cho bắt tướng quân về trị tội.\" The general bows calmly: \"Xin "
                      "khoan vài ngày, để lập công chuộc tội.\" 5-10s: Anh Tư whispers to the viewer: \"Sếp bị dọa đuổi "
                      "việc... còn xin thêm mấy ngày chạy KPI.\""),
                 subs=[(0.3, 2.5, "Thượng hoàng cho bắt / tướng quân về trị tội."),
                       (2.5, 4.9, "Xin khoan vài ngày, / để lập công chuộc tội."),
                       (5.0, 9.5, "Sếp bị dọa đuổi việc... / còn xin thêm mấy ngày / chạy KPI.")]),
            dict(name="Thuyền lương", tiktok="0-5", label="Đêm hôm ấy",
                 img=f"First-person view at night from a small war boat hidden behind a rocky island, a long line of heavy, low-riding wooden junks loaded with rice sacks sailing past slowly, the general crouching at the bow, {FACE} peering out beside the viewer, realistic, vertical 9:16.",
                 vid=("0-5s: At night, from behind a rocky island, a long line of heavy junks loaded with rice sacks glides "
                      "past slowly. Anh Tư whispers: \"Thuyền gì mà toàn gạo... nồi cơm của cả đạo quân à?\" 5-10s: The "
                      "general, crouching at the bow, raises one hand and says quietly: \"Đánh.\""),
                 subs=[(0.5, 4.8, "Thuyền gì mà toàn gạo... / nồi cơm của cả đạo quân à?"),
                       (5.0, 9.5, "Đánh.")]),
            dict(name="Câu chốt", label="Rạng sáng",
                 img=f"First-person view at dawn among rocky islands, heavy grain junks captured and surrounded by small Trần war boats, rice sacks being unloaded, no people in the water, the lean general standing on a boat, {FACE} holding up a sack of rice with a huge grin, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn; small Trần war boats surround the captured grain junks and unload sacks; no people in the "
                      "water. A calm narrator's voice says: \"Trần Khánh Dư phá tan đoàn thuyền lương. Thượng hoàng tha tội: "
                      "giặc mất lương, hết đường hung hăng.\" 5-10s: Anh Tư holds up a sack of rice and grins at the camera: "
                      "\"Ông bán than ấy, em mua than của ông ấy đấy! ...Em còn nợ ông ấy hai đồng.\""),
                 subs=[(0.3, 4.8, "Trần Khánh Dư phá tan / đoàn thuyền lương. / Thượng hoàng tha tội."),
                       (5.0, 8.4, "Ông bán than ấy, em mua than / của ông ấy đấy! / ...Em còn nợ ông ấy hai đồng.")]),
        ],
        caption=("Khách quen bán than trên sông nói chuyện toàn binh pháp, mấy năm sau ông ấy cứu cả cuộc kháng chiến 😳 "
                 "Trần Khánh Dư từng bị cách chức, về Chí Linh buôn than, được vua Trần Nhân Tông nhận ra và dùng lại. "
                 "Năm 1288, sau khi để lọt chiến thuyền Ô Mã Nhi, ông xin vài ngày lập công, rồi phá tan đoàn thuyền lương "
                 "quân Nguyên ở Vân Đồn, mở đường cho trận Bạch Đằng. Bạn đã từng gặp \"cao nhân ẩn mình\" nào chưa? 👇"),
        tags="#trandanhnoitieng #vandon #trankhanhdu #chongnguyen #1288",
        tt_title="Ông bán than trên sông nói toàn binh pháp, mấy năm sau cứu cả cuộc kháng chiến",
        hooks_alt=["POV: Sếp bị dọa đuổi việc / còn xin thêm mấy ngày", "POV: Mặc cả / với một vị tướng"],
        pin=("Không có trận Vân Đồn thì chưa chắc có trận Bạch Đằng 1288 🔥 Xem trận Bạch Đằng ở trang cá nhân 👆 "
             "Follow để xem trận đánh tiếp theo!"),
        yt_title="Năm 1288: ông bán than được vua nhận ra, phá đoàn thuyền lương quân Nguyên ở Vân Đồn",
        yt_tags=("vân đồn, trần khánh dư, thuyền lương, trương văn hổ, ô mã nhi, trần nhân tông, kháng chiến chống "
                 "nguyên, 1288, nhà trần, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts"),
    ),
    # ------------------------------------------------------------------ 1426
    dict(
        slug="cay-lua-gia-tot-dong-1426", prefix="td1426",
        title="Bị sai ra ruộng cấy lúa ngay bên đường giặc đi qua, mắt không được nhìn lúa (Tốt Động – Chúc Động, 1426)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** tháng 11 năm 1426, tướng Minh Vương Thông đem đại quân từ Đông Quan đánh ra phía tây nam. "
                 "Nghĩa quân Lam Sơn đặt phục binh ở vùng đồng lầy Tốt Động và Chúc Động (Chương Mỹ, Hà Nội). Quân Minh sa "
                 "vào trận địa, thua lớn; thượng thư Trần Hiệp tử trận, Vương Thông bị thương, rút về cố thủ ở Đông Quan "
                 "(*Đại Việt sử ký toàn thư*, sử nhà Minh cũng chép trận thua này, mức A). Các nguồn ghi số quân khác nhau, "
                 "nên tập phim không nêu số. **Hư cấu:** Anh Tư giả làm nông dân cấy lúa để dò đường, mọi lời thoại. Không "
                 "dựng cảnh chết chóc."),
        setting=("Vietnam, November 1426, flat muddy rice fields and marshes beside a raised dirt road at Tốt Động – "
                 "Chúc Động: bamboo hedges, buffalo, mist. Lam Sơn fighters disguised as farmers in brown clothes and "
                 f"conical hats; real local farmers. {MING}. Anh Tư is {FACE}, disguised as a farmer, barefoot in the mud. "
                 f"{NO_TEXT}"),
        visual=VIS["minh"],
        hook="POV: Cấy lúa / ngay bên đường / giặc đi qua",
        end=END,
        clips=[
            dict(name="Ra ruộng cấy", label="Tốt Động · tháng 11 năm 1426",
                 img=f"First-person view at the edge of a muddy rice field beside a raised road, a Lam Sơn officer disguised as a farmer handing a bundle of rice seedlings to {FACE}, mist over the fields, realistic, vertical 9:16.",
                 vid=("Two clearly different men: the GIVER is a stern Lam Sơn officer disguised as a farmer; the RECEIVER is "
                      "Anh Tư. 0-5s: The officer hands him a bundle of seedlings: \"Ra ruộng cấy. Cấy chậm thôi, mắt nhìn "
                      "đường.\" 5-10s: Anh Tư stares at the seedlings: \"Đánh giặc mà... đi cấy lúa ạ?\" The officer: "
                      "\"Không hỏi.\""),
                 subs=[(0.5, 4.8, "Ra ruộng cấy. Cấy chậm thôi, / mắt nhìn đường."),
                       (5.0, 7.6, "Đánh giặc mà... / đi cấy lúa ạ?"),
                       (7.6, 9.6, "Không hỏi.")]),
            dict(name="Cấy ngược", tiktok="bo", label="",
                 img=f"First-person view in a muddy rice field, {FACE} planting seedlings while staring at the road, an old real farmer next to him pointing angrily at seedlings planted upside down, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư plants seedlings while staring at the road; an old farmer beside him scolds: \"Cấy ngược "
                      "rễ lên trời thế kia à?\" 5-10s: Anh Tư looks down, pulls one out quickly and grins: \"Em... cấy kiểu "
                      "mới cụ ạ.\""),
                 subs=[(0.5, 4.8, "Cấy ngược rễ lên trời / thế kia à?"),
                       (5.0, 9.5, "Em... cấy kiểu mới cụ ạ.")]),
            dict(name="Giặc đi qua", label="",
                 img=f"First-person view from a rice field as a long column of Ming soldiers in red padded coats and round helmets marches along the raised road, one soldier glancing down, {FACE} bent over the seedlings with a frozen smile, realistic, vertical 9:16.",
                 vid=("0-5s: A long column of Ming soldiers marches along the raised road; one glances down at the field. Anh "
                      "Tư smiles and waves a muddy hand, then bends back over the seedlings. 5-10s: He whispers to the viewer "
                      "without looking up: \"Diễn nông dân thôi... mà em cấy nhanh hơn cả nông dân thật.\""),
                 subs=[(5.0, 9.5, "Diễn nông dân thôi... / mà em cấy nhanh hơn / cả nông dân thật.")]),
            dict(name="Ám hiệu", tiktok="bo", label="",
                 img=f"First-person view in a misty rice field, {FACE} raising his conical hat high above his head as a signal, around him dozens of 'farmers' straightening up from the mud with spears hidden under straw, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư straightens up and raises his conical hat high; all around, dozens of 'farmers' rise from "
                      "the mud and pull spears out from under bundles of straw. 5-10s: Anh Tư whispers to the viewer: \"Cả "
                      "cánh đồng này... không có ai là nông dân thật.\""),
                 subs=[(5.0, 9.5, "Cả cánh đồng này... / không có ai là nông dân thật.")]),
            dict(name="Câu chốt", label="",
                 img=f"First-person view from a rice field at dusk, the Ming column on the road broken up and retreating in disorder toward the distant city, abandoned weapons in the mud, no bodies, {FACE} standing in the field with a huge chipped-tooth grin, realistic, vertical 9:16.",
                 vid=("0-5s: Dusk; the Ming column, broken up, retreats in disorder toward the distant city, leaving weapons "
                      "in the mud; no bodies shown. A calm narrator's voice says: \"Tháng 11 năm 1426, nghĩa quân Lam Sơn phục "
                      "kích ở Tốt Động – Chúc Động. Vương Thông bị thương, chạy về Đông Quan.\" 5-10s: Anh Tư grins at the "
                      "camera: \"Ruộng ấy em cấy đấy! Cấy ngược mà vẫn thắng!\""),
                 subs=[(0.3, 4.8, "Năm 1426, Lam Sơn phục kích / ở Tốt Động – Chúc Động. / Vương Thông chạy về Đông Quan."),
                       (5.0, 9.8, "Ruộng ấy em cấy đấy! / Cấy ngược mà vẫn thắng!")]),
        ],
        caption=("Bị sai ra ruộng cấy lúa ngay bên đường giặc đi qua, mắt không được nhìn lúa 🌾 Tháng 11 năm 1426, nghĩa "
                 "quân Lam Sơn phục kích quân Minh ở vùng đồng lầy Tốt Động – Chúc Động (Chương Mỹ, Hà Nội), Vương Thông "
                 "bị thương phải chạy về Đông Quan. Bạn có quê ở Chương Mỹ không? 👇"),
        tags="#trandanhnoitieng #totdongchucdong #lamson #leloi #1426",
        tt_title="Bị sai ra ruộng cấy lúa ngay bên đường giặc đi qua, mắt không được nhìn lúa",
        hooks_alt=["POV: Cả cánh đồng / không ai là nông dân thật", "POV: Cấy ngược rễ / lên trời"],
        pin=("Sau trận này, quân Minh chỉ còn cố thủ ở Đông Quan, và một năm sau thì có trận Chi Lăng 🔥 Xem tập Chi Lăng "
             "ở trang cá nhân 👆 Follow để xem trận đánh tiếp theo!"),
        yt_title="Năm 1426: cấy lúa ngay bên đường giặc đi qua (Tốt Động – Chúc Động)",
        yt_tags=("tốt động chúc động, lam sơn, lê lợi, vương thông, quân minh, 1426, chương mỹ, lịch sử việt nam, "
                 "pov lịch sử, anh tư, đại việt, shorts"),
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#trandanhnoitieng #anhtu", note=NOTE, unit="Tập", file_unit="tap")
