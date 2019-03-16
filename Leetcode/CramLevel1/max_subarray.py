# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_slice, max_slice = 0, 0
        for el in nums:
            curr_slice = max(0, curr_slice + el) # Extend curr_slice or start anew
            max_slice = max(max_slice, curr_slice)
        # If we cannot find a max slice greater than zero we only have negative values in nums
        if max_slice == 0 and not 0 in nums:
            return max(nums)
        return max_slice
