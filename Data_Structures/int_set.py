# IntSet where you know the max
class MaxIntSet:
    def __init__(self, max):
        self.store = [False] * max
    
    def insert(self, num):
        self.validate(num)
        if self.store[num]: return False
        self.store[num] = True

    def remove(self, num):
        self.validate(num)
        if not num in self: raise ValueError(str(num) + ' not found')
        self.store[num] = False
        return num

    def __contains__(self, num):
        self.validate(num)
        return self.store[num]
    
    def is_valid(self, num):
        return 0 <= num <= self.store.length - 1

    def validate(self, num):
        if not self.is_valid(num): raise Exception("Out of bounds")
    

class IntSet:
    def __init__(self, num_buckets=20):
        self.store = [[] for _ in num_buckets]
        self.num_buckets = num_buckets

    def insert(self, num):
        if num in self: return False
        self.store[num % self.num_buckets].append(num)
        return num

    def remove(self, num):
        self.store[num % self.num_buckets].remove(num)

    def __contains__(self, num):
        return num in self.store[num % self.num_buckets]

class ResizingIntSet:
    def __init__(self, num_buckets=20):
        self.store = [[] for _ in num_buckets]
        self.count = 0

    def insert(self, num):
        if num in self: return False
        self.store[num % len(self.store)].append(num)
        self.count += 1
        if len(self.store) < self.count: self._resize()
        return num

    def remove(self, num):
        self.store[num % len(self.store)].remove(num)
        self.count -= 1

    def __contains__(self, num):
        return num in self.store[num % len(self.store)]

    def _resize(self):
        old_store = self.store
        self.count = 0
        self.store = [[] for _ in len(self.store)*2]
        for num in [el for bucket in old_store for el in bucket]:
            self.insert(num)
