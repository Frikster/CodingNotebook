 # Write a method, `Array#two_sum`, that finds all pairs of positions where the
 # elements at those positions sum to zero.

 # NB: ordering matters. I want each of the pairs to be sorted smaller index
 # before bigger index. I want the array of pairs to be sorted
 # "dictionary-wise":
 #   [0, 2] before [1, 2] (smaller first elements come first)
 #   [0, 1] before [0, 2] (then smaller second elements come first)

def two_sum(arr):
    res = []
    for idx in range(len(arr)):
        for jdx in range(len(arr)):
            if arr[idx] + arr[jdx] == 0 and idx < jdx:
                res.append([idx, jdx])
    return res


two_sum([5, -1, -5, 1])
#[[0, 2], [1, 3]]
two_sum([5, -5, -5])
#[[0, 1], [0, 2]]
two_sum([0, 1, 2, 3])
#[]
