 # Write a String#symmetric_substrings method that returns an array of substrings
 # that are palindromes, e.g. "cool".symmetric_substrings => ["oo"]
 # Only include substrings of length > 1.

# Old brute force method
# def substrings(string):
#     res = []
#     for idx in range(len(string)):
#         for jdx in range(idx+1, len(string)+1):
#             res.append(string[idx:jdx])
#     return res

# def symmetric_substrings(string):
#     return [substr for substr in substrings(string) if list(reversed(substr)) == list(substr)]
import pdb

def symmetric_substrings(string):
    def manachers(string):
        A = '$#' + '#'.join(string) + '#@'
        # palin_len_tracker[idx] tracks what the longest palindrome in A is with center at idx
        palin_len_tracker = [0] * len(A)
        # right tracks the rightmost point of the longest palindrome found
        # center tracks the point that presently has the longest palindrome
        center = right = 0
        # idx is our "candidate center"
        for idx in range(1, len(A) - 1):
            mirror_idx = 2*center - idx # the mirrod of idx if idx < right
            # if our idx is withint the boundaries of right, we know that a palindrom at this center exists that is at least
            # as long as what we have or what we found at the mirror (which would include this point in the palindrome)
            # I presume this prevents O(n*2) as you prevent making the palindrome each time
            if idx < right:
                palin_len_tracker[idx] = min(right - idx, palin_len_tracker[mirror_idx])
            #'$#A#B#A#B#A#B#A@' - if you start at any point and expand in both directions. 
            # If palin_len_tracker already has a value at this point you are trying to do better than this length
            while A[idx + palin_len_tracker[idx] + 1] == A[idx - palin_len_tracker[idx] - 1]:
                palin_len_tracker[idx] += 1
            # If our palindrome goes beyond right we have a new winner and have to update center and right
            if idx + palin_len_tracker[idx] > right:
                center, right = idx, idx + palin_len_tracker[idx]
        return palin_len_tracker

    #'$#c#o#o#l#@' index 2 is actually index 0 in original string, 4 is 1, 6 is 2. i.e. (idx//2)-1
    # '$#c#o#o#l#@'       at index 5 we are at 5//2 - 1 = 1 for 'cool' and to the left of the mid-point of a palindrome of even length
    # '$#a#b#a#1#c#d#c#@' at index 4 we are at 4//2 - 1 = 1 for 'aba1cdc' and at the midpoint of a palindrome of odd length

    # Once you have the midpoint it's (length//2) on either side from the mid point if odd length
    # o/w one less on one side than the other with an even length
    res = []
    for idx, length in enumerate(manachers(string)):
        if idx % 2 == 0:
            res.append(string[(idx//2)-1-(length//2):(idx//2)+(length//2)])
        else:
            res.append(string[(idx//2)-1-(length//2)+1:(idx//2)+(length//2)])
    return [sub for sub in res if len(sub) > 1]
    

print(symmetric_substrings("cool") == ['oo'])
print(symmetric_substrings('aba1cdc') == ['aba', 'cdc'])
print(symmetric_substrings("cool"))
print(symmetric_substrings('aba1cdc'))

print(symmetric_substrings('cooool'))
print(symmetric_substrings('coooool'))
