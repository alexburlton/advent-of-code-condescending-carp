from typing import List, Optional


class Node(object):
    value: int
    next: 'Node'

    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = self


class CircularLinkedList(object):
    value_to_node: dict[int, Node] = {}

    def __init__(self, regular_list: List[int]):
        first_value = regular_list.pop(0)
        first_node = Node(first_value)
        self.value_to_node[first_value] = first_node
        previous_node = first_node
        for item in regular_list:
            node = Node(item)
            previous_node.next = node
            previous_node = node
            self.value_to_node[item] = node

        # Complete the circle by joining the final node to the first one
        previous_node.next = self.value_to_node[first_value]

    def get_node_with_value(self, value: int) -> Node:
        return self.value_to_node[value]

    def insert_after(self, node: Node, value_to_insert: int):
        old_next = node.next
        new_node = Node(value_to_insert)
        new_node.next = old_next
        node.next = new_node
        self.value_to_node[value_to_insert] = new_node

    def remove_after(self, node: Node) -> int:
        node_to_remove = node.next
        new_next = node_to_remove.next
        node.next = new_next
        self.value_to_node.pop(node_to_remove.value)
        return node_to_remove.value

    def to_string(self, start_value: int):
        first_node = self.value_to_node[start_value]
        result = str(first_node.value)
        current_node = first_node.next
        while current_node.value != first_node.value:
            result += ',' + str(current_node.value)
            current_node = current_node.next
        return result


def iterate_cups(initial_cups: str, cup_count: int, turns: int) -> CircularLinkedList:
    linked_list = prepare_linked_list(initial_cups, cup_count)

    starting_cup = int(initial_cups[0])

    max_cup = cup_count
    current_cup_node = linked_list.get_node_with_value(starting_cup)
    for turn in range(0, turns):
        removed_cups = []
        for i in range(0, 3):
            removed_cup = linked_list.remove_after(current_cup_node)
            removed_cups.append(removed_cup)

        destination_cup = find_destination_cup(current_cup_node.value, removed_cups, max_cup)

        destination_cup_node = linked_list.get_node_with_value(destination_cup)
        for removed in reversed(removed_cups):
            linked_list.insert_after(destination_cup_node, removed)

        current_cup_node = current_cup_node.next

    return linked_list


def prepare_linked_list(initial_cups: str, cup_count: int) -> CircularLinkedList:
    cups = [int(cup) for cup in initial_cups]
    cups = pad_cups(cups, cup_count)
    return CircularLinkedList(cups)


def part_a(input_str: str) -> str:
    result = iterate_cups(input_str, 9, 100)
    result_str = result.to_string(1)
    result_str = result_str.replace(',', '')
    return result_str[1::]


def part_b(input_str: str):
    result = iterate_cups(input_str, 1000000, 10000000)
    cup_1_node = result.get_node_with_value(1)
    next_node = cup_1_node.next
    next_next_node = next_node.next
    print(next_node.value)
    print(next_next_node.value)
    return next_node.value * next_next_node.value


def pad_cups(cups: List[int], cup_count: int) -> List[int]:
    padded_cups = cups.copy()
    current_max = max(cups)
    current_count = len(cups)
    for i in range(current_count, cup_count):
        padded_cups.append(current_max + 1)
        current_max = current_max + 1

    return padded_cups


def find_destination_cup(current_cup: int, removed_cups: List[int], max_cup: int) -> int:
    candidate = next_destination_cup(current_cup, max_cup)
    while candidate in removed_cups:
        candidate = next_destination_cup(candidate, max_cup)
    return candidate


def next_destination_cup(current_candidate: int, max_cup: int) -> int:
    result = current_candidate - 1
    if result == 0:
        return max_cup
    else:
        return result


if __name__ == '__main__':
    print(part_a('318946572'))
    print(part_b('318946572'))
