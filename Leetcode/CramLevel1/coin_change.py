# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

# App Academy Burglar problem gives great insight into this
def coinChange(self, coins, amount):
            if not amount:
                    return 0

            dp = [float("inf")] * (amount+1)

            for val in range(1, amount+1):
                final_coins = [coin for coin in coins if coin <= val]
                # check each of the coins you could use to get to this amount
                for final_coin in final_coins:
                    if final_coin == val:
                        dp[val] = 1
                        break
                    else:
                        dp[val] = min(dp[val], dp[val-final_coin]+1)
            if dp[-1] == float('inf'):
                    return -1
            return dp[-1]

# All sets
def coin_change_sets(amount, coins):
            if not amount:
                    return []

            dp = [float("inf")] * (amount+1)
            dp_set = [[] for _ in range(amount+1)]
            # NB: below WILL NOT work because then all nested lists have SAME REFERENCE, add to one you change them all.
            # dp_set = [[]] * (amount+1)

            for val in range(1, amount+1):
                final_coins = [coin for coin in coins if coin <= val]
                # check each of the coins you could use to get to this amount
                for final_coin in final_coins:
                    if final_coin == val:
                        dp[val] = 1
                        dp_set[val] = [[val]]
                        break
                    else:
                        if min(dp[val], dp[val-final_coin]+1) == dp[val-final_coin]+1:
                            # add current coin
                            coin_added_sets = [d + [final_coin] for d in dp_set[val-final_coin]]
                            # print('val: ' + str(val))
                            # print('coin_added_sets: ' + str(coin_added_sets))
                            # print('dp_set[val]: ' + str(dp_set[val]))
                            # print('both: ' + str(dp_set[val] + coin_added_sets))
                            dp_set[val] += coin_added_sets 
                            # print(dp_set)
                        dp[val] = min(dp[val], dp[val-final_coin]+1)
                    # print(dp_set)

            if dp[-1] == float('inf'):
                    return -1
            return dp_set[-1]

if __name__ == "__main__":
    # print(coin_change_sets(24, [1, 5, 10, 25]))
    # print(coin_change_sets(24, [10, 7, 1]))
    # print(coin_change_sets(25, [10, 7, 1]))
    # print(coin_change_sets(25, [10, 8, 7, 1]))
    # print(coin_change_sets(6249, [186, 419, 83, 408]))
    print(coin_change_sets(10, [9, 4, 2, 1, 6]))
    # print(coin_change_sets(11, [9, 4, 2, 7]))
