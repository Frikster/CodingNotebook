import unittest
import pdb
from Data_Structures.binary_search_tree import BinarySearchTree, BSTNode

class RankFromStream:
    def __init__(self):
        self.bst_store = BinarySearchTree() 

    # O(n) worst case; O(logn) avg case.
    def track(self, x):
        if self.bst_store.root is None:
            self.bst_store.root = BSTNode(x)
        else:
            self.bst_store.insert(x, self.bst_store.root)

    # O(n)
    def get_rank(self, num):
        in_order = self.bst_store.in_order_traversal(self.bst_store.root)
        return len([x for x in in_order if x < num])

        # All wrong! Because num isn't necesarrily even in the BST!
        # modified search
        # def count_less_than(value, tree_node):
        #     if tree_node is None:
        #         return 0
        #     if tree_node.value == value:
        #         return 1 + count_less_than(value, tree_node.left)
        #     if tree_node.value > value:         
        #         return count_less_than(value, tree_node.left)
        #     else:
        #         return 1 + count_less_than(value, tree_node.right)   
        # return count_less_than(num, self.bst_store.root)


class Test(unittest.TestCase):
  def test_rank_tree(self):
    rt = RankFromStream()
    self.assertEqual(rt.get_rank(20), 0)
    rt.track(11)
    self.assertEqual(rt.get_rank(20), 1)
    self.assertEqual(rt.get_rank(10), 0)
    rt.track(30)
    rt.track(7)
    rt.track(7)
    rt.track(10)
    rt.track(15)
    rt.track(7)
    rt.track(3)
    rt.track(22)
    self.assertEqual(rt.get_rank(20), 7)
    self.assertEqual(rt.get_rank(7), 1)
    self.assertEqual(rt.get_rank(8), 4)
    self.assertEqual(rt.get_rank(14), 6)


if __name__ == "__main__":
  unittest.main()
