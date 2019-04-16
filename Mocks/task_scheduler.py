# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2. n
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


# A: 1
# B: 2
# n = 2
# res 4
# A -> B -> idle -> A ->


# A: 3
# b: 3
# n: 10
# A -> B -> id -> id -> id -> id


# [(3, 'A'), (3, 'B')]

# n - len(heap) + 1



# while heap and task_not_ok:
#   task_num, task = heap.pop


#   if interval_ok[task]:
#     interval_ok[task] = False
#     task_num -= 1
#     res += 1
#     heap.push((task_num, task))

# ABCC n=3


# Counter(tasks)

import heapq
from collections import Counter
def task_scheduler(tasks, n):
    heap = []
    for task_count in Counter(tasks).values():
        heapq.heappush(heap, -task_count)

    res = 0
    while heap:
        len_heap = len(heap)
        task_arr = []
        for _ in range(min(len(heap),n+1)):
            res+=1
            task_count = heapq.heappop(heap)
            task_count+=1
            if task_count:
                task_arr.append(task_count)
        for task_count in task_arr:
            heapq.heappush(heap, task_count)
        if heap and len_heap < n+1:
            res += n - len_heap + 1
    return res


print(task_scheduler([c for c in 'CCCCAABB'], 2))
print(task_scheduler(["A", "A", "A", "B", "B", "B"], 2))
print(task_scheduler([c for c in 'AABB'], 10))
# CCCCAABB 
# len_heap 1
# heap[]
# task_arr []
# res 10
# task_count 0

# Huzzah!

