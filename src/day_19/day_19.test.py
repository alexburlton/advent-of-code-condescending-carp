import unittest

from src.day_19.day_19 import *


class TestDay19(unittest.TestCase):
    def test_parse_simple_rule(self):
        self.assertEqual(parse_rule('"a"'), SimpleRule('a'))

    def test_parse_multi_rule(self):
        self.assertEqual(parse_rule('106 45 32'), MultiRule([106, 45, 32]))

    def test_parse_choice_Rule(self):
        self.assertEqual(parse_rule('106 45 | 32 64'), ChoiceRule(MultiRule([106, 45]), MultiRule([32, 64])))

    def test_read_rules_and_messages(self):
        rules, messages = read_rules_and_messages("day_19_example.txt")
        self.assertEqual(rules, {0: MultiRule([4, 1, 5]),
                                 1: ChoiceRule(MultiRule([2, 3]), MultiRule([3, 2])),
                                 2: ChoiceRule(MultiRule([4, 4]), MultiRule([5, 5])),
                                 3: ChoiceRule(MultiRule([4, 5]), MultiRule([5, 4])),
                                 4: SimpleRule('a'),
                                 5: SimpleRule('b')
                                 })

        self.assertEqual(messages, ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb'])


if __name__ == '__main__':
    unittest.main()
