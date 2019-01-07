 # Write a String#symmetric_substrings method that returns an array of substrings
 # that are palindromes, e.g. "cool".symmetric_substrings => ["oo"]
 # Only include substrings of length > 1.

def substrings(string):
    res = []
    for idx in range(len(string)):
        for jdx in range(idx+1, len(string)):
            res.append(string[idx:jdx+1])
    return res

def symmetric_substrings(string):
    return list(filter(lambda substr: list(reversed(substr)) == list(substr), substrings(string)))

symmetric_substrings("cool") == ['oo']
symmetric_substrings('aba1cdc') == ['aba', 'cdc']
