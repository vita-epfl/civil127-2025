import unittest


def wrap_underscores(word):
    '''Adds an underscore between each letter. E.g. "hello" becomes "_h_e_l_l_o_".'''
    r = "_"
    for i in range(len(word)):
        r = word[i] + "_"
    return r


class TestWrapUnderscores(unittest.TestCase):
    def test(self):
        a = wrap_underscores("hello")
        self.assertEqual(a, "_h_e_l_l_o_")

