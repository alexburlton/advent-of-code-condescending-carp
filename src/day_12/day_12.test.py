import unittest

from src.day_12.day_12 import *


class TestDay12(unittest.TestCase):
    def test_move_forward(self):
        ship: Ship = Ship()
        ship.move_forward(10)
        self.assertEqual(ship.current_position, (10, 0))
        ship.current_direction = (0, 1)
        ship.move_forward(5)
        self.assertEqual(ship.current_position, (10, 5))

    def test_move_north(self):
        ship: Ship = Ship()
        ship.move_north(7)
        self.assertEqual(ship.current_position, (0, 7))

    def test_move_south(self):
        ship: Ship = Ship()
        ship.move_south(10)
        self.assertEqual(ship.current_position, (0, -10))

    def test_move_east(self):
        ship: Ship = Ship()
        ship.move_east(8)
        self.assertEqual(ship.current_position, (8, 0))

    def test_move_west(self):
        ship: Ship = Ship()
        ship.move_west(5)
        self.assertEqual(ship.current_position, (-5, 0))

    def test_turn_right(self):
        ship: Ship = Ship()
        self.assertEqual(ship.current_direction, (1, 0))  # east
        ship.turn_right()
        self.assertEqual(ship.current_direction, (0, -1))  # south
        ship.turn_right()
        self.assertEqual(ship.current_direction, (-1, 0))  # west
        ship.turn_right()
        self.assertEqual(ship.current_direction, (0, 1))  # north
        ship.turn_right()
        self.assertEqual(ship.current_direction, (1, 0))  # east

    def test_turn_left(self):
        ship: Ship = Ship()
        self.assertEqual(ship.current_direction, (1, 0))  # east
        ship.turn_left()
        self.assertEqual(ship.current_direction, (0, 1))  # north
        ship.turn_left()
        self.assertEqual(ship.current_direction, (-1, 0))  # west
        ship.turn_left()
        self.assertEqual(ship.current_direction, (0, -1))  # south
        ship.turn_left()
        self.assertEqual(ship.current_direction, (1, 0))  # east

    def test_manhatten_distance(self):
        ship: Ship = Ship()
        self.assertEqual(ship.manhatten_distance(), 0)
        ship.current_position = (17, -8)
        self.assertEqual(ship.manhatten_distance(), 25)


if __name__ == '__main__':
    unittest.main()
