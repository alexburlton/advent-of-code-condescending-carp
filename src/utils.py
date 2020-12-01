from typing import List


def read_integer_list(file_name: str) -> List[int]:
    f = open(file_name, "r")
    return list(map(int, f.readlines()))
