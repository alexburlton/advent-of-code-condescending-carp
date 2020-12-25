import unittest

from src.day_25.day_25 import *


class TestDay25(unittest.TestCase):
    def test_find_loop_number(self):
        self.assertEqual(find_loop_number(5764801), 8)
        self.assertEqual(find_loop_number(17807724), 11)

    def test_part_a(self):
        self.assertEqual(part_a('day_25_example.txt'), 14897079)


if __name__ == '__main__':
    unittest.main()
