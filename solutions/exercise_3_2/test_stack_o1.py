from .test_stack import TestStack
from exercise_3_1.stack_o1 import StackO1


class TestStackO1(TestStack):
    """ test StackO1 by inheriting the Stack tests. """

    def test(self):
        self.t(StackO1())

    def testEmpty(self):
        self.empty(StackO1())
