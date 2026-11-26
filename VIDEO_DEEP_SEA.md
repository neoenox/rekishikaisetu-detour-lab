# Produced Short — "Uncovering What Really Happens at the Deepest and Darkest Point of the Ocean"

Status: built, machine-checked and re-built on 2026-11-25. The replacement upload is scheduled for **2026-11-28 21:30 JST**. Fourth video for the channel. The earlier upload (`wGuQ63JNCLk`) had its schedule cancelled and remains private; its video ID for the replacement was not recorded because the Studio content list returned an error.

Files: `build_deepsea.py`, `out_en/deepsea_fv.mp4`, `out_en/deep_sea_script.md`, `out_en/deepsea.srt`, `out_en/deepsea_scene_starts.json`, `out_en/deepsea_description.md`, `out_en/deepsea_disclosure.md`.

Background: the first build reused the bright shallow-coral clips from `assets/ocean2500/fv/`, which contradicted the aphotic/hadal script. On the user's report it was rebuilt with three new FreeVideo / MiniMax H3 clips in `assets/ocean2500/deep/` (deep blue ocean, dim blue light shafts, near-black deep water). `build_deepsea.py` now points at that directory and uses clips 1, 2, 3, 3, 2 across the five scenes.

Sources opened and read on 2026-11-25: NOAA Ocean Exploration "How far does light travel in the ocean?" — https://oceanexplorer.noaa.gov/ocean-fact/light-distributed/ and NOAA National Ocean Service "5 Ocean Terms You May Not Know — But Should!" — https://oceanservice.noaa.gov/ocean/five-ocean-terms.html . Both are secondary explainer pages; the original papers were not checked. Claims use only the 1,000 m light limit and the roughly 6,000 m hadal-zone start that appear on those pages.

Verification: 35.042 s / 841 frames, 1080x1920 24 fps H.264 + AAC, full decode exit 0, -15.3 LUFS / -1.3 dBTP, no silence events in the final mp4, SRT starts match the scene-start JSON to the ms, all five scenes have two-line keyword captions with no heading overlap. The narration WAV has a 1.281 s tail gap, covered by BGM in the final file, as in the earlier videos.

Note: this is prepared as a Short for the launch burst. A longer form version remains a separate possibility if sources are added.
