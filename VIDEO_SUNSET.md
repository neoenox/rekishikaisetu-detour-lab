# Produced Short — "Why sunsets turn red instead of the usual blue sky"

Status: built and machine-checked on 2026-11-25. Uploaded to YouTube the same day and scheduled for **2026-11-26 21:30 JST** (video ID `TIZC-zpz4Xc`, URL https://youtube.com/shorts/TIZC-zpz4Xc ). Second video for the channel, following the same format as `VIDEO_OCEAN_BLUE.md`.

## Files

| File | What it is |
| --- | --- |
| `out_en/sunset_fv.mp4` | Final draft, 1080x1920, 24 fps, 31.000 s, Kokoro `af_heart`, FreeVideo background, two-line keyword captions, BGM |
| `build_sunset.py` | Reproducible build script (narration, overlays, background, audio mix) |
| `out_en/sunset_script.md` | Script, sources, keyword caption plan |
| `out_en/sunset_description.md` | Description draft |
| `out_en/sunset_disclosure.md` | AI-use declaration text |
| `out_en/sunset.srt` | Full narration subtitles, timings from the actual audio |
| `out_en/sunset_narration.wav` | Narration audio |
| `out_en/sunset_scene_starts.json` | Actual scene start times |
| `out_en/sunset_overlay1.png` … `5.png` | Caption/heading layers |
| `out_en/sunset_scene1.mp4` … `5.mp4` | Scene clips before concat |

## Script

1. The same white sunlight gives a blue daytime sky and a red sunset.
2. NASA says the path through air gets much longer near the horizon.
3. NASA says air molecules — tiny bits of air — scatter short blue waves most.
4. NOAA says a long path scatters blue away, leaving more red and yellow.
5. We can say air changes the light. We cannot say yet how much dust matters. We did not check the original paper. Same sun, two colors.

## Sources (opened and read on 2026-11-25)

- NASA Space Place, "Why Is the Sky Blue?" — https://spaceplace.nasa.gov/blue-sky/en/
- NOAA Global Monitoring Laboratory, "Red Sky" — https://gml.noaa.gov/grad/about/redsky/

Both are secondary explainer pages. The original papers were not checked; the script says so with the fixed wording from SPEC section 4.

## Verification performed

| Check | Result |
| --- | --- |
| Duration | 31.000 s / 744 frames — PASS against the 30–45 s Shorts spec |
| Resolution / frame rate / codec | 1080x1920 (9:16), 24 fps, H.264 High + AAC LC — PASS |
| Full decode | `ffmpeg -f null -` exit 0, stderr empty — PASS |
| Loudness | -15.4 LUFS integrated (LRA 1.5 LU), -1.3 dBTP — in line with video 1 |
| Silence | No events at -40 dB / -25 dB with `d=0.2` in either the final mp4 or the narration WAV — PASS |
| SRT timings | Starts 0 / 4.873 / 9.469 / 15.131 / 20.176 s match `sunset_scene_starts.json` to the ms; last cue ends at 30.923 s — PASS |
| Scene cuts | 4.875 / 9.458 / 15.125 / 20.167 s, at most 11 ms from the audio scene starts — PASS |
| Captions | Five scenes, all two lines, keywords only, no narration sentences. Heading y110–430, caption strip y1400–1660, no overlap — PASS |
| Safe-area note | Some second lines reach y1582 and one right edge reaches x952, 8–9 px / 2 px past the desktop estimate. The user confirmed on a real phone for video 1 that the same layout is visible; no real-device check for this video yet |

## Known differences from video 1

- The SRT contains the full narration while the burned-in captions are keywords. Per SPEC section 2 this is the intended definition: the SRT is the accessibility transcript timed to the audio, and it is not uploaded as a visible subtitle track.
- The build reuses the existing FreeVideo clips. The sunset clip is now the subject rather than a mismatch.

## Not performed

- Publication will happen at the scheduled time; nothing else is pending
- Human listen-through by ear
- Real-device check for this specific video
