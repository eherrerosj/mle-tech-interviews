"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.

Learnings:
- Facebook real Q solved in 20' but using handy py "sorted()"
- My hashmap counting object could have been a Counter (from collections) object
- Can be solved in O(k*log(k)) using heaps (worst case of O(log(k!)) is O(k*log(k))):
    Study implementation: https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l203
    Py: heapq.nlargest(k, count.keys(), key=count.get)
- Another possible approach is using Quickselect (Hoare's selection algorithm). typically used
    to solve the problems "find kth something". O(n) average time complexity (O(n2) worst case, rare).
    The approach is the same as for quicksort. One chooses a pivot and defines its position in
    a sorted array in a linear time using so-called partition algorithm
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(f"\nnums: {nums}")
        hmap = {}
        sol = []

        if len(nums) == 1:
            return nums

        # Create counting hashmap (O(n))
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1

        # Find keys of k largest values in hashmap (O(n))
        sol = [k for k, v in sorted(hmap.items(), key=lambda x: -x[1])[:k]]
        print(f"hmap: {hmap}  ->  Sol: {sol}")
        return sol


sol = Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
print(sol == [1, 2])


sol = Solution().topKFrequent(nums=[1], k=2)
print(sol == [1])

sol = Solution().topKFrequent(nums=[-1, -1], k=1)
print(sol == [-1])
