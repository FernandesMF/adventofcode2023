from itertools import starmap, batched
from unittest import TestCase

from challenges.day3_1 import (
    has_symbol,
    gather_number,
    check_for_adjacent_symbol,
    schematics_processor,
)
from challenges.day3_2 import collect_number, is_gear, find_gear_ratios


class TestDay3P1(TestCase):
    def setUp(self):
        self.sample_schematics = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

    def test_has_symbol(self):
        expected_outputs = [
            False,
            True,
            False,
            True,
            True,
            True,
            False,
            False,
            True,
            False,
        ]
        outputs = [has_symbol(x) for x in self.sample_schematics]
        self.assertEqual(outputs, expected_outputs)

    def test_gather_number(self):
        inputs = [
            (self.sample_schematics[0], 0),
            (self.sample_schematics[0], 5),
            (self.sample_schematics[2], 2),
            (self.sample_schematics[2], 6),
            (self.sample_schematics[4], 0),
            (self.sample_schematics[5], 7),
            (self.sample_schematics[6], 2),
            (self.sample_schematics[7], 6),
            (self.sample_schematics[9], 1),
            (self.sample_schematics[9], 5),
        ]
        expected_outputs = [
            (467, 0, 3),
            (114, 5, 3),
            (35, 2, 2),
            (633, 6, 3),
            (617, 0, 3),
            (58, 7, 2),
            (592, 2, 3),
            (755, 6, 3),
            (664, 1, 3),
            (598, 5, 3),
        ]
        outputs = list(starmap(gather_number, inputs))
        self.assertEqual(outputs, expected_outputs)

    def test_check_for_adjacent_symbol(self):
        inputs = [
            (self.sample_schematics, 0, 0, 3),
            (self.sample_schematics, 0, 5, 3),
            (self.sample_schematics, 2, 2, 2),
            (self.sample_schematics, 2, 6, 3),
            (self.sample_schematics, 4, 0, 3),
            (self.sample_schematics, 5, 7, 2),
            (self.sample_schematics, 6, 2, 3),
            (self.sample_schematics, 7, 6, 3),
            (self.sample_schematics, 9, 1, 3),
            (self.sample_schematics, 9, 5, 3),
        ]
        expected_outputs = [
            True,
            False,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
        ]
        outputs = list(starmap(check_for_adjacent_symbol, inputs))
        self.assertEqual(outputs, expected_outputs)

    def test_schematics_processor(self):
        expected_output = [467, 35, 633, 617, 592, 755, 664, 598]
        output = schematics_processor(self.sample_schematics)
        self.assertEqual(output, expected_output)


class TestDay3P2(TestCase):
    def setUp(self):
        self.sample_schematics = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        self.small_schema = load_small_schema()

    def test_collect_number(self):
        inputs = [
            (self.sample_schematics[0], 0),
            (self.sample_schematics[0], 1),
            (self.sample_schematics[0], 2),
            (self.sample_schematics[0], 5),
            (self.sample_schematics[0], 6),
            (self.sample_schematics[0], 7),
            (self.sample_schematics[0][0:8], 5),
            (self.sample_schematics[0][0:8], 6),
            (self.sample_schematics[0][0:8], 7),
        ]
        expected_outputs = [
            (467, 0, 2),
            (467, 0, 2),
            (467, 0, 2),
            (114, 5, 7),
            (114, 5, 7),
            (114, 5, 7),
            (114, 5, 7),
            (114, 5, 7),
            (114, 5, 7),
        ]
        outputs = list(starmap(collect_number, inputs))
        self.assertEqual(outputs, expected_outputs)

    def test_is_gear(self):
        inputs = [
            (self.sample_schematics, 1, 3),
            (self.sample_schematics, 4, 3),
            (self.sample_schematics, 8, 5),
        ]
        expected_outputs = [(True, 467 * 35), (False, None), (True, 755 * 598)]
        outputs = list(starmap(is_gear, inputs))
        self.assertEqual(outputs, expected_outputs)

    def test_is_gear_small_schema(self):
        inputs = [(self.small_schema[3:6], 1, 1)]
        expected_outputs = [(True, 3)]
        outputs = list(starmap(is_gear, inputs))
        self.assertEqual(outputs, expected_outputs)

    def test_find_gear_ratios(self):
        expected_output = [467 * 35, 755 * 598]
        output = find_gear_ratios(self.sample_schematics)
        self.assertEqual(output, expected_output)

    def test_find_gear_ratios_small_schema(self):
        expected_output = [
            2,
            3,
            4,
            5,
            6,
            7,
            2,
            3,
            4,
            5,
            6,
            2,
            3,
            4,
            5,
            6,
            2,
            3,
            4,
            5,
            2,
            3,
            4,
            2,
        ]
        output = find_gear_ratios(self.small_schema)
        self.assertEqual(output, expected_output)


def load_small_schema() -> list[list[str]]:
    small_schemas_path = "tests/small_schemas.txt"

    with open(small_schemas_path, "r") as f:
        text_lines = f.readlines()

    text_lines = list(map(str.strip, text_lines))

    return text_lines
