# 10.9
import pdb
def sorted_mat_search(mat, target):
    if len(mat) == 0:
        return None
    return sorted_mat_search_bounds(mat, target, (0,0), (len(mat), len(mat[0])))

def sorted_mat_search_bounds(mat, target, top_left, bot_right):
    if top_left[0] >= bot_right[0] or top_left[1] >= bot_right[1]:
        return None
    mid = ((top_left[0] + bot_right[0]) // 2, (top_left[1] + bot_right[1]) // 2)
    if mat[mid[0]][mid[1]] == target:
        return (mid[0], mid[1])

    # note that bot_right coords are always +1 from where the "actual" bot_right is in the matrix
    if mat[mid[0]][mid[1]] > target:
        # top-left segment then top-right segment then bot-left segment
        return sorted_mat_search_bounds(mat, target, top_left, mid) or \
            sorted_mat_search_bounds(mat, target, (top_left[0], mid[1]), (mid[0], bot_right[1])) or \
            sorted_mat_search_bounds(mat, target, (mid[0], top_left[1]), (bot_right[0], mid[1]))
    else:
        # bot-right segment then top-right segment then bot-left segment
        return sorted_mat_search_bounds(mat, target, (mid[0]+1, mid[1]+1), bot_right) or \
            sorted_mat_search_bounds(mat, target, (top_left[0], mid[1]+1), (mid[0]+1, bot_right[1])) or \
            sorted_mat_search_bounds(mat, target, (mid[0]+1, top_left[1]), (bot_right[0], mid[1]+1))

mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
        [5,  10, 15, 20, 25, 30, 35, 40, 45],
        [10, 20, 30, 40, 50, 60, 70, 80, 90],
        [13, 23, 33, 43, 53, 63, 73, 83, 93],
        [14, 24, 34, 44, 54, 64, 74, 84, 94],
        [15, 25, 35, 45, 55, 65, 75, 85, 95],
        [16, 26, 36, 46, 56, 66, 77, 88, 99]]
print(sorted_mat_search(mat, 10))
print(sorted_mat_search(mat, 13))
print(sorted_mat_search(mat, 14))
print(sorted_mat_search(mat, 16))
print(sorted_mat_search(mat, 56))
print(sorted_mat_search(mat, 65))
print(sorted_mat_search(mat, 74))
print(sorted_mat_search(mat, 99))
# as expected: https://github.com/w-hat/ctci-solutions/blob/master/ch-10-sorting-and-searching/09-sorted-matrix-search.py
