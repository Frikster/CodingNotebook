 # Write a method, `Array#two_sum`, that finds all pairs of positions where the
 # elements at those positions sum to zero.

 # NB: ordering matters. I want each of the pairs to be sorted smaller index
 # before bigger index. I want the array of pairs to be sorted
 # "dictionary-wise":
 #   [0, 2] before [1, 2] (smaller first elements come first)
 #   [0, 1] before [0, 2] (then smaller second elements come first)


def two_sum(arr, target_sum):
    complement_idxs = {}
    res = []

    for idx, el in enumerate(arr):
        target = target_sum - el
        if target in complement_idxs:
            res.append(sorted([idx, complement_idxs[target]]))
        complement_idxs[el] = idx
    return res


# O(n^2) time complexity (as opposed to O(n^4) brute force)
# O(n^2) space complexity

def four_sum(arr, target):
    # the first hash contains each of the elements that we have checked thus far
    all_hash = {}
    # two_sum_hash contains sums of two elements from our array
    two_sum_hash = {}
    # three_sum_hash contains sums of three elements from our array
    three_sum_hash = {}
    res = []

    for idx, num in enumerate(arr):
        # Return true if there is a sum of three numbers equal to the difference of
        # the target and the current num (i.e., if the current num and one of the
        # three_sums sum to the target)
        if target - num in three_sum_hash:
            res.append(sorted([idx] + three_sum_hash[target - num]))

        # if we have any nums in our two_sum hash, add the current num to each to
        # populate a hash of three_sums
        for key in two_sum_hash.keys():
            three_sum_hash[key + num] = two_sum_hash[key] + [idx]

        # if we have any nums in our single num hash, sum the current num
        # with each of these numbers and store them in a hash of possible two sums
        for key in all_hash.keys():
            two_sum_hash[key + num] = all_hash[key] + [idx]

        # lastly, add the num to a hash of all nums
        all_hash[num] = [idx]

    return res


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
# [[1, 3, 4, 5], [1, 2, 5, 6]]
