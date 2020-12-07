from typing import List, TypeVar, Callable, Iterable


def read_integer_list(file_name: str) -> List[int]:
    f = open(file_name, "r")
    return list(map(int, f.readlines()))


def read_text_list(file_name: str) -> List[str]:
    f = open(file_name, "r")
    ret = list(f.read().splitlines())
    f.close()
    return ret


T = TypeVar('T')


def count_where(fn: Callable[[T], bool], iterable: Iterable[T]) -> int:
    return len(list(filter(fn, iterable)))
