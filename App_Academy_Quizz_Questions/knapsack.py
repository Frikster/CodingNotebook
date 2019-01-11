#   Knapsack Problem: write a function that takes in an array of weights, an array of values,
#   and a weight capacity and returns the maximum value possible given the weight constraint.
#   For example: if weights = [1, 2, 3], values = [10, 4, 8], and capacity = 3, your function 
#   should return 10 + 4 = 14, as the best possible set of items to include are items 0 and 1, 
#   whose values are 10 and 4 respectively. Duplicates are not allowed - - that is, you can 
#   only include a particular item once.

# Top-down
class Knapsack:
    def __init__(self):
        self.cache = {}

    def knapsack(self, weights_values, capacity, idx=0):
        if (capacity,idx) in self.cache: return self.cache[(capacity, idx)]
        if not weights_values or idx >= len(weights_values): return [[]]
        weight, value = weights_values[idx]
        branches = capacity // weight
        res = []
        while branches >= 0:
            if weight <= capacity:
                combos_without_item = self.knapsack(weights_values, capacity-branches*weight, idx+1)
                # TODO: fix this
                # print(idx)
                # print(combos_without_item)
                # max_combo = max(combos_without_item, key=lambda combo: sum([c[1] for c in combo]))
                # max_val = sum([c[1] for c in max_combo])
                # combos_without_item = filter(lambda combo: sum([c[1] for c in combo]) == max_val, combos_without_item)
                for combo in combos_without_item:
                    res.append([(weight, value)]*branches + combo)
            branches-=1
        self.cache[(capacity, idx)] = res
        return res

print(Knapsack().knapsack([(1,10),(2,4),(3,8)], 7))
