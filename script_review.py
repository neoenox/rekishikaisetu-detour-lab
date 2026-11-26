"""台本（SAMPLE_SCRIPT.md など）を ChatGPT / Google AI にレビューさせる。

usage:
  python script_review.py ocean_blue                 # SAMPLE_SCRIPT.md を送る
  python script_review.py ocean_blue --dry-run
  python script_review.py ocean_blue --path other.md --target chatgpt
"""
import argparse
import os
from pathlib import Path

os.environ.setdefault('PYTHONIOENCODING', 'utf8')

from ytkit.review.__main__ import main

ROOT = Path(__file__).resolve().parent


def run():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('slug')
    ap.add_argument('--path', default=str(ROOT / 'SAMPLE_SCRIPT.md'))
    args, rest = ap.parse_known_args()
    return main(['run', args.path, '--adapter', 'markdown', '--project',
                 'rekishikaisetu-detour-lab', '--slug', args.slug,
                 '--out-dir', str(ROOT / 'out_en')] + rest)


if __name__ == '__main__':
    raise SystemExit(run())
