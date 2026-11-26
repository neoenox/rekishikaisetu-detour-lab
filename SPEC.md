# Specification — The Detour Lab (English edition)

Status: design complete on 2026-11-24. Items marked OPEN need a decision before production starts.

## 1. Identity

| Item | Decision |
| --- | --- |
| Display name | The Detour Lab |
| Handle | `@detour-lab` — checked in YouTube on 2026-11-25. `@thedetourlab` was already taken; YouTube suggested `@thedetourlab-x9k`, which was rejected. |
| Language | English (simple, for learners and general viewers) |
| Category | Education |
| Relationship to Japanese channel | Separate brand, separate folder, separate account. No file in the Japanese project is edited. |
| Tagline | "Follow the small questions" |
| Core promise | One small question, checked against real sources, ending with what we know and what we do not know yet. |

## 2. Format

| Item | Decision |
| --- | --- |
| Shorts | 9:16, 1080x1920, 30–45 seconds, 5–7 scenes |
| Long form | 16:9, 3–7 minutes, chapters in the description |
| Narration rate | About 130–150 words per minute. Final timing must be checked against the actual audio. |
| Scene length | 3–9 seconds per scene |
| On-screen text | Keywords and numbers only. Maximum two lines per screen. No full sentence from the narration. |
| Captions | On-screen: English, plain white, keywords and numbers only, at most two lines per scene, timed from the actual narration audio. A separate `.srt` containing the full narration is delivered for accessibility; its timings follow the audio, not the keyword captions. Do not upload it as a visible subtitle track when the keyword captions are burned in, because the text would appear twice. Word-level highlighting is not used. |
| No face on camera. No live presenter. | |

## 3. Episode structure

1. First 0–3 seconds: state the common belief. Do not open with a question.
2. Within 8 seconds: point to the answer's direction.
3. Body: at most three claims. Each claim names its source.
4. Last scene: separate "what we can say" from "what we cannot say yet".
5. Closing line: return to the opening idea. No subscribe prompt.

## 4. Evidence rules

- A claim may be stated only if a source was opened and read for this project.
- Name the organization. Do not write "experts say".
- If the original paper was not checked, write "We did not check the original paper."
- If a number is calculated by us, write "Our calculation".
- If an image or video is AI-generated, say so. For a still image write "This is an illustration, not a real photo." For video write "This is AI-generated video, not real footage."
- For news, write the full date and "Information as of YYYY-MM-DD".
- Corrections go in the description and, if needed, a pinned comment.

## 5. Voice, music, fonts — decisions recorded

The Japanese channel uses VOICEVOX:四国めたん. That voice reads Japanese and cannot be reused for English.

Voice candidates to evaluate before production:

| Candidate | What to check |
| --- | --- |
| A free English TTS voice (for example Edge/Azure neural voices) | Export rights, license text, whether audio files can be kept and published |
| A paid TTS service | Commercial license, cost per video, attribution requirement |
| Vocana + VOICEVOX (English through a Japanese voice bank) | License of both tools, intelligibility at normal speed |

Decision recorded: Kokoro `af_heart`; the license URL is in `channel.toml` and the credit line is in `ABOUT.md` and `DESCRIPTION_TEMPLATE.md`.

Music: 魔王魂 "Piano 12" (https://maou.audio/), the same track as the Japanese channel, used at low volume. License checked on the official site on 2026-11-24: commercial use OK, modification OK, no permission or report needed; credit "音楽：魔王魂" is sufficient. AI arrangement and training are prohibited; neither was done.

Fonts: Noto Sans JP (installed on Windows), the same typeface family as the Japanese channel. Headings use the Bold variation; captions use Medium; sub-labels use Regular.

### Voice — adopted

Kokoro `af_heart` (Kokoro-82M, Apache 2.0) is the voice in the final video `out_en/ocean_blue_fv.mp4`. License details and the open point are recorded in the Kokoro section below.

Build scripts: `build_short_kokoro.py` (narration) and `build_fv.py` (final assembly, including the audio and BGM mix at `build_fv.py:116-127`). Final output: `out_en/ocean_blue_fv.mp4` (27.0 s).

### Voice — earlier drafts (not adopted)

Piper `en_US-kristin-medium` (US English female, 22,050 Hz), generated locally with piper-tts 1.8.0. Voice file: `assets/tts/en_US-kristin-medium.onnx`. The user listened to both voices on 2026-11-24 and chose Piper at that time; the final video later adopted Kokoro `af_heart` instead.

**License: public domain.** The voice's MODEL_CARD says its recordings came from LibriVox.org and are public domain, trained from scratch (no fine-tuned base). No attribution is required, but the source is recorded here.

- MODEL_CARD: https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/kristin/medium/MODEL_CARD
- Piper commercial-use list: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/COMMERCIAL_USE.md
- Piper licensing notes: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/LICENSING.md

The Piper engine is GPL-3.0-or-later. The engine is a build tool and is not distributed with the video. Do not pick `en_US-lessac-medium`: its corpus is restricted to research use by the project's own documentation.

Build script: `build_short_piper.py`. Output: `out_en/ocean_blue_piper.mp4` (31.5 s). This draft must not be presented as the final voice.

### Kokoro — adopted, license details and open point

Kokoro-82M, Apache 2.0. License confirmed on 2026-11-24:
- Model card: https://huggingface.co/hexgrad/Kokoro-82M/raw/main/README.md has `license: apache-2.0` in its front matter.
- HuggingFace API reports `cardLicense=apache-2.0`, ungated and public.
- Apache 2.0 full text: https://github.com/hexgrad/kokoro/blob/main/LICENSE
- Model card says: "With Apache-licensed weights, Kokoro can be deployed anywhere from production environments to personal projects."

**Open point — handled by a description note:** the model card says part of the training data came from Koniwa (CC BY 3.0) and SIWIS (CC BY 4.0). No document states whether that attribution obligation reaches the generated audio. Not confirmed; this section does not decide either way. Because the voice was adopted, the following one-line source note is used in the description:

```
Voice: Kokoro af_heart (Kokoro-82M, Apache 2.0). Its training data includes Koniwa (CC BY 3.0) and SIWIS (CC BY 4.0); whether those attribution terms apply to this generated narration has not been confirmed.
```

### Voices previously tried (not adopted)

- Microsoft Azure `en-US-AvaNeural` via edge-tts. Better-sounding but no public license document confirms commercial use. File `out_en/ocean_blue.mp4` is kept as a draft only.
- Microsoft Zira Desktop (SAPI). Rejected as too mechanical.
- https://learn.microsoft.com/en-us/answers/questions/5925556/commercial-use-of-edge-read-aloud-voices-via-edge
- https://learn.microsoft.com/en-us/answers/questions/6032190/commercial-use-rights-for-microsoft-edge-read-alou
- https://raw.githubusercontent.com/rany2/edge-tts/master/README.md

### Background — adopted

The final video uses four existing FreeVideo AI-generated clips from `assets/ocean2500/fv/clip1-4.mp4` as the background, with heading panels and captions made for this video overlaid. The description says the background is AI-generated imagery and not real footage.

The user confirmed on 2026-11-25 that the clips were generated with FlashML-org/FreeVideo. Primary sources were opened and read on the same date:

- FreeVideo code is Apache 2.0 — https://github.com/FlashML-org/FreeVideo
- The model weights are under the MiniMax H3 Community License — https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/LICENSE
- The license defines the Applicable Territory as worldwide except the EU, the UK, the Republic of Korea and the USA (sections I.3 and I.5). Japan is inside it. Use within the territory is licensed with conditions.
- Section IV.1 requires prior written authorization if the commercial product or service generates more than US$20 million in yearly revenue. Section IV.2 requires prominent display of "MiniMax H3" on the user interface of a commercial product or service that uses it. Exhibit A item 12 requires clear and prominent disclosure when machine-generated content is published in a public environment.
- Section III.3 encourages, but does not require, a "Powered by MiniMax H3" notice and an AI-generation identifier. Section VI.4 says MiniMax claims no rights over the generated Outputs.
- For this video, the description discloses that the background is AI-generated and names FreeVideo and MiniMax H3 as a precaution. This paragraph records the license text; it is not legal advice.

### Background used in the first draft (not the final video)

The first draft used diagrams drawn with Pillow: a schematic ocean surface, underwater particles, a sunlight spectrum with red absorbed, and blue light scattered. No photo or AI-generated illustration was used in that draft. The on-screen notice was removed because the diagrams cannot be mistaken for photographs. That version is kept as `out_en/ocean_blue_kokoro.mp4`; it is not the final background.

## 6. Upload settings

| Setting | Value |
| --- | --- |
| Video language | English |
| Category | Education |
| License | Standard YouTube License |
| Comments | On, hold potentially inappropriate comments for review |
| "Altered or synthetic content" question | Answer yes when synthetic voice, AI images, or AI video are used. Declare exactly what was used. |
| Subtitles | English |
| Playlists | Maps and geography / History / Science and words / Money and work |

## 7. Reuse from the Japanese project

Allowed to reuse: research notes (facts, source URLs, dates) and diagram ideas.

Not reused without checking: scripts (they are in Japanese), narration audio, BGM files, thumbnails, channel art, and all `[TO BE SET]` credit lines.

Every reused source URL must be opened again and its wording confirmed before an English script is written.

## 8. Pre-production checklist

- [ ] Handle availability checked
- [ ] Voice chosen, license URL recorded
- [ ] Music chosen, license URL recorded
- [ ] Fonts chosen, license URL recorded
- [ ] Source URLs for the episode opened and confirmed
- [ ] Script follows the episode structure in section 3
- [ ] English subtitles made and checked against audio
- [ ] "Altered or synthetic content" answered truthfully
- [ ] Video watched end to end before upload
