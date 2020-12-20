import math
import re
from typing import List, Callable, Set

from utils import Grid, parse_coordinate_grid, Point, read_text_groups


class Tile(object):
    points: Grid
    id: int
    width: int

    def __init__(self, id: int, points: Grid):
        self.id = id
        self.points = points
        self.width = int(math.sqrt(len(points)))

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
        for point, value in self.points.items():
            new_point: Point = point_transformer(point)
            new_points[new_point] = value

        return Tile(self.id, new_points)

    def get_edges(self) -> Set[str]:
        sorted_points: List[Point] = sorted(self.points.keys())
        return {''.join([self.points[point] for point in sorted_points if point[0] == 0]),
                ''.join([self.points[point] for point in sorted_points if point[0] == self.width - 1]),
                ''.join([self.points[point] for point in sorted_points if point[1] == 0]),
                ''.join([self.points[point] for point in sorted_points if point[1] == self.width - 1])}

    def get_all_possible_edges(self) -> Set[str]:
        current_edges = self.get_edges()
        flipped_edges = {edge[::-1] for edge in current_edges}
        return current_edges.union(flipped_edges)


def parse_tile(tile_lines: List[str]) -> Tile:
    id_line = tile_lines.pop(0)
    re_match = re.match(r'^Tile ([\d]+):$', id_line)
    id: int = int(re_match.group(1))
    return Tile.from_lines(id, tile_lines)


def find_corners(tiles: List[Tile]) -> List[int]:
    tile_to_matches: dict[int, int] = {}
    for tile in tiles:
        matches: int = 0
        my_edges = tile.get_all_possible_edges()
        other_tiles = [other_tile for other_tile in tiles if other_tile.get_all_possible_edges() != tile.get_all_possible_edges()]
        for other_tile in other_tiles:
            other_edges = other_tile.get_all_possible_edges()
            intersection = other_edges.intersection(my_edges)
            matches += len(intersection)
        tile_to_matches[tile.id] = matches

    return [key for key, value in tile_to_matches.items() if value == 4]


if __name__ == '__main__':
    tile_groups = read_text_groups('day_20.txt')
    tiles: List[Tile] = [parse_tile(group.splitlines()) for group in tile_groups]
    print(len(tiles))
    print(math.prod(find_corners(tiles)))
