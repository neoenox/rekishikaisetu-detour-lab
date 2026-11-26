"""完成動画を Google AI にレビューさせる。

usage:
  python script_review_video.py out_en/ocean_blue_fv.mp4 --slug ocean_blue
  python script_review_video.py out_en/ocean_blue_fv.mp4 --dry-run
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.environ.setdefault('PYTHONIOENCODING', 'utf8')

from ytkit.review.__main__ import main

if __name__ == '__main__':
    argv = sys.argv[1:]
    if argv and not argv[0].startswith('-'):
        argv = ['video', argv[0]] + argv[1:]
        if '--out-dir' not in argv:
            argv += ['--out-dir', str(ROOT / 'out_en')]
    raise SystemExit(main(argv))
