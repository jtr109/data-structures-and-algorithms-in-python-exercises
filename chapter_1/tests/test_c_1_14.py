import unittest

from chapter_1.c_1_14 import separate_odd_product_exists


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        data = [1, 2, 3, 4]
        self.assertTrue(separate_odd_product_exists(data))
        data = [1, 2, 4]
        self.assertFalse(separate_odd_product_exists(data))
        data = [1, 2, 4, 1]
        self.assertFalse(separate_odd_product_exists(data))
