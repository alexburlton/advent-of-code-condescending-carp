import re
from typing import Set, List

from utils import flatten, count_where, read_text_list

Ingredient = str
Allergen = str


def get_ingredients_and_allergens(input_line: str) -> tuple[Set[Ingredient], List[Allergen]]:
    match_result = re.match(r'^([a-z ]+) \(contains ([a-z, ]+)\)$', input_line)
    ingredients: Set[Ingredient] = set(match_result.group(1).split(' '))
    allergens: List[Allergen] = match_result.group(2).split(', ')
    return ingredients, allergens


def get_safe_ingredients(input_lines: List[str]) -> Set[Ingredient]:
    allergen_to_possible_culprits = get_allergen_to_culprits_dict(input_lines)
    all_ingredients = set(get_all_ingredients_flat(input_lines))

    unsafe_ingredients = set.union(*allergen_to_possible_culprits.values())
    return all_ingredients.difference(unsafe_ingredients)


def get_allergen_to_culprits_dict(input_lines: List[str]) -> dict[Allergen, Set[Ingredient]]:
    allergen_to_possible_culprits: dict[Allergen, Set[Ingredient]] = {}
    for line in input_lines:
        ingredients, allergens = get_ingredients_and_allergens(line)
        for allergen in allergens:
            known_culprits = allergen_to_possible_culprits.get(allergen, ingredients)
            allergen_to_possible_culprits[allergen] = known_culprits.intersection(ingredients)

    return allergen_to_possible_culprits


def get_all_ingredients_flat(input_lines: List[str]) -> List[Ingredient]:
    return flatten([list(get_ingredients_and_allergens(line)[0]) for line in input_lines])


def count_safe_ingredient_appearances(input_lines: List[str]) -> int:
    safe = get_safe_ingredients(input_lines)
    all_ingredient_occurrences: List[Ingredient] = get_all_ingredients_flat(input_lines)
    return count_where(lambda ingredient: ingredient in safe, all_ingredient_occurrences)


def get_canonical_dangerous_list(input_lines: List[str]) -> str:
    allergen_to_culprits = get_allergen_to_culprits_dict(input_lines)
    resolved = resolve_allergens(allergen_to_culprits)
    alphabetical_allergens = sorted(resolved.keys())
    ingredients = [resolved[allergen] for allergen in alphabetical_allergens]
    return ','.join(ingredients)


def resolve_allergens(possible_allergens: dict[Allergen, Set[Ingredient]]) -> dict[Allergen, Ingredient]:
    resolved_positions: dict[Allergen, Ingredient] = {}
    while len(possible_allergens) > 0:
        determined_fields = list(filter(lambda e: len(e[1]) == 1, possible_allergens.items()))
        for allergen, ingredients in determined_fields:
            ingredient: Ingredient = possible_allergens.pop(allergen).pop()
            resolved_positions[allergen] = ingredient
            remove_from_all_values(possible_allergens, ingredient)

    return resolved_positions


def remove_from_all_values(possible_allergens: dict[Allergen, Set[Ingredient]], ingredient: Ingredient):
    for ingredients in possible_allergens.values():
        ingredients.discard(ingredient)


if __name__ == '__main__':
    lines = read_text_list('day_21.txt')
    print(count_safe_ingredient_appearances(lines))
    print(get_canonical_dangerous_list(lines))
