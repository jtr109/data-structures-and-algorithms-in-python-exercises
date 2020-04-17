import unittest

from chapter_1.p_1_29 import list_combinations


class MyTestCase(unittest.TestCase):

    def test_list_combinations(self):
        chars = ['a', 'b', 'c']
        expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertListEqual(sorted(list_combinations(chars)), sorted(expected))
