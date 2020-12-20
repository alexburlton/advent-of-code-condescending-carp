import unittest

from src.day_20.day_20 import *
from utils import read_text_list, get_grid_lines


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
        self.assertEqual(tile.matched_edges, {'abc', 'cba'})

    def test_strip_border(self):
        tile: Tile = Tile.from_lines(3, ['abcd', 'efgh', 'ijkl', 'mnop'])
        stripped = tile.strip_border()
        self.assertEqual(stripped.grid, {(0, 0): 'f', (1, 0): 'g',
                                         (0, 1): 'j', (1, 1): 'k'})

    def test_is_edge_point(self):
        tile: Tile = Tile.from_lines(3, ['abc', 'def', 'ghi'])
        self.assertTrue(tile.is_edge_point((0, 0)))
        self.assertTrue(tile.is_edge_point((1, 0)))
        self.assertTrue(tile.is_edge_point((2, 0)))
        self.assertTrue(tile.is_edge_point((0, 1)))
        self.assertFalse(tile.is_edge_point((1, 1)))
        self.assertTrue(tile.is_edge_point((2, 1)))
        self.assertTrue(tile.is_edge_point((0, 2)))
        self.assertTrue(tile.is_edge_point((1, 2)))
        self.assertTrue(tile.is_edge_point((2, 2)))

    def test_puzzle_to_tile(self):
        tile_one = Tile.from_lines(1, ['0000', '0ab0', '0cd0', '0000'])
        tile_two = Tile.from_lines(1, ['0000', '0wx0', '0yz0', '0000'])
        tile_three = Tile.from_lines(1, ['0000', '0330', '0330', '0000'])
        tile_four = Tile.from_lines(1, ['0000', '0440', '0440', '0000'])
        puzzle = Puzzle(2)
        puzzle.add_tile((0, 0), tile_one)
        puzzle.add_tile((1, 0), tile_two)
        puzzle.add_tile((0, 1), tile_three)
        puzzle.add_tile((1, 1), tile_four)

        resulting_tile = puzzle.to_tile()
        self.assertEqual(resulting_tile.grid, {(0, 0): 'a', (1, 0): 'b', (2, 0): 'w', (3, 0): 'x',
                                               (0, 1): 'c', (1, 1): 'd', (2, 1): 'y', (3, 1): 'z',
                                               (0, 2): '3', (1, 2): '3', (2, 2): '4', (3, 2): '4',
                                               (0, 3): '3', (1, 3): '3', (2, 3): '4', (3, 3): '4'})

    def test_puzzle_to_tile_3_by_3(self):
        tile_one = Tile.from_lines(1, ['0000', '0110', '0110', '0000'])
        tile_two = Tile.from_lines(1, ['0000', '0220', '0220', '0000'])
        tile_three = Tile.from_lines(1, ['0000', '0330', '0330', '0000'])
        tile_four = Tile.from_lines(1, ['0000', '0440', '0440', '0000'])
        file_five = Tile.from_lines(1, ['0000', '0550', '0550', '0000'])
        file_six = Tile.from_lines(1, ['0000', '0660', '0660', '0000'])
        tile_seven = Tile.from_lines(1, ['0000', '0770', '0770', '0000'])
        tile_eight = Tile.from_lines(1, ['0000', '0880', '0880', '0000'])
        tile_nine = Tile.from_lines(1, ['0000', '0990', '0990', '0000'])

        puzzle = Puzzle(3)
        puzzle.add_tile((0, 0), tile_one)
        puzzle.add_tile((1, 0), tile_two)
        puzzle.add_tile((2, 0), tile_three)
        puzzle.add_tile((0, 1), tile_four)
        puzzle.add_tile((1, 1), file_five)
        puzzle.add_tile((2, 1), file_six)
        puzzle.add_tile((0, 2), tile_seven)
        puzzle.add_tile((1, 2), tile_eight)
        puzzle.add_tile((2, 2), tile_nine)

        resulting_tile = puzzle.to_tile()
        self.assertEqual(resulting_tile.width, 6)
        resulting_rows = get_grid_lines(resulting_tile.grid)
        self.assertEqual(resulting_rows, ['112233', '112233', '445566', '445566', '778899', '778899'])

    def test_count_sea_monsters(self):
        sea_monster = Tile.from_lines(1, ['                  # ',
                                          '#    ##    ##    ###',
                                          ' #  #  #  #  #  #   '])

        self.assertEqual(sea_monster.count_sea_monsters(), 1)

    def test_has_sea_monster(self):
        example_tile_lines = read_text_list('day_20_sea_monsters_grid.txt')
        tile = Tile.from_lines(5, example_tile_lines)
        self.assertTrue(tile.has_sea_monster((2, 2)))

    def test_count_sea_monsters_2(self):
        example_tile_lines = read_text_list('day_20_sea_monsters_grid.txt')
        tile = Tile.from_lines(5, example_tile_lines)
        self.assertEqual(tile.count_sea_monsters(), 2)

    def assert_equal_any_order(self, list_a, list_b):
        self.assertEqual(sorted(list_a), sorted(list_b))


if __name__ == '__main__':
    unittest.main()
