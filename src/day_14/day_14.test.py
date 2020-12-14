import unittest

from src.day_14.day_14 import *


class TestDay14(unittest.TestCase):
    def test_bitwise_add(self):
        self.assertEqual(bitwise_add('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11), 73)
        self.assertEqual(bitwise_add('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101), 101)
        self.assertEqual(bitwise_add('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0), 64)

    def test_process_memory_instruction_a(self):
        memory = {}
        bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        process_memory_instruction_a(memory, 'mem[8] = 11', bitmask)
        self.assertEqual(memory, {8:73})

    def test_part_a(self):
        lines = read_text_list('day_14_example.txt')
        self.assertEqual(part_a(lines), 165)




if __name__ == '__main__':
    unittest.main()
