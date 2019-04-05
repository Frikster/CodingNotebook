# TODO: redo on O(srt(N)) - https://codility.com/media/train/8-PrimeNumbers.pdf

# Write a method that returns the factors of a number in ascending order.
def factors(num):
    return [n for n in range(1,num) if num % n == 0]
    # return sorted(filter(lambda n: num % n == 0, range(1,num)))

print(factors(20))
# [1, 2, 4, 5, 10]
