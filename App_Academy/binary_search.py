import pdb
# Write a monkey patch of binary search:
# E.g. [1, 2, 3, 4, 5, 7].my_bsearch(5) => 4
def my_bsearch(arr, target, start=0, end=None, key=None):
    end = end or len(arr)
    if end <= start: return None
    key = key or (lambda a,b: -1 if a<b else 1 if a>b else 0)
    mid = start + ((end - start) // 2)
    if len(arr) == 0: return None
    if arr[mid] == target: return mid
    if key(arr[mid], target) == -1:
        return my_bsearch(arr, target, mid+1, end, key)
        # sub_res = my_bsearch(arr[(mid+1):], target, key)
        #if sub_res == None : return None
        #return mid + sub_res + 1
    else:
        return my_bsearch(arr, target, start, mid, key)
        # return my_bsearch(arr[:mid], target, key)


print(my_bsearch([1, 2, 3, 4, 5, 7], 5))
print(my_bsearch([1, 2, 3, 4, 5, 7], 2))
print(my_bsearch([1, 2, 3, 4, 5, 7], 8))
print(my_bsearch([1, 2, 3, 4, 5, 7, 8], 4))
print(my_bsearch([0], 0))
print(my_bsearch([0,1,2,3], 0))

 

