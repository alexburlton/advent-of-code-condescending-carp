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

    # print('=== Game', game_number, '===')
    # print('')

    round_number = 1

    while len(deck_one) > 0 and len(deck_two) > 0:
        # print('-- Round', round_number, ' (Game', game_number, ') --')
        # print('')
        current_state = get_state_string(deck_one, deck_two)
        if current_state in states_seen_before:
            return 1, calculate_final_score(deck_one)

        states_seen_before.add(current_state)

        # print('Player 1s deck:', deck_one)
        # print('Player 2s deck:', deck_two)

        card_one = deck_one.pop(0)
        card_two = deck_two.pop(0)

        # print('Player 1 plays:', card_one)
        # print('Player 2 players:', card_two)

        if len(deck_one) >= card_one and len(deck_two) >= card_two:
            # print('Playing a sub-game to determine the winner...')
            sub_deck_one = deck_one.copy()[0:card_one]
            sub_deck_two = deck_two.copy()[0:card_two]
            winner, _ = play_recursive(sub_deck_one, sub_deck_two)
            # print('...anyway, back to Game', game_number)
            if winner == 1:
                # print('Player 1 wins round!')
                deck_one.append(card_one)
                deck_one.append(card_two)
            else:
                # print('Player 2 wins round!')
                deck_two.append(card_two)
                deck_two.append(card_one)
        elif card_one > card_two:
            # print('Player 1 wins round!')
            deck_one.append(card_one)
            deck_one.append(card_two)
        else:
            # print('Player 2 wins round!')
            deck_two.append(card_two)
            deck_two.append(card_one)

        round_number = round_number + 1

    winning_player, winning_deck = (1, deck_one) if len(deck_one) > 0 else (2, deck_two)
    # print('The winner of game', game_number, 'is player', winning_player)
    return winning_player, calculate_final_score(winning_deck)


if __name__ == '__main__':
    print(play_until_game_ends('day_22.txt'))
    deck_1, deck_2 = parse_decks('day_22.txt')
    print(play_recursive(deck_1, deck_2))
