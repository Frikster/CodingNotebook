# primes(num) returns an array of the first "num" primes.
# You may wish to use an is_prime? helper method.

def is_prime(num):
    for n in range(2,num):
        if num % n == 0: return False
    return True

def primes(num):
    res = []
    candidate = 2
    while len(res) < num:
        if is_prime(candidate):
            res.append(candidate)
        candidate += 1
    return res

primes(5)
#[2, 3, 5, 7, 11]
