from challenges.day2_1 import load_data, parse_data


DATA_PATH = "challenges/day2-input.txt"


def find_minimum_cube_amounts(
    data: dict[int : list[tuple[int, int, int]]]
) -> dict[tuple[int, int, int]]:
    max_cubes = {}
    for k in data.keys():
        max_tuple = tuple(map(max, zip(*data[k])))
        max_cubes.update({k: max_tuple})

    return max_cubes


def find_games_power(min_cubes: dict[tuple[int, int, int]]) -> dict[int:int]:
    powers = {}
    for k, tuple_ in min_cubes.items():
        powers.update({k: tuple_[0] * tuple_[1] * tuple_[2]})

    return powers


def main() -> None:
    raw_data = load_data(DATA_PATH)
    parsed_data = parse_data(raw_data)
    min_cubes = find_minimum_cube_amounts(parsed_data)
    game_powers = find_games_power(min_cubes)

    print(sum(v for v in game_powers.values()))


if __name__ == "__main__":
    main()
