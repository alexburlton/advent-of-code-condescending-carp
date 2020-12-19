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

    def test_is_valid_simple(self):
        rules = {0: SimpleRule('a')}
        self.assertTrue(is_valid(rules, 'a'))
        self.assertFalse(is_valid(rules, 'b'))
        self.assertFalse(is_valid(rules, 'aa'))

    def test_is_valid_multi(self):
        rules = {0: MultiRule([1, 2]), 1: SimpleRule('a'), 2: SimpleRule('b')}
        self.assertTrue(is_valid(rules, 'ab'))
        self.assertFalse(is_valid(rules, 'aba'))
        self.assertFalse(is_valid(rules, 'a'))
        self.assertFalse(is_valid(rules, 'ba'))
        self.assertFalse(is_valid(rules, 'b'))

    def test_is_valid_choice(self):
        rules = {0: ChoiceRule(MultiRule([1, 2]), MultiRule([2, 1])), 1: SimpleRule('a'), 2: SimpleRule('b')}
        self.assertTrue(is_valid(rules, 'ab'))
        self.assertTrue(is_valid(rules, 'ba'))
        self.assertFalse(is_valid(rules, 'aba'))
        self.assertFalse(is_valid(rules, 'a'))
        self.assertFalse(is_valid(rules, 'b'))

    def test_is_valid_examples(self):
        rules, _ = read_rules_and_messages("day_19_example.txt")
        self.assertTrue(is_valid(rules, 'ababbb'))
        self.assertTrue(is_valid(rules, 'abbbab'))
        self.assertFalse(is_valid(rules, 'bababa'))
        self.assertFalse(is_valid(rules, 'aaabbb'))
        self.assertFalse(is_valid(rules, 'aaaabbb'))

    def test_count_valids(self):
        self.assertEqual(count_valids("day_19_example.txt"), 2)


if __name__ == '__main__':
    unittest.main()
