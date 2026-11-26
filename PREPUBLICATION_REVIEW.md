# 公開前レビュー — "Why does the ocean look blue?"

- レビュー日: 2026-11-25
- 対象: `out_en/ocean_blue_fv.mp4`
- 編成: evidence（出典・台本） / techqc（技術QC） / credits（クレジット・申告） / display（表示・可読性）
- neoen の指定どおり、この任務に必要な4名だけを参加させ、完了時点で解散させた。
- 既存ファイルの変更はなし。この報告書を新規作成したのみ。

## 判定（2026-11-25 追記で更新）

P0 の指摘はすべて反映済み。説明文と申告文案のファイルも作成した。技術的な破損はない。

残るのは仕様判断3項目（尺、字幕、セーフエリア）と、このレビューでは代替できない人手作業である。これらが片付くまで公開は保留。

## 対応状況（2026-11-25 追記）

完了:

- 1.1 声のクレジットを Kokoro `af_heart` に統一（`DESCRIPTION_TEMPLATE.md`, `ABOUT.md`, `channel.toml`, `VIDEO_OCEAN_BLUE.md`, `SPEC.md`）。Piper は初期ドラフトとして明記。
- 1.2 AI生成背景を申告する記述に統一。古い「Pillow 図解で AI生成ではない」という記述は初期ドラフト限定に書き換えた。
- 1.3 説明文を `out_en/ocean_blue_description.md` に新規作成。
- 1.4 申告文案を `out_en/ocean_blue_disclosure.md` に新規作成（audio と visual の両方を申告）。
- 1.5 ユーザーが生成ツールを FlashML-org/FreeVideo と確認。一次資料（FreeVideo README、MiniMax H3 Community License）を開いて事実を記録した。日本は許可地域内、地域内での商用利用は条件付きで可。年収益2,000万米ドル超には事前の書面承認、商用 product/service の UI への "MiniMax H3" 表示、公衆への公表時の機械生成コンテンツの明確な開示が条項としてある。説明文にツール名を入れて開示済み。法務判断はしていない。

あわせて修正:

- `VIDEO_OCEAN_BLUE.md` のラウドネスを実測 −15.8 LUFS / −1.4 dBTP に更新（旧記録 −16.3 / −1.3 は削除）。
- 同ファイルの無音記述を更新。最終 mp4 では無音イベントなし、ナレーション単体ではフレーズ間 0.291–0.575 s・末尾 1.280 s。
- `README.md` にチャンネル ID と公開 URL、現在の公開名・ハンドルを記録。ユーザーが `The Detour Lab` / `@thedetourlab` へ変更予定。

未判断（P1）:

- 2.1 尺 26.958 s を維持するか、仕様の30秒に戻すか。
- 2.2 字幕を2行キーワードに直すか、`SPEC.md:25` を明文化して全文表示を認めるか。
- 2.3 Shorts UI のセーフエリアは実機確認が必要。

未実施:

- 人の耳による全編視聴、Google AI mode レビュー、実機スマホ確認、アップロード・予約公開、サムネイル。
- Studio の確認は bsk で実施した（ブラウザ拡張は不使用）。表示名を `The Detour Lab` に変更し、公開ページで確認済み。ハンドル `@thedetourlab` は取得済みだったため `@detour-lab` を維持。チャンネル説明も `ABOUT.md` から設定し公開済み（1000文字制限に合わせて短縮）。
- アイコンとバナーも FreeVideo 生成画像を設定し、公開ページで確認済み（`assets/branding/`）。
- 表示レビュー指摘を受けて字幕を2行キーワードに修正し再ビルド。techqc の再計測は尺・音声系が前回と同値、display は全シーン2行・重なりなしと確認。credits の3点一致ゲートも OK。
- 2026-11-25 21:30 JST に公開予約済み。YouTube Studio のコンテンツ一覧で「公開予約 2026/11/25 21:30」を確認。AI使用ははい（音声・映像）、子ども向け・有料プロモーションはいいえと申告済み。
- 実機確認は完了。ユーザーがスマホで確認し、左下のブランド文字と2行字幕の両方が見えるとの報告。ウォーターマーク修正は不要と判断。
- SRTは `out_en/ocean_blue_fv.srt` として全文・音声タイミングで成果物化。焼き込み字幕との二重表示を避けるため字幕トラックとしてはアップロードしない。SPEC §2 に明記済み。
- 残る: 人の耳での全編視聴のみ。

---

## 1. 公開前に直す問題（P0）

### 1.1 声のクレジットが最終版と一致しない

最終動画は Kokoro `af_heart`（Apache 2.0）。定型文と設定は Piper `en_US-kristin-medium`（public domain）のまま。

| file:line | 現状 | 修正 |
| --- | --- | --- |
| `DESCRIPTION_TEMPLATE.md:13` | Voice: Piper … | Kokoro `af_heart` + 出典注記（下記 3.3） |
| `ABOUT.md:20` | Voice: Piper … | Kokoro `af_heart` / Apache 2.0 |
| `channel.toml:12-19` | `speaker` / `credit` / `label` / `license_url` / `model` がすべて Piper | 5項目を Kokoro に更新。ライセンス URL は `SPEC.md:82-84` の確認済み URL |
| `VIDEO_OCEAN_BLUE.md:48` | 「Adopted voice is public domain: LibriVox」 | Kokoro `af_heart` / Apache 2.0 に変更。public domain は Piper ドラフトの説明に限定 |
| `SPEC.md:65-77`, `:93` | Piper が adopted、Kokoro が being tested / not needed | Piper を過去ドラフトに格下げし、Kokoro を採用済みに |
| `VIDEO_OCEAN_BLUE.md:16` | `build_short_piper.py` を adopted の再現スクリプトと表記 | 初期ドラフト用に変更。最終版は `build_fv.py:116-127` |

### 1.2 AI 生成背景の申告が欠けている

最終版の背景は FreeVideo の AI 生成映像4クリップ（`build_fv.py:27-33`, `:99-112`）。ところが `VIDEO_OCEAN_BLUE.md:58-60` は「Pillow で自作した図解、AI生成も写真も使っていない」と説明しており、同一ファイルの `:3` `:9` `:43` と矛盾する。

- `DESCRIPTION_TEMPLATE.md:15` の `made for this video` だけでは不十分。`:31` の自ルールにも反する。
- `SPEC.md:43`, `:99-101` は静止画向けの文言のまま。映像にも適用する必要がある。
- `ABOUT.md:11`, `channel.toml:21-28` に AI 生成背景の項目がない。

### 1.3 最終動画用の説明文が存在しない

`*description*` / `*desc*` で探したが見つかったのはテンプレートのみ。下記 3.3 の草案を新規作成する必要がある。

### 1.4 YouTube「Altered or synthetic content」を Yes で申告する

`SPEC.md:111` に従い回答は Yes。音声（合成ナレーション）と映像（AI生成クリップ）の両方に該当する。申告はアップロード画面で行うもので、説明文の注記では代替できない。

```
This video contains altered or synthetic content. Audio: the narration is AI-generated speech (Kokoro af_heart, text-to-speech), not a recording of a real person. Visual: the background is AI-generated video (four FreeVideo clips), not real footage. The music is a licensed track by 魔王魂, and the headings and captions were made for this video.
```

`SPEC.md:109` の Standard YouTube License は変更不要。

### 1.5 FreeVideo クリップのライセンス記録がない

`VIDEO_OCEAN_BLUE.md:43` にクリップの利用は記録されているが、規約の確認記録がない。`SPEC.md` §5 と `channel.toml` にもない。公開前に利用規約を確認して記録する。このレビューでは根拠がないため違法性も適法性も断定しない。

---

## 2. 仕様判断が必要な項目（P1）

### 2.1 尺が仕様の下限を割っている

| 項目 | 実測 | 照合 |
| --- | --- | --- |
| 再生時間 | 26.958 s | `SPEC.md:21` の 30〜45 s を 3.04 s 下回る |
| 記録との差 | `VIDEO_OCEAN_BLUE.md:39` の 27.0 s とは −0.042 s（一致） | 同ファイルの Files 表の 30.5 s とは −3.542 s（文書内で矛盾） |
| 話速 | 台本75語 / 26.958 s = 約167 wpm | `SPEC.md:23` の 130〜150 wpm を上回る |

`VIDEO_OCEAN_BLUE.md:39` には「2026-11-25、ユーザー依頼で末尾無音を 4.5 s → 1.0 s に短縮。短い終わりを優先した」とある。仕様を変えるか、尺を戻すかの判断が必要。

### 2.2 字幕が仕様に抵触する

`display` が代表6フレームと `fv_overlay1.png`〜`5.png` を確認した結果:

| シーン | 字幕行数 | 台本との関係 |
| --- | --- | --- |
| 1〜4 | 3行 | 台本の全文と一致 |
| 5 | 4行 | 台本の全文と一致 |

`SPEC.md:25` は「Maximum two lines per screen」「No full sentence from the narration」と定める一方、`:26` は「Captions: English, plain white, one caption block per scene」と定める。字幕に2行制限を適用するかは仕様内で曖昧。白字・1シーン1ブロック・音声タイミング自体は満たしている。

- 修正するなら `build_fv.py:49-59` の `wrap()` をキーワード表示に変更。
- 仕様を変えるなら `SPEC.md:25` に「字幕は全文表示を可」と明記。

### 2.3 セーフエリア

全テキストは画面内（x71–952、y110–1906）に収まり、見出しと字幕の重なりなし。ただし字幕の2行目以降（y1593〜）とブランド文字（y1883–1906）は Shorts の下部 UI ゾーンに入る可能性がある。シーン5の見出し右端 x952 が右12%の目安境界 x950 を2 px 超える。実際の覆う範囲は端末とアプリ版で異なるため、**確認できず**。字幕ブロックの上寄せとブランド文字の位置見直しを推奨。

---

## 3. 担当ごとの詳細

### 3.1 evidence（出典・台本）

`SPEC.md:7` に従い2件の URL を `web_fetch` で開き直した。両方 HTTP 200、本文取得可。原文論文は未確認。

| 台本 | 出典 | 原文の該当表現 | 判定 |
| --- | --- | --- | --- |
| "You may have heard that the ocean is blue because it reflects the sky." | WHOI | "One idea is that it reflects the sky. And it does—on the surface." | 一致（通説提示） |
| "The surface does reflect the sky. But divers still see blue underwater." | WHOI | "But if we sink below the surface, the blue color remains. Here, the water isn't reflecting the sky." | 一致。"divers" は画像キャプションの語 |
| "NOAA says water absorbs the red part of sunlight. The blue part is left." | NOAA | "The ocean is blue because water absorbs colors in the red part of the light spectrum. Like a filter, this leaves behind colors in the blue part…" | 一致 |
| "WHOI adds that particles in the water scatter the blue light back to our eyes." | WHOI | "…they're scattered by particles in the water, making it seem as though the water itself is blue." | 趣旨一致。"back to our eyes" は意訳 |
| "So the sky is part of the answer…" / "We did not check the original papers." | 両ページ | WHOI "And it does—on the surface." / "The blue hue is created by water itself." | 一致 |

軽微な点:

- `SPEC.md:41` の固定文言は単数 "paper"、台本は複数 "papers"。複数を使うなら記録に理由を残す。
- WHOI が略称のままで初出の全称がない（`STYLE_GUIDE.md:9`）。`SAMPLE_SCRIPT.md` は全称。
- 文2の事実主張に出典名がない（`SPEC.md:33`, `:40`）。
- `STYLE_GUIDE.md:7` の 12〜18語に対して 6/6/9/5/7語の文がある。意図的な短さなら記録に残す。
- `SPEC.md:34` の「残る問いで終わる」について、道徳はないが明示的な問いで終わっていない（軽微）。
- "In conclusion" / "Let's dive in" / "Don't forget to subscribe" などの禁止表現なし。

### 3.2 techqc（技術QC）

ffmpeg / ffprobe 8.1.2。計測できなかった項目なし。ファイルは未変更。

| 項目 | 実測 | 判定 |
| --- | --- | --- |
| 完全デコード | exit 0、stderr 空 | PASS |
| 解像度 / fps / 映像 | 1080x1920（9:16）/ 24 fps / H.264 High 約2.85 Mbps / 647フレーム | PASS |
| 音声 | AAC LC 96 kHz mono 約193 kbps（元 WAV 24 kHz をアップサンプリング） | 要判断 |
| Integrated loudness | −15.8 LUFS（LRA 1.9 LU） | 記録 −16.3 / ビルド指定 −14 と不一致 |
| True peak | −1.4 dB | 記録 −1.3 dBTP とわずかな差 |
| 無音（最終 mp4） | −40/−30/−25/−20/−15 dB、`d=0.2` すべてイベントなし | 記録「0.8〜1.1 s のギャップ」は**再現せず**（BGM が全域で鳴る） |
| 無音（ナレーション単体） | フレーズ間 0.291〜0.575 s が9ヶ所、末尾 1.280 s | 0.8 s 超は末尾のみ |
| SRT 開始 | 0.000 / 4.457 / 9.426 / 14.693 / 19.598 s | `kokoro_scene_starts.json` と ms 単位で一致 PASS |
| 映像カット位置 | 4.458 / 9.417 / 14.667 / 19.583 s | 音声との差 1〜27 ms（1フレーム未満）PASS |
| 焼き込み字幕 | `build_fv.py:62-79` が overlay PNG を表示。SRT を直接 burn-in していない | テキストは5件とも一致 |
| ファイルサイズ | 10,292,237 bytes（9.81 MiB） | — |

補足: `fv_list.txt` のパスは `E:\rekishikaisetu-honnoji\yorimichi-lab-en\out_en\` を指し、現環境に存在しない。`build_fv.py` が再生成するため成果物への影響はないが、再現性の観点で要判断。

### 3.3 credits（クレジット・申告）

矛盾一覧は 1.1 / 1.2 に統合済み。背景音楽は矛盾なし（`build_fv.py:117`, `:123` と `ABOUT.md:21`, `channel.toml:24`, `:27`, `DESCRIPTION_TEMPLATE.md:14`, `SPEC.md:61` が整合）。

**Kokoro の出典注記** — `SPEC.md:87` の open point は未確認のまま。同行の「採用するなら説明文に1行の出典注記を入れる」に従い、義務が及ぶとは書かずに事実と未確認の別だけを明記する。

```
Voice: Kokoro af_heart (Kokoro-82M, Apache 2.0). Its training data includes Koniwa (CC BY 3.0) and SIWIS (CC BY 4.0); whether those attribution terms apply to this generated narration has not been confirmed.
```

**説明文の草案** — 実ファイルが存在しないため、新規作成用。

```
A longer version with all the sources: [VIDEO URL]

Sources:
- NOAA National Ocean Service, "Why is the ocean blue?" — https://oceanservice.noaa.gov/facts/oceanblue.html
- Woods Hole Oceanographic Institution, "Why is the ocean blue?" — https://www.whoi.edu/ocean-learning-hub/ocean-facts/why-is-the-ocean-blue/
We did not check the original papers.

■ About this channel
The Detour Lab checks the things you think you know, using real sources and simple math.

■ Corrections
If you find a mistake, tell us in the comments. We will check it and correct it.

■ Credits
Voice: Kokoro af_heart (Kokoro-82M, Apache 2.0). Its training data includes Koniwa (CC BY 3.0) and SIWIS (CC BY 4.0); whether those attribution terms apply to this generated narration has not been confirmed.
Music: 魔王魂 (https://maou.audio/) Piano 12, composed by 森田交一
Background: AI-generated video clips (FreeVideo), not real footage. Headings and captions were made for this video.
```

`[VIDEO URL]` は `DESCRIPTION_TEMPLATE.md:23` のプレースホルダのまま。ロング版の URL はプロジェクト内に記載がない。

### 3.4 display（表示・可読性）

詳細は 2.2 / 2.3 に統合済み。1080x1920 を 270x480（25%）に縮小した静止画では見出し・サブラベル・字幕とも読めた。文字の欠落、画面外へのはみ出し、見出しと字幕の重なり、明るい背景での白字の沈みは代表フレームで見られなかった。コントラスト比の数値は未計測。実機の輝度・周囲光・グレア・Shorts UI・再生中の動きは再現できていない。

判定: **条件付き不合格**（字幕の行数と全文表示、セーフエリア悬念）。

---

## 4. このレビューで代替できない作業

1. 人の耳によるナレーション全編視聴
2. Google AI mode での動画レビュー（手動でファイル添付が必要）
3. 実機スマホでの表示確認（Shorts UI の覆う範囲、輝度、周囲光）
4. アップロード、予約公開、サムネイル

---

## 5. 推奨する進め方

1. P0（1.1〜1.5）をまとめて修正。クレジット表記は5ファイル＋設定にまたがるため、一度に揃える。
2. P1（2.1〜2.3）は判断が必要。尺は「短縮を維持する」か「仕様に戻す」か、字幕は「2行キーワードに直す」か「仕様を明文化する」かを決める。
3. 説明文を草案どおり新規作成し、FreeVideo の規約を確認して記録する。
4. そのうえで人手作業（全編視聴・Google AI mode・実機チェック）へ進む。

レビュー担当: lead（統合） / evidence / techqc / credits / display
