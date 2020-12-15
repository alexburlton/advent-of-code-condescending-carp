import unittest

from src.day_13.day_13 import *


class TestDay12(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(part_a(['939', '7,13,x,x,59,x,31,19']), 295)

    def test_part_b(self):
        self.assertEqual(part_b('17,x,13,19'), 3417)
        self.assertEqual(part_b('67,7,59,61'), 754018)
        self.assertEqual(part_b('67,x,7,59,61'), 779210)
        self.assertEqual(part_b('67,7,x,59,61'), 1261476)
        self.assertEqual(part_b('1789,37,47,1889'), 1202161486)


if __name__ == '__main__':
    unittest.main()
