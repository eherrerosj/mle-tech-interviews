"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
    1 <= nums.length <= 3 * 104
    0 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 1

        if len(nums) == 1:
            return 0

        starting_index = nums[0]

        while starting_index < len(nums) - 1:
            sub_nums = nums[1 : 1 + starting_index]
            idx, _ = max(
                [(k + 1, k + sub_nums[k]) for k, v in enumerate(sub_nums)],
                key=lambda x: x[1],
            )
            nums = nums[idx:]
            starting_index = nums[0]
            min_jumps += 1
            # print(
            #     f"total jumps: {min_jumps}\nnew starting index: {idx} -> value {starting_index}"
            # )
        return min_jumps


# test1 = Solution().jump(nums=[2, 3, 1, 1, 4])
# print(f"Test 1 worked: {test1 == 2}\n")

# test2 = Solution().jump(nums=[2, 3, 0, 1, 4])
# print(f"Test 2 worked: {test2 == 2}\n")

# test3 = Solution().jump(nums=[1])
# print(f"Test 3 worked: {test3 == 0}\n")

# test4 = Solution().jump(nums=[1, 1, 3, 0, 4, 2, 1])
# print(f"Test 4 worked: {test4 == 4}\n")

# test5 = Solution().jump(nums=[1, 2])
# print(f"Test 5 worked: {test5 == 1}\n")

test6 = Solution().jump(nums=[4, 3, 2, 2, 1, 6, 1, 3, 1, 0, 8, 1])
print(f"Test 6 worked: {test6 == 3}\n")
