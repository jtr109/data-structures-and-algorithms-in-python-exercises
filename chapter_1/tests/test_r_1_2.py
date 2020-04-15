import unittest
from chapter_1.r_1_2 import is_even


class MyTestCase(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
