import unittest

from chapter_1.p_1_31 import return_change


class MyTestCase(unittest.TestCase):

    def test_list_combinations(self):
        self.assertListEqual(sorted(return_change(100, 8)), sorted([50, 20, 20, 2]))
        self.assertListEqual(sorted(return_change(10, 2)), sorted([5, 2, 1]))
