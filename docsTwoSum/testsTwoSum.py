import unittest
from docsTwoSum import twoSum


class TwoSumTesting(unittest.TestCase):
    def test_one(self):
        nums = [2, 7, 11, 15]
        target = 9
        final = [0, 1]
        self.assertEqual(twoSum.two_sum(nums, target), final)

    def test_two(self):
        nums = [3, 2, 4]
        target = 6
        final = [1, 2]
        self.assertEqual(twoSum.two_sum(nums, target), final)

    def test_three(self):
        nums = [3, 3]
        target = 6
        final = [0, 1]
        self.assertEqual(twoSum.two_sum(nums, target), final)

    def test_four(self):
        nums = [3, 2, 3]
        target = 6
        final = [0, 2]
        self.assertEqual(twoSum.two_sum(nums, target), final)
