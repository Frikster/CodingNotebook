# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2, 3, 1, 1, 4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        pos = 0
        res = 0
        while pos != len(nums)-1:
            jumps = nums[pos]
            max_range = 0
            next_pos = 0
            if pos+jumps+1 >= len(nums):
                return res+1  # we are at a position where we can jump to the end. Do so immediately!
            for idx in range(pos+1, pos+jumps+1):
                if idx + nums[idx] > max_range:
                    max_range = idx + nums[idx]
                    next_pos = idx
            pos = next_pos
            res += 1
        return res
