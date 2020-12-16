import re
from typing import List

from utils import read_text_groups

FieldRules = dict[str, tuple[range, range]]
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
    range_one = range(int(result.group(2)), int(result.group(3)))
    range_two = range(int(result.group(4)), int(result.group(5)))
    rules[rule_name] = (range_one, range_two)
