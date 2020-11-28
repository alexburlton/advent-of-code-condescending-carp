import math


def part_a(input_lines: list):
    fuel = 0
    for line in input_lines:
        fuel += calculate_fuel_for_mass(int(line))
    print(fuel)


def part_b(input_lines: list):
    fuel = 0
    for line in input_lines:
        fuel += calculate_adjusted_fuel_for_mass(int(line))
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


f = open("../resources/day_1_2019.txt", "r")
inputLines = f.readlines()

part_a(inputLines)
part_b(inputLines)
