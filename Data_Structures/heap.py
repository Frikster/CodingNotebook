import pdb
class BinaryMinHeap:

  def __init__(self, key=None):
    key = key or (lambda a,b: 1 if a > b else -1 if a < b else 0)
    self.key = key
    self.store = []
  
  def extract(self):
    self.store[0], self.store[len(self.store) - 1] = self.store[len(self.store) - 1], self.store[0]
    val = self.store.pop()
    BinaryMinHeap.heapify_down(self.store, 0, len(self.store), self.key)
    return val

  def peek(self):
    return self.store[0]

  def push(self, val):
    self.store.append(val)
    # pdb.set_trace()
    BinaryMinHeap.heapify_up(self.store, len(self.store) - 1, len(self.store), self.key)
  
  @classmethod
  def child_indices(self, length, parent_index):
    left = 2*parent_index + 1
    right = 2*parent_index + 2
    return [left, right] if right < length else [left] if left < length else []
  
  @classmethod
  def parent_index(self, child_index):
    if child_index == 0 : raise "root has no parent" 
    return (child_index - 1) // 2
  
  @classmethod
  def heapify_down(self, array, parent_idx, length=None, key=None):
    length = length or len(array)
    key = key or (lambda a, b: 1 if a > b else -1 if a < b else 0)

    idxs = BinaryMinHeap.child_indices(length, parent_idx)
    if not idxs : return array

    smallest_idx = idxs[0]
    if len(idxs) == 2:
      smallest_idx = idxs[0] if key(array[idxs[0]], array[idxs[1]]) <= 0 else idxs[1]

    if key(array[smallest_idx], array[parent_idx]) < 0:
      array[parent_idx], array[smallest_idx] = array[smallest_idx], array[parent_idx]
      BinaryMinHeap.heapify_down(array, smallest_idx, length, key)
    
    return array

  @classmethod
  def heapify_up(self, array, child_idx, length=None, key=None):
    length = length or len(array)
    key = key or (lambda a, b: 1 if a > b else -1 if a < b else 0)

    if child_idx == 0 : return array 
    parent_idx = BinaryMinHeap.parent_index(child_idx)

    if key(array[parent_idx], array[child_idx]) > 0:
      array[parent_idx], array[child_idx] = array[child_idx], array[parent_idx]
      BinaryMinHeap.heapify_up(array, parent_idx, length, key)
    
    return array
  
heap = BinaryMinHeap()
heap.push(7)
heap.push(5)
heap.push(6)
heap.push(4)
assert(heap.store == [4, 5, 6, 7])
assert(heap.extract() == 4)
assert(heap.extract() == 5)
assert(heap.store == [6,7])

