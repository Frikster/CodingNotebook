# Write a method that returns the factors of a number in ascending order.
def factors(num):
    return sorted(filter(lambda n: num % n == 0, range(1,num)))

factors(20)
# [1, 2, 4, 5, 10]
