import unittest

from chapter_1.c_1_15 import separate


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        data = [1, 2, 3, 4]
        self.assertTrue(separate(data))
        data = [1, 2, 3, 1]
        self.assertFalse(separate(data))
