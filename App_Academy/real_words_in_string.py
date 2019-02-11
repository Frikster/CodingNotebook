 # Returns an array of all the subwords of the string that appear in the
 # dictionary argument. The method does NOT return any duplicates.

def real_words_in_string(string, dictionary):
    return [w for w in dictionary if w in string]

print(real_words_in_string("batcabtarbrat", ["cat", "car"]))
#[]

dictionary = ["bears", "ear", "a", "army"]
print(real_words_in_string("erbearsweatmyajs", dictionary))
# ["bears", "ear", "a"]
