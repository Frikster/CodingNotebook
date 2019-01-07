class QuickSort:
 # Quick sort has average case time complexity O(nlogn), but worst
 # case O(n**2).
 # Checked for correctness here: https://repl.it/@DirkHaupt/QuickSort

 # Not in-place. Uses O(n) memory.
    @classmethod
    def sort1(self, arr, key=None):
        if len(arr) <= 1:
            return arr
        key = key or (lambda a, b: -1 if a < b else 1 if a > b else 0)
        pivot = arr.pop(0)
        left = list(filter(lambda el: key(el, pivot) == -1, arr))
        right = list(filter(lambda el: key(el, pivot) != -1, arr))
        return self.sort1(left, key) + [pivot] + self.sort1(right, key)

    # In-place.
    @classmethod
    def sort2(self, array, start=0, length=None, key=None):
        length = length or len(array)
        key = key or (lambda a, b: -1 if a < b else 1 if a > b else 0)
        if length < 2:
            return array
        pivot_idx = self.partition(array, start, length, key)
        left_len = pivot_idx - start
        right_len = length - (left_len + 1)
        if left_len:
            self.sort2(array, start, left_len, key)
        if right_len:
            self.sort2(array, pivot_idx+1, right_len, key)
        return array

    @classmethod
    def partition(self, array, start, length, key=None):
        key = key or (lambda a, b: -1 if a < b else 1 if a > b else 0)
        pivot_idx = start
        pivot = array[pivot_idx]
        for idx in range((start + 1), (start + length)):
            if key(pivot, array[idx]) >= 0:
                array[idx], array[pivot_idx +
                                  1] = array[pivot_idx + 1], array[idx]
                pivot_idx += 1
        array[start], array[pivot_idx] = array[pivot_idx], array[start]
        return pivot_idx


QuickSort.sort2([2, 4, 345, 23, 3, 3, 45, 3, 6, 3, 6, 346, 456, 6, 6, 6])
# [2, 3, 3, 3, 3, 4, 6, 6, 6, 6, 6, 23, 45, 345, 346, 456]
