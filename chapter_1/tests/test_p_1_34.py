import unittest

from chapter_1.p_1_34 import repeat


class MyTestCase(unittest.TestCase):

    def test_list_combinations(self):
        text = 'I will never spam my friends again.'
        self.assertEqual(len(list(filter(lambda x: x != text, list(repeat())))), 8)
