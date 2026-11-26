# The Detour Lab — English edition

An independent English-language explainer channel. This is a separate project from the Japanese channel "寄り道ラボ" (`E:\rekishikaisetu-honnoji`). It has its own directory, assets, voice, and build scripts. No file in the Japanese project is modified by this work.

Build scripts use `detour_ffmpeg.py`, which resolves ffmpeg through `ytkit.ffmpeg_tools` in `E:\yt-shorts-kit`. The voice (Kokoro / Piper) and subtitle text stay local to this project.

## Script review

`script_review.py` sends a script to ChatGPT and Google AI (`www.google.com/ai`) in parallel through the shared `ytkit.review` package. The default input is `SAMPLE_SCRIPT.md`; `--path` selects another file.

```
python script_review.py ocean_blue                 # both targets, in parallel
python script_review.py ocean_blue --target chatgpt
python script_review.py ocean_blue --path draft.md --dry-run
```

Sign in to both sites in the review Chrome first. `REVIEW_CDP_PORT` sets the CDP port (default 9222). Replies are saved as `out_en/review_<target>_<slug>.md`. Google AI takes one to three minutes to finish.

The markdown adapter turns each `##` heading into one scene and leaves the claims list empty. For a real script review, pass a JSON file with `scenes` and `claims` and add `--adapter honnoji_json`; see `out_en/violet_review_input.json`. Use Python 3.12 with `PYTHONPATH=E:\yt-shorts-kit` (playwright is installed there).

The sample script is a production note, not narration. Both reviewers flagged this; use a real narration script before acting on their comments.

To review a finished video in Google AI:

```
python script_review_video.py out_en/ocean_blue_fv.mp4 --slug ocean_blue
python script_review_video.py out_en/ocean_blue_fv.mp4 --dry-run
```

The reply is saved as `out_en/review_google_video_<slug>.md`. Uploading takes a few minutes.

## What this project is

The Detour Lab makes short, source-based explainers for English speakers. Each video starts with something you think you know, checks it against real sources, and ends by separating **what we can say** from **what we cannot say yet**.

The voice is plain and careful:

- Short sentences. One idea per sentence.
- No facts without a source. If a number is uncertain, say so.
- No made-up stories, no invented quotes, no invented dates.
- "We checked" means a source was actually opened and read.

## Files

| File | What it is |
| --- | --- |
| `SPEC.md` | Specification: format, evidence rules, upload settings, voice licenses, open decisions |
| `channel.toml` | Channel name, tagline, about text, voice and credit settings |
| `ABOUT.md` | Full channel description, ready to paste into YouTube |
| `DESCRIPTION_TEMPLATE.md` | Template for the bottom of every video description |
| `STYLE_GUIDE.md` | Plain-English writing rules and the Japanese-to-English term table |
| `SAMPLE_SCRIPT.md` | One sample script, in English, with sources |
| `VIDEO_OCEAN_BLUE.md` | Result and verification record for the first Short |
| `VIDEO_SUNSET.md` | Result and verification record for the second Short |
| `VIDEO_CLOUDS.md` | Result and verification record for the third Short |
| `VIDEO_DEEP_SEA.md` | Result and verification record for the fourth Short |
| `RETENTION_PLAN.md` | Viewer-retention plan and its current blockers |
| `TRENDS.md` | Trend scan and how it maps to the channel |
| `VIDEO_RAINBOW.md` | Result and verification record for the fifth Short |
| `build_rainbow.py` | Build script for the fifth Short (rainbow) |
| `build_sunset.py` | Build script for the second Short (sunset red sky) |
| `PREPUBLICATION_REVIEW.md` | Pre-publication review and response status |
| `GOOGLE_AI_REVIEW.md` | Google AI Mode video review and how its findings were assessed |
| `PUBLISHING_STRATEGY.md` | Posting cadence, timing, and the full team's reasoning |
| `build_fv.py` | Build script for the final video (FreeVideo background) |
| `build_short_kokoro.py` | Build script for the Kokoro narration (drawn-diagram background) |
| `build_short_kokoro_high.py` | High-pitch voice experiment (bf_alice) |
| `build_short_piper.py` | Earlier Piper-voice build script |
| `build_short.py` | Original edge-tts build script (voice license unconfirmed) |
| `out_en/ocean_blue_fv.mp4` | Final Short (27.0 s, Kokoro af_heart, FreeVideo background) |
| `assets/tts/kokoro/` | Kokoro model and voices, Apache 2.0, with MANIFEST.json |
| `assets/tts/en_US-kristin-medium.onnx` | Piper voice model, public domain |
| `assets/bgm_maou/maou_bgm_piano12.mp3` | BGM, 魔王魂, commercial use OK |
| `assets/ocean2500/fv/clip1-4.mp4` | FreeVideo clips used in the final video |

## YouTube channel

- Channel ID: `UCVaaGEdA388lGHitFY9PNSw`
- Public URL: https://www.youtube.com/channel/UCVaaGEdA388lGHitFY9PNSw
- Display name changed to `The Detour Lab` on 2026-11-25 with bsk. Verified on the public page.
- Handle remains `@detour-lab`. `@thedetourlab` was already taken, so the name change was published while keeping the handle.
- Channel description set from `ABOUT.md` on 2026-11-25, shortened to fit YouTube's 1000-character limit.

## Branding images

- `assets/branding/profile.png` — 800x800 avatar. Deep navy background with a blue detour path and a small marker.
- `assets/branding/banner.png` — 2048x1152 channel banner. Deep navy map with a blue winding road; no text.
- Both were generated with FreeVideo 0.6.10 / MiniMax H3 Image on 2026-11-25. Prompts are recorded in the build note from that task. They are AI-generated images and are covered by the channel's synthetic-content disclosure.
- Both were uploaded to YouTube Studio with bsk on 2026-11-25 and verified on the public channel page. bsk's own upload command was refused by the browser, so the image bytes were staged into the page with `bsk evaluate` and applied to the file inputs there.

## Publication status

- Cadence is three Shorts per week (Mon/Wed/Fri) at 21:30 JST; see `PUBLISHING_STRATEGY.md`. Revise after two weeks of analytics.
- Launch burst: four Shorts scheduled for 21:30 JST on consecutive days — 11/25 (ocean blue), 11/26 (sunset, `TIZC-zpz4Xc`), 11/27 (clouds, `pp5UjX3HSPQ`), 11/28 (deep sea, replacement upload). The cadence returns to three per week after the burst.
- The deep-sea video was rebuilt with new dark-ocean clips after the user reported that the reused bright coral footage was unconvincing. The earlier upload (`wGuQ63JNCLk`) is no longer scheduled and remains private.
- The first Short is scheduled for 2026-11-25 21:30 JST: https://youtube.com/shorts/SEPK3A5vXOw?feature=share
- Title: "Why Is the Ocean Blue? The Real Reason #Shorts"
- Uploaded with bsk; AI use declared as yes (audio and visual), made-for-kids and paid promotion declared no.
- The on-screen captions were changed from full narration sentences to two keyword lines before upload. The old file is kept as `out_en/ocean_blue_fv_before_caption_fix.mp4`.

## Not done yet

- Full listen-through of the narration by a person
- Google AI mode video review (done; see `GOOGLE_AI_REVIEW.md`)
- Smartphone display check on a real device
- SRT handling: the existing `.srt` still contains the full narration, not the two-line keywords
- Thumbnail design (auto-generated thumbnails are currently enabled)

## Naming

- Display name: **The Detour Lab**
- Suggested handle: `@thedetourlab` (availability must be checked in YouTube)
- Meaning: a "detour" is the small side road you take when you follow a curiosity. It keeps the spirit of the Japanese name without using Japanese words.
