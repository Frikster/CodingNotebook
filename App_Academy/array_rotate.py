# This is O(n^2) !! and O(n) space
# def my_rotate(arr, num=1):
#     rotations = num % len(arr)
#     dupe = arr.copy() # Simply don't use if duplicate isn't required
#     for _ in range(rotations):
#         first = dupe.pop(0)
#         dupe.append(first)
#     return dupe

def my_rotate(arr, num=1):
    # arr = arr.copy() if needed
    # reverse segment in place
    def reverse_segment(start, end):
        end -= 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    rotations = num % len(arr)
    reverse_segment(0, len(arr))
    reverse_segment(len(arr) - rotations, len(arr))
    reverse_segment(0, len(arr) - rotations)
    return arr

print(my_rotate([1, 2, 3, 4, 5]))
#[2, 3, 4, 5, 1]
print(my_rotate([1, 2, 3, 4, 5], 3))
#[4, 5, 1, 2, 3]
