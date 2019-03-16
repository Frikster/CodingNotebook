# Given a 2d grid map of '1's(land) and '0's(water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if grid == [[]]:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid, row, col):
        if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '#'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col-1)
