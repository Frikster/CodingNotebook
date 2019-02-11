from .min_max_stack import MinMaxStack
import pdb

class MinMaxStackQueue:
    def __init__(self):
        self.in_stack = MinMaxStack()
        self.out_stack = MinMaxStack()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()

    def peek(self):
        return self.out_stack.peek()

    def enqueue(self, val):
        self.in_stack.push(val) 

    def dequeue(self):
        if not self.out_stack.size():
            while self.in_stack.size():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def max(self):
        return max(self.in_stack.max(), self.out_stack.max())

    def min(self):
        return min(self.in_stack.min(), self.out_stack.min())

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
