# Array Index & Element Equality
# Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

# Examples:

# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2

# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.
# Constraints:

# [time limit] 5000ms

# [input] array.integer arr

# 1 ≤ arr.length ≤ 100
# [output] integer

def bin_search(arr, start=0, end=-1, result=float('inf')):
  end = end if end != -1 else len(arr)
  if end <= start or arr == []:
    if result == float('inf'):
      return -1
    return result

  mid = start + ((end - start) // 2)
  
  if arr[mid] == mid and mid < result:
    result = mid
    return bin_search(arr, start, mid, result)
  if arr[mid] < mid:
    return bin_search(arr, mid+1, end, result)
  else:
    return bin_search(arr, start, mid, result)

def index_equals_value_search(arr):
  return bin_search(arr)