from challenges.utils import load_data


DATA_PATH = "challenges/day5-input.txt"


class SegmentedDict(dict):
    "Dictionary made of intervals"

    def __init__(self, name: str | None) -> None:
        self._name = name if name else ""
        self._ranges: list[tuple(range, range)] = []

    def add_ranges(
        self,
        source_range_start: int | float,
        dest_range_start: int | float,
        range_len: int | float,
    ) -> None:
        self._ranges.append(
            (
                range(source_range_start, source_range_start + range_len),
                range(dest_range_start, dest_range_start + range_len),
            )
        )

    def __getitem__(self, x: int | float) -> int | float:
        for r in self._ranges:
            if x in r[0]:
                return x - r[0].start + r[1].start
        return x

    def __repr__(self):
        return f"<{self._name} SegmentedDict with ranges {self._ranges}>"

    def __str__(self):
        return f"{{{self._ranges}}}"


def organize_raw_input(
    raw_data: list[str],
) -> tuple[
    list[int],
    dict[int:int],
    dict[int:int],
    dict[int:int],
    dict[int:int],
    dict[int:int],
    dict[int:int],
    dict[int:int],
]:
    """
    Reorganizes the raw input into seed list and the various maps
    Return: (
        seeds list,
        seed-to-soil map,
        soil-to-fertilizer map,
        fertilizer-to-water map,
        water-to-light map,
        light-to-temperature map,
        temperature-to-humidity map,
        humidity-to-location map
    )
    """
    sep_idxs = (
        [0] + [i for i, x in enumerate(raw_data) if x == ""] + [len(raw_data)]
    )  # empty lines separate sections
    data_chunks = [raw_data[sep_idxs[i] : sep_idxs[i + 1]] for i in range(len(sep_idxs[:-1]))]
    seeds_list = list(map(int, data_chunks[0][0].split()[1:]))
    seed_to_soil_map = build_mapping(data_chunks[1][2:], "seed_to_soil_map")
    soil_to_fertilizer_map = build_mapping(data_chunks[2][2:], "soil_to_fertilizer_map")
    fertilizer_to_water_map = build_mapping(data_chunks[3][2:], "fertilizer_to_water_map")
    water_to_light_map = build_mapping(data_chunks[4][2:], "water_to_light_map")
    light_to_temperature_map = build_mapping(data_chunks[5][2:], "light_to_temperature_map")
    temperature_to_humidity_map = build_mapping(data_chunks[6][2:], "temperature_to_humidity_map")
    humidity_to_location_map = build_mapping(data_chunks[7][2:], "humidity_to_location_map")

    return (
        seeds_list,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    )


def build_mapping(range_info_list: list[str], name: str | None = None) -> dict[int:int]:
    map_ = SegmentedDict(name)
    split_data = list(map(str.split, range_info_list))

    for info in split_data:
        dest_range_start = int(info[0])
        source_range_start = int(info[1])
        range_len = int(info[2])
        map_.add_ranges(source_range_start, dest_range_start, range_len)

    return map_


def find_soil(
    seed_num: int,
    seed_to_soil_map: SegmentedDict,
    soil_to_fertilizer_map: SegmentedDict,
    fertilizer_to_water_map: SegmentedDict,
    water_to_light_map: SegmentedDict,
    light_to_temperature_map: SegmentedDict,
    temperature_to_humidity_map: SegmentedDict,
    humidity_to_location_map: SegmentedDict,
) -> int:
    x = seed_to_soil_map[seed_num]
    x = soil_to_fertilizer_map[x]
    x = fertilizer_to_water_map[x]
    x = water_to_light_map[x]
    x = light_to_temperature_map[x]
    x = temperature_to_humidity_map[x]
    x = humidity_to_location_map[x]
    return x


def main() -> None:
    raw_data = load_data(DATA_PATH)
    (
        seeds_list,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    ) = organize_raw_input(raw_data)
    locations = [
        find_soil(
            x,
            seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map,
        )
        for x in seeds_list
    ]
    print(min(locations))


if __name__ == "__main__":
    main()
