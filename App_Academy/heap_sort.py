# heap_sort! method. This method should not create a new array. 
# It should start by heapifying the array in place. Once the items have been heapified, 
# use the ::heapify_down method to extract items from the heap one by one, moving them past a partition in the array. 
# Voila! Your array has been heap sorted.

# What is the time complexity of HeapSort? O(nlogn) What is the space complexity? O(1) since in-place

from Data_Structures.heap import BinaryMinHeap

def heap_sort_in_place(arr, key = None):
    key = key or (lambda a,b: -1 if b < a else 1 if b > a else 0)
    # NB: Note that key is switched otherwise this will come out in reverse!
    # Because using MinHeap

    for idx in range(len(arr)):
        BinaryMinHeap.heapify_up(arr, idx, idx+1, key)
    # At this point our arr has been transformed into a reversed MinHeap in place
    for idx in range(len(arr)-1,0,-1):
        arr[0], arr[idx] = arr[idx], arr[0]
        BinaryMinHeap.heapify_down(arr, 0, idx, key)
    # We could have also just have used the MinHeap with a normal key and then reversed the final result
    return arr


def heap_sort(arr, key=None):
    heap = BinaryMinHeap()
    for el in arr:
        heap.push(el)
    res = []
    for _ in range(len(arr)):
        res.append(heap.extract())
    return res


print(heap_sort_in_place([4, 2, 1, 3, 5, 7, 8, 9]))
print(heap_sort_in_place([5, 4, 3, 2, 1]))
print(heap_sort_in_place([1, 2, 3, 4, 5]))
# [1, 2, 3, 4, 5, 7, 8, 9]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

print(heap_sort([4, 2, 1, 3, 5, 7, 8, 9]))
print(heap_sort([5, 4, 3, 2, 1]))
print(heap_sort([1, 2, 3, 4, 5]))
# [1, 2, 3, 4, 5, 7, 8, 9]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
