# Write a method that capitalizes each word in a string like a book title
# Do not capitalize words like 'a', 'and', 'of', 'over' or 'the'
def titleize(title):
    ignore = ['a', 'and', 'of', 'over' , 'the']
    title_split = title.split()
    for idx, word in enumerate(title_split):
       if idx == 0 or not word in ignore:
           title_split[idx] = title_split[idx][0].upper() + word[1:]
    return ' '.join(title_split)

print(titleize("dfgdfg fdgdfg a and dfgdfg"))
#'Dfgdfg Fdgdfg a and Dfgdfg'
