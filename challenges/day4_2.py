from challenges.day4_1 import organize_card_data
from challenges.utils import load_data


DATA_PATH = "challenges/day4-input.txt"


def find_matches(card_info: tuple[list[int], list[int]]) -> int:
    winning_nums = card_info[0]
    elf_nums = card_info[1]
    return sum([x in winning_nums for x in elf_nums])


def process_card_chain(match_counts: list[int]) -> list[int]:
    n = len(match_counts)
    card_count = [1 for i in range(n)]

    for i in range(n):
        for j in range(match_counts[i]):
            card_count[i + j + 1] += card_count[i]

    return card_count


def main():
    raw_data = load_data(DATA_PATH)
    card_data = organize_card_data(raw_data)
    match_counts = [find_matches(x) for x in card_data]
    card_count = process_card_chain(match_counts)
    print(sum(card_count))


if __name__ == "__main__":
    main()
