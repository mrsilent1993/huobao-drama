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

NOTE = ("**Cú lật:** cả 5 clip không lộ năm, tên thành hay phe, mốc thời gian chỉ ghi \"Ngày thứ 42\". Ở clip 5, "
        "người đưa tin báo Tri châu không chịu hàng, rồi giọng người kể xác nhận: \"Phải... bạn là lính nhà Tống. "
        "Ung Châu, năm 1076. Và đội quân ngoài kia... là quân Đại Việt.\" **Kiểm duyệt:** đọc mục \"Kiểm duyệt TikTok\" "
        "trong `README.md` trước khi đăng.")

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
                 "**Hư cấu:** người lính Tống, bạn đồng ngũ Lão Trương, chuyện tờ hịch lọt vào trong thành, Anh Tư thoáng qua ở clip 3 "
                 "và mọi lời thoại.\n\n"
                 "**Cái chết của Tô Giám:** chỉ nói bằng một câu báo tin (thà chết trong lửa, không chịu hàng), không có "
                 "hình ảnh lửa hay người. Con số thương vong không đưa vào video."),
        setting=("Yongzhou, a walled city of the Northern Song dynasty in southern China, early spring 1076, during a "
                 "long siege: rammed-earth wall faced with grey brick, crenellated parapet, wooden gate tower with dark "
                 "tiled roof; grey dawn mist, smoke haze, cold desaturated colors. The viewer and his friend are ordinary, "
                 "tired Song foot soldiers in dark red padded jackets and cloth head-wraps, gaunt and dirty but human and "
                 "sympathetic; the friend, Lão Trương, is a skinny, sarcastic veteran around 45 with a thin moustache. "
                 "The besieging army are 11th-century Đại Việt soldiers in dark tunics, conical woven helmets, round "
                 f"rattan shields, long spears, plain red and yellow banners, a few war elephants far behind. {SAFE}"),
        hook="POV: Lính giữ thành / Ngày thứ 42",
        end="Follow để xem / quân Tống phản công →", end_secs=1.2,
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
                 img=f"First-person view looking down over a city wall at a steep ramp made of thousands of stacked earth sacks rising against the wall, almost reaching the parapet, a chain of besieging soldiers carrying more sacks up, among them {ANH_TU} glancing up with a grin, the skinny veteran beside the viewer staring down, realistic, no blood, vertical 9:16.",
                 vid="0-5s: The viewer looks down: against the outside of the wall, a huge ramp of stacked earth sacks has grown almost to the top, and a chain of enemy soldiers keeps carrying more; one of them, with a chipped front tooth and a scar on his eyebrow, glances up and grins. 5-10s: Lão Trương says flatly: \"Hôm qua dốc đến thắt lưng. Hôm nay đến cằm. Mai nó vào tận bếp!\"",
                 subs=[(5.0, 9.8, "Hôm qua dốc đến thắt lưng. / Hôm nay đến cằm. / Mai nó vào tận bếp!")]),
            dict(name="Tin đến muộn", tiktok="bo", label="Ngày thứ 42 · chạng vạng",
                 img="First-person view on a city wall at dusk, a thin exhausted messenger whispering to two soldiers crouched behind the parapet, the skinny veteran's face frozen in disbelief, realistic, no blood, vertical 9:16.",
                 vid="0-5s: A messenger crouches beside them and whispers: \"Viện binh bị đánh tan ở Côn Lôn rồi. Từ ba tuần trước.\" 5-10s: The viewer whispers back, stunned: \"Ba tuần trước?! Thế ai hô sắp tới suốt ba tuần nay?\" Lão Trương slowly closes his eyes.",
                 subs=[(0.5, 4.8, "Viện binh bị đánh tan ở Côn Lôn rồi. / Từ ba tuần trước."),
                       (5.0, 9.8, "Ba tuần trước?! / Thế ai hô sắp tới suốt ba tuần nay?")]),
            dict(name="Phải... bạn là lính nhà Tống", label="Ngày thứ 42 · rạng sáng",
                 img="First-person high view from a city wall at grey dawn through drifting smoke, a huge column of 11th-century Đại Việt soldiers with conical woven helmets, round rattan shields, long spears and plain red and yellow banners pouring up a ramp of earth sacks onto the wall, a few war elephants far behind, a messenger kneeling beside the viewer, no fire in frame, no blood, realistic, vertical 9:16.",
                 vid="0-3.5s: Drums thunder as the enemy pours up the ramp onto the wall; a soot-faced messenger stumbles up beside the viewer and says, out of breath: \"Tri châu thà chết trong lửa, không chịu hàng.\" Lão Trương lowers his spear in silence. 3.5-10s: The camera slowly turns and rises into a high wide shot over the wall: an endless column of Đại Việt soldiers with conical woven helmets, rattan shields and red and yellow banners, war elephants far behind; everything goes quiet except the wind. A calm, low narrator's voice says slowly: \"Phải... bạn là lính nhà Tống. Ung Châu, năm 1076. Và đội quân ngoài kia... là quân Đại Việt.\" Hold on the wide view. No fire, no people burning, no bodies shown.",
                 subs=[(0.3, 3.5, "Tri châu thà chết trong lửa, / không chịu hàng."),
                       (3.8, 6.3, "Phải... / bạn là lính nhà Tống. / Ung Châu, năm 1076."),
                       (6.4, 9.8, "Và đội quân ngoài kia... / là quân Đại Việt.")]),
        ],
        caption=("Bạn là lính giữ thành. Ngày thứ 42, viện binh vẫn chưa tới… 😶 Xem đến cuối mới biết mình đứng phía "
                 "nào. (Video dựng bằng AI, lời thoại là hư cấu, chi tiết lịch sử ở bình luận ghim.)"),
        tags="#lythuongkiet #ungchau #1076 #phiabenkia",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="khieng-ong-dong-1288", prefix="pbk2",
        title="Bị bắt khiêng một cái ống đồng nặng trịch về nước, đến biên giới mới biết bên trong là ai (1288)",
        length="YouTube 50 giây (5 clip) · TikTok 30 giây (clip 1, 3, 5)",
        history=("**Lịch sử:** năm 1288, sau thất bại ở Bạch Đằng, quân Nguyên do Thoát Hoan (con trai Hốt Tất Liệt) "
                 "rút về phương Bắc theo đường bộ và bị quân Trần đánh dọc đường. Theo *Nguyên sử* và *Tân Nguyên sử*, "
                 "sau thất bại này Hốt Tất Liệt không muốn gặp lại Thoát Hoan, và Thoát Hoan phải đến ở Dương Châu cho đến khi "
                 "mất.\n\n"
                 "**Giai thoại (C):** chuyện Thoát Hoan chui vào ống đồng cho lính khiêng chạy về nước được kể rộng rãi trong "
                 "các bài viết phổ thông, nhưng chưa tìm thấy trong nguyên văn sử, và các nguồn không thống nhất năm (1285 hay "
                 "1288). Caption và bình luận ghim phải ghi \"tương truyền\".\n\n"
                 "**Hư cấu:** người lính Nguyên, bạn đồng ngũ, Anh Tư và mọi lời thoại. Tiếng cười nhắm vào tình huống trớ "
                 "trêu, không chế giễu người Mông Cổ hay bất kỳ dân tộc nào."),
        setting=("Northern Vietnam near the border, spring 1288, a steep jungle mountain road and a narrow pass, mist and "
                 "rain. Retreating Yuan soldiers in worn leather armor and fur-trimmed hats, tired and muddy, carrying a "
                 "long, heavy, sealed bronze tube on two wooden poles on their shoulders; the tube has small air holes and "
                 "ornate ends. The viewer is an ordinary Yuan foot soldier; his friend is a stocky, grumbling veteran around "
                 "40 with a round face. A stern Yuan officer on foot. Đại Việt soldiers appear only on distant cliffs. "
                 f"Prince Thoát Hoan is a proud young nobleman around 30 in ornate armor and a tall hat, appearing only at "
                 f"the end. Anh Tư is {ANH_TU}, with 'Sát Thát' tattooed on his forearm. {SAFE}"),
        hook="POV: Bị bắt khiêng / một cái ống đồng",
        end="Về nước, bố anh ấy đón thế nào? / Follow để xem tập sau →",
        clips=[
            dict(name="Ống đồng nặng trịch", label="Đường rút về phương Bắc / năm 1288",
                 img="First-person close-up of muddy hands gripping a wooden carrying pole on the shoulder, a long heavy sealed bronze tube with small air holes hanging below it, four tired Yuan soldiers carrying it on a steep misty jungle road, a stern officer walking beside, realistic, vertical 9:16.",
                 vid="0-5s: Close-up: muddy hands grip a carrying pole; four soldiers stagger up a steep jungle road under a long sealed bronze tube; the officer barks: \"Khiêng cẩn thận! Rơi là chém cả bọn!\" 5-10s: The viewer pants to the stocky veteran in front: \"Ống đồng gì mà nặng hơn cả con trâu thế này...\"",
                 subs=[(0.5, 4.8, "Khiêng cẩn thận! / Rơi là chém cả bọn!"),
                       (5.0, 9.5, "Ống đồng gì mà / nặng hơn cả con trâu thế này...")]),
            dict(name="Ống đồng biết nói", tiktok="bo", label="Nghỉ chân",
                 img="First-person view at a muddy rest stop on a jungle road, a long bronze tube resting on two rocks, a stocky soldier knocking on it curiously with his knuckles, both soldiers frozen with wide eyes, realistic, vertical 9:16.",
                 vid="0-5s: At a rest stop, the stocky veteran knocks on the bronze tube with his knuckles, curious. From inside, a muffled, furious voice: \"Đứa nào gõ đấy?!\" 5-10s: Both soldiers freeze; the veteran slowly pulls his hand back and whispers: \"...Ống đồng biết nói.\"",
                 subs=[(0.5, 4.8, "Đứa nào gõ đấy?!"),
                       (5.0, 9.5, "...Ống đồng biết nói.")]),
            dict(name="Ống đồng biết ra lệnh", label="Ải núi · bị phục kích",
                 img="First-person view on a narrow mountain pass, arrows flying from distant cliffs and hitting the rocks and mud around, Yuan soldiers scattering, the viewer about to set down a heavy bronze tube, no one hit, no blood, realistic, vertical 9:16.",
                 vid="0-5s: In a narrow pass, drums boom from the cliffs and arrows rain down, sticking into the mud and rocks around them; soldiers scatter, and the viewer starts to lower the bronze tube to run. From inside, the muffled voice roars: \"Không được bỏ! Khiêng chạy tiếp!\" 5-10s: The viewer stares at the tube, then at his friend: \"Ống đồng gì mà biết... ra lệnh?\" They hoist it and run.",
                 subs=[(0.5, 4.8, "Không được bỏ! / Khiêng chạy tiếp!"),
                       (5.0, 9.5, "Ống đồng gì mà biết... / ra lệnh?")]),
            dict(name="Con mắt trong lỗ thở", tiktok="bo", label="Qua suối",
                 img="First-person extreme close-up of a small air hole in a bronze tube, an eye under an ornate tall hat brim looking back out through the hole, the viewer's muddy fingers on the metal, realistic, vertical 9:16.",
                 vid="0-5s: Crossing a stream, the tube gets stuck on a rock; while pushing, the viewer leans close to a small air hole and peeks in. 5-10s: An eye under the brim of an ornate tall hat stares straight back at him; he jumps back and nearly falls into the water; the stocky veteran hisses: \"Đừng nhìn! Không thấy gì hết!\"",
                 subs=[(5.0, 9.5, "Đừng nhìn! Không thấy gì hết!")]),
            dict(name="Bên trong là ai", label="Ải biên giới",
                 img=f"First-person view at a border pass at dusk, the bronze tube set on the ground and opened, a proud young nobleman in dusty ornate armor and a tall hat climbing out and straightening his hat, exhausted soldiers staring, on a distant cliff {ANH_TU} waving, realistic, vertical 9:16.",
                 vid=f"0-5s: At the border pass the tube is set down and opened; a proud young nobleman in dusty ornate armor climbs out, straightens his tall hat and says coldly: \"Không ai được kể chuyện này.\" The soldiers stare; the viewer whispers: \"Khiêng cả tháng... hóa ra mình khiêng Thái tử.\" 5-10s: From a distant cliff, a Đại Việt soldier with a chipped front tooth ({ANH_TU}) cups his hands and shouts cheerfully: \"Về nhớ kể cho bố anh ấy nghe nhé!\"",
                 subs=[(0.3, 2.5, "Không ai được kể chuyện này."),
                       (2.6, 4.9, "Khiêng cả tháng... / hóa ra mình khiêng Thái tử."),
                       (5.0, 9.5, "Về nhớ kể cho bố anh ấy nghe nhé!")]),
        ],
        caption=("Bị bắt khiêng một cái ống đồng nặng trịch về nước, đến biên giới mới biết bên trong là ai 😂 Tương truyền "
                 "năm 1288, sau thất bại ở Bạch Đằng, Thoát Hoan phải chui vào ống đồng để chạy về nước. Còn sử nhà Nguyên "
                 "chép: Hốt Tất Liệt không muốn gặp lại con trai nữa. (Video dựng bằng AI, lời thoại là hư cấu.)"),
        tags="#thoathoan #bachdang #1288 #phiabenkia",
    ),
]

if __name__ == "__main__":
    build(EPISODES, os.path.dirname(os.path.abspath(__file__)), series_tag="#anhtu", note=NOTE,
          unit="Tập", file_unit="tap")
