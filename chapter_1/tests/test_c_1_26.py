import unittest

from chapter_1.c_1_26 import calculative


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        self.assertTrue(calculative(1, 2, 3))
        self.assertFalse(calculative(1, 3, 5))
        self.assertTrue(calculative(2, 6, 3))
