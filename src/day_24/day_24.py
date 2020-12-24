from dataclasses import dataclass
from typing import List, Set

from utils import read_text_list, count_where


@dataclass
class Hex(object):
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        if x + y + z != 0:
            raise ValueError('Coordinates must add up to 0 for a valid Hex tile!')

        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def east(self) -> 'Hex':
        return Hex(self.x + 1, self.y - 1, self.z)

    def west(self) -> 'Hex':
        return Hex(self.x - 1, self.y + 1, self.z)

    def north_east(self) -> 'Hex':
        return Hex(self.x + 1, self.y, self.z - 1)

    def south_west(self) -> 'Hex':
        return Hex(self.x - 1, self.y, self.z + 1)

    def north_west(self) -> 'Hex':
        return Hex(self.x, self.y + 1, self.z - 1)

    def south_east(self) -> 'Hex':
        return Hex(self.x, self.y - 1, self.z + 1)

    def neighbours(self) -> Set['Hex']:
        return {self.east(), self.west(), self.north_east(), self.north_west(), self.south_east(), self.south_west()}


def line_to_hex(instruction_line: str) -> Hex:
    result = Hex(0, 0, 0)
    movements = split_instruction(instruction_line)
    for movement in movements:
        if movement == 'e':
            result = result.east()
        elif movement == 'w':
            result = result.west()
        elif movement == 'ne':
            result = result.north_east()
        elif movement == 'nw':
            result = result.north_west()
        elif movement == 'se':
            result = result.south_east()
        else:
            result = result.south_west()

    return result


def split_instruction(line: str) -> List[str]:
    character_list = list(line)
    resulting_list = []
    while len(character_list) > 0:
        first_char = character_list.pop(0)
        second_char = ''
        if first_char == 'n' or first_char == 's':
            second_char = character_list.pop(0)

        resulting_list.append(first_char + second_char)

    return resulting_list


def parse_black_tiles(file_name: str) -> Set[Hex]:
    lines = read_text_list(file_name)
    tiles = [line_to_hex(line) for line in lines]
    return {tile for tile in tiles if tiles.count(tile) % 2 != 0}


def iterate_tiles(black_tiles: Set[Hex]) -> Set[Hex]:
    return {tile for tile in get_tiles_to_consider(black_tiles) if iterate_tile(tile, black_tiles)}


def get_tiles_to_consider(black_tiles: Set[Hex]) -> Set[Hex]:
    all_neighbours = [tile.neighbours() for tile in black_tiles]
    return set.union(*all_neighbours)


def iterate_tile(tile: Hex, black_tiles: Set[Hex]) -> bool:
    currently_black = tile in black_tiles
    neighbour_black_count = count_where(lambda neighbour: neighbour in black_tiles, tile.neighbours())
    return flip_tile(currently_black, neighbour_black_count)


def flip_tile(currently_black: bool, neighbour_black_count: int) -> bool:
    if currently_black:
        # Stays black if 1 or 2 neighbours are black
        return neighbour_black_count in [1, 2]
    else:
        # Flips to black if exactly 2 neighbours are black
        return neighbour_black_count == 2


def part_a(file_name: str) -> int:
    return len(parse_black_tiles(file_name))


def part_b(file_name: str) -> int:
    black_tiles = parse_black_tiles(file_name)
    for _ in range(0, 100):
        black_tiles = iterate_tiles(black_tiles)

    return len(black_tiles)


if __name__ == '__main__':
    print(part_a('day_24.txt'))
    print(part_b('day_24.txt'))
