def bubble_sort(array, key=None):
    key = key or (lambda a,b: -1 if a < b else 1 if a > b else 0)
    for idx in range(len(array)):
        for jdx in range(idx+1,len(array)):
            if key(array[jdx], array[idx]) == -1:
                array[jdx], array[idx] = array[idx], array[jdx]
    return array

def bubble_sort_dup(array, key=None):
    return bubble_sort(array.copy(), key)


a = [1, 3, 7, 2, 7, 234, 2, 2, 1]
bubble_sort(a) 
# a = [1, 1, 2, 2, 2, 3, 7, 7, 234]
a = [1, 3, 7, 2, 7, 234, 2, 2, 1]
bubble_sort_dup([1,3,7,2,7,234,2,2,1])
# a = [1, 3, 7, 2, 7, 234, 2, 2, 1]
