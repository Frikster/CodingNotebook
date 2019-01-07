# Write a recursive function that returns the prime factorization of
# a given number. Assume num > 1
#
# prime_factorization(12) => [2,2,3]
def prime_factorization(num):
    if is_prime(num) : return [num]
    for candidate in range(2,num+1):
        if num % candidate == 0 and is_prime(candidate):
            return [candidate] + prime_factorization(num // candidate) 

def is_prime(num):
    for n in range(2, num):
        if num % n == 0 : return False
    return True


prime_factorization(12) == [2, 2, 3]
