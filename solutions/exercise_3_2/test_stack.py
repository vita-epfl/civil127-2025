import unittest

from exercise_3_1.stack import Stack


class TestStack(unittest.TestCase):
    def test(self):
        self.t(Stack())

    def testEmpty(self):
        self.empty(Stack())

    def t(self, s):
        s.push(1)
        s.push(5)
        self.assertEqual(s.max(), 5)
        self.assertEqual(s.min(), 1)
        s.push(9)
        self.assertEqual(s.pop(), 9)
        s.push(2)
        self.assertEqual(s.max(), 5)
        self.assertEqual(s.min(), 1)

    def empty(self, s):
        self.assertRaises(IndexError, s.pop)
        self.assertRaises(IndexError, s.max)
        self.assertRaises(IndexError, s.min)
