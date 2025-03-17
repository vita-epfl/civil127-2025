import os
import unittest
from exercise_4_1.cal import Cal


class TestCal(unittest.TestCase):
    def testJan2025(self):
        c = Cal()
        c.year(2025)
        c.month('jan')
        c.week_start('sun')
        output = c.build()
        # add the newline which print() adds
        output += "\n"
        file = os.path.join("exercise_4_1", "jan_2025.txt")
        with open(file, "r") as f:
            file_content = "".join(f)
        self.assertEqual(output, file_content)

    def testAug2025(self):
        c = Cal()
        c.year(2025)
        c.month('aug')
        output = c.build()
        # add the newline which print() adds
        output += "\n"
        file = os.path.join("exercise_4_1", "aug_2025.txt")
        with open(file, "r") as f:
            file_content = "".join(f)
        self.assertEqual(output, file_content)
