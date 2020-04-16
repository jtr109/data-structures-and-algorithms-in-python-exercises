import unittest

from chapter_1.r_1_10 import sequence


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        self.assertListEqual(sequence(), [8, 6, 4, 2, 0, -2, -4, -6, -8])
