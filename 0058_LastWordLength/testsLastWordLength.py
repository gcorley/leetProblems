import unittest
import lastWordLength


class LastWordLengthTesting(unittest.TestCase):
    def test_one(self):
        s = 'Hello World'
        actual_answer = lastWordLength.last_word_length(s)
        expected_answer = 5
        self.assertEqual(actual_answer, expected_answer)

    def test_two(self):
        s = '   fly me   to   the moon  '
        actual_answer = lastWordLength.last_word_length(s)
        expected_answer = 4
        self.assertEqual(actual_answer, expected_answer)

    def test_three(self):
        s = 'luffy is still joyboy'
        actual_answer = lastWordLength.last_word_length(s)
        expected_answer = 6
        self.assertEqual(actual_answer, expected_answer)
