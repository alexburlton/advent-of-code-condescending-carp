import math
from typing import List

import numpy

from utils import read_text_list


def part_b(bus_times: str) -> int:
    raw_bus_times = bus_times.split(',')
    buses_with_offset = [(int(raw_bus_times[i]), i) for i in range(0, len(raw_bus_times)) if raw_bus_times[i] != 'x']
    buses_with_offset = list(reversed(sorted(buses_with_offset, key=lambda item: item[0])))

    candidate = 1
    amount_to_add = 1
    bus, offset = buses_with_offset.pop(0)

    found = False
    while not found:
        if (candidate + offset) % bus == 0:
            if len(buses_with_offset) == 0:
                found = True
            else:
                amount_to_add *= bus
                bus, offset = buses_with_offset.pop(0)
        else:
            candidate += amount_to_add

    return candidate


def part_a(input_lines: List[str]) -> int:
    arrival_time = int(input_lines[0])
    buses: List[int] = [int(bus) for bus in input_lines[1].replace(',x', '').split(',')]
    remainders = [(bus, math.ceil(arrival_time / bus) * bus - arrival_time) for bus in buses]
    best_bus = min(remainders, key=lambda bus_and_wait: bus_and_wait[1])
    return best_bus[0] * best_bus[1]


if __name__ == '__main__':
    lines = read_text_list('day_13.txt')
    print(part_a(lines))
    print(part_b(lines[1]))
