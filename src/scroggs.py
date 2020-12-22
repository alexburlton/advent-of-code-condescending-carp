from itertools import permutations
from typing import List

from utils import count_where, windowed


# Day 21. Seemingly A000255 on OEIS.
# Recurrence relation: a_n = na_(n-1) - a_(n-2) + a_(n-3) - a_(n-4) + ...
def calculate_for_n(n: int) -> int:
    number_strs = [str(i) for i in range(1, n+1)]
    illegal_parts: List[str] = [''.join(seq) for seq in windowed(number_strs, 2)]
    all_permutations = [''.join(perm) for perm in permutations(number_strs, n)]
    return count_where(lambda permutation: is_allowed(permutation, illegal_parts), all_permutations)


def is_allowed(permutation: str, illegal_parts: List[str]) -> bool:
    return all([part not in permutation for part in illegal_parts])


if __name__ == '__main__':
    for n in range(1, 10):
        print(n, calculate_for_n(n))
