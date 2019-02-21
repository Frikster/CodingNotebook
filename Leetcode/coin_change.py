# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

# Forget your method. This is the path to enlightenment:
# App Academy Burglar problem gives great insight into this
def coinChange(self, coins, amount):
            if not amount:
                    return 0

            dp = [float("inf") for i in range(amount+1)]

            for i in range(1, amount+1):
                if i in coins:
                    dp[i] = 1
                else:
                    new = [coin for coin in coins if coin < i]
                    if not new:
                        dp[i] = float("inf")
                    for j in new:
                        # check each of the coins you could use to get to this amount
                        dp[i] = min(dp[i], 1 + dp[i-j])
            if dp[-1] == float("inf"):
                return -1

            return dp[-1]
