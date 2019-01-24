# Implement a queue with #enqueue and #dequeue, as well as a #max API,
# a method which returns the maximum element still in the queue. This
# is trivial to do by spending O(n) time upon dequeuing.
# Can you do it in O(1) amortized? Maybe use an auxiliary storage structure?

# Use your RingBuffer to achieve optimal shifts! Write any additional
# methods you need.

from ring_buffer import RingBuffer

class QueueWithMax:
    def __init__(self):
        self.store = RingBuffer()
    
    def enqueue(self, val):
        if val > self.max():
            self.store.append({"val": val, "max": val})
        else:
            self.store.append({"val": val, "max": self.max()})
        return self.store.append(val)

    def dequeue(self):
        return self.store.shift()['val']

    def max(self):
        if len(self) == 0: return float("-inf")
        return self.store[-1]['max']
        
    def __len__(self):
        return len(self.store)


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
