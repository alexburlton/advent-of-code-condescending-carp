import unittest

from src.day_5.day_5 import *

test_report: List[int] = [1721, 979, 366, 299, 675, 1456]


class TestDay5(unittest.TestCase):

    def test_get_row_number(self):
        self.assertEqual(get_row_number('FBFBBFF'), 44)
        self.assertEqual(get_row_number('BFFFBBF'), 70)
        self.assertEqual(get_row_number('FFFBBBF'), 14)
        self.assertEqual(get_row_number('BBFFBBF'), 102)

    def test_get_column_number(self):
        self.assertEqual(get_column_number('RLR'), 5)
        self.assertEqual(get_column_number('RRR'), 7)
        self.assertEqual(get_column_number('RLL'), 4)

    def test_get_seat_id(self):
        self.assertEqual(get_seat_id('FBFBBFFRLR'), 357)
        self.assertEqual(get_seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_seat_id('BBFFBBFRLL'), 820)

    def test_get_missing_seat(self):
        self.assertEqual(get_missing_seat(2, 4), 3)

        self.assertEqual(get_missing_seat(2, 5), None)
        self.assertEqual(get_missing_seat(2, 3), None)

    def test_find_missing_seat(self):
        self.assertEqual(find_missing_seat([1, 2, 3, 4, 6]), 5)
        self.assertEqual(find_missing_seat([2, 3, 6, 1, 4]), 5)
        self.assertEqual(find_missing_seat([1, 4, 7, 9]), 8)
        self.assertEqual(find_missing_seat([3, 10, 4, 9, 7]), 8)


if __name__ == '__main__':
    unittest.main()
