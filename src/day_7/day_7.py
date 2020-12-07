import re
from dataclasses import dataclass
from typing import List

from utils import read_text_list


@dataclass
class BagAndCount:
    attribute: str
    count: int


def parse_bag_attribute(bag_desc: str) -> str:
    result = bag_desc.replace(' bags', '')
    result = result.replace(' bag', '')
    return result


def parse_bag_and_count(bag_and_count_desc: str) -> BagAndCount:
    stripped = bag_and_count_desc.replace('.', '')
    count = re.match('^([0-9]+).*$', stripped).group(1)
    attribute = parse_bag_attribute(stripped.replace(count, '').lstrip())
    return BagAndCount(attribute, int(count))


def parse_bag_contents(bag_contents: str) -> List[BagAndCount]:
    if bag_contents == 'no other bags.':
        return []

    bags_with_counts = bag_contents.split(', ')
    return [parse_bag_and_count(value) for value in bags_with_counts]


def parse_bag_fact(bag_fact: str) -> dict[str, List[BagAndCount]]:
    split = bag_fact.split(' contain ')
    parent_attribute = parse_bag_attribute(split[0])
    contents = parse_bag_contents(split[1])
    return {parent_attribute: contents}


def parse_bag_hierarchy(bag_fact_lines: List[str]) -> dict[str, List[BagAndCount]]:
    bag_facts = [parse_bag_fact(line) for line in bag_fact_lines]
    result: dict[str, List[BagAndCount]] = {}
    for fact in bag_facts:
        result.update(fact)

    return result


def get_possible_containers(bag_hierarchy: dict[str, List[BagAndCount]], bag: str) -> set[str]:
    direct_parents = {parent for (parent, children) in bag_hierarchy.items() if contains_bag(children, bag)}
    if len(direct_parents) == 0:
        return set()
    return set.union(direct_parents, *[get_possible_containers(bag_hierarchy, parent) for parent in direct_parents])


def contains_bag(children: List[BagAndCount], bag: str) -> bool:
    bag_attributes = [bag.attribute for bag in children]
    return bag in bag_attributes


def count_contents(bag_hierarchy: dict[str, List[BagAndCount]], bag: str) -> int:
    contents: List[BagAndCount] = bag_hierarchy.get(bag, [])
    return sum([content.count * (1 + count_contents(bag_hierarchy, content.attribute)) for content in contents])


if __name__ == '__main__':
    input_lines = read_text_list('day_7.txt')
    hierarchy = parse_bag_hierarchy(input_lines)
    print(len(get_possible_containers(hierarchy, 'shiny gold')))
    print(count_contents(hierarchy, 'shiny gold'))
