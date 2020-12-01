import math

from typing import List

from utils import read_integer_list


def part_a(input_lines: List[int]) -> None:
    fuels = map(calculate_fuel_for_mass, input_lines)
    fuel = sum(fuels)
    print(fuel)


def part_b(input_lines: List[int]) -> None:
    fuels = map(calculate_adjusted_fuel_for_mass, input_lines)
    fuel = sum(fuels)
    print(fuel)


def calculate_fuel_for_mass(mass: int) -> int:
    return math.floor(mass / 3) - 2


def calculate_adjusted_fuel_for_mass(mass: int) -> int:
    total_fuel = calculate_fuel_for_mass(mass)
    fuel_to_add = calculate_fuel_for_mass(total_fuel)
    while fuel_to_add > 0:
        total_fuel += fuel_to_add
        fuel_to_add = calculate_fuel_for_mass(fuel_to_add)
    return total_fuel


if __name__ == '__main__':
    inputLines = read_integer_list("day_1_2019.txt")

    part_a(inputLines)
    part_b(inputLines)
