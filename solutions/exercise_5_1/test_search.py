import unittest
from exercise_5_1.search import all_different, alternating, three_consecutive


class TestSearch(unittest.TestCase):
    def test_three_consecutive(self):
        self.assertTrue(three_consecutive("122234"))

    def test_all_different(self):
        self.assertTrue(all_different("921035"))

    def test_alternating(self):
        self.assertTrue(alternating("285609"))
        self.assertTrue(alternating("638342"))
        self.assertFalse(alternating("842305"))
        self.assertFalse(alternating("285600"))
