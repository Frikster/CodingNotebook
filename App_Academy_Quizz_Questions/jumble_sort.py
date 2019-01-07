# Jumble sort takes a string and an alphabet. It returns a copy of the string
# with the letters re-ordered according to their positions in the alphabet. If
# no alphabet is passed in, it defaults to normal alphabetical order (a-z).

# Example:
# jumble_sort("hello") => "ehllo"
# jumble_sort("hello", ['o', 'l', 'h', 'e']) => 'ollhe'

def jumble_sort(string, alphabet = None):
    alphabet = alphabet or [c for c in 'abcdefghijklmnopqrstuvwxyz']
    return ''.join(sorted(string, key=lambda el: alphabet.index(el)))

jumble_sort("hello") == "ehllo"
jumble_sort("hello", ['o', 'l', 'h', 'e']) == 'ollhe'
