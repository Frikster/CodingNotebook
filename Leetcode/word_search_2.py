# hints: obviously don't try to create a trie for every element in board going to every other element... O(N^4)
# Use trie and add all words to trie. Now think dfs using the trie as help.
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        for char in word:
            if not char in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return '*' in curr  # i.e. to check if the word terminates here


class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        self.board = board
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.res = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(row, col, trie.root, '')
        return list(self.res)

    def dfs(self, row, col, node, word):
        if '*' in node:
            self.res.add(word)
        if row >= len(self.board) or row < 0 or col >= len(self.board[0]) or col < 0:
            return
        curr = self.board[row][col]
        if curr in node:
            node = node[curr]
        else:
            return
        word += curr
        for (next_row, next_col) in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
            self.board[row][col] = '#'
            self.dfs(next_row, next_col, node, word)
            self.board[row][col] = curr
