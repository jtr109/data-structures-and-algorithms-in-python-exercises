import unittest

from chapter_1.c_1_21 import reverse_lines


class MyTestCase(unittest.TestCase):

    def test_shuffle(self):
        text = '''Chor. Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventur'd piteous overthrows
Doth with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, naught could remove,
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend.'''
        expected = '''What here shall miss, our toil shall strive to mend.
The which if you with patient ears attend,
Is now the two hours' traffic of our stage;
Which, but their children's end, naught could remove,
And the continuance of their parents' rage,
The fearful passage of their death-mark'd love,
Doth with their death bury their parents' strife.
Whose misadventur'd piteous overthrows
A pair of star-cross'd lovers take their life;
From forth the fatal loins of these two foes
Where civil blood makes civil hands unclean.
From ancient grudge break to new mutiny,
In fair Verona, where we lay our scene,
Chor. Two households, both alike in dignity,'''
        self.assertEqual(reverse_lines(text), expected)
