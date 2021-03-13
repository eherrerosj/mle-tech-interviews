"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45

Learning:
- Better to create an internal additional method
- Brute force approach implemented in Solution 1 using recursion. O(2^n). Possible
    optimization would be adding memoization (a dict of already known step results)
- Alternatively and more optimal would be Dynamic Programming with O(n), solution 2.
    It breaks the problem into subproblems
"""


class Solution1:
    def climbStairs(self, n: int) -> int:
        return self._climbStairs(0, n)

    def _climbStairs(self, i, n):
        if i > n:
            return 0
        elif i == n:
            return 1
        sol = self._climbStairs(i + 1, n) + self._climbStairs(i + 2, n)
        print("sol:", sol)
        return sol


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        sol = [0] * (n + 1)
        sol[1], sol[2] = 1, 2

        for i in range(3, n + 1):
            sol[i] = sol[i - 2] + sol[i - 1]
        return sol[n]


# Recursion
sol = Solution1().climbStairs(n=2)
print(sol == 2)

sol = Solution1().climbStairs(n=3)
print(sol == 3)

sol = Solution1().climbStairs(n=4)
print(sol == 5)


# Dynamic Programming
sol = Solution2().climbStairs(n=2)
print(sol == 2)

sol = Solution2().climbStairs(n=3)
print(sol == 3)

sol = Solution2().climbStairs(n=4)
print(sol == 5)

sol = Solution2().climbStairs(n=5)
print(sol == 8)