import unittest

from chapter_1.c_1_20 import shuffle


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        data = ['a', 'b', 'c', 'd', 'e', 'd']
        original_data = data.copy()
        shuffle(data)
        self.assertNotEqual(data, original_data)
        self.assertListEqual(sorted(data), sorted(original_data))
