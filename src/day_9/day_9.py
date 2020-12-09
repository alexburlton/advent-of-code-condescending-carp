from itertools import combinations
from typing import List

from utils import read_integer_list, windowed


def is_valid(preamble: List[int], number: int) -> int:
    pairs = combinations(preamble, 2)
    pair_sums = [sum(pair) for pair in pairs]
    return number in pair_sums


def find_first_invalid(numbers: List[int], preamble_length: int) -> int:
    current_ix = -1
    valid = True
    while valid:
        current_ix += 1
        preamble = numbers[current_ix:current_ix+preamble_length]
        digit = numbers[current_ix+preamble_length]
        valid = is_valid(preamble, digit)

    return numbers[current_ix+preamble_length]


def find_contiguous_set_that_sums_to(desired_sum: int, numbers: List[int]) -> List[int]:
    combination_length = 2
    combos = windowed(numbers, combination_length)
    correct_combo = next((combo for combo in combos if sum(combo) == desired_sum), None)
    while correct_combo is None:
        combination_length += 1
        combos = windowed(numbers, combination_length)
        correct_combo = next((combo for combo in combos if sum(combo) == desired_sum), None)

    return correct_combo


def find_encryption_weakness(numbers: list[int]) -> int:
    return min(numbers) + max(numbers)


if __name__ == '__main__':
    input_lines = read_integer_list('day_9.txt')
    invalid_digit = find_first_invalid(input_lines, 25)
    print(invalid_digit)
    contiguous_set = find_contiguous_set_that_sums_to(invalid_digit, input_lines)
    print(find_encryption_weakness(contiguous_set))

