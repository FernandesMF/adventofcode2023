from string import digits

from challenges.day3_1 import load_schematics

DATA_PATH = "challenges/day3-input.txt"


def collect_number(schema_line: str, line_pos: int) -> tuple[int, int, int]:
    """
    Finds the whole number given some part of it

    Return: (number itself, its beginning index, its ending index)
    """
    line_len = len(schema_line)

    index = line_pos
    num_start = index
    while index >= 0 and schema_line[index] in digits:
        num_start = index
        index -= 1

    index = line_pos
    num_end = index
    while index <= line_len - 1 and schema_line[index] in digits:
        num_end = index
        index += 1

    return (int(schema_line[num_start : num_end + 1]), num_start, num_end)


def is_gear(schema: list[str], line_num: int, line_pos: int) -> tuple[bool, int | None]:
    "Checks if an '*' is a gear, and if so returns its power as well"

    assert (
        schema[line_num][line_pos] == "*"
    ), "'is_gear' is being called for a non-gear character"

    line_len = len(schema[0])
    schema_len = len(schema)
    num_list = []

    if line_num > 0:
        i = line_pos - 1 if line_pos > 0 else 0
        max_i = line_pos + 1 if line_pos < line_len - 1 else line_pos
        while i <= max_i:
            if schema[line_num - 1][i] in digits:
                num, num_start, num_stop = collect_number(schema[line_num - 1], i)
                num_list.append(num)
                i = num_stop + 1
            else:
                i += 1

    if line_pos > 0:
        if schema[line_num][line_pos - 1] in digits:
            num, num_start, num_stop = collect_number(schema[line_num], line_pos - 1)
            num_list.append(num)

    if line_pos < line_len - 1:
        if schema[line_num][line_pos + 1] in digits:
            num, num_start, num_stop = collect_number(schema[line_num], line_pos + 1)
            num_list.append(num)

    if line_num < schema_len - 1:
        i = line_pos - 1 if line_pos > 0 else 0
        max_i = line_pos + 1 if line_pos < line_len - 1 else line_pos
        while i <= max_i:
            if schema[line_num + 1][i] in digits:
                num, num_start, num_stop = collect_number(schema[line_num + 1], i)
                num_list.append(num)
                i = num_stop + 1
            else:
                i += 1

    if len(num_list) == 2:
        return (True, num_list[0] * num_list[1])

    return (False, None)


def find_gear_ratios(schema: list[str]) -> list[int]:
    line_len = len(schema[0])
    gear_ratios = []

    for ln in range(len(schema)):
        index = 0
        while index < line_len:
            if schema[ln][index] == "*":
                is_gear_, gear_ratio = is_gear(schema, ln, index)
                if is_gear_:
                    gear_ratios.append(gear_ratio)
            index += 1

    return gear_ratios


def main():
    schematics = load_schematics()
    gear_ratios = find_gear_ratios(schematics)
    print(sum(gear_ratios))


if __name__ == "__main__":
    main()
