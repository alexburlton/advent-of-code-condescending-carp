import unittest

from src.day_22.day_22 import *


class TestDay22(unittest.TestCase):
    def test_parse_decks(self):
        deck_one, deck_two = parse_decks('day_22_example.txt')
        self.assertEqual(deck_one, [9, 2, 6, 3, 1])
        self.assertEqual(deck_two, [5, 8, 4, 7, 10])

    def test_play_round(self):
        deck_one, deck_two = parse_decks('day_22_example.txt')
        play_round(deck_one, deck_two)

        self.assertEqual(deck_one, [2, 6, 3, 1, 9, 5])
        self.assertEqual(deck_two, [8, 4, 7, 10])

    def test_play_until_game_ends(self):
        resulting_score: int = play_until_game_ends('day_22_example.txt')
        self.assertEqual(resulting_score, 306)

    def test_get_state_string(self):
        deck_one = [5, 2, 9]
        deck_two = [20, 7, 18]
        state_str = get_state_string(deck_one, deck_two)
        self.assertEqual(state_str, '5,2,9|20,7,18')

    def test_doesnt_loop(self):
        deck_one, deck_two = parse_decks('day_22_loop_example.txt')
        winner, score = play_recursive(deck_one, deck_two)
        self.assertEqual(winner, 1)
        self.assertEqual(score, 19 + (2*43))

    def test_recursive_game(self):
        deck_one, deck_two = parse_decks('day_22_example.txt')
        winner, score = play_recursive(deck_one, deck_two)
        self.assertEqual(deck_one, [])
        self.assertEqual(deck_two, [7, 5, 6, 2, 4, 1, 10, 8, 9, 3])
        self.assertEqual(winner, 2)
        self.assertEqual(score, 291)


if __name__ == '__main__':
    unittest.main()
