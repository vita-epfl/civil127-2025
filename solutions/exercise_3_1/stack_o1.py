class StackO1:
    """
    Stack with O(1) runtime for push, pop, max, and min operations.
    
    Uses additional O(1) memory compared to stack.py, we trade
    memory for cpu.
    """

    def __init__(self):
        self.s = []
        self.max_stack = []
        self.min_stack = []

    def push(self, n):
        self.s.append(n)
        new_max = n
        if self.max_stack != []:
            new_max = max(self.max(), n)
        self.max_stack.append(new_max)

        new_min = n
        if self.min_stack != []:
            new_min = min(self.min(), n)
        self.min_stack.append(new_min)

    def pop(self):
        self.max_stack.pop()
        self.min_stack.pop()
        return self.s.pop()

    def max(self):
        if self.s == []:
            raise IndexError("empty stack")
        return self.max_stack[-1]

    def min(self):
        if self.s == []:
            raise IndexError("empty stack")
        return self.min_stack[-1]

