"""Regression tests for output overwrite protection."""
import tempfile
import unittest
from pathlib import Path

from output_guard import ensure_output_available


class OutputGuardTests(unittest.TestCase):
    def test_missing_output_is_allowed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "video.mp4"
            ensure_output_available(path)
            self.assertFalse(path.exists())

    def test_existing_output_is_refused_and_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "video.mp4"
            path.write_bytes(b"original")
            with self.assertRaises(FileExistsError):
                ensure_output_available(path)
            self.assertEqual(path.read_bytes(), b"original")


if __name__ == "__main__":
    unittest.main()
