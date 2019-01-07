# Write a recursive method that takes in a base 10 number n and
# converts it to a base b number. Return the new number as a string
#
# E.g. base_converter(5, 2) == "101"
# base_converter(31, 16) == "1f"

def base_converter(num, b):
    if num == 0 : return ""
    hex = [_ for _ in 'abcdef']    
    base_b = num % b
    if base_b >= 10 : base_b = hex[base_b - 10] 
    return base_converter(num // b, b) + str(base_b)


base_converter(5, 2) == "101"
base_converter(31, 16) == "1f"
