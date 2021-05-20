"""
We are given two arrays words1 and words2 of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.
For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from words1 is universal if for every b in words2, b is a subset of a.

Return a list of all universal words in words1.  You can return the words in any order.


Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

Follow up: Recursive solution is trivial, could you do it iteratively?


Learnings:
- Recursive approach DFS or BFS
"""

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        pass


sol = Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"])
print(sol == ["facebook", "google", "leetcode"])

sol = Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["l", "e"])
print(sol == ["apple", "google", "leetcode"])

sol = Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "oo"])
print(sol == ["facebook", "google"])
