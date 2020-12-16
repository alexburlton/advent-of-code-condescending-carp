import unittest

from src.day_16.day_16 import *


class TestDay16(unittest.TestCase):
    def test_parse_rule(self):
        rule_dict = {}
        parse_rule_and_add('class: 1-3 or 5-7', rule_dict)
        parse_rule_and_add('departure location: 26-715 or 727-972', rule_dict)
        self.assertEqual(rule_dict, {'class': FieldRule(range(1, 4), range(5, 8)),
                                     'departure location': FieldRule(range(26, 716), range(727, 973))})

    def test_parse_rules(self):
        rules: List[str] = ['class: 1-3 or 5-7', 'departure location: 26-715 or 727-972']
        rule_dict = parse_rules(rules)
        self.assertEqual(rule_dict, {'class': FieldRule(range(1, 4), range(5, 8)),
                                     'departure location': FieldRule(range(26, 716), range(727, 973))})

    def test_parse_ticket(self):
        self.assertEqual(parse_ticket('50,67,100,73'), [50, 67, 100, 73])

    def test_parse_input(self):
        rules, my_ticket, other_tickets = parse_input('day_16_example.txt')
        self.assertEqual(rules, {'class': FieldRule(range(1, 4), range(5, 8)),
                                 'row': FieldRule(range(6, 12), range(33, 45)),
                                 'seat': FieldRule(range(13, 41), range(45, 51))})
        self.assertEqual(my_ticket, [7, 1, 14])
        self.assertEqual(other_tickets, [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]])

    def test_is_invalid_field(self):
        rules, _, _ = parse_input('day_16_example.txt')
        self.assertTrue(is_invalid_field(4, rules))
        self.assertTrue(is_invalid_field(55, rules))
        self.assertTrue(is_invalid_field(12, rules))

        for field in [7, 3, 47, 40, 50, 2, 20, 38, 6]:
            self.assertFalse(is_invalid_field(field, rules))

    def test_sum_invalid_fields(self):
        rules, _, _ = parse_input('day_16_example.txt')
        self.assertEqual(sum_invalid_fields([7, 3, 47], rules), 0)
        self.assertEqual(sum_invalid_fields([40, 4, 50], rules), 4)
        self.assertEqual(sum_invalid_fields([55, 2, 20], rules), 55)
        self.assertEqual(sum_invalid_fields([38, 6, 12], rules), 12)

    def test_is_valid_ticket(self):
        rules, _, _ = parse_input('day_16_example.txt')
        self.assertTrue(is_valid_ticket([7, 3, 47], rules))
        self.assertFalse(is_valid_ticket([40, 4, 50], rules))
        self.assertFalse(is_valid_ticket([55, 2, 20], rules))
        self.assertFalse(is_valid_ticket([38, 6, 12], rules))
        # grr, stupid edge case
        self.assertFalse(is_valid_ticket([0, 3, 47], rules))

    def test_get_ticket_error_rate(self):
        rules, _, other_tickets = parse_input('day_16_example.txt')
        self.assertEqual(get_ticket_error_rate(other_tickets, rules), 71)

    def test_is_valid_field_order(self):
        class_field = FieldRule(range(0, 2), range(4, 20))
        row_field = FieldRule(range(0, 6), range(8, 20))
        seat_field = FieldRule(range(0, 14), range(16, 20))

        tickets = [[3, 9, 18], [15, 1, 5], [5, 14, 9]]

        self.assertTrue(is_valid_field_order(tickets, [row_field, class_field, seat_field]))
        self.assertFalse(is_valid_field_order(tickets, [row_field, seat_field, class_field]))
        self.assertFalse(is_valid_field_order(tickets, [class_field, row_field, seat_field]))
        self.assertFalse(is_valid_field_order(tickets, [class_field, seat_field, row_field]))
        self.assertFalse(is_valid_field_order(tickets, [seat_field, class_field, row_field]))
        self.assertFalse(is_valid_field_order(tickets, [seat_field, row_field, class_field]))

    def test_get_field_order(self):
        rules, _, tickets = parse_input('day_16_example_b.txt')
        self.assertEqual(get_field_order(tickets, rules), {'class': 1, 'row': 0, 'seat': 2})

    def test_remove_value(self):
        self.assertEqual(remove_value([1, 3, 10], 3), [1, 10])

    def test_remove_from_all_values(self):
        some_map = {'foo': [1, 3, 5], 'bar': [1, 7, 10, 15], 'baz': [3, 5, 10]}
        self.assertEqual(remove_from_all_values(some_map, 3), {'foo': [1, 5], 'bar': [1, 7, 10, 15], 'baz': [5, 10]})

    def test_resolve_positions(self):
        possible_positions = {'foo': [1, 3, 10], 'bar': [1, 2, 10], 'baz': [10, 3], 'buzz': [3]}
        resolved = resolve_positions(possible_positions)
        self.assertEqual(resolved, {'foo': 1, 'bar': 2, 'baz': 10, 'buzz': 3})


if __name__ == '__main__':
    unittest.main()
