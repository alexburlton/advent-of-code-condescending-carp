import math
from itertools import count
from typing import List

from utils import read_text_list, count_where


def part_a(input_lines: List[str]):
    print(count_trees_for_slope(input_lines, 3, 1))


def part_b(input_lines: List[str]):
    print(get_tree_product(input_lines))


def get_tree_product(input_lines: List[str]) -> int:
    slopes: List[tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts: List[int] = [count_trees_for_slope(input_lines, slope[0], slope[1]) for slope in slopes]
    return math.prod(tree_counts)


def count_trees_for_slope(input_lines: List[str], x_slope: int, y_slope: int) -> int:
    row_count: int = len(input_lines)
    rows_visited: List[str] = [input_lines[ix] for ix in range(0, row_count, y_slope)]

    x_coords: iter = count(0, x_slope)
    path: List[str] = [get_item_at_location(row, next(x_coords)) for row in rows_visited]
    return count_where(is_tree, path)


def is_tree(item: str) -> bool:
    return item == '#'


def get_item_at_location(row: str, x_coord: int) -> str:
    return row[x_coord % len(row)]


if __name__ == '__main__':
    inputLines = read_text_list("day_3.txt")
    part_a(inputLines)
    part_b(inputLines)
