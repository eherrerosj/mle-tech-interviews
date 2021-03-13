"""
A string S of lowercase English letters is given.
We want to partition this string into as many parts
as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        # edge case handling
        if len(S) == 1:
            return 1

        # populate hashmap
        hmap = {}
        for idx, letter in enumerate(S):
            if hmap.get(letter):
                hmap[letter][1] = idx + 1
            else:
                hmap[letter] = [idx, idx + 1]

        chunks = sorted(hmap.values(), key=lambda x: x[0])
        print(chunks)

        # calculate minimum partitions
        solution = []
        l, r = chunks[0]
        for chunk in chunks:
            if chunk[0] >= r:
                solution.append(chunk[0] - l)
                l, r = chunk
            elif chunk[1] > r:
                r = chunk[1]
        solution.append(r - l)

        print(f"Solution: {solution}")
        return solution


sol = Solution().partitionLabels(S="ababcbacadefegdehijhklij")
print(sol == [9, 7, 8])

sol = Solution().partitionLabels(S="abcabc")
print(sol == [6])

sol = Solution().partitionLabels(S="caedbdedda")
print(sol == [1, 9])
