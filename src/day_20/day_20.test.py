import unittest

from src.day_20.day_20 import *


class TestDay19(unittest.TestCase):
    def test_construct_tile(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        self.assertEqual(tile.id, 3)
        self.assertEqual(tile.width, 3)
        self.assertEqual(tile.grid, {(0, 0): 'a', (1, 0): 'b', (2, 0): 'c',
                                     (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                     (0, 2): 'g', (1, 2): 'h', (2, 2): 'i'})

    def test_parse_tile(self):
        tile_lines = ['Tile 2843:', 'abc', 'def', 'ghi']
        tile: Tile = parse_tile(tile_lines)
        self.assertEqual(tile.id, 2843)
        self.assertEqual(tile.grid, {(0, 0): 'a', (1, 0): 'b', (2, 0): 'c',
                                     (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                     (0, 2): 'g', (1, 2): 'h', (2, 2): 'i'})

    def test_rotate_tile_right(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        rotated = tile.rotate_right()

        self.assertEqual(rotated.grid, {(0, 0): 'g', (1, 0): 'd', (2, 0): 'a',
                                        (0, 1): 'h', (1, 1): 'e', (2, 1): 'b',
                                        (0, 2): 'i', (1, 2): 'f', (2, 2): 'c'})

    def test_flip_tile_horizontal(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        flipped = tile.flip_horizontal()

        self.assertEqual(flipped.grid, {(0, 0): 'c', (1, 0): 'b', (2, 0): 'a',
                                        (0, 1): 'f', (1, 1): 'e', (2, 1): 'd',
                                        (0, 2): 'i', (1, 2): 'h', (2, 2): 'g'})

    def test_flip_tile_vertical(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        flipped = tile.flip_vertical()

        self.assertEqual(flipped.grid, {(0, 0): 'g', (1, 0): 'h', (2, 0): 'i',
                                        (0, 1): 'd', (1, 1): 'e', (2, 1): 'f',
                                        (0, 2): 'a', (1, 2): 'b', (2, 2): 'c'})

    def test_get_edges(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        edges = tile.get_edges()
        self.assertEqual(edges, {'abc', 'adg', 'cfi', 'ghi'})
        self.assertEqual(tile.top_edge(), 'abc')
        self.assertEqual(tile.bottom_edge(), 'ghi')
        self.assertEqual(tile.left_edge(), 'adg')
        self.assertEqual(tile.right_edge(), 'cfi')

    def test_get_edges_after_rotation(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        rotated = tile.rotate_right()
        edges = rotated.get_edges()
        self.assertEqual(edges, {'abc', 'gda', 'ifc', 'ghi'})

    def test_get_edges_after_vertical_flip(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        flipped = tile.flip_vertical()
        edges = flipped.get_edges()
        self.assertEqual(edges, {'abc', 'gda', 'ifc', 'ghi'})

    def test_get_edges_after_horizontal_flip(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        flipped = tile.flip_horizontal()
        edges = flipped.get_edges()
        self.assertEqual(edges, {'cba', 'cfi', 'ihg', 'adg'})

    def test_get_all_possible_edges(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        edges = tile.get_all_possible_edges()
        self.assertEqual(edges, {'abc', 'cba', 'adg', 'gda', 'ghi', 'ihg', 'cfi', 'ifc'})

    def test_classify_tiles(self):
        tile_groups = read_text_groups('day_20_example.txt')
        tiles: List[Tile] = [parse_tile(group.splitlines()) for group in tile_groups]
        corners, edges, inners = classify_tiles(tiles)
        self.assert_equal_any_order([corner.id for corner in corners], [1951, 3079, 2971, 1171])
        self.assert_equal_any_order([edge.id for edge in edges], [2311, 2729, 2473, 1489])
        self.assert_equal_any_order([inner.id for inner in inners], [1427])

    def test_update_matched_edges(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        tile.update_matched_edges({'abc', 'cba'})
        self.assertEqual(tile.matched_edges, {'abc'})

    def assert_equal_any_order(self, list_a, list_b):
        self.assertEqual(sorted(list_a), sorted(list_b))


if __name__ == '__main__':
    unittest.main()
