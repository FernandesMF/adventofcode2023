from string import punctuation, digits

SYMBOLS = punctuation.replace(".", "")
DATA_PATH = "challenges/day3-input.txt"


def load_schematics() -> list[str]:
    with open(DATA_PATH, "r") as f:
        data = f.readlines()
    return data


def has_symbol(s: str) -> bool:
    return any(ss in SYMBOLS for ss in s)


def gather_number(
    schema_line: str,
    line_pos: int,
) -> tuple[int, int, int]:
    """
    Finds the whole number given its istarting position.

    Return: (number itself, starting position, lenght)
    """
    number_len = 0
    while schema_line[line_pos + number_len] in digits:
        number_len += 1
    return (int(schema_line[line_pos : line_pos + number_len]), line_pos, number_len)


def check_for_adjacent_symbol(
    schema: list[str], line_num: int, number_start_pos: int, number_len: len
) -> bool:
    surrounding_chars = ""
    line_len = len(schema[0])
    schema_len = len(schema)

    if line_num > 0:
        i = number_start_pos - 1 if number_start_pos > 0 else 0
        j = (
            number_start_pos + number_len + 1
            if (number_start_pos + number_len + 1) < line_len
            else line_len
        )
        surrounding_chars += schema[line_num - 1][i:j]
    if number_start_pos > 0:
        surrounding_chars += schema[line_num][number_start_pos - 1]
    if number_start_pos + number_len < line_len - 1:
        surrounding_chars += schema[line_num][number_start_pos + number_len]
    if line_num < schema_len - 1:
        i = number_start_pos - 1 if number_start_pos > 0 else 0
        j = (
            number_start_pos + number_len + 1
            if (number_start_pos + number_len + 1) < line_len
            else line_len
        )
        surrounding_chars += schema[line_num + 1][i:j]

    return has_symbol(surrounding_chars)


def schematics_processor(schema: list[str]) -> list[int]:
    line_len = len(schema[0])
    part_numbers = []

    for ln in range(len(schema)):
        index = 0
        while index < line_len:
            if schema[ln][index] in digits:
                num, num_start_pos, num_len = gather_number(schema[ln], index)
                if check_for_adjacent_symbol(schema, ln, num_start_pos, num_len):
                    part_numbers.append(num)
                index += num_len
            else:
                index += 1

    return part_numbers


def main():
    schematics = load_schematics()
    part_numbers = schematics_processor(schematics)
    print(sum(part_numbers))
    breakpoint()


if __name__ == "__main__":
    main()
