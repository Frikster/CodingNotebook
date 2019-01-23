# TODO: Test
from .static_array import StaticArray

class RingBuffer:
    def __init__(self, capacity = 8):
        self.store = StaticArray(capacity)
        self.count = 0
        self.start_idx = 0

    def __len__(self):
        return self.count

    def capacity(self):
        return len(self.store)

    def __getitem__(self, idx):
        if not -len(self) < idx < len(self): 
            return None
        if idx < 0:
            return self[len(self) + idx]
        return self.store[(self.start_idx + idx) % self.capacity()]

    def __setitem__(self, idx, val):
        if idx >= len(self):
            for _ in range(idx - len(self)):
                self.append(None)
        elif idx < 0:
            if idx < -len(self): return None
            self[len(self) + idx] = val
        if idx == len(self):
            if self.capacity() == len(self): self.__resize()
            self.count += 1
        self.store[(self.start_idx + idx) % self.capacity()] = val # cant use negatives as static array doesn't allow it

    def __contains__(self, val):
        return True if val in self.store else False

    def append(self, val):
        if self.capacity() == len(self): self.__resize()
        self.store[(self.start_idx + len(self)) % self.capacity()] = val
        self.count += 1
        return self

    def unshift(self, val):
        if self.capacity() == len(self): self.__resize()
        self.start_idx = (self.start_idx - 1) % self.capacity()
        self.store[self.start_idx] = val
        self.count += 1
        return self

    def pop(self):
        if self.count == 0: return None
        self.count -= 1
        return self.store[(self.start_idx + len(self)) % self.capacity()]
        
    def shift(self):
        if len(self) == 0: return None
        self.count -= 1
        first_item = self.store[self.start_idx]
        self.start_idx = (self.start_idx + 1) % self.capacity()
        return first_item

    def first(self):
        if len(self) == 0: return None
        return self.store[self.start_idx]

    def last(self):
        if len(self) == 0: return None
        return self.store[(self.start_idx + self.count - 1) % self.capacity()]

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        res = "["
        for idx, el in enumerate(self):
            res += str(el) + ', ' if idx < len(self) - 1 else str(el)
        return res + ']' 

    def __eq__(self, other):
        if len(other) != len(self): return False
        for idx, el in enumerate(self):
            if el != other[idx]:
                return False
        return True

    def __resize(self):
        new_store = StaticArray(self.capacity() * 2)
        for idx, el in enumerate(self):
            new_store[idx] = el
        self.store = new_store
        self.start_idx = 0
