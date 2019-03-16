# TODO: Redo
from collections import Counter


class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':

        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        # witchcraft! This is the line of code you didn't know you could do
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

# Your not working solution
#         print(word1)
#         if word1 == word2:
#             return 0

#         word1_counter = Counter(word1)
#         word2_counter = Counter(word2)

#         res = float('inf')
#         for char in 'abcdefghijklmnopqrstuvwxyz':
#             if char in word2 and word1_counter[char] < word2_counter[char]:
#                 for idx in range(len(word1)+1):
#                     insertion = 1 + self.minDistance(word1[0:idx] + char + word1[idx:], word2)
#                     print("insertion")
#                     if insertion < res:
#                         res = insertion

#         for char in 'abcdefghijklmnopqrstuvwxyz':
#             if char in word2 and word1_counter[char] < word2_counter[char]:
#                 for idx in range(len(word1)):
#                     replacement = 1 + self.minDistance(word1[0:idx] + char + word1[idx+1:], word2)
#                     print("replacement")
#                     if replacement < res:
#                         res = replacement

#         for idx in range(len(word1)):
#             if word1_counter[word1[idx]] > word2_counter[word1[idx]]:
#                 deletion = 1 + self.minDistance(word1[0:idx] + word1[idx+1:], word2)
#                 print("deletion")
#                 if deletion < res:
#                     res = replacement

#         return res
