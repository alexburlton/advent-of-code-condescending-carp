import unittest

from src.day_2.day_2 import *

rule_one_str: str = '1-3 a: abcde'
rule_two_str: str = '1-3 b: cdefg'
rule_three_str: str = '2-9 c: ccccccccc'

rule_one = PasswordAndRule(password='abcde', ruleMin=1, ruleMax=3, ruleLetter='a')
rule_two = PasswordAndRule(password='cdefg', ruleMin=1, ruleMax=3, ruleLetter='b')
rule_three = PasswordAndRule(password='ccccccccc', ruleMin=2, ruleMax=9, ruleLetter='c')


class TestDay2(unittest.TestCase):

    def test_parse_password_line(self):
        self.assertEqual(parse_password_line(rule_one_str), rule_one)
        self.assertEqual(parse_password_line(rule_two_str), rule_two)
        self.assertEqual(parse_password_line(rule_three_str), rule_three)

    def test_parse_password_lines(self):
        lines: List[str] = [rule_one_str, rule_two_str, rule_three_str]
        self.assertEqual(parse_lines(lines), [rule_one, rule_two, rule_three])

    def test_rule_validation(self):
        self.assertTrue(is_valid(rule_one))
        self.assertFalse(is_valid(rule_two))
        self.assertTrue(is_valid(rule_three))

    def test_valid_count(self):
        self.assertEqual(count_valid([rule_one_str, rule_two_str, rule_three_str]), 2)
        self.assertEqual(count_valid([rule_one_str, rule_one_str, rule_three_str]), 3)
        self.assertEqual(count_valid([rule_two_str, rule_two_str, rule_two_str]), 0)

    def test_new_rule_validation(self):
        self.assertTrue(is_valid_new_way(rule_one))
        self.assertFalse(is_valid_new_way(rule_two))
        self.assertFalse(is_valid_new_way(rule_three))

    def test_new_valid_count(self):
        self.assertEqual(count_valid_new_way([rule_one_str, rule_two_str, rule_three_str]), 1)
        self.assertEqual(count_valid_new_way([rule_one_str, rule_one_str]), 2)
        self.assertEqual(count_valid_new_way([rule_two_str, rule_three_str, rule_three_str]), 0)


if __name__ == '__main__':
    unittest.main()
