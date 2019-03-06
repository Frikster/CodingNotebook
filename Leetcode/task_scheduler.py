# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.


# Example:

# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


# Note:

# The number of tasks is in the range[1, 10000].
# The integer n is in the range[0, 100].


# For next time: The trick is that Python does not have a max heap queue, so we must make every number negative when we throw it into the heap.
# Create a priorityQueue of numbers where the numbers are the amount of a particular task. Pop greedily taking the biggest number (most duplicated task) first
# heap = []
# heapq.heappush(heap, el)
# heapq.heappop(heap)
# https://leetcode.com/problems/task-scheduler/discuss/104528/Python-solution-Max-Heap-Queue-easier-than-Awice's
# Or possibly this one: https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation

import heapq
from collections import Counter


class Solution:
        def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
            if n == 0:
                    return len(tasks)
            counter = Counter(tasks)
            heap = []
            for task in counter:
                heapq.heappush(heap, (-counter[task], task))

            res = 0
            uniq_tasks = []
            while heap:
                (num, task) = heapq.heappop(heap)
                res += 1
                # print((num, task))
                uniq_tasks.append((num, task))
                if len(uniq_tasks) == n+1 or (not heap and uniq_tasks):
                    for (num, task) in uniq_tasks:
                        num += 1
                        if num:
                            heapq.heappush(heap, (num, task))
                    if heap:
                        res += (n-len(uniq_tasks)+1)  # CPU idling
                        # print((n-len(uniq_tasks)+1) * '#')
                    uniq_tasks = []  # reset for the next n unique intervals
            # print(res)
            # print('---')
            return res
