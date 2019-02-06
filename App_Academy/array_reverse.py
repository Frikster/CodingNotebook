def my_reverse(arr):
    reversed = []
    for _ in range(len(arr)):
        reversed.append(arr.pop())
    return reversed


def reverse_inplace(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    return arr

my_reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
print(reverse_inplace([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
