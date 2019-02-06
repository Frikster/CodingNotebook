  # Write a version of merge. This should NOT modify the original hash
def my_merge(hash1, hash2):
    dupe = hash1.copy()
    for k in hash2:
        dupe[k] = hash2[k]
    return dupe


a = {1: 1, 2: 2, 3: 4}
b = {1: 2, 4: 4}
my_merge(a, b)
# {1: 2, 2: 2, 3: 4, 4: 4}
a
# {1: 1, 2: 2, 3: 4}
