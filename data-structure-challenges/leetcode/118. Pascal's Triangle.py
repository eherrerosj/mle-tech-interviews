"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows > 2:
            for _ in range(1, numRows - 1):
                nr = self.generate_row(res[-1])
                res.append(nr)
        return res

    def generate_row(self, row: list) -> List:
        new_row = [1]
        for i in range(len(row) - 1):
            suma = sum(row[i : i + 2])
            new_row.append(suma)
        new_row.append(1)
        return new_row


sol = Solution()
print(sol.generate(5))