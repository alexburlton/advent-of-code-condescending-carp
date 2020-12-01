import unittest

from src.day_1.day_1 import *

test_report: List[int] = [1721, 979, 366, 299, 675, 1456]


class TestDay1(unittest.TestCase):

    def test_sums_to_2020(self):
        self.assertTrue(sums_to_2020([2000, 15, 5]))
        self.assertTrue(sums_to_2020([1800, 220]))
        self.assertTrue(sums_to_2020([2020]))

        self.assertFalse(sums_to_2020([2000, 15, 6]))
        self.assertFalse(sums_to_2020([2000, 15, 4]))
        self.assertFalse(sums_to_2020([2019]))

    def test_part_a(self):
        self.assertEqual(get_expense_report_product(test_report, 2), 514579)

    def test_part_b(self):
        self.assertEqual(get_expense_report_product(test_report, 3), 241861950)


if __name__ == '__main__':
    unittest.main()
