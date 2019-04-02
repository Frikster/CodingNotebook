# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TODO: redo. Hint: do it recusrively when whiteboarding.
# Try doing it iteratively. You actually had the right idea:

# 1. Keep pushing the nodes from the preorder into a stack (and keep making the tree by adding nodes to the left of the previous node) until the top of the stack matches the inorder.
# 2. At this point, pop the top of the stack until the top does not equal inorder (keep a flag to note that you have made a pop).
# 3. Repeat 1 and 2 until preorder is empty. The key point is that whenever the flag is set, insert a node to the right and reset the flag.


class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if inorder:
            # suboptimal, also your index version without pop does not work
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

        # return self.buildTree_helper(preorder, 0, inorder)

    def buildTree_helper(self, preorder, preorder_idx, inorder):
        if preorder_idx == len(preorder) or not inorder:
            return None
        ind = inorder.index(preorder[preorder_idx])
        root = TreeNode(inorder[ind])
        root.left = self.buildTree_helper(
            preorder, preorder_idx+1, inorder[:ind])
        root.right = self.buildTree_helper(
            preorder, preorder_idx+2, inorder[ind+1:])
        return root
