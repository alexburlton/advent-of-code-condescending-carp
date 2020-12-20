import re
from typing import List

from utils import Grid, parse_coordinate_grid, Point


class Tile(object):
    points: Grid
    id: int
    width: int

    def __init__(self, id: int, grid_lines: List[str]):
        self.id = id
        self.points = parse_coordinate_grid(grid_lines)
        self.width = len(grid_lines)

    def rotate_right(self):
        new_points = Grid()
        for point, value in self.points.items():
            new_point: Point = (self.width - 1 - point[1], point[0])
            new_points[new_point] = value

        self.points = new_points


def parse_tile(tile_lines: List[str]) -> Tile:
    id_line = tile_lines.pop(0)
    re_match = re.match(r'^Tile ([\d]+):$', id_line)
    id: int = int(re_match.group(1))
    return Tile(id, tile_lines)
