# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for idx in range(len(nums)):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                candidate = nums[idx] + nums[left] + nums[right]
                if candidate == 0:
                    res.add((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif candidate < 0:
                    left += 1
                else:
                    right -= 1
        return list(res)
