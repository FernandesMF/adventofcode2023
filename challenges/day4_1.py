from itertools import starmap

from challenges.utils import load_data


DATA_PATH = "challenges/day4-input.txt"


def organize_card_data(raw_data: list[str]) -> list[tuple[list[int], list[int]]]:
    card_data = []
    for line in raw_data:
        numbers = line.split(":")[1]
        winning_nums, elf_nums = numbers.split("|")
        winning_nums = winning_nums.split()
        elf_nums = elf_nums.split()
        card_data.append((winning_nums, elf_nums))
    return card_data


def calculate_card_points(winning_nums: list[int], elf_nums: list[int]) -> int:
    num_matches = sum([x in winning_nums for x in elf_nums])
    return 2 ** (num_matches - 1) if num_matches > 0 else 0


def main():
    raw_data = load_data(DATA_PATH)
    card_data = organize_card_data(raw_data)
    points = list(starmap(calculate_card_points, card_data))
    print(sum(points))


if __name__ == "__main__":
    main()
