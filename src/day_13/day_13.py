import math
from typing import List

import numpy

from utils import read_text_list


if __name__ == '__main__':
    lines = read_text_list('day_13.txt')
    arrival_time = int(lines[0])
    buses: List[int] = [int(bus) for bus in lines[1].replace(',x', '').split(',')]

    print(arrival_time)
    print(buses)

    remainders = [(bus, math.ceil(arrival_time/bus) * bus - arrival_time) for bus in buses]
    print(remainders)

    raw_bus_times = lines[1].split(',')
    print(raw_bus_times)

    noticed_factors = [983, 17, 23, 37]
    product = numpy.product(noticed_factors)
    added_number = 17

    id_with_offset = [(int(raw_bus_times[i]), i) for i in range(0, len(raw_bus_times)) if raw_bus_times[i] != 'x']
    id_with_offset = [(id_and_offset[0], id_and_offset[1] - added_number) for id_and_offset in id_with_offset if id_and_offset[0] not in noticed_factors]
    print(id_with_offset)

    starting_list = range(product, 1000000000000000, product)
    print(len(starting_list))
    for (bus, offset) in id_with_offset:
        starting_list = [i for i in starting_list if (i + offset) % bus == 0]
        print(len(starting_list))

    print(starting_list[0] - added_number)
