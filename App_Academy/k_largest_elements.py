from Data_Structures.heap import BinaryMinHeap

# Given an array and an integer k, return the k-largest elements in O(nlogk) time.
def k_largest_elements(array, k):
    heap = BinaryMinHeap()
    for el in array:
        heap.push(el)  # building a heap is O(n) (tighter bound than O(nlogn))
        if len(heap) > k: 
            heap.extract() # O(logk), so loop is O(nlogk)
    return heap.store

print(k_largest_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(k_largest_elements([0, 10, 2, 13, 14, 5, 26, 7, 8, 9], 5))
# [7, 8, 9]
# [9, 10, 13, 14, 26]
