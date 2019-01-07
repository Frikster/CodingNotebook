# Write a monkey patch of binary search:
# E.g. [1, 2, 3, 4, 5, 7].my_bsearch(5) => 4
def my_bsearch(arr, target, key=None):
    key = key or (lambda a,b: -1 if a<b else 1 if a>b else 0)
    mid = len(arr)//2
    if len(arr) == 0: return None
    if arr[mid] == target: return mid
    if key(arr[mid], target) == -1:
        sub_res = my_bsearch(arr[(mid+1):], target, key)
        if sub_res == None : return None
        return mid + sub_res + 1
    else:
        return my_bsearch(arr[:mid], target, key)
    

