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

    def test_read_coordinate_grid(self):
        input_lines = ['#.', '@@', '..']
        grid = parse_coordinate_grid(input_lines)
        self.assertEqual(grid[(0, 0)], '#')
        self.assertEqual(grid[(1, 0)], '.')
        self.assertEqual(grid[(0, 1)], '@')
        self.assertEqual(grid[(1, 1)], '@')
        self.assertEqual(grid[(0, 2)], '.')
        self.assertEqual(grid[(1, 2)], '.')

    def test_add_points(self):
        self.assertEqual(add_points((0, 1), (5, 10)), (5, 11))

    def test_get_adjacents(self):
        input_lines = ['abc', 'def', 'ghi']
        grid = parse_coordinate_grid(input_lines)
        self.assert_equal_any_order(get_adjacents(grid, (0, 0)), ['b', 'd', 'e'])
        self.assert_equal_any_order(get_adjacents(grid, (1, 0)), ['a', 'c', 'd', 'e', 'f'])
        self.assert_equal_any_order(get_adjacents(grid, (2, 0)), ['b', 'e', 'f'])

        self.assert_equal_any_order(get_adjacents(grid, (0, 1)), ['a', 'b', 'e', 'g', 'h'])
        self.assert_equal_any_order(get_adjacents(grid, (1, 1)), ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i'])
        self.assert_equal_any_order(get_adjacents(grid, (2, 1)), ['b', 'c', 'e', 'h', 'i'])

        self.assert_equal_any_order(get_adjacents(grid, (0, 2)), ['d', 'e', 'h'])
        self.assert_equal_any_order(get_adjacents(grid, (1, 2)), ['d', 'e', 'f', 'g', 'i'])
        self.assert_equal_any_order(get_adjacents(grid, (2, 2)), ['e', 'f', 'h'])

    def assert_equal_any_order(self, list_a, list_b):
        self.assertEqual(sorted(list_a), sorted(list_b))


if __name__ == '__main__':
    unittest.main()
