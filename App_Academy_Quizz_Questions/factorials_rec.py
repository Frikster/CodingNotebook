# Write a recursive method that returns the first "num" factorial numbers.
# Note that the 1st factorial number is 0!, which equals 1. The 2nd factorial
# is 1!, the 3rd factorial is 2!, etc.

def factorials_rec_no_dp(num):
  if num == 1: return [1] 
  prev_fac = factorials_rec(num - 1)
  return factorials_rec(num - 1) + [(num - 1) * prev_fac[-1]]

def factorials_rec(num):
  cache = {1: [1], 2: [1, 1]}
  for n in range(3,num+1):
      cache[n] = cache[n-1] + [factorial(n)] #or can also make new Factorial class and use that
  return cache[num]

# Bottom-up
def factorials_cache_builder(num):
  # Builds the cache, starting at 1 and ending at n
  cache = { 1: 1, 2: 1 }
  if num < 3: return cache
  for n in range(3,num+1):
    cache[n] = (n-1) * cache[n - 1]
  return cache

def factorial(num):
  # Calls the helper function
  cache = factorials_cache_builder(num)
  # Returns the nth entry
  return cache[num]

# Top-down
class Factorial:
  def __init__(self):
    self.cache = { 1: 1, 2: 1 }

  def factorial(self, num):
    # return 1 if n == 1 || n == 2
    # Check our cache instead of the original base case
    if self.cache.get(num, False): return self.cache[num]

    # Record our answer in our cache before returning it
    ans = (num-1) * self.factorial(num - 1)
    self.cache[num] = ans
    return ans


factorials_rec(6) == [1, 1, 2, 6, 24, 120]