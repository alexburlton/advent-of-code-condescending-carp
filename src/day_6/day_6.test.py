import unittest

from src.day_6.day_6 import *


class TestDay6(unittest.TestCase):

    def test_read_customs_groups(self):
        self.assertEqual(read_customs_groups('day_6_example.txt'), ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b'])

    def test_count_unique_answers(self):
        self.assertEqual(count_unique_answers('abc'), 3)
        self.assertEqual(count_unique_answers('a\nb\nc'), 3)
        self.assertEqual(count_unique_answers('ab\nac'), 3)
        self.assertEqual(count_unique_answers('a\na\na\na'), 1)
        self.assertEqual(count_unique_answers('b'), 1)

    def test_part_a(self):
        self.assertEqual(part_a('day_6_example.txt'), 11)

    def test_count_answers_given_by_all(self):
        self.assertEqual(count_answers_given_by_all('abc'), 3)
        self.assertEqual(count_answers_given_by_all('a\nb\nc'), 0)
        self.assertEqual(count_answers_given_by_all('ab\nac'), 1)
        self.assertEqual(count_answers_given_by_all('a\na\na\na'), 1)
        self.assertEqual(count_answers_given_by_all('b'), 1)

    def test_part_b(self):
        self.assertEqual(part_b('day_6_example.txt'), 6)


if __name__ == '__main__':
    unittest.main()
