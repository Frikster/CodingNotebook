from .stack import Stack
import pdb

class MinMaxStack:
    def __init__(self, store=[]):
        self.store = Stack(store)

    def peek(self):
        return self.store.peek()

    def size(self):
        return self.store.size()

    def push(self, el):
        new_max = el if el > self.max() else self.max()
        new_min = el if el < self.min() else self.min()
        self.store.push({'value': el, 'min': new_min, 'max': new_max})

    def pop(self):
        return self.store.pop()['value']

    def min(self):
        return self.peek()['min'] if self.peek() else float('inf')

    def max(self):
        return self.peek()['max'] if self.peek() else float('-inf')
