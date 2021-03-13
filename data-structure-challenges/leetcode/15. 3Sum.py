"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

Learnings:
- O(n^2) is the best runtime complexity we can reach
- Sorting first is fundamental here, it allows us to skip many sum checks
- The (enumerate in the nested for loop + next if) could be replaced with range(i+1)
- Another elegant solution: loop over each num and then use (left - right) cursors.
    Increase left if total sum < 0, decrease right cursor if total sum > 0
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(f"\nnums: {nums}")
        hmap = {}
        sols = set()

        if len(nums) < 3:
            return []

        for i, num in enumerate(nums):
            hmap[num] = i

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if j <= i:
                    continue
                complement = -(num1 + num2)
                if complement in hmap and hmap[complement] > j:
                    sols.add((num1, num2, complement))
        print(f"sols: {list(sols)}")
        return list(sols)


sol = Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4])
print(sol == [[-1, -1, 2], [-1, 0, 1]])
