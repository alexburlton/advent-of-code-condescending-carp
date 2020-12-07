import unittest

from src.day_7.day_7 import *

input_lines = read_text_list('day_7_example.txt')
example_hierarchy = parse_bag_hierarchy(input_lines)

class TestDay7(unittest.TestCase):

    def test_parse_individual_bag(self):
        self.assertEqual(parse_bag_attribute('shiny gold bags'), 'shiny gold')
        self.assertEqual(parse_bag_attribute('faded blue bag'), 'faded blue')

    def test_parse_bag_and_count(self):
        self.assertEqual(parse_bag_and_count('6 shiny gold bags.'), BagAndCount('shiny gold', 6))

    def test_parse_bag_contents(self):
        self.assertEqual(parse_bag_contents('1 bright white bag, 2 muted yellow bags.'),
                         [BagAndCount('bright white', 1), BagAndCount('muted yellow', 2)])
        self.assertEqual(parse_bag_contents('1 shiny gold bag.'), [BagAndCount('shiny gold', 1)])
        self.assertEqual(parse_bag_contents('no other bags.'), [])

    def test_parse_bag_fact(self):
        self.assertEqual(parse_bag_fact('bright white bags contain 1 shiny gold bag.'),
                         {'bright white': [BagAndCount('shiny gold', 1)]})
        self.assertEqual(parse_bag_fact('light red bags contain 1 bright white bag, 2 muted yellow bags.'),
                         {'light red': [BagAndCount('bright white', 1), BagAndCount('muted yellow', 2)]})
        self.assertEqual(parse_bag_fact('faded blue bags contain no other bags.'), {'faded blue': []})

    def test_parse_bag_hierarchy(self):
        lines = ['bright white bags contain 1 shiny gold bag.',
                 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.']

        parsed = parse_bag_hierarchy(lines)
        self.assertEqual(parsed, {'bright white': [BagAndCount('shiny gold', 1)],
                                  'muted yellow': [BagAndCount('shiny gold', 2), BagAndCount('faded blue', 9)]})

    def test_contains_bag(self):
        self.assertTrue(contains_bag([BagAndCount('bright white', 1), BagAndCount('muted yellow', 2)], 'muted yellow'))
        self.assertTrue(contains_bag([BagAndCount('bright white', 1), BagAndCount('muted yellow', 2)], 'bright white'))
        self.assertFalse(contains_bag([BagAndCount('bright white', 1), BagAndCount('muted yellow', 2)], 'shiny gold'))

    def test_get_possible_containers(self):
        self.assertEqual(get_possible_containers(example_hierarchy, 'shiny gold'),
                         {'bright white', 'muted yellow', 'dark orange', 'light red'})

    def test_count_contents(self):
        self.assertEqual(count_contents(example_hierarchy, 'shiny gold'), 32)


if __name__ == '__main__':
    unittest.main()
