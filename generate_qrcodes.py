import os
import qrcode
from PIL import Image

output_dir = r"c:\Users\ABC\Documents\Anti_G\真鍋庭園‗QRコード作成\qr_codes"
os.makedirs(output_dir, exist_ok=True)

items = [
    {
        "filename": "00_総合案内看板_gate.png",
        "name": "会場入口・総合案内看板",
        "artist": "全体用",
        "work": "森のオープンギャラリー「大きな木」",
        "source": "gate",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=gate&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "00_チラシ・ポスター_flyer.png",
        "name": "チラシ・ポスター・DM用",
        "artist": "広報物",
        "work": "配布用",
        "source": "flyer",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=flyer&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "01_赤木ミライ_akagi.png",
        "name": "赤木ミライ",
        "artist": "赤木ミライ (Mirai Akagi)",
        "work": "仮住まい",
        "source": "akagi",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=akagi&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "02_アザミユウカ_azami.png",
        "name": "アザミユウカ",
        "artist": "アザミユウカ (Yuuka Azami)",
        "work": "庭の中の布",
        "source": "azami",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=azami&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "03_清水日菜乃_shimizu.png",
        "name": "清水日菜乃",
        "artist": "清水日菜乃 (Hinano Shimizu)",
        "work": "穏やかな日",
        "source": "shimizu",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=shimizu&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "04_髙野友希_takano.png",
        "name": "髙野友希",
        "artist": "髙野友希 (Tomoki Takano)",
        "work": "羽衣 / 思うがままに",
        "source": "takano",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=takano&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "05_武田なのか_takeda.png",
        "name": "武田なのか",
        "artist": "武田なのか (Nanoka Takeda)",
        "work": "へびとくも",
        "source": "takeda",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=takeda&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "06_中林拓巳_nakabayashi.png",
        "name": "中林拓巳",
        "artist": "中林拓巳 (Takumi Nakabayashi)",
        "work": "返礼",
        "source": "nakabayashi",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=nakabayashi&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "07_水野夏_mizuno.png",
        "name": "水野夏",
        "artist": "水野夏 (Natsu Mizuno)",
        "work": "1070.43",
        "source": "mizuno",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=mizuno&utm_medium=qr&utm_campaign=fisc2026"
    },
    {
        "filename": "08_渡邉光子_watanabe.png",
        "name": "渡邉光子",
        "artist": "渡邉光子 (Mitsuko Watanabe)",
        "work": "人はみな言葉でできた、庭だから",
        "source": "watanabe",
        "url": "https://awakuf.github.io/forest_gallery_web/?utm_source=watanabe&utm_medium=qr&utm_campaign=fisc2026"
    }
]

print("QRコード生成開始...")
for item in items:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M, # 屋外印刷等に耐えられるM (15%復元)
        box_size=12, # 高解像度
        border=4,
    )
    qr.add_data(item["url"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    path = os.path.join(output_dir, item["filename"])
    img.save(path)
    print(f"作成完了: {item['filename']} -> {item['url']}")

print(f"\n合計 {len(items)} 個のQRコード画像の出力を完了しました。")
