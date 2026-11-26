"""Build the ocean-blue Short with FreeVideo clips as the background.

Reuses the Kokoro narration already built in out_en/ocean_blue_kokoro.wav and
its scene timings. Replaces the drawn diagrams with FreeVideo clips from
../assets/ocean2500/fv/, with the heading panel and caption strip overlaid as
transparent PNGs.

Output: out_en/ocean_blue_fv.mp4 (does not overwrite any previous video).
"""
import json
import subprocess
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from detour_ffmpeg import ffmpeg as _ffmpeg
FFMPEG = _ffmpeg()

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out_en"
FVF = ROOT / "assets" / "ocean2500" / "fv"
W, H, FPS = 1080, 1920, 24


# Each scene carries at most two keyword caption lines. No narration sentence
# is shown on screen (SPEC.md section 2).
SCENES = [
    ("Reflects the sky?", "The common explanation", "NOAA / WHOI", 1,
     ["Common belief", "Sky reflection"]),
    ("Blue underwater", "The sky is not there", "WHOI", 3,
     ["Underwater", "Still blue"]),
    ("Red absorbed", "NOAA: water is a filter", "NOAA", 2,
     ["NOAA", "Red absorbed"]),
    ("Blue scattered", "WHOI: particles scatter light", "WHOI", 4,
     ["WHOI", "Particles scatter"]),
    ("What we did not check", "Sources: NOAA and WHOI explainers", "NOAA / WHOI", 1,
     ["We can say", "Papers not checked"]),
]
NARRATIONS = [
    "You may have heard that the ocean is blue because it reflects the sky.",
    "The surface does reflect the sky. But divers still see blue underwater.",
    "NOAA says water absorbs the red part of sunlight. The blue part is left.",
    "WHOI adds that particles in the water scatter the blue light back to our eyes.",
    "So the sky is part of the answer, but not the whole answer. We did not check the original papers.",
]


def font(size, variation):
    f = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", size)
    f.set_variation_by_name(variation)
    return f


def wrap(text, width=30):
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines[:4]


def make_overlay(big, sub, src, captions, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    # Heading panel
    d.rounded_rectangle([70, 110, W - 70, 430], radius=36, fill=(2, 18, 45, 205))
    d.text((110, 150), big, font=font(76, "Bold"), fill=(255, 255, 255, 255))
    d.text((110, 270), sub, font=font(42, "Regular"), fill=(205, 230, 255, 255))
    d.text((110, 350), src, font=font(32, "Regular"), fill=(160, 200, 240, 255))
    # Caption strip: keywords only, at most two lines, raised away from the
    # bottom Shorts UI area.
    d.rectangle([0, 1400, W, 1660], fill=(0, 10, 30, 215))
    y = 1440
    for line in captions[:2]:
        box = d.textbbox((0, 0), line, font=font(58, "Medium"))
        x = (W - (box[2] - box[0])) / 2 - box[0]
        d.text((x, y), line, font=font(58, "Medium"), fill=(255, 255, 255, 255))
        y += 72
    d.text((70, 1875), "THE DETOUR LAB", font=font(32, "Regular"), fill=(255, 255, 255, 255))
    img.save(path)


def read_timings():
    """Read scene starts from the Kokoro build by re-deriving from its WAV parts."""
    # The Kokoro script prints them, but to keep this script standalone we store
    # them in a JSON next to the audio when available.
    p = OUT / "kokoro_scene_starts.json"
    if p.exists():
        d = json.loads(p.read_text(encoding="utf8"))
        return d["scene_starts"], d["audio_duration"]
    raise RuntimeError("kokoro_scene_starts.json missing; run build_short_kokoro.py once with timing export")


def build():
    starts, audio_duration = read_timings()
    ends = list(starts[1:]) + [audio_duration]
    dur_list = [ends[i] - starts[i] for i in range(5)]
    concat = OUT / "fv_list.txt"
    lines = []
    for i, (big, sub, src, clipno, captions) in enumerate(SCENES):
        overlay = OUT / f"fv_overlay{i + 1}.png"
        make_overlay(big, sub, src, captions, overlay)
        clip = FVF / f"clip{clipno}.mp4"
        scene_out = OUT / f"fv_scene{i + 1}.mp4"
        # Trim the 7.3 s clip to this scene's duration; loop if the scene is longer.
        cmd = [
            FFMPEG, "-y", "-stream_loop", "-1", "-i", str(clip),
            "-i", str(overlay),
            "-filter_complex", f"[0:v]scale={W}:{H},fps={FPS},trim=duration={dur_list[i]:.3f}[bg];[bg][1:v]overlay=0:0[v]",
            "-map", "[v]", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
            str(scene_out),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        lines.append(f"file '{scene_out}'")
    concat.write_text("\n".join(lines), encoding="utf8")

    audio = OUT / "ocean_blue_kokoro.wav"
    bgm = ROOT / "assets" / "bgm_maou" / "maou_bgm_piano12.mp3"
    final = OUT / "ocean_blue_fv.mp4"
    cmd = [
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
        "-i", str(audio), "-i", str(bgm),
        "-filter_complex",
        "[1:a]volume=1.0[narr];[2:a]volume=0.10[bg];[narr][bg]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]",
        "-map", "0:v:0", "-map", "[mix]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", str(final),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print("VIDEO", final)


if __name__ == "__main__":
    build()
