def my_zip(array, *arrs):
    res = [[el] for el in array]
    for arr in arrs:
        for idx in range(len(res)):
            res[idx].append(arr[idx])
    return res


my_zip([1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 6])
#[[1, 4, 1], [2, 3, 2], [3, 2, 3], [4, 1, 6]]
