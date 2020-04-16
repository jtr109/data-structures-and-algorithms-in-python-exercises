import unittest

from chapter_1.c_1_19 import list_letters


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.assertListEqual(list_letters(), expected)
