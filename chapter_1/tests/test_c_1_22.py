import unittest

from chapter_1.c_1_22 import dot_product


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        self.assertListEqual(dot_product(a, b), [4, 10, 18])
