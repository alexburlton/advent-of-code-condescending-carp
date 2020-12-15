import unittest

from src.day_11.day_11 import *

example_grid = read_coordinate_grid('day_11_example.txt')


class TestDay11(unittest.TestCase):
    def test_is_occupied(self):
        self.assertTrue(is_occupied('#'))
        self.assertFalse(is_occupied('L'))
        self.assertFalse(is_occupied('.'))
        self.assertFalse(is_occupied('@'))

    def test_is_seat(self):
        self.assertTrue(is_seat('#'))
        self.assertTrue(is_seat('L'))
        self.assertFalse(is_seat('.'))
        self.assertFalse(is_seat('@'))

    def test_get_new_value_for_empty_seat(self):
        self.assertEqual(get_new_value('L', 0, 4), '#')
        self.assertEqual(get_new_value('L', 1, 4), 'L')
        self.assertEqual(get_new_value('L', 2, 4), 'L')
        self.assertEqual(get_new_value('L', 3, 4), 'L')
        self.assertEqual(get_new_value('L', 4, 4), 'L')

    def test_get_new_value_for_occupied_seat(self):
        self.assertEqual(get_new_value('#', 0, 2), '#')
        self.assertEqual(get_new_value('#', 1, 2), '#')
        self.assertEqual(get_new_value('#', 2, 2), 'L')
        self.assertEqual(get_new_value('#', 3, 2), 'L')
        self.assertEqual(get_new_value('#', 4, 2), 'L')

    def test_count_occupied(self):
        self.assertEqual(count_occupied(['#', 'L', '.', '.', '#']), 2)
        self.assertEqual(count_occupied([]), 0)

    def test_iterate_grid_part_a(self):
        self.assertEqual(self.iterate_part_a('day_11_example.txt'), read_coordinate_grid('day_11_a_1.txt'))
        self.assertEqual(self.iterate_part_a('day_11_a_1.txt'), read_coordinate_grid('day_11_a_2.txt'))
        self.assertEqual(self.iterate_part_a('day_11_a_2.txt'), read_coordinate_grid('day_11_a_3.txt'))
        self.assertEqual(self.iterate_part_a('day_11_a_3.txt'), read_coordinate_grid('day_11_a_4.txt'))
        self.assertEqual(self.iterate_part_a('day_11_a_4.txt'), read_coordinate_grid('day_11_a_5.txt'))
        self.assertEqual(self.iterate_part_a('day_11_a_5.txt'), read_coordinate_grid('day_11_a_5.txt'))

    @staticmethod
    def iterate_part_a(file_name: str):
        return iterate_grid(read_coordinate_grid(file_name), iterate_seat_part_a)

    def test_part_a(self):
        self.assertEqual(part_a(example_grid), 37)

    def test_get_visible_occupied_seats_1(self):
        grid = read_coordinate_grid('day_11_b_sight_example_1.txt')
        self.assertEqual(get_visible_occupied_seats(grid, (3, 4)), 8)

    def test_get_visible_occupied_seats_2(self):
        grid = read_coordinate_grid('day_11_b_sight_example_2.txt')
        self.assertEqual(get_visible_occupied_seats(grid, (1, 1)), 0)
        self.assertEqual(get_visible_occupied_seats(grid, (3, 1)), 1)
        self.assertEqual(get_visible_occupied_seats(grid, (5, 1)), 1)
        self.assertEqual(get_visible_occupied_seats(grid, (7, 1)), 2)

    def test_get_visible_occupied_seats_3(self):
        grid = read_coordinate_grid('day_11_b_sight_example_3.txt')
        self.assertEqual(get_visible_occupied_seats(grid, (3, 3)), 0)

    def test_iterate_grid_part_b(self):
        self.assertEqual(self.iterate_part_b('day_11_example.txt'), read_coordinate_grid('day_11_b_1.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_1.txt'), read_coordinate_grid('day_11_b_2.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_2.txt'), read_coordinate_grid('day_11_b_3.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_3.txt'), read_coordinate_grid('day_11_b_4.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_4.txt'), read_coordinate_grid('day_11_b_5.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_5.txt'), read_coordinate_grid('day_11_b_6.txt'))
        self.assertEqual(self.iterate_part_b('day_11_b_6.txt'), read_coordinate_grid('day_11_b_6.txt'))

    @staticmethod
    def iterate_part_b(file_name: str):
        return iterate_grid(read_coordinate_grid(file_name), iterate_seat_part_b)

    def test_part_b(self):
        self.assertEqual(part_b(example_grid), 26)


if __name__ == '__main__':
    unittest.main()
