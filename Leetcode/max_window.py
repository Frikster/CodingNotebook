# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# Note that there may be duplicates in T so this is different from Pramp one. i.e. S = "AA", T = "AA". Output should be: "AA"

from collections import Counter

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        counter_hash = Counter(t)
        # for char in t:
        #     if char in counter_hash:
        #         counter_hash[char] += 1
        #     else:
        #         counter_hash[char] = 1
        left, right = 0, 0
        stored_left, stored_right = 0, len(s)
        uniq_counter = 0

        while left < len(s):
            if s[left] in counter_hash:
                if counter_hash[s[left]] == 1:
                    uniq_counter += 1
                counter_hash[s[left]] -= 1
            left += 1
            while uniq_counter >= len(set(t)):
                if left - right < stored_left - stored_right:
                    stored_left = left
                    stored_right = right
                if s[right] in counter_hash:
                    if counter_hash[s[right]] == 0:
                        uniq_counter -= 1
                    counter_hash[s[right]] += 1
                right += 1

        if stored_left == float('inf') or stored_right == float('-inf'):
            return ""
        return s[stored_right:stored_left]

# Alternative (waaay faster)
    def minWindow2(self, s: 'str', t: 'str') -> 'str':
        count = 0
        m = {}
        for c in t:
            if c not in m:
                count += 1
                m[c] = 0
            m[c] += 1

        start = 0
        size = len(s)
        ansLen = size + 1
        ans = ''
        for end in range(size):
            if s[end] not in m:
                continue
            m[s[end]] -= 1
            if m[s[end]] == 0:
                count -= 1

            while count == 0:
                if end - start + 1 < ansLen:
                    ansLen = end-start+1
                    ans = s[start:end+1]
                startC = s[start]
                start += 1
                if startC not in m:
                    continue
                m[startC] += 1
                if m[startC] == 1:
                    count += 1
                    break

        if ansLen == size + 1:
            return ''
        return ans
