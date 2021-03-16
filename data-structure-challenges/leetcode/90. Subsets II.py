"""
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10


Learnings:
- Sort first, much better, since you won't have to do it later
- There can be repeated items, so you need to use
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res


sol = Solution().subsetsWithDup(nums=[1, 2, 2])
print(sol == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

sol = Solution().subsetsWithDup(nums=[0])
print(sol == [[], [0]])
