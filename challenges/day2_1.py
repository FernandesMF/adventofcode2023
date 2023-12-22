import re


DATA_PATH = "challenges/day2-input.txt"
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def load_data(path: str) -> list[str]:
    data = []
    with open(path, "r") as f:
        data = f.readlines()
    return data


def parse_data(data: list[str]) -> dict[int : list[tuple[int, int, int]]]:
    "Parses the data in an organized format: {id: [(R, G, B), ...]}"
    parsed_data = {}
    for line in data:
        game_id = int(re.search(r"Game (\d+):", line).groups()[0])
        round_info = re.split(";", line[8:])
        parsed_round_info = []
        for r in round_info:
            reds = (
                int(re.search(r"(\d+) red", r).groups()[0])
                if re.search(r"(\d+) red", r)
                else 0
            )
            greens = (
                int(re.search(r"(\d+) green", r).groups()[0])
                if re.search(r"(\d+) green", r)
                else 0
            )
            blues = (
                int(re.search(r"(\d+) blue", r).groups()[0])
                if re.search(r"(\d+) blue", r)
                else 0
            )
            parsed_round_info.append((reds, greens, blues))
        parsed_data.update({game_id: parsed_round_info})
    return parsed_data


def is_possible_game(game_info: list[tuple[int, int, int]]) -> bool:
    return all(
        [
            x[0] <= MAX_RED_CUBES and x[1] <= MAX_GREEN_CUBES and x[2] <= MAX_BLUE_CUBES
            for x in game_info
        ]
    )


def find_possible_games(data: dict[int : list[tuple[int, int, int]]]) -> list[int]:
    return [x for x in data.keys() if is_possible_game(data[x])]


def main() -> None:
    raw_data = load_data(DATA_PATH)
    parsed_data = parse_data(raw_data)
    possible_games = find_possible_games(parsed_data)
    print(sum(possible_games))


if __name__ == "__main__":
    main()
