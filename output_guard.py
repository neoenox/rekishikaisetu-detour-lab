"""Guard generated outputs against accidental replacement."""
from pathlib import Path


def ensure_output_available(path: Path) -> None:
    """Raise when an output path already exists, without changing it."""
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {path}")
