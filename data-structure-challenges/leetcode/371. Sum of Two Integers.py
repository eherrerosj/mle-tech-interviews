"""
Given two integers a and b, return the sum of the two integers
without using the operators + and -.


Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5


Constraints:
    -1000 <= a, b <= 1000

Learnings:
- Almost got it right the xor with and trick with shifting,
    I just missed the recursive trick with xor + b as carry. Great learning!
- Set union A | B
- Set intersection A & B
- Set subtraction A & ~B
- Set negation ALL_BITS ^ A or ~A
- Set bit A |= 1 << bit
- Clear bit A &= ~(1 << bit)
- Test bit (A & 1 << bit) != 0
- Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
- Remove last bit A&(A-1)
- Get all 1-bits ~0
- Pretty useful summary post on bit manipulation:
    https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
"""
from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a

        return self.getSum(a ^ b, (a & b) << 1)


sol = Solution().getSum(a=2, b=3)
print(sol == 5)

sol = Solution().getSum(a=3, b=2)
print(sol == 5)
