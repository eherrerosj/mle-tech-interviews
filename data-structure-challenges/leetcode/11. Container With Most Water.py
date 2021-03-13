"""
Given n non-negative integers a1, a2, ..., an , where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that the
two endpoints of the line i is at (i, ai) and (i, 0). Find two lines,
which, together with the x-axis forms a container, such that the
container contains the most water.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2


Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

Learnings:
- Again, the power of double cursor in arrays
- We can only get more area if we find higher bars, since width is only going to decrease
- My mistake was trying to optimize only for the right cursor an iterating through
    every possible value on the left side. This is not optimal
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        sol = 0
        l, r = 0, len(height) - 1
        while l < r:
            sol = max(sol, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        print(sol)
        return sol


sol = Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
print(sol == 49)

sol = Solution().maxArea(height=[4, 3, 2, 1, 4])
print(sol == 16)
