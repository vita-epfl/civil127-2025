import unittest


def wrap_underscores(word):
    '''
    Adds an underscore between each letter. E.g. "hello" becomes "_h_e_l_l_o_".
    If word is empty, returns an empty string.
    '''
    if word == "":
        return ""
    if word == "":
        return ""
    return "_" + "_".join(word) + "_"


class TestWrapUnderscores(unittest.TestCase):
    def test(self):
        a = wrap_underscores("hello")
        self.assertEqual(a, "_h_e_l_l_o_")

    def testEmpty(self):
        self.assertEqual(wrap_underscores(""), "")
