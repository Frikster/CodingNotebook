#returns all subsets of an array
def subsets(array):
  if len(array) == 0 : return [[]]
  first = array[0]
  rest_sub = subsets(array[1:])
  return rest_sub + list(map(lambda sub: [first] + sub, rest_sub))

subsets([1, 2, 3])
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
