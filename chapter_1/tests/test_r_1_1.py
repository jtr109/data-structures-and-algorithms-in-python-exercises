import unittest
from chapter_1.r_1_1 import is_multiple


class MyTestCase(unittest.TestCase):

    def test_is_multiple(self):
        self.assertTrue(is_multiple(4, 2))
        self.assertFalse(is_multiple(3, 2))
