 # TODO: test
import pdb
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Note that root has to be set manually before insert works
    def insert(self, value, tree_node):
        if tree_node is None: return BSTNode(value)
        if value <= tree_node.value:
            tree_node.left = self.insert(value, tree_node.left)
        else:
            tree_node.right = self.insert(value, tree_node.right)
        return tree_node

    # You cannot set tree_node to default to self.root because then if it doesn't find the value
    # on the next recursive level tree_node is none and then set to self.root -> infinite loop
    def find(self, value, tree_node):
        if tree_node is None: return None 
        if tree_node.value == value: return tree_node       
        if value < tree_node.value:
            return self.find(value, tree_node.left)
        else:
            return self.find(value, tree_node.right)

    def maximum(self, tree_node):
        return self.maximum(tree_node.right) if tree_node.right else tree_node

    def minimum(self, tree_node):
        return self.minimum(tree_node.left) if tree_node.left else tree_node

    def depth(self, tree_node):
        if tree_node is None: return -1
        left_depth = self.depth(tree_node.left)
        right_depth = self.depth(tree_node.right)
        return left_depth + 1 if left_depth > right_depth else right_depth + 1

    def is_balanced(self, tree_node):
        if tree_node is None: return True
        left_depth = self.depth(tree_node.left)
        right_depth = self.depth(tree_node.right)
        return abs(left_depth - right_depth) <= 1 and \
         self.is_balanced(tree_node.left) and self.is_balanced(tree_node.right)

    def in_order_traversal(self, tree_node, arr=None):
        if arr is None: arr = []
        if tree_node is None: return arr
        if tree_node.left:
            self.in_order_traversal(tree_node.left, arr)
        arr.append(tree_node.value)
        if tree_node.right:
            self.in_order_traversal(tree_node.right, arr)
        return arr 

    def delete(self, value, tree_node):
        if value == tree_node.value:
            tree_node = self.__remove_node(tree_node)
        elif value <= tree_node.value:
            tree_node.left = self.delete(value, tree_node.left)
        else:
            tree_node.right = self.delete(value, tree_node.right)
        return tree_node

    def __remove_node(self, node):
        if node.left is None and node.right is None:
            node = None 
        elif node.left is None and node.right:
            node = node.right
        elif node.left and node.right is None:
            node = node.left 
        else:
            replacement_node = self.maximum(node.left)
            if replacement_node.left:
                replacement_parent = self.__find_parent(replacement_node, node)
                # Replacement made on right side o/w replacement_node isn't the max
                replacement_parent.right = replacement_node.left
            replacement_node.left = node.left
            replacement_node.right = node.right 
            node = replacement_node
        return node

    def __find_parent(self, child_node, tree_node):
        if tree_node is None: return None 
        if tree_node.left is child_node or tree_node.right is child_node:
            return tree_node
        if child_node.value < tree_node.value:
            return self.__find_parent(child_node, tree_node.left)
        else:
            return self.__find_parent(child_node, tree_node.right)

    # I think this is too conceptually complicated...
    # def __promote_child(self, tree_node):
    #     if tree_node.right:
    #         parent = tree_node
    #         child = tree_node.right 
    #         while child.right:
    #             parent = parent.right 
    #             child = child.right 
    #         parent.right = child.left
