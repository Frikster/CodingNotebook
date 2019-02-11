class MazeSolver:
    def __init__(self):
        self.maze_cache = {}

    def maze_solver(self, maze, start_pos, end_pos):
        self.dfs_builder(maze, start_pos, end_pos, [start_pos], 0)
        return self.best_path

    def dfs_builder(self, maze, start_pos, end_pos, this_path, steps):
        if start_pos == end_pos and (not end_pos in self.maze_cache or steps < self.maze_cache[end_pos]):
            self.best_path = this_path
        self.maze_cache[start_pos] = steps
        for next_pos in self.get_moves(maze, start_pos):
            if next_pos in self.maze_cache and self.maze_cache[next_pos] < steps + 1:
                continue
            self.dfs_builder(maze, next_pos, end_pos, this_path + [next_pos], steps + 1)

    def get_moves(self, maze, from_pos):
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        x, y = from_pos
        result = []

        for dx,dy in directions:
            new_loc = (x + dx, y + dy)
            if self.is_valid_pos(maze, new_loc):
                result.append(new_loc)
        return result

    def is_valid_pos(self, maze, pos):
        x, y = pos
        return x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] != "X"

maze1 =  [['X', 'X', 'X', 'X'],
          ['X', 'S', ' ', 'X'],
          ['X', 'X', 'F', 'X']] 
maze2 =  [['X', 'X', 'X', ' ', 'X', 'X', 'F', 'X'],
          ['X', 'S', 'X', ' ', 'X', 'X', ' ', 'X'],
          ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          ['X', 'X', 'X', ' ', 'X', 'X', ' ', 'X'],
          ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']] 
maze3 =   [['X', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
           ['X', 'S', ' ', ' ', 'X', 'X', ' ', 'X'],
           ['X', ' ', 'X', ' ', ' ', 'X', ' ', 'X'],
           ['X', ' ', ' ', 'X', ' ', ' ', 'F', 'X'],
           ['X', 'X', ' ', ' ', ' ', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']] 

ms = MazeSolver()
print(ms.maze_solver(maze1, (1, 1), (2, 2)))
ms = MazeSolver()
print(ms.maze_solver(maze2, (1, 1), (0, 6)))
ms = MazeSolver()
print(ms.maze_solver(maze3, (1, 1), (3, 6)))
#[(1, 1), (1, 2), (2, 2)]
#[(1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (1, 6), (0, 6)]
#[(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6)]
