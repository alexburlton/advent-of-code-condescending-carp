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

    def test_process_instruction_f(self):
        ship: Ship = Ship()
        ship.process_instruction("F10")
        self.assertEqual(ship.current_position, (10, 0))

    def test_process_instruction_e(self):
        ship: Ship = Ship()
        ship.process_instruction("E5")
        self.assertEqual(ship.current_position, (5, 0))

    def test_process_instruction_w(self):
        ship: Ship = Ship()
        ship.process_instruction("W5")
        self.assertEqual(ship.current_position, (-5, 0))

    def test_process_instruction_n(self):
        ship: Ship = Ship()
        ship.process_instruction("N5")
        self.assertEqual(ship.current_position, (0, 5))

    def test_process_instruction_s(self):
        ship: Ship = Ship()
        ship.process_instruction("S5")
        self.assertEqual(ship.current_position, (0, -5))

    def test_process_instruction_r(self):
        ship: Ship = Ship()
        ship.process_instruction("R180")
        self.assertEqual(ship.current_direction, (-1, 0))  # west
        ship.process_instruction("R90")
        self.assertEqual(ship.current_direction, (0, 1))  # north

    def test_process_instruction_l(self):
        ship: Ship = Ship()
        ship.process_instruction("L270")
        self.assertEqual(ship.current_direction, (0, -1))  # south
        ship.process_instruction("L90")
        self.assertEqual(ship.current_direction, (1, 0))  # east

    def test_process_instructions(self):
        instructions = ['F10', 'N3', 'F7', 'R90', 'F11']
        ship: Ship = Ship()
        ship.process_instructions(instructions)
        self.assertEqual(ship.current_position, (17, -8))
        self.assertEqual(ship.current_direction, (0, -1))  # south
        self.assertEqual(ship.manhatten_distance(), 25)


if __name__ == '__main__':
    unittest.main()
