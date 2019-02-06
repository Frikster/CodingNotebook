# Implement a method that finds the sum of the first n
# fibonacci numbers recursively. Assume n > 0

def fibs_sum_no_dp(n):
  if n == 1: return 1
  if n == 2: return 2 
  return fibs_sum(n - 1) + fibs_sum(n - 2) + 1

def fibs_sum(num):
  fib_cache = fib_cache_builder(num)
  fibs_sum_cache = {1: 1, 2: 2}
  for n in range(3,num+1):
      fibs_sum_cache[n] = fibs_sum_cache[n-1] + fib_cache[n] 
  return fibs_sum_cache[n]

# Bottom-up
def fib_cache_builder(num):
  # Builds the cache, starting at 1 and ending at n
  cache = { 1: 1, 2: 1 }
  if num < 3: return cache
  for n in range(3,num+1):
    cache[n] = cache[n - 1] + cache[n - 2]
  return cache

# Top-down
class Fibonacci:
  def __init__(self):
    self.fib_cache = { 1: 1, 2: 1 }
    self.fibs_sum_cache = { 1: 1, 2: 2 }

  def fibonacci(self, num):
    # Check our cache instead of the original base case
    if num in self.fib_cache: return self.fib_cache[num]
    # Record our answer in our cache before returning it
    ans = self.fibonacci(num - 1) + self.fibonacci(num - 2)
    self.fib_cache[num] = ans
    return ans
  
  def fibs_sum(self, num):
    if num in self.fibs_sum_cache: return self.fibs_sum_cache[num]
    ans = self.fibs_sum(num - 1) + self.fibonacci(num)
    self.fibs_sum_cache[num] = ans
    return ans
    # there's no reason not to mix top and bottom up:
    # for n in range(3,num+1):
    #     memo[n] = memo[n-1] + self.fibonacci(n) 
    # return memo[n]


print(fibs_sum(6) == 20)
fib = Fibonacci()
print(fib.fibs_sum(6))
# 20