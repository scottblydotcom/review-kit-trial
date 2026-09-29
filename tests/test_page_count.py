import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pages import page_count  # noqa: E402


class PageCountTest(unittest.TestCase):
    def test_exact_multiple(self):
        self.assertEqual(page_count(9, 3), 3)


if __name__ == "__main__":
    unittest.main()
