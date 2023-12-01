from unittest import TestCase

from challenges.day1_2 import find_first_and_last_digit, substitute_spelled_out_digits


class TestD1C2(TestCase):

    def test_substitute_spelled_out_digits(self):
        inputs = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        expected_outputs = [
            '2two19nine',
            '8eigh2two3three',
            'abc1one23threexyz',
            'x2tw1one34four',
            '49nine8eight7seven2',
            'z1on8eight234',
            '7pqrst6sixteen'
        ]

        outputs = [substitute_spelled_out_digits(x) for x in inputs]

        self.assertEqual(outputs, expected_outputs)

    def test_find_first_and_last_digit(self):
        inputs = [
            '219', '8wo3', 'abc123xyz', 'x2ne34', '49872', 'z1ight234', '7pqrst6teen'
        ]
        expected_outputs = [
            29, 83, 13, 24, 42, 14, 76
        ]

        outputs = [find_first_and_last_digit(x) for x in inputs]

        self.assertEqual(outputs, expected_outputs)
