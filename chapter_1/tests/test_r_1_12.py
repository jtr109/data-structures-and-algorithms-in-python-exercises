import unittest

from chapter_1.r_1_12 import choice


class MyTestCase(unittest.TestCase):

    def test_sequence(self):
        data = ['foo', 'bar', 'biz', 'buz']
        self.assertIn(choice(data), data)
