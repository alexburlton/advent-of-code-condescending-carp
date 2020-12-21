import unittest

from src.day_21.day_21 import *
from utils import read_text_list

example_lines = read_text_list('day_21_example.txt')


class TestDay21(unittest.TestCase):
    def test_get_ingredients_and_allergens(self):
        ingredients, allergens = get_ingredients_and_allergens('mxmxvkd kfcds sqjhc nhms (contains dairy, fish)')
        self.assertEqual(ingredients, {'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'})
        self.assertEqual(allergens, ['dairy', 'fish'])

    def test_get_ingredients_and_allergens_2(self):
        ingredients, allergens = get_ingredients_and_allergens('trh fvjkl sbzzf mxmxvkd (contains dairy)')
        self.assertEqual(ingredients, {'trh', 'fvjkl', 'sbzzf', 'mxmxvkd'})
        self.assertEqual(allergens, ['dairy'])

    def test_get_safe_ingredients(self):
        ingredients = get_safe_ingredients(example_lines)
        self.assertEqual(ingredients, {'kfcds', 'nhms', 'sbzzf', 'trh'})

    def test_count_safe_ingredient_appearances(self):
        count = count_safe_ingredient_appearances(example_lines)
        self.assertEqual(count, 5)

    def test_get_allergen_to_culprits_dict(self):
        result = get_allergen_to_culprits_dict(example_lines)
        self.assertEqual(result, {'dairy': {'mxmxvkd'}, 'fish': {'sqjhc', 'mxmxvkd'}, 'soy': {'sqjhc', 'fvjkl'}})

    def test_resolve_allergens(self):
        result = resolve_allergens({'dairy': {'mxmxvkd'}, 'fish': {'sqjhc', 'mxmxvkd'}, 'soy': {'sqjhc', 'fvjkl'}})
        self.assertEqual(result, {'dairy': 'mxmxvkd', 'fish': 'sqjhc', 'soy': 'fvjkl'})

    def test_get_canonical_dangerous_list(self):
        list = get_canonical_dangerous_list(example_lines)
        self.assertEqual(list, 'mxmxvkd,sqjhc,fvjkl')


if __name__ == '__main__':
    unittest.main()
