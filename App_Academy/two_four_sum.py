 # Write a method, `Array#two_sum`, that finds all pairs of positions where the
 # elements at those positions sum to zero.

 # NB: ordering matters. I want each of the pairs to be sorted smaller index
 # before bigger index. I want the array of pairs to be sorted
 # "dictionary-wise":
 #   [0, 2] before [1, 2] (smaller first elements come first)
 #   [0, 1] before [0, 2] (then smaller second elements come first)

def two_sum(arr, target):
    complement_idxs = {}
    res = []

    for idx, el in enumerate(arr):
        if target - el in complement_idxs:
            res.append(sorted([idx, complement_idxs[target - el]]))
        complement_idxs[el] = idx
    return sorted(res)

# https://stackoverflow.com/a/14737071/2734863
# O(N^2) Time O(N^2) Space in average case
def four_sum(arr, target):
    pair_sums = {}
    for idx in range(len(arr)):
        for jdx in range(idx+1, len(arr)):
            if arr[idx]+arr[jdx] in pair_sums:
                pair_sums[arr[idx]+arr[jdx]].append([idx, jdx])
            else:
                pair_sums[arr[idx]+arr[jdx]] = [[idx, jdx]]
    res = []
    for pair_sum in pair_sums:
        # At this point pair_sums is of size O(N^2) so this single loop is O(N^2)
        # However, with a ton of duplicates, pair_sums gets smaller and smaller (one key to an array of all the index pairs that sum to the key)
        # In the worst case of all duplicates, this loop is O(1) and the ones below are O(N^2)
        # Because then there is only one key and the two following loops need to loop through O(N) each
        # From this I conclude that the algorithm is O(N^2) generally
        if target - pair_sum in pair_sums:
            for pair1 in pair_sums[pair_sum]:
                for pair2 in pair_sums[target - pair_sum]: # Reaches O(N^3) for a lot of duplicate values. Note it is O(N^2) if no duplicates since the two for loops essentially "don't exist"
                    candidate = pair1+pair2
                    if sorted(candidate) == candidate and len(list(set(candidate))) == 4:
                        res.append(sorted(candidate))
    return sorted(res)


# 1533153315331533153315331533... (million repeated), target = 6... each 1 to each 5 and each 5 to each 1... lot of indices
# also each 3 to each 3,

# NOTE: I am not convinced this is correct because we are iterating through every element in the array O(N) and every possible combination in two_sum_hash which in the worst case is O(N^2). So the algorithm as written is actually O(N^3) is it not?
# O(n^2) time complexity (as opposed to O(n^4) brute force)
# O(n^2) space complexity

# App Academy's more convoluted four_sum

# def four_sum(arr, target):
#     # the first hash contains each of the elements that we have checked thus far
#     all_hash = {}
#     # two_sum_hash contains sums of two elements from our array
#     two_sum_hash = {}
#     # three_sum_hash contains sums of three elements from our array
#     three_sum_hash = {}
#     res = []

#     for idx, num in enumerate(arr):
#         # Return true if there is a sum of three numbers equal to the difference of
#         # the target and the current num (i.e., if the current num and one of the
#         # three_sums sum to the target)
#         if target - num in three_sum_hash:
#             res.append(sorted([idx] + three_sum_hash[target - num]))

#         # if we have any nums in our two_sum hash, add the current num to each to
#         # populate a hash of three_sums
#         for key in two_sum_hash.keys():
#             three_sum_hash[key + num] = two_sum_hash[key] + [idx]

#         # if we have any nums in our single num hash, sum the current num
#         # with each of these numbers and store them in a hash of possible two sums
#         for key in all_hash.keys():
#             two_sum_hash[key + num] = all_hash[key] + [idx]

#         # lastly, add the num to a hash of all nums
#         all_hash[num] = [idx]

#     return res


print(two_sum([5, -1, -5, 1],0))
#[[0, 2], [1, 3]]
print(two_sum([5, -5, -5],0))
#[[0, 1], [0, 2]]
print(two_sum([0, 1, 2, 3],0))
#[]

print(four_sum([5, -1, -5, 1], 0))
# [[0, 1, 2, 3]]
print(four_sum([5, 1, -5, 3, 2, 2], 8))
# [[1, 3, 4, 5]]
print(four_sum([5, 1, -5, 3, 2, 2, 10], 8))
# [[1, 2, 4, 6], [1, 2, 5, 6], [1, 3, 4, 5]]
