# Write a recursive method that returns the first "num" factorial numbers.
# Note that the 1st factorial number is 0!, which equals 1. The 2nd factorial
# is 1!, the 3rd factorial is 2!, etc.

def factorials_rec_no_dp(num):
  if num == 1: return [1] 
  prev_fac = factorials_rec(num - 1)
  return factorials_rec(num - 1) + [(num - 1) * prev_fac[-1]]

# Bottom-up
def factorials_rec(num):
  fac_cache = factorials_cache_builder(num)
  facs_cache = {1: [1], 2: [1, 1]}
  for n in range(3,num+1):
      facs_cache[n] = facs_cache[n-1] + [fac_cache[n]] 
  return facs_cache[num]

def factorials_cache_builder(num):
  # Builds the cache, starting at 1 and ending at n
  fac_cache = { 1: 1, 2: 1 }
  if num < 3: return fac_cache
  for n in range(3,num+1):
    fac_cache[n] = (n-1) * fac_cache[n - 1]
  return fac_cache

# Top-down
class Factorial:
  def __init__(self):
    self.fac_cache = { 1: 1, 2: 1 }
    self.facs_cache = {1: [1], 2: [1, 1]}

  def factorial(self, num):
    if num in self.fac_cache: return self.fac_cache[num]
    # Record our answer in our cache before returning it
    ans = (num-1) * self.factorial(num - 1)
    self.fac_cache[num] = ans
    return ans

  def factorials_rec(self, num):
    if num in self.facs_cache: return self.facs_cache[num]
    ans = self.factorials_rec(num-1) + [self.factorial(num)]
    self.facs_cache[num] = ans 
    return ans
    # There is no reason not to use bottom up for one top down for the other
    # i.e. this could also work here:
    # for n in range(3, num+1):
    #     self.facs_cache[n] = self.facs_cache[n-1] + [self.factorial(n)]
    # return self.facs_cache[num]


print(factorials_rec(6) == [1, 1, 2, 6, 24, 120])
fac = Factorial()
print(fac.factorials_rec(6))
