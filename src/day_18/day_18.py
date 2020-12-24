import re
from typing import List, Callable

from utils import read_text_list


def resolve_complex_expression(expression: str) -> int:
    simplified = simplify_expression_fully(expression, resolve_simple_expression)
    return resolve_simple_expression(simplified)


def resolve_complex_expression_b(expression: str) -> int:
    simplified = simplify_expression_fully(expression, resolve_simple_expression_b)
    return resolve_simple_expression_b(simplified)


def resolve_addition(expression: str) -> str:
    result = re.search(r'(\d+ \+ \d+)', expression)
    if result is None:
        return expression
    matched = result.group(1)
    return expression.replace(matched, str(resolve_simple_expression(matched)), 1)


def resolve_simple_expression_b(expression: str) -> int:
    simplified = expression
    while '+' in simplified:
        simplified = resolve_addition(simplified)
    return resolve_simple_expression(simplified)


def simplify_expression_fully(expression: str, resolve_simple: Callable[[str], int]) -> str:
    simplified = expression
    while '(' in simplified:
        simplified = simplify_expression(simplified, resolve_simple)
    return simplified


def simplify_expression(expression: str, resolve_simple: Callable[[str], int]) -> str:
    result = re.match(r'^.*(\([0-9 *+]+\)).*$', expression)
    if result is None:
        return expression
    matched = result.group(1)
    simple_expression = matched.replace('(', '').replace(')', '')
    return expression.replace(matched, str(resolve_simple(simple_expression)))


def resolve_simple_expression(expression: str) -> int:
    expression_parts: List[str] = expression.split(' ')
    total = int(expression_parts.pop(0))
    while len(expression_parts) > 0:
        operator = expression_parts.pop(0)
        operand = int(expression_parts.pop(0))
        total = process_next_instruction(total, operator, operand)

    return total


def process_next_instruction(total_so_far: int, operator: str, operand: int) -> int:
    if operator == '+':
        return total_so_far + operand
    else:
        return total_so_far * operand


def part_a(input_lines: List[str]) -> int:
    return sum([resolve_complex_expression(e) for e in input_lines])


def part_b(input_lines: List[str]) -> int:
    return sum([resolve_complex_expression_b(e) for e in input_lines])


if __name__ == '__main__':
    lines = read_text_list('day_18.txt')
    print(part_a(lines))
    print(part_b(lines))
