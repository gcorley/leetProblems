import unittest
import plusOne


class PlusOneTesting(unittest.TestCase):
    def test_one(self):
        digits = [1, 2, 3]
        actual_answer = plusOne.plus_one(digits)
        expected_answer = [1, 2, 4]
        self.assertEqual(actual_answer, expected_answer)

    def test_two(self):
        digits = [4, 3, 2, 1]
        actual_answer = plusOne.plus_one(digits)
        expected_answer = [4, 3, 2, 2]
        self.assertEqual(actual_answer, expected_answer)

    def test_three(self):
        digits = [9]
        actual_answer = plusOne.plus_one(digits)
        expected_answer = [1, 0]
        self.assertEqual(actual_answer, expected_answer)
