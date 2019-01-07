 # Takes a multi-dimentional array and returns a single array of all the elements
 # [1,[2,3], [4,[5]]].my_controlled_flatten(1) => [1,2,3,4,5]
def my_flatten(arr):
    res = []
    for el in arr:
        if isinstance(el,list):
            res += my_flatten(el)
        else: 
            res.append(el)
    return res

# Write a version of flatten that only flattens n levels of an array.
# E.g. If you have an array with 3 levels of nested arrays, and run
# my_flatten(1), you should return an array with 2 levels of nested
# arrays
#
# [1,[2,3], [4,[5]]].my_controlled_flatten(1) => [1,2,3,4,[5]]
def my_controlled_flatten(arr, n):
    if n < 1 : return arr
    res = []
    for el in arr:
        if isinstance(el, list):
            res += my_controlled_flatten(el, n-1)
        else: 
            res.append(el)
    return res


my_flatten([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
my_controlled_flatten([1, [2, 3], [4, [5]]], 1) == [1, 2, 3, 4, [5]]
