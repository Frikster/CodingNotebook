# https://leetcode.com/problems/range-sum-query-immutable/
# Given an integer array nums, find the sum of the elements between indices i and j(i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.


class NumArray:
    def __init__(self, nums: 'List[int]'):
        self.store = nums
        self.cache = {} # Interval sums all starting from 0
        for idx in range(len(nums)):
            if idx-1 in self.cache:
                self.cache[idx] = self.cache[idx-1] + nums[idx]
            else:
                self.cache[idx] = nums[idx]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.cache[j] - self.cache[i] + self.store[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
