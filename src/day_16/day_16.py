import math
import re
from dataclasses import dataclass
from itertools import permutations
from typing import List

import numpy

from utils import read_text_groups, flatten


@dataclass
class FieldRule:
    def __init__(self, range_one: range, range_two: range):
        self.range_one = range_one
        self.range_two = range_two

    def is_valid_value(self, value: int) -> bool:
        return value in self.range_one or value in self.range_two


FieldRules = dict[str, FieldRule]
Ticket = List[int]


def parse_input(file_name: str) -> (FieldRules, Ticket, List[Ticket]):
    groups: List[str] = read_text_groups(file_name)
    rules: FieldRules = parse_rules(groups[0].splitlines())
    my_ticket: Ticket = parse_ticket(groups[1])
    other_tickets: List[Ticket] = [parse_ticket(ticket) for ticket in groups[2].splitlines()]
    return rules, my_ticket, other_tickets


def parse_rules(rules: List[str]) -> FieldRules:
    rule_dict: FieldRules = {}
    for rule in rules:
        parse_rule_and_add(rule, rule_dict)
    return rule_dict


def parse_ticket(ticket_line: str) -> Ticket:
    return [int(field) for field in ticket_line.split(',')]


def parse_rule_and_add(rule: str, rules: FieldRules):
    result = re.match('^([A-Za-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', rule)
    rule_name = result.group(1)
    range_one = range(int(result.group(2)), int(result.group(3)) + 1)
    range_two = range(int(result.group(4)), int(result.group(5)) + 1)
    rules[rule_name] = FieldRule(range_one, range_two)


def get_ticket_error_rate(tickets: List[Ticket], rules: FieldRules) -> int:
    return sum([sum_invalid_fields(ticket, rules) for ticket in tickets])


def sum_invalid_fields(ticket: Ticket, rules: FieldRules) -> int:
    return sum([field for field in ticket if is_invalid_field(field, rules)])


def is_invalid_field(field: int, rules: FieldRules) -> bool:
    all_rules = rules.values()
    possible_rules = [r for r in all_rules if r.is_valid_value(field)]
    return len(possible_rules) == 0


def is_valid_ticket(ticket: Ticket, rules: FieldRules) -> bool:
    return all(not is_invalid_field(field, rules) for field in ticket)


def get_field_order(tickets: List[Ticket], rules: FieldRules) -> dict[str, int]:
    possible_positions = list(range(0, len(rules)))
    possible_field_positions = {field: possible_positions for field in rules.keys()}
    for ticket in tickets:
        knock_out_invalid_positions(possible_field_positions, ticket, rules)

    resolved = resolve_positions(possible_field_positions)
    return resolved


def knock_out_invalid_positions(possible_positions: dict[str, List[int]], ticket: Ticket, rules: FieldRules):
    for field, possible_so_far in possible_positions.items():
        rule = rules[field]
        updated = list(filter(lambda pos: rule.is_valid_value(ticket[pos]), possible_so_far))

        possible_positions[field] = updated


def resolve_positions(possible_field_positions: dict[str, List[int]]) -> dict[str, int]:
    resolved_positions: dict[str, int] = {}
    while len(possible_field_positions) > 0:
        determined_fields = list(filter(lambda e: len(e[1]) == 1, possible_field_positions.items()))
        for field, positions in determined_fields:
            position: int = possible_field_positions.pop(field)[0]
            resolved_positions[field] = position
            possible_field_positions = remove_from_all_values(possible_field_positions, position)

    return resolved_positions


def remove_from_all_values(possible_field_positions: dict[str, List[int]], position: int) -> dict[str, List[int]]:
    return {field: remove_value(positions, position) for field, positions in possible_field_positions.items()}


def remove_value(positions: List[int], position: int) -> List[int]:
    return list(filter(lambda pos: pos != position, positions))


def is_valid_field_order(tickets: List[Ticket], field_order: List[FieldRule]) -> bool:
    return all(is_valid_field_order_for_ticket(ticket, field_order) for ticket in tickets)


def is_valid_field_order_for_ticket(ticket: Ticket, field_order: List[FieldRule]) -> bool:
    zipped = zip(ticket, field_order)
    valid_positions = [rule for ticket_value, rule in zipped if rule.is_valid_value(ticket_value)]
    return len(valid_positions) == len(ticket)


if __name__ == '__main__':
    field_rules, my_ticket, other_tickets = parse_input('day_16.txt')
    print(get_ticket_error_rate(other_tickets, field_rules))
    valid_other_tickets: List[Ticket] = list(filter(lambda ticket: is_valid_ticket(ticket, field_rules), other_tickets))
    order = get_field_order(valid_other_tickets, field_rules)
    departure_only = list(filter(lambda e: 'departure' in e[0], order.items()))
    my_ticket_values = [my_ticket[pos] for _, pos in departure_only]
    print(math.prod(my_ticket_values))
