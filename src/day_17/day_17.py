from dataclasses import dataclass
from itertools import product
from typing import List, TypeVar, Callable

from utils import read_text_list, flatten, count_where


@dataclass
class Point3D(object):
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other) -> 'Point3D':
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def neighbours(self) -> List['Point3D']:
        unit_directions = [-1, 0, 1]
        result: List[tuple[int, int, int]] = list(product(unit_directions, repeat=3))
        result.remove((0, 0, 0))
        return [self + Point3D(p[0], p[1], p[2]) for p in result]


@dataclass
class Point4D(object):
    x: int
    y: int
    z: int
    w: int

    def __init__(self, x: int, y: int, z: int, w: int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other) -> 'Point4D':
        return Point4D(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w))

    def neighbours(self) -> List['Point4D']:
        unit_directions = [-1, 0, 1]
        result: List[tuple[int, int, int, int]] = list(product(unit_directions, repeat=4))
        result.remove((0, 0, 0, 0))
        return [self + Point4D(p[0], p[1], p[2], p[3]) for p in result]


Grid3D = dict[Point3D, bool]
Grid4D = dict[Point4D, bool]
Grid = Grid3D or Grid4D
Point = Point3D or Point4D


def read_input_3d(file_name: str) -> Grid3D:
    rows: List[str] = read_text_list(file_name)
    grid: Grid3D = {}
    for y in range(0, len(rows)):
        row = rows[y]
        coords: Grid3D = {Point3D(i, y, 0): (value == '#') for i, value in enumerate(row)}
        grid.update(coords)

    return grid


def read_input_4d(file_name: str) -> Grid4D:
    rows: List[str] = read_text_list(file_name)
    grid: Grid4D = {}
    for y in range(0, len(rows)):
        row = rows[y]
        coords: Grid4D = {Point4D(i, y, 0, 0): (value == '#') for i, value in enumerate(row)}
        grid.update(coords)

    return grid


def iterate_input(grid: Grid) -> Grid:
    all_points_to_consider = set(flatten([point.neighbours() for point in grid.keys()]))
    new_grid: Grid = {}
    for point in all_points_to_consider:
        currently_active = is_active(point, grid)
        active_count = count_where(lambda pt: is_active(pt, grid), point.neighbours())
        now_active = compute_new_state(currently_active, active_count)
        new_grid[point] = now_active

    return new_grid


def compute_new_state(currently_active: bool, active_neighbour_count: int) -> bool:
    if currently_active:
        return active_neighbour_count in [2, 3]
    else:
        return active_neighbour_count == 3


def is_active(point: Point, grid: Grid) -> bool:
    return grid.get(point, False)


def part_a(file_name: str) -> int:
    return read_and_boot(file_name, read_input_3d)


def part_b(file_name: str) -> int:
    return read_and_boot(file_name, read_input_4d)


def read_and_boot(file_name: str, parse_as_grid: Callable[[str], Grid]) -> int:
    grid: Grid = parse_as_grid(file_name)
    for i in range(0, 6):
        grid = iterate_input(grid)

    return count_where(lambda pt: is_active(pt, grid), grid.keys())


if __name__ == '__main__':
    print(part_a('day_17.txt'))
    print(part_b('day_17.txt'))
