import unittest

from src.day_10.day_10 import *

example_one: List[int] = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
example_two: List[int] = read_integer_list('day_10_example.txt')

sorted_example_one: List[int] = sort_and_add_device(example_one)
sorted_example_two: List[int] = sort_and_add_device(example_two)


class TestDay9(unittest.TestCase):
    def test_calculate_built_in_joltage(self):
        self.assertEqual(calculate_built_in_joltage(example_one), 22)

    def test_calculate_adaptor_distribution(self):
        self.assertEqual(calculate_adaptor_distribution(sorted_example_one), 35)
        self.assertEqual(calculate_adaptor_distribution(sorted_example_two), 220)

    def test_get_options_for_next_adaptor(self):
        self.assertEqual(get_options_for_next_adaptor(0, sorted_example_one), [1])
        self.assertEqual(get_options_for_next_adaptor(4, sorted_example_one), [5, 6, 7])
        self.assertEqual(get_options_for_next_adaptor(10, sorted_example_one), [11, 12])

    def test_calculate_adaptor_combinations(self):
        self.assertEqual(calculate_adaptor_combinations(sorted_example_one), 8)
        self.assertEqual(calculate_adaptor_combinations(sorted_example_two), 19208)


if __name__ == '__main__':
    unittest.main()
