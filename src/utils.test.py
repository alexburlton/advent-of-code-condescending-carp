import unittest

from src.utils import *


class TestUtils(unittest.TestCase):

    def test_count_where(self):
        def is_zero(x: int) -> bool:
            return x == 0

        self.assertEqual(count_where(is_zero, [0, 1, 0, 0]), 3)
        self.assertEqual(count_where(is_zero, [1, 2, 3, 4]), 0)
        self.assertEqual(count_where(is_zero, [100, 20, 5, 0]), 1)


if __name__ == '__main__':
    unittest.main()
