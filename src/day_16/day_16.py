import re
from typing import List

from utils import read_text_groups, count_where, flatten

FieldRules = dict[str, List[range]]
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
    rules[rule_name] = [range_one, range_two]


def get_ticket_error_rate(tickets: List[Ticket], rules: FieldRules) -> int:
    return sum([sum_invalid_fields(ticket, rules) for ticket in tickets])


def sum_invalid_fields(ticket: Ticket, rules: FieldRules) -> int:
    return sum([field for field in ticket if is_invalid_field(field, rules)])


def is_invalid_field(field: int, rules: FieldRules) -> bool:
    all_ranges = flatten(list(rules.values()))
    possible_ranges = [r for r in all_ranges if field in r]
    return len(possible_ranges) == 0


if __name__ == '__main__':
    rules, my_ticket, other_tickets = parse_input('day_16.txt')
    print(get_ticket_error_rate(other_tickets, rules))
