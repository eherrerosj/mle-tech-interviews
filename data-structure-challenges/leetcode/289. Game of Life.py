"""
According to Wikipedia's article: "The Game of Life, also known simply as Life,
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
    live (represented by a 1) or dead (represented by a 0). Each cell interacts with its
    eight neighbors (horizontal, vertical, diagonal) using the following four rules
    (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Learnings:
- Important to notice that a board copy must be done to avoid chained reactions on a single step
- I failed at copying the board by doing board[:][:] <- not right
- Building a neighbors matrix is very interesting to then solve the position lookup in a single conditional
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        num_rows = len(board)
        num_cols = len(board[0])
        board_copy = [[board[row][col] for col in range(num_cols)] for row in range(num_rows)]

        for m in range(num_rows):
            for n in range(num_cols):
                total = 0
                for neighbor in neighbors:
                    r = m + neighbor[0]
                    c = n + neighbor[1]

                    if (r < num_rows and r >= 0) and (c < num_cols and c >= 0):
                        total += board_copy[r][c]

                if board_copy[m][n] == 0:
                    if total == 3:
                        board[m][n] = 1
                else:
                    if total < 2 or total > 3:
                        board[m][n] = 0


sol = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(sol == 6)
