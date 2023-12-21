import string

DATA_PATH = "challenges/day1-input.txt"


def load_data(path: str) -> list[str]:
    data = []
    with open(path, "r") as f:
        data = f.readlines()
    return data


def find_first_and_last_digit(s: str) -> int:
    numeric_chars = [x for x in s if x in string.digits]
    return int(numeric_chars[0] + numeric_chars[-1])


if __name__ == "__main__":
    data = load_data(DATA_PATH)
    numeric_values = [find_first_and_last_digit(x) for x in data]
    print(sum(numeric_values))
