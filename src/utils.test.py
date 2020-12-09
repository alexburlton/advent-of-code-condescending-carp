import unittest

from src.utils import *


class TestUtils(unittest.TestCase):

    def test_count_where(self):
        def is_zero(x: int) -> bool:
            return x == 0

        self.assertEqual(count_where(is_zero, [0, 1, 0, 0]), 3)
        self.assertEqual(count_where(is_zero, [1, 2, 3, 4]), 0)
        self.assertEqual(count_where(is_zero, [100, 20, 5, 0]), 1)

    def test_windowed_2(self):
        result = windowed([1, 2, 5, 10], 2)
        self.assertEqual(result, [(1, 2), (2, 5), (5, 10)])

    def test_windowed_3(self):
        result = windowed([1, 3, 6, 10, 15], 3)
        self.assertEqual(result, [(1, 3, 6), (3, 6, 10), (6, 10, 15)])


if __name__ == '__main__':
    unittest.main()
