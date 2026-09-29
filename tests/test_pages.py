import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pages import paginate  # noqa: E402


class PaginateTest(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(paginate(list(range(10)), 1, 3), [0, 1, 2])

    def test_last_partial_page(self):
        self.assertEqual(paginate(list(range(10)), 4, 3), [9])

    def test_rejects_page_zero(self):
        with self.assertRaises(ValueError):
            paginate([1], 0, 3)


if __name__ == "__main__":
    unittest.main()
