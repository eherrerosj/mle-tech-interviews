"""
Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements
of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does
not count as extra space for the purpose of space complexity analysis.)

Learnings:
- Make 3 passes: first in-order, second in-reverse, then to compute products
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        leftarr = [1] * nums_len
        rightarr = [1] * nums_len
        sol = [1] * nums_len
        for idx in range(nums_len):
            if idx == 0:
                continue
            leftarr[idx] = leftarr[idx - 1] * nums[idx - 1]

        for idx in range(nums_len, 0, -1):
            if idx == nums_len:
                continue
            rightarr[idx - 1] = rightarr[idx] * nums[idx]

        for i in range(len(nums)):
            sol[i] = leftarr[i] * rightarr[i]

        print(f"\nsol: {sol}\n")
        return sol


sol = Solution().productExceptSelf([2, 3, 4])
print(sol == [12, 8, 6])

sol = Solution().productExceptSelf([2, 3])
print(sol == [3, 2])

sol = Solution().productExceptSelf([1, 2, 3, 4])
print(sol == [24, 12, 8, 6])

sol = Solution().productExceptSelf([3, 2, 6, 2])
print(sol == [24, 36, 12, 36])

sol = Solution().productExceptSelf([1, 1, 1, 3])
print(sol == [3, 3, 3, 1])
