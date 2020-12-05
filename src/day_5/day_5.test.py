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


if __name__ == '__main__':
    unittest.main()
