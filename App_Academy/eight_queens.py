# CHALLENGE: Eight queens puzzle precursor
#
# Write a recursive method that generates all BOARD_SIZE possible unique ways to
# place eight queens on a chess board such that no two queens are in
# the same board row or column (the same diagonal is OK).
#
# Each of the 8! elements in the return array should be an array of positions:
# E.g. [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7]]
#
# My solution used 3 method parameters: current_row, taken_columns, and
# positions so far

# TODO: Grok eight-queens
# also works and don't get it:
GRID_SIZE = 8

def place_queens(row=0, columns=[], results=[]):
    if not columns:
        columns = ["_"] * 8
    if row == GRID_SIZE:
        results.append([(row,col) for row,col in enumerate(columns)])
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col #column at this row has queen at c
                place_queens(row + 1, columns, results)
    
    return results

def check_valid(columns, candidate_row, candidate_col):
    for row in range(candidate_row):
        col = columns[row]
        if candidate_col == col:
            return False 
        if abs(col - candidate_col) == abs(row - candidate_row):
            return False
    return True


print(place_queens(row=0, columns=[], results=[]))
print(len(place_queens(row=0, columns=[], results=[])))


# below works but difficult to understand
# import pdb

def under_attack(row, column, existing_queens):
    if not len(existing_queens):
        return False
    for queen in existing_queens:
        if not len(queen):
            continue
        r, c = queen
        if r == row:
            return True  # Check row
        if c == column:
            return True  # Check column
        if (column-c) == (row-r):
            return True  # Check left diagonal
        if (column-c) == -(row-r):
            return True  # Check right diagonal
    return False


def iter_solve(n):
    solutions = None
    for row in range(1, n+1):
        # for each row, check all valid column
        solutions = check(solutions, row, n)
    return solutions


def check(solutions, row, n):
    new_solutions = []
    for column in range(1, n+1):
        if not solutions:
            new_solutions.append([(row, column)])
        else:
            for solution in solutions:
                # pdb.set_trace()
                if not under_attack(row, column, solution):
                    new_solutions.append(solution + [(row, column)])
    return new_solutions

# print(iter_solve(8))
# 92 solutions (i.e. not rotationally invariant)
