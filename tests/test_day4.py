from unittest import TestCase
from unittest.mock import patch

from challenges.day4_2 import find_matches, process_card_chain


class TestDay4P2(TestCase):
    def setUp(self):
        self.sample_card_data = [
            ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
            ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
            ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
            ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
            ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
            ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
        ]

    def test_find_matches(self):
        expected_outputs = [4, 2, 2, 1, 0, 0]
        outputs = [find_matches(x) for x in self.sample_card_data]
        self.assertEqual(outputs, expected_outputs)

    def test_process_card_chain(self):
        input_ = [find_matches(x) for x in self.sample_card_data]
        expected_output = [1, 2, 4, 8, 14, 1]
        output = process_card_chain(input_)
        self.assertEqual(output, expected_output)
