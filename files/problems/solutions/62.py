class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * n] * m
        for row in range(m):
            for col in range(n):
                if not (row and col):
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        return grid[-1][-1]
