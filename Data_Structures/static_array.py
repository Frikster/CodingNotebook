# This class just dumbs down a regular Array to be statically sized.
class StaticArray:
    def __init__(self, length):
        self._store = [None] * length
        self.length = length

    # O(1)
    def __getitem__(self, index):
        if not 0 < index < len(self):
            raise IndexError('static array bad index')
        return self._store[index]

    # O(1)
    def __setitem__(self, index, value):
        if not 0 < index < len(self):
            raise IndexError('static array bad index')
        self._store[index] = value

    def __len__(self):
        return self.length
