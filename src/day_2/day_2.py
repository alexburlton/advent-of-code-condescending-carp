from typing import NamedTuple, List

from utils import read_text_list


class PasswordAndRule(NamedTuple):
    password: str
    ruleMin: int
    ruleMax: int
    ruleLetter: str


def parse_password_line(line: str) -> PasswordAndRule:
    rule_and_password = line.split(': ')
    rule: str = rule_and_password[0]
    password: str = rule_and_password[1]

    numbers_and_letter = rule.split(' ')
    numbers = numbers_and_letter[0].split('-')

    return PasswordAndRule(password=password,
                           ruleMin=int(numbers[0]),
                           ruleMax=int(numbers[1]),
                           ruleLetter=numbers_and_letter[1])


def is_valid(rule: PasswordAndRule) -> bool:
    count: int = rule.password.count(rule.ruleLetter)
    return rule.ruleMin <= count <= rule.ruleMax


def is_valid_new_way(rule: PasswordAndRule) -> bool:
    first_char_correct = rule.password[rule.ruleMin - 1] == rule.ruleLetter
    second_char_correct = rule.password[rule.ruleMax - 1] == rule.ruleLetter
    return first_char_correct != second_char_correct


def parse_lines(password_list: List[str]) -> List[PasswordAndRule]:
    return list(map(parse_password_line, password_list))


def count_valid(password_list: List[str]) -> int:
    parsed_lines: List[PasswordAndRule] = parse_lines(password_list)
    return len(list(filter(is_valid, parsed_lines)))


def count_valid_new_way(password_list: List[str]) -> int:
    parsed_lines: List[PasswordAndRule] = parse_lines(password_list)
    return len(list(filter(is_valid_new_way, parsed_lines)))


def part_a(input_lines: List[str]) -> None:
    print(count_valid(input_lines))


def part_b(input_lines: List[str]) -> None:
    print(count_valid_new_way(input_lines))


if __name__ == '__main__':
    inputLines = read_text_list("day_2.txt")

    part_a(inputLines)
    part_b(inputLines)
