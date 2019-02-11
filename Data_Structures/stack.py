# Note: for Queue in Python either of enqueue or dequeue will be O(n) or you should use:
# from collections import deque (double-sided queue so you have peek available)
# d = deque()
# d.count()
# >> > d.append('j')                    # add a new entry to the right side O(1)
# >> > d.appendleft('f')                # add a new entry to the left side O(1)
# >> > d.append('j')                    # add a new entry to the right side O(1)
# >> > d.appendleft('f')                # add a new entry to the left side O(1)
# >> > list(d)                          # list the contents of the deque
# ['g', 'h', 'i']
# >> > d[0]                             # peek at leftmost item
# 'g'
# >> > d[-1]                            # peek at rightmost item
# 'i'
import pdb
class Stack:
    def __init__(self, store=None):
        self.store = [el for el in store] #NB: Do not just assign to store. This will be one list shared across objects!

    def peek(self):
        return self.store[-1] if self.size() else None

    def size(self):
        return len(self.store)

    def pop(self):
        return self.store.pop() if self.size() else None
            
    def push(self, val):
        self.store.append(val)

    def __len__(self):
        return len(self.store)