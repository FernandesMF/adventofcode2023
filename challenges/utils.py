def load_data(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.readlines()
    data = list(map(str.strip, data))
    return data
