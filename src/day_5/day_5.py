from typing import List

from utils import read_text_list


def get_row_number(row_str: str) -> int:
    binary = row_str.replace('F', '0').replace('B', '1')
    return int(binary, 2)


def get_column_number(col_str: str) -> int:
    binary = col_str.replace('R', '1').replace('L', '0')
    return int(binary, 2)


def get_seat_id(seat_str: str) -> int:
    row_str: str = seat_str[0:7]
    col_str: str = seat_str[7:10]
    return (get_row_number(row_str) * 8) + get_column_number(col_str)


def part_a(input_lines: List[str]) -> None:
    seat_ids: List[int] = [get_seat_id(seat_str) for seat_str in input_lines]
    print(max(seat_ids))


def part_b(input_lines: List[str]) -> None:
    seat_ids: List[int] = [get_seat_id(seat_str) for seat_str in input_lines]
    sorted_seats: List[int] = sorted(seat_ids)

    current_seat = 0
    for seat in sorted_seats:
        diff = seat - current_seat
        if diff == 2:
            print(seat - 1)

        current_seat = seat


if __name__ == '__main__':
    inputLines = read_text_list("day_5.txt")

    part_a(inputLines)
    part_b(inputLines)
