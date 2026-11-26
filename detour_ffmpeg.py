"""The Detour Lab の ffmpeg 探索。実装は ytkit.ffmpeg_tools に置く。

環境変数 FFMPEG → PATH → このプロジェクトで使ってきた既存パスの順で探す。
各 build_*.py にあったハードコードをここに集約した。
"""
from ytkit.ffmpeg_tools import find_ffmpeg

# 古いビルドスクリプトが使っていたパス。PATH に ffmpeg が無い環境の保険。
FALLBACK = (
    r"C:\Users\neoen\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\tools\ffmpeg\bin\ffmpeg.exe",
    r"C:\Users\neoen\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe",
    r"E:\rekishikaisetu-honnoji\tools\ffmpeg\bin\ffmpeg.exe",
)


def ffmpeg():
    """ffmpeg の実行ファイルを返す。見つからなければ FFmpegNotFound。"""
    return find_ffmpeg(fallback=FALLBACK)
