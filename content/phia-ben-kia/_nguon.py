#!/usr/bin/env python3
"""Nguồn của loạt "Phía bên kia" (POV lính phía đối phương, cú lật ở cuối). Sửa ở đây rồi chạy: python3 _nguon.py

Làm lại từ bản SHORT.md "Bạn là lính giữ thành. Ngày thứ 42, viện binh vẫn chưa tới."
- Giữ cú lật: người xem tưởng mình là lính Việt, cuối video mới biết mình là lính nhà Tống.
- Theo công thức video 1,4 triệu: người lính thường, câu thoại đời thường đáng gửi bạn bè, Anh Tư xuất hiện ở cú lật.
- Kiểm duyệt TikTok: không có tự tử hay tự thiêu (kể cả bằng lời), không máu, không xác người, không trẻ em,
  không bêu riếu dân tộc nào; lính Tống được kể với sự cảm thông.
- TikTok 30 giây = clip 1, 3, 5. YouTube 50 giây = đủ 5 clip.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from series import build  # noqa: E402

ANH_TU = ("a Vietnamese soldier around 30 with deeply tanned skin, a scar across his left eyebrow and a wide grin "
          "with a chipped front tooth")

SAFE = ("No blood, no gore, no corpses, no wounded close-ups, no people on fire, no children; arrows hit stone and "
        "wood, never people. No visible writing on banners.")

NOTE = ("**Cú lật:** 4 clip đầu không lộ năm, tên thành hay phe. Mốc thời gian chỉ ghi \"Ngày thứ 42\". Đến clip 5, "
        "dòng mốc mới hiện **\"Ung Châu, năm 1076 · Bạn là lính nhà Tống\"**. **Kiểm duyệt:** đọc mục \"Kiểm duyệt "
        "TikTok\" trong `README.md` trước khi đăng.")

EPISODES = [
    dict(
        slug="ngay-thu-42-ung-chau-1076", prefix="pbk1",
        title="Bạn là lính giữ thành. Ngày thứ 42, viện binh vẫn chưa tới.",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử (đã kiểm tra ở tập Lý Thường Kiệt):** cuối năm 1075, quân Đại Việt đánh sang đất Tống. "
                 "Thành Ung Châu (nay là Nam Ninh, Trung Quốc) bị vây từ khoảng 18/1/1076 đến khoảng 1/3/1076, hơn 40 "
                 "ngày. Viện binh Tống do Trương Thủ Tiết dẫn bị quân Lý đánh tan ở ải Côn Lôn, không tới được thành. "
                 "Quân Lý xếp bao đất sát chân thành thành con dốc để leo lên. Dọc đường, quân Lý dán bài *Phạt Tống lộ "
                 "bố văn* đổ lỗi cho phép thanh miêu, trợ dịch của Vương An Thạch. Tri châu Tô Giám không chịu hàng.\n\n"
                 "**Hư cấu:** người lính Tống, bạn đồng ngũ Lão Trương, chuyện tờ hịch lọt vào trong thành, cảnh Anh Tư "
                 "và mọi lời thoại.\n\n"
                 "**Không đưa vào video (vì kiểm duyệt):** cái chết của Tô Giám và con số thương vong."),
        setting=("Yongzhou, a walled city of the Northern Song dynasty in southern China, early spring 1076, during a "
                 "long siege: rammed-earth wall faced with grey brick, crenellated parapet, wooden gate tower with dark "
                 "tiled roof; grey dawn mist, smoke haze, cold desaturated colors. The viewer and his friend are ordinary, "
                 "tired Song foot soldiers in dark red padded jackets and cloth head-wraps, gaunt and dirty but human and "
                 "sympathetic; the friend, Lão Trương, is a skinny, sarcastic veteran around 45 with a thin moustache. "
                 "The besieging army are 11th-century Đại Việt soldiers in dark tunics, conical woven helmets, round "
                 f"rattan shields, long spears, plain red and yellow banners, a few war elephants far behind. {SAFE}"),
        hook="POV: Lính giữ thành / Ngày thứ 42",
        end="Cùng một trận, hai bên nhớ hai cách. / Follow để xem quân Tống phản công →",
        clips=[
            dict(name="Viện binh sắp tới", label="Ngày thứ 42",
                 img="First-person close-up at grey dawn of dirty, cracked hands gripping a stone parapet, a skinny sarcastic soldier around 45 with a thin moustache leaning beside the viewer, below in the mist countless campfires of a besieging army, realistic, cold desaturated colors, no blood, vertical 9:16.",
                 vid="0-5s: Close-up: the viewer's cracked hands grip the stone parapet; an officer's voice calls along the wall: \"Giữ vững! Viện binh sắp tới!\" Two arrows thud into the stone beside the camera. 5-10s: Lão Trương, leaning on the parapet, doesn't even look up: \"Câu đó nghe bốn mươi ngày rồi. Tai tao thuộc hơn tên vợ.\"",
                 subs=[(0.5, 4.8, "Giữ vững! / Viện binh sắp tới!"),
                       (5.0, 9.8, "Câu đó nghe bốn mươi ngày rồi. / Tai tao thuộc hơn tên vợ.")]),
            dict(name="Tờ hịch của giặc", tiktok="bo", label="Ngày thứ 42 · giữa buổi",
                 img="First-person view of tired soldiers sitting on top of a city wall, one holding a large crumpled sheet of paper found tied to an arrow, the skinny veteran reading it with a confused face, no visible writing in close-up, realistic, vertical 9:16.",
                 vid="0-5s: A soldier pulls a folded paper off an enemy arrow and hands it over; Lão Trương reads, frowning: \"Bên kia bảo đánh sang để cứu dân mình khỏi phép thanh miêu của Vương An Thạch?\" 5-10s: The viewer stares at him: \"Nó đánh để cứu mình khỏi thuế... còn mình giữ thành cho ai?\"",
                 subs=[(0.5, 4.8, "Bên kia bảo đánh sang / để cứu dân mình khỏi phép thanh miêu / của Vương An Thạch?"),
                       (5.0, 9.8, "Nó đánh để cứu mình khỏi thuế... / còn mình giữ thành cho ai?")]),
            dict(name="Con dốc bao đất", label="Ngày thứ 42 · chiều",
                 img="First-person view looking down over a city wall at a steep ramp made of thousands of stacked earth sacks rising against the wall, almost reaching the parapet, besieging soldiers carrying more sacks up, the skinny veteran beside the viewer staring down, realistic, no blood, vertical 9:16.",
                 vid="0-5s: The viewer looks down: against the outside of the wall, a huge ramp of stacked earth sacks has grown almost to the top, and a chain of enemy soldiers keeps carrying more. 5-10s: Lão Trương says flatly: \"Hôm qua dốc đến thắt lưng. Hôm nay đến cằm. Mai nó vào tận bếp!\"",
                 subs=[(5.0, 9.8, "Hôm qua dốc đến thắt lưng. / Hôm nay đến cằm. / Mai nó vào tận bếp!")]),
            dict(name="Tin đến muộn", tiktok="bo", label="Ngày thứ 42 · chạng vạng",
                 img="First-person view on a city wall at dusk, a thin exhausted messenger whispering to two soldiers crouched behind the parapet, the skinny veteran's face frozen in disbelief, realistic, no blood, vertical 9:16.",
                 vid="0-5s: A messenger crouches beside them and whispers: \"Viện binh bị đánh tan ở Côn Lôn rồi. Từ ba tuần trước.\" 5-10s: The viewer whispers back, stunned: \"Ba tuần trước?! Thế ai hô sắp tới suốt ba tuần nay?\" Lão Trương slowly closes his eyes.",
                 subs=[(0.5, 4.8, "Viện binh bị đánh tan ở Côn Lôn rồi. / Từ ba tuần trước."),
                       (5.0, 9.8, "Ba tuần trước?! / Thế ai hô sắp tới suốt ba tuần nay?")]),
            dict(name="Bạn đứng phía nào?", label="Ung Châu · năm 1076 / Bạn là lính nhà Tống",
                 img=f"First-person high view from a city wall at dawn, a huge column of 11th-century Đại Việt soldiers with conical woven helmets, rattan shields and plain red and yellow banners pouring up a ramp of earth sacks onto the wall, war elephants far behind, {ANH_TU} reaching the top of the ramp and grinning at the viewer, no blood, realistic, vertical 9:16.",
                 vid=f"0-5s: Drums thunder; the enemy army pours up the ramp of earth sacks onto the wall; the camera rises into a high wide shot: an endless column of Đại Việt soldiers with conical woven helmets, rattan shields and red and yellow banners, war elephants far behind. 5-10s: At the top of the ramp, a grinning Đại Việt soldier with a chipped front tooth and a scar on his eyebrow ({ANH_TU}) waves cheerfully at the viewer: \"Chào anh! Cái dốc này em đắp đấy!\" Lão Trương drops his spear and raises both hands.",
                 subs=[(5.0, 9.5, "Chào anh! / Cái dốc này em đắp đấy!")]),
        ],
        caption=("Bạn là lính giữ thành. Ngày thứ 42, viện binh vẫn chưa tới… 😶 Xem đến cuối mới biết mình đứng phía "
                 "nào. (Video dựng bằng AI, lời thoại là hư cấu, chi tiết lịch sử ở bình luận ghim.)"),
        tags="#lythuongkiet #ungchau #1076 #phiabenkia",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#anhtu", note=NOTE,
          unit="Tập", file_unit="tap")
