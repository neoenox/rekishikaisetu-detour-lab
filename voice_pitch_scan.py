"""Temporary helper: synthesize one sentence with several Kokoro voices for pitch comparison."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
import build_short_kokoro as b

b.SPEED = 0.88
TEXT = b.SCENES[0]["narr"]
NAMES = [
    "af_aoede",
    "af_bella",
    "af_nicole",
    "af_river",
    "af_sarah",
    "bf_alice",
    "bf_emma",
    "bf_isabella",
]

for name in NAMES:
    b.VOICE_NAME = name
    out = ROOT / "out_en" / f"voice_test_kokoro_{name}.wav"
    b.synth_scene(TEXT, out)
    print(name, "OK", out, flush=True)
