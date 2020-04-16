import unittest

from chapter_1.r_1_7 import sum_of_odd_square


class MyTestCase(unittest.TestCase):

    def test_sum_of_odd_square(self):
        self.assertEqual(sum_of_odd_square(1), 1)
        self.assertEqual(sum_of_odd_square(2), 1)
        self.assertEqual(sum_of_odd_square(3), 10)
        self.assertEqual(sum_of_odd_square(4), 10)
