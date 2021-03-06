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
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
      if key(left[left_idx], right[right_idx]) == -1:
       res.append(left[left_idx])
       left_idx+=1
      else:
       res.append(right[right_idx])
       right_idx+=1
    for idx in range(left_idx, len(left)):
        res.append(left[idx])
    for idx in range(right_idx, len(right)):
        res.append(right[idx])
    return res

print(merge(sorted([23, 5, 3, 4, 4]),sorted([4, 5, 35, 7, 567, 6])))
print(merge_sort([23, 5, 3, 4, 4, 4, 5, 35, 7, 567, 6]))
# [3, 4, 4, 4, 5, 5, 6, 7, 23, 35, 567]
