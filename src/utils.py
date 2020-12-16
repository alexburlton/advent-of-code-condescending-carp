from itertools import tee
from typing import List, TypeVar, Callable, Iterable

Point = tuple[int, int]
Grid = dict[Point, str]


def read_integer_list(file_name: str) -> List[int]:
    f = open(file_name, "r")
    values = list(map(int, f.readlines()))
    f.close()
    return values


def read_text_list(file_name: str) -> List[str]:
    f = open(file_name, "r")
    ret = list(f.read().splitlines())
    f.close()
    return ret


def read_text_groups(file_name: str) -> List[str]:
    f = open(file_name, "r")
    ret = f.read().split("\n\n")
    f.close()
    return ret


def get_adjacents(grid: Grid, coord: Point) -> List[str]:
    adjacent_coords = [add_points(coord, d) for d in get_unit_directions()]
    return [grid.get(adj, None) for adj in adjacent_coords if grid.get(adj, None) is not None]


def get_unit_directions() -> List[Point]:
    return [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def add_points(a: Point, b: Point) -> Point:
    return a[0] + b[0], a[1] + b[1]


def read_coordinate_grid(file_name: str) -> Grid:
    text_list: List[str] = read_text_list(file_name)
    return parse_coordinate_grid(text_list)


def parse_coordinate_grid(rows: List[str]) -> Grid:
    grid = {}
    for y in range(0, len(rows)):
        row = rows[y]
        coords = {(i, y): value for i, value in enumerate(row)}
        grid.update(coords)

    return grid


def windowed(iterable, size):
    iters = tee(iterable, size)
    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)
    return list(zip(*iters))


T = TypeVar('T')


def count_where(fn: Callable[[T], bool], iterable: Iterable[T]) -> int:
    return len(list(filter(fn, iterable)))
