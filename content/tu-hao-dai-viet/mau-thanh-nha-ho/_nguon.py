#!/usr/bin/env python3
"""Thành nhà Hồ 1397: 3 mẫu kịch bản, mỗi mẫu một kiểu kể. Chuẩn mới: 7 clip, YouTube 60–70 giây, TikTok 30–35 giây.
Chạy: python3 _nguon.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from series import build, MUC_MOI  # noqa: E402
from _nguon import FACE, NO_TEXT, END, LEN7, NOTE  # noqa: E402

HIST = ("**Lịch sử:** tháng Giêng năm 1397, Hồ Quý Ly (khi ấy còn là quyền thần nhà Trần, năm 1400 mới lên ngôi) sai "
        "Thượng thư Đỗ Tỉnh đi xem đất ở động An Tôn (Thanh Hóa) để xây kinh đô mới, gọi là Tây Đô. Thành xây xong trong "
        "khoảng **3 tháng** (*Đại Việt sử ký toàn thư*, mức B). Tường và cổng xây bằng những phiến đá vôi xanh, dài trung "
        "bình 1,5 m, có phiến dài tới khoảng 6 m, nặng phổ biến 10–20 tấn, **xếp khít lên nhau không dùng vữa**; đá lấy ở "
        "núi An Tôn cách thành khoảng 2 km. Năm 2011, UNESCO công nhận thành là di sản văn hóa thế giới. Hơn 600 năm sau, "
        "các cổng thành vẫn đứng (một vài đoạn tường đã sạt lở). **Chưa rõ:** người xưa đưa đá về và nâng đá lên bằng "
        "cách nào; cảnh lăn đá, trượt đá trên đường đất ướt chỉ là giả thuyết. **Hư cấu:** Anh Tư, ông thợ cả, phép thử "
        "khe đá bằng sợi tóc và mọi lời thoại.")
SET = ("Đại Việt, early 1397: a vast stone-building site in a green valley below limestone mountains in Thanh Hóa. Huge "
       "rectangular blue-grey limestone blocks (1.5 to 6 meters long, each as big as a bed or bigger) stacked tightly with "
       "NO mortar; earth ramps, wooden rollers, thick ropes, bamboo scaffolding, a half-built arched stone gate. Hundreds of "
       "late-Trần Vietnamese laborers with hair in topknots or cloth turbans, black-lacquered teeth, bare-chested in brown "
       "short trousers, sweating, working in teams; officials in dark robes. Hồ Quý Ly never appears. Adults only, no "
       f"children. Anh Tư is {FACE}, a laborer with a rope over his shoulder. {NO_TEXT}")
NOW = ("the very same arched stone gate today: weathered, mossy, huge blue-grey blocks still tight, green rice fields around, "
       "soft sunrise, no people, no signs, no modern objects")
VIS = ("**Chuẩn hình ảnh:** đá vôi xanh xám, phiến to bằng cái giường, xếp khít không vữa; cổng vòm đá; người làm búi tóc "
       "hoặc quấn khăn, răng đen, cởi trần, quần nâu. Không cờ, không chữ, không trẻ em. Cảnh hôm nay: chỉ cổng đá, ruộng "
       "lúa, không người, không biển hiệu.")
COMMON = dict(length=LEN7, muc=MUC_MOI, history=HIST, setting=SET, visual=VIS, end=END, end_secs=1.6,
              tags="#tuhaodaiviet #thanhnhaho #hoquyly #disanthegioi #1397")
YT_TAGS = ("thành nhà hồ, tây đô, hồ quý ly, 1397, thành đá, di sản thế giới, thanh hóa, xây thành không vữa, tự hào đại "
           "việt, lịch sử việt nam, pov lịch sử, anh tư, đại việt, shorts")

EPISODES = [
    # ================================================================== Mẫu A: Đá không vữa (công thức cổ điển)
    dict(COMMON,
        slug="thanh-nha-ho-khong-hoi", prefix="th1397a",
        voices={"official": "a short, stern male voice", "old mason": "a slow, gravelly old male voice, dry humor",
                "coworker": "a cheeky young adult male voice"},
        title="Mẫu A · Đá không vữa: bị sai khiêng đá to bằng cái giường, xếp thành tường mà không có vữa (Thành nhà Hồ, 1397)",
        hook="POV: Xây thành / không cần vữa / trong 3 tháng",
        clips=[
            dict(name="Lệnh", tiktok="0-5", label="An Tôn, Thanh Hóa · 1397",
                 img=f"First-person view at a vast stone-building site, a stern official pointing at a huge blue-grey limestone block as big as a bed, {FACE} beside the viewer holding a rope, jaw dropped, realistic, vertical 9:16.",
                 vid=("0-5s: The official points at a huge stone block: \"Khiêng đá. Xếp thành tường.\" Anh Tư: \"Vữa đâu ạ?\" "
                      "The official: \"Có vữa thì đã chẳng cần mày.\" 5-10s: Anh Tư walks around the block, measuring it with his arms, and "
                      "whispers: \"Hòn này... to bằng cái giường nhà em.\""),
                 subs=[(0.3, 2.4, "Khiêng đá. / Xếp thành tường."),
                       (2.4, 3.4, "Vữa đâu ạ?"),
                       (3.4, 4.9, "Có vữa / thì đã chẳng cần mày."),
                       (5.2, 9.5, "Hòn này... / to bằng cái giường nhà em.")]),
            dict(name="Hai mươi người", tiktok="5-10", label="",
                 img=f"First-person view as twenty bare-chested laborers strain on thick ropes around one giant stone block on wooden rollers, {FACE} pulling in the front, face red, realistic, vertical 9:16.",
                 vid=("0-5s: Twenty laborers heave on thick ropes; \"Dô ta!\"; the giant block on wooden rollers does not move. "
                      "5-10s: Anh Tư, gasping, whispers to the viewer: \"Hai mươi người khiêng một hòn... đá vẫn nằm im.\""),
                 subs=[(0.5, 4.8, "Dô ta! Dô ta!"),
                       (5.0, 9.5, "Hai mươi người / khiêng một hòn đá... / đá vẫn nằm im.")]),
            dict(name="Không lọt cọng cỏ", tiktok="5-10", label="",
                 img=f"Close first-person view of two huge stone blocks set tightly together with no mortar, {FACE}'s hand trying to push a blade of grass into the joint, it bends and will not go in, realistic, vertical 9:16.",
                 vid=("0-5s: The block is lowered onto the wall with a heavy thud; it sits perfectly tight. Anh Tư tries to push "
                      "a blade of grass into the joint; it bends. 5-10s: Anh Tư whispers, amazed: \"Không vữa... mà cọng cỏ "
                      "cũng không lọt.\""),
                 subs=[(0.5, 4.8, "Rầm!"),
                       (5.0, 9.5, "Không vữa... / mà cọng cỏ cũng không lọt.")]),
            dict(name="Ba tháng", tiktok="5-10", label="",
                 img=f"First-person view at the half-built wall, the stern official holding up three fingers, {FACE} staring at the endless wall line, horrified, realistic, vertical 9:16.",
                 vid=("0-5s: The official holds up three fingers: \"Ba tháng. Phải xong cả tòa thành.\" 5-10s: Anh Tư turns to "
                      "the viewer: \"Nhà em xây cái chuồng lợn... còn mất nửa năm.\""),
                 subs=[(0.5, 4.8, "Ba tháng. / Phải xong cả tòa thành."),
                       (5.0, 9.5, "Nhà em xây cái chuồng lợn... / còn mất nửa năm.")]),
            dict(name="Đứng dưới vòm", tiktok="5-10", label="",
                 img=f"First-person view from under a freshly finished stone arch gate with no mortar, an old mason calmly telling {FACE} to stand right under the arch, Anh Tư looking up nervously, realistic, vertical 9:16.",
                 vid=("0-5s: Under the new stone arch, the old mason tells Anh Tư: \"Đứng yên. Đá tự giữ nhau.\" Anh Tư looks "
                      "up at the tons of stone. 5-10s: Anh Tư whispers: \"Không vữa... mà em vẫn phải đứng dưới?\""),
                 subs=[(0.5, 4.8, "Đứng yên. / Đá tự giữ nhau."),
                       (5.0, 9.5, "Không vữa... / mà em vẫn phải đứng dưới?")]),
            dict(name="Vì sao gấp", tiktok="5-10", label="",
                 img=f"First-person view at dusk on top of the stone wall, the old mason looking north toward the mountains, {FACE} sitting beside him eating a rice ball, realistic, vertical 9:16.",
                 vid=("0-5s: Dusk on the wall. Anh Tư asks: \"Xây gì mà gấp thế ông?\" The old mason looks north: \"Kinh đô "
                      "mới. Phương Bắc đang nhìn sang.\" 5-10s: Anh Tư stops chewing and nods slowly: \"Thảo nào... ba tháng.\""),
                 subs=[(0.5, 2.2, "Xây gì mà gấp thế ông?"),
                       (2.2, 4.8, "Kinh đô mới. / Phương Bắc đang nhìn sang."),
                       (5.0, 9.5, "Thảo nào... ba tháng.")]),
            dict(name="Câu chốt", tiktok="3-10", label="", chuyen="fade:0.4",
                 img=f"First-person view at the finished arched stone gate at sunrise, {FACE} dusting his hands and patting the wall proudly, a coworker beside him, realistic, vertical 9:16.",
                 vid=("0-4.5s: At the finished gate, the coworker asks: \"Xây vội thế, được mấy năm?\" Anh Tư pats the stone: "
                      "\"Ba tháng xây xong... sáu trăm năm chưa đổ.\" 4.5-10s: The image slowly ages into " + NOW + ". A calm "
                      "narrator's voice says: \"Hơn 600 năm sau, cổng thành vẫn đứng.\""),
                 subs=[(3.0, 4.4, "Xây vội thế, / được mấy năm?"),
                       (4.5, 6.6, "Ba tháng xây xong... / sáu trăm năm chưa đổ."),
                       (6.7, 8.4, "Hơn 600 năm sau, / cổng thành vẫn đứng.")]),
        ],
        caption=("Bị sai khiêng đá to bằng cái giường, xếp thành tường mà không có vữa 😳 Năm 1397, thành nhà Hồ xây xong trong "
                 "khoảng 3 tháng, đá nặng hàng chục tấn xếp khít không cần chất kết dính. Hơn 600 năm sau, cổng thành vẫn đứng. "
                 "Bạn đã đến thành nhà Hồ chưa? 👇"),
        tt_title="Khiêng đá to bằng cái giường, xây thành không vữa trong 3 tháng",
        hooks_alt=["POV: Hai mươi người / khiêng một hòn đá", "POV: Xây thành / mà không ai đưa vữa"],
        pin=("Đến giờ vẫn chưa ai biết chắc người xưa đưa những phiến đá hàng chục tấn lên bằng cách nào 🤔 Bạn đoán thử xem? "
             "Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Năm 1397: xây thành nhà Hồ không vữa trong 3 tháng | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
    # ================================================================== Mẫu B: Nhật ký 90 ngày (đếm mốc)
    dict(COMMON,
        slug="thanh-nha-ho-nhat-ky-90-ngay", prefix="th1397b",
        voices={"official": "a short, stern male voice", "old mason": "a slow, gravelly old male voice, dry humor"},
        title="Mẫu B · Nhật ký 90 ngày: đếm từng ngày xây một tòa thành đá (Thành nhà Hồ, 1397)",
        hook="POV: Nhật ký / 90 ngày / xây thành đá",
        clips=[
            dict(name="Ngày 1", tiktok="0-5", label="Ngày 1 · An Tôn, 1397",
                 img=f"First-person view at dawn on an empty field below limestone mountains, a stern official pointing at rows of huge stone blocks, {FACE} holding a rope, stunned, realistic, vertical 9:16.",
                 vid=("0-5s: Dawn on an empty field. The official: \"Chín mươi ngày. Xong cả tòa thành.\" Anh Tư: \"Chín "
                      "mươi... ngày ạ?\" The official: \"Giờ còn tám chín ngày rưỡi.\" 5-10s: Anh Tư looks at the empty field, then at the "
                      "camera: \"Ngày một. Cánh đồng này... chưa có gì.\""),
                 subs=[(0.3, 2.4, "Chín mươi ngày. / Xong cả tòa thành."),
                       (2.4, 3.4, "Chín mươi... ngày ạ?"),
                       (3.4, 4.9, "Giờ còn / tám chín ngày rưỡi."),
                       (5.2, 9.5, "Ngày một. / Cánh đồng này... chưa có gì.")]),
            dict(name="Ngày 5", tiktok="5-10", label="Ngày 5",
                 img=f"First-person view at a lunch break, {FACE} sitting on a huge stone block, rubbing his bruised shoulder and eating a rice ball, exhausted laborers around, realistic, vertical 9:16.",
                 vid=("0-5s: Lunch break; Anh Tư sits on a stone block rubbing a big bruise on his shoulder. 5-10s: He says to "
                      "the camera, deadpan: \"Ngày năm. Vai em giờ... cũng cứng như đá.\""),
                 subs=[(5.0, 9.5, "Ngày năm. / Vai em giờ... / cũng cứng như đá.")]),
            dict(name="Ngày 20", tiktok="5-10", label="Ngày 20",
                 img=f"First-person view as laborers pour buckets of water on a path of wet clay and a giant stone block on a wooden sledge slides forward, {FACE} pulling a rope and grinning, realistic, vertical 9:16.",
                 vid=("0-5s: Laborers pour water on a wet clay path; a giant block on a wooden sledge suddenly slides forward "
                      "and everyone stumbles. 5-10s: Anh Tư grins at the camera: \"Ngày hai mươi. Đá nặng thì... cho nó trượt.\""),
                 subs=[(0.5, 4.8, "Đổ nước! Kéo!"),
                       (5.0, 9.5, "Ngày hai mươi. / Đá nặng thì... cho nó trượt.")]),
            dict(name="Ngày 45", tiktok="5-10", label="Ngày 45",
                 img=f"First-person view at the half-built wall, {FACE} trying to slip a leaf into a joint between two stone blocks so he can lean and nap, the leaf will not go in, realistic, vertical 9:16.",
                 vid=("0-5s: The wall is half built. Anh Tư tries to wedge a leaf into a joint to make a little pillow for a nap; "
                      "the leaf crumples, the joint is too tight. 5-10s: He sighs to the camera: \"Ngày bốn lăm. Khe đá không "
                      "lọt nổi cái lá.\""),
                 subs=[(5.0, 9.5, "Ngày bốn lăm. / Khe đá không lọt / nổi cái lá.")]),
            dict(name="Ngày 70", tiktok="5-10", label="Ngày 70",
                 img=f"First-person view at night by a campfire, {FACE} holding a folded paper letter from home (no visible writing), smiling tiredly, the tall stone walls behind him, realistic, vertical 9:16.",
                 vid=("0-5s: By the campfire Anh Tư unfolds a letter from home and smiles. 5-10s: He tells the camera: \"Vợ hỏi "
                      "bao giờ về. Em bảo: khi nào đá thôi nặng.\""),
                 subs=[(5.0, 9.5, "Vợ hỏi bao giờ về. / Em bảo: / khi nào đá thôi nặng.")]),
            dict(name="Ngày 89", tiktok="5-10", label="Ngày 89",
                 img=f"First-person view under the stone arch gate as the last wedge-shaped keystone is lowered by ropes into the top of the arch, everyone holding their breath, {FACE} gripping a rope, realistic, vertical 9:16.",
                 vid=("0-5s: Silence; the last wedge-shaped stone is lowered into the top of the arch... it slides in perfectly. "
                      "Cheers. 5-10s: Anh Tư, wiping tears and sweat, to the camera: \"Ngày tám chín. Hòn cuối cùng... vừa khít.\""),
                 subs=[(0.5, 4.8, "Thả từ từ... / thả từ từ..."),
                       (5.0, 9.5, "Ngày tám chín. / Hòn cuối cùng... vừa khít.")]),
            dict(name="Ngày 90", tiktok="3-10", label="Ngày 90",
                 img=f"First-person view at sunrise in front of the finished arched stone gate, {FACE} standing proudly with his rope coiled on his shoulder, realistic, vertical 9:16.",
                 vid=("0-4.5s: Sunrise at the finished gate. Anh Tư to the camera: \"Ngày chín mươi. Ba tháng xây xong... sáu "
                      "trăm năm chưa đổ.\" 4.5-10s: The image slowly ages into " + NOW + ". A calm narrator's voice says: \"Ngày "
                      "thứ hơn hai trăm hai mươi nghìn... thành vẫn đứng.\""),
                 subs=[(3.0, 4.4, "Ngày chín mươi."),
                       (4.5, 6.6, "Ba tháng xây xong... / sáu trăm năm chưa đổ."),
                       (6.7, 8.4, "Ngày thứ 229 nghìn: / vẫn đứng.")]),
        ],
        caption=("90 ngày, một tòa thành đá, không một chút vữa 😳 Năm 1397, thành nhà Hồ xây xong trong khoảng 3 tháng bằng "
                 "những phiến đá nặng hàng chục tấn xếp khít lên nhau. Hơn 600 năm sau vẫn đứng. Ngày nào trong nhật ký làm bạn "
                 "cười nhất? 👇"),
        tt_title="Nhật ký 90 ngày xây thành đá không vữa",
        hooks_alt=["POV: 90 ngày / một tòa thành / không chút vữa", "POV: Khe đá / không lọt nổi cái lá"],
        pin=("Từ 1397 đến nay là khoảng 229 nghìn ngày 😮 Bạn có biết thành nhà Hồ đã được UNESCO công nhận năm nào không? "
             "Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Nhật ký 90 ngày xây thành nhà Hồ không vữa (1397) | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
    # ================================================================== Mẫu C: Ông thợ cả khó tính (cặp đôi hài)
    dict(COMMON,
        slug="thanh-nha-ho-tho-ca-kho-tinh", prefix="th1397c",
        voices={"old mason": "a slow, gravelly, very strict old male voice with dry humor"},
        title="Mẫu C · Ông thợ cả khó tính: khe đá nào lọt sợi tóc là dỡ ra xếp lại (Thành nhà Hồ, 1397)",
        hook="POV: Ông thợ cả / thử khe đá / bằng sợi tóc",
        clips=[
            dict(name="Luật sợi tóc", tiktok="0-5", label="An Tôn, Thanh Hóa · 1397",
                 img=f"First-person view of a nearly bald, very strict old master mason with a thin white beard holding up a single strand of hair between two fingers in front of a stone wall, {FACE} beside him, confused, realistic, vertical 9:16.",
                 vid=("0-5s: The old master mason plucks one strand of hair and holds it up: \"Khe nào lọt sợi tóc này... là "
                      "dỡ ra xếp lại.\" Anh Tư: \"Không có vữa ạ?\" The mason: \"Vữa là cho thợ vụng.\" 5-10s: Anh Tư glances at the "
                      "mason's nearly bald head and covers a smile."),
                 subs=[(0.3, 2.6, "Khe nào lọt sợi tóc này / là dỡ ra xếp lại."),
                       (2.6, 3.4, "Không có vữa ạ?"),
                       (3.4, 4.9, "Vữa là / cho thợ vụng.")]),
            dict(name="Dỡ!", tiktok="5-10", label="",
                 img=f"Close view of the old mason's fingers sliding a strand of hair into a tiny gap between two huge stone blocks, laborers groaning behind, {FACE} slapping his forehead, realistic, vertical 9:16.",
                 vid=("0-5s: The mason slides his hair into a joint; it goes in a little. He says flatly: \"Dỡ.\" Twenty "
                      "laborers groan. 5-10s: Anh Tư whispers to the viewer: \"Ông còn có ba sợi tóc... mà đòi thử cả tòa "
                      "thành.\""),
                 subs=[(0.5, 4.8, "Dỡ."),
                       (5.0, 9.5, "Ông còn có ba sợi tóc... / mà đòi thử cả tòa thành.")]),
            dict(name="Vữa tự nhiên", tiktok="5-10", label="",
                 img=f"First-person view as the old mason rubs a bit of mud from a stone joint between his fingers and sniffs it, {FACE} standing with muddy hands behind his back, guilty, realistic, vertical 9:16.",
                 vid=("0-5s: The mason rubs mud from a joint and sniffs it: \"Bùn à?\" Anh Tư, hiding muddy hands: \"Dạ... vữa "
                      "tự nhiên ạ.\" 5-10s: The mason, without blinking: \"Dỡ.\" Anh Tư to the viewer: \"Em giấu được vợ... "
                      "không giấu được ông.\""),
                 subs=[(0.5, 2.2, "Bùn à?"),
                       (2.2, 4.8, "Dạ... / vữa tự nhiên ạ."),
                       (5.0, 6.4, "Dỡ."),
                       (6.4, 9.5, "Em giấu được vợ... / không giấu được ông.")]),
            dict(name="Đá nghe hò", tiktok="5-10", label="",
                 img=f"First-person view as the old mason starts a rhythmic work chant and dozens of laborers pull ropes in time, a giant stone block finally rolling forward on logs, {FACE} chanting along, realistic, vertical 9:16.",
                 vid=("0-5s: The block will not move. The mason starts a rhythmic work chant: \"Hò dô ta... nào!\" Everyone "
                      "pulls in time and the block rolls forward. 5-10s: Anh Tư, amazed: \"Hóa ra đá... phải nghe hò mới chịu "
                      "đi.\""),
                 subs=[(0.5, 4.8, "Hò dô ta... nào!"),
                       (5.0, 9.5, "Hóa ra đá... / phải nghe hò mới chịu đi.")]),
            dict(name="Thử vòm", tiktok="5-10", label="",
                 img=f"First-person view under a newly finished stone arch with no mortar, {FACE} standing alone right underneath looking up nervously, the old mason standing safely outside the arch with arms crossed, realistic, vertical 9:16.",
                 vid=("0-5s: The mason tells Anh Tư to stand under the new arch: \"Đứng đấy. Đá tự giữ nhau.\" 5-10s: Anh Tư "
                      "looks up, then at the mason standing well outside: \"Ông bảo đá tự giữ nhau... ông đứng ra ngoài làm "
                      "gì?\""),
                 subs=[(0.5, 4.8, "Đứng đấy. / Đá tự giữ nhau."),
                       (5.0, 9.5, "Đá tự giữ nhau... / ông đứng ra ngoài làm gì?")]),
            dict(name="Lần đầu ông cười", tiktok="5-10", label="",
                 img=f"Close view of the old mason trying to push a strand of hair into the final joint of the finished gate, the hair bending and not going in, the mason smiling for the first time, {FACE} in the background staring in disbelief, realistic, vertical 9:16.",
                 vid=("0-5s: At the final joint the mason pushes his hair; it bends, it will not go in. Silence. Then, slowly, "
                      "the strict old man smiles. 5-10s: Anh Tư whispers to the viewer: \"Ba tháng... lần đầu ông ấy cười.\""),
                 subs=[(5.0, 9.5, "Ba tháng... / lần đầu ông ấy cười.")]),
            dict(name="Câu chốt", tiktok="3-10", label="",
                 img=f"First-person view at sunrise at the finished arched stone gate, the old mason and {FACE} sitting side by side on a stone, looking at the wall, realistic, vertical 9:16.",
                 vid=("0-4.5s: Sunrise; the old mason and Anh Tư sit side by side looking at the gate. Anh Tư: \"Ba tháng xây "
                      "xong... sáu trăm năm chưa đổ.\" 4.5-10s: The image slowly ages into " + NOW + "; a strand of hair caught "
                      "by the wind presses against a joint and does not go in. A calm narrator's voice says: \"Hơn 600 năm "
                      "sau... sợi tóc vẫn không lọt.\""),
                 subs=[(3.0, 4.4, "Ông ơi..."),
                       (4.5, 6.6, "Ba tháng xây xong... / sáu trăm năm chưa đổ."),
                       (6.7, 8.4, "Hơn 600 năm sau... / sợi tóc vẫn không lọt.")]),
        ],
        caption=("Ông thợ cả khó tính nhất Đại Việt: khe đá nào lọt sợi tóc là dỡ ra xếp lại 😂 Năm 1397, thành nhà Hồ xây xong "
                 "trong khoảng 3 tháng bằng đá nặng hàng chục tấn, không dùng vữa. Sếp bạn có khó tính bằng ông này không? 👇"),
        tt_title="Ông thợ cả thử khe đá bằng sợi tóc, lọt là dỡ ra xếp lại",
        hooks_alt=["POV: Khe đá lọt sợi tóc / là dỡ ra làm lại", "POV: Ông thợ cả / khó tính nhất Đại Việt"],
        pin=("Phép thử sợi tóc là hư cấu cho vui, nhưng đá thành nhà Hồ xếp khít không vữa là thật 🔥 Bạn đã thử đến tận nơi "
             "xem khe đá chưa? Follow để xem Tự hào Đại Việt tập tiếp theo!"),
        yt_title="Ông thợ cả khó tính và tòa thành không vữa (thành nhà Hồ 1397) | Tự hào Đại Việt",
        yt_tags=YT_TAGS,
    ),
]

if __name__ == "__main__":
    build(EPISODES, HERE, series_tag="#tuhaodaiviet #anhtu", note=NOTE, unit="Mẫu", file_unit="mau")
