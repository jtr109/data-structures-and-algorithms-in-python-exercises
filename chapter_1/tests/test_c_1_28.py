import unittest

from chapter_1.c_1_28 import norm


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        self.assertEqual(norm([4, 3], 2), 5)
