import unittest
import longestDistinctSubstring


class TestingLongestDistinctSubstring(unittest.TestCase):
    def test_one(self):
        input_str = 'abcabcbb'
        answer = 3
        self.assertEqual(longestDistinctSubstring.longest_substring(input_str), answer)

    def test_two(self):
        input_str = 'bbbbb'
        answer = 1
        self.assertEqual(longestDistinctSubstring.longest_substring(input_str), answer)

    def test_three(self):
        input_str = 'pwwkew'
        answer = 3
        self.assertEqual(longestDistinctSubstring.longest_substring(input_str), answer)

    def test_four(self):
        input_str = '123abcabc564j'
        answer = 7
        self.assertEqual(longestDistinctSubstring.longest_substring(input_str), answer)
