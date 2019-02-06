# Write a recursive method that takes in a base 10 number n and
# converts it to a base b number. Return the new number as a string
#
# E.g. base_converter(5, 2) == "101"
# base_converter(31, 16) == "1f"

def base_converter_rec(num, b):
    if num == 0 : return ""
    hex = [_ for _ in 'abcdef']    
    base_b = num % b
    if base_b >= 10 : base_b = hex[base_b - 10] 
    return base_converter_rec(num // b, b) + str(base_b)

def base_converter(num, b):
    if num == 0: return '0'
    if num < 0:
        return '-' + base_converter_rec(-num, b)
    else:
        return base_converter_rec(num, b)

print(base_converter(6, 2) == "110")
print(base_converter(31, 16) == "1f")
print(base_converter(1, 16) == "1")
print(base_converter(-31, 16) == "-1f")
