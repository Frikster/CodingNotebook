# TODO: Test
# from collections import defaultdict

# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.isWord = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for w in word:
#             node = node.children[w] # return empty TrieNode if no children for w
#         node.isWord = True

#     def search(self, word):
#         node = self.root
#         for w in word:
#             node = node.children.get(w)
#             if not node:
#                 return False
#         return node.isWord

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        current_node = self.root 

        for i in len(word):
            if not word[i] in current_node:
                current_node[word[i]] = {}
            current_node = current_node[word[i]]
        current_node['*'] = True

    def search(self, word):
        current_node = self.root

        for i in len(word):
            if not word[i] in current_node:
                return False
            current_node = current_node[word[i]]
        return current_node['*']

