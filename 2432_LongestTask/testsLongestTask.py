import unittest
import longestTask


class LongestTaskTesting(unittest.TestCase):
    def test_one(self):
        n = 10
        logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
        actual_answer = longestTask.longest_task(n, logs)
        expected_answer = 1
        self.assertEqual(actual_answer, expected_answer)

    def test_two(self):
        n = 26
        logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
        actual_answer = longestTask.longest_task(n, logs)
        expected_answer = 3
        self.assertEqual(actual_answer, expected_answer)

    def test_three(self):
        n = 2
        logs = [[0, 10], [1, 20]]
        actual_answer = longestTask.longest_task(n, logs)
        expected_answer = 0
        self.assertEqual(actual_answer, expected_answer)

    def test_four(self):
        n = 70
        logs = [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]
        actual_answer = longestTask.longest_task(n, logs)
        expected_answer = 12
        self.assertEqual(actual_answer, expected_answer)
