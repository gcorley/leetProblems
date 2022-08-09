import unittest
from docsValidParentheses import validParentheses


class ValidParenthesesTesting(unittest.TestCase):
    def test_one(self):
        s = '()'
        answer = True
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_two(self):
        s = '()[]{}'
        answer = True
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_three(self):
        s = '(]'
        answer = False
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_four(self):
        s = 'abc'
        answer = False
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_five(self):
        s = '{abc}'
        answer = False
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_six(self):
        s = '['
        answer = False
        self.assertEqual(validParentheses.is_valid(s), answer)

    def test_seven(self):
        s = ']'
        answer = False
        self.assertEqual(validParentheses.is_valid(s), answer)
