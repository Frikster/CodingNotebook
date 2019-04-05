# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# Note that there may be duplicates in T so this is different from Pramp one. i.e. S = "AA", T = "AA". Output should be: "AA"

from collections import Counter

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        counter_hash = Counter(t) # defaults to 0.
        left, right = 0, 0
        store = (float('-inf'), float('inf'))
        uniq_counter = 0

        while right < len(s):
            if s[right] in counter_hash:
                if counter_hash[s[right]] == 1:
                    uniq_counter += 1
                counter_hash[s[right]] -= 1
            right+=1
            while uniq_counter >= len(set(t)):
                if right - left < store[1] - store[0]:
                    store = (left, right)
                if s[left] in counter_hash:
                    if counter_hash[s[left]] == 0:
                        uniq_counter -= 1
                    counter_hash[s[left]] += 1
                left += 1

        if store == (float('-inf'), float('inf')):
            return ""
        return s[store[0]:store[1]]  

# TEMPLATE
# int findSubstring(string s){
#     vector < int > map(128, 0)
#     int counter
#     // check whether the substring is valid
#     int begin = 0, end = 0
#     // two pointers, one point to tail and one  head
#     int d
#     // the length of substring

#         for() { / * initialize the hash map here * / }

#     while(end < s.size()){

#             if(map[s[end++]]-- ?){ / * modify counter here * / }

#             while(/* counter condition * /){

#                 / * update d here if finding minimum substring*/

#                 // increase begin to make it invalid/valid again

#                 if(map[s[begin++]]++ ?){/ *modify counter here*/ }
#             }

#             / * update d here if finding maximum substring*/
#     }
#     return d
# }
