import unittest

from src.day_20.day_20 import *


class TestDay19(unittest.TestCase):
    def test_construct_tile(self):
        tile: Tile = Tile(3, ['abc', 'def', 'ghi'])
        self.assertEqual(tile.id, 3)
        self.assertEqual(tile.width, 3)
        self.assertEqual(tile.points, {(0, 0): 'a', (1, 0): 'b', (2, 0): 'c',
                                       (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                       (0, 2): 'g', (1, 2): 'h', (2, 2): 'i'})

    def test_parse_tile(self):
        tile_lines = ['Tile 2843:', 'abc', 'def', 'ghi']
        tile: Tile = parse_tile(tile_lines)
        self.assertEqual(tile.id, 2843)
        self.assertEqual(tile.points, {(0, 0): 'a', (1, 0): 'b', (2, 0): 'c',
                                       (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                       (0, 2): 'g', (1, 2): 'h', (2, 2): 'i'})

    def test_rotate_tile_right(self):
        tile: Tile = Tile(3, ['abc', 'def', 'ghi'])
        tile.rotate_right()

        self.assertEqual(tile.points, {(0, 0): 'g', (1, 0): 'd', (2, 0): 'a',
                                       (0, 1): 'h', (1, 1): 'e', (2, 1): 'b',
                                       (0, 2): 'i', (1, 2): 'f', (2, 2): 'c'})

    def test_flip_tile_horizontal(self):
        tile: Tile = Tile(3, ['abc', 'def', 'ghi'])
        tile.flip_horizontal()

        self.assertEqual(tile.points, {(0, 0): 'c', (1, 0): 'b', (2, 0): 'a',
                                       (0, 1): 'f', (1, 1): 'e', (2, 1): 'd',
                                       (0, 2): 'i', (1, 2): 'h', (2, 2): 'g'})

    def test_flip_tile_vertical(self):
        tile: Tile = Tile(3, ['abc', 'def', 'ghi'])
        tile.flip_vertical()

        self.assertEqual(tile.points, {(0, 0): 'g', (1, 0): 'h', (2, 0): 'i',
                                       (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                       (0, 2): 'a', (1, 2): 'b', (2, 2): 'c'})


if __name__ == '__main__':
    unittest.main()
