from .static_array import StaticArray

# Methods missing can be found in ring_buffer
class DynamicArray:
    def __init__(self):
        self._store = StaticArray(8)
        self._capacity = 8
        self.length = 0

     # O(1)
    def __getitem__(self, index):
        self.__check_index(index)
        self._store[index] 

    # O(1)
    def __setitem__(self, index, value):
        self.__check_index(index)
        self._store[index] = value

    def __len__(self):
        return self.length

    def __check_index(self, index):
        if not 0 < index < len(self):
                raise IndexError('index out of bounds')

    # O(1)
    def pop(self):
        self.__check_index(len(self) - 1)
        self.length -= 1
        return self._store[len(self) + 1]

    # O(1) ammortized; O(n) worst case. Variable because of the possible
    # resize.
    def append(self, val):
        if len(self) == self._capacity: self.resize()
        self.length += 1
        self[len(self) - 1] = val

    # O(n): has to shift over all the elements.
    def shift(self):
        self.__check_index(len(self) - 1)
        for idx in range(len(self)):
            self[idx] = self[idx+1]
        self.length -= 1

    # O(n): has to shift over all the elements.
    def unshift(self, val):
        if len(self) == self._capacity: self.resize()
        self.length += 1
        for idx in range(len(self),0,-1):
            self[idx] = self[idx-1]
        self[0] = val

    # O(n): has to copy over all the elements to the new store.
    def resize(self):
        newStore = StaticArray(self._capacity * 2)
        for idx in range(len(self)):
            newStore[idx] = self[idx]
        self._capacity *= 2
        self._store = newStore
