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

# Alternative solutions:
# https://leetcode.com/problems/task-scheduler/discuss/104528/Python-solution-Max-Heap-Queue-easier-than-Awice's
# https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation

# TODO: redo but use the sorting approach (look at the Java solution on Leetcode)

import heapq
from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        heap = []
        for task_count in Counter(tasks).values():
            heapq.heappush(heap, -task_count)

        res = 0
        while heap:
            len_heap = len(heap)
            task_arr = []
            for _ in range(min(len(heap), n+1)):
                res += 1
                task_count = heapq.heappop(heap)
                task_count += 1
                if task_count:
                    task_arr.append(task_count)
            for task_count in task_arr:
                heapq.heappush(heap, task_count)
            if heap and len_heap < n+1:
                res += n - len_heap + 1
        return res

    def old_leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
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
            # Note it is n+1 as we need n unique intervals BETWEEN a task and another that is identical to it (i.e. excluding the task itself)
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



