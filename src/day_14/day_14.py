import re
from typing import List, Callable

from utils import read_text_list

BITMASK_LENGTH = 36


def bitwise_add(bitmask: str, number: int) -> int:
    number_in_binary: str = bin(number)[2:]
    binary_chars = list(number_in_binary.zfill(BITMASK_LENGTH))
    for i in range(0, len(bitmask)):
        if bitmask[i] != 'X':
            binary_chars[i] = bitmask[i]

    return int("".join(binary_chars), 2)


def process_memory_instruction_a(mem: dict[int, int], instruction: str, bitmask: str):
    result = re.match('^mem\[([0-9]+)\] = ([0-9]+)$', instruction)
    address = int(result.group(1))
    value = int((result.group(2)))
    mem[address] = bitwise_add(bitmask, value)


def process_memory_instruction_b(mem: dict[int, int], instruction: str, bitmask: str):
    result = re.match('^mem\[([0-9]+)\] = ([0-9]+)$', instruction)
    address = int(result.group(1))
    value = int((result.group(2)))
    mem[address] = bitwise_add(bitmask, value)


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
