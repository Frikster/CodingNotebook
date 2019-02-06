from Data_Structures.min_max_stack_queue import MinMaxStackQueue

# Note, run with python3 -m App_Academy_Quizz_Questions.max_windowed_range
# O(n) optimized
def max_windowed_range(array, window_size):
    min_max_stack_queue = MinMaxStackQueue()
    max_range = float('-inf')

    for el in array:
        min_max_stack_queue.enqueue(el)
        if min_max_stack_queue.size() == window_size:
            if min_max_stack_queue.max() - min_max_stack_queue.min() > max_range:
                max_range = min_max_stack_queue.max() - min_max_stack_queue.min()
            min_max_stack_queue.dequeue()
    return max_range

print(max_windowed_range([1, 0, 2, 5, 4, 8], 2) == 4) # 4, 8
print(max_windowed_range([1, 0, 2, 5, 4, 8], 3) == 5) # 0, 2, 5
print(max_windowed_range([1, 0, 2, 5, 4, 8], 4) == 6) # 2, 5, 4, 8
print(max_windowed_range([1, 3, 2, 5, 4, 8], 5) == 6) # 3, 2, 5, 4, 8
