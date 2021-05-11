"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

Learnings:
- Typical fb
- Good job sorting first looking for nlogn complexity!
- Another very similar way of solving this problem is adding the interval to the solution and then
    modifying the end elem of that interval if there is overlap
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # sort array. O(n)
        intervals = sorted(intervals, key=lambda x: x[0])

        # init vars
        sol = []
        left, right = intervals[0]

        # iterate once with 2-pointer update
        print(f"Intervals: {intervals}")
        for interval in intervals[1:]:
            start, end = interval
            if start > right:
                sol.append([left, right])
                left = start
                right = end
            else:
                if end > right:
                    right = end
        sol.append([left, right])
        return sol


sol = Solution().merge([[1, 4], [4, 5]])
print(sol == [[1, 5]])

sol = Solution().merge([[1, 4], [5, 6]])
print(sol == [[1, 4], [5, 6]])

sol = Solution().merge([[1, 4], [2, 3]])
print(sol == [[1, 4]])

sol = Solution().merge([[3, 4], [1, 7]])
print(sol == [[1, 7]])

sol = Solution().merge([[1, 8], [10, 10]])
print(sol == [[1, 8], [10, 10]])
