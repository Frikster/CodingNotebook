#   Knapsack Problem: write a function that takes in an array of weights, an array of values,
#   and a weight capacity and returns the maximum value possible given the weight constraint.
#   For example: if weights = [1, 2, 3], values = [10, 4, 8], and capacity = 3, your function 
#   should return 10 + 4 = 14, as the best possible set of items to include are items 0 and 1, 
#   whose values are 10 and 4 respectively. Duplicates are not allowed - - that is, you can 
#   only include a particular item once.

import pdb
# from functools import lru_cache

class Knapsack:
    def __init__(self):
        self.cache = {}

    def knapsack(self, weights_values, capacity, items_left=None):
        if items_left is None: items_left = len(weights_values)
        if (capacity, items_left) in self.cache: return self.cache[(capacity, items_left)]
        if capacity <= 0 or items_left <= 0: return []
        res = []
        weight, value = weights_values[items_left - 1]
        if weight > capacity:
            return self.knapsack(weights_values, capacity, items_left-1)
        else:
            with_item = self.knapsack(weights_values, capacity-weight, items_left-1)
            without_item = self.knapsack(weights_values, capacity, items_left-1)
            # pdb.set_trace()
            with_item_val = weight + sum([item[1] for item in with_item]) if with_item else 0
            without_item_val = sum([item[1] for item in without_item]) if without_item else 0
            if with_item_val >= without_item_val:
                res += [(weight, value)] + with_item
            else: 
                res += without_item




            #     max_combo = max(combos_without_item, key=lambda combo: sum(
            #         [c[1] for c in combo]))
            #     max_val = sum([c[1] for c in max_combo])
            #     combos_without_item = filter(lambda combo: sum(
            #         [c[1] for c in combo]) == max_val, combos_without_item)
            # for combo in combos_without_item:
            #     res.append([(weight, value)] + combo)
        self.cache[(capacity, items_left)] = res
        return res


# https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution
    # def knapsack_best(items, maxweight):
    #     """Solve the knapsack problem by finding the most valuable subsequence
    #     of items that weighs no more than maxweight.

    #     items must be a sequence of pairs (value, weight), where value is a
    #     number and weight is a non-negative integer.

    #     maxweight is a non-negative integer.

    #     Return a pair whose first element is the sum of values in the most
    #     valuable subsequence, and whose second element is the subsequence.

    #     >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    #     >>> knapsack(items, 15)
    #     (11, [(2, 1), (6, 4), (1, 1), (2, 2)])

    #     """
    #     @lru_cache(maxsize=None)
    #     def bestvalue(i, j):
    #         # Return the value of the most valuable subsequence of the first
    #         # i elements in items whose weights sum to no more than j.
    #         if j < 0:
    #             return float('-inf')
    #         if i == 0:
    #             return 0
    #         value, weight = items[i - 1]
    #         return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    #     j = maxweight
    #     result = []
    #     for i in reversed(range(len(items))):
    #         if bestvalue(i + 1, j) != bestvalue(i, j):
    #             result.append(items[i])
    #             j -= items[i][1]
    #     result.reverse()
    #     return bestvalue(len(items), maxweight), result




# Top-down... this "solution" forgot that **duplicates are not allowed!!**
# class Knapsack:
#     def __init__(self):
#         self.cache = {}

#     def knapsack(self, weights_values, capacity, idx=0):
#         if (capacity,idx) in self.cache: return self.cache[(capacity, idx)]
#         if capacity <= 0 or idx >= len(weights_values): return [[]]
#         weight, value = weights_values[idx]
#         branches = capacity // weight # max number of times this weight can be used
#         res = []
#         while branches >= 0:
#             if weight <= capacity:
#                 combos_without_item = self.knapsack(weights_values, capacity-branches*weight, idx+1)
#                 # TODO: fix this
#                 if combos_without_item:
#                     max_combo = max(combos_without_item, key=lambda combo: sum([c[1] for c in combo]))
#                     max_val = sum([c[1] for c in max_combo])
#                     combos_without_item = filter(lambda combo: sum([c[1] for c in combo]) == max_val, combos_without_item)
#                 for combo in combos_without_item:
#                     res.append([(weight, value)]*branches + combo)
#             branches-=1
#         self.cache[(capacity, idx)] = res
#         return res

print(Knapsack().knapsack([(1,10),(2,4),(3,10),(4,4)], 5))
print(Knapsack().knapsack([(2, 10), (3, 4), (3, 10), (4, 4)], 7))
