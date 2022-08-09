import unittest
from docsPalindrome import palindrome


class PalindromeTesting(unittest.TestCase):
    def test_one(self):
        x = 121
        answer = True
        self.assertEqual(palindrome.is_palindrome(x), answer)

    def test_two(self):
        x = -121
        answer = False
        self.assertEqual(palindrome.is_palindrome(x), answer)

    def test_three(self):
        x = 10
        answer = False
        self.assertEqual(palindrome.is_palindrome(x), answer)

    def test_four(self):
        x = 0
        answer = True
        self.assertEqual(palindrome.is_palindrome(x), answer)

    def test_five(self):
        x = 123454321
        answer = True
        self.assertEqual(palindrome.is_palindrome(x), answer)
