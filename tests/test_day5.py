from unittest import TestCase

from challenges.day5_1 import SegmentedDict


class TestSegmentedDict(TestCase):
    def setUp(self):
        self.seg_dict = SegmentedDict("test segmented dict")
        self.seg_dict.add_ranges(1, 11, 5)
        self.seg_dict.add_ranges(21, 31, 5)

    def test_get_item(self):
        def expected_output(x):
            if 1 <= x <= 5 or 21 <= x <= 25:
                return x + 10
            return x

        [self.assertEqual(self.seg_dict[x], expected_output(x)) for x in range(-10, 50)]
