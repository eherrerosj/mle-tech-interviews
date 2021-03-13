"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Learnings:
- Use hash map to instantly check for difference value,
    map will add index of last occurrence of a num, don’t use same element twice;
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Single-pass hashmap with O(n) time complexity and O(n) space."""
        print("\n", nums)
        hmap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hmap:
                return [idx, hmap.get(complement)]
            hmap[num] = idx


sol = Solution().twoSum([2, 7, 11, 15], 9)
print(set(sol) == set([0, 1]))

sol = Solution().twoSum([-2, 7, 11, 15], 5)
print(set(sol) == set([0, 1]))

sol = Solution().twoSum([3, 2, 4], 6)
print(set(sol) == set([1, 2]))
