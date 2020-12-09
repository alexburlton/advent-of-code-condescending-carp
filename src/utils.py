from itertools import tee
from typing import List, TypeVar, Callable, Iterable


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


def windowed(iterable, size):
    iters = tee(iterable, size)
    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)
    return list(zip(*iters))


T = TypeVar('T')


def count_where(fn: Callable[[T], bool], iterable: Iterable[T]) -> int:
    return len(list(filter(fn, iterable)))
