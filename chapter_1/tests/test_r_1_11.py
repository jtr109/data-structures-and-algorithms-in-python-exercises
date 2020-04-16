import unittest

from chapter_1.r_1_11 import sequence


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        self.assertListEqual(sequence(), [1, 2, 4, 8, 16, 32, 64, 128, 256])
