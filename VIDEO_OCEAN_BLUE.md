# Produced Short — "Why does the ocean look blue?"

Status: built and machine-checked on 2026-11-24/25. Adopted: Kokoro `af_heart` voice (Apache 2.0) with FreeVideo ocean clips as background. The final file is `out_en/ocean_blue_fv.mp4`. Scheduled for 2026-11-25 21:30 JST at https://youtube.com/shorts/SEPK3A5vXOw?feature=share . Not reviewed in Google AI mode; still needs a full listen and a real-device smartphone check.

## Files

| File | What it is |
| --- | --- |
| `out_en/ocean_blue_fv.mp4` | Final draft, 1080x1920, 24 fps, 27.0 s, Kokoro voice, FreeVideo background, plain white captions, BGM |
| `build_fv.py` | Build script for the final FreeVideo-background version |
| `out_en/ocean_blue_kokoro.mp4` | Earlier Kokoro version with drawn-diagram background |
| `out_en/ocean_blue_piper.mp4` | Earlier Piper-voice draft |
| `out_en/ocean_blue_piper.wav` | Narration audio, Piper en_US-kristin-medium (public domain) |
| `out_en/ocean_blue_piper.srt` | English subtitles, timed from the actual audio timeline |
| `assets/tts/en_US-kristin-medium.onnx` | Voice model, public-domain LibriVox recordings |
| `build_short_piper.py` | Build script for the earlier Piper draft, not the adopted voice. Final video: see `build_fv.py:116-127` (audio, BGM, mix) |
| `out_en/ocean_blue.mp4` | Previous AvaNeural draft, kept only as a reference; license unconfirmed |
| `build_short.py` | Previous build script (edge-tts) |
| `out_en/frames/scene1.png` … `scene5.png` | Background diagrams drawn for the earlier draft, not the final background |
| `out_en/frames_piper.png` | Contact sheet of the earlier Piper draft |

## Script

1. You may have heard that the ocean is blue because it reflects the sky.
2. The surface does reflect the sky. But divers still see blue underwater.
3. NOAA says water absorbs the red part of sunlight. The blue part is left.
4. WHOI adds that particles in the water scatter the blue light back to our eyes.
5. So the sky is part of the answer, but not the whole answer. We did not check the original papers.

## Sources (opened and read on 2026-11-24)

- NOAA National Ocean Service, "Why is the ocean blue?" — https://oceanservice.noaa.gov/facts/oceanblue.html
- Woods Hole Oceanographic Institution, "Why is the ocean blue?" — https://www.whoi.edu/ocean-learning-hub/ocean-facts/why-is-the-ocean-blue/

## Verification performed

| Check | Result |
| --- | --- |
| Duration (ffprobe) | 27.0 s after shortening the tail silence from 4.5 s to 1.0 s (2026-11-25, user request). Below the 30 s spec; the shorter ending was prioritised. |
| Resolution / frame rate / codec | 1080x1920, 24 fps, H.264 + AAC |
| Full decode (`ffmpeg -f null -`) | exit 0, no errors |
| Loudness | Re-measured on 2026-11-25: -15.8 LUFS integrated (LRA 1.9 LU), -1.4 dBTP true peak. The build script specifies `loudnorm=I=-14:TP=-1.5:LRA=11`. The earlier record of -16.3 LUFS / -1.3 dBTP is superseded. |
| Background | Four existing FreeVideo clips from `assets/ocean2500/fv/`, reused. Each clip checked as a still: no text, no people. The description must say the background is AI-generated imagery. |
| Silence detection | Re-measured on 2026-11-25 on the final mp4: no silence events at -40/-30/-25/-20/-15 dB with `d=0.2`, because the BGM plays throughout. In the narration-only WAV, phrase gaps are 0.291–0.575 s and the tail gap is 1.280 s. The earlier note about 0.8–1.1 s gaps is superseded. |
| Contact sheet | Five scenes, captions fully visible, no overlap with headings; headings use Noto Sans JP Bold, matching the Japanese channel |
| Captions | On 2026-11-25 the burned-in captions were changed from full narration sentences to at most two keyword lines per scene, and the caption strip was raised to y1400–1660. Verified by frame extraction: all five scenes are two lines and do not overlap the heading. The previous file is `out_en/ocean_blue_fv_before_caption_fix.mp4`. Scene boundaries still use the actual audio scene starts. The `.srt` has not been updated and still contains the full narration. |
| Music license | Checked on https://maou.audio/ — commercial use OK, modification OK, no permission or report needed; credit "音楽：魔王魂" is sufficient |
| Voice license | Adopted voice is Kokoro `af_heart` (Kokoro-82M, Apache 2.0; license confirmed on the model card). The earlier Piper `en_US-kristin-medium` voice is public domain: LibriVox recordings, trained from scratch (MODEL_CARD confirmed). The earlier AvaNeural voice had no license document; that draft is kept only as a reference and must not be published. |
| Source pages | Opened and read; wording matches the script |

## Not performed

- Listening to the full narration by ear (not possible for this agent)
- Google AI mode video review — completed on 2026-11-25 with bsk; findings and our assessment are in `GOOGLE_AI_REVIEW.md`
- Smartphone display check on a real device — completed on 2026-11-25. The user confirmed that the bottom-left brand text and the two-line caption strip are both visible on a phone; no layout change is needed.
- Upload, scheduling, or any external publication

## Notes on the background

The final video `out_en/ocean_blue_fv.mp4` uses four existing FreeVideo AI-generated clips from `assets/ocean2500/fv/clip1-4.mp4` as the background. Each clip was checked as a still: no text, no people. The description states that the background is AI-generated imagery and not real footage. The user confirmed the generator as FlashML-org/FreeVideo on 2026-11-25; the license facts are recorded in `SPEC.md` section 5 and `channel.toml` `[background]`.

The earlier draft used diagrams drawn with Pillow: a schematic ocean surface, underwater particles, a sunlight spectrum with red absorbed, and blue light scattered back. No photo or AI-generated illustration was used in that draft. That version is `out_en/ocean_blue_kokoro.mp4`; it is not the final background. The on-screen notice "This is a diagram, not a real photo" was removed because the diagrams cannot be mistaken for photographs.

Headings and captions use Noto Sans JP, the same typeface family as the Japanese channel. BGM is 魔王魂 "Piano 12" (https://maou.audio/), the same track the Japanese channel uses.
