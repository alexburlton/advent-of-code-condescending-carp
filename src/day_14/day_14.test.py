import unittest

from src.day_14.day_14 import *


class TestDay14(unittest.TestCase):
    def test_convert_to_binary_and_pad(self):
        self.assertEqual(convert_to_binary_and_pad(11, 36), list('000000000000000000000000000000001011'))

    def test_apply_bitmask_a(self):
        self.assertEqual(apply_bitmask_a('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11), 73)
        self.assertEqual(apply_bitmask_a('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101), 101)
        self.assertEqual(apply_bitmask_a('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0), 64)

    def test_parse_memory_instruction(self):
        self.assertEqual(parse_memory_instruction('mem[42] = 100'), (42, 100))

    def test_process_memory_instruction_a(self):
        memory = {}
        bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        process_memory_instruction_a(memory, 'mem[8] = 11', bitmask)
        self.assertEqual(memory, {8: 73})

    def test_part_a(self):
        lines = read_text_list('day_14_example.txt')
        self.assertEqual(part_a(lines), 165)

    def test_replace_floating_values(self):
        value_with_floats: List[str] = list('000000000000000000000000000000X1101X')
        self.assertEqual(replace_floating_values(value_with_floats, ['0', '0']), 26)
        self.assertEqual(replace_floating_values(value_with_floats, ['0', '1']), 27)
        self.assertEqual(replace_floating_values(value_with_floats, ['1', '0']), 58)
        self.assertEqual(replace_floating_values(value_with_floats, ['1', '1']), 59)

    def test_apply_bitmask_b(self):
        bitmask = '000000000000000000000000000000X1001X'
        self.assertEqual(apply_bitmask_b(bitmask, 42), [26, 27, 58, 59])

    def test_apply_bitmask_b_2(self):
        bitmask = '00000000000000000000000000000000X0XX'
        self.assertEqual(apply_bitmask_b(bitmask, 26), [16, 17, 18, 19, 24, 25, 26, 27])

    def test_process_memory_instruction_b(self):
        memory = {}
        bitmask = '000000000000000000000000000000X1001X'
        process_memory_instruction_b(memory, 'mem[42] = 100', bitmask)
        self.assertEqual(memory, {26: 100, 27: 100, 58: 100, 59: 100})


if __name__ == '__main__':
    unittest.main()
