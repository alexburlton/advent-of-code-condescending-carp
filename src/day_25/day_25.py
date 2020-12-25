from utils import read_integer_list


def perform_loop(value: int, subject_number: int = 7) -> int:
    squared = value * subject_number
    return squared % 20201227


def find_loop_number(final_value: int) -> int:
    value: int = 1
    loops: int = 0
    while value != final_value:
        value = perform_loop(value)
        loops += 1

    return loops


def part_a(file_name: str) -> int:
    pub_1, pub_2 = read_integer_list(file_name)
    loop_size_2 = find_loop_number(pub_2)

    encryption_key_value = 1
    for i in range(0, loop_size_2):
        encryption_key_value = perform_loop(encryption_key_value, pub_1)

    return encryption_key_value


if __name__ == '__main__':
    print(part_a('day_25.txt'))
