# Implement a method that finds the sum of the first n
# fibonacci numbers recursively. Assume n > 0

def fibs_sum_no_dp(n):
  if n == 1: return 1
  if n ==2: return 2 
  return fibs_sum(n - 1) + fibs_sum(n - 2) + 1

def fibs_sum(num):
  memo = {1: 1, 2: 2}
  for n in range(3,num+1):
      memo[n] = memo[n-1] + fibonacci(n) #or can also make new Fibonacci class and use that
  return memo[n]

# Bottom-up
def fib_cache_builder(num):
  # Builds the cache, starting at 1 and ending at n
  cache = { 1: 1, 2: 1 }
  if num < 3: return cache
  for n in range(3,num+1):
    cache[n] = cache[n - 1] + cache[n - 2]
  return cache

def fibonacci(num):
  # Calls the helper function
  cache = fib_cache_builder(num)
  # Returns the nth entry
  return cache[num]

# Top-down
class Fibonacci:
  def __init__(self):
    self.cache = { 1: 1, 2: 1 }

  def fibonacci(self, n):
    # return 1 if n == 1 || n == 2
    # Check our cache instead of the original base case
    if self.cache.get(n, False): return self.cache[n]

    # Record our answer in our cache before returning it
    ans = fibonacci(n - 1) + self.fibonacci(n - 2)
    self.cache[n] = ans
    return ans


fibs_sum(6) == 20