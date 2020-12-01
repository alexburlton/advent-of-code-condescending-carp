import math
from itertools import combinations
from typing import List

from utils import read_integer_list


def part_a(report: List[int]) -> None:
    print(get_expense_report_product(report, 2))


def part_b(report: List[int]) -> None:
    print(get_expense_report_product(report, 3))


def get_expense_report_product(report: List[int], count: int) -> int:
    perms = combinations(report, count)
    right_perm = next(filter(sums_to_2020, perms))
    return math.prod(right_perm)


def sums_to_2020(permutation: List[int]) -> bool:
    return sum(permutation) == 2020


if __name__ == '__main__':
    inputLines = read_integer_list("day_1.txt")

    part_a(inputLines)
    part_b(inputLines)
