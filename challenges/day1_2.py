import string
from re import search

DATA_PATH = "challenges/day1-input.txt"
SPELLED_OUT_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def load_data(path: str) -> list[str]:
    data = []
    with open(path, "r") as f:
        data = f.readlines()
    return data


def substitute_spelled_out_digits(ss: str) -> str:
    match_str = f"({'|'.join(SPELLED_OUT_DIGITS.keys())})"
    index = 0
    match = search(match_str, ss[index:])
    while match:
        ss = (
            ss[0 : index + match.span()[0]]
            + str(SPELLED_OUT_DIGITS[match.group()])
            + ss[index + match.span()[0] :]
        )
        index += match.span()[0] + 2
        match = search(match_str, ss[index:])
    return ss


def find_first_and_last_digit(s: str) -> int:
    numeric_chars = [
        x for x in s if (x in string.digits or x in SPELLED_OUT_DIGITS.values())
    ]
    return int(numeric_chars[0] + numeric_chars[-1])


if __name__ == "__main__":
    data = load_data(DATA_PATH)
    data2 = [substitute_spelled_out_digits(x) for x in data]
    numeric_values = [find_first_and_last_digit(x) for x in data2]
    print(sum(numeric_values))
