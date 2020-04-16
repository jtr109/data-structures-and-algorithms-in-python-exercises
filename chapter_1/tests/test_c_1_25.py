import unittest

from chapter_1.c_1_25 import excluding_symbols


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        text = "Let's try, Mike."
        expected = 'Lets try Mike'
        self.assertEqual(excluding_symbols(text), expected)
