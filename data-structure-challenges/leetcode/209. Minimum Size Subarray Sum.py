"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
numsr-1, numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 105
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

Learnings
- Left and Right cursor FTW again
- Template with min/max subarray can be solved normally with this for(while()) template
- How it works: R moves forward until target met, then L moves forward until target is not met.
    Kind of an expand + stretch.
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while target <= current_sum and l <= r:
                res = min(res, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return 0 if res == float("inf") else res


sol = Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
print(sol == 2)
