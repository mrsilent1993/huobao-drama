#!/usr/bin/env python3
"""Tiền giấy đầu tiên 1396 (Thông bảo hội sao): 3 mẫu, mỗi mẫu một kiểu kể. Chuẩn 7 clip, YouTube 60–70s, TikTok 30–35s.
Kênh đã có tập "Bạn đi chợ bằng tiền giấy năm 1396" (chuyen-la-dai-viet tập 1): KHÔNG lặp các câu đùa cũ
(bà bán cá chê tờ con rùa, phơi tiền, giấu hũ đồng "Suỵt"). Chạy: python3 _nguon.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from series import build, MUC_MOI  # noqa: E402
from _nguon import FACE, END, LEN7, NOTE  # noqa: E402

HIST = ("**Lịch sử:** tháng 4 năm Bính Tý (1396), dưới quyền Hồ Quý Ly (khi ấy là quyền thần nhà Trần), triều đình phát "
        "hành tiền giấy **Thông bảo hội sao** và bắt dân đổi tiền đồng lấy tiền giấy, **1 quan tiền đồng đổi được 1 quan 2 "
        "tiền giấy** (*Đại Việt sử ký toàn thư*, mức B). Mỗi mệnh giá vẽ một hình riêng; theo các nguồn hiện có, tờ 1 quan "
        "vẽ **rồng**, tờ 2 tiền vẽ rùa, tờ 5 tiền vẽ phượng. Người làm tiền giả bị trị tội rất nặng. Đây là một trong những lần "
        "phát hành tiền giấy sớm nhất ở Đông Nam Á, nhưng dân không tin, vẫn chuộng tiền đồng, và chính sách không duy trì "
        "được lâu. **Hư cấu:** Anh Tư, vợ Anh Tư, mọi nhân vật ở chợ và mọi lời thoại.")
SET = ("Thăng Long, spring 1396, late Trần dynasty: a busy riverside market with thatched stalls, baskets of rice, fish, "
       "betel, chickens; a government exchange office with officials in dark robes behind low tables, heavy strings of "
       "copper coins with square holes. Paper money = sheets of grayish handmade paper with a painted picture (a dragon, a "
       "turtle, a phoenix or clouds) and a red seal; any characters on them are blurred and unreadable. Common people with "
       "short cropped hair or topknots, black-lacquered teeth, brown and indigo clothes. Hồ Quý Ly never appears. Adults "
       f"only, no children. Anh Tư is {FACE}. No flags, no legible writing anywhere, no modern objects, no blood.")
VIS = ("**Chuẩn hình ảnh:** chợ Thăng Long cuối Trần; tiền đồng lỗ vuông xâu thành chuỗi; tiền giấy là tờ giấy dó xám có "
       "vẽ hình (rồng, rùa, phượng, mây) và dấu son, chữ trên tờ tiền làm mờ. Không cờ, không chữ đọc được, không trẻ em.")
COMMON = dict(length=LEN7, muc=MUC_MOI, history=HIST, setting=SET, visual=VIS, end=END, end_secs=1.6,
              tags="#tuhaodaiviet #tiengiay #hoquyly #thongbaohoisao #1396")
YT_TAGS = ("tiền giấy đầu tiên việt nam, thông bảo hội sao, hồ quý ly, 1396, lịch sử tiền tệ, nhà hồ, tự hào đại việt, "
           "lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts")

EPISODES = [
    # ================================================================== Mẫu A: Không hỏi (người vẽ rồng)
    dict(COMMON,
        slug="tien-giay-ve-rong", prefix="th1396a",
        voices={"official": "a short, stern male voice", "teahouse woman": "a sharp, quick-witted middle-aged woman's voice"},
        title="Mẫu A · Không hỏi: bị sai vẽ rồng lên giấy cả đêm, sáng ra mới biết mình vừa vẽ ra… tiền (tiền giấy 1396)",
        hook="POV: Vẽ rồng / cả đêm / mà không biết để làm gì",
        clips=[
            dict(name="Vẽ rồng", tiktok="0-5", label="Thăng Long · 1396",
                 img=f"First-person view at night in a lamplit workshop, a stern official dropping a tall stack of blank grayish paper sheets on a low table, a brush and a bowl of ink, {FACE} sitting before it, confused, realistic, vertical 9:16.",
                 vid=("0-5s: The official drops a tall stack of paper: \"Vẽ rồng. Mỗi tờ một con.\" Anh Tư: \"Vẽ rồng... để "
                      "làm gì ạ?\" The official: \"Không hỏi.\" 5-10s: Anh Tư stares at the stack and whispers: \"Cả chồng "
                      "này... là cả đêm nay.\""),
                 subs=[(0.3, 2.4, "Vẽ rồng. / Mỗi tờ một con."),
                       (2.4, 3.8, "Vẽ rồng... / để làm gì ạ?"),
                       (3.8, 4.9, "Không hỏi."),
                       (5.2, 9.5, "Cả chồng này... / là cả đêm nay.")]),
            dict(name="Con giun", tiktok="5-10", label="",
                 img=f"Close view of a sheet of grayish paper with a clumsy, wiggly painted dragon that looks like an earthworm, {FACE} holding the brush and grinning sheepishly, the official frowning, realistic, vertical 9:16.",
                 vid=("0-5s: The official holds up Anh Tư's clumsy dragon that looks like an earthworm and frowns. 5-10s: Anh "
                      "Tư whispers to the viewer: \"Rồng em vẽ... giống con giun hơn con rồng.\""),
                 subs=[(5.0, 9.5, "Rồng em vẽ... / giống con giun / hơn con rồng.")]),
            dict(name="Một quan", tiktok="5-10", label="",
                 img=f"First-person view at dawn as the official stamps a red seal on Anh Tư's dragon sheet and adds it to a neat stack, {FACE} staring with wide eyes, realistic, vertical 9:16.",
                 vid=("0-5s: At dawn the official stamps a red seal on the dragon sheet: \"Tờ này... đáng một quan.\" 5-10s: Anh "
                      "Tư, stunned, to the viewer: \"Em vẽ con giun một khắc... mà đáng một quan?\""),
                 subs=[(0.5, 4.8, "Tờ này... / đáng một quan."),
                       (5.0, 9.5, "Em vẽ con giun một khắc... / mà đáng một quan?")]),
            dict(name="Được lãi", tiktok="5-10", label="Nơi đổi tiền",
                 img=f"First-person view at a government exchange table, {FACE} handing over a heavy string of copper coins and receiving a dragon paper note plus a smaller paper note, a long line of people behind, realistic, vertical 9:16.",
                 vid=("0-5s: At the exchange table Anh Tư hands over a heavy string of copper coins; the clerk gives back a dragon "
                      "note plus an extra small note: \"Một quan đồng, đổi một quan hai tiền giấy.\" 5-10s: Anh Tư narrows his "
                      "eyes at the viewer: \"Đổi tiền mà còn được lãi... thì chắc chắn có vấn đề.\""),
                 subs=[(0.5, 4.8, "Một quan đồng, / đổi một quan hai tiền giấy."),
                       (5.0, 9.5, "Đổi tiền mà còn được lãi... / thì chắc chắn có vấn đề.")]),
            dict(name="Quán nước", tiktok="5-10", label="",
                 img=f"First-person view at a roadside tea stall, a sharp-tongued middle-aged woman holding Anh Tư's dragon note up to the light and squinting, {FACE} waiting hopefully, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư pays for tea with the dragon note. The tea woman holds it up to the light: \"Con rồng này "
                      "ai vẽ mà xấu thế?\" 5-10s: Anh Tư smiles weakly at the viewer: \"Em không dám nhận... em vẽ.\""),
                 subs=[(0.5, 4.8, "Con rồng này / ai vẽ mà xấu thế?"),
                       (5.0, 9.5, "Em không dám nhận... / em vẽ.")]),
            dict(name="Vẫn đòi đồng", tiktok="5-10", label="",
                 img=f"First-person view of the tea woman pushing the paper note back and tapping a single copper coin on the table, {FACE} digging in his pocket, realistic, vertical 9:16.",
                 vid=("0-5s: The tea woman pushes the note back and taps the table: \"Bát nước thôi. Trả đồng đi.\" 5-10s: Anh "
                      "Tư digs out his last copper coin and sighs to the viewer: \"Em vẽ rồng cả đêm... cô ấy vẫn tin cái đồng "
                      "xu.\""),
                 subs=[(0.5, 4.8, "Bát nước thôi. / Trả đồng đi."),
                       (5.0, 9.5, "Em vẽ rồng cả đêm... / cô ấy vẫn tin / cái đồng xu.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view at sunset on the riverbank, {FACE} folding his dragon note into a little paper boat and setting it on the water, realistic, vertical 9:16.",
                 vid=("0-4.5s: At sunset Anh Tư folds his dragon note into a little paper boat. A calm narrator's voice says: "
                      "\"Năm 1396, Đại Việt phát hành tiền giấy, một trong những lần sớm nhất ở Đông Nam Á.\" 4.5-10s: He sets the "
                      "boat on the river and says to the camera: \"Tiền thì chưa ai tin... nhưng con giun của em vào sử rồi.\""),
                 subs=[(3.0, 6.0, "Năm 1396, Đại Việt / phát hành tiền giấy. / Sớm nhất nhì Đông Nam Á."),
                       (6.1, 8.4, "Tiền chưa ai tin... / nhưng con giun của em / vào sử rồi.")]),
        ],
        caption=("Bị sai vẽ rồng lên giấy cả đêm, sáng ra mới biết mình vừa vẽ ra tiền 😳 Năm 1396, Đại Việt phát hành tiền giấy "
                 "Thông bảo hội sao, đổi 1 quan tiền đồng được 1 quan 2 tiền giấy. Được lãi mà dân vẫn không tin. Nếu là bạn, "
                 "bạn có đổi không? 👇"),
        tt_title="Vẽ rồng lên giấy cả đêm, sáng ra mới biết mình vừa vẽ ra tiền",
        hooks_alt=["POV: Đổi tiền / mà còn được lãi", "POV: Rồng em vẽ / giống con giun"],
        pin=("Đổi tiền mà còn được lãi… thì chắc chắn có vấn đề 😂 Bạn có biết vì sao dân năm 1396 không tin tiền giấy không? "
             "Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1396: vẽ rồng cả đêm, sáng ra thành tiền giấy | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
    # ================================================================== Mẫu B: Một tờ tiền đi một vòng chợ
    dict(COMMON,
        slug="tien-giay-mot-vong-cho", prefix="th1396b",
        voices={"official": "a short, stern male voice", "barber": "a chatty, cheerful old male voice",
                "ferryman": "a gruff, lazy male voice", "betel woman": "a sharp, quick-witted middle-aged woman's voice"},
        title="Mẫu B · Một vòng chợ: được trả công bằng một tờ tiền giấy, đi cả ngày không tiêu được (tiền giấy 1396)",
        hook="POV: Cầm tờ tiền / mới nhất nước / đi tiêu",
        clips=[
            dict(name="Sáng: lĩnh công", tiktok="0-5", label="Sáng · chợ Thăng Long, 1396",
                 img=f"First-person view at a market gate in the morning, a stern official handing {FACE} a single grayish paper note with a painted dragon and a red seal instead of coins, Anh Tư holding it up, puzzled, realistic, vertical 9:16.",
                 vid=("0-5s: The official hands Anh Tư a single paper note with a dragon: \"Công cả tháng. Một quan.\" Anh Tư: "
                      "\"Tiền... bằng giấy ạ?\" The official: \"Không hỏi.\" 5-10s: Anh Tư flaps the light note and whispers: "
                      "\"Cả tháng làm... nhẹ hơn cái lá.\""),
                 subs=[(0.3, 2.4, "Công cả tháng. / Một quan."),
                       (2.4, 3.8, "Tiền... bằng giấy ạ?"),
                       (3.8, 4.9, "Không hỏi."),
                       (5.2, 9.5, "Cả tháng làm... / nhẹ hơn cái lá.")]),
            dict(name="Cắt tóc", tiktok="5-10", label="Gần trưa",
                 img=f"First-person view at a roadside barber under a tree, a chatty old barber with a razor stopping halfway through cutting {FACE}'s hair to stare at the paper note, realistic, vertical 9:16.",
                 vid=("0-5s: Halfway through the haircut Anh Tư offers the dragon note. The old barber stops, razor in the air: "
                      "\"Tiền giấy à? Thế tôi cắt nửa đầu thôi.\" 5-10s: Anh Tư, with half a haircut, to the viewer: \"Tờ tiền "
                      "mới nhất nước... đổi được nửa cái đầu.\""),
                 subs=[(0.5, 4.8, "Tiền giấy à? / Thế tôi cắt nửa đầu thôi."),
                       (5.0, 9.5, "Tờ tiền mới nhất nước... / đổi được nửa cái đầu.")]),
            dict(name="Đò ngang", tiktok="5-10", label="Trưa",
                 img=f"First-person view at a river ferry landing, a gruff ferryman leaning on his pole and shaking his head at the paper note, {FACE} with an uneven half haircut, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư offers the note to the ferryman. The ferryman: \"Giấy rơi xuống sông thì ai đền?\" 5-10s: Anh "
                      "Tư rolls up his trousers to wade across and mutters: \"Đi đò không được... thì lội.\""),
                 subs=[(0.5, 4.8, "Giấy rơi xuống sông / thì ai đền?"),
                       (5.0, 9.5, "Đi đò không được... / thì lội.")]),
            dict(name="Hàng trầu", tiktok="5-10", label="Chiều",
                 img=f"First-person view at a betel stall, a sharp-tongued woman holding the dragon note next to a single copper coin as if weighing them, {FACE} soaking wet from the waist down, realistic, vertical 9:16.",
                 vid=("0-5s: The betel woman weighs the note in one hand and a copper coin in the other: \"Con rồng này nhẹ hơn "
                      "đồng xu đấy anh.\" 5-10s: Anh Tư, wet to the waist, to the viewer: \"Một quan giấy... không nặng bằng "
                      "một xu đồng.\""),
                 subs=[(0.5, 4.8, "Con rồng này / nhẹ hơn đồng xu đấy anh."),
                       (5.0, 9.5, "Một quan giấy... / không nặng bằng một xu đồng.")]),
            dict(name="Một vòng chợ", tiktok="5-10", label="Tối",
                 img=f"First-person view at dusk as a stall keeper hands the very same dragon note back to {FACE} as change after buying a bowl of rice soup with it, Anh Tư staring at it in disbelief, realistic, vertical 9:16.",
                 vid=("0-5s: At dusk a soup seller finally accepts the note, then rummages and hands back change... the very same "
                      "dragon note, plus a bowl of rice soup. 5-10s: Anh Tư stares at it and tells the viewer: \"Một tờ tiền... "
                      "đi một vòng cả chợ, lại về túi em.\""),
                 subs=[(0.5, 4.8, "Đây, tiền thừa của anh."),
                       (5.0, 9.5, "Một tờ tiền... / đi một vòng cả chợ, / lại về túi em.")]),
            dict(name="Đêm", tiktok="5-10", label="Đêm",
                 img=f"First-person view at night on a bamboo bed, {FACE} lying down holding the dragon note above his face by lamplight, realistic, vertical 9:16.",
                 vid=("0-5s: Night; Anh Tư lies on a bamboo bed, holding the note above his face by lamplight. 5-10s: He says "
                      "softly: \"Xấu thì xấu... nhưng con rồng này là của nước mình in ra.\""),
                 subs=[(5.0, 9.5, "Xấu thì xấu... / nhưng con rồng này / là nước mình in ra.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view on a hot afternoon, {FACE} sitting in front of his house fanning himself with the dragon paper note, smiling contentedly, realistic, vertical 9:16.",
                 vid=("0-4.5s: A calm narrator's voice says: \"Năm 1396, Đại Việt phát hành tiền giấy, một trong những lần sớm "
                      "nhất ở Đông Nam Á. Dân chưa quen, vẫn chuộng tiền đồng.\" 4.5-10s: Anh Tư fans himself with the note "
                      "and grins at the camera: \"Không mua được gì... nhưng quạt thì mát.\""),
                 subs=[(3.0, 6.0, "Năm 1396, Đại Việt / phát hành tiền giấy. / Sớm nhất nhì Đông Nam Á."),
                       (6.1, 8.4, "Không mua được gì... / nhưng quạt thì mát.")]),
        ],
        caption=("Được trả công cả tháng bằng một tờ tiền giấy, đi cả ngày không tiêu được 😂 Năm 1396, Đại Việt phát hành tiền "
                 "giấy Thông bảo hội sao, một trong những lần sớm nhất ở Đông Nam Á. Bạn sẽ tiêu tờ tiền này vào đâu? 👇"),
        tt_title="Được trả công bằng tiền giấy năm 1396, đi cả ngày không tiêu được",
        hooks_alt=["POV: Một tờ tiền / đi một vòng chợ / lại về túi em", "POV: Tờ tiền mới nhất nước / đổi được nửa cái đầu"],
        pin=("Tờ 1 quan vẽ rồng, tờ 2 tiền vẽ rùa, tờ 5 tiền vẽ phượng 🐉 Bạn đoán tờ 3 tiền vẽ con gì? Follow để xem Tự hào "
             "Đại Việt tập tiếp theo!"),
        yt_title="Năm 1396: một tờ tiền giấy đi một vòng chợ Thăng Long | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
    # ================================================================== Mẫu C: Hai vợ chồng (cặp đôi hài)
    dict(COMMON,
        slug="tien-giay-vo-chong", prefix="th1396c",
        voices={"Chị Tư": "a sharp, practical, quick-witted woman's voice around 30, Northern accent",
                "official": "a short, stern male voice"},
        title="Mẫu C · Vợ chồng Anh Tư: chồng mang cả xấp tiền giấy về khoe lãi, vợ chỉ hỏi một câu (tiền giấy 1396)",
        hook="POV: Mang tiền giấy / về khoe vợ",
        setting=SET + (" Chị Tư (Anh Tư's wife) is a sharp, practical Vietnamese woman around 30 with black-lacquered teeth, "
                       "hair wrapped in a brown headscarf, in an indigo blouse, hands on hips."),
        clips=[
            dict(name="Đổi tiền", tiktok="0-5", label="Thăng Long · 1396",
                 img=f"First-person view at a government exchange table, a stern official pushing a stack of grayish paper notes with painted dragons toward {FACE} and pulling away his heavy strings of copper coins, realistic, vertical 9:16.",
                 vid=("0-5s: The official takes Anh Tư's copper strings and pushes a stack of paper notes back: \"Đổi hết. Đồng "
                      "nộp lại.\" Anh Tư: \"Hết ạ? Cả tiền vợ em?\" The official: \"Không hỏi.\" 5-10s: Anh Tư hugs the paper "
                      "stack, grinning: \"Mà lại còn được lãi!\""),
                 subs=[(0.3, 2.4, "Đổi hết. / Đồng nộp lại."),
                       (2.4, 3.8, "Hết ạ? / Cả tiền vợ em?"),
                       (3.8, 4.9, "Không hỏi."),
                       (5.2, 9.5, "Mà lại còn được lãi!")]),
            dict(name="Khoe vợ", tiktok="5-10", label="",
                 img=f"First-person view in a thatched house, {FACE} proudly fanning out a stack of dragon paper notes in front of his wife Chị Tư, who stands with hands on hips, unimpressed, realistic, vertical 9:16.",
                 vid=("0-5s: At home Anh Tư fans out the notes proudly: \"Mình ơi, một quan đồng đổi được một quan hai!\" 5-10s: "
                      "Chị Tư, hands on hips, not impressed: \"Thế mua được con gà không?\""),
                 subs=[(0.5, 4.8, "Mình ơi, một quan đồng / đổi được một quan hai!"),
                       (5.0, 9.5, "Thế mua được / con gà không?")]),
            dict(name="Trời mưa", tiktok="5-10", label="",
                 img=f"First-person view as sudden rain pours through a leaky thatched roof, {FACE} desperately covering the paper notes with his body, Chị Tư calmly holding a clay jar under her arm, dry, realistic, vertical 9:16.",
                 vid=("0-5s: Sudden rain leaks through the roof; Anh Tư throws himself over the paper notes. Chị Tư calmly hugs a "
                      "clay jar, dry. 5-10s: Chị Tư: \"Tiền gì mà sợ nước... như mèo.\""),
                 subs=[(0.5, 4.8, "Ối! Ối! Tiền của tôi!"),
                       (5.0, 9.5, "Tiền gì mà sợ nước... / như mèo.")]),
            dict(name="Đi chợ", tiktok="5-10", label="",
                 img=f"First-person view at the market as Chị Tư pays a chicken seller instantly with a copper coin from her headscarf, while {FACE} behind her is still arguing with another seller over a paper note, realistic, vertical 9:16.",
                 vid=("0-5s: At the market Chị Tư pulls a copper coin from her headscarf and walks off with a chicken in seconds. "
                      "Behind her Anh Tư is still arguing with a seller over his paper note. 5-10s: Anh Tư to the viewer: "
                      "\"Vợ em đi chợ năm giây... em mặc cả nửa buổi.\""),
                 subs=[(5.0, 9.5, "Vợ em đi chợ năm giây... / em mặc cả nửa buổi.")]),
            dict(name="Hũ của vợ", tiktok="5-10", label="",
                 img=f"First-person view at night, Chị Tư lifting a loose floor brick by the hearth to reveal a small clay jar of copper coins, {FACE} staring with his mouth open, realistic, vertical 9:16.",
                 vid=("0-5s: At night Chị Tư lifts a brick by the hearth and shows a small jar of copper coins: \"Để dành. Phòng "
                      "khi tiền của mình... bay mất.\" 5-10s: Anh Tư, stunned, to the viewer: \"Cả nước đổi tiền... trừ vợ em.\""),
                 subs=[(0.5, 4.8, "Để dành. / Phòng khi tiền của mình... / bay mất."),
                       (5.0, 9.5, "Cả nước đổi tiền... / trừ vợ em.")]),
            dict(name="Làm hòa", tiktok="5-10", label="",
                 img=f"First-person view by the hearth, {FACE} sheepishly handing his wife a dragon paper note, Chị Tư folding it into a neat paper fan and smiling for the first time, realistic, vertical 9:16.",
                 vid=("0-5s: Anh Tư sheepishly hands his wife a dragon note. She folds it neatly into a little paper fan and fans "
                      "herself, smiling. 5-10s: Anh Tư, relieved, to the viewer: \"Tiền giấy cũng có lúc dùng được... dỗ vợ.\""),
                 subs=[(5.0, 9.5, "Tiền giấy cũng có lúc / dùng được... dỗ vợ.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view in the morning at the doorway, Chị Tư holding the clay jar of copper coins and {FACE} holding the stack of paper notes, both looking at the camera, realistic, vertical 9:16.",
                 vid=("0-4.5s: A calm narrator's voice says: \"Năm 1396, Đại Việt phát hành tiền giấy, một trong những lần sớm "
                      "nhất ở Đông Nam Á. Nhưng dân vẫn chuộng tiền đồng.\" 4.5-10s: Chị Tư hugs her jar and says to the "
                      "camera: \"Tiền giấy thì chồng giữ. Hũ đồng thì vợ giữ.\""),
                 subs=[(3.0, 6.0, "Năm 1396, Đại Việt / phát hành tiền giấy. / Sớm nhất nhì Đông Nam Á."),
                       (6.1, 8.4, "Tiền giấy thì chồng giữ. / Hũ đồng thì vợ giữ.")]),
        ],
        caption=("Chồng mang cả xấp tiền giấy về khoe được lãi, vợ chỉ hỏi đúng một câu: \"Thế mua được con gà không?\" 😂 Năm "
                 "1396, Đại Việt phát hành tiền giấy Thông bảo hội sao. Nhà bạn ai giữ tiền? 👇"),
        tt_title="Mang tiền giấy năm 1396 về khoe vợ, vợ hỏi đúng một câu",
        hooks_alt=["POV: Cả nước đổi tiền / trừ vợ em", "POV: Tiền gì / mà sợ nước như mèo"],
        pin=("Năm 1396 cứ 1 quan tiền đồng đổi được 1 quan 2 tiền giấy, được lãi mà dân vẫn không đổi 🤔 Nếu là vợ bạn thì "
             "sao? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1396: mang tiền giấy về khoe vợ | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#tuhaodaiviet #anhtu", note=NOTE, unit="Mẫu", file_unit="mau")
