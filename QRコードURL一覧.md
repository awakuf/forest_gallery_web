# FISC 2026 真鍋庭園「大きな木」QRコード個別集計URL一覧

各QRコードにはGoogle標準の「UTMパラメータ（`utm_source` / `utm_medium` / `utm_campaign`）」を設定しています。  
これにより、**Google アナリティクス (GA4) の管理画面で「どのQRコードから何人アクセスしたか」が自動で分類・集計**されます。

高画質QRコード画像（PNG）は `qr_codes/` フォルダに保存されています。

---

## 1. QRコード & URL一覧

### ■ 全体・広報用
| 分類・場所 | ファイル名 | GA4集計キー (utm_source) | 個別計測用URL |
| :--- | :--- | :--- | :--- |
| **会場入口・総合案内看板** | `00_総合案内看板_gate.png` | `gate` | `https://awakuf.github.io/forest_gallery_web/?utm_source=gate&utm_medium=qr&utm_campaign=fisc2026` |
| **チラシ・ポスター・DM** | `00_チラシ・ポスター_flyer.png` | `flyer` | `https://awakuf.github.io/forest_gallery_web/?utm_source=flyer&utm_medium=qr&utm_campaign=fisc2026` |

### ■ 各アーティスト作品キャプション用（50音順・全8名）
| 作家名 | 作品名 | ファイル名 | GA4集計キー (utm_source) | 個別計測用URL |
| :--- | :--- | :--- | :--- | :--- |
| **赤木ミライ** | 『仮住まい』 | `01_赤木ミライ_akagi.png` | `akagi` | `https://awakuf.github.io/forest_gallery_web/?utm_source=akagi&utm_medium=qr&utm_campaign=fisc2026` |
| **アザミユウカ** | 『庭の中の布』 | `02_アザミユウカ_azami.png` | `azami` | `https://awakuf.github.io/forest_gallery_web/?utm_source=azami&utm_medium=qr&utm_campaign=fisc2026` |
| **清水日菜乃** | 『穏やかな日』 | `03_清水日菜乃_shimizu.png` | `shimizu` | `https://awakuf.github.io/forest_gallery_web/?utm_source=shimizu&utm_medium=qr&utm_campaign=fisc2026` |
| **髙野友希** | 『羽衣』/『思うがままに』 | `04_髙野友希_takano.png` | `takano` | `https://awakuf.github.io/forest_gallery_web/?utm_source=takano&utm_medium=qr&utm_campaign=fisc2026` |
| **武田なのか** | 『へびとくも』 | `05_武田なのか_takeda.png` | `takeda` | `https://awakuf.github.io/forest_gallery_web/?utm_source=takeda&utm_medium=qr&utm_campaign=fisc2026` |
| **中林拓巳** | 『返礼』 | `06_中林拓巳_nakabayashi.png` | `nakabayashi` | `https://awakuf.github.io/forest_gallery_web/?utm_source=nakabayashi&utm_medium=qr&utm_campaign=fisc2026` |
| **水野夏** | 『1070.43』 | `07_水野夏_mizuno.png` | `mizuno` | `https://awakuf.github.io/forest_gallery_web/?utm_source=mizuno&utm_medium=qr&utm_campaign=fisc2026` |
| **渡邉光子** | 『人はみな言葉でできた、庭だから』 | `08_渡邉光子_watanabe.png` | `watanabe` | `https://awakuf.github.io/forest_gallery_web/?utm_source=watanabe&utm_medium=qr&utm_campaign=fisc2026` |

---

## 2. Google アナリティクス (GA4) での集計確認方法

QRコードからのアクセスは、以下の手順で簡単に確認できます。

1. **[Google アナリティクス](https://analytics.google.com/)** にログイン
2. 左メニューから **「レポート」 ＞ 「集客」 ＞ 「トラフィック獲得」** をクリック
3. 表の左上にあるプルダウン（デフォルトは「セッションのデフォルト チャネル グループ」）をクリックし、**「セッションの参照元 / メディア」** または **「セッションの参照元」** を選択します。
4. 表に以下のように表示され、それぞれの**ユーザー数（来場者数）**と**セッション数（開かれた回数）**が一覧で確認できます：
   * `gate / qr`
   * `flyer / qr`
   * `akagi / qr`
   * `azami / qr`
   * `shimizu / qr`
   * …

※また、キャンペーン名に `fisc2026` を指定しているため、「セッションのキャンペーン」を選べばこの展示のQRコード経由のアクセスだけを絞り込んで確認することもできます。
