import unittest

from chapter_1.r_1_9 import sequence


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        self.assertListEqual(sequence(), [50, 60, 70, 80])
