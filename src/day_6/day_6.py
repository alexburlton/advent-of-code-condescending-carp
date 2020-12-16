from typing import List

from utils import read_text_groups


def count_unique_answers(customs_group: str) -> int:
    stripped_group = customs_group.replace('\n', '')
    return len(set(stripped_group))


def count_answers_given_by_all(customs_group: str) -> int:
    individual_answers = customs_group.split('\n')
    answer_sets = [set(answers) for answers in individual_answers]
    return len(set.intersection(*answer_sets))


def part_a(file_name: str) -> int:
    groups = read_text_groups(file_name)
    counts = [count_unique_answers(group) for group in groups]
    return sum(counts)


def part_b(file_name: str) -> int:
    groups = read_text_groups(file_name)
    counts = [count_answers_given_by_all(group) for group in groups]
    return sum(counts)


if __name__ == '__main__':
    print(part_a('day_6.txt'))
    print(part_b('day_6.txt'))
