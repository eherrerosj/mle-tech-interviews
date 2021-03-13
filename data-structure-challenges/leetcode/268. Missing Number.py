"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space
complexity and O(n) runtime complexity?

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing
number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing
number in the range since it does not appear in nums.

Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

Learnings:
- Can be solved with manipulation: initialize an integer to nnn and XOR it with every index and value,
    we will be left with the missing number.
- It can also be solved with the Gauss Formula (expected_sum = len(nums)*(len(nums)+1)//2), then substract
    the actual sum
- The "obvious" solution would be:
    sol = 0
    for i in range(len(nums)):
        sol += (i+1-nums[i])
    return sol
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sol = 0
        for i in range(len(nums)):
            sol ^= i
            sol ^= nums[i]
        return sol ^ len(nums)


sol = Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1])
print(sol == 8)
