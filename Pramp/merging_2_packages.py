'''
Merging 2 Packages
Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input] integer limit

[output] array.integer
'''

def get_indices_of_item_wights(arr, limit):
  index_hash = {}

  for idx, el in reversed(list(enumerate(arr))):
   if index_hash.get(limit - el, False):
     el1 = index_hash[limit - el]
     el2 = idx
     return [el1, el2] if el1 > el2 else [el2, el1]
   index_hash[el] = idx

  return []
