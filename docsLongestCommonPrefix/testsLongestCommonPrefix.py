import unittest
from docsLongestCommonPrefix import longestCommonPrefix


class LongestCommonPrefixTesting(unittest.TestCase):
    def test_one(self):
        strs = ["flower", "flow", "flight"]
        verify = 'fl'
        self.assertEqual(longestCommonPrefix.longest_common_prefix(strs), verify)

    def test_two(self):
        strs = ["dog", "racecar", "car"]
        verify = ''
        self.assertEqual(longestCommonPrefix.longest_common_prefix(strs), verify)

    def test_three(self):
        strs = ["apple", "apple"]
        verify = 'apple'
        self.assertEqual(longestCommonPrefix.longest_common_prefix(strs), verify)

    def test_four(self):
        strs = ["Computer", "comp"]
        verify = 'comp'
        self.assertEqual(longestCommonPrefix.longest_common_prefix(strs), verify)
