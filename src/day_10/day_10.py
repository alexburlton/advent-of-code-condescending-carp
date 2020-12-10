from typing import List

from utils import read_integer_list


def calculate_built_in_joltage(adaptors: List[int]) -> int:
    return max(adaptors) + 3


def sort_and_add_device(adaptors: List[int]) -> List[int]:
    sorted_adaptors = sorted(adaptors)
    sorted_adaptors.append(calculate_built_in_joltage(sorted_adaptors))
    return sorted_adaptors


def calculate_adaptor_distribution(adaptors: List[int]) -> int:
    current_joltage: int = 0
    differences: dict[int, int] = {}
    for adaptor in adaptors:
        diff = adaptor - current_joltage
        differences[diff] = differences.get(diff, 0) + 1
        current_joltage = adaptor

    return differences[1] * differences[3]


def calculate_adaptor_combinations(adaptors: List[int]) -> int:
    memoised_counts: dict[int, int] = {}
    return calculate_adaptor_combinations_rec(adaptors, 0, memoised_counts) + 1


def calculate_adaptor_combinations_rec(adaptors: List[int], current_joltage: int, memoised_counts: dict[int, int]) -> int:
    memoised = memoised_counts.get(current_joltage)
    if memoised is not None:
        return memoised

    current_options = get_options_for_next_adaptor(current_joltage, adaptors)
    if len(current_options) == 0:
        return 0

    count = len(current_options) - 1
    result = count + sum([calculate_adaptor_combinations_rec(adaptors, option, memoised_counts) for option in current_options])
    memoised_counts[current_joltage] = result
    return result


def get_options_for_next_adaptor(current_joltage: int, adaptors: List[int]) -> List[int]:
    return [adaptor for adaptor in adaptors if current_joltage < adaptor < current_joltage + 4]


if __name__ == '__main__':
    input_lines = read_integer_list('day_10.txt')
    sorted_adaptors = sort_and_add_device(input_lines)
    print(calculate_adaptor_distribution(sorted_adaptors))
    print(calculate_adaptor_combinations(sorted_adaptors))


