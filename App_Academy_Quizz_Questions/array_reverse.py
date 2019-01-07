def my_reverse(arr):
    reversed = []
    for _ in range(len(arr)):
        reversed.append(arr.pop())
    return reversed

my_reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
