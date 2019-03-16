# TODO: Similar questions:
# 62. Unique Paths
# 70. Climbing Stairs
# 509. Fibonacci Number
# Practice them in a row for better understanding 😉

# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Combining code from previous two approaches:
class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        for uncrackable in range(30, 100, 10):
            if str(uncrackable) in s:
                return 0
        if s == '' or '00' in s or s[0] == '0':
            return 0
        if len(s) == 1: return 1
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 2 if s[0:2] <= '26' and s[1] != '0' else 1
        for idx in range(2, len(dp)):
            if '09' < s[idx-1:idx+1] <= '26':
                if s[idx] != '0':
                    dp[idx] = dp[idx-1] + dp[idx-2]
                else:
                    dp[idx] = dp[idx-2]
            else:
                dp[idx] = dp[idx-1]
        return dp[len(s)-1]

class Solution2:
    def numDecodings(self, s: 'str') -> 'int':
        if s == '' or s[0] == '0': return 0
        if len(s) == 1: return 1
        if s[1] == '0' and s[0] > '2': return 0
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 2 if s[0:2] <= '26' and s[1] != '0' else 1
        for idx in range(2, len(dp)):
            if s[idx] == '0':
                if '0' < s[idx-1] <= '2':
                    if '09' < s[idx-2:idx] <= '26':
                        dp[idx] = dp[idx-2]
                    else:
                        dp[idx] = dp[idx-1]
                else:
                    return 0
            elif '09' < s[idx-1:idx+1] <= '26':
                dp[idx] = dp[idx-1] + dp[idx-2]
            else:
                dp[idx] = dp[idx-1]
        return dp[len(s)-1]


# Old Solution (also works and is O(n)):
class Solution3:
    def __init__(self):
        # cache substring up to and including char ending at index (key) to number of possible decode interpretations (val) of substring
        self.cache = {0: 1}

    def numDecodings(self, s: 'str') -> 'int':
        for uncrackable in range(30, 100, 10):
            if str(uncrackable) in s:
                return 0
        if '00' in s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # if s[1] is zero then we can only consider the two digits as a single entity
        # if the first two digits are less than 26 then we can only consider each digit alone which is a single possible decoding
        if int(s[0:2]) <= 26 and s[1] != '0':
            self.cache[1] = 2
        else:
            self.cache[1] = 1
        self.numDecoding_cache_bulder(s)
        return self.cache[len(s)-1]

    def numDecoding_cache_bulder(self, s):
        # Bottom-up DP to build the cache:
        for idx in range(2, len(s)):
            # If either s[idx-1] or s[idx] are '0' adding the next char wont increase the number of possible decodings
            if int(s[idx-1:idx+1]) <= 26 and s[idx-1] != '0' and s[idx] != '0':
                self.cache[idx] = self.cache[idx-2] + self.cache[idx-1]
            elif int(s[idx-1:idx+1]) <= 26 and s[idx-1] != '0' and s[idx] == '0':
                self.cache[idx] = self.cache[idx-2]
            else:
                self.cache[idx] = self.cache[idx-1]

