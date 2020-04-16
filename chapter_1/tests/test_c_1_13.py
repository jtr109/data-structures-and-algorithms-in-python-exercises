import unittest

from chapter_1.c_1_13 import my_reverse


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        data = ['foo', 'bar', 'biz', 'buz']
        my_reverse(data)
        expected_reversed = ['buz', 'biz', 'bar', 'foo']
        self.assertListEqual(data, expected_reversed)
        data = [3, 1, 4, 1, 5]
        my_reverse(data)
        expected_reversed = [5, 1, 4, 1, 3]
        self.assertListEqual(data, expected_reversed)
