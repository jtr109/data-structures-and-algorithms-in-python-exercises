import unittest

from chapter_1.r_1_4 import sum_of_square


class MyTestCase(unittest.TestCase):

    def test_sum_of_square(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
