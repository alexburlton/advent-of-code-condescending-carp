from itertools import count
from typing import List

from utils import read_text_list


def part_a(input_lines: List[str]):
    print(count_trees_for_slope(input_lines, 3, 1))


def part_b(input_lines: List[str]):
    print(get_tree_product(input_lines))


def get_tree_product(input_lines: List[str]) -> int:
    slope_a = count_trees_for_slope(input_lines, 1, 1)
    slope_b = count_trees_for_slope(input_lines, 3, 1)
    slope_c = count_trees_for_slope(input_lines, 5, 1)
    slope_d = count_trees_for_slope(input_lines, 7, 1)
    slope_e = count_trees_for_slope(input_lines, 1, 2)
    return slope_a * slope_b * slope_c * slope_d * slope_e


def count_trees_for_slope(input_lines: List[str], x_slope: int, y_slope: int) -> int:
    grid = convert_to_grid(input_lines)
    x_coords = count(0, x_slope)

    row_count = len(grid)

    row_indices_visited = range(0, row_count, y_slope)

    tree_count = 0
    for row_ix in row_indices_visited:
        row = grid[row_ix]
        x_coord = next(x_coords) % len(row)
        if row[x_coord] == '#':
            tree_count = tree_count + 1

    return tree_count


def convert_to_grid(input_lines: List[str]) -> List[List[str]]:
    return list(map(convert_to_array, input_lines))


def convert_to_array(input_line: str) -> List[str]:
    return [char for char in input_line]


if __name__ == '__main__':
    inputLines = read_text_list("day_3.txt")
    part_a(inputLines)
    part_b(inputLines)
