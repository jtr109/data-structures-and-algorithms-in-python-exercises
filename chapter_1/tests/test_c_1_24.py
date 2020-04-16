import unittest

from chapter_1.c_1_24 import count_vowel


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        text = 'Data Structures and Algorithms in Python'
        expected = {'a': 4, 'e': 1, 'i': 2, 'o': 2, 'u': 2}
        self.assertDictEqual(count_vowel(text), expected)
