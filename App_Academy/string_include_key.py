# Write a recursive method that takes in a string to search and a key string.
# Return true if the string contains all of the characters in the key
#
# in the same order that they appear in the key.
#
# string_include_key?("cadbpc", "abc") => true
# string_include_key("cba", "abc") => false
def string_include_key(string, key):
    if key == "" : return True
    if string == "" : return False
    if string[0] == key[0]:
        return string_include_key(string[1:], key[1:])
    else:
        return string_include_key(string[1:], key)


string_include_key("cadbpc", "abc") == True
string_include_key("cba", "abc") == False
