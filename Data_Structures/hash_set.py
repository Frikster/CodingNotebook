class HashSet:
  def __init__(self, num_buckets = 8):
    self.store = [[] for _ in range(num_buckets)]
    self.count = 0

  def insert(self, key):
    if self.__contains__(key):
      return False
    self.store[hash(key) % self._num_buckets].append(key)
    self.count += 1
    if self._num_buckets < self.count: self._resize()
    return key

  def __contains__(self, key):
    return key in self.store[hash(key) % self._num_buckets]

  def remove(self, key):
    if not key in self:
      return None
    self.store[hash(key) % self._num_buckets].remove(key)
    self.count -= 1

  def _num_buckets(self):
    return len(self.store)

  def _resize(self):
    old_store = self.store
    self.count = 0
    self.store = [[] for _ in self._num_buckets * 2]
    for num in [num for bucket in old_store for num in bucket]:
        self.insert(num)

