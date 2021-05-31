"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -9999 <= nums[i], target <= 9999
    All the integers in nums are unique.
    nums is sorted in an ascending order.

Learnings:
- 
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4)
print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1)
