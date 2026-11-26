"""Build the second Short: why sunsets turn red instead of blue.

Reuses the Kokoro af_heart narration path, the FreeVideo background clips and
the two-line keyword caption layout from build_fv.py.

Sources opened and read on 2026-11-25:
  NASA Space Place  https://spaceplace.nasa.gov/blue-sky/en/
  NOAA GML          https://gml.noaa.gov/grad/about/redsky/
Script: out_en/sunset_script.md
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



MODEL = ROOT / "assets" / "tts" / "kokoro" / "kokoro-v1.0.int8.onnx"
VOICES = ROOT / "assets" / "tts" / "kokoro" / "voices-v1.0.bin"
VOICE_NAME = "af_heart"
LANG = "en-us"
SPEED = 0.88

SCENES = [
    {
        "narr": "The same white sunlight gives a blue daytime sky and a red sunset.",
        "big": "White sunlight",
        "sub": "Blue noon, red sunset",
        "src": "NASA / NOAA",
        "clip": 1,
        "captions": ["White sunlight", "Blue daytime / red sunset"],
    },
    {
        "narr": "NASA says the path through air gets much longer near the horizon.",
        "big": "Longer path",
        "sub": "Near the horizon",
        "src": "NASA",
        "clip": 1,
        "captions": ["Longer path", "Near the horizon"],
    },
    {
        "narr": "NASA says air molecules — tiny bits of air — scatter short blue waves most.",
        "big": "Blue scattered",
        "sub": "Air molecules, tiny air bits",
        "src": "NASA",
        "clip": 3,
        "captions": ["Molecules = tiny air bits", "Blue scattered — NASA"],
    },
    {
        "narr": "NOAA says a long path scatters blue away, leaving more red and yellow.",
        "big": "Red + yellow",
        "sub": "A long path leaves them",
        "src": "NOAA",
        "clip": 4,
        "captions": ["Blue away", "Red + yellow through — NOAA"],
    },
    {
        "narr": "We can say air changes the light. We cannot say yet how much dust matters. We did not check the original paper. Same sun, two colors.",
        "big": "What we cannot say",
        "sub": "Dust: how much?",
        "src": "NASA / NOAA",
        "clip": 1,
        "captions": ["Can say / cannot say yet", "Original paper: not checked"],
    },
]


def font(size, variation):
    f = ImageFont.truetype("C:/Windows/Fonts/NotoSansJP-VF.ttf", size)
    f.set_variation_by_name(variation)
    return f


def make_overlay(scene, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([70, 110, W - 70, 430], radius=36, fill=(2, 18, 45, 205))
    d.text((110, 150), scene["big"], font=font(76, "Bold"), fill=(255, 255, 255, 255))
    d.text((110, 270), scene["sub"], font=font(42, "Regular"), fill=(205, 230, 255, 255))
    d.text((110, 350), scene["src"], font=font(32, "Regular"), fill=(160, 200, 240, 255))
    d.rectangle([0, 1400, W, 1660], fill=(0, 10, 30, 215))
    y = 1440
    for line in scene["captions"][:2]:
        box = d.textbbox((0, 0), line, font=font(58, "Medium"))
        x = (W - (box[2] - box[0])) / 2 - box[0]
        d.text((x, y), line, font=font(58, "Medium"), fill=(255, 255, 255, 255))
        y += 72
    d.text((70, 1875), "THE DETOUR LAB", font=font(32, "Regular"), fill=(255, 255, 255, 255))
    img.save(path)


def synth_scene(text, wav_path):
    import soundfile as sf
    from kokoro_onnx import Kokoro
    samples, sr = Kokoro(str(MODEL), str(VOICES)).create(
        text, voice=VOICE_NAME, lang=LANG, speed=SPEED
    )
    sf.write(str(wav_path), samples, sr, subtype="PCM_16")


def make_audio():
    wavs = []
    for i, scene in enumerate(SCENES, 1):
        wav = OUT / f"sunset_scene{i}.wav"
        synth_scene(scene["narr"], wav)
        wavs.append(wav)
    frames, starts = [], []
    acc = 0.0
    for i, p in enumerate(wavs):
        with wave.open(str(p), "rb") as w:
            rate = w.getframerate()
            dur = w.getnframes() / rate
            frames.append(w.readframes(w.getnframes()))
        starts.append(acc)
        acc += dur
        if i < len(wavs) - 1:
            frames.append(b"\x00\x00" * int(rate * 0.2))
            acc += 0.2
    frames.append(b"\x00\x00" * int(rate * 1.0))
    audio = OUT / "sunset_narration.wav"
    with wave.open(str(audio), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(b"".join(frames))
    with wave.open(str(audio), "rb") as wf:
        duration = wf.getnframes() / wf.getframerate()
    (OUT / "sunset_scene_starts.json").write_text(
        json.dumps({"scene_starts": starts, "audio_duration": duration}), encoding="utf8"
    )
    return audio, starts, duration


def stamp(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def make_srt(starts, duration):
    ends = [starts[i + 1] - 0.1 for i in range(4)] + [duration - 0.1]
    lines = []
    for i, scene in enumerate(SCENES):
        lines += [str(i + 1), f"{stamp(starts[i])} --> {stamp(ends[i])}", scene["narr"], ""]
    (OUT / "sunset.srt").write_text("\n".join(lines), encoding="utf8")


def build():
    audio, starts, duration = make_audio()
    make_srt(starts, duration)
    ends = list(starts[1:]) + [duration]
    clips = []
    for i, scene in enumerate(SCENES):
        overlay = OUT / f"sunset_overlay{i + 1}.png"
        make_overlay(scene, overlay)
        clip = FVF / f"clip{scene['clip']}.mp4"
        out_clip = OUT / f"sunset_scene{i + 1}.mp4"
        dur = ends[i] - starts[i]
        cmd = [
            FFMPEG, "-y", "-stream_loop", "-1", "-i", str(clip),
            "-i", str(overlay),
            "-filter_complex",
            f"[0:v]scale={W}:{H},fps={FPS},trim=duration={dur:.3f}[bg];[bg][1:v]overlay=0:0[v]",
            "-map", "[v]", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
            str(out_clip),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        clips.append(f"file '{out_clip}'")
    (OUT / "sunset_list.txt").write_text("\n".join(clips), encoding="utf8")
    bgm = ROOT / "assets" / "bgm_maou" / "maou_bgm_piano12.mp3"
    final = OUT / "sunset_fv.mp4"
    cmd = [
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(OUT / "sunset_list.txt"),
        "-i", str(audio), "-i", str(bgm),
        "-filter_complex",
        "[1:a]volume=1.0[narr];[2:a]volume=0.10[bg];[narr][bg]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]",
        "-map", "0:v:0", "-map", "[mix]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(final),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print("VIDEO", final)


if __name__ == "__main__":
    build()
