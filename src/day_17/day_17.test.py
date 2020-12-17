import unittest

from src.day_17.day_17 import *


class TestDay16(unittest.TestCase):
    def test_add_points(self):
        self.assertEqual(Point3D(0, 1, 5) + Point3D(-2, 2, 3), Point3D(-2, 3, 8))

    def test_neighbours(self):
        pt: Point3D = Point3D(1, 1, 1)
        neighbours: List[Point3D] = pt.neighbours()
        self.assertEqual(len(neighbours), 26)
        self.assertTrue(Point3D(0, 0, 0) in neighbours)
        self.assertFalse(Point3D(1, 1, 1) in neighbours)

    def test_read_input(self):
        grid: Grid = read_input_3d('day_17_example.txt')
        self.assertEqual(grid,
                         {
                             Point3D(0, 0, 0): False,
                             Point3D(1, 0, 0): True,
                             Point3D(2, 0, 0): False,
                             Point3D(0, 1, 0): False,
                             Point3D(1, 1, 0): False,
                             Point3D(2, 1, 0): True,
                             Point3D(0, 2, 0): True,
                             Point3D(1, 2, 0): True,
                             Point3D(2, 2, 0): True,
                         })

    def test_part_a(self):
        self.assertEqual(part_a('day_17_example.txt'), 112)

    def test_add_4d_points(self):
        self.assertEqual(Point4D(0, 1, 5, -3) + Point4D(-2, 2, 3, 7), Point4D(-2, 3, 8, 4))

    def test_neighbours_4d(self):
        pt: Point4D = Point4D(1, 1, 1, 1)
        neighbours: List[Point4D] = pt.neighbours()
        self.assertEqual(len(neighbours), 80)
        self.assertTrue(Point4D(0, 0, 0, 0) in neighbours)
        self.assertFalse(Point4D(1, 1, 1, 1) in neighbours)

    def test_read_input_4d(self):
        grid: Grid4D = read_input_4d('day_17_example.txt')
        self.assertEqual(grid,
                         {
                             Point4D(0, 0, 0, 0): False,
                             Point4D(1, 0, 0, 0): True,
                             Point4D(2, 0, 0, 0): False,
                             Point4D(0, 1, 0, 0): False,
                             Point4D(1, 1, 0, 0): False,
                             Point4D(2, 1, 0, 0): True,
                             Point4D(0, 2, 0, 0): True,
                             Point4D(1, 2, 0, 0): True,
                             Point4D(2, 2, 0, 0): True,
                         })

    def test_part_b(self):
        self.assertEqual(part_b('day_17_example.txt'), 848)


if __name__ == '__main__':
    unittest.main()
