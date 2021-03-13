"""
 Given a list of daily temperatures T, return a list such that,
 for each day in the input, tells you how many days you would
 have to wait until a warmer temperature. If there is no future
 day for which this is possible, put 0 instead.

For example, given the list of temperatures:
T = [73, 74, 75, 71, 69, 72, 76, 73]
Output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100]. 
"""

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        print(f"\ninput: {T}\tof len {len(T)}")
        sol = [0] * len(T)
        pointer = []
        for i, t in enumerate(T):
            while pointer and T[pointer[-1]] < t:
                pv = pointer.pop(-1)
                sol[pv] = i - pv
            pointer.append(i)

        print("solution", sol)
        return sol


# sol = Solution().dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73])
# print(sol == [1, 1, 4, 2, 1, 1, 0, 0])

sol = Solution().dailyTemperatures(T=[55, 38, 53, 81, 61, 93, 97, 32, 43, 78])
print(sol == [3, 1, 1, 2, 1, 1, 0, 1, 1, 0])

# sol = Solution().dailyTemperatures(T=[77, 77, 77, 77, 77, 41, 77, 41, 41, 77])
# print(sol == [0, 0, 0, 0, 0, 1, 0, 2, 1, 0])
# print("expected", [0, 0, 0, 0, 0, 1, 0, 2, 1, 0])
