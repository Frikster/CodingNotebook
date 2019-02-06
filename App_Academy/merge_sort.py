 # Write an Array#merge_sort method; it should not modify the original array.

def merge_sort(arr, key=None):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key=None):
    key = key or (lambda a,b: -1 if a < b else 1 if a > b else 0)
    res = []
    while len(left) > 0 and len(right) > 0:
      if key(left[0], right[0]) == -1:
       res.append(left.pop(0)) #TODO: This is O(n) and has to be fixed...
      else:
       res.append(right.pop(0))
    return res + left + right


merge_sort([23, 5, 3, 4, 4, 4, 5, 35, 7, 567, 6])
# [3, 4, 4, 4, 5, 5, 6, 7, 23, 35, 567]
