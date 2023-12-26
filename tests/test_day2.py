from unittest import TestCase

from challenges.day2_1 import parse_data, is_possible_game, find_possible_games
from challenges.day2_2 import find_minimum_cube_amounts, find_games_power


class TestDay2P1(TestCase):
    def setUp(self):
        self.parsed_data = {
            1: [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
            2: [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
            3: [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
            4: [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
            5: [(6, 3, 1), (1, 2, 2)],
        }

    def test_parse_data(self):
        fake_data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        expected_output = self.parsed_data

        output = parse_data(fake_data)

        self.assertEqual(output, expected_output)

    def test_is_possible_game(self):
        expected_outputs = [True, True, False, False, True]

        outputs = [is_possible_game(x) for x in self.parsed_data.values()]

        self.assertEqual(outputs, expected_outputs)

    def test_find_possible_games(self):
        expected_output = [1, 2, 5]

        output = find_possible_games(self.parsed_data)

        self.assertEqual(output, expected_output)


class TestDay2P2(TestCase):
    def setUp(self):
        self.parsed_data = {
            1: [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
            2: [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
            3: [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
            4: [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
            5: [(6, 3, 1), (1, 2, 2)],
        }
        self.min_cubes = {
            1: (4, 2, 6),
            2: (1, 3, 4),
            3: (20, 13, 6),
            4: (14, 3, 15),
            5: (6, 3, 2),
        }

    def test_find_minimum_cube_amounts(self):
        expected_output = self.min_cubes

        output = find_minimum_cube_amounts(self.parsed_data)

        self.assertEqual(output, expected_output)

    def test_find_games_power(self):
        expected_output = {
            1: 48,
            2: 12,
            3: 1560,
            4: 630,
            5: 36,
        }

        output = find_games_power(self.min_cubes)

        self.assertEqual(output, expected_output)
