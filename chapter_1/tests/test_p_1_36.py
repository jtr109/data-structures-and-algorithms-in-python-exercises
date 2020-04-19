import unittest

from chapter_1.p_1_36 import count_words


class MyTestCase(unittest.TestCase):

    def test_count_words(self):
        text = 'to be or not to be'
        expected = {
            'to': 2,
            'be': 2,
            'or': 1,
            'not': 1,
        }
        self.assertDictEqual(count_words(text), expected)
