import unittest

from src.day_24.day_24 import *


class TestDay24(unittest.TestCase):
    def test_hex_equals(self):
        self.assertEqual(Hex(0, 1, -1), Hex(0, 1, -1))
        self.assertNotEqual(Hex(0, 1, -1), Hex(1, 0, -1))

    def test_hex_movement(self):
        origin: Hex = Hex(0, 0, 0)
        self.assertEqual(origin.east(), Hex(1, -1, 0))
        self.assertEqual(origin.west(), Hex(-1, 1, 0))
        self.assertEqual(origin.north_east(), Hex(1, 0, -1))
        self.assertEqual(origin.south_west(), Hex(-1, 0, 1))
        self.assertEqual(origin.north_west(), Hex(0, 1, -1))
        self.assertEqual(origin.south_east(), Hex(0, -1, 1))

    def test_circuits(self):
        origin: Hex = Hex(0, 0, 0)
        self.assertEqual(origin.east().west(), origin)
        self.assertEqual(origin.north_east().south_west(), origin)
        self.assertEqual(origin.south_east().north_west(), origin)
        self.assertEqual(origin.north_west().west().south_west().east().east(), origin)

    def test_split_instruction(self):
        self.assertEqual(split_instruction('esenee'), ['e', 'se', 'ne', 'e'])
        self.assertEqual(split_instruction('nwwswee'), ['nw', 'w', 'sw', 'e', 'e'])

    def test_line_to_hex(self):
        self.assertEqual(line_to_hex('esew'), Hex(0, 0, 0).south_east())
        self.assertEqual(line_to_hex('nwwswee'), Hex(0, 0, 0))
        self.assertEqual(line_to_hex('nwwswee'), Hex(0, 0, 0))
        self.assertEqual(line_to_hex('esenee'), Hex(3, -3, 0))

    def test_part_a(self):
        self.assertEqual(part_a('day_24_example.txt'), 10)

    def test_flip_black_tile(self):
        self.assertEqual(flip_tile(True, 0), False)
        self.assertEqual(flip_tile(True, 1), True)
        self.assertEqual(flip_tile(True, 2), True)
        self.assertEqual(flip_tile(True, 3), False)
        self.assertEqual(flip_tile(True, 4), False)
        self.assertEqual(flip_tile(True, 5), False)
        self.assertEqual(flip_tile(True, 6), False)

    def test_flip_white_tile(self):
        self.assertEqual(flip_tile(False, 0), False)
        self.assertEqual(flip_tile(False, 1), False)
        self.assertEqual(flip_tile(False, 2), True)
        self.assertEqual(flip_tile(False, 3), False)
        self.assertEqual(flip_tile(False, 4), False)
        self.assertEqual(flip_tile(False, 5), False)
        self.assertEqual(flip_tile(False, 6), False)

    def test_iterate_tiles(self):
        black_tiles = parse_black_tiles('day_24_example.txt')
        day_1 = iterate_tiles(black_tiles)
        day_2 = iterate_tiles(day_1)
        self.assertEqual(len(day_1), 15)
        self.assertEqual(len(day_2), 12)

    def test_part_b(self):
        self.assertEqual(part_b('day_24_example.txt'), 2208)


if __name__ == '__main__':
    unittest.main()
