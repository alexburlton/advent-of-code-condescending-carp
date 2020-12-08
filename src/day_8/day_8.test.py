import unittest

from src.day_8.day_8 import *


class TestDay8(unittest.TestCase):
    def test_process_acc(self):
        instruction_list = ['acc +42']
        computer = IntCodeComputer(instruction_list)
        computer.process_next_instruction()
        self.assertEqual(computer.accumulator, 42)
        self.assertEqual(computer.instruction_pointer, 1)

    def test_process_acc_negative(self):
        instruction_list = ['acc -150']
        computer = IntCodeComputer(instruction_list)
        computer.process_next_instruction()
        self.assertEqual(computer.accumulator, -150)
        self.assertEqual(computer.instruction_pointer, 1)

    def test_process_nop(self):
        instruction_list = ['nop 65']
        computer = IntCodeComputer(instruction_list)
        computer.process_next_instruction()
        self.assertEqual(computer.accumulator, 0)
        self.assertEqual(computer.instruction_pointer, 1)

    def test_process_jmp(self):
        instruction_list = ['jmp 52']
        computer = IntCodeComputer(instruction_list)
        computer.process_next_instruction()
        self.assertEqual(computer.accumulator, 0)
        self.assertEqual(computer.instruction_pointer, 52)

    def test_process_with_loop(self):
        instruction_list = read_text_list('day_8_example.txt')
        computer = IntCodeComputer(instruction_list)
        result = computer.process_instructions()
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], False)

    def test_process_with_loop_real(self):
        instruction_list = read_text_list('day_8.txt')
        computer = IntCodeComputer(instruction_list)
        result = computer.process_instructions()
        self.assertEqual(result[0], 1782)
        self.assertEqual(result[1], False)

    def test_flip_instruction(self):
        instruction_list = ['acc +42', 'nop +456', 'jmp +5']
        self.assertEqual(flip_instruction(instruction_list, 0), ['acc +42', 'nop +456', 'jmp +5'])
        self.assertEqual(flip_instruction(instruction_list, 1), ['acc +42', 'jmp +456', 'jmp +5'])
        self.assertEqual(flip_instruction(instruction_list, 2), ['acc +42', 'nop +456', 'nop +5'])
        # shouldn't modify in-place
        self.assertEqual(instruction_list, ['acc +42', 'nop +456', 'jmp +5'])

    def test_process_with_termination(self):
        instruction_list = read_text_list('day_8_example.txt')
        result = run_program(instruction_list, 7)
        self.assertEqual(result[0], 8)
        self.assertEqual(result[1], True)

    def test_run_until_terminates(self):
        instruction_list = read_text_list('day_8_example.txt')
        result = run_until_terminates(instruction_list)
        self.assertEqual(result, 8)

    def test_run_until_terminates_real(self):
        instruction_list = read_text_list('day_8.txt')
        result = run_until_terminates(instruction_list)
        self.assertEqual(result, 797)


if __name__ == '__main__':
    unittest.main()
