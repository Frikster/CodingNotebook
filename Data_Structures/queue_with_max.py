# Implement a queue with #enqueue and #dequeue, as well as a #max API,
# a method which returns the maximum element still in the queue. This
# is trivial to do by spending O(n) time upon dequeuing.
# Can you do it in O(1) amortized? Maybe use an auxiliary storage structure?

import pdb
import unittest
from Data_Structures.ring_buffer import RingBuffer
from Data_Structures.min_max_stack_queue import MinMaxStackQueue

class QueueWithMax:
    def __init__(self):
        self.store = MinMaxStackQueue()
    
    def enqueue(self, val):
        self.store.enqueue(val)

    def dequeue(self):
        return self.store.dequeue()

    def max(self):
        if len(self) == 0: return float("-inf")
        return self.store.max()
        
    def __len__(self):
        return len(self.store)


class Queue:
    def __init__(self):
        self.store = RingBuffer()

    def enqueue(self, val):
        self.store.append(val)

    def dequeue(self):
        return self.store.shift()

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return self.store.__str__()


class Test(unittest.TestCase):
    def test_queue_with_max(self):
        q = QueueWithMax()
        print(q.max())
        q.enqueue(5)
        print(q.max())
        q.enqueue(1)
        print(q.max())
        q.enqueue(50)
        print(q.max())
        q.enqueue(5)
        print(q.max())
        q.dequeue()
        q.dequeue()
        print(q.max())
        q.dequeue()
        print(q.max())


    def test_queue(self):
        q = Queue()
        print(q)
        q.enqueue(5)
        print(q)
        q.enqueue(1)
        print(q)
        q.enqueue(50)
        print(q)
        q.enqueue(5)
        print(q)
        q.dequeue()
        q.dequeue()
        print(q)
        q.dequeue()
        print(q)

if __name__ == "__main__":
  unittest.main()
