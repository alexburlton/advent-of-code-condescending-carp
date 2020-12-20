import math
import re
from typing import List, Callable, Set

from utils import Grid, parse_coordinate_grid, Point, read_text_groups


class Tile(object):
    grid: Grid
    id: int
    width: int
    sorted_points: List[Point] = []
    matched_edges: Set[str] = set()

    def __init__(self, id: int, grid: Grid):
        self.id = id
        self.grid = grid
        self.width = int(math.sqrt(len(grid)))
        self.sorted_points = sorted(grid.keys())

    @classmethod
    def from_lines(cls, id: int, grid_lines: List[str]):
        grid = parse_coordinate_grid(grid_lines)
        return cls(id, grid)

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

        return Tile(self.id, new_points)

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
        self.matched_edges = matched_edges.intersection(self.get_edges())

    def get_all_possible_edges(self) -> Set[str]:
        current_edges = self.get_edges()
        flipped_edges = {edge[::-1] for edge in current_edges}
        return current_edges.union(flipped_edges)


PuzzleGrid = dict[Point, Tile]


class Puzzle(object):
    grid: PuzzleGrid

    def __init__(self):
        self.grid = PuzzleGrid()

    def add_tile(self, point: Point, tile: Tile):
        self.grid[point] = tile


def parse_tile(tile_lines: List[str]) -> Tile:
    id_line = tile_lines.pop(0)
    re_match = re.match(r'^Tile ([\d]+):$', id_line)
    id: int = int(re_match.group(1))
    return Tile.from_lines(id, tile_lines)


def classify_tiles(tiles: List[Tile]) -> tuple[List[Tile], List[Tile], List[Tile]]:
    corners: List[Tile] = []
    edges: List[Tile] = []
    inners: List[Tile] = []
    for tile in tiles:
        matches: Set[str] = set()
        my_edges = tile.get_all_possible_edges()
        other_tiles = [other_tile for other_tile in tiles if other_tile.get_all_possible_edges() != tile.get_all_possible_edges()]
        for other_tile in other_tiles:
            other_edges = other_tile.get_all_possible_edges()
            intersection = other_edges.intersection(my_edges)
            matches = matches.union(intersection)
        tile.update_matched_edges(matches)
        if len(matches) == 4:
            corners.append(tile)
        elif len(matches) == 6:
            edges.append(tile)
        else:
            inners.append(tile)

    return corners, edges, inners


# def make_full_puzzle(corners: List[Tile], edges: List[Tile], inners: List[Tile]) -> Puzzle:



if __name__ == '__main__':
    tile_groups = read_text_groups('day_20.txt')
    tiles: List[Tile] = [parse_tile(group.splitlines()) for group in tile_groups]
    print(len(tiles))
    corners, edges, inners = classify_tiles(tiles)
    print(math.prod([corner.id for corner in corners]))
