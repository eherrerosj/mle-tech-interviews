"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot 
index k (0 <= k < nums.length) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is guaranteed to be rotated at some pivot.
    -104 <= target <= 104
 
Follow up: Can you achieve this in O(log n) time complexity?

Learnings:
- Best to build the possible test cases: all sorted, lowest value is on left, lowest value is on right,
    lowest value is on middle
- At most two sorted halfs, mid will be apart of left sorted or right
    sorted, if target is in range of sorted portion then search it, otherwise search other half
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if not nums:
            return -1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


sol = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
print(sol == 4)

sol = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=5)
print(sol == 1)

sol = Solution().search(nums=[7, 0, 1, 2, 3, 4, 5], target=0)
print(sol == 1)

sol = Solution().search(nums=[0, 1, 2, 3, 4, 5], target=1)
print(sol == 1)

sol = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
print(sol == -1)

sol = Solution().search(nums=[1], target=0)
print(sol == -1)
