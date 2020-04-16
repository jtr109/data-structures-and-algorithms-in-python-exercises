import unittest

from chapter_1.c_1_18 import sequence


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        self.assertListEqual(sequence(), [0, 2, 6, 12, 20, 30, 42, 56, 72, 90])
