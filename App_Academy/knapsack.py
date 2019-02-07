#   Knapsack Problem: write a function that takes in an array of weight-value tuples,
#   and a weight capacity and returns the an array of weight-value tuples that maximizes
#   their total value given the weight capacity constraint.
#   For example: if weight-value = [(1,10),(2,4),(3,8)] and capacity = 3, your function
#   should return [(1,10),(2,4)] as the best possible set of items
#   **Duplicates are not allowed** - - that is, you can only include a particular item once.

# Top-down - gives the weight-value pairs chosen. Simply iterate through returned values to get total value
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
            with_item = [(weight, value)] + self.knapsack(weights_values, capacity-weight, items_left-1)
            without_item = self.knapsack(weights_values, capacity, items_left-1)
            with_item_val = value + sum([item[1] for item in with_item]) if with_item else 0
            without_item_val = sum([item[1] for item in without_item]) if without_item else 0
            if with_item_val >= without_item_val:
                res += with_item
            else: 
                res += without_item

        self.cache[(capacity, items_left)] = res
        return res

# Bottom-up
def knapsack(weight_values, capacity):
    if capacity == 0 or len(weight_values) == 0 : return []
    solution_table = knapsack_table(weight_values, capacity)
    return solution_table[(capacity, len(weight_values)-1)]

def knapsack_table(weight_values, capacity):
    solution_table = {}
    # Build solutions for knapsacks of increasing capacity
    for cap in range(capacity+1):
        for item in range(len(weight_values)):
            weight, value = weight_values[item]
            if cap <= 0:
                solution_table[(cap, item)] = []
            elif item == 0:
                # for the first item in our list, you must check for capacity
                # if there is, then you enter its value in the first slot, otherwise 0
                solution_table[(cap, item)] = [(weight, value)] if weight <= cap else []
            else:
                # the first option is the entry from considering the previous item at this capacity
                option1 = solution_table[(cap, item - 1)]
                option1_val = sum([wv[1] for wv in option1]) if option1 else 0
                # the second option (assuming enough capacity) is the entry from a smaller bag
                # (with enough room for this item) plus this item's value
                # other_items = solution_table[(cap - weight,item - 1)] if cap - weight >= 0 else []
                option2 = [(weight, value)] + solution_table[(cap - weight, item - 1)] if cap - weight >= 0 else []
                option2_val = value + sum([wv[1] for wv in option2]) if option2 else 0

                # the actual entry for this item is the optimum of the two choices
                optimum = option2 if option2_val >= option1_val else option1
                solution_table[(cap, item)] = optimum

    return solution_table


print(Knapsack().knapsack([(1,10),(2,4),(3,10),(4,4)], 5))
print(Knapsack().knapsack([(4, 4), (3, 10), (2, 4), (1, 10)], 5)) 
print(Knapsack().knapsack([(2, 10), (3, 4), (3, 10), (4, 4)], 7))
print(Knapsack().knapsack([(4, 4), (3, 10), (3, 4), (2, 10)], 7))

print(knapsack([(1, 10), (2, 4), (3, 10), (4, 4)], 5))
print(knapsack([(4, 4), (3, 10), (2, 4), (1, 10)], 5))
print(knapsack([(2, 10), (3, 4), (3, 10), (4, 4)], 7))
print(knapsack([(4, 4), (3, 10), (3, 4), (2, 10)], 7))
