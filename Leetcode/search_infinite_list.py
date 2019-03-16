def bsearch(arr, target, start=0, end=None, key=None):
    end = end or len(arr)
    if end <= start:
        return -1
    mid = (start + end) // 2
    key = key or (lambda a,b: -1 if a<b else 1 if a>b else 0)
    if arr[mid] == target:
        return mid
    if key(target, arr[mid]) == -1:
        return bsearch(arr, target, 0, mid, key)
    else:
        return bsearch(arr, target, mid+1, end, key)

# function takes an infinite size array and a key to be
# searched and returns its position if found else -1.
# We don't know size of a[] and we can assume size to be
# infinite in this function.
# NOTE THAT THIS FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE
# THEREFORE, THERE IS NO INDEX OUT OF BOUND CHECKING
def find_pos(arr, key):
    if arr[0] == key:
        return 0
    end_idx = 1
    while arr[end_idx] < key: # O(logn)
        end_idx*=2
    return bsearch(arr, key, 0, end_idx) # O(logn)


