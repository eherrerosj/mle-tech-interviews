"""
Given an array of integers nums and an integer k, return the total number of
    continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107

Learnings:
- Tricky to notice that sliding windows are a bad idea here due to the negative numbers
- Cumulative sum is the most optimal. Use a hashmap to store total sum and number of occurrences
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        cumsum = 0
        for i, v in enumerate(nums):
            cumsum += v
            # check cumsum - k
            if cumsum not in hm.keys():
                hm[cumsum]


sol = Solution().subarraySum(arr=[1, 1, 1], k=2)
print(sol == 2)


sol = Solution().findKthPositive(arr=[1, 2, 3], k=3)
print(sol == 2)
