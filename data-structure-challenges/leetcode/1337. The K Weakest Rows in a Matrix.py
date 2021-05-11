"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.


Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]


Constraints:
    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""

from typing import List
import unittest


class TestSum(unittest.TestCase):
    def test_solution_1(self):
        mat = [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
        k = 3
        output = [2, 0, 3]
        sol = Solution().kWeakestRows(mat, k)
        self.assertEqual(output, sol)

    def test_solution_2(self):
        mat = [[1, 0], [1, 0], [1, 0], [1, 1]]
        k = 4
        output = [0, 1, 2, 3]
        sol = Solution().kWeakestRows(mat, k)
        self.assertEqual(output, sol)

    def test_solution_3(self):
        mat = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
        ]
        k = 3
        output = [1, 2, 3]
        sol = Solution().kWeakestRows(mat, k)
        self.assertEqual(output, sol)

    def test_solution_4(self):
        mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
        k = 1
        output = [0]
        sol = Solution().kWeakestRows(mat, k)
        self.assertEqual(output, sol)


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Iterate through every column. For each column iterate each value and append if it's a 0.
        A last for loop is needed in case 1s need to be considered
        """
        num_rows, num_cols = len(mat), len(mat[0])
        sol = []

        for n in range(num_cols):
            for m in list(range(num_rows)):
                if not mat[m][n] and m not in sol:
                    sol.append(m)
                    k -= 1
                if not k:
                    return sol

        for m in range(num_rows):
            if mat[m][n] and m not in sol:
                sol.append(m)
                k -= 1
            if not k:
                return sol


unittest.main()
