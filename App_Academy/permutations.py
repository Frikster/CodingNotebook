# Write a recursive method that returns all of the permutations of an array
def permutations(array):
    if len(array) <= 1 : return [array]
    first = array[0]
    perms = permutations(array[1:])
    res = []
    for perm in perms:
        for idx in range(len(perm)+1):
            res.append(perm[0:idx] + [first] + perm[idx:])
    return res


print(permutations([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
