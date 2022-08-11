import unittest
import sortedArrayDuplicates


class SortedArrayDuplicatesTesting(unittest.TestCase):
    def test_one(self):
        x = [1, 1, 2]
        length_answer = 2
        # final_answer = [1, 2]
        self.assertEqual(sortedArrayDuplicates.remove_duplicates(x), length_answer)
        # self.assertEqual(sortedArrayDuplicates.remove_duplicates.final, final_answer)

    def test_two(self):
        x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        answer = 5
        # final_answer = [0, 1, 2, 3, 4]
        self.assertEqual(sortedArrayDuplicates.remove_duplicates(x), answer)
