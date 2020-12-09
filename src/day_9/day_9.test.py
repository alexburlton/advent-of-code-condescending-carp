import unittest

from src.day_9.day_9 import *


class TestDay9(unittest.TestCase):
    def test_is_valid(self):
        preamble = list(range(1, 26))
        self.assertTrue(is_valid(preamble, 26))
        self.assertTrue(is_valid(preamble, 49))
        self.assertFalse(is_valid(preamble, 100))
        self.assertFalse(is_valid(preamble, 50))

    def test_is_valid_2(self):
        preamble = list(range(1, 26))
        preamble[19] = 45
        self.assertTrue(is_valid(preamble, 26))
        self.assertFalse(is_valid(preamble, 65))
        self.assertTrue(is_valid(preamble, 64))
        self.assertTrue(is_valid(preamble, 66))

    def test_find_first_invalid(self):
        numbers = read_integer_list('day_9_example.txt')
        result = find_first_invalid(numbers, 5)
        self.assertEqual(result, 127)

    def test_find_first_invalid_real(self):
        numbers = read_integer_list('day_9.txt')
        result = find_first_invalid(numbers, 25)
        self.assertEqual(result, 15353384)

    def test_find_contiguous_set_that_sums_to(self):
        numbers = read_integer_list('day_9_example.txt')
        result = find_contiguous_set_that_sums_to(127, numbers)
        self.assertEqual(result, (15, 25, 47, 40))

    def test_find_encryption_weakness(self):
        self.assertEqual(find_encryption_weakness([15, 25, 47, 40]), 62)


if __name__ == '__main__':
    unittest.main()
