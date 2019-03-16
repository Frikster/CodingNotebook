# Given an integer array nums, find the sum of the elements between indices i and j(i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element at index i to val.

# Example:

# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:

# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

# tips: yes, build a segment tree so you will need to manually make a node class
# i.e. do it as below but make your segment tree from scratch
# For the update function, change the leaf node and then propogate that change up
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees


class Node:
    def __init__(self, start, end, val=0):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.val = val


class SegmentSumTree:
    def __init__(self, nums):
        def build_tree(nums, left, right):
            if left > right:
                return None
            if left == right:
                return Node(left, right, nums[left])
            mid = (left + right) // 2
            root = Node(left, right)
            root.left = build_tree(nums, left, mid)
            root.right = build_tree(nums, mid+1, right)
            root.val = root.left.val + root.right.val
            return root
        self.root = build_tree(nums, 0, len(nums)-1)

    def sumRange(self, start, end, root):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.val
        mid = (root.start + root.end) // 2
        if end <= mid:
            # We know from build_tree mid is on left
            return self.sumRange(start, end, root.left)
        if start > mid:
            return self.sumRange(start, end, root.right)
        # We know from build_tree that mid is on left
        return self.sumRange(start, mid, root.left) + self.sumRange(mid+1, end, root.right)

    def update(self, idx, val, root):
        if root.start == idx and root.end == idx:
            root.val = val
            return val
        mid = (root.start + root.end) // 2
        if idx <= mid:
            # We know from build_tree that mid is within left side
            self.update(idx, val, root.left)
        else:
            self.update(idx, val, root.right)
        root.val = root.left.val + root.right.val
        return root.val


class NumArray:
    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        self.seg_tree = SegmentSumTree(nums)

    def update(self, i: 'int', val: 'int') -> 'None':
        self.seg_tree.update(i, val, self.seg_tree.root)

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i < 0:
            i = 0
        if j >= len(self.nums):
            j = len(self.nums) - 1
        return self.seg_tree.sumRange(i, j, self.seg_tree.root)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
