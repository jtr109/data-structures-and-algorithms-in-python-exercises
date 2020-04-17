import unittest

from chapter_1.p_1_30 import flat_division


class MyTestCase(unittest.TestCase):

    def test_list_combinations(self):
        self.assertEqual(flat_division(4), 2)
        self.assertEqual(flat_division(5), 2)
        self.assertEqual(flat_division(8), 3)
        self.assertEqual(flat_division(10), 3)
        self.assertEqual(flat_division(16), 4)
