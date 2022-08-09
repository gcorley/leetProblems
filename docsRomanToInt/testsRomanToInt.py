import unittest
from docsRomanToInt import romanToInt


class RomanToIntTesting(unittest.TestCase):
    def test_one(self):
        self.assertEqual(romanToInt.roman_to_int("III"), 3)

    def test_two(self):
        self.assertEqual(romanToInt.roman_to_int("LVIII"), 58)

    def test_three(self):
        self.assertEqual(romanToInt.roman_to_int("MCMXCIV"), 1994)

    def test_four(self):
        self.assertEqual(romanToInt.roman_to_int("IVPM"), 0)

    def test_five(self):
        self.assertEqual(romanToInt.roman_to_int("MIC"), 0)
