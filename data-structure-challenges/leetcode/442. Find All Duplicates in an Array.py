"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Time complexity: O(n); Space complexity: O(n) due to hasmap. For O(1) space complexity:
            https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92390/Python-O(n)-time-O(1)-space
        """
        sol = []
        hm = {}
        for elm in nums:
            if hm.get(elm) and elm not in sol:
                sol.append(elm)
            else:
                hm[elm] = True
        return sol


sol = Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
print(sol == [2, 3])