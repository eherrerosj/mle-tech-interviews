"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-100000]
Output: -100000

Constraints:
    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105

Learnings:
- Dynamic programming to partition the problem into subproblems
- Kadenzes algorithm. More here: https://www.youtube.com/watch?v=86CQq3pKSUw
- Pattern: prev subarray cant be negative. Compute max sum for each prefix
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = curmax = nums[0]
        if len(nums) == 1:
            return sol

        for i in range(1, len(nums)):
            curmax = max(nums[i], curmax + nums[i])
            sol = max(curmax, sol)
        return sol


sol = Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(sol == 6)

sol = Solution().maxSubArray(nums=[-2, 3, 2, -1])
print(sol == 5)

sol = Solution().maxSubArray(nums=[-2, 3, -2, 7, -1])
print(sol == 8)


sol = Solution().maxSubArray(nums=[1])
print(sol == 1)

sol = Solution().maxSubArray(nums=[0])
print(sol == 0)

sol = Solution().maxSubArray(nums=[-100000])
print(sol == -100000)
