"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105

Learnings:
- Typical fb
- Actually hard to realize that the solution can be either of these 3:
    1. 2 pointers (L and R): update smaller cursor. Keep track of left max and right max
        and compare with updated cursor
    2. DP: min-max 3xO(n), 2 first loops for sorting, last loop for summing water vol
    3. Stacks: push elements until we find an element higher than the one on top,
        then pop elements calculating the water that fits in the bar
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        print(f"\nheight: {height}")
        input_len = len(height)
        if input_len < 3:
            return 0
        left_max_array = [0] * input_len
        right_max_array = [0] * input_len
        sol = 0

        # compute left-max of each array position
        for i in range(input_len):
            if i == 0:
                left_max_array[i] = height[i]
                continue
            left_max_array[i] = max(left_max_array[i - 1], height[i])
        print(f"\tleft_max_array: {left_max_array}")

        # compute right-max of each array position
        for i in range(input_len - 1, -1, -1):
            if i == input_len - 1:
                right_max_array[i] = height[i]
                continue
            right_max_array[i] = max(right_max_array[i + 1], height[i])
        print(f"\tright_max_array: {right_max_array}")

        # compute units of water per column (per array element)
        for i, h in enumerate(height):
            sol += min(left_max_array[i], right_max_array[i]) - h
            print(f"\ti: {i}\th: {h}\tsol: {sol}")
        return sol


sol = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(sol == 6)

sol = Solution().trap(height=[4, 2, 0, 3, 2, 5])
print(sol == 9)

# sol = Solution().trap(height=[2, 3, 4])
# print(sol == 0)

# sol = Solution().trap(height=[4, 3, 2])
# print(sol == 0)

# sol = Solution().trap(height=[2, 2, 0, 2])
# print(sol == 2)

# sol = Solution().trap(height=[3, 4, 4])
# print(sol == 0)

# sol = Solution().trap(height=[4, 4, 4, 4, 4])
# print(sol == 0)

# sol = Solution().trap(height=[4, 5, 0, 1])
# print(sol == 1)

# sol = Solution().trap(height=[4, 5, 0, 1, 2])
# print(sol == 3)
