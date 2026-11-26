"""Temporary helper: estimate median F0 (Hz) of the Kokoro voice test WAVs with Praat."""
from pathlib import Path
import statistics

import parselmouth

ROOT = Path(__file__).resolve().parent / "out_en"
NAMES = [
    "af_heart",
    "af_alloy",
    "af_nova",
    "af_sky",
    "af_kore",
    "af_jessica",
    "bf_lily",
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
    path = ROOT / f"voice_test_kokoro_{name}.wav"
    snd = parselmouth.Sound(str(path))
    pitch = snd.to_pitch_ac(pitch_floor=80, pitch_ceiling=500, very_accurate=True)
    values = [f for f in pitch.selected_array["frequency"] if 0 < f < 500]
    if not values:
        print(f"{name:12s} no voiced frames")
        continue
    values.sort()
    q1 = values[len(values) // 4]
    med = statistics.median(values)
    q3 = values[(3 * len(values)) // 4]
    print(f"{name:12s} frames={len(values):4d} q1={q1:6.1f} median={med:6.1f} q3={q3:6.1f} Hz")
