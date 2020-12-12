from typing import List

from utils import Point, add_points


class Ship:
    def __init__(self):
        self.current_position: Point = (0, 0)
        self.current_direction: Point = (1, 0)

    def move_forward(self, amount: int):
        vector: Point = (amount * self.current_direction[0], amount * self.current_direction[1])
        self.current_position = add_points(self.current_position, vector)

    def move_north(self, amount: int):
        self.current_position = add_points(self.current_position, (0, amount))

    def move_south(self, amount: int):
        self.current_position = add_points(self.current_position, (0, -amount))

    def move_east(self, amount: int):
        self.current_position = add_points(self.current_position, (amount, 0))

    def move_west(self, amount: int):
        self.current_position = add_points(self.current_position, (-amount, 0))

    def turn_right(self):
        self.current_direction = (self.current_direction[1], -self.current_direction[0])

    def turn_left(self):
        self.current_direction = (-self.current_direction[1], self.current_direction[0])

    def manhatten_distance(self) -> int:
        return abs(self.current_position[0]) + abs(self.current_position[1])