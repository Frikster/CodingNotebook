from .stack import Stack
import pdb 

class StackQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()

    def enqueue(self, val):
        self.in_stack.push(val)

    def dequeue(self):
        # only have to do this once for every n dequeue operations, so it amortizes
        # to O(1)
        if not self.out_stack.size():
            while self.in_stack.size():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

