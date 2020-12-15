import unittest

from src.day_15.day_15 import *


class TestDay15(unittest.TestCase):
    def test_the_thing(self):
        self.assertEqual(play_until_nth_turn('0,3,6', 4), 0)
        self.assertEqual(play_until_nth_turn('0,3,6', 5), 3)
        self.assertEqual(play_until_nth_turn('0,3,6', 6), 3)
        self.assertEqual(play_until_nth_turn('0,3,6', 7), 1)
        self.assertEqual(play_until_nth_turn('0,3,6', 2020), 436)
        self.assertEqual(play_until_nth_turn('1,3,2', 2020), 1)
        self.assertEqual(play_until_nth_turn('2,1,3', 2020), 10)
        self.assertEqual(play_until_nth_turn('1,2,3', 2020), 27)
        self.assertEqual(play_until_nth_turn('2,3,1', 2020), 78)
        self.assertEqual(play_until_nth_turn('3,2,1', 2020), 438)
        self.assertEqual(play_until_nth_turn('3,1,2', 2020), 1836)

    def test_the_thing_bigger(self):
        self.assertEqual(play_until_nth_turn('0,3,6', 30000000), 175594)


if __name__ == '__main__':
    unittest.main()
