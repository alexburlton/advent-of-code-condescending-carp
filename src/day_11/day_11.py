from typing import List, Optional, Callable

from utils import read_coordinate_grid, get_adjacents, count_where, Grid, Point, get_unit_directions, add_points


def iterate_grid(grid: Grid, replace_fn: Callable[[Point, Grid], str]) -> Grid:
    new_grid = {}
    for (point, item) in grid.items():
        if not is_seat(item):
            new_grid[point] = item
            continue

        new_grid[point] = replace_fn(point, grid)

    return new_grid


def iterate_seat_part_a(point: Point, grid: Grid) -> str:
    adjacents: List[str] = get_adjacents(grid, point)
    occupied_adjacents = count_occupied(adjacents)
    return get_new_value(grid[point], occupied_adjacents, 4)


def iterate_seat_part_b(point: Point, grid: Grid) -> str:
    occupied_adjacents = get_visible_occupied_seats(grid, point)
    return get_new_value(grid[point], occupied_adjacents, 5)


def get_visible_occupied_seats(grid: Grid, point: Point) -> int:
    directions = get_unit_directions()
    seats = [get_seat_for_direction(grid, point, d) for d in directions]
    return count_where(is_occupied, seats)


def get_seat_for_direction(grid: Grid, point: Point, direction: Point) -> Optional[str]:
    next_stop = add_points(point, direction)
    next_point = grid.get(next_stop, None)
    while True:
        if next_point is None or is_seat(next_point):
            return next_point
        next_stop = add_points(next_stop, direction)
        next_point = grid.get(next_stop, None)


def get_new_value(seat: str, occupied_adjacents: int, tolerance: int) -> str:
    if seat == 'L' and occupied_adjacents == 0:
        return '#'
    elif seat == '#' and occupied_adjacents >= tolerance:
        return 'L'
    else:
        return seat


def is_seat(seat_str: str) -> bool:
    return seat_str == '#' or seat_str == 'L'


def is_occupied(seat_str: str) -> bool:
    return seat_str == '#'


def count_occupied(seat_list: List[str]) -> int:
    return count_where(is_occupied, seat_list)


def iterate_until_stable(grid: Grid, replace_fn: Callable[[Point, Grid], str]) -> int:
    old_grid = grid
    new_grid = iterate_grid(grid, replace_fn)
    while old_grid != new_grid:
        old_grid = new_grid
        new_grid = iterate_grid(new_grid, replace_fn)

    return count_occupied(list(new_grid.values()))


def part_a(grid: Grid) -> int:
    return iterate_until_stable(grid, iterate_seat_part_a)


def part_b(grid: Grid) -> int:
    return iterate_until_stable(grid, iterate_seat_part_b)


if __name__ == '__main__':
    lines = read_coordinate_grid('day_11.txt')
    print(part_a(lines))
    print(part_b(lines))


