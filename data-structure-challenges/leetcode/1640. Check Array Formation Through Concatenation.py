"""
You are given an array of distinct integers arr and
an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr
from pieces. Otherwise, return false.

Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Example 2:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 3:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 4:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Example 5:
Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false

Constraints:
    1 <= pieces.length <= arr.length <= 100
    sum(pieces[i].length) == arr.length
    1 <= pieces[i].length <= arr.length
    1 <= arr[i], pieces[i][j] <= 100
    The integers in arr are distinct.
    The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""

from typing import List
import unittest


class TestSum(unittest.TestCase):
    def test_solution_1(self):
        """
        Test solution below
        """
        arr = [91, 4, 64, 78, 10]
        pieces = [[78, 10], [4, 64], [91]]
        expected_output = True
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_2(self):
        """
        Test solution below
        """
        arr = [91, 4, 64, 78]
        pieces = [[78], [4, 64], [91]]
        expected_output = True
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_3(self):
        """
        Test solution below
        """
        arr = [1, 3, 5, 7]
        pieces = [[2, 4, 6, 8]]
        expected_output = False
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_4(self):
        """
        Test solution below
        """
        arr = [49, 18, 16]
        pieces = [[16, 18, 49]]
        expected_output = False
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_5(self):
        """
        Test solution below
        """
        arr = [49]
        pieces = [[49]]
        expected_output = True
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_6(self):
        """
        Test solution below
        """
        arr = [49, 20]
        pieces = [[49], [20]]
        expected_output = True
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_7(self):
        """
        Test solution below
        """
        arr = [91, 4, 64, 78]
        pieces = [[78], [64, 4], [91]]
        expected_output = False
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)

    def test_solution_8(self):
        """
        Test solution below
        """
        arr = [1, 2, 3]
        pieces = [[2], [1, 3]]
        expected_output = False
        sol = Solution().canFormArray(arr, pieces)
        self.assertEquals(sol, expected_output)


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_len = len(arr)
        for piece_set in pieces:
            len_piece_set = len(piece_set)
            for i in range(arr_len - len_piece_set + 1):
                if arr[i : i + len_piece_set] == piece_set:
                    arr[i : i + len_piece_set] = [0 for _ in range(len_piece_set)]
                    break
        if sum(arr):
            return False
        return True


unittest.main()
