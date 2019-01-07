# Write a method, `digital_root(num)`. It should Sum the digits of a positive
# integer. If it is greater than 10, sum the digits of the resulting number.
# Keep repeating until there is only one digit in the result, called the
# "digital root". **Do not use string conversion within your method.**
#
# You may wish to use a helper function, `digital_root_step(num)` which performs
# one step of the process.

def digital_root_step(num):
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10
    return res

def digital_root(num):
    while True:
        num = digital_root_step(num)
        if num < 10: return num

digital_root(123)
#6
digital_root(1234)
#1
digital_root(12346)
#7


