import unittest
import removeElement


class RemoveElementTesting(unittest.TestCase):
    def test_one(self):
        nums = [3, 2, 2, 3]
        val = 3
        actual_answer = removeElement.remove_element(nums, val)
        expected_list = [2, 2]
        expected_length = 2
        self.assertEqual(actual_answer, expected_list)

    def test_two(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        actual_answer = removeElement.remove_element(nums, val)
        expected_list = [0, 1, 4, 0, 3]
        expected_length = 5
        self.assertEqual(actual_answer, expected_list)
