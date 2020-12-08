from dataclasses import dataclass
from typing import List, Optional

from utils import read_text_list


def run_program(instruction_list: List[str], instruction_to_replace: Optional[int] = None) -> tuple[int, bool]:
    accumulator: int = 0
    instruction_pointer: int = 0
    instructions_visited: set[int] = set()
    terminated: bool = False

    if instruction_to_replace is not None:
        instruction_list = instruction_list.copy()
        current_value = instruction_list[instruction_to_replace]
        if 'acc' in current_value:
            return accumulator, terminated
        elif 'nop' in current_value:
            new_value = current_value.replace('nop', 'jmp')
            instruction_list[instruction_to_replace] = new_value
        else:
            new_value = current_value.replace('jmp', 'nop')
            instruction_list[instruction_to_replace] = new_value

    current_instruction = instruction_list[instruction_pointer]
    while instruction_pointer not in instructions_visited:
        instructions_visited.add(instruction_pointer)
        code_and_value = current_instruction.split(' ')
        op_code = code_and_value[0]
        op_value = int(code_and_value[1])

        if op_code == 'acc':
            accumulator += op_value
            instruction_pointer += 1
        elif op_code == 'nop':
            instruction_pointer += 1
        else:
            instruction_pointer += op_value

        if instruction_pointer > len(instruction_list) - 1:
            terminated = True
            break

        current_instruction = instruction_list[instruction_pointer]

    return accumulator, terminated


def part_b(instruction_list: List[str]) -> int:
    instruction_to_replace = 0
    result: tuple[int, bool] = run_program(instruction_list, instruction_to_replace)
    while not result[1]:
        instruction_to_replace += 1
        result = run_program(instruction_list, instruction_to_replace)

    return result[0]


if __name__ == '__main__':
    input_lines = read_text_list('day_8.txt')
    print(run_program(input_lines))
    print(part_b(input_lines))
