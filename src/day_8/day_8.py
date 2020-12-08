from typing import List, Optional

from utils import read_text_list


class IntCodeComputer:
    def __init__(self, instruction_list: List[str]):
        self.instruction_list = instruction_list
        self.accumulator = 0
        self.instruction_pointer = 0
        self.instructions_visited: set[int] = set()
        self.terminated: bool = False
        self.current_instruction = instruction_list[0]

    def process_instructions(self) -> tuple[int, bool]:
        while self.instruction_pointer not in self.instructions_visited and not self.terminated:
            self.process_next_instruction()

        return self.accumulator, self.terminated

    def process_next_instruction(self):
        self.instructions_visited.add(self.instruction_pointer)
        code_and_value = self.current_instruction.split(' ')
        op_code = code_and_value[0]
        op_value = int(code_and_value[1])

        if op_code == 'acc':
            self.accumulator += op_value
            self.instruction_pointer += 1
        elif op_code == 'nop':
            self.instruction_pointer += 1
        else:
            self.instruction_pointer += op_value

        if self.instruction_pointer > len(self.instruction_list) - 1:
            self.terminated = True
        else:
            self.current_instruction = self.instruction_list[self.instruction_pointer]


def run_program(instruction_list: List[str], instruction_to_replace: Optional[int] = None) -> tuple[int, bool]:
    if instruction_to_replace is not None:
        instruction_list = flip_instruction(instruction_list, instruction_to_replace)

    computer = IntCodeComputer(instruction_list)
    return computer.process_instructions()


def flip_instruction(instruction_list: List[str], instruction_to_replace: int) -> List[str]:
    new_list = instruction_list.copy()
    current_value = new_list[instruction_to_replace]
    if 'acc' in current_value:
        return instruction_list
    elif 'nop' in current_value:
        new_value = current_value.replace('nop', 'jmp')
        new_list[instruction_to_replace] = new_value
    else:
        new_value = current_value.replace('jmp', 'nop')
        new_list[instruction_to_replace] = new_value

    return new_list


def run_until_terminates(instruction_list: List[str]) -> int:
    instruction_to_replace = 0
    result: tuple[int, bool] = run_program(instruction_list, instruction_to_replace)
    while not result[1]:
        instruction_to_replace += 1
        result = run_program(instruction_list, instruction_to_replace)

    return result[0]


if __name__ == '__main__':
    input_lines = read_text_list('day_8.txt')
    print(run_program(input_lines))
    print(run_until_terminates(input_lines))
