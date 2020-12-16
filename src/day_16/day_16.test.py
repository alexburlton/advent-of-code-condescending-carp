import unittest

from src.day_16.day_16 import *


class TestDay16(unittest.TestCase):
    def test_parse_rule(self):
        rule_dict = {}
        parse_rule_and_add('class: 1-3 or 5-7', rule_dict)
        parse_rule_and_add('departure location: 26-715 or 727-972', rule_dict)
        self.assertEqual(rule_dict, {'class': (range(1, 3), range(5, 7)),
                                     'departure location': (range(26, 715), range(727, 972))})

    def test_parse_rules(self):
        rules: List[str] = ['class: 1-3 or 5-7', 'departure location: 26-715 or 727-972']
        rule_dict = parse_rules(rules)
        self.assertEqual(rule_dict, {'class': (range(1, 3), range(5, 7)),
                                     'departure location': (range(26, 715), range(727, 972))})

    def test_parse_ticket(self):
        self.assertEqual(parse_ticket('50,67,100,73'), [50, 67, 100, 73])

    def test_parse_input(self):
        rules, my_ticket, other_tickets = parse_input('day_16_example.txt')
        self.assertEqual(rules, {'class': (range(1, 3), range(5, 7)),
                                 'row': (range(6, 11), range(33, 44)),
                                 'seat': (range(13, 40), range(45, 50))})
        self.assertEqual(my_ticket, [7, 1, 14])
        self.assertEqual(other_tickets, [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]])


if __name__ == '__main__':
    unittest.main()
