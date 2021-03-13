"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

Learnings:
- Use a Hashmap to get unique values in array, then check for duplicates easily
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if hm.get(num):
                return True
            else:
                hm[num] = 1
        return False


sol = Solution().containsDuplicate([1, 2, 3, 1])
print(sol == True)


sol = Solution().containsDuplicate([1, 2, 3, 4])
print(sol == False)

sol = Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(sol == True)
