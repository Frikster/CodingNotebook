# Write a method that translates a sentence into pig latin. You may want a helper method.
# 'apple' => 'appleay'
# 'pearl' => 'earlpay'
# 'quick' => 'ickquay'
def pig_latinify(sentence):
    return ' '.join([pig_word(word) for word in sentence.split()])

def pig_word(word):
    vowels = [v for v in 'aeiouAEIOU']
    if word[0] in vowels: return word + "ay"
    consonants = ""
    for idx,c in enumerate(word):
        if not c in vowels: consonants += c
        if c == 'u' and idx != 0 and word[idx-1] == 'q': consonants += c 
        if c in vowels: break
    return word[len(consonants):] + consonants + "ay"

pig_latinify("apple pearl quick") == 'appleay earlpay ickquay'
