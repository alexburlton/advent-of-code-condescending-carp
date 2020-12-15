from typing import Callable, List

from utils import Point, add_points, read_text_list


class Ship:
    def __init__(self):
        self.current_position: Point = (0, 0)
        self.current_direction: Point = (1, 0)

    def process_instructions(self, instructions: List[str]):
        for instruction in instructions:
            self.process_instruction(instruction)

    def process_instruction(self, instruction: str):
        code: str = instruction[0]
        amount: int = int(instruction[1:])
        if code == 'F':
            self.move_forward(amount)
        elif code == 'N':
            self.move_north(amount)
        elif code == 'S':
            self.move_south(amount)
        elif code == 'E':
            self.move_east(amount)
        elif code == 'W':
            self.move_west(amount)
        elif code == 'R':
            self.turn_by_degrees(amount, self.turn_right)
        elif code == 'L':
            self.turn_by_degrees(amount, self.turn_left)

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

    @staticmethod
    def turn_by_degrees(degrees: int, turn_fn: Callable[[], None]):
        turns = int(degrees / 90)
        for i in range(0, turns):
            turn_fn()

    def turn_right(self):
        self.current_direction = (self.current_direction[1], -self.current_direction[0])

    def turn_left(self):
        self.current_direction = (-self.current_direction[1], self.current_direction[0])

    def manhatten_distance(self) -> int:
        return abs(self.current_position[0]) + abs(self.current_position[1])


class ShipAndWaypoint(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint_position = (10, 1)

    def move_forward(self, amount: int):
        vector: Point = (amount * self.waypoint_position[0], amount * self.waypoint_position[1])
        self.current_position = add_points(self.current_position, vector)

    def move_north(self, amount: int):
        self.waypoint_position = add_points(self.waypoint_position, (0, amount))

    def move_south(self, amount: int):
        self.waypoint_position = add_points(self.waypoint_position, (0, -amount))

    def move_east(self, amount: int):
        self.waypoint_position = add_points(self.waypoint_position, (amount, 0))

    def move_west(self, amount: int):
        self.waypoint_position = add_points(self.waypoint_position, (-amount, 0))

    def turn_right(self):
        self.waypoint_position = (self.waypoint_position[1], -self.waypoint_position[0])

    def turn_left(self):
        self.waypoint_position = (-self.waypoint_position[1], self.waypoint_position[0])


if __name__ == '__main__':
    lines = read_text_list('day_12.txt')
    ship: Ship = Ship()
    ship.process_instructions(lines)
    print(ship.manhatten_distance())

    shipAndWaypoint: ShipAndWaypoint = ShipAndWaypoint()
    shipAndWaypoint.process_instructions(lines)
    print(shipAndWaypoint.manhatten_distance())
