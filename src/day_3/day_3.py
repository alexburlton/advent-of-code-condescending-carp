import math
from itertools import count
from typing import List

from utils import read_text_list


def part_a(input_lines: List[str]):
    print(count_trees_for_slope(input_lines, 3, 1))


def part_b(input_lines: List[str]):
    print(get_tree_product(input_lines))


def get_tree_product(input_lines: List[str]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod((map(lambda slope: count_trees_for_slope(input_lines, slope[0], slope[1]), slopes)))


def count_trees_for_slope(input_lines: List[str], x_slope: int, y_slope: int) -> int:
    x_coords = count(0, x_slope)

    row_count = len(input_lines)

    row_indices_visited = range(0, row_count, y_slope)

    tree_count = 0
    for row_ix in row_indices_visited:
        row = input_lines[row_ix]
        x_coord = next(x_coords) % len(row)
        if row[x_coord] == '#':
            tree_count = tree_count + 1

    return tree_count


if __name__ == '__main__':
    inputLines = read_text_list("day_3.txt")
    part_a(inputLines)
    part_b(inputLines)
