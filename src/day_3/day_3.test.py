import unittest

from src.day_3.day_3 import *

example_input = read_text_list('day_3_example.txt')


class TestDay3(unittest.TestCase):

    def test_is_tree(self):
        self.assertTrue(is_tree('#'))
        self.assertFalse(is_tree('.'))
        self.assertFalse(is_tree(' '))

    def test_get_item_at_location(self):
        self.assertEqual(get_item_at_location('#..#', 0), '#')
        self.assertEqual(get_item_at_location('#..#', 1), '.')
        self.assertEqual(get_item_at_location('#..#', 5), '.')
        self.assertEqual(get_item_at_location('#..#', 405), '.')

    def test_count_trees_for_slope(self):
        self.assertEqual(count_trees_for_slope(example_input, 1, 1), 2)
        self.assertEqual(count_trees_for_slope(example_input, 3, 1), 7)
        self.assertEqual(count_trees_for_slope(example_input, 5, 1), 3)
        self.assertEqual(count_trees_for_slope(example_input, 7, 1), 4)
        self.assertEqual(count_trees_for_slope(example_input, 1, 2), 2)

    def test_tree_product(self):
        self.assertEqual(get_tree_product(example_input), 336)


if __name__ == '__main__':
    unittest.main()
