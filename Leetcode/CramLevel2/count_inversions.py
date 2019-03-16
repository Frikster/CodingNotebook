# Function Description
# Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.
# countInversions has the following parameter(s):
# arr: an array of integers to sort .

# input: 1 1 1 2 2
# output: 0
# input: 2 1 3 1 2
# output: 4

#!/bin/python3
# Complete the countInversions function below.
def countInversions(arr):
    inversion_sort = countInversionsSort()
    inversion_sort.merge_sort(arr)
    return inversion_sort.count


class countInversionsSort:
    def __init__(self):
        self.count = 0

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        left_idx = 0
        right_idx = 0
        while left_idx < len(left) and right_idx < len(right):
            if right[right_idx] < left[left_idx]:
                res.append(right[right_idx])
                right_idx += 1
                # We would add the length of the remaining elements on the left side
                # because as soon as we add an element from the right side all these
                # elements are getting shifted (?)
                self.count += (len(left)-left_idx)
            else:
                res.append(left[left_idx])
                left_idx += 1
        for idx in range(left_idx, len(left)):
            res.append(left[idx])
        for idx in range(right_idx, len(right)):
            res.append(right[idx])
        return res

