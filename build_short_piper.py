"""Piper-voice variant of the ocean-blue Short.

Produces out_en/ocean_blue_piper.mp4 with the public-domain Piper voice
en_US-kristin-medium. Kept as a separate file so the AvaNeural version is not
overwritten.

Voice license: LibriVox recordings, public domain (trained from scratch).
  MODEL_CARD https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/kristin/medium/MODEL_CARD
  Piper engine GPL-3.0-or-later (code only, not distributed with this video).
  https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/COMMERCIAL_USE.md

Sources opened and read on 2026-11-24:
  NOAA  https://oceanservice.noaa.gov/facts/oceanblue.html
  WHOI  https://www.whoi.edu/ocean-learning-hub/ocean-facts/why-is-the-ocean-blue/
"""
import json
import math
import os
import subprocess
import wave
from pathlib import Path

from detour_ffmpeg import ffmpeg as _ffmpeg
FFMPEG = _ffmpeg()


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out_en"
FR = OUT / "frames"
OUT.mkdir(exist_ok=True)
FR.mkdir(exist_ok=True)



W, H = 1080, 1920
FPS = 24
SR = 24000

SCENES = [
    {
        "narr": "You may have heard that the ocean is blue because it reflects the sky.",
        "big": "Reflects the sky?",
        "sub": "The common explanation",
        "src": "NOAA / WHOI",
        "kind": "surface",
        "sec": 4.5,
    },
    {
        "narr": "The surface does reflect the sky. But divers still see blue underwater.",
        "big": "Blue underwater",
        "sub": "The sky is not there",
        "src": "WHOI",
        "kind": "underwater",
        "sec": 5.9,
    },
    {
        "narr": "NOAA says water absorbs the red part of sunlight. The blue part is left.",
        "big": "Red absorbed",
        "sub": "NOAA: water is a filter",
        "src": "NOAA",
        "kind": "absorb",
        "sec": 6.6,
    },
    {
        "narr": "WHOI adds that particles in the water scatter the blue light back to our eyes.",
        "big": "Blue scattered",
        "sub": "WHOI: particles scatter light",
        "src": "WHOI",
        "kind": "scatter",
        "sec": 5.8,
    },
    {
        "narr": "So the sky is part of the answer, but not the whole answer. We did not check the original papers.",
        "big": "What we did not check",
        "sub": "Sources: NOAA and WHOI explainers",
        "src": "NOAA / WHOI",
        "kind": "summary",
        "sec": 8.2,
    },
]

# ---------- audio ----------

VOICE_MODEL = ROOT / "assets" / "tts" / "en_US-kristin-medium.onnx"
_voice = None


def get_voice():
    global _voice
    if _voice is None:
        from piper import PiperVoice
        _voice = PiperVoice.load(str(VOICE_MODEL))
    return _voice


def synth_scene(text, wav_path):
    """Synthesize one scene directly to WAV. No word timings (plain captions)."""
    with wave.open(str(wav_path), "wb") as w:
        get_voice().synthesize_wav(text, w)


def make_audio():
    """Synthesize scenes with Piper and join into one narration WAV."""
    wavs = []
    for i, s in enumerate(SCENES, 1):
        wav = OUT / f"scene{i}_piper.wav"
        synth_scene(s["narr"], wav)
        wavs.append(wav)

    # Join with short gaps between scenes.
    frames, scene_starts = [], []
    acc = 0.0
    for i, p in enumerate(wavs):
        with wave.open(str(p), "rb") as w:
            rate = w.getframerate()
            dur = w.getnframes() / rate
            raw = w.readframes(w.getnframes())
            frames.append(raw)
        scene_starts.append(acc)
        acc += dur
        if i < len(wavs) - 1:
            gap = b"\x00\x00" * int(rate * 0.2)
            frames.append(gap)
            acc += 0.2

    joined = b"".join(frames) + b"\x00\x00" * int(rate * 4.5)
    out = OUT / "ocean_blue_piper.wav"
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(joined)

    with wave.open(str(out), "rb") as wf:
        audio_duration = wf.getnframes() / wf.getframerate()
    return out, scene_starts, audio_duration

# ---------- background diagrams (made for this video) ----------

def bg_gradient(top, bottom):
    from PIL import Image
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[k] * (1 - t) + bottom[k] * t) for k in range(3))
        for x in range(W):
            px[x, y] = c
    return img

def draw_frame(kind, big, sub, src, path, narration=""):
    from PIL import Image, ImageDraw, ImageFont
    palettes = {
        "surface": ((120, 185, 225), (12, 70, 130)),
        "underwater": ((20, 92, 160), (2, 25, 70)),
        "absorb": ((30, 105, 170), (3, 30, 80)),
        "scatter": ((22, 110, 175), (2, 28, 75)),
        "summary": ((28, 95, 155), (3, 25, 70)),
    }
    top, bottom = palettes[kind]
    img = bg_gradient(top, bottom)
    d = ImageDraw.Draw(img, "RGBA")

    # wave lines (schematic, not a photo)
    if kind in ("surface", "underwater"):
        for k in range(9):
            y = 420 + k * 95
            pts = [(x, int(y + 12 * math.sin((x / 150.0) + k * 0.7))) for x in range(0, W, 12)]
            d.line(pts, fill=(255, 255, 255, 35), width=3)

    # sunlight spectrum + absorption
    if kind in ("absorb", "scatter", "summary"):
        colors = [(220, 60, 50), (235, 140, 45), (235, 220, 80), (80, 200, 110), (60, 130, 230), (110, 80, 210)]
        for i, c in enumerate(colors):
            x0 = 120 + i * 140
            d.rectangle([x0, 560, x0 + 120, 660], fill=c + (220,))
            if kind == "absorb" and i < 3:
                # red/orange/yellow absorbed: fade downward
                for t in range(8):
                    a = int(180 * (1 - t / 8))
                    d.rectangle([x0 + t * 4, 670 + t * 45, x0 + 120 - t * 4, 700 + t * 45], fill=c + (a,))
            if kind in ("scatter", "summary") and i >= 4:
                # blue/violet scattered back: arrows toward viewer
                for t in range(5):
                    yy = 690 + t * 70
                    d.line([(x0 + 60, yy), (x0 + 60, yy - 40)], fill=c + (200,), width=6)
                    d.ellipse([x0 + 50, yy - 60, x0 + 70, yy - 40], fill=c + (220,))

    if kind == "underwater":
        for i in range(30):
            x = (i * 197) % W
            y = 300 + (i * 311) % 1100
            r = 3 + (i % 4)
            d.ellipse([x - r, y - r, x + r, y + r], fill=(180, 225, 255, 90))

    # text panel (dark translucent) — this is a diagram, not a photo.
    d.rounded_rectangle([70, 110, W - 70, 430], radius=36, fill=(2, 18, 45, 205))
    # Same typeface family as the Japanese channel (Noto Sans JP).
    font_big = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", 76)
    font_big.set_variation_by_name("Bold")
    font_sub = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", 42)
    font_sub.set_variation_by_name("Regular")
    font_src = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", 32)
    font_src.set_variation_by_name("Regular")
    d.text((110, 150), big, font=font_big, fill=(255, 255, 255, 255))
    d.text((110, 270), sub, font=font_sub, fill=(205, 230, 255, 255))
    d.text((110, 350), src, font=font_src, fill=(160, 200, 240, 255))

    # Caption strip and credits are drawn per frame in draw_caption_frame().
    img.save(path)

# ---------- karaoke caption frames ----------

def wrap_words(words, width=30):
    """Wrap word records into lines of at most `width` characters."""
    lines, cur = [], []
    for w in words:
        candidate = " ".join([x["text"] for x in cur + [w]])
        if len(candidate) > width and cur:
            lines.append(cur)
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(cur)
    return lines


def draw_caption_frame(bg_path, narration, path):
    """Draw one plain-white caption strip for a whole scene (no word highlight)."""
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open(bg_path).convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle([0, 1480, W, H], fill=(0, 10, 30, 215))

    font_cap = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", 58)
    font_cap.set_variation_by_name("Medium")
    font_src = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", 32)
    font_src.set_variation_by_name("Regular")

    # Wrap on words only; no per-word color change.
    words = narration.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > 30 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)

    y = 1515
    for line in lines[:4]:
        box = d.textbbox((0, 0), line, font=font_cap)
        x = (W - (box[2] - box[0])) / 2 - box[0]
        d.text((x, y), line, font=font_cap, fill=(255, 255, 255, 255))
        y += 66

    d.text((70, 1875), "THE DETOUR LAB", font=font_src, fill=(255, 255, 255, 255))
    img.convert("RGB").save(path)


def build_caption_frames(scene_starts, audio_duration):
    """One caption image per scene, displayed for that scene's actual audio span."""
    entries = []
    starts = list(scene_starts) + [audio_duration]
    for i, s in enumerate(SCENES, 1):
        bg = FR / f"scene{i}.png"
        out = FR / f"scene{i}_caption.png"
        draw_caption_frame(bg, s["narr"], out)
        dur = starts[i] - starts[i - 1]
        entries.append((out, dur))
    return entries

# ---------- subtitles ----------

def srt_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int((sec - int(sec)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def split_caption(text, width=34):
    """Wrap a caption into at most two short lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return "\\N".join(lines[:3])

def write_srt(path, scene_starts, audio_duration):
    """Subtitle timing follows the actual audio timeline, with real newlines."""
    out = []
    starts = list(scene_starts) + [audio_duration]
    for i, s in enumerate(SCENES):
        a = starts[i]
        b = starts[i + 1]
        text = split_caption(s["narr"]).replace("\\N", "\n")
        out += [str(i + 1), f"{srt_time(a)} --> {srt_time(b - 0.1)}", text, ""]
    path.write_text("\n".join(out), encoding="utf8")

# ---------- video ----------

def build_video(audio, srt, scene_starts, audio_duration):
    # One plain-caption still per scene, timed from the actual audio timeline.
    entries = build_caption_frames(scene_starts, audio_duration)
    concat = OUT / "img_list.txt"
    lines = []
    for path, dur in entries:
        lines.append(f"file '{path}'")
        lines.append(f"duration {dur:.3f}")
    # Repeat the last still so its duration is honored by the concat demuxer.
    lines.append(f"file '{entries[-1][0]}'")
    concat.write_text("\n".join(lines), encoding="utf8")

    # Captions are drawn into the PNG frames with Pillow, so no subtitle filter here.
    sub_filter = f"scale={W}:{H},fps={FPS}"
    bgm = ROOT / "assets" / "bgm_maou" / "maou_bgm_piano12.mp3"
    cmd = [
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
        "-i", str(audio),
        "-i", str(bgm),
        "-vf", sub_filter,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
        # Narration on top, quiet piano underneath (same track as the Japanese channel).
        "-filter_complex",
        "[1:a]volume=1.0[narr];[2:a]volume=0.10[bg];[narr][bg]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]",
        "-map", "0:v:0", "-map", "[mix]",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(OUT / "ocean_blue_piper.mp4"),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return OUT / "ocean_blue_piper.mp4"

def main():
    audio, scene_starts, audio_duration = make_audio()
    for i, s in enumerate(SCENES, 1):
        draw_frame(s["kind"], s["big"], s["sub"], s["src"], FR / f"scene{i}.png", s["narr"])
    srt = OUT / "ocean_blue_piper.srt"
    write_srt(srt, scene_starts, audio_duration)
    video = build_video(audio, srt, scene_starts, audio_duration)
    print("VIDEO", video)
    print("AUDIO", audio)
    print("SRT", srt)
    print("DURATION", audio_duration)

if __name__ == "__main__":
    main()
