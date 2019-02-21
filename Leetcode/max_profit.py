# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(self, prices: 'List[int]') -> 'int':
        if len(prices) < 2:
            return 0
        profits = []
        for idx in range(1, len(prices)):
            profits.append(prices[idx] - prices[idx-1])

        def maxSubArray(arr):
            max_slice, curr_slice = 0, 0
            for el in arr:
                curr_slice = max(0, el + curr_slice)
                max_slice = max(curr_slice, max_slice)
            if max_slice == 0 and not 0 in arr:
                return max(arr)
            return max_slice

        max_profits = maxSubArray(profits)
        return max_profits if max_profits > 0 else 0

# Alternative (I prefer my way)
def maxProfit2(self, prices: 'List[int]') -> 'int':
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
