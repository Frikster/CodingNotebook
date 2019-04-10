# Dont bother solving this anymore. Rather grok coin_change.py

# make better change problem from class
# make_better_change(24, [10,7,1]) should return [10,7,7]
# make change with the fewest number of coins

# write make_better_change(value, coins) that returns an array of arrays which are all the possible
# combinations of coins that sum to value. Never rule out denominations that we've already used.
# This allows each coin to be available each time we get a new remainder.
# By iterating over the denominations and continuing to search for the best change, we assure that we test
# for 'non-greedy' uses of each denomination

# e.g. make_better_change(24, [1,5,10,25]) will return 
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5], 
# [1, 1, 1, 1, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 10], 
# [1, 1, 1, 1, 5, 5, 10], [1, 1, 1, 1, 10, 10]]

import pdb
# : this solution doesn't work for cases like 6249, [186, 419, 83, 408]

# Top-down: simply modify to return the array with the fewest coins if that is what you desire
class MakeChange:
    def __init__(self):
        self.cache = {}

    def make_better_change_better(self, value, coins, idx=0):
        if (value, idx) in self.cache: return self.cache[(value, idx)]
        if value <= 0 or idx >= len(coins): return []
        coin = coins[idx]
        branches = value // coin  # max number of times we can pick this coin.
        res = [branches*[coin]] if branches * coin == value else []
        while branches >= 0:
            combos_without_coins = self.make_better_change_better(value-(branches*coin), coins, idx+1)
            for combo in combos_without_coins:
                res.append(branches*[coin] + combo)
            branches -= 1
        self.cache[(value, idx)] = res
        return res

# Bottom-up 
def make_better_change_better(value, coins):
    if value == 0: return []
    coins.sort() # o/w you will build from the largest and might get combos that don't sum to value
    cache = make_better_change_cache_builder(value, coins, 0)
    return cache[(value, len(coins)-1)]

def make_better_change_cache_builder(value, coins, idx=0):
    cache = {}
    for idx in range(len(coins)):
        for value in range(value+1):
            coin = coins[idx]
            branches = value // coin 
            if value <= 0:
                cache[(value, idx)] = []
            elif idx == 0:
                cache[(value, idx)] = [[coin]*branches]
            elif coin > value:
                cache[(value, idx)] = cache[(value, idx - 1)]
            else:
                cache[(value, idx)] = cache[(value, idx - 1)]
                for combo in cache[(value - coin, idx)]:
                    cache[(value, idx)].append(combo + [coin])  
                # Also consider the case where no prior coins are used   
                # You have to check if this is already in the cache because for instance
                # It might have been added when the value was the same but for a prior idx
                # when the coin at the prior idx couldn't be used 
                if branches * coin == value and not [coin]*branches in cache[(value, idx)]:
                    cache[(value, idx)].append([coin]*branches)
    return cache

# less optimized than the one above. Computes all possible subsets but only returns one valid coin combo for each due to the use of sets
def make_better_change(value, coins, memo={}):
    if value <= 0: return [tuple()]
    coins = set(filter(lambda c: c <= value, coins))
    res = set() 
    for idx, coin in enumerate(coins):
        if coin <= value:
            if (value - coin, idx) in memo: 
                combos_without_coin = memo[(value - coin, idx)]
            else:
                combos_without_coin = make_better_change(value - coin, coins, memo)
                combos_without_coin = {tuple(sorted(combo)) for combo in combos_without_coin}
                memo[(value - coin, idx)] = combos_without_coin
            for combo in combos_without_coin:
                res.add(tuple(sorted((coin,) + combo)))
    return res

# Only returns number (can be further optimized with memo)
def coin_representations(n, denom_index=0, denoms=(1, 5, 10, 25)):
    if n == 0:  # base case: we've found a combination of coins that divides evenly into amount of change
        return 1
    if denom_index >= len(denoms):  # check for case where we don't ever pick any coins
        return 0
    # current coin we pick. we only pick one type of coin at each recursion level
    coin = denoms[denom_index]
    branches = n // coin  # max number of times we can pick this coin.
    representations = 0
    while branches >= 0:  # subtract coin value from n for each recursive call. there is one case where we pick 0 coins!
        representations += coin_representations(
            n - branches*coin, denom_index + 1, denoms)
        branches -= 1
    return representations

# Least optimized. Returns all possible subsets
def make_change(value, coins):
    coins_to_check = list(filter(lambda coin: coin <= value, coins))
    if not coins_to_check: return []

    solutions = []

    coins_to_check.sort(reverse=True)
    for coin in coins_to_check:
        remainder = value - coin

        if remainder > 0:
            # remainder_solution = make_change(remainder, coins_to_check) # use commented out to only return one with least amount of coins
            # if remainder_solution:
            #     solutions.append([coin] + remainder_solution) 

            remainder_solutions = make_change(remainder, coins_to_check)
            if remainder_solutions:
                for remainder_solution in remainder_solutions:
                    solutions.append([coin] + remainder_solution)

        else:
            solutions.append([coin])
    
    return sorted(solutions, key=lambda arr: len(arr))
    # return sorted(solutions, key=lambda arr: len(arr))[0]


# Iterative works:
# print(make_better_change_better(24, [1, 5, 10, 25]))
# print(make_better_change_better(24, [10, 7, 1]))
# print(make_better_change_better(25, [10, 7, 1]))
# print(make_better_change_better(25, [10, 8, 7, 1]))
# : seems incorrect for this case (should return 20 combos)
print(len(make_better_change_better(6249, [186, 419, 83, 408])))


# Recursive works:
# print(MakeChange().make_better_change_better(24, [1, 5, 10, 25]))
# print(MakeChange().make_better_change_better(24, [1, 7, 10]))
# print(MakeChange().make_better_change_better(25, [10, 7, 1]))
# print(MakeChange().make_better_change_better(25, [10, 8, 7, 1]))
# : seems incorrect for this case (should return 20 combos)
print(len(MakeChange().make_better_change_better(6249, [186, 419, 83, 408])))


# print(len(make_better_change(24, [1, 5, 10, 25])))
# print((make_better_change(24, [1, 5, 10, 25])))
# print(coin_representations(24))

# print(make_better_change(24, [10, 7, 1]))
# print(len(make_better_change(24, [10, 7, 1])))
# print(make_better_change(24, [10, 7, 1]) == [10, 7, 7])
