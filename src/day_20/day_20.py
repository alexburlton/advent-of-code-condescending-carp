import re
from typing import List, Callable

from utils import Grid, parse_coordinate_grid, Point, read_text_groups


class Tile(object):
    points: Grid
    id: int
    width: int

    def __init__(self, id: int, grid_lines: List[str]):
        self.id = id
        self.points = parse_coordinate_grid(grid_lines)
        self.width = len(grid_lines)

    def rotate_right(self):
        self.transform(lambda point: (self.width - 1 - point[1], point[0]))

    def flip_horizontal(self):
        self.transform(lambda point: (self.width - 1 - point[0], point[1]))

    def flip_vertical(self):
        self.transform(lambda point: (point[0], self.width - 1 - point[1]))

    def transform(self, point_transformer: Callable[[Point], Point]):
        new_points = Grid()
        for point, value in self.points.items():
            new_point: Point = point_transformer(point)
            new_points[new_point] = value

        self.points = new_points


def parse_tile(tile_lines: List[str]) -> Tile:
    id_line = tile_lines.pop(0)
    re_match = re.match(r'^Tile ([\d]+):$', id_line)
    id: int = int(re_match.group(1))
    return Tile(id, tile_lines)


if __name__ == '__main__':
    tile_groups = read_text_groups('day_20.txt')
    tiles: List[Tile] = [parse_tile(group.splitlines()) for group in tile_groups]
    print(len(tiles))
