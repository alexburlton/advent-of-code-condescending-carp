import re
from itertools import product
from typing import List, Callable

from utils import read_text_list, count_where


def convert_to_binary_and_pad(number: int, padded_length: int) -> List[str]:
    number_in_binary: str = bin(number)[2:]
    return list(number_in_binary.zfill(padded_length))


def apply_bitmask_a(bitmask: str, number: int) -> int:
    binary_chars = convert_to_binary_and_pad(number, len(bitmask))
    for i in range(0, len(bitmask)):
        if bitmask[i] != 'X':
            binary_chars[i] = bitmask[i]

    return int("".join(binary_chars), 2)


def parse_memory_instruction(instruction: str) -> tuple[int, int]:
    result = re.match('^mem\[([0-9]+)\] = ([0-9]+)$', instruction)
    return int(result.group(1)), int((result.group(2)))


def process_memory_instruction_a(mem: dict[int, int], instruction: str, bitmask: str):
    address, value = parse_memory_instruction(instruction)
    mem[address] = apply_bitmask_a(bitmask, value)


def process_memory_instruction_b(mem: dict[int, int], instruction: str, bitmask: str):
    address, value = parse_memory_instruction(instruction)
    addresses = apply_bitmask_b(bitmask, address)
    for address in addresses:
        mem[address] = value


def apply_bitmask_b(bitmask: str, number: int) -> List[int]:
    binary_chars = convert_to_binary_and_pad(number, len(bitmask))
    for i in range(0, len(bitmask)):
        if bitmask[i] != '0':
            binary_chars[i] = bitmask[i]

    floating_count: int = count_where(is_floating, binary_chars)
    perms = [list(perm) for perm in product('01', repeat=floating_count)]
    return [replace_floating_values(binary_chars, perm) for perm in perms]


def replace_floating_values(value_with_floats: List[str], replacements: List[str]) -> int:
    copy = value_with_floats.copy()
    for i in range(0, len(value_with_floats)):
        if is_floating(copy[i]):
            copy[i] = replacements.pop(0)

    return int("".join(copy), 2)


def is_floating(value: str) -> bool:
    return value == 'X'


def process_instructions(input_lines: List[str], memory_instruction_fn: Callable[[dict[int, int], str, str], None]) -> int:
    mem: dict[int, int] = {}
    bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for instruction in input_lines:
        if 'mask = ' in instruction:
            bitmask = instruction.replace('mask = ', '')
        else:
            memory_instruction_fn(mem, instruction, bitmask)

    return sum(mem.values())


def part_a(input_lines: List[str]) -> int:
    return process_instructions(input_lines, process_memory_instruction_a)


def part_b(input_lines: List[str]) -> int:
    return process_instructions(input_lines, process_memory_instruction_b)


if __name__ == '__main__':
    lines = read_text_list('day_14.txt')
    print(part_a(lines))
    print(part_b(lines))
