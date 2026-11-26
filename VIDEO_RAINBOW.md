# Produced Short — "Why rainbows appear after rain?"

Status: built, machine-checked and uploaded to YouTube on 2026-11-26 as **private** (video ID `TtA1aMXxEIM`, URL https://youtube.com/shorts/TtA1aMXxEIM ). No publication date set yet. Fifth video for the channel.

Files: `build_rainbow.py`, `out_en/rainbow_fv.mp4`, `out_en/rainbow_script.md`, `out_en/rainbow.srt`, `out_en/rainbow_scene_starts.json`, `out_en/rainbow_description.md`, `out_en/rainbow_disclosure.md`.

Sources opened and read on 2026-11-26: Met Office "Rainbows: optical wonders" — https://weather.metoffice.gov.uk/learn-about/weather/optical-effects/rainbows ; NOAA NESDIS "What Causes a Rainbow?" — https://www.nesdis.noaa.gov/about/k-12-education/optical-phenomena/what-causes-rainbow . Both are secondary explainer pages; original papers were not checked. The JMA FAQ was read as corroboration but is not named in the English script.

Background: two new FreeVideo / MiniMax H3 clips in `assets/ocean2500/rainbow/` (dark sky after rain with a natural rainbow; rainbow over a dark sea). No people, text or logos. `build_rainbow.py` uses clips 1, 2, 1, 2, 1 across the five scenes.

Verification: 31.458 s / 755 frames, 1080x1920 24 fps H.264 + AAC, full decode exit 0, -15.4 LUFS / -1.4 dBTP, no silence events, SRT starts match the scene-start JSON to the ms, all five scenes have two-line keyword captions with no heading overlap. Display review found the white text more legible than in earlier videos because of the dark rainy background; the usual 8–9 px overshoot of the desktop safe-area estimate remains, but real-device checks on earlier videos found the text visible.

## Google AI モードでのレビュー（2026-11-26、公開前にやり直し）

1回目は要約が返っただけだったため、同じスレッドで「問題点だけをタイムスタンプ付きで列挙してください」と聞き直した。批判的な指摘が返った。

| AI の指摘 | こちらの判定 |
| --- | --- |
| 字幕帯が画面下端から15〜25%の位置にあり Shorts UI と被るリスク | 既に1・2本目で実機確認済み。静画の目安より実機を優先し、今回は変更しない |
| 左下ウォーターマークが最下部で UI に隠れる | 1・2本目は実機で見えていた。虹は未確認だが、位置は従来どおりなので変更しない |
| 5シーン目で字幕が固定されたままナレーションが進む | 採用。見出し枠の副題に "How many colors?" はあるが、字幕帯に出ていない。次回の型に反映する |
| "Bending, not scattering" は屈折のみに単純化 | 部分的に採用。台本本体は bend / bounce / split と書いており不正確ではないが、字幕は "Bend + bounce" の方が安全 |
| 画面に出典のページ名・URL が無い | 不採用。SPEC §4 は説明文への出典記載を想定しており、画面は組織名のみという設計 |
| 「何色あるか言えない」は不自然 | 保留。Met Office は連続的な色の範囲を説明し、気象庁は6色と7色を挙げる。出典の表現差を「まだ言えない」に置いた判断は記録済みだが、自然さは改善余地あり |
| 動画内に AI 生成の開示が無い | 不採用。YouTube の申告フォームと説明文で開示する方針。動画内ラベルは現仕様に無い |

ユーザーから「毎回、アップロード前に動画のレビューを Google AI モードに聞く」ルールを指示済み。`PUBLISHING_STRATEGY.md` に必須ルールとして記録。`VIDEO_RAINBOW.md` に指摘と判定を残したことで、QC 記録の1行は満たした。5本目はアップロード後に実施したが、公開前にもやり直した。

Not performed: a human listen-through of the narration, a real-device check for this specific video, and a publication date.
