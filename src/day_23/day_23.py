from typing import List

EXAMPLE_INPUT = '389125467'


def iterate_cups(initial_cups: str):
    cups = [int(cup) for cup in initial_cups]
    max_cup = max(cups)
    current_cup_index = 0
    for turn in range(0, 100):
        current_cup = cups[current_cup_index]

        removed_cups = []
        index_to_remove = (current_cup_index + 1) % (len(cups))
        for i in range(0, 3):
            removed_cup = cups.pop(index_to_remove)
            removed_cups.append(removed_cup)
            index_to_remove = index_to_remove % len(cups)

        destination_cup = find_destination_cup(current_cup, cups, max_cup)

        destination_index = cups.index(destination_cup)
        for removed in reversed(removed_cups):
            cups.insert(destination_index + 1, removed)

        current_cup_index = cups.index(current_cup)
        current_cup_index = (current_cup_index + 1) % (len(cups))

    return ''.join([str(cup) for cup in cups])


def find_destination_cup(current_cup: int, remaining_cups: List[int], max_cup: int) -> int:
    candidate = next_destination_cup(current_cup, max_cup)
    while candidate not in remaining_cups:
        candidate = next_destination_cup(candidate, max_cup)
    return candidate


def next_destination_cup(current_candidate: int, max_cup: int) -> int:
    result = current_candidate - 1
    if result < 0:
        return max_cup
    else:
        return result


if __name__ == '__main__':
    print(iterate_cups('318946572'))
