from .linked_list import LinkedList, Node

class HashMap:
    def __init__(self, num_buckets=8):
        self.store = [LinkedList() for _ in range(num_buckets)]
        self.count = 0

    def __len__(self):
        return len(self.store)

    def __contains__(self, key):
        return key in self._bucket(key)

    def __setitem__(self, key, val):
        if self.count >= self._num_buckets:
            self._resize()
        if key in self:
            self._bucket(key)[key] = val
        else:
            self._bucket(key).append(key, val)
            self.count += 1

    def __getitem__(self, key):
        return self._bucket(key)[key]

    def delete(self, key):
        removal = self._bucket(key).remove(key)
        if removal: self.count -= 1
        return removal

    def __iter__(self):
        for bucket in self.store:
            for link in bucket:
                yield [link.key, link.val]

    def __str__(self):
        res = ''
        for key in self:
            res += f'{key}: {self[key]} \n'
        return res

    def _num_buckets(self):
        return len(self.store)

    def _resize(self):
        old_store = self.store
        self.store = [LinkedList() for _ in range(self._num_buckets)]
        self.count = 0
        for bucket in old_store:
            for link in bucket:
                self[link.key] = link.val

    def _bucket(self, key):
        return self.store[hash(key) % self._num_buckets]

