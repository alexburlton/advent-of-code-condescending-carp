import unittest

from src.day_18.day_18 import *


class TestDay18(unittest.TestCase):
    def test_process_next_instruction(self):
        total = 30
        self.assertEqual(process_next_instruction(total, '+', 40), 70)
        self.assertEqual(process_next_instruction(total, '*', 3), 90)

    def test_resolve_simple_expression(self):
        self.assertEqual(resolve_simple_expression('1 + 2 * 3 + 4 * 5 + 6'), 71)
        self.assertEqual(resolve_simple_expression('51'), 51)

    def test_simplify_expression_no_op(self):
        self.assertEqual(simplify_expression('1 + 2 * 3 + 4 * 5 + 6', resolve_simple_expression), '1 + 2 * 3 + 4 * 5 + 6')

    def test_simplify_expression(self):
        self.assertEqual(simplify_expression('1 + (2 * 3) + (4 * (5 + 6))', resolve_simple_expression), '1 + (2 * 3) + (4 * 11)')
        self.assertEqual(simplify_expression('1 + (2 * 3) + (4 * 11)', resolve_simple_expression), '1 + (2 * 3) + 44')
        self.assertEqual(simplify_expression('1 + (2 * 3) + 44', resolve_simple_expression), '1 + 6 + 44')

    def test_resolve_complex_expression(self):
        self.assertEqual(resolve_complex_expression('1 + 2 * 3 + 4 * 5 + 6'), 71)
        self.assertEqual(resolve_complex_expression('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(resolve_complex_expression('2 * 3 + (4 * 5)'), 26)
        self.assertEqual(resolve_complex_expression('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
        self.assertEqual(resolve_complex_expression('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)
        self.assertEqual(resolve_complex_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)

    def test_resolve_addition(self):
        self.assertEqual(resolve_addition('58 + 6'), '64')
        self.assertEqual(resolve_addition('15 * 8 + 6'), '15 * 14')
        self.assertEqual(resolve_addition('15 * 20 + 6 * 2 + 15'), '15 * 26 * 2 + 15')
        self.assertEqual(resolve_addition('15 * 26 * 2 + 15'), '15 * 26 * 17')
        self.assertEqual(resolve_addition('15 * 26 * 17'), '15 * 26 * 17')

    def test_resolve_simple_expression_b(self):
        self.assertEqual(resolve_simple_expression_b('1 + 2 * 3 + 4 * 5 + 6'), 231)
        self.assertEqual(resolve_simple_expression_b('1 + 6 + 44'), 51)
        self.assertEqual(resolve_simple_expression_b('11664 + 2 + 4 * 2'), 23340)

    def test_resolve_complex_expression_b(self):
        self.assertEqual(resolve_complex_expression_b('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(resolve_complex_expression_b('2 * 3 + (4 * 5)'), 46)
        self.assertEqual(resolve_complex_expression_b('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)
        self.assertEqual(resolve_complex_expression_b('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)
        self.assertEqual(resolve_complex_expression_b('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)


if __name__ == '__main__':
    unittest.main()
