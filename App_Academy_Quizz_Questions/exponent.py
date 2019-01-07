# return b^n recursively. Your solution should accept negative values
# for n
def exponent(b, n):
  if n == 0 : return 1
  if n < 0 : return 1 / exponent(b, -n)
  return b * exponent(b, n-1)


exponent(4, -2) == 4**-2
exponent(5, 5) == 5**5
