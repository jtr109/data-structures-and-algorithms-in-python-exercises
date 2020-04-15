import random
import unittest

from chapter_1.r_1_3 import minmax


class MyTestCase(unittest.TestCase):

    def test_minmax(self):
        data = [random.randint(0, 99) for _ in range(100)]
        self.assertEqual(minmax(data), (min(data), max(data)))
