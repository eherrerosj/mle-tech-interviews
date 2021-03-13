"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Learning:
- Dynamic programming like #53
- Variation of Kadenze's algo
- Left - Right cursor with DP. Negatives and positives alter the product each time
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(f"\nnums: {nums}")
        prefix = suffix = 0
        global_max = float("-inf")
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            global_max = max(prefix, suffix, global_max)
        return global_max


sol = Solution().maxProduct(nums=[2, 3, -2, 4])
print(sol == 6)

sol = Solution().maxProduct(nums=[0, 2])
print(sol == 2)

sol = Solution().maxProduct(nums=[2, 3])
print(sol == 6)


sol = Solution().maxProduct(nums=[-2, 3, -2, 4])
print(sol == 48)

sol = Solution().maxProduct(nums=[-5, 0, 2])
print(sol == 2)

sol = Solution().maxProduct(nums=[-2, 0, -1])
print(sol == 0)

sol = Solution().maxProduct(nums=[2, 0, -1])
print(sol == 2)

sol = Solution().maxProduct(nums=[-2, 10, -1])
print(sol == 20)

sol = Solution().maxProduct(nums=[-3, 0, 1, -2])
print(sol == 1)
