import unittest

from src.day_16.day_16 import *


class TestDay16(unittest.TestCase):
    def test_parse_rule(self):
        rule_dict = {}
        parse_rule_and_add('class: 1-3 or 5-7', rule_dict)
        parse_rule_and_add('departure location: 26-715 or 727-972', rule_dict)
        self.assertEqual(rule_dict, {'class': [range(1, 4), range(5, 8)],
                                     'departure location': [range(26, 716), range(727, 973)]})

    def test_parse_rules(self):
        rules: List[str] = ['class: 1-3 or 5-7', 'departure location: 26-715 or 727-972']
        rule_dict = parse_rules(rules)
        self.assertEqual(rule_dict, {'class': [range(1, 4), range(5, 8)],
                                     'departure location': [range(26, 716), range(727, 973)]})

    def test_parse_ticket(self):
        self.assertEqual(parse_ticket('50,67,100,73'), [50, 67, 100, 73])

    def test_parse_input(self):
        rules, my_ticket, other_tickets = parse_input('day_16_example.txt')
        self.assertEqual(rules, {'class': [range(1, 4), range(5, 8)],
                                 'row': [range(6, 12), range(33, 45)],
                                 'seat': [range(13, 41), range(45, 51)]})
        self.assertEqual(my_ticket, [7, 1, 14])
        self.assertEqual(other_tickets, [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]])

    def test_is_invalid_field(self):
        rules, _, _ = parse_input('day_16_example.txt')
        self.assertTrue(is_invalid_field(4, rules))
        self.assertTrue(is_invalid_field(55, rules))
        self.assertTrue(is_invalid_field(12, rules))

        for field in [7, 3, 47, 40, 50, 2, 20, 38, 6]:
            self.assertFalse(is_invalid_field(field, rules))

    def test_is_invalid_ticket(self):
        rules, _, _ = parse_input('day_16_example.txt')
        self.assertEqual(sum_invalid_fields([7, 3, 47], rules), 0)
        self.assertEqual(sum_invalid_fields([40, 4, 50], rules), 4)
        self.assertEqual(sum_invalid_fields([55, 2, 20], rules), 55)
        self.assertEqual(sum_invalid_fields([38, 6, 12], rules), 12)

    def test_get_ticket_error_rate(self):
        rules, _, other_tickets = parse_input('day_16_example.txt')
        self.assertEqual(get_ticket_error_rate(other_tickets, rules), 71)


if __name__ == '__main__':
    unittest.main()
