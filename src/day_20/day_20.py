import math
import random
import re
from typing import List, Callable, Set

from utils import Grid, parse_coordinate_grid, Point, read_text_groups, add_points, count_where

sea_monster_points = [(18, 0),
                      (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
                      (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]


class Tile(object):
    grid: Grid
    id: int
    width: int
    sorted_points: List[Point] = []
    matched_edges: Set[str] = set()

    def __init__(self, id: int, grid: Grid, matched_edges: Set[str]):
        self.id = id
        self.grid = grid
        self.width = int(math.sqrt(len(grid)))
        self.sorted_points = sorted(grid.keys())
        self.matched_edges = matched_edges

    @classmethod
    def from_lines(cls, id: int, grid_lines: List[str]):
        grid = parse_coordinate_grid(grid_lines)
        return cls(id, grid, set())

    def do_random_transform(self) -> 'Tile':
        result = random.randint(0, 2)
        if result == 0:
            return self.rotate_right()
        elif result == 1:
            return self.flip_vertical()
        else:
            return self.flip_horizontal()

    def rotate_right(self) -> 'Tile':
        return self.transform(lambda point: (self.width - 1 - point[1], point[0]))

    def flip_horizontal(self) -> 'Tile':
        return self.transform(lambda point: (self.width - 1 - point[0], point[1]))

    def flip_vertical(self) -> 'Tile':
        return self.transform(lambda point: (point[0], self.width - 1 - point[1]))

    def transform(self, point_transformer: Callable[[Point], Point]) -> 'Tile':
        new_points = Grid()
        for point, value in self.grid.items():
            new_point: Point = point_transformer(point)
            new_points[new_point] = value

        return Tile(self.id, new_points, self.matched_edges)

    def top_edge(self) -> str:
        return ''.join([self.grid[point] for point in self.sorted_points if point[1] == 0])

    def bottom_edge(self) -> str:
        return ''.join([self.grid[point] for point in self.sorted_points if point[1] == self.width - 1])

    def left_edge(self) -> str:
        return ''.join([self.grid[point] for point in self.sorted_points if point[0] == 0])

    def right_edge(self) -> str:
        return ''.join([self.grid[point] for point in self.sorted_points if point[0] == self.width - 1])

    def get_edges(self) -> Set[str]:
        return {self.top_edge(), self.bottom_edge(), self.left_edge(), self.right_edge()}

    def update_matched_edges(self, matched_edges: Set[str]):
        self.matched_edges = self.matched_edges.union(matched_edges)

    def get_all_possible_edges(self) -> Set[str]:
        current_edges = self.get_edges()
        flipped_edges = {edge[::-1] for edge in current_edges}
        return current_edges.union(flipped_edges)

    def strip_border(self) -> 'Tile':
        new_points = Grid()
        for point, value in self.grid.items():
            if not self.is_edge_point(point):
                new_points[(point[0] - 1, point[1] - 1)] = value

        return Tile(self.id, new_points, self.matched_edges)

    def is_edge_point(self, point: Point) -> bool:
        return point[0] == 0 or point[0] == self.width - 1 or point[1] == 0 or point[1] == self.width - 1

    def get_water_roughness(self) -> int:
        hash_count: int = count_where(lambda key: self.grid[key] == '#', self.grid.keys())
        return hash_count - (self.count_sea_monsters() * len(sea_monster_points))

    def count_sea_monsters(self) -> int:
        return count_where(self.has_sea_monster, self.grid.keys())

    def has_sea_monster(self, point: Point) -> bool:
        transformed_points = [add_points(point, monster_point) for monster_point in sea_monster_points]
        matches = [self.grid.get(transformed_point, None) == '#' for transformed_point in transformed_points]
        return all(matches)


PuzzleGrid = dict[Point, Tile]


class Puzzle(object):
    grid: PuzzleGrid
    dimension: int

    def __init__(self, dimension: int):
        self.grid = PuzzleGrid()
        self.dimension = dimension

    def add_tile(self, point: Point, tile: Tile):
        self.grid[point] = tile

    def get_tile(self, point: Point):
        return self.grid.get(point, None)

    def to_tile(self):
        tile_grid: Grid = Grid()
        for puzzle_point, tile in self.grid.items():
            stripped = tile.strip_border()
            scaled_point = (puzzle_point[0] * stripped.width, puzzle_point[1] * stripped.width)
            for child_point, value in stripped.grid.items():
                actual_point = add_points(scaled_point, child_point)
                tile_grid[actual_point] = value

        return Tile(-1, tile_grid, set())


def parse_tile(tile_lines: List[str]) -> Tile:
    id_line = tile_lines.pop(0)
    re_match = re.match(r'^Tile ([\d]+):$', id_line)
    id: int = int(re_match.group(1))
    return Tile.from_lines(id, tile_lines)


def classify_tiles(tiles: List[Tile]) -> tuple[List[Tile], List[Tile], List[Tile]]:
    corners: List[Tile] = []
    edges: List[Tile] = []
    inners: List[Tile] = []
    remaining_tiles: List[Tile] = tiles.copy()

    for tile in tiles:
        remaining_tiles.remove(tile)
        update_matching_edges(tile, remaining_tiles)

        if len(tile.matched_edges) == 4:
            corners.append(tile)
        elif len(tile.matched_edges) == 6:
            edges.append(tile)
        else:
            inners.append(tile)

    return corners, edges, inners


def update_matching_edges(tile: Tile, other_tiles: List[Tile]):
    my_edges = tile.get_all_possible_edges()

    for other_tile in other_tiles:
        other_edges = other_tile.get_all_possible_edges()
        intersection = other_edges.intersection(my_edges)
        tile.update_matched_edges(intersection)
        other_tile.update_matched_edges(intersection)


def make_full_puzzle(corners: List[Tile], edges: List[Tile], inners: List[Tile]) -> Puzzle:
    puzzle_dimensions = compute_puzzle_dimensions(corners, edges, inners)

    puzzle = Puzzle(puzzle_dimensions)
    add_row(puzzle, corners, edges, 0)

    for row in range(1, puzzle_dimensions - 1):
        add_row(puzzle, edges, inners, row)

    add_row(puzzle, corners, edges, puzzle_dimensions - 1)
    return puzzle


def add_row(puzzle: Puzzle, edges: List[Tile], inners: List[Tile], row: int):
    above_edge = puzzle.get_tile((0, row - 1))

    if above_edge is None:
        # We're building the very first row. So just pick an arbitrary corner piece, and rotate so
        # the joinable edges are right and bottom
        left_edge = edges.pop(0)
        left_edge = rotate_and_flip_until_condition(left_edge, left_corner_condition)
    else:
        # Find the first piece of the row, by joining bottom -> top edge from row above
        desired_edge = above_edge.bottom_edge()
        left_edge = remove_and_rotate_piece(edges, desired_edge, lambda edge: edge.top_edge())

    puzzle.add_tile((0, row), left_edge)

    # Add the rest of the row, by joining right -> left edge
    for i in range(1, puzzle.dimension):
        previous_piece = puzzle.get_tile((i - 1, row))
        desired_edge = previous_piece.right_edge()
        pile_to_take_from = edges if i == puzzle.dimension - 1 else inners
        next_piece = remove_and_rotate_piece(pile_to_take_from, desired_edge, lambda inner: inner.left_edge())
        puzzle.add_tile((i, row), next_piece)


def left_corner_condition(tile: Tile):
    return tile.right_edge() in tile.matched_edges and tile.bottom_edge() in tile.matched_edges


def remove_and_rotate_piece(pieces: List[Tile], desired_edge: str, edge_fn: Callable[[Tile], str]) -> Tile:
    next_piece = next(filter(lambda piece: desired_edge in piece.matched_edges, pieces))
    pieces.remove(next_piece)
    return rotate_and_flip_until_condition(next_piece, lambda tile: edge_fn(tile) == desired_edge)


def compute_puzzle_dimensions(corners: List[Tile], edges: List[Tile], inners: List[Tile]) -> int:
    return int(math.sqrt(len(corners) + len(edges) + len(inners)))


def rotate_and_flip_until_condition(tile: Tile, condition: Callable[[Tile], bool]) -> Tile:
    while not condition(tile):
        tile = tile.do_random_transform()
    return tile


def get_classified_tiles(file_name: str) -> tuple[List[Tile], List[Tile], List[Tile]]:
    tile_groups = read_text_groups(file_name)
    tiles: List[Tile] = [parse_tile(group.splitlines()) for group in tile_groups]
    return classify_tiles(tiles)


def part_a(file_name: str) -> int:
    corners, _, _ = get_classified_tiles(file_name)
    return math.prod([corner.id for corner in corners])


def part_b(file_name: str) -> int:
    corners, edges, inners = get_classified_tiles(file_name)
    puzzle = make_full_puzzle(corners, edges, inners)
    final_tile = puzzle.to_tile()
    final_tile = rotate_and_flip_until_condition(final_tile, lambda tile: tile.count_sea_monsters() > 0)
    return final_tile.get_water_roughness()


if __name__ == '__main__':
    print(part_a('day_20.txt'))
    print(part_b('day_20.txt'))
