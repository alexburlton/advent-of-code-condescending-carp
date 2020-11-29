import unittest

from src.day_1_2019.day_1_2019 import *


class TestDay1(unittest.TestCase):

    def test_calculate_fuel_for_mass(self):
        self.assertEqual(calculate_fuel_for_mass(12), 2)
        self.assertEqual(calculate_fuel_for_mass(14), 2)
        self.assertEqual(calculate_fuel_for_mass(1969), 654)
        self.assertEqual(calculate_fuel_for_mass(100756), 33583)

    def test_calculate_adjusted_fuel_for_mass(self):
        self.assertEqual(calculate_adjusted_fuel_for_mass(14), 2)
        self.assertEqual(calculate_adjusted_fuel_for_mass(1969), 966)
        self.assertEqual(calculate_adjusted_fuel_for_mass(100756), 50346)


if __name__ == '__main__':
    unittest.main()
