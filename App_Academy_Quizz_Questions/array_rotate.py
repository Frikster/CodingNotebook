def my_rotate(arr, num=1):
    rotations = num % len(arr)
    dupe = arr.copy()
    for _ in range(rotations):
        first = dupe.pop(0)
        dupe.append(first)
    return dupe

my_rotate([1, 2, 3, 4, 5])
#[2, 3, 4, 5, 1]
my_rotate([1, 2, 3, 4, 5], 3)
#[4, 5, 1, 2, 3]
