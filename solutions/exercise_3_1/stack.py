class Stack:
    """
    list(), min(), max() give us everything we need, so our stack is a thin wrapper
    around those.
    """

    def __init__(self):
        self.s = []

    def push(self, n):
        self.s.append(n)

    def pop(self):
        return self.s.pop()

    def max(self):
        if self.s == []:
            raise IndexError("empty stack")
        return max(self.s)

    def min(self):
        if self.s == []:
            raise IndexError("empty stack")
        return min(self.s)
