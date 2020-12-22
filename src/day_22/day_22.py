from typing import List, Set, Tuple

from utils import read_text_groups

Card = int


def parse_decks(file_name: str) -> tuple[List[Card], List[Card]]:
    decks = read_text_groups(file_name)
    deck_one = [Card(card) for card in decks[0].splitlines() if not card.startswith('Player')]
    deck_two = [Card(card) for card in decks[1].splitlines() if not card.startswith('Player')]
    return deck_one, deck_two


def calculate_final_score(deck: List[Card]) -> int:
    card_values = [(len(deck) - i) * deck[i] for i in range(0, len(deck))]
    return sum(card_values)


def play_until_game_ends(file_name: str) -> int:
    deck_one, deck_two = parse_decks(file_name)
    while len(deck_one) > 0 and len(deck_two) > 0:
        play_round(deck_one, deck_two)

    winning_deck = deck_one if len(deck_one) > 0 else deck_two
    return calculate_final_score(winning_deck)


def play_round(deck_one: List[Card], deck_two: List[Card]):
    card_one = deck_one.pop(0)
    card_two = deck_two.pop(0)
    resolve_simple_round(card_one, card_two, deck_one, deck_two)


def resolve_simple_round(card_one: Card, card_two: Card, deck_one: List[Card], deck_two: List[Card]):
    if card_one > card_two:
        deck_one.append(card_one)
        deck_one.append(card_two)
    else:
        deck_two.append(card_two)
        deck_two.append(card_one)


def get_state_string(deck_one: List[Card], deck_two: List[Card]) -> str:
    return ','.join(map(str, deck_one)) + '|' + ','.join(map(str, deck_two))


def play_recursive(deck_one: List[Card], deck_two: List[Card]) -> Tuple[int, int]:
    states_seen_before: Set[str] = set()

    while len(deck_one) > 0 and len(deck_two) > 0:
        current_state = get_state_string(deck_one, deck_two)
        if current_state in states_seen_before:
            return 1, calculate_final_score(deck_one)

        states_seen_before.add(current_state)

        card_one = deck_one.pop(0)
        card_two = deck_two.pop(0)

        if len(deck_one) >= card_one and len(deck_two) >= card_two:
            play_sub_game(card_one, card_two, deck_one, deck_two)
        else:
            resolve_simple_round(card_one, card_two, deck_one, deck_two)

    winning_player, winning_deck = (1, deck_one) if len(deck_one) > 0 else (2, deck_two)
    return winning_player, calculate_final_score(winning_deck)


def play_sub_game(card_one: Card, card_two: Card, deck_one: List[Card], deck_two: List[Card]):
    sub_deck_one = deck_one.copy()[0:card_one]
    sub_deck_two = deck_two.copy()[0:card_two]
    winner, _ = play_recursive(sub_deck_one, sub_deck_two)
    if winner == 1:
        deck_one.append(card_one)
        deck_one.append(card_two)
    else:
        deck_two.append(card_two)
        deck_two.append(card_one)


if __name__ == '__main__':
    print(play_until_game_ends('day_22.txt'))
    deck_1, deck_2 = parse_decks('day_22.txt')
    print(play_recursive(deck_1, deck_2))
