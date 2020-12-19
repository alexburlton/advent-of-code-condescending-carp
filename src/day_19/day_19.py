from dataclasses import dataclass
from typing import List

from utils import read_text_groups, count_where


class Rule:
    pass


@dataclass
class SimpleRule(Rule):
    character: str

    def __init__(self, character: str):
        self.character = character


@dataclass
class ChoiceRule(Rule):
    rule_one: Rule
    rule_two: Rule

    def __init__(self, rule_one: Rule, rule_two: Rule):
        self.rule_one = rule_one
        self.rule_two = rule_two


@dataclass
class MultiRule(Rule):
    rule_ids: List[int]

    def __init__(self, rule_ids: List[int]):
        self.rule_ids = rule_ids


def parse_rules(rule_lines: List[str]) -> dict[int, Rule]:
    all_rules: dict[int, Rule] = {}
    for rule in rule_lines:
        id_and_rule_str: List[str] = rule.split(': ')
        rule_id = int(id_and_rule_str[0])
        rule = parse_rule(id_and_rule_str[1])
        all_rules[rule_id] = rule

    return all_rules


def parse_rule(rule_str: str) -> Rule:
    if '"' in rule_str:
        character: str = rule_str.replace('"', '')
        return SimpleRule(character)
    elif '|' in rule_str:
        rules = [parse_rule(child) for child in rule_str.split(' | ')]
        return ChoiceRule(rules[0], rules[1])
    else:
        rule_ids = [int(child) for child in rule_str.split(' ')]
        return MultiRule(rule_ids)


def read_rules_and_messages(file_name: str) -> (dict[int, Rule], List[str]):
    groups = read_text_groups(file_name)
    rules = parse_rules(groups[0].splitlines())
    messages = groups[1].splitlines()
    return rules, messages


def count_valids(file_name: str) -> int:
    rules, messages = read_rules_and_messages(file_name)
    return count_where(lambda message: is_valid(rules, message), messages)


def is_valid(rules: dict[int, Rule], message: str) -> bool:
    remaining, valid = is_valid_rec(rules, message, rules[0])
    return valid and len(remaining) == 0


def is_valid_rec(rules: dict[int, Rule], message: str, rule: Rule) -> (str, bool):
    if isinstance(rule, SimpleRule):
        return message[1:], message.startswith(rule.character)
    elif isinstance(rule, MultiRule):
        rule_ids = rule.rule_ids
        valid = True
        remaining = message
        for id in rule_ids:
            remaining, was_valid = is_valid_rec(rules, remaining, rules[id])
            valid = valid and was_valid
        return remaining, valid
    elif isinstance(rule, ChoiceRule):
        remaining_one, valid_one = is_valid_rec(rules, message, rule.rule_one)
        if valid_one:
            return remaining_one, valid_one
        else:
            return is_valid_rec(rules, message, rule.rule_two)


if __name__ == '__main__':
    print(count_valids("day_19.txt"))