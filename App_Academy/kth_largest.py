# Write a function that takes in a binary search tree (as a tree_node) and an integer k,
# and returns the kth largest element in the BST.

from Data_Structures.binary_search_tree import BinarySearchTree, BSTNode

def kth_largest(tree_node, k):
  kth_node = { 'count': 0, 'correct_node': None }
  return reverse_inorder(tree_node, kth_node, k)['correct_node']

def reverse_inorder(tree_node, kth_node, k):
    if tree_node and kth_node['count'] < k:
        kth_node = reverse_inorder(tree_node.right, kth_node, k)
        if kth_node['count'] < k:
           kth_node['count'] += 1
           kth_node['correct_node'] = tree_node 

        if kth_node['count'] < k:
            kth_node = reverse_inorder(tree_node.left, kth_node, k)

    return kth_node


bst = BinarySearchTree()
bst.root = BSTNode(5)
for el in [3, 7, 1, 4, 9, 0, 2, 1.5, 10]:
  bst.insert(el, bst.root)

print(kth_largest(bst.root, 7) is bst.root.left.left.right)

bst = BinarySearchTree()
bst.root = BSTNode(14)
for el in [4, 16, 1, 10, 20]:
  bst.insert(el, bst.root)

print(kth_largest(bst.root, 2) is bst.root.right)
