from dataclasses import dataclass
from typing import List, Set

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
    rules: List[Rule]

    def __init__(self, rules: List[Rule]):
        self.rules = rules


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
        return ChoiceRule(rules)
    else:
        rule_ids = [int(child) for child in rule_str.split(' ')]
        return MultiRule(rule_ids)


def read_rules_and_messages(file_name: str) -> (dict[int, Rule], List[str]):
    groups = read_text_groups(file_name)
    rules = parse_rules(groups[0].splitlines())
    messages = groups[1].splitlines()
    return rules, messages


def count_valids(rules: dict[int, Rule], messages: List[str]) -> int:
    return count_where(lambda message: is_valid(rules, message), messages)


def is_valid(rules: dict[int, Rule], message: str) -> bool:
    return len(message) in test_rule(message, rules, rules[0])


def test_rule(message: str, rules: dict[int, Rule], rule: Rule) -> Set[int]:
    if len(message) == 0:
        return set()

    if isinstance(rule, SimpleRule):
        return {1} if (message[0] == rule.character) else set()
    elif isinstance(rule, MultiRule):
        return test_multi_rule(message, rules, rule)
    elif isinstance(rule, ChoiceRule):
        overall_matches = set()
        for choice in rule.rules:
            overall_matches |= test_rule(message, rules, choice)
        return overall_matches


def test_multi_rule(message: str, rules: dict[int, Rule], rule: MultiRule) -> Set[int]:
    child_rules = rule.rule_ids
    matches = {0}
    for rule_id in child_rules:
        new_match = set()
        for n in matches:
            new_match |= {n + m for m in test_rule(message[n:], rules, rules[rule_id])}
        matches = new_match
    return matches


def update_rules_for_part_b(rules: dict[int, Rule]):
    rules[8] = parse_rule('42 | 42 8')
    rules[11] = parse_rule('42 31 | 42 11 31')


if __name__ == '__main__':
    rules_and_messages = read_rules_and_messages('day_19.txt')
    print(count_valids(rules_and_messages[0], rules_and_messages[1]))

    update_rules_for_part_b(rules_and_messages[0])
    print(count_valids(rules_and_messages[0], rules_and_messages[1]))
