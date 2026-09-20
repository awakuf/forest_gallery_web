# FISC 2026 真鍋庭園「森のオープンギャラリー」アクセス解析＆QRコード運用ガイド

本ドキュメントは、真鍋庭園 森のオープンギャラリー「大きな木」Vol.18 (FISC 2026) Webサイトにおける、**来場者アクセス数の確認手順**および**個別QRコードの管理・運用方法**についての公式マニュアルです。

---

## 1. システム設定概要

* **対象Webサイト**: [https://awakuf.github.io/forest_gallery_web/](https://awakuf.github.io/forest_gallery_web/)
* **アクセス解析基盤**: Google アナリティクス 4 (GA4)
* **測定ID**: `G-6LRDWNFBVW`
* **対象ソースコード**: `index.html`, `forest_gallery_web.html`（タグ組み込み済み）

---

## 2. アクセス数の確認方法（完全手順）

Google アナリティクスを使うと、**「今現在のアクセス（リアルタイム）」** と **「過去の累計アクセス（日別・作品別）」** の両方を確認できます。

### 【手順A】 今現在のアクセスを見る（リアルタイム確認）
現地の展示中やテスト時に、「今誰かが見ているか」を即座に確認する方法です。

1. **[Google アナリティクス](https://analytics.google.com/)** にログインします。
2. 画面左側のメニューアイコンから **「レポート」**（グラフのアイコン）をクリックします。
3. **「リアルタイム」** をクリックします。
4. **表示される内容**:
   * **過去30分間のユーザー**: 直近30分間にアクセスした人数
   * **ユーザーの国・地域**: どこからアクセスされたか（日本・北海道・帯広市など）
   * **デバイス**: モバイル（スマホ）かパソコンか

---

### 【手順B】 作品別・QRコード別のアクセス数を見る（最重要）
「どの作品のQRコードが何回読まれたか」「看板と作品どちらが多いか」を確認する方法です。

1. **[Google アナリティクス](https://analytics.google.com/)** にログインします。
2. 左メニューから **「レポート」 ＞ 「集客」 ＞ 「トラフィック獲得」** を開きます。
3. 画面右上の **「日付範囲（期間）」** をクリックし、集計したい期間（例:「過去7日間」「今月」「全期間」など）を選び「適用」します。
4. 画面下部に表示されるテーブル（表）の左上にあるプルダウンをクリックします。
   * デフォルトでは「セッションのデフォルト チャネル グループ」になっています。
   * これを **「セッションの参照元 / メディア」**（または「セッションの参照元」）に変更します。
5. **表の確認**:
   以下のように、設置したQRコードごとのアクセス数が一覧表示されます。
   * **ユーザー**: アクセスした「実人数」
   * **セッション**: ページが開かれた「延べ回数」

| 表の表示例 (`参照元 / メディア`) | 意味 |
| :--- | :--- |
| `gate / qr` | 会場入口・総合案内看板のQRコード |
| `flyer / qr` | チラシ・ポスター・DMのQRコード |
| `akagi / qr` | 赤木ミライ 作品キャプションのQRコード |
| `azami / qr` | アザミユウカ 作品キャプションのQRコード |
| `shimizu / qr` | 清水日菜乃 作品キャプションのQRコード |
| `takano / qr` | 髙野友希 作品キャプションのQRコード |
| `takeda / qr` | 武田なのか 作品キャプションのQRコード |
| `nakabayashi / qr` | 中林拓巳 作品キャプションのQRコード |
| `mizuno / qr` | 水野夏 作品キャプションのQRコード |
| `watanabe / qr` | 渡邉光子 作品キャプションのQRコード |
| `(direct) / (none)` | QRコードではなくURL直接入力やブックマークからのアクセス |

> 💡 **ワンポイント（展示全体の絞り込み）**:  
> プルダウンで **「セッションのキャンペーン」** を選ぶと、今回設定した `fisc2026` というキャンペーン名で、QRコード全体の合計アクセス数だけを簡単にひとまとめで見ることもできます。

---

### 【手順C】 来場者の端末や利用状況を見る
* **スマホの種類（iPhone / Android）**:
  * 左メニュー **「ユーザー」 ＞ 「テクノロジー」 ＞ 「ユーザーの環境の詳細」**
* **アクセスされた時間帯や曜日**:
  * 左メニュー **「レポート スナップショット」** の概要カード等で時間帯別の山を確認できます。

---

## 3. QRコード・URL対応一覧表

生成済みの高画質QR画像は `qr_codes/` フォルダに保存されています。

| # | 設置場所 / 作家名 | 作品名 | ファイル名 (qr_codes/) | GA4キー | 個別計測用URL |
| :-: | :--- | :--- | :--- | :---: | :--- |
| 1 | **総合案内看板** | 全体案内 | `00_総合案内看板_gate.png` | `gate` | `https://awakuf.github.io/forest_gallery_web/?utm_source=gate&utm_medium=qr&utm_campaign=fisc2026` |
| 2 | **チラシ・ポスター** | 広報配布物 | `00_チラシ・ポスター_flyer.png` | `flyer` | `https://awakuf.github.io/forest_gallery_web/?utm_source=flyer&utm_medium=qr&utm_campaign=fisc2026` |
| 3 | **赤木ミライ** | 『仮住まい』 | `01_赤木ミライ_akagi.png` | `akagi` | `https://awakuf.github.io/forest_gallery_web/?utm_source=akagi&utm_medium=qr&utm_campaign=fisc2026` |
| 4 | **アザミユウカ** | 『庭の中の布』 | `02_アザミユウカ_azami.png` | `azami` | `https://awakuf.github.io/forest_gallery_web/?utm_source=azami&utm_medium=qr&utm_campaign=fisc2026` |
| 5 | **清水日菜乃** | 『穏やかな日』 | `03_清水日菜乃_shimizu.png` | `shimizu` | `https://awakuf.github.io/forest_gallery_web/?utm_source=shimizu&utm_medium=qr&utm_campaign=fisc2026` |
| 6 | **髙野友希** | 『羽衣』/『思うがままに』 | `04_髙野友希_takano.png` | `takano` | `https://awakuf.github.io/forest_gallery_web/?utm_source=takano&utm_medium=qr&utm_campaign=fisc2026` |
| 7 | **武田なのか** | 『へびとくも』 | `05_武田なのか_takeda.png` | `takeda` | `https://awakuf.github.io/forest_gallery_web/?utm_source=takeda&utm_medium=qr&utm_campaign=fisc2026` |
| 8 | **中林拓巳** | 『返礼』 | `06_中林拓巳_nakabayashi.png` | `nakabayashi` | `https://awakuf.github.io/forest_gallery_web/?utm_source=nakabayashi&utm_medium=qr&utm_campaign=fisc2026` |
| 9 | **水野夏** | 『1070.43』 | `07_水野夏_mizuno.png` | `mizuno` | `https://awakuf.github.io/forest_gallery_web/?utm_source=mizuno&utm_medium=qr&utm_campaign=fisc2026` |
| 10 | **渡邉光子** | 『人はみな言葉でできた、庭だから』 | `08_渡邉光子_watanabe.png` | `watanabe` | `https://awakuf.github.io/forest_gallery_web/?utm_source=watanabe&utm_medium=qr&utm_campaign=fisc2026` |

---

## 4. よくある質問・注意点 (FAQ)

### Q. GitHubリポジトリの「Insights > Traffic」と何が違うのですか？
* **GitHubのTraffic**: プログラムのソースコード（GitHub）を見に来た回数です。**一般来場者の数字はここには出ません。**
* **Google アナリティクス**: スマホでQRコードを読み取ってWebサイトを開いた**実際の来場者数**が集計されます。

### Q. QRコードを新しく作成・追加したいときは？
上記の一覧表にある「個別計測用URL」をコピーし、無料のQRコード生成サイトやデザインツール等に入力して作成してください。
新しく別の場所用に追加したい場合は、URL末尾の `utm_source=任意の英数字`（例: `utm_source=goods` など）を変更するだけで自動的にGA4で個別集計されます。

### Q. 当日のアクセス数が反映されるまでに時間はかかりますか？
* **「リアルタイム」レポート**: 数秒〜数十秒で即座に反映されます。
* **「トラフィック獲得」レポート（日別・作品別の詳細表）**: データ確定・集計処理のため、前日や数時間前のデータが反映されるまでに通常24時間〜48時間程度かかる場合があります。当日の速報を見たいときは「リアルタイム」画面をご確認ください。
