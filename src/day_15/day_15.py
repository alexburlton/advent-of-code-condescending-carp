

def play_until_nth_turn(starting_number_str: str, n: int) -> int:
    numbers_spoken: dict[int, int] = {}
    starting_numbers = [int(number) for number in starting_number_str.split(',')]
    for i in range(0, len(starting_numbers) - 1):
        numbers_spoken[starting_numbers[i]] = i+1

    last_spoken = starting_numbers[len(starting_numbers) - 1]
    current_turn = len(starting_numbers) + 1
    number_to_speak = 0
    while current_turn < n + 1:
        last_spoken_round = numbers_spoken.get(last_spoken, None)
        if last_spoken_round is None:
            number_to_speak = 0
        else:
            number_to_speak = current_turn - last_spoken_round - 1

        numbers_spoken[last_spoken] = current_turn - 1
        last_spoken = number_to_speak
        current_turn += 1

    return last_spoken


if __name__ == '__main__':
    print(play_until_nth_turn('6,13,1,15,2,0', 2020))
    print(play_until_nth_turn('6,13,1,15,2,0', 30000000))
